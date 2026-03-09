from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from zpe_neuro.wave1 import _pipeline_signature


class Wave1DeterminismTests(unittest.TestCase):
    def test_signature_is_stable_for_fixed_seed(self) -> None:
        first = _pipeline_signature(20260220)
        second = _pipeline_signature(20260220)
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()

