#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import json

from _bootstrap import bootstrap, configure_artifact_root


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artifact-root",
        default=None,
        help="Override the repo-local artifact root for this run.",
    )
    parser.add_argument("--sample-limit", type=int, default=6000)
    parser.add_argument("--channel-limit", type=int, default=8)
    parser.add_argument("--window-policy", choices=["first", "scan"], default="scan")
    parser.add_argument("--candidate-windows", type=int, default=9)
    args = parser.parse_args()
    configure_artifact_root(args.artifact_root)
    bootstrap()
    from zpe_neuro.public_corpus import run_public_corpus_eval

    result = run_public_corpus_eval(
        sample_limit=args.sample_limit,
        channel_limit=args.channel_limit,
        window_policy=args.window_policy,
        candidate_windows=args.candidate_windows,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
