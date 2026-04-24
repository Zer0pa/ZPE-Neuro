from __future__ import annotations

from datetime import datetime, timezone
from dataclasses import dataclass
from pathlib import Path
from time import perf_counter
from typing import TYPE_CHECKING, Any

import numpy as np

from . import wave1 as wave1_module
from .wave1 import (
    ARTIFACT_ROOT,
    REPO_ROOT,
    WINDOW_SAMPLES,
    Recording,
    SpikeEvent,
    _nwb_roundtrip,
    _spikeinterface_e2e,
    append_command_log,
    build_templates,
    classify_window_template_shift_resilient,
    compression_ratio,
    decode_recording,
    encode_recording,
    rmse_uv,
    utc_now_iso,
    validate_recording_metadata,
    write_json,
)

if TYPE_CHECKING:
    from pynwb.ecephys import ElectricalSeries


@dataclass(frozen=True)
class PublicCorpusTarget:
    label: str
    tier: str
    dandiset_id: str
    asset_path: str
    role: str
    counted_in_breadth: bool
    alternate_asset_paths: tuple[str, ...] = ()


DEFAULT_WINDOW_POLICY = "scan"
DEFAULT_CANDIDATE_WINDOWS = 9
WINDOW_POLICY_CHOICES = ("first", "scan")
DEFAULT_BENCHMARK_REPETITIONS = 5


PUBLIC_CORPUS_TARGETS = [
    PublicCorpusTarget(
        label="dandi_000034_mouse412804_ecephys",
        tier="tier1_authority",
        dandiset_id="000034",
        asset_path="sub-mouse412804/sub-mouse412804_ecephys.nwb",
        role="tier1_authority_anchor",
        counted_in_breadth=False,
    ),
    PublicCorpusTarget(
        label="ajile12_sub01_ses7_ecephys",
        tier="tier2_breadth",
        dandiset_id="000055",
        asset_path="sub-01/sub-01_ses-7_behavior+ecephys.nwb",
        role="out_of_family_control",
        counted_in_breadth=False,
    ),
    PublicCorpusTarget(
        label="dandi_000003_yutamouse20_ecephys",
        tier="tier2_breadth",
        dandiset_id="000003",
        asset_path="sub-YutaMouse20/sub-YutaMouse20_ses-YutaMouse20-140327_behavior+ecephys.nwb",
        role="next_extracellular_target",
        counted_in_breadth=True,
        alternate_asset_paths=(
            "sub-YutaMouse20/sub-YutaMouse20_ses-YutaMouse20-140321_behavior+ecephys.nwb",
        ),
    ),
]


def get_public_corpus_target(*, label: str | None = None, dandiset_id: str | None = None) -> PublicCorpusTarget:
    for target in PUBLIC_CORPUS_TARGETS:
        if label is not None and target.label == label:
            return target
        if dandiset_id is not None and target.dandiset_id == dandiset_id:
            return target
    if label is not None:
        raise ValueError(f"UNKNOWN_PUBLIC_CORPUS_TARGET:{label}")
    raise ValueError(f"UNKNOWN_PUBLIC_CORPUS_DANDISET:{dandiset_id}")


def _target_asset_paths(target: PublicCorpusTarget) -> tuple[str, ...]:
    return (target.asset_path, *tuple(target.alternate_asset_paths))


