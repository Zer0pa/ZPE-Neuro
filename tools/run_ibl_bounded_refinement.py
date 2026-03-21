#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import json

from _bootstrap import bootstrap

bootstrap()

from zpe_neuro.ibl_refinement import run_ibl_bounded_refinement


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--window-samples", type=int, default=6000)
    parser.add_argument("--channel-limit", type=int, default=8)
    parser.add_argument("--search-chunk-count", type=int, default=9)
    parser.add_argument("--channel-step", type=int, default=32)
    parser.add_argument("--windows-per-chunk", type=int, default=5)
    parser.add_argument("--top-k-peak-probe", type=int, default=12)
    parser.add_argument("--top-k-full-eval", type=int, default=3)
    args = parser.parse_args()
    result = run_ibl_bounded_refinement(
        window_samples=args.window_samples,
        channel_limit=args.channel_limit,
        search_chunk_count=args.search_chunk_count,
        channel_step=args.channel_step,
        windows_per_chunk=args.windows_per_chunk,
        top_k_peak_probe=args.top_k_peak_probe,
        top_k_full_eval=args.top_k_full_eval,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
