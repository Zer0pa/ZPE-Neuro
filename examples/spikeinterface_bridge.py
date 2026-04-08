from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import zpe_neuro.wave1 as wave1
from zpe_neuro.public_corpus import PublicCorpusRunner


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="SpikeInterface bridge demo for ZPE-Neuro recordings.")
    parser.add_argument("--dandiset-id", default="000034", help="DANDI dandiset id to target.")
    parser.add_argument("--data-root", default=None, help="Optional local download root for NWB assets.")
    parser.add_argument("--artifact-root", default=None, help="Optional artifact output directory.")
    parser.add_argument("--sample-limit", type=int, default=6000, help="Sample window length.")
    parser.add_argument("--channel-limit", type=int, default=8, help="Channel limit for the slice.")
    parser.add_argument("--window-policy", default="scan", choices=("first", "scan"), help="Window selection policy.")
    parser.add_argument("--offline", action="store_true", help="Use the repo's offline fixture instead of streaming.")
    return parser.parse_args()


def _spikeinterface_available() -> bool:
    return importlib.util.find_spec("spikeinterface") is not None


def _run_spikeinterface(recording, *, artifact_root: str | None) -> dict[str, object]:
    previous_root = wave1.ARTIFACT_ROOT
    if artifact_root is None:
        target_root = previous_root
    else:
        target_root = Path(artifact_root)
        target_root.mkdir(parents=True, exist_ok=True)
    wave1.ARTIFACT_ROOT = target_root
    try:
        return wave1._spikeinterface_e2e(recording)
    finally:
        wave1.ARTIFACT_ROOT = previous_root


def _offline_recording():
    try:
        from tests._public_fixture import load_dandi_fixture_recording
    except ModuleNotFoundError:
        print("Offline fixture helpers unavailable. Run from a repo clone.", file=sys.stderr)
        return None
    try:
        recording, _ = load_dandi_fixture_recording()
    except Exception as exc:
        print(f"Offline fixture unavailable: {exc}", file=sys.stderr)
        return None
    return recording


def main() -> int:
    args = _parse_args()
    if not _spikeinterface_available():
        print("SpikeInterface not installed. Install extras: pip install -e '.[public]'.", file=sys.stderr)
        return 0

    if args.offline:
        recording = _offline_recording()
        if recording is None:
            return 0
    else:
        try:
            runner = PublicCorpusRunner(
                dandiset_id=args.dandiset_id,
                data_root=args.data_root,
                sample_limit=args.sample_limit,
                channel_limit=args.channel_limit,
                window_policy=args.window_policy,
            )
            recording, _, _ = runner._load_recording()
        except ModuleNotFoundError as exc:
            missing = exc.name or "dependency"
            print(f"Missing dependency: {missing}. Install extras: pip install -e '.[public]'.", file=sys.stderr)
            return 0
        except Exception as exc:  # pragma: no cover - runtime-only failures
            print(f"Recording load failed: {exc}", file=sys.stderr)
            return 1

    try:
        payload = _run_spikeinterface(recording, artifact_root=args.artifact_root)
    except Exception as exc:  # pragma: no cover - runtime-only failures
        print(f"SpikeInterface run failed: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
