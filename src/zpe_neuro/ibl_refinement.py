from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import numpy as np

from .ibl_public import (
    DEFAULT_IBL_TARGET,
    IblPublicTarget,
    load_ibl_public_chunk_manifest,
    load_ibl_public_recording,
    load_ibl_public_trace_slice,
)
from .public_corpus import (
    _candidate_rank_key,
    _evaluate_recording,
    _recording_from_trace_slice,
    _run_target_insertion_evals,
    _window_candidate_payload,
)
from .wave1 import ARTIFACT_ROOT, append_command_log, utc_now_iso, write_json
from .wave1 import _spikeinterface_peak_probe


_CHUNK_FILE_RE = re.compile(r"^chunk(\d{4})_")


def _chunk_index_grid(chunk_count: int, search_chunk_count: int) -> list[int]:
    if chunk_count <= 0:
        return [0]
    raw = np.linspace(0, max(0, chunk_count - 1), num=max(2, int(search_chunk_count)), dtype=np.float64)
    return sorted({int(round(value)) for value in raw.tolist()})


def _channel_start_grid(total_channels: int, channel_limit: int, step: int) -> list[int]:
    max_start = max(0, int(total_channels) - int(channel_limit))
    starts = list(range(0, max_start + 1, max(1, int(step))))
    if not starts:
        starts = [0]
    if starts[-1] != max_start:
        starts.append(max_start)
    return sorted(set(starts))


def _window_start_grid(total_samples: int, window_samples: int, windows_per_chunk: int) -> list[int]:
    max_start = max(0, int(total_samples) - int(window_samples))
    if max_start == 0 or windows_per_chunk <= 1:
        return [0]
    raw = np.linspace(0, max_start, num=max(2, int(windows_per_chunk)), dtype=np.float64)
    starts = sorted({int(round(value)) for value in raw.tolist()})
    if starts[0] != 0:
        starts.insert(0, 0)
    if starts[-1] != max_start:
        starts.append(max_start)
    return starts


def _coarse_rank_key(candidate: dict[str, Any]) -> tuple[int, int, int, int, int, int, int, int]:
    return (
        *_candidate_rank_key(candidate),
        -int(candidate["chunk_index"]),
        -int(candidate["channel_start"]),
        -int(candidate["window_start"]),
    )


def _peak_probe_rank_key(candidate: dict[str, Any]) -> tuple[int, int, int, int, int, int, int, int, int]:
    peak_count = int(candidate.get("peak_count") or 0)
    return (
        peak_count,
        *_candidate_rank_key(candidate),
        -int(candidate["chunk_index"]),
        -int(candidate["channel_start"]),
        -int(candidate["window_start"]),
        -int(candidate.get("coarse_rank", 0)),
    )


def _full_eval_rank_key(candidate: dict[str, Any]) -> tuple[int, int, int, int, int, int, int, int, int, int]:
    evaluation_status = 1 if candidate["evaluation_status"] == "PASS" else 0
    peak_count = int(candidate.get("peak_count") or 0)
    sorter_pass = 1 if candidate["spikeinterface"]["sorter_probe_status"] == "PASS" else 0
    return (
        evaluation_status,
        sorter_pass,
        peak_count,
        *_candidate_rank_key(candidate),
        -int(candidate["chunk_index"]),
        -int(candidate["channel_start"]),
        -int(candidate["window_start"]),
        -int(candidate.get("coarse_rank", 0)),
    )


def _candidate_recording(
    candidate: dict[str, Any],
    sample_limit: int,
    channel_limit: int,
    target: IblPublicTarget,
) -> tuple[Any, dict[str, Any]]:
    return load_ibl_public_recording(
        sample_limit=sample_limit,
        channel_limit=channel_limit,
        chunk_index=int(candidate["chunk_index"]),
        channel_start=int(candidate["channel_start"]),
        start_sample=int(candidate["window_start"]),
        target=target,
    )


def _summarize_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    payload = dict(candidate)
    payload["rank_key"] = list(_candidate_rank_key(candidate))
    if "peak_probe" in payload:
        payload["peak_probe"] = {
            key: value
            for key, value in payload["peak_probe"].items()
            if key != "band"
        }
    if "spikeinterface" in payload:
        payload["spikeinterface"] = dict(payload["spikeinterface"])
    return payload


