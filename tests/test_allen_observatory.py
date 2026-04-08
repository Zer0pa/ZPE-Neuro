from __future__ import annotations

import os
from pathlib import Path

import pytest


def test_allen_observatory_scaffold() -> None:
    pytest.importorskip("allensdk")
    cache_root = os.environ.get("ALLEN_BRAIN_OBSERVATORY_ROOT")
    if not cache_root:
        pytest.skip("Set ALLEN_BRAIN_OBSERVATORY_ROOT to a local cache directory.")
    assert Path(cache_root).exists()
