#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import json
from pathlib import Path


CORE_JSON_FIELDS = {
    "schema_version",
    "generated_at_utc",
}


def check_json(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"{path}: invalid JSON ({exc})"]

    missing = sorted(field for field in CORE_JSON_FIELDS if field not in payload)
    if missing:
        errors.append(f"{path}: missing core fields {missing}")
    return errors


def check_text(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8").strip()
    if not content:
        return [f"{path}: empty text artifact"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-root", required=True)
    parser.add_argument("--files", nargs="+", required=True)
    args = parser.parse_args()

    root = Path(args.artifact_root)
    errors: list[str] = []
    for name in args.files:
        path = root / name
        if not path.exists():
            errors.append(f"{path}: missing file")
            continue
        if path.suffix == ".json":
            errors.extend(check_json(path))
        else:
            errors.extend(check_text(path))

    if errors:
        for error in errors:
            print(error)
        return 1
    print("ARTIFACT_SCHEMA_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

