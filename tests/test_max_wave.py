from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from zpe_neuro.max_wave import _safe_extract_zip


class SafeExtractZipTests(unittest.TestCase):
    def test_safe_extract_zip_allows_nested_member(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            archive = Path(tmpdir) / "safe.zip"
            unpack_dir = Path(tmpdir) / "out"
            with zipfile.ZipFile(archive, "w") as handle:
                handle.writestr("nested/audio.wav", b"wave")

            unpack_dir.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(archive, "r") as handle:
                _safe_extract_zip(handle, unpack_dir)

            self.assertTrue((unpack_dir / "nested" / "audio.wav").exists())

    def test_safe_extract_zip_rejects_parent_traversal(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            archive = Path(tmpdir) / "unsafe.zip"
            unpack_dir = Path(tmpdir) / "out"
            with zipfile.ZipFile(archive, "w") as handle:
                handle.writestr("../escape.wav", b"wave")

            unpack_dir.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(archive, "r") as handle:
                with self.assertRaisesRegex(RuntimeError, "ZIP_PATH_TRAVERSAL"):
                    _safe_extract_zip(handle, unpack_dir)

    def test_safe_extract_zip_rejects_backslash_parent_traversal(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            archive = Path(tmpdir) / "unsafe-backslash.zip"
            unpack_dir = Path(tmpdir) / "out"
            with zipfile.ZipFile(archive, "w") as handle:
                handle.writestr("..\\escape.wav", b"wave")

            unpack_dir.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(archive, "r") as handle:
                with self.assertRaisesRegex(RuntimeError, "ZIP_PATH_TRAVERSAL"):
                    _safe_extract_zip(handle, unpack_dir)


if __name__ == "__main__":
    unittest.main()
