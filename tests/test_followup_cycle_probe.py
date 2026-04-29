import json
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "followup_cycle_probe.py"


class FollowupCycleProbeTests(unittest.TestCase):
    def test_enforce_minimums_fails_when_queries_missing(self):
        cmd = [
            "python3",
            str(SCRIPT),
            "--enforce-followup-minimums",
            "--bluesky-query",
            "q1",
            "--poly-term",
            "p1",
        ]
        p = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(p.returncode, 2)
        self.assertIn("FOLLOWUP requires at least 5 Bluesky queries", p.stderr)

    def test_out_writes_json_payload(self):
        with tempfile.TemporaryDirectory() as td:
            out_path = Path(td) / "probe.json"
            cmd = [
                "python3",
                str(SCRIPT),
                "--bluesky-query",
                "a",
                "--bluesky-query",
                "b",
                "--poly-term",
                "oil",
                "--out",
                str(out_path),
            ]
            p = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(p.returncode, 0)
            self.assertTrue(out_path.exists())
            parsed = json.loads(out_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["minimums"]["bluesky_queries"], 2)
            self.assertEqual(parsed["minimums"]["polymarket_queries"], 1)


if __name__ == "__main__":
    unittest.main()
