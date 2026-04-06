from __future__ import annotations

from pathlib import Path
import sys
import unittest
from types import SimpleNamespace

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from zpe_neuro.public_corpus import (
    _center_clip_to_int16,
    _extract_time_by_channel_slice,
    _series_scale_to_uv,
)


class ScalingTests(unittest.TestCase):
    def test_series_scale_to_uv_converts_volts(self) -> None:
        series = SimpleNamespace(unit="volts", conversion=1e-6)
        self.assertEqual(_series_scale_to_uv(series), 1.0)

    def test_extract_time_by_channel_slice_applies_scale_and_offset(self) -> None:
        series = SimpleNamespace(
            data=np.asarray(
                [
                    [0.001, -0.001],
                    [0.002, -0.002],
                    [0.003, -0.003],
                ],
                dtype=np.float32,
            ),
            electrodes=SimpleNamespace(data=[0, 1]),
            unit="volts",
            conversion=1.0,
            offset=1.5,
        )
        extracted = _extract_time_by_channel_slice(series=series, sample_limit=3, channel_limit=2)
        expected = np.asarray(
            [
                [1001.5, -998.5],
                [2001.5, -1998.5],
                [3001.5, -2998.5],
            ],
            dtype=np.float32,
        )
        np.testing.assert_allclose(extracted, expected)

    def test_center_clip_to_int16_normalizes_extreme_values(self) -> None:
        samples = np.asarray(
            [
                [0.0, 1_000_000.0],
                [np.nan, -1_000_000.0],
            ],
            dtype=np.float32,
        )
        clipped, normalization = _center_clip_to_int16(samples)
        self.assertEqual(clipped.dtype, np.int16)
        self.assertLess(normalization, 1.0)
        self.assertLessEqual(int(np.max(np.abs(clipped))), 32000)


if __name__ == "__main__":
    unittest.main()
