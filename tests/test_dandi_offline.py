from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from tests._public_fixture import (
    FIXTURE_PATH,
    HAS_PYNWB,
    load_dandi_fixture_metrics,
    load_dandi_fixture_recording,
)


@unittest.skipUnless(HAS_PYNWB and FIXTURE_PATH.exists(), "requires offline DANDI fixture")
class DandiOfflineTests(unittest.TestCase):
    def test_fixture_stays_below_size_budget(self) -> None:
        self.assertLess(FIXTURE_PATH.stat().st_size, 5 * 1024 * 1024)

    def test_fixture_recording_shape_matches_selected_window(self) -> None:
        recording, slice_meta = load_dandi_fixture_recording()
        self.assertEqual(recording.channels, 8)
        self.assertEqual(recording.samples.shape, (8, 6000))
        self.assertEqual(recording.sampling_rate_hz, 30000)
        self.assertEqual(slice_meta["event_count"], 41)

    def test_fixture_reproduces_benchmark_metrics(self) -> None:
        metrics = load_dandi_fixture_metrics(repetitions=1)
        self.assertEqual(metrics["event_count"], 41)
        self.assertAlmostEqual(metrics["compression_ratio"], 401.0443864229765)
        self.assertAlmostEqual(metrics["rmse_uv"], 78.4409949420582)
        self.assertFalse(metrics["roundtrip_exact"])


if __name__ == "__main__":
    unittest.main()
