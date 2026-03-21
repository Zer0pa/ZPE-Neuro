from __future__ import annotations

import unittest

from zpe_neuro.ibl_refinement import (
    _channel_start_grid,
    _chunk_index_grid,
    _window_start_grid,
)


class IblRefinementTests(unittest.TestCase):
    def test_chunk_index_grid_spans_start_and_end(self) -> None:
        starts = _chunk_index_grid(chunk_count=10, search_chunk_count=4)

        self.assertEqual(starts[0], 0)
        self.assertEqual(starts[-1], 9)
        self.assertGreaterEqual(len(starts), 4)

    def test_channel_start_grid_keeps_last_span(self) -> None:
        starts = _channel_start_grid(total_channels=385, channel_limit=8, step=32)

        self.assertEqual(starts[0], 0)
        self.assertEqual(starts[-1], 377)
        self.assertIn(352, starts)

    def test_window_start_grid_keeps_edges(self) -> None:
        starts = _window_start_grid(total_samples=30000, window_samples=6000, windows_per_chunk=5)

        self.assertEqual(starts[0], 0)
        self.assertEqual(starts[-1], 24000)
        self.assertGreaterEqual(len(starts), 5)


if __name__ == "__main__":
    unittest.main()
