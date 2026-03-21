#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import json

from _bootstrap import bootstrap, configure_artifact_root


def _parse_replay_seeds(raw: str) -> list[int]:
    values = [item.strip() for item in raw.split(",") if item.strip()]
    return [int(value) for value in values]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artifact-root",
        default=None,
        help="Override the repo-local artifact root for this run.",
    )
    parser.add_argument("--gate", choices=["A", "B", "C", "D", "E"], default=None)
    parser.add_argument("--max-wave", action="store_true")
    parser.add_argument("--seed", type=int, default=20260220)
    parser.add_argument(
        "--replay-seeds",
        default="20260220,20260221,20260222,20260223,20260224",
    )
    args = parser.parse_args()
    configure_artifact_root(args.artifact_root)
    bootstrap()
    from zpe_neuro.max_wave import run_max_wave
    from zpe_neuro.wave1 import run_full, run_gate_a, run_gate_b, run_gate_c, run_gate_d, run_gate_e

    replay = _parse_replay_seeds(args.replay_seeds)

    if args.max_wave and args.gate is not None:
        raise SystemExit("Cannot set --max-wave with --gate")

    if args.gate == "A":
        result = run_gate_a()
    elif args.gate == "B":
        result = run_gate_b(seed=args.seed)
    elif args.gate == "C":
        result = run_gate_c(seed=args.seed)
    elif args.gate == "D":
        result = run_gate_d(replay_seeds=replay)
    elif args.gate == "E":
        result = run_gate_e()
    elif args.max_wave:
        base = run_full(seed=args.seed, replay_seeds=replay)
        max_wave = run_max_wave()
        result = {
            "status": "PASS"
            if base.get("status") == "PASS" and max_wave.get("status") == "PASS"
            else "FAIL",
            "base": base,
            "max_wave": max_wave,
        }
    else:
        result = run_full(seed=args.seed, replay_seeds=replay)

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result.get("status") == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
