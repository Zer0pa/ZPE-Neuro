#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import bootstrap


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Benchmark a local NWB file with the ZPE-Neuro codec.")
    parser.add_argument("--nwb-path", required=True, help="Path to a local NWB file.")
    parser.add_argument("--dataset-id", required=True, help="Dataset identifier (e.g., DANDI 000003).")
    parser.add_argument("--asset-path", default="local.nwb", help="Dataset-relative asset path for provenance.")
    parser.add_argument("--sample-limit", type=int, default=6000, help="Sample window length.")
    parser.add_argument("--channel-limit", type=int, default=8, help="Channel limit for the slice.")
    parser.add_argument("--start-sample", type=int, default=0, help="Start sample for the slice.")
    parser.add_argument("--benchmark-repetitions", type=int, default=3, help="Codec repetitions for timing.")
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    nwb_path = Path(args.nwb_path)
    if not nwb_path.exists():
        raise SystemExit(f"NWB file not found: {nwb_path}")

    bootstrap()
    try:
        from pynwb import NWBHDF5IO
    except ModuleNotFoundError as exc:
        raise SystemExit(f"Missing dependency: {exc.name}. Install extras: pip install -e '.[public]'.") from exc

    from zpe_neuro.public_corpus import (
        _extract_time_by_channel_slice,
        _first_electrical_series,
        _recording_from_trace_slice,
        _timed_codec_metrics,
    )

    with NWBHDF5IO(str(nwb_path), "r", load_namespaces=True) as io:
        nwbfile = io.read()
        series_name, series = _first_electrical_series(nwbfile)
        sampling_rate_hz = float(getattr(series, "rate", 0.0) or 0.0)
        samples_uv_t_by_c = _extract_time_by_channel_slice(
            series=series,
            sample_limit=args.sample_limit,
            channel_limit=args.channel_limit,
            start_sample=args.start_sample,
        )
        recording, slice_meta = _recording_from_trace_slice(
            name=f"{args.dataset_id}:{series_name}",
            dataset_id=args.dataset_id,
            asset_path=args.asset_path,
            sampling_rate_hz=sampling_rate_hz,
            samples_uv_t_by_c=samples_uv_t_by_c,
        )

    metrics = _timed_codec_metrics(recording=recording, repetitions=args.benchmark_repetitions)
    payload = {
        "dataset_id": args.dataset_id,
        "asset_path": args.asset_path,
        "nwb_path": str(nwb_path),
        "series_name": series_name,
        "sampling_rate_hz": sampling_rate_hz,
        "slice_meta": slice_meta,
        "codec_metrics": metrics,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
