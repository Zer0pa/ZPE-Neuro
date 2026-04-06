from __future__ import annotations

from pathlib import Path
import sys
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from zpe_neuro.wave1 import (
    Recording,
    WINDOW_SAMPLES,
    build_templates,
    decode_recording,
    encode_recording,
    validate_recording_metadata,
)


def make_manual_recording(samples: np.ndarray) -> Recording:
    return Recording(
        name="manual",
        profile="manual",
        seed=0,
        sampling_rate_hz=30000,
        channels=int(samples.shape[0]),
        duration_s=float(samples.shape[1]) / 30000.0 if samples.ndim == 2 else 0.0,
        samples=samples,
        templates=build_templates(),
        events=[],
        metadata={},
    )


class EdgeCaseTests(unittest.TestCase):
    def test_empty_recording_is_rejected(self) -> None:
        recording = make_manual_recording(np.zeros((1, 0), dtype=np.int16))
        with self.assertRaisesRegex(ValueError, "INSUFFICIENT_SAMPLE_LENGTH"):
            validate_recording_metadata(recording)

    def test_single_sample_recording_is_rejected(self) -> None:
        recording = make_manual_recording(np.zeros((1, 1), dtype=np.int16))
        with self.assertRaisesRegex(ValueError, "INSUFFICIENT_SAMPLE_LENGTH"):
            validate_recording_metadata(recording)

    def test_single_channel_silence_roundtrips_exactly(self) -> None:
        recording = make_manual_recording(np.zeros((1, WINDOW_SAMPLES + 1), dtype=np.int16))
        validate_recording_metadata(recording)
        packet = encode_recording(recording)
        decoded = decode_recording(packet, recording.templates)
        self.assertTrue(np.array_equal(recording.samples, decoded))

    def test_long_silence_recording_roundtrips_without_shape_drift(self) -> None:
        recording = make_manual_recording(np.zeros((1, 120_000), dtype=np.int16))
        validate_recording_metadata(recording)
        packet = encode_recording(recording)
        decoded = decode_recording(packet, recording.templates)
        self.assertEqual(decoded.shape, recording.samples.shape)
        self.assertTrue(np.array_equal(recording.samples, decoded))


if __name__ == "__main__":
    unittest.main()
