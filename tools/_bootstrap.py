from __future__ import annotations

import os
import sys
from pathlib import Path


def configure_artifact_root(artifact_root: str | None) -> None:
    if artifact_root is None:
        return
    value = artifact_root.strip()
    if not value:
        return
    os.environ["ZPE_NEURO_ARTIFACT_ROOT"] = value


def bootstrap() -> Path:
    repo_root = Path(__file__).resolve().parents[1]
    src_path = repo_root / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
    return repo_root
