#!/usr/bin/env python3.11
from __future__ import annotations

import json
import sys

from _bootstrap import bootstrap

bootstrap()

from zpe_neuro.wave1 import RUNBOOK_FILES


def main() -> int:
    missing = [str(path) for path in RUNBOOK_FILES if not path.exists()]
    payload = {
        "status": "PASS" if not missing else "FAIL",
        "missing": missing,
    }
    print(json.dumps(payload, indent=2))
    if missing:
        return 1
    print("RUNBOOK_CONTRACT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

