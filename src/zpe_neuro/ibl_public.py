from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np

from .public_corpus import (
    _evaluate_recording,
    _recording_from_trace_slice,
    _run_target_insertion_evals,
)
from .wave1 import ARTIFACT_ROOT, REPO_ROOT, append_command_log, utc_now_iso, write_json


_S3_REGION = "us-east-1"
_READ_TIMEOUT_SECONDS = 60


@dataclass(frozen=True)
class IblPublicTarget:
    label: str
    tier: str
    bucket: str
    subject: str
    session_date: str
    experiment_number: int
    probe: str
    meta_key: str
    ch_key: str
    cbin_key: str


DEFAULT_IBL_TARGET = IblPublicTarget(
    label="ibl_ks014_2019_12_03_probe00_ap",
    tier="tier2_breadth",
    bucket="ibl-brain-wide-map-public",
    subject="KS014",
    session_date="2019-12-03",
    experiment_number=1,
    probe="probe00",
    meta_key=(
        "data/cortexlab/Subjects/KS014/2019-12-03/001/raw_ephys_data/probe00/"
        "_spikeglx_ephysData_g0_t0.imec0.ap.45c44949-8d6a-4caa-80bf-8c79708cbd1d.meta"
    ),
    ch_key=(
        "data/cortexlab/Subjects/KS014/2019-12-03/001/raw_ephys_data/probe00/"
        "_spikeglx_ephysData_g0_t0.imec0.ap.35b7a884-522a-4be5-aab4-c80a05dd34e4.ch"
    ),
    cbin_key=(
        "data/cortexlab/Subjects/KS014/2019-12-03/001/raw_ephys_data/probe00/"
        "_spikeglx_ephysData_g0_t0.imec0.ap.d4fee543-dc5e-4df8-80f2-aa42b1f252ec.cbin"
    ),
)


def _unsigned_s3_client():
    import boto3
    from botocore import UNSIGNED
    from botocore.config import Config

    return boto3.client(
        "s3",
        region_name=_S3_REGION,
        config=Config(signature_version=UNSIGNED, read_timeout=_READ_TIMEOUT_SECONDS),
    )


def _relative_to_repo(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT)) if path.is_relative_to(REPO_ROOT) else str(path)


def _download_object(
    client,
    bucket: str,
    key: str,
    destination: Path,
    byte_range: str | None = None,
) -> int:
    if destination.exists():
        return int(destination.stat().st_size)
    request: dict[str, Any] = {"Bucket": bucket, "Key": key}
    if byte_range is not None:
        request["Range"] = byte_range
    body = client.get_object(**request)["Body"].read()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(body)
    return len(body)


def _trim_chunk_metadata(
    chunk_meta: dict[str, Any],
    chunk_index: int,
) -> tuple[dict[str, Any], int, int, int, int]:
    offsets = [int(value) for value in chunk_meta["chunk_offsets"]]
    bounds = [int(value) for value in chunk_meta["chunk_bounds"]]
    if not 0 <= chunk_index < len(offsets) - 1:
        raise IndexError(f"CHUNK_INDEX_OUT_OF_RANGE:{chunk_index}")

    byte_start = offsets[chunk_index]
    byte_stop = offsets[chunk_index + 1]
    sample_start = bounds[chunk_index]
    sample_stop = bounds[chunk_index + 1]

    trimmed = dict(chunk_meta)
    trimmed["chunk_offsets"] = [0, byte_stop - byte_start]
    trimmed["chunk_bounds"] = [0, sample_stop - sample_start]
    trimmed["shape"] = [sample_stop - sample_start, int(chunk_meta["n_channels"])]
    trimmed["sha1_compressed"] = None
    trimmed["sha1_uncompressed"] = None
    trimmed["chopped"] = True
    return trimmed, byte_start, byte_stop, sample_start, sample_stop


def _materialize_chunk(
    target: IblPublicTarget,
    artifact_root: Path,
    chunk_index: int,
) -> dict[str, Any]:
    client = _unsigned_s3_client()
    local_root = artifact_root / target.label / "remote_probe_cache"
    local_root.mkdir(parents=True, exist_ok=True)

    meta_path = local_root / Path(target.meta_key).name
    full_ch_path = local_root / Path(target.ch_key).name
    local_ch_path = local_root / f"chunk{chunk_index:04d}_{Path(target.ch_key).name}"
    local_cbin_path = local_root / f"chunk{chunk_index:04d}_{Path(target.cbin_key).name}"

    meta_bytes = _download_object(client, target.bucket, target.meta_key, meta_path)
    full_ch_bytes = _download_object(client, target.bucket, target.ch_key, full_ch_path)

    full_chunk_meta = json.loads(full_ch_path.read_text(encoding="utf-8"))
    chunk_meta, byte_start, byte_stop, sample_start, sample_stop = _trim_chunk_metadata(
        full_chunk_meta, chunk_index=chunk_index
    )
    local_ch_path.write_text(json.dumps(chunk_meta), encoding="utf-8")

    range_header = f"bytes={byte_start}-{byte_stop - 1}"
    cbin_bytes = _download_object(
        client,
        target.bucket,
        target.cbin_key,
        local_cbin_path,
        byte_range=range_header,
    )

    return {
        "meta_path": meta_path,
        "full_ch_path": full_ch_path,
        "ch_path": local_ch_path,
        "cbin_path": local_cbin_path,
        "meta_bytes": meta_bytes,
        "ch_bytes": full_ch_bytes,
        "cbin_bytes": cbin_bytes,
        "range_header": range_header,
        "chunk_index": int(chunk_index),
        "chunk_sample_start": int(sample_start),
        "chunk_sample_stop": int(sample_stop),
        "chunk_samples": int(sample_stop - sample_start),
    }


