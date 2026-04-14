#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import bootstrap


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--target-label",
        default="dandi_000034_mouse412804_ecephys",
        help="Public corpus target label to stream and freeze as an offline fixture.",
    )
    parser.add_argument("--sample-limit", type=int, default=6000)
    parser.add_argument("--channel-limit", type=int, default=8)
    parser.add_argument("--window-policy", choices=["first", "scan"], default="scan")
    parser.add_argument("--candidate-windows", type=int, default=9)
    parser.add_argument(
        "--fixture-path",
        default=None,
        help="Optional explicit output path for the fixture file.",
    )
    args = parser.parse_args()

    bootstrap()
    from zpe_neuro.public_corpus import create_public_corpus_fixture

    result = create_public_corpus_fixture(
        target_label=args.target_label,
        sample_limit=args.sample_limit,
        channel_limit=args.channel_limit,
        window_policy=args.window_policy,
        candidate_windows=args.candidate_windows,
        fixture_path=Path(args.fixture_path) if args.fixture_path else None,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
