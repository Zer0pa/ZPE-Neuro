from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from zpe_neuro.public_corpus import PublicCorpusRunner


def _offline_fixture_metrics(*, repetitions: int) -> dict[str, object] | None:
    try:
        from tests._public_fixture import HAS_PYNWB, FIXTURE_PATH, load_dandi_fixture_metrics
    except ModuleNotFoundError:
        print("Offline fixture helpers unavailable. Run from a repo clone.", file=sys.stderr)
        return None
    if not HAS_PYNWB:
        print("Missing pynwb. Install extras: pip install -e '.[public]'.", file=sys.stderr)
        return None
    if not FIXTURE_PATH.exists():
        print(f"Offline fixture missing at {FIXTURE_PATH}.", file=sys.stderr)
        return None
    metrics = load_dandi_fixture_metrics(repetitions=repetitions)
    return {
        "mode": "offline_fixture",
        "fixture_path": str(FIXTURE_PATH),
        "metrics": metrics,
    }


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compress DANDI 000034 via the ZPE-Neuro public corpus runner.")
    parser.add_argument("--dandiset-id", default="000034", help="DANDI dandiset id to target.")
    parser.add_argument("--data-root", default=None, help="Optional local download root for NWB assets.")
    parser.add_argument("--artifact-root", default=None, help="Optional output directory for benchmark artifacts.")
    parser.add_argument("--sample-limit", type=int, default=6000, help="Sample window length.")
    parser.add_argument("--channel-limit", type=int, default=8, help="Channel limit for the slice.")
    parser.add_argument("--benchmark-repetitions", type=int, default=3, help="Number of codec repetitions.")
    parser.add_argument("--window-policy", default="scan", choices=("first", "scan"), help="Window selection policy.")
    parser.add_argument("--offline", action="store_true", help="Use the repo's offline fixture instead of streaming.")
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    if args.offline:
        payload = _offline_fixture_metrics(repetitions=args.benchmark_repetitions)
        if payload is None:
            return 0
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    try:
        runner = PublicCorpusRunner(
            dandiset_id=args.dandiset_id,
            data_root=args.data_root,
            artifact_root=args.artifact_root,
            sample_limit=args.sample_limit,
            channel_limit=args.channel_limit,
            window_policy=args.window_policy,
            benchmark_repetitions=args.benchmark_repetitions,
        )
        payload = runner.run_benchmark()
    except ModuleNotFoundError as exc:
        missing = exc.name or "dependency"
        print(f"Missing dependency: {missing}. Install extras: pip install -e '.[public]'.", file=sys.stderr)
        return 0
    except Exception as exc:  # pragma: no cover - runtime-only failures
        print(f"Benchmark failed: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