def load_ibl_public_chunk_manifest(
    target: IblPublicTarget = DEFAULT_IBL_TARGET,
) -> dict[str, Any]:
    client = _unsigned_s3_client()
    local_root = ARTIFACT_ROOT / target.label / "remote_probe_cache"
    local_root.mkdir(parents=True, exist_ok=True)

    meta_path = local_root / Path(target.meta_key).name
    full_ch_path = local_root / Path(target.ch_key).name
    meta_bytes = _download_object(client, target.bucket, target.meta_key, meta_path)
    full_ch_bytes = _download_object(client, target.bucket, target.ch_key, full_ch_path)
    chunk_meta = json.loads(full_ch_path.read_text(encoding="utf-8"))
    chunk_offsets = [int(value) for value in chunk_meta.get("chunk_offsets", [])]
    chunk_bounds = [int(value) for value in chunk_meta.get("chunk_bounds", [])]
    return {
        "meta_path": meta_path,
        "full_ch_path": full_ch_path,
        "meta_bytes": int(meta_bytes),
        "ch_bytes": int(full_ch_bytes),
        "n_channels": int(chunk_meta.get("n_channels", 0)),
        "chunk_count": max(0, len(chunk_offsets) - 1),
        "chunk_offsets": chunk_offsets,
        "chunk_bounds": chunk_bounds,
    }


def load_ibl_public_trace_slice(
    sample_limit: int = 6000,
    channel_limit: int = 8,
    chunk_index: int = 0,
    channel_start: int = 0,
    start_sample: int = 0,
    target: IblPublicTarget = DEFAULT_IBL_TARGET,
) -> tuple[np.ndarray, dict[str, Any]]:
    import spikeglx

    materialized = _materialize_chunk(target=target, artifact_root=ARTIFACT_ROOT, chunk_index=chunk_index)
    reader = spikeglx.Reader(
        materialized["cbin_path"],
        meta_file=materialized["meta_path"],
        ch_file=materialized["ch_path"],
        ignore_warnings=True,
    )
    try:
        total_channels = int(reader.nc)
        channel_start = int(channel_start)
        if not 0 <= channel_start < total_channels:
            raise ValueError(f"CHANNEL_START_OUT_OF_RANGE:{channel_start}")

        start_sample = int(start_sample)
        chunk_samples = int(materialized["chunk_samples"])
        if not 0 <= start_sample < chunk_samples:
            raise ValueError(f"START_SAMPLE_OUT_OF_RANGE:{start_sample}")

        channel_stop = min(total_channels, channel_start + int(channel_limit))
        loaded_channels = int(channel_stop - channel_start)
        if loaded_channels <= 0:
            raise ValueError("CHANNEL_SELECTION_EMPTY")

        loaded_samples = min(int(sample_limit), chunk_samples - start_sample)
        if loaded_samples <= 0:
            raise ValueError("SAMPLE_LIMIT_EMPTY")

        volts_t_by_c, sync_t_by_bits = reader.read_samples(
            first_sample=start_sample,
            last_sample=start_sample + loaded_samples,
            channels=slice(channel_start, channel_stop),
        )
        samples_uv_t_by_c = np.asarray(volts_t_by_c * 1_000_000.0, dtype=np.float32)
        sync_bits = int(sync_t_by_bits.shape[1]) if sync_t_by_bits is not None and sync_t_by_bits.ndim == 2 else 0
        source_meta = {
            "target_label": target.label,
            "tier": target.tier,
            "subject": target.subject,
            "session_date": target.session_date,
            "experiment_number": target.experiment_number,
            "probe": target.probe,
            "bucket": target.bucket,
            "meta_key": target.meta_key,
            "ch_key": target.ch_key,
            "cbin_key": target.cbin_key,
            "sample_limit_requested": int(sample_limit),
            "sample_limit_loaded": int(loaded_samples),
            "chunk_index": int(chunk_index),
            "chunk_sample_start": int(materialized["chunk_sample_start"]),
            "chunk_sample_stop": int(materialized["chunk_sample_stop"]),
            "chunk_samples": int(materialized["chunk_samples"]),
            "chunk_local_start": int(start_sample),
            "chunk_local_stop": int(start_sample + loaded_samples),
            "absolute_sample_start": int(materialized["chunk_sample_start"] + start_sample),
            "absolute_sample_stop": int(materialized["chunk_sample_start"] + start_sample + loaded_samples),
            "sampling_rate_hz": float(reader.fs),
            "channel_start": int(channel_start),
            "channel_stop": int(channel_stop),
            "channels": int(loaded_channels),
            "total_channels": total_channels,
            "sample2volts_first": float(reader.sample2volts[channel_start]),
            "sync_bits": sync_bits,
            "materialized": {
                "meta_path": _relative_to_repo(materialized["meta_path"]),
                "ch_path": _relative_to_repo(materialized["ch_path"]),
                "cbin_path": _relative_to_repo(materialized["cbin_path"]),
                "meta_bytes": int(materialized["meta_bytes"]),
                "ch_bytes": int(materialized["ch_bytes"]),
                "cbin_bytes": int(materialized["cbin_bytes"]),
                "range_header": materialized["range_header"],
            },
        }
        return samples_uv_t_by_c, source_meta
    finally:
        reader.close()


