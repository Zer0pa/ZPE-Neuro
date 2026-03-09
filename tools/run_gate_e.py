#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import json
import os

from _bootstrap import bootstrap

bootstrap()

from zpe_neuro.wave1 import run_gate_e


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artifact-root",
        default=os.getenv("ZPE_NEURO_ARTIFACT_ROOT", "artifacts/2026-02-20_zpe_neuro_wave1"),
    )
    _ = parser.parse_args()
    result = run_gate_e()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