def _series_selection_artifacts(
    *,
    series: ElectricalSeries,
    target: PublicCorpusTarget,
    sample_limit: int,
    channel_limit: int,
    window_policy: str,
    candidate_windows: int,
) -> tuple[Recording, dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
    series_shape = list(int(part) for part in series.data.shape)
    total_series_samples = int(series_shape[0] if series_shape[0] >= series_shape[1] else series_shape[1])
    if window_policy == "first":
        starts = [0]
    else:
        starts = _candidate_window_starts(
            total_samples=total_series_samples,
            sample_limit=sample_limit,
            candidate_windows=candidate_windows,
        )

    candidates: list[dict[str, Any]] = []
    candidate_artifacts: list[tuple[Recording, dict[str, Any], dict[str, Any]]] = []
    sampling_rate_hz = float(getattr(series, "rate", 0.0) or 0.0)
    for start_sample in starts:
        samples_uv_t_by_c = _extract_time_by_channel_slice(
            series=series,
            sample_limit=sample_limit,
            channel_limit=channel_limit,
            start_sample=start_sample,
        )
        recording, slice_meta = _recording_from_trace_slice(
            name=target.label,
            dataset_id=target.dandiset_id,
            asset_path=target.asset_path,
            sampling_rate_hz=sampling_rate_hz,
            samples_uv_t_by_c=samples_uv_t_by_c,
        )
        candidate = _window_candidate_payload(recording=recording, start_sample=start_sample)
        candidates.append(candidate)
        candidate_artifacts.append((recording, slice_meta, candidate))

    selected = _select_window_candidate(candidates)
    for recording, slice_meta, candidate in candidate_artifacts:
        if int(candidate["start_sample"]) != int(selected["start_sample"]):
            continue
        return recording, slice_meta, selected, candidates
    raise ValueError("SELECTED_WINDOW_RECORDING_NOT_FOUND")


def _find_downloaded_asset_path(download_root: Path, target: PublicCorpusTarget) -> Path:
    root = Path(download_root)
    for asset_path in _target_asset_paths(target):
        exact = root / asset_path
        if exact.exists():
            return exact

    matches = [
        path
        for path in root.rglob(Path(target.asset_path).name)
        if any(str(path.as_posix()).endswith(asset_path) for asset_path in _target_asset_paths(target))
    ]
    if not matches:
        raise FileNotFoundError(f"DOWNLOADED_ASSET_NOT_FOUND:{_target_asset_paths(target)}")
    matches.sort(key=lambda item: (len(item.parts), str(item)))
    return matches[0]


def _write_fixture_nwb(
    *,
    recording: Recording,
    fixture_path: Path,
    source_meta: dict[str, Any],
    selection_payload: dict[str, Any],
) -> dict[str, Any]:
    from pynwb import NWBFile, NWBHDF5IO
    from pynwb.ecephys import ElectricalSeries

    path = Path(fixture_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    nwbfile = NWBFile(
        session_description=(
            f"{source_meta['target_label']} extracted window for offline benchmark regression testing"
        ),
        identifier=f"{source_meta['target_label']}-{selection_payload['selected_start_sample']}",
        session_start_time=datetime.now(timezone.utc),
    )
    device = nwbfile.create_device("fixture_device")
    group = nwbfile.create_electrode_group(
        name="fixture_electrodes",
        description="Offline public corpus fixture electrodes",
        location="unknown",
        device=device,
    )
    for channel in range(recording.channels):
        nwbfile.add_electrode(
            id=int(channel),
            x=float(channel),
            y=0.0,
            z=0.0,
            imp=float("nan"),
            location="unknown",
            filtering="none",
            group=group,
        )
    electrodes = nwbfile.create_electrode_table_region(
        region=list(range(recording.channels)),
        description="All extracted fixture electrodes",
    )
    series = ElectricalSeries(
        name="ElectricalSeries",
        data=recording.samples.T.astype(np.int16),
        electrodes=electrodes,
        rate=float(recording.sampling_rate_hz),
        conversion=1.0,
        description=(
            f"Selected start sample {selection_payload['selected_start_sample']} from "
            f"{source_meta['dandiset_id']}::{source_meta['asset_path']}"
        ),
    )
    nwbfile.add_acquisition(series)

    with NWBHDF5IO(path, "w") as io:
        io.write(nwbfile)

    return {
        "fixture_path": str(path),
        "fixture_size_bytes": path.stat().st_size,
        "selected_start_sample": int(selection_payload["selected_start_sample"]),
        "channels": int(recording.channels),
        "total_samples": int(recording.samples.shape[1]),
    }


def _first_electrical_series(nwbfile: Any) -> tuple[str, ElectricalSeries]:
    from pynwb.ecephys import ElectricalSeries

    for key, value in nwbfile.acquisition.items():
        if isinstance(value, ElectricalSeries):
            return key, value
    raise ValueError("NO_ELECTRICAL_SERIES_FOUND")


def _series_scale_to_uv(series: ElectricalSeries) -> float:
    unit = str(getattr(series, "unit", "") or "").strip().lower()
    scale = float(getattr(series, "conversion", 1.0) or 1.0)
    if unit in {"v", "volt", "volts"}:
        scale *= 1_000_000.0
    return scale


def _extract_time_by_channel_slice(
    series: ElectricalSeries,
    sample_limit: int,
    channel_limit: int,
    start_sample: int = 0,
) -> np.ndarray:
    shape = tuple(int(part) for part in series.data.shape)
    if len(shape) != 2:
        raise ValueError(f"UNSUPPORTED_SERIES_RANK:{shape}")

    electrode_count = None
    if getattr(series, "electrodes", None) is not None:
        try:
            electrode_count = len(series.electrodes.data)
        except Exception:
            electrode_count = None

    time_axis = 0
    if electrode_count is not None:
        if shape[1] == electrode_count:
            time_axis = 0
        elif shape[0] == electrode_count:
            time_axis = 1
    elif shape[0] <= channel_limit and shape[1] > shape[0]:
        time_axis = 1

    total_samples = int(shape[0] if time_axis == 0 else shape[1])
    max_start = max(0, total_samples - sample_limit)
    start = min(max(int(start_sample), 0), max_start)
    stop = min(total_samples, start + sample_limit)

    if time_axis == 0:
        raw = np.asarray(series.data[start:stop, :channel_limit], dtype=np.float32)
    else:
        raw = np.asarray(series.data[:channel_limit, start:stop], dtype=np.float32).T

    scale_to_uv = _series_scale_to_uv(series)
    offset_uv = float(getattr(series, "offset", 0.0) or 0.0)
    if scale_to_uv != 1.0 or offset_uv != 0.0:
        raw = raw * np.float32(scale_to_uv) + np.float32(offset_uv)
    return raw


def _candidate_window_starts(
    total_samples: int,
    sample_limit: int,
    candidate_windows: int,
) -> list[int]:
    max_start = max(0, int(total_samples) - int(sample_limit))
    if max_start == 0 or candidate_windows <= 1:
        return [0]

    raw = np.linspace(0, max_start, num=max(2, int(candidate_windows)), dtype=np.float64)
    starts = sorted({int(round(value)) for value in raw.tolist()})
    if starts[0] != 0:
        starts.insert(0, 0)
    if starts[-1] != max_start:
        starts.append(max_start)
    return starts


def _center_clip_to_int16(samples_uv_t_by_c: np.ndarray) -> tuple[np.ndarray, float]:
    centered = samples_uv_t_by_c - np.median(samples_uv_t_by_c, axis=0, keepdims=True)
    centered = np.nan_to_num(centered, nan=0.0, posinf=32_767.0, neginf=-32_768.0)
    abs_max = float(np.max(np.abs(centered))) if centered.size else 0.0
    normalization = 1.0
    if abs_max > 32_000.0:
        normalization = 32_000.0 / abs_max
        centered = centered * normalization
    clipped = np.clip(np.rint(centered), -32768, 32767).astype(np.int16)
    return clipped, normalization


def _extract_template_events(
    samples_ch_by_t: np.ndarray,
    templates: np.ndarray,
) -> list[dict[str, int]]:
    peak_offset = int(np.median(np.argmin(templates, axis=1)))
    refractory = WINDOW_SAMPLES + 2
    events: list[dict[str, int]] = []
    total_samples = int(samples_ch_by_t.shape[1])
    end_idx = total_samples - (WINDOW_SAMPLES - peak_offset) - 1

    for channel in range(samples_ch_by_t.shape[0]):
        trace = samples_ch_by_t[channel].astype(np.float32, copy=False)
        sigma = float(np.std(trace))
        threshold = -4.0 * max(1.0, sigma)
        idx = max(peak_offset, 1)
        while idx < end_idx:
            value = float(trace[idx])
            if value > threshold:
                idx += 1
                continue
            if value > float(trace[idx - 1]) or value >= float(trace[idx + 1]):
                idx += 1
                continue
            start = idx - peak_offset
            window = trace[start : start + WINDOW_SAMPLES]
            if window.shape[0] != WINDOW_SAMPLES:
                idx += 1
                continue
            template_id = classify_window_template_shift_resilient(window, templates)
            amplitude_uv = int(np.clip(np.max(np.abs(window)), 1.0, 255.0))
            events.append(
                {
                    "channel": channel,
                    "start": start,
                    "template_id": template_id,
                    "amplitude_uv": amplitude_uv,
                }
            )
            idx = start + refractory
    return events


def _recording_from_trace_slice(
    name: str,
    dataset_id: str,
    asset_path: str,
    sampling_rate_hz: float,
    samples_uv_t_by_c: np.ndarray,
) -> tuple[Recording, dict[str, Any]]:
    templates = build_templates()
    pcm_t_by_c, normalization = _center_clip_to_int16(samples_uv_t_by_c)
    pcm_ch_by_t = pcm_t_by_c.T.copy()
    events_raw = _extract_template_events(pcm_ch_by_t, templates)
    recording = Recording(
        name=name,
        profile=f"public-{dataset_id}",
        seed=0,
        sampling_rate_hz=int(round(float(sampling_rate_hz))),
        channels=int(pcm_ch_by_t.shape[0]),
        duration_s=float(pcm_ch_by_t.shape[1]) / float(sampling_rate_hz),
        samples=pcm_ch_by_t,
        templates=templates,
        events=[
            SpikeEvent(
                channel=int(item["channel"]),
                start=int(item["start"]),
                template_id=int(item["template_id"]),
                amplitude_uv=int(item["amplitude_uv"]),
            )
            for item in events_raw
        ],
        metadata={
            "source_dataset_id": dataset_id,
            "source_asset_path": asset_path,
            "normalization_scale": normalization,
            "event_count": len(events_raw),
        },
    )
    validate_recording_metadata(recording)
    return recording, {
        "channels": recording.channels,
        "total_samples": int(recording.samples.shape[1]),
        "duration_s": recording.duration_s,
        "normalization_scale": normalization,
        "event_count": len(events_raw),
    }


def _window_candidate_payload(
    recording: Recording,
    start_sample: int,
) -> dict[str, Any]:
    samples = recording.samples.astype(np.float32, copy=False)
    channel_std = np.std(samples, axis=1)
    p95_abs_uv = float(np.percentile(np.abs(samples), 95.0))
    max_abs_uv = float(np.max(np.abs(samples))) if samples.size else 0.0
    active_channels = len({int(event.channel) for event in recording.events})
    rank_key = [
        int(len(recording.events)),
        int(active_channels),
        int(round(p95_abs_uv)),
        int(round(max_abs_uv)),
        -int(start_sample),
    ]
    return {
        "start_sample": int(start_sample),
        "event_count": int(len(recording.events)),
        "active_channels": int(active_channels),
        "mean_channel_std_uv": float(np.mean(channel_std)),
        "p95_abs_uv": p95_abs_uv,
        "max_abs_uv": max_abs_uv,
        "duration_s": float(recording.duration_s),
        "rank_key": rank_key,
    }


def _candidate_rank_key(candidate: dict[str, Any]) -> tuple[int, int, int, int, int]:
    raw = candidate.get("rank_key", [0, 0, 0, 0, 0])
    padded = list(raw)[:5]
    while len(padded) < 5:
        padded.append(0)
    return tuple(int(value) for value in padded)


def _select_window_candidate(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    if not candidates:
        raise ValueError("NO_WINDOW_CANDIDATES")

    ranked = sorted(candidates, key=_candidate_rank_key, reverse=True)
    selected = dict(ranked[0])
    selected["rank"] = 1
    return selected


def _selection_reason(selected: dict[str, Any]) -> str:
    return (
        "Selected the highest-ranked candidate using "
        "event_count -> active_channels -> p95_abs_uv -> max_abs_uv -> earlier_start."
    )


def _selection_summary(
    target: PublicCorpusTarget,
    window_policy: str,
    candidate_windows: int,
    source_meta: dict[str, Any],
    candidates: list[dict[str, Any]],
    selected: dict[str, Any],
) -> dict[str, Any]:
    ranked = sorted(candidates, key=_candidate_rank_key, reverse=True)
    ranked_payload: list[dict[str, Any]] = []
    first_window_rank = None
    for rank, candidate in enumerate(ranked, start=1):
        item = dict(candidate)
        item["rank"] = rank
        if item["start_sample"] == 0 and first_window_rank is None:
            first_window_rank = rank
        ranked_payload.append(item)

    return {
        "schema_version": "window-policy-2026-03-20",
        "generated_at_utc": utc_now_iso(),
        "target_label": target.label,
        "tier": target.tier,
        "window_policy": window_policy,
        "candidate_windows_requested": int(candidate_windows),
        "candidate_windows_evaluated": len(ranked_payload),
        "selection_reason": _selection_reason(selected),
        "selected_start_sample": int(selected["start_sample"]),
        "selected_rank_key": list(_candidate_rank_key(selected)),
        "first_window_rank": first_window_rank,
        "all_candidates_quiet": all(int(item["event_count"]) == 0 for item in ranked_payload),
        "source": {
            "dandiset_id": source_meta["dandiset_id"],
            "asset_path": source_meta["asset_path"],
            "series_shape": source_meta["series_shape"],
            "sampling_rate_hz": source_meta["sampling_rate_hz"],
            "sample_limit": source_meta["total_samples"],
            "channel_limit": source_meta["channels"],
        },
        "candidates": ranked_payload,
    }


def _selection_rank_tuple(selection_payload: dict[str, Any]) -> tuple[int, int, int, int, int]:
    return tuple(int(value) for value in selection_payload.get("selected_rank_key", [0, 0, 0, 0, 0]))


def _stream_target_recording_for_asset_path(
    target: PublicCorpusTarget,
    asset_path: str,
    sample_limit: int,
    channel_limit: int,
    window_policy: str,
    candidate_windows: int,
) -> tuple[Recording, dict[str, Any], dict[str, Any]]:
    import h5py
    import remfile
    from dandi.dandiapi import DandiAPIClient
    from pynwb import NWBHDF5IO

    with DandiAPIClient.for_dandi_instance("dandi") as client:
        dandiset = client.get_dandiset(target.dandiset_id, "draft")
        dataset_name = str(dandiset.get_raw_metadata().get("name", ""))
        asset = dandiset.get_asset_by_path(asset_path)
        asset_meta = asset.get_raw_metadata()
        content_url = asset.get_content_url()

    remote_file = remfile.File(content_url)
    h5_file = h5py.File(remote_file, "r")
    try:
        io = NWBHDF5IO(file=h5_file, load_namespaces=True)
        try:
            nwbfile = io.read()
            series_name, series = _first_electrical_series(nwbfile)
            series_shape = list(int(part) for part in series.data.shape)
            selected_recording, selected_slice_meta, selected, candidates = _series_selection_artifacts(
                series=series,
                target=target,
                sample_limit=sample_limit,
                channel_limit=channel_limit,
                window_policy=window_policy,
                candidate_windows=candidate_windows,
            )
        finally:
            io.close()
    finally:
        h5_file.close()

    source_meta = {
        "target_label": target.label,
        "tier": target.tier,
        "role": target.role,
        "counted_in_breadth": bool(target.counted_in_breadth),
        "dandiset_id": target.dandiset_id,
        "dataset_name": dataset_name,
        "asset_path": asset_path,
        "content_size_bytes": asset_meta.get("contentSize"),
        "content_url": content_url,
        "series_name": series_name,
        "series_shape": series_shape,
        "sampling_rate_hz": selected_recording.sampling_rate_hz,
        "selected_start_sample": int(selected["start_sample"]),
        "window_policy": window_policy,
        **selected_slice_meta,
    }
    selection_payload = _selection_summary(
        target=target,
        window_policy=window_policy,
        candidate_windows=candidate_windows,
        source_meta=source_meta,
        candidates=candidates,
        selected=selected,
    )
    return selected_recording, source_meta, selection_payload


def _load_local_target_recording(
    *,
    target: PublicCorpusTarget,
    download_root: Path,
    sample_limit: int,
    channel_limit: int,
    window_policy: str,
    candidate_windows: int,
) -> tuple[Recording, dict[str, Any], dict[str, Any]]:
    from pynwb import NWBHDF5IO

    asset_path = _find_downloaded_asset_path(download_root, target)
    with NWBHDF5IO(asset_path, "r", load_namespaces=True) as io:
        nwbfile = io.read()
        series_name, series = _first_electrical_series(nwbfile)
        series_shape = list(int(part) for part in series.data.shape)
        selected_recording, selected_slice_meta, selected, candidates = _series_selection_artifacts(
            series=series,
            target=target,
            sample_limit=sample_limit,
            channel_limit=channel_limit,
            window_policy=window_policy,
            candidate_windows=candidate_windows,
        )

    source_meta = {
        "target_label": target.label,
        "tier": target.tier,
        "role": target.role,
        "counted_in_breadth": bool(target.counted_in_breadth),
        "dandiset_id": target.dandiset_id,
        "dataset_name": asset_path.parent.name,
        "asset_path": str(asset_path.relative_to(download_root)).replace("\\", "/"),
        "download_root": str(download_root),
        "local_asset_path": str(asset_path),
        "series_name": series_name,
        "series_shape": series_shape,
        "sampling_rate_hz": selected_recording.sampling_rate_hz,
        "selected_start_sample": int(selected["start_sample"]),
        "window_policy": window_policy,
        **selected_slice_meta,
    }
    selection_payload = _selection_summary(
        target=target,
        window_policy=window_policy,
        candidate_windows=candidate_windows,
        source_meta=source_meta,
        candidates=candidates,
        selected=selected,
    )
    return selected_recording, source_meta, selection_payload


def _stream_target_recording(
    target: PublicCorpusTarget,
    sample_limit: int,
    channel_limit: int,
    window_policy: str,
    candidate_windows: int,
) -> tuple[Recording, dict[str, Any], dict[str, Any]]:
    best_payload: tuple[Recording, dict[str, Any], dict[str, Any]] | None = None
    errors: list[str] = []
    for asset_path in _target_asset_paths(target):
        try:
            candidate_payload = _stream_target_recording_for_asset_path(
                target=target,
                asset_path=asset_path,
                sample_limit=sample_limit,
                channel_limit=channel_limit,
                window_policy=window_policy,
                candidate_windows=candidate_windows,
            )
        except Exception as exc:
            errors.append(f"{asset_path}:{exc}")
            continue
        if best_payload is None:
            best_payload = candidate_payload
            continue
        _, _, best_selection = best_payload
        _, _, candidate_selection = candidate_payload
        if _selection_rank_tuple(candidate_selection) > _selection_rank_tuple(best_selection):
            best_payload = candidate_payload
    if best_payload is not None:
        return best_payload
    raise RuntimeError(f"PUBLIC_CORPUS_STREAM_TARGET_FAIL:{target.label}:{errors}")


def _run_single_target_eval(
    *,
    target: PublicCorpusTarget,
    sample_limit: int,
    channel_limit: int,
    window_policy: str,
    candidate_windows: int,
) -> tuple[dict[str, Any], dict[str, Any]]:
    artifact_name = f"public_corpus_eval_{target.label}.json"
    selection_artifact_name = f"public_corpus_window_selection_{target.label}.json"
    try:
        recording, source_meta, selection_payload = _stream_target_recording(
            target=target,
            sample_limit=sample_limit,
            channel_limit=channel_limit,
            window_policy=window_policy,
            candidate_windows=candidate_windows,
        )
        codec_metrics = _evaluate_recording(recording)
        target_artifact_root, nwb_roundtrip, spikeinterface = _run_target_insertion_evals(
            recording=recording,
            target_label=target.label,
        )
        failure_reasons: list[str] = []
        if codec_metrics["event_count"] <= 0:
            failure_reasons.append("NO_CODEC_EVENTS_DETECTED")
        if nwb_roundtrip["status"] != "PASS":
            failure_reasons.append(f"NWB_ROUNDTRIP_{nwb_roundtrip['status']}")
        if spikeinterface["status"] != "PASS":
            failure_reasons.append(f"SPIKEINTERFACE_{spikeinterface['status']}")
        target_status = "PASS" if not failure_reasons else "FAIL"
        write_json(ARTIFACT_ROOT / selection_artifact_name, selection_payload)
        selection_artifact = {
            "target_label": target.label,
            "artifact": selection_artifact_name,
            "selected_start_sample": int(selection_payload["selected_start_sample"]),
            "first_window_rank": selection_payload["first_window_rank"],
            "all_candidates_quiet": selection_payload["all_candidates_quiet"],
        }
        payload = {
            "schema_version": "wave1-2026-03-20",
            "generated_at_utc": utc_now_iso(),
            "status": target_status,
            "source": source_meta,
            "window_selection": {
                "artifact": selection_artifact_name,
                "selected_start_sample": int(selection_payload["selected_start_sample"]),
                "first_window_rank": selection_payload["first_window_rank"],
                "all_candidates_quiet": selection_payload["all_candidates_quiet"],
            },
            "codec_metrics": codec_metrics,
            "nwb_roundtrip": nwb_roundtrip,
            "spikeinterface": spikeinterface,
            "artifacts_root": target_artifact_root,
            "failure_reasons": failure_reasons,
        }
    except Exception as exc:
        selection_artifact = {
            "target_label": target.label,
            "artifact": selection_artifact_name,
            "selected_start_sample": None,
            "first_window_rank": None,
            "all_candidates_quiet": None,
        }
        payload = {
            "schema_version": "wave1-2026-03-20",
            "generated_at_utc": utc_now_iso(),
            "status": "FAIL",
            "source": {
                "target_label": target.label,
                "tier": target.tier,
                "role": target.role,
                "counted_in_breadth": bool(target.counted_in_breadth),
                "dandiset_id": target.dandiset_id,
                "asset_path": target.asset_path,
                "alternate_asset_paths": list(target.alternate_asset_paths),
            },
            "error": f"PUBLIC_CORPUS_EVAL_FAIL:{exc}",
        }
    write_json(ARTIFACT_ROOT / artifact_name, payload)
    return payload, selection_artifact


def _evaluate_recording(recording: Recording) -> dict[str, Any]:
    packet = encode_recording(recording)
    decoded = decode_recording(packet, recording.templates)
    raw_bits = int(recording.samples.size * 16)
    return {
        "event_count": len(recording.events),
        "raw_bits": raw_bits,
        "encoded_bits": int(packet["encoded_bits"]),
        "compression_ratio": compression_ratio(raw_bits, int(packet["encoded_bits"])),
        "rmse_uv": rmse_uv(recording.samples, decoded),
        "dropped_overlap_events": int(packet["dropped_overlap_events"]),
    }


def _timed_codec_metrics(
    recording: Recording,
    repetitions: int = DEFAULT_BENCHMARK_REPETITIONS,
) -> dict[str, Any]:
    packets: list[dict[str, Any]] = []
    encode_timings_ms: list[float] = []
    for _ in range(max(1, repetitions)):
        start = perf_counter()
        packet = encode_recording(recording)
        encode_timings_ms.append((perf_counter() - start) * 1000.0)
        packets.append(packet)

    packet = packets[-1]
    decode_timings_ms: list[float] = []
    decoded = recording.samples
    for _ in range(max(1, repetitions)):
        start = perf_counter()
        decoded = decode_recording(packet, recording.templates)
        decode_timings_ms.append((perf_counter() - start) * 1000.0)

    error = recording.samples.astype(np.float64) - decoded.astype(np.float64)
    signal_rms = float(np.sqrt(np.mean(np.square(recording.samples.astype(np.float64)))))
    noise_rms = float(np.sqrt(np.mean(np.square(error))))
    snr_db = float("inf") if noise_rms == 0.0 else float(20.0 * np.log10(signal_rms / noise_rms))
    exact_match_ratio = float(np.mean(recording.samples == decoded))

    return {
        "event_count": int(len(recording.events)),
        "raw_bits": int(recording.samples.size * 16),
        "encoded_bits": int(packet["encoded_bits"]),
        "compression_ratio": compression_ratio(int(recording.samples.size * 16), int(packet["encoded_bits"])),
        "rmse_uv": rmse_uv(recording.samples, decoded),
        "snr_db": snr_db,
        "roundtrip_exact": bool(np.array_equal(recording.samples, decoded)),
        "roundtrip_fidelity": exact_match_ratio,
        "encode_latency_ms": {
            "mean": float(np.mean(encode_timings_ms)),
            "min": float(np.min(encode_timings_ms)),
            "max": float(np.max(encode_timings_ms)),
            "runs": len(encode_timings_ms),
        },
        "decode_latency_ms": {
            "mean": float(np.mean(decode_timings_ms)),
            "min": float(np.min(decode_timings_ms)),
            "max": float(np.max(decode_timings_ms)),
            "runs": len(decode_timings_ms),
        },
        "dropped_overlap_events": int(packet["dropped_overlap_events"]),
    }


class PublicCorpusRunner:
    def __init__(
        self,
        *,
        dandiset_id: str,
        label: str | None = None,
        data_root: str | None = None,
        artifact_root: str | None = None,
        sample_limit: int = 6000,
        channel_limit: int = 8,
        window_policy: str = DEFAULT_WINDOW_POLICY,
        candidate_windows: int = DEFAULT_CANDIDATE_WINDOWS,
        benchmark_repetitions: int = DEFAULT_BENCHMARK_REPETITIONS,
    ) -> None:
        self.target = get_public_corpus_target(label=label, dandiset_id=dandiset_id)
        self.data_root = None if data_root is None else Path(data_root)
        self.artifact_root = None if artifact_root is None else Path(artifact_root)
        self.sample_limit = int(sample_limit)
        self.channel_limit = int(channel_limit)
        self.window_policy = window_policy
        self.candidate_windows = int(candidate_windows)
        self.benchmark_repetitions = int(benchmark_repetitions)

    def _load_recording(self) -> tuple[Recording, dict[str, Any], dict[str, Any]]:
        if self.data_root is not None:
            return _load_local_target_recording(
                target=self.target,
                download_root=self.data_root,
                sample_limit=self.sample_limit,
                channel_limit=self.channel_limit,
                window_policy=self.window_policy,
                candidate_windows=self.candidate_windows,
            )
        return _stream_target_recording(
            target=self.target,
            sample_limit=self.sample_limit,
            channel_limit=self.channel_limit,
            window_policy=self.window_policy,
            candidate_windows=self.candidate_windows,
        )

    def run_benchmark(self, *, fixture_output: str | None = None) -> dict[str, Any]:
        recording, source_meta, selection_payload = self._load_recording()
        codec_metrics = _timed_codec_metrics(
            recording=recording,
            repetitions=self.benchmark_repetitions,
        )
        payload = {
            "schema_version": "wave1-benchmark-2026-04-06",
            "generated_at_utc": utc_now_iso(),
            "target_label": self.target.label,
            "dandiset_id": self.target.dandiset_id,
            "source": source_meta,
            "window_selection": selection_payload,
            "codec_metrics": codec_metrics,
        }
        fixture_manifest = None
        if fixture_output is not None:
            fixture_manifest = _write_fixture_nwb(
                recording=recording,
                fixture_path=Path(fixture_output),
                source_meta=source_meta,
                selection_payload=selection_payload,
            )
            payload["fixture"] = fixture_manifest

        if self.artifact_root is not None:
            self.artifact_root.mkdir(parents=True, exist_ok=True)
            write_json(self.artifact_root / "benchmark_summary.json", payload)
            write_json(self.artifact_root / "selection_summary.json", selection_payload)
            write_json(self.artifact_root / "source_summary.json", source_meta)
            if fixture_manifest is not None:
                write_json(self.artifact_root / "fixture_manifest.json", fixture_manifest)
        return payload


def _run_target_insertion_evals(
    recording: Recording,
    target_label: str,
) -> tuple[str, dict[str, Any], dict[str, Any]]:
    previous_root = wave1_module.ARTIFACT_ROOT
    target_root = ARTIFACT_ROOT / target_label
    target_root.mkdir(parents=True, exist_ok=True)
    wave1_module.ARTIFACT_ROOT = target_root
    try:
        nwb_roundtrip = _nwb_roundtrip(recording)
        spikeinterface = _spikeinterface_e2e(recording)
    finally:
        wave1_module.ARTIFACT_ROOT = previous_root
    target_root_rel = (
        str(target_root.relative_to(REPO_ROOT))
        if target_root.is_relative_to(REPO_ROOT)
        else str(target_root)
    )
    return target_root_rel, nwb_roundtrip, spikeinterface


def _probe_ibl_public_metadata() -> dict[str, Any]:
    try:
        from one.api import ONE
    except ModuleNotFoundError:
        return {
            "status": "SKIPPED",
            "waveform_slice_executed": False,
            "blocked_reason": (
                "ONE-api is not part of the clean packaged public replay surface. "
                "Provision it manually only when you are explicitly working the repo-local IBL metadata path."
            ),
        }

    one = ONE(
        base_url="https://openalyx.internationalbrainlab.org",
        username="intbrainlab",
        password="international",
        silent=True,
    )
    session = one.alyx.rest("sessions", "list", limit=1)[0]
    datasets = one.alyx.rest("datasets", "list", session=session["id"], limit=25)
    dataset_summaries = [
        {
            "name": item.get("name"),
            "dataset_type": item.get("dataset_type"),
            "file_size": item.get("file_size"),
        }
        for item in datasets
    ]
    return {
        "status": "PASS",
        "session_id": session["id"],
        "subject": session.get("subject"),
        "start_time": session.get("start_time"),
        "dataset_count_returned": len(dataset_summaries),
        "datasets": dataset_summaries,
        "waveform_slice_executed": False,
        "blocked_reason": (
            "Public Alyx metadata access succeeds locally, but waveform-level slice execution was not "
            "reduced to an M1-friendly path within this run."
        ),
    }


def run_public_corpus_eval(
    sample_limit: int = 6000,
    channel_limit: int = 8,
    window_policy: str = DEFAULT_WINDOW_POLICY,
    candidate_windows: int = DEFAULT_CANDIDATE_WINDOWS,
    label: str | None = None,
    dandiset_id: str | None = None,
) -> dict[str, Any]:
    if window_policy not in WINDOW_POLICY_CHOICES:
        raise ValueError(f"UNSUPPORTED_WINDOW_POLICY:{window_policy}")

    append_command_log(
        "python3.11 tools/run_public_corpus_eval.py "
        f"--sample-limit {sample_limit} --channel-limit {channel_limit} "
        f"--window-policy {window_policy} --candidate-windows {candidate_windows}"
        + (f" --label {label}" if label is not None else "")
        + (f" --dandiset {dandiset_id}" if dandiset_id is not None else "")
    )

    target_results: list[dict[str, Any]] = []
    selection_artifacts: list[dict[str, Any]] = []
    selected_targets = (
        [get_public_corpus_target(label=label, dandiset_id=dandiset_id)]
        if label is not None or dandiset_id is not None
        else list(PUBLIC_CORPUS_TARGETS)
    )
    for target in selected_targets:
        payload, selection_artifact = _run_single_target_eval(
            target=target,
            sample_limit=sample_limit,
            channel_limit=channel_limit,
            window_policy=window_policy,
            candidate_windows=candidate_windows,
        )
        selection_artifacts.append(selection_artifact)
        target_results.append(
            {
                "target_label": target.label,
                "tier": target.tier,
                "role": target.role,
                "counted_in_breadth": bool(target.counted_in_breadth),
                "status": payload["status"],
                "artifact": f"public_corpus_eval_{target.label}.json",
                "selection_artifact": f"public_corpus_window_selection_{target.label}.json",
            }
        )

    try:
        ibl_probe = _probe_ibl_public_metadata()
    except Exception as exc:
        ibl_probe = {
            "status": "FAIL",
            "error": f"IBL_PUBLIC_PROBE_FAIL:{exc}",
            "waveform_slice_executed": False,
        }
    write_json(ARTIFACT_ROOT / "public_corpus_ibl_probe.json", ibl_probe)

    summary = {
        "schema_version": "wave1-2026-03-20",
        "generated_at_utc": utc_now_iso(),
        "status": "PASS" if all(item["status"] == "PASS" for item in target_results) else "FAIL",
        "sample_limit": sample_limit,
        "channel_limit": channel_limit,
        "window_policy": window_policy,
        "candidate_windows": int(candidate_windows),
        "window_selection_artifact": "public_corpus_window_selection_summary.json",
        "window_selection_targets": selection_artifacts,
        "targets": target_results,
        "ibl_probe_status": ibl_probe["status"],
        "ibl_probe_artifact": "public_corpus_ibl_probe.json",
    }
    write_json(
        ARTIFACT_ROOT / "public_corpus_window_selection_summary.json",
        {
            "schema_version": "window-policy-2026-03-20",
            "generated_at_utc": utc_now_iso(),
            "window_policy": window_policy,
            "candidate_windows": int(candidate_windows),
            "sample_limit": sample_limit,
            "channel_limit": channel_limit,
            "targets": selection_artifacts,
        },
    )
    write_json(ARTIFACT_ROOT / "public_corpus_summary.json", summary)
    return summary
