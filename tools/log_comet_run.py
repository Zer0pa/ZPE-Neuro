#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path
from typing import Any

from _bootstrap import bootstrap

REPO_ROOT = bootstrap()

from zpe_neuro.wave1 import utc_now_iso

STATUS_SCORE = {
    "PASS": 1.0,
    "INCONCLUSIVE": 0.5,
    "OPEN": 0.25,
    "UNTESTED": 0.0,
    "PAUSED_EXTERNAL": -0.5,
    "FAIL": -1.0,
}


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _git_branch() -> str:
    proc = subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=REPO_ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    return proc.stdout.strip() or "UNKNOWN"


def _git_remote() -> str:
    proc = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        cwd=REPO_ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    return proc.stdout.strip() or "UNKNOWN"


def _relative_str(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _flatten(prefix: str, value: Any) -> list[tuple[str, Any]]:
    if isinstance(value, dict):
        items: list[tuple[str, Any]] = []
        for key, child in value.items():
            child_prefix = f"{prefix}.{key}" if prefix else str(key)
            items.extend(_flatten(child_prefix, child))
        return items
    if isinstance(value, list):
        return [(prefix, json.dumps(value, sort_keys=True))]
    return [(prefix, value)]


def _log_payload(experiment: Any, prefix: str, payload: dict[str, Any]) -> None:
    for key, value in _flatten(prefix, payload):
        if isinstance(value, bool):
            experiment.log_other(key, str(value).lower())
            continue
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            experiment.log_metric(key, value)
            continue
        if isinstance(value, str) and value in STATUS_SCORE:
            experiment.log_other(key, value)
            experiment.log_metric(f"{key}_score", STATUS_SCORE[value])
            continue
        experiment.log_other(key, str(value))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-root", required=True)
    parser.add_argument("--packet-dir", required=False)
    parser.add_argument("--lane", default="ZPE-Neuro")
    parser.add_argument("--current-gate", default="AM-NEU-01")
    parser.add_argument("--workspace-path", default=str(REPO_ROOT.parent))
    parser.add_argument("--project-name", default="zpe-neuro")
    parser.add_argument("--workspace-name", default="zer0pa")
    parser.add_argument("--run-name", default="2026-03-20_operational_realignment")
    args = parser.parse_args()

    api_key = os.getenv("COMET_API_KEY", "").strip()
    if not api_key:
        raise SystemExit("COMET_API_KEY_MISSING")

    artifact_root = Path(args.artifact_root).resolve()
    packet_dir = Path(args.packet_dir).resolve() if args.packet_dir else None
    artifact_root.mkdir(parents=True, exist_ok=True)

    from comet_ml import Experiment

    experiment = Experiment(
        api_key=api_key,
        workspace=args.workspace_name,
        project_name=args.project_name,
        auto_output_logging="simple",
        auto_metric_logging=False,
        auto_param_logging=False,
        parse_args=False,
        log_code=False,
    )
    experiment.set_name(args.run_name)
    experiment.log_parameter("lane", args.lane)
    experiment.log_parameter("workspace_path", args.workspace_path)
    experiment.log_parameter("repo_path", str(REPO_ROOT))
    experiment.log_parameter("branch", _git_branch())
    experiment.log_parameter("origin_remote", _git_remote())
    experiment.log_parameter("artifact_root", _relative_str(artifact_root))
    experiment.log_other("current_gate", args.current_gate)

    logged_files: list[str] = []
    summary_files = [
        "gate_c_summary.json",
        "gate_d_summary.json",
        "public_corpus_summary.json",
        "public_corpus_eval_dandi_000034_mouse412804_ecephys.json",
        "public_corpus_eval_ajile12_sub01_ses7_ecephys.json",
        "public_corpus_ibl_probe.json",
    ]
    for file_name in summary_files:
        path = artifact_root / file_name
        if not path.exists():
            continue
        payload = _read_json(path)
        _log_payload(experiment, path.stem, payload)
        experiment.log_asset(str(path), file_name=_relative_str(path))
        logged_files.append(_relative_str(path))

    if packet_dir and packet_dir.exists():
        for doc_path in sorted(packet_dir.glob("*.md")):
            experiment.log_asset(str(doc_path), file_name=_relative_str(doc_path))
            logged_files.append(_relative_str(doc_path))

    manifest = {
        "generated_at_utc": utc_now_iso(),
        "status": "PASS",
        "lane": args.lane,
        "current_gate": args.current_gate,
        "workspace_path": args.workspace_path,
        "repo_path": str(REPO_ROOT),
        "branch": _git_branch(),
        "origin_remote": _git_remote(),
        "artifact_root": _relative_str(artifact_root),
        "packet_dir": _relative_str(packet_dir) if packet_dir else None,
        "run_name": args.run_name,
        "project_name": args.project_name,
        "workspace_name": args.workspace_name,
        "experiment_key": experiment.get_key(),
        "experiment_url": getattr(experiment, "url", None),
        "logged_files": logged_files,
    }
    manifest_path = artifact_root / "comet_run_manifest.json"
    with manifest_path.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2, sort_keys=True)
        handle.write("\n")

    experiment.log_asset(str(manifest_path), file_name=_relative_str(manifest_path))
    experiment.end()
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
