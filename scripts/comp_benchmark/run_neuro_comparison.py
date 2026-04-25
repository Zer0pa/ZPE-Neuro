"""Wave-CB comp benchmark for ZPE-Neuro.

Two non-commensurable metrics are computed and reported separately:
  (a) lossless raw int16 compression ratios for gzip / lz4 / zstd, and
  (b) ZPE-Neuro's documented event-extraction ratio (LOSSY by design;
      drops non-event samples and retains spike events).

The lossless CRs are computed live from the committed fixture
``tests/fixtures/dandi_000034_mouse412804_ecephys_scan_6000x8.npz``.
The event-extraction ratio is read from the lane's existing benchmark
artifact at ``proofs/artifacts/dandi000034_benchmark/benchmark_summary.json``
(401.044x, from raw_bits=768000 / encoded_bits=1915 over the same window).

These operations are NOT comparable. Do not collapse them.
"""

from __future__ import annotations

import gzip
import json
from pathlib import Path

import lz4.frame
import numpy as np
import zstandard


REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURE = REPO_ROOT / "tests" / "fixtures" / "dandi_000034_mouse412804_ecephys_scan_6000x8.npz"
LANE_BENCH = REPO_ROOT / "proofs" / "artifacts" / "dandi000034_benchmark" / "benchmark_summary.json"
OUT = REPO_ROOT / "proofs" / "artifacts" / "comp_benchmarks" / "neuro_codec_comparison.json"


def lossless_cr(raw: bytes) -> dict:
    raw_bytes = len(raw)
    gz = len(gzip.compress(raw, compresslevel=6))
    l4 = len(lz4.frame.compress(raw))
    zs = len(zstandard.ZstdCompressor(level=3).compress(raw))
    return {
        "raw_bytes": raw_bytes,
        "gzip": {"compressed_bytes": gz, "cr": round(raw_bytes / gz, 4)},
        "lz4": {"compressed_bytes": l4, "cr": round(raw_bytes / l4, 4)},
        "zstd": {"compressed_bytes": zs, "cr": round(raw_bytes / zs, 4)},
    }


def main() -> None:
    data = np.load(FIXTURE)
    arr = data["samples"]
    if arr.dtype != np.int16:
        raise SystemExit(f"Expected int16 samples; got {arr.dtype}")
    raw = arr.tobytes()

    lossless = lossless_cr(raw)

    lane_summary = json.loads(LANE_BENCH.read_text())
    codec = lane_summary["codec_metrics"]
    raw_bits = codec["raw_bits"]
    encoded_bits = codec["encoded_bits"]
    event_count = codec["event_count"]
    event_extraction_ratio = raw_bits / encoded_bits

    payload = {
        "wave": "Wave-CB",
        "date": "2026-04-25",
        "lane": "ZPE-Neuro",
        "data_source": "tests/fixtures/dandi_000034_mouse412804_ecephys_scan_6000x8.npz",
        "framing_note": (
            "ZPE-Neuro's 401x event-extraction ratio is LOSSY (drops non-event samples). "
            "The lossless gzip/lz4/zstd CRs are 1.5-5x on raw int16. "
            "These are non-commensurable operations and must not be compared directly."
        ),
        "lossless_raw_int16": {
            "raw_bytes": lossless["raw_bytes"],
            "gzip": lossless["gzip"],
            "lz4": lossless["lz4"],
            "zstd": lossless["zstd"],
        },
        "zpe_event_extraction": {
            "input_samples": int(arr.size),
            "events_kept": int(event_count),
            "raw_bits": int(raw_bits),
            "encoded_bits": int(encoded_bits),
            "event_extraction_ratio": round(event_extraction_ratio, 4),
            "operation_type": "lossy event extraction (drops non-event samples)",
            "fidelity_contract": (
                f"window-scoped on 8x6000 int16 @ 30 kHz; "
                f"RMSE {codec['rmse_uv']:.2f} uV; "
                f"roundtrip_fidelity {codec['roundtrip_fidelity']:.4f}; "
                f"roundtrip_exact={codec['roundtrip_exact']}; "
                f"snr_db {codec['snr_db']:.4f}; "
                f"reference: proofs/artifacts/dandi000034_benchmark/benchmark_summary.json"
            ),
        },
        "honest_verdict": (
            "ZPE-Neuro is not a lossless general-purpose compressor and should not be compared "
            "to gzip/lz4/zstd as if it were. The 401x number is the event-extraction ratio - a "
            "different operation. For lossless raw-channel storage, gzip/lz4/zstd remain the "
            "appropriate baselines."
        ),
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
