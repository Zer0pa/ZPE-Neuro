#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import json

from _bootstrap import bootstrap

bootstrap()

from zpe_neuro.wave1 import run_gate_d


def _parse_replay_seeds(raw: str) -> list[int]:
    values = [item.strip() for item in raw.split(",") if item.strip()]
    return [int(value) for value in values]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--replay-seeds",
        default="20260220,20260221,20260222,20260223,20260224",
    )
    args = parser.parse_args()
    result = run_gate_d(replay_seeds=_parse_replay_seeds(args.replay_seeds))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

