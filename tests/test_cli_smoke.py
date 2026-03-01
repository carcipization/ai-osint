from __future__ import annotations

import subprocess
import unittest
from pathlib import Path


def _find_repo_root() -> Path:
    here = Path(__file__).resolve()
    for p in [here.parent, *here.parents]:
        candidate = p / "scripts" / "osintctl_cli.py"
        if candidate.exists():
            return p
    # fallback for direct local execution
    return Path("/home/pi/.openclaw/workspace/ai-osint")


ROOT = _find_repo_root()
CLI = ROOT / "scripts" / "osintctl_cli.py"


class CliSmokeTests(unittest.TestCase):
    def test_help(self) -> None:
        proc = subprocess.run(["python3", str(CLI), "--help"], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, msg=proc.stderr or proc.stdout)
        self.assertIn("AI-OSINT control CLI", proc.stdout)

    def test_oneoff_dry_run(self) -> None:
        proc = subprocess.run(
            ["python3", str(CLI), "enqueue-oneoff", "STORY", "--dry-run"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, msg=proc.stderr or proc.stdout)
        self.assertIn("openclaw cron add", proc.stdout)


if __name__ == "__main__":
    unittest.main()
