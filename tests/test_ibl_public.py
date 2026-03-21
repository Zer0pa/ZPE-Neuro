from __future__ import annotations

import unittest

from zpe_neuro.ibl_public import _trim_chunk_metadata


class IblPublicTests(unittest.TestCase):
    def test_trim_chunk_metadata_rebases_offsets_and_bounds(self) -> None:
        meta = {
            "chunk_offsets": [0, 10, 25, 60],
            "chunk_bounds": [0, 100, 250, 600],
            "n_channels": 4,
            "shape": [600, 4],
            "sha1_compressed": "abc",
            "sha1_uncompressed": "def",
        }

        trimmed, byte_start, byte_stop, sample_start, sample_stop = _trim_chunk_metadata(
            meta, chunk_index=1
        )

        self.assertEqual((byte_start, byte_stop), (10, 25))
        self.assertEqual((sample_start, sample_stop), (100, 250))
        self.assertEqual(trimmed["chunk_offsets"], [0, 15])
        self.assertEqual(trimmed["chunk_bounds"], [0, 150])
        self.assertEqual(trimmed["shape"], [150, 4])
        self.assertIsNone(trimmed["sha1_compressed"])
        self.assertIsNone(trimmed["sha1_uncompressed"])
        self.assertTrue(trimmed["chopped"])

    def test_trim_chunk_metadata_rejects_invalid_index(self) -> None:
        meta = {
            "chunk_offsets": [0, 5],
            "chunk_bounds": [0, 50],
            "n_channels": 2,
        }

        with self.assertRaises(IndexError):
            _trim_chunk_metadata(meta, chunk_index=1)


if __name__ == "__main__":
    unittest.main()