def load_ibl_public_recording(
    sample_limit: int = 6000,
    channel_limit: int = 8,
    chunk_index: int = 0,
    channel_start: int = 0,
    start_sample: int = 0,
    target: IblPublicTarget = DEFAULT_IBL_TARGET,
) -> tuple[Any, dict[str, Any]]:
    samples_uv_t_by_c, source_meta = load_ibl_public_trace_slice(
        sample_limit=sample_limit,
        channel_limit=channel_limit,
        chunk_index=chunk_index,
        channel_start=channel_start,
        start_sample=start_sample,
        target=target,
    )
    recording, slice_meta = _recording_from_trace_slice(
        name=target.label,
        dataset_id=f"ibl-public:{target.subject}",
        asset_path=target.cbin_key,
        sampling_rate_hz=float(source_meta["sampling_rate_hz"]),
        samples_uv_t_by_c=samples_uv_t_by_c,
    )
    return recording, {
        **source_meta,
        **slice_meta,
    }


def run_ibl_public_waveform_eval(
    sample_limit: int = 6000,
    channel_limit: int = 8,
    chunk_index: int = 0,
    channel_start: int = 0,
    start_sample: int = 0,
    target: IblPublicTarget = DEFAULT_IBL_TARGET,
) -> dict[str, Any]:
    append_command_log(
        "python3.11 tools/run_ibl_public_waveform_eval.py "
        f"--sample-limit {sample_limit} --channel-limit {channel_limit} --chunk-index {chunk_index} "
        f"--channel-start {channel_start} --start-sample {start_sample}"
    )

    recording, source_meta = load_ibl_public_recording(
        sample_limit=sample_limit,
        channel_limit=channel_limit,
        chunk_index=chunk_index,
        channel_start=channel_start,
        start_sample=start_sample,
        target=target,
    )
    codec_metrics = _evaluate_recording(recording)
    target_artifact_root, nwb_roundtrip, spikeinterface = _run_target_insertion_evals(
        recording=recording,
        target_label=target.label,
    )
    evaluation_failure_reasons: list[str] = []
    if codec_metrics["event_count"] <= 0:
        evaluation_failure_reasons.append("NO_CODEC_EVENTS_DETECTED")
    if nwb_roundtrip["status"] != "PASS":
        evaluation_failure_reasons.append(f"NWB_ROUNDTRIP_{nwb_roundtrip['status']}")
    if spikeinterface["status"] != "PASS":
        evaluation_failure_reasons.append(f"SPIKEINTERFACE_{spikeinterface['status']}")

    payload = {
        "schema_version": "ibl-waveform-2026-03-20",
        "generated_at_utc": utc_now_iso(),
        "status": "PASS",
        "waveform_slice_executed": True,
        "evaluation_status": "PASS" if not evaluation_failure_reasons else "FAIL",
        "source": source_meta,
        "codec_metrics": codec_metrics,
        "nwb_roundtrip": nwb_roundtrip,
        "spikeinterface": spikeinterface,
        "evaluation_failure_reasons": evaluation_failure_reasons,
        "artifacts_root": target_artifact_root,
        "resource_notes": {
            "local_feasibility": (
                "Real IBL raw AP slice executed locally by materializing one compressed chunk plus "
                "small companion files from the public S3 bucket."
            ),
            "disk_bytes_materialized": int(source_meta["materialized"]["cbin_bytes"])
            + int(source_meta["materialized"]["meta_bytes"])
            + int(source_meta["materialized"]["ch_bytes"]),
        },
    }
    write_json(ARTIFACT_ROOT / "public_corpus_ibl_waveform_eval.json", payload)
    return payload
