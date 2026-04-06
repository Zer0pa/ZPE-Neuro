#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import json

from _bootstrap import bootstrap


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dandiset", required=True, help="DANDI dandiset id, for example 000034.")
    parser.add_argument("--artifact-root", required=True, help="Directory for benchmark artifacts.")
    parser.add_argument(
        "--data-root",
        default=None,
        help="Optional local download root created by `dandi download`.",
    )
    parser.add_argument(
        "--fixture-output",
        default=None,
        help="Optional path for a small extracted NWB fixture.",
    )
    parser.add_argument("--sample-limit", type=int, default=6000)
    parser.add_argument("--channel-limit", type=int, default=8)
    parser.add_argument("--window-policy", choices=["first", "scan"], default="scan")
    parser.add_argument("--candidate-windows", type=int, default=9)
    parser.add_argument("--benchmark-repetitions", type=int, default=5)
    args = parser.parse_args()

    bootstrap()
    from zpe_neuro.public_corpus import PublicCorpusRunner

    runner = PublicCorpusRunner(
        dandiset_id=args.dandiset,
        data_root=args.data_root,
        artifact_root=args.artifact_root,
        sample_limit=args.sample_limit,
        channel_limit=args.channel_limit,
        window_policy=args.window_policy,
        candidate_windows=args.candidate_windows,
        benchmark_repetitions=args.benchmark_repetitions,
    )
    result = runner.run_benchmark(fixture_output=args.fixture_output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
