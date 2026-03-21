from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from zpe_neuro.public_corpus import (
    _candidate_rank_key,
    _candidate_window_starts,
    _select_window_candidate,
)


class PublicCorpusWindowSelectionTests(unittest.TestCase):
    def test_candidate_window_starts_include_edges_and_are_sorted(self) -> None:
        starts = _candidate_window_starts(total_samples=1000, sample_limit=200, candidate_windows=5)
        self.assertEqual(starts[0], 0)
        self.assertEqual(starts[-1], 800)
        self.assertEqual(starts, sorted(starts))
        self.assertEqual(len(starts), len(set(starts)))

    def test_selection_prefers_eventfulness_then_earlier_start(self) -> None:
        quiet = {
            "start_sample": 0,
            "rank_key": [0, 0, 10, 15, 0],
        }
        active_late = {
            "start_sample": 400,
            "rank_key": [4, 2, 20, 25, -400],
        }
        active_early = {
            "start_sample": 200,
            "rank_key": [4, 2, 20, 25, -200],
        }

        selected = _select_window_candidate([quiet, active_late, active_early])
        self.assertEqual(selected["start_sample"], 200)
        self.assertGreater(_candidate_rank_key(active_early), _candidate_rank_key(quiet))


if __name__ == "__main__":
    unittest.main()
