from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from osintctl.state import ROTATION, StatePaths, advance_slot, read_slot, write_slot


class StateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.paths = StatePaths(self.root)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_default_slot_is_story_a(self) -> None:
        self.assertEqual(read_slot(self.paths), "STORY_A")

    def test_write_syncs_legacy(self) -> None:
        write_slot(self.paths, "FOLLOWUP")
        self.assertEqual(read_slot(self.paths), "FOLLOWUP")
        self.assertEqual(self.paths.legacy_slot_file.read_text().strip(), "FOLLOWUP")

    def test_advance_rotation(self) -> None:
        write_slot(self.paths, ROTATION[-1])
        prev, cur = advance_slot(self.paths)
        self.assertEqual(prev, ROTATION[-1])
        self.assertEqual(cur, ROTATION[0])


if __name__ == "__main__":
    unittest.main()