def _cleanup_remote_probe_cache(cache_root: Path, keep_chunk_indices: set[int]) -> dict[str, Any]:
    removed_files: list[str] = []
    freed_bytes = 0
    if not cache_root.exists():
        return {"removed_files": removed_files, "freed_bytes": freed_bytes}

    for path in sorted(cache_root.iterdir()):
        match = _CHUNK_FILE_RE.match(path.name)
        if match is None:
            continue
        chunk_index = int(match.group(1))
        if chunk_index in keep_chunk_indices:
            continue
        if not path.is_file():
            continue
        freed_bytes += int(path.stat().st_size)
        removed_files.append(path.name)
        path.unlink()
    return {
        "removed_files": removed_files,
        "freed_bytes": freed_bytes,
    }


def _decision_note(
    best_candidate: dict[str, Any],
    final_verdict: str,
    artifact_name: str,
) -> str:
    if final_verdict == "PASS":
        heading = "Bounded IBL refinement found a real second extracellular breadth pass."
        next_step = (
            "Rerun breadth adjudication and update lane state surfaces without weakening the remaining "
            "blind-clone, Allen, or release-boundary gates."
        )
    else:
        heading = "Bounded IBL refinement did not close the second extracellular breadth target."
        next_step = (
            "Treat the failure as stronger falsification of the current Lane 1 breadth route. "
            "Do not narrate `AM-NEU-01` closed from the DANDI anchor alone."
        )

    return "\n".join(
        [
            "# IBL Refinement Decision",
            "",
            heading,
            "",
            "## Best Candidate",
            f"- chunk index: `{best_candidate['chunk_index']}`",
            f"- channel span: `{best_candidate['channel_start']}:{best_candidate['channel_stop']}`",
            f"- window start within chunk: `{best_candidate['window_start']}` samples",
            f"- codec events: `{best_candidate['event_count']}`",
            f"- SpikeInterface peak count: `{best_candidate.get('peak_count', 0)}`",
            f"- evaluation status: `{best_candidate['evaluation_status']}`",
            f"- artifact: `{artifact_name}`",
            "",
            "## Interpretation",
            "- The bounded search preserved the existing downstream contract: same codec, same NWB roundtrip requirement, same SpikeInterface path.",
            "- The search broadened only chunk choice, channel window, and representative slice selection.",
            f"- Final verdict: `{final_verdict}`.",
            "",
            "## Next Step",
            next_step,
            "",
        ]
    )


