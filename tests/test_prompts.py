from __future__ import annotations

import unittest

from osintctl.prompts import cadence_prompt, oneoff_prompt


class PromptTests(unittest.TestCase):
    def test_cadence_prompt_contains_slot_and_state(self) -> None:
        text = cadence_prompt(slot="DATASETS_A", to="123", state_file="/tmp/state.txt")
        self.assertIn("Current slot for this run: DATASETS_A", text)
        self.assertIn("Slot source of truth: /tmp/state.txt", text)

    def test_oneoff_prompt_out_of_cadence(self) -> None:
        text = oneoff_prompt(slot="STORY", to="123")
        self.assertIn("out-of-cadence", text.lower())
        self.assertIn("Do NOT read/write cadence state files", text)


if __name__ == "__main__":
    unittest.main()
