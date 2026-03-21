#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import json

from _bootstrap import bootstrap

bootstrap()

from zpe_neuro.ibl_public import run_ibl_public_waveform_eval


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sample-limit", type=int, default=6000)
    parser.add_argument("--channel-limit", type=int, default=8)
    parser.add_argument("--chunk-index", type=int, default=0)
    parser.add_argument("--channel-start", type=int, default=0)
    parser.add_argument("--start-sample", type=int, default=0)
    args = parser.parse_args()
    result = run_ibl_public_waveform_eval(
        sample_limit=args.sample_limit,
        channel_limit=args.channel_limit,
        chunk_index=args.chunk_index,
        channel_start=args.channel_start,
        start_sample=args.start_sample,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
