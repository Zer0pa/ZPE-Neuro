from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from zpe_neuro.wave1 import compression_ratio, encode_recording, generate_recording


class Wave1MetricTests(unittest.TestCase):
    def test_sparse_compression_exceeds_threshold(self) -> None:
        recording = generate_recording("sparse", seed=20260220, channels=8, duration_s=1.0)
        packet = encode_recording(recording)
        raw_bits = int(recording.samples.size * 16)
        cr = compression_ratio(raw_bits, int(packet["encoded_bits"]))
        self.assertGreaterEqual(cr, 50.0)


if __name__ == "__main__":
    unittest.main()

