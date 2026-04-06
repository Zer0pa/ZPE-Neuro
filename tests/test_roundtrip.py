from __future__ import annotations

from pathlib import Path
import sys
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from tests._public_fixture import FIXTURE_PATH, HAS_PYNWB, load_dandi_fixture_recording
from zpe_neuro.wave1 import (
    Recording,
    WINDOW_SAMPLES,
    build_templates,
    decode_recording,
    encode_recording,
    validate_recording_metadata,
)


class RoundtripTests(unittest.TestCase):
    def test_silence_recording_roundtrips_bit_exactly(self) -> None:
        samples = np.zeros((1, WINDOW_SAMPLES + 1), dtype=np.int16)
        recording = Recording(
            name="silence",
            profile="manual",
            seed=0,
            sampling_rate_hz=30000,
            channels=1,
            duration_s=float(samples.shape[1]) / 30000.0,
            samples=samples,
            templates=build_templates(),
            events=[],
            metadata={"fixture": "silence"},
        )
        validate_recording_metadata(recording)
        packet = encode_recording(recording)
        decoded = decode_recording(packet, recording.templates)
        self.assertTrue(np.array_equal(recording.samples, decoded))

    @unittest.skipUnless(HAS_PYNWB and FIXTURE_PATH.exists(), "requires offline DANDI fixture")
    def test_offline_fixture_roundtrip_is_deterministic(self) -> None:
        recording, _ = load_dandi_fixture_recording()
        packet_a = encode_recording(recording)
        packet_b = encode_recording(recording)
        decoded_a = decode_recording(packet_a, recording.templates)
        decoded_b = decode_recording(packet_b, recording.templates)

        self.assertEqual(packet_a["encoded_bits"], packet_b["encoded_bits"])
        self.assertTrue(np.array_equal(decoded_a, decoded_b))


if __name__ == "__main__":
    unittest.main()
