from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"


def _run_example(script: str, args: list[str]) -> None:
    result = subprocess.run(
        [sys.executable, str(EXAMPLES / script), *args],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr or result.stdout


def test_dandi_example_offline() -> None:
    _run_example("dandi_compress.py", ["--offline"])


def test_spikeinterface_example_offline() -> None:
    _run_example("spikeinterface_bridge.py", ["--offline"])