def run_ibl_bounded_refinement(
    target: IblPublicTarget = DEFAULT_IBL_TARGET,
    window_samples: int = 6000,
    channel_limit: int = 8,
    search_chunk_count: int = 9,
    channel_step: int = 32,
    windows_per_chunk: int = 5,
    top_k_peak_probe: int = 12,
    top_k_full_eval: int = 3,
) -> dict[str, Any]:
    append_command_log(
        "python3.11 tools/run_ibl_bounded_refinement.py "
        f"--window-samples {window_samples} --channel-limit {channel_limit} "
        f"--search-chunk-count {search_chunk_count} --channel-step {channel_step} "
        f"--windows-per-chunk {windows_per_chunk} --top-k-peak-probe {top_k_peak_probe} "
        f"--top-k-full-eval {top_k_full_eval}"
    )

    manifest = load_ibl_public_chunk_manifest(target=target)
    chunk_indices = _chunk_index_grid(
        chunk_count=int(manifest["chunk_count"]),
        search_chunk_count=search_chunk_count,
    )
    channel_starts = _channel_start_grid(
        total_channels=int(manifest["n_channels"]),
        channel_limit=channel_limit,
        step=channel_step,
    )

    coarse_candidates: list[dict[str, Any]] = []
    chunk_scan_samples = int(window_samples) * max(1, int(windows_per_chunk))
    dataset_id = f"ibl-public:{target.subject}"
    for chunk_index in chunk_indices:
        for channel_start in channel_starts:
            samples_uv_t_by_c, source_meta = load_ibl_public_trace_slice(
                sample_limit=chunk_scan_samples,
                channel_limit=channel_limit,
                chunk_index=chunk_index,
                channel_start=channel_start,
                start_sample=0,
                target=target,
            )
            window_starts = _window_start_grid(
                total_samples=int(samples_uv_t_by_c.shape[0]),
                window_samples=window_samples,
                windows_per_chunk=windows_per_chunk,
            )
            for window_start in window_starts:
                window_stop = min(int(samples_uv_t_by_c.shape[0]), int(window_start) + int(window_samples))
                window_samples_uv_t_by_c = samples_uv_t_by_c[window_start:window_stop]
                recording, _ = _recording_from_trace_slice(
                    name=target.label,
                    dataset_id=dataset_id,
                    asset_path=target.cbin_key,
                    sampling_rate_hz=float(source_meta["sampling_rate_hz"]),
                    samples_uv_t_by_c=window_samples_uv_t_by_c,
                )
                payload = _window_candidate_payload(recording=recording, start_sample=window_start)
                coarse_candidates.append(
                    {
                        **payload,
                        "chunk_index": int(chunk_index),
                        "chunk_sample_start": int(source_meta["chunk_sample_start"]),
                        "chunk_sample_stop": int(source_meta["chunk_sample_stop"]),
                        "window_start": int(window_start),
                        "window_stop": int(window_stop),
                        "absolute_start_sample": int(source_meta["chunk_sample_start"] + window_start),
                        "absolute_stop_sample": int(source_meta["chunk_sample_start"] + window_stop),
                        "channel_start": int(channel_start),
                        "channel_stop": int(source_meta["channel_stop"]),
                        "channel_limit": int(channel_limit),
                    }
                )

    ranked_coarse = sorted(coarse_candidates, key=_coarse_rank_key, reverse=True)
    for rank, candidate in enumerate(ranked_coarse, start=1):
        candidate["coarse_rank"] = rank

    peak_probe_candidates: list[dict[str, Any]] = []
    for candidate in ranked_coarse[: max(1, int(top_k_peak_probe))]:
        recording, _ = _candidate_recording(
            candidate=candidate,
            sample_limit=window_samples,
            channel_limit=channel_limit,
            target=target,
        )
        peak_probe = _spikeinterface_peak_probe(recording)
        peak_count = int(peak_probe.get("peak_count") or 0) if peak_probe["status"] == "PASS" else -1
        peak_probe_candidates.append(
            {
                **candidate,
                "peak_probe": peak_probe,
                "peak_count": peak_count,
            }
        )

    ranked_peak_probe = sorted(peak_probe_candidates, key=_peak_probe_rank_key, reverse=True)

    evaluated_candidates: list[dict[str, Any]] = []
    for candidate in ranked_peak_probe[: max(1, int(top_k_full_eval))]:
        recording, source_meta = _candidate_recording(
            candidate=candidate,
            sample_limit=window_samples,
            channel_limit=channel_limit,
            target=target,
        )
        codec_metrics = _evaluate_recording(recording)
        candidate_label = (
            f"{target.label}__chunk{int(candidate['chunk_index']):04d}"
            f"_ch{int(candidate['channel_start']):03d}"
            f"_w{int(candidate['window_start']):05d}"
        )
        target_artifact_root, nwb_roundtrip, spikeinterface = _run_target_insertion_evals(
            recording=recording,
            target_label=candidate_label,
        )
        evaluation_failure_reasons: list[str] = []
        if codec_metrics["event_count"] <= 0:
            evaluation_failure_reasons.append("NO_CODEC_EVENTS_DETECTED")
        if nwb_roundtrip["status"] != "PASS":
            evaluation_failure_reasons.append(f"NWB_ROUNDTRIP_{nwb_roundtrip['status']}")
        if spikeinterface["status"] != "PASS":
            evaluation_failure_reasons.append(f"SPIKEINTERFACE_{spikeinterface['status']}")
        evaluation_status = "PASS" if not evaluation_failure_reasons else "FAIL"
        payload = {
            "schema_version": "ibl-refinement-2026-03-21",
            "generated_at_utc": utc_now_iso(),
            "status": "PASS",
            "waveform_slice_executed": True,
            "search_candidate": {
                "chunk_index": int(candidate["chunk_index"]),
                "channel_start": int(candidate["channel_start"]),
                "channel_stop": int(candidate["channel_stop"]),
                "window_start": int(candidate["window_start"]),
                "absolute_start_sample": int(candidate["absolute_start_sample"]),
                "coarse_rank": int(candidate["coarse_rank"]),
                "peak_probe_rank": int(ranked_peak_probe.index(candidate) + 1),
            },
            "source": source_meta,
            "codec_metrics": codec_metrics,
            "nwb_roundtrip": nwb_roundtrip,
            "spikeinterface": spikeinterface,
            "evaluation_status": evaluation_status,
            "evaluation_failure_reasons": evaluation_failure_reasons,
            "resource_notes": {
                "local_feasibility": (
                    "Bounded IBL refinement reused the public S3 raw-byte path and searched chunk, channel, "
                    "and representative window choice without changing the downstream insertion contract."
                ),
            },
        }
        artifact_rel = Path("candidates") / f"{candidate_label}.json"
        write_json(ARTIFACT_ROOT / artifact_rel, payload)
        evaluated_candidates.append(
            {
                **candidate,
                "source": source_meta,
                "codec_metrics": codec_metrics,
                "nwb_roundtrip": nwb_roundtrip,
                "spikeinterface": spikeinterface,
                "evaluation_status": evaluation_status,
                "evaluation_failure_reasons": evaluation_failure_reasons,
                "artifact": str((ARTIFACT_ROOT / artifact_rel).relative_to(ARTIFACT_ROOT)),
                "target_artifact_root": target_artifact_root,
            }
        )

    if not evaluated_candidates:
        raise RuntimeError("NO_IBL_REFINEMENT_CANDIDATES_EVALUATED")

    ranked_evaluated = sorted(evaluated_candidates, key=_full_eval_rank_key, reverse=True)
    best_candidate = ranked_evaluated[0]
    best_candidate_payload = {
        "schema_version": "ibl-refinement-2026-03-21",
        "generated_at_utc": utc_now_iso(),
        "status": "PASS",
        "waveform_slice_executed": True,
        "search_summary_artifact": "ibl_refinement_search.json",
        "search_candidate": {
            "chunk_index": int(best_candidate["chunk_index"]),
            "channel_start": int(best_candidate["channel_start"]),
            "channel_stop": int(best_candidate["channel_stop"]),
            "window_start": int(best_candidate["window_start"]),
            "absolute_start_sample": int(best_candidate["absolute_start_sample"]),
            "coarse_rank": int(best_candidate["coarse_rank"]),
        },
        "source": best_candidate["source"],
        "codec_metrics": best_candidate["codec_metrics"],
        "nwb_roundtrip": best_candidate["nwb_roundtrip"],
        "spikeinterface": best_candidate["spikeinterface"],
        "evaluation_status": best_candidate["evaluation_status"],
        "evaluation_failure_reasons": best_candidate["evaluation_failure_reasons"],
        "resource_notes": {
            "local_feasibility": (
                "Bounded IBL refinement searched the public target across chunk, channel, and representative window "
                "choice while preserving the existing codec + NWB + SpikeInterface contract."
            ),
        },
    }
    write_json(ARTIFACT_ROOT / "public_corpus_ibl_waveform_eval.json", best_candidate_payload)

    final_verdict = best_candidate["evaluation_status"]
    decision_note = _decision_note(
        best_candidate=best_candidate,
        final_verdict=final_verdict,
        artifact_name=best_candidate["artifact"],
    )
    (ARTIFACT_ROOT / "ibl_refinement_decision.md").write_text(decision_note, encoding="utf-8")

    cleanup = _cleanup_remote_probe_cache(
        cache_root=ARTIFACT_ROOT / target.label / "remote_probe_cache",
        keep_chunk_indices={int(best_candidate["chunk_index"])},
    )

    summary = {
        "schema_version": "ibl-refinement-search-2026-03-21",
        "generated_at_utc": utc_now_iso(),
        "target_label": target.label,
        "status": final_verdict,
        "search_config": {
            "window_samples": int(window_samples),
            "channel_limit": int(channel_limit),
            "search_chunk_count": int(search_chunk_count),
            "channel_step": int(channel_step),
            "windows_per_chunk": int(windows_per_chunk),
            "top_k_peak_probe": int(top_k_peak_probe),
            "top_k_full_eval": int(top_k_full_eval),
            "chunk_indices": chunk_indices,
            "channel_starts": channel_starts,
        },
        "target_manifest": {
            "chunk_count": int(manifest["chunk_count"]),
            "n_channels": int(manifest["n_channels"]),
        },
        "candidate_counts": {
            "coarse": len(coarse_candidates),
            "peak_probed": len(peak_probe_candidates),
            "evaluated": len(evaluated_candidates),
        },
        "top_coarse_candidates": [_summarize_candidate(candidate) for candidate in ranked_coarse[:10]],
        "peak_probe_candidates": [_summarize_candidate(candidate) for candidate in ranked_peak_probe],
        "evaluated_candidates": [_summarize_candidate(candidate) for candidate in ranked_evaluated],
        "best_candidate": _summarize_candidate(best_candidate),
        "cleanup": cleanup,
        "decision_artifact": "ibl_refinement_decision.md",
        "best_eval_artifact": "public_corpus_ibl_waveform_eval.json",
    }
    write_json(ARTIFACT_ROOT / "ibl_refinement_search.json", summary)
    return summary
