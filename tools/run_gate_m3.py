#!/usr/bin/env python3.11
from __future__ import annotations

import json

from _bootstrap import bootstrap

bootstrap()

from zpe_neuro.max_wave import run_gate_m3


def main() -> int:
    result = run_gate_m3()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

