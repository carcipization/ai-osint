#!/usr/bin/env python3
"""Run slot-specific trace guards against latest private traces.

Usage:
  python3 scripts/cadence_trace_audit.py [--story PATH] [--followup PATH]

Default behavior (no explicit paths):
  - auto-detect latest STORY and FOLLOWUP traces under research-traces/
  - run corresponding guard scripts
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACE_DIR = ROOT / "research-traces"


def latest_matching(pattern: str) -> Path | None:
    files = sorted(TRACE_DIR.glob(pattern), key=lambda p: p.stat().st_mtime, reverse=True)
    return files[0] if files else None


def run_guard(script_name: str, trace_path: Path) -> tuple[int, str]:
    cmd = [sys.executable, str(ROOT / "scripts" / script_name), str(trace_path)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    output = (p.stdout or "") + (p.stderr or "")
    return p.returncode, output.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--story", type=Path)
    ap.add_argument("--followup", type=Path)
    args = ap.parse_args()

    story_path = args.story or latest_matching("*story*trace*.md") or latest_matching("*story-slot*.md")
    followup_path = args.followup or latest_matching("*followup*trace*.md") or latest_matching("*followup-slot*.md")

    checks: list[tuple[str, str, Path | None]] = [
        ("STORY", "story_trace_guard.py", story_path),
        ("FOLLOWUP", "followup_trace_guard.py", followup_path),
    ]

    overall_fail = False
    for label, guard, trace in checks:
        if trace is None:
            print(f"{label}: SKIP (no trace found)")
            continue
        code, out = run_guard(guard, trace)
        status = "PASS" if code == 0 else "FAIL"
        print(f"{label}: {status} :: {trace}")
        if out:
            print(out)
        if code != 0:
            overall_fail = True

    return 1 if overall_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
