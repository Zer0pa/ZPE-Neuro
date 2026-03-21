#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import bootstrap

bootstrap()

from zpe_neuro.breadth_adjudication import run_breadth_adjudication


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artifact-root",
        default="proofs/selected_artifacts/2026-03-21_zpe_neuro_breadth_adjudication",
    )
    parser.add_argument(
        "--window-root",
        default="proofs/selected_artifacts/2026-03-20_zpe_neuro_window_policy_rerun",
    )
    parser.add_argument(
        "--ibl-root",
        default="proofs/selected_artifacts/2026-03-20_zpe_neuro_ibl_waveform_probe",
    )
    args = parser.parse_args()
    result = run_breadth_adjudication(
        artifact_root=Path(args.artifact_root),
        window_root=Path(args.window_root),
        ibl_root=Path(args.ibl_root),
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
