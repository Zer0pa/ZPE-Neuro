from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from zpe_neuro.wave1 import decode_recording, encode_recording, generate_recording, rmse_uv


class Wave1CodecTests(unittest.TestCase):
    def test_encode_decode_rmse_under_one_uv(self) -> None:
        recording = generate_recording("sparse", seed=20260220, channels=8, duration_s=1.0)
        packet = encode_recording(recording)
        decoded = decode_recording(packet, recording.templates)
        self.assertLessEqual(rmse_uv(recording.samples, decoded), 1.0)


if __name__ == "__main__":
    unittest.main()

