#!/usr/bin/env python3
"""Backward-compatible wrapper for one-off slot runs.

Use scripts/osintctl.py enqueue-oneoff instead.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "osintctl_cli.py"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slot", choices=["STORY", "DATASETS"])
    parser.add_argument("--to", default="5694918526")
    parser.add_argument("--timeout-seconds", type=int, default=1800)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    cmd = [
        "python3",
        str(CLI),
        "enqueue-oneoff",
        args.slot,
        "--to",
        args.to,
        "--timeout-seconds",
        str(args.timeout_seconds),
    ]
    if args.dry_run:
        cmd.append("--dry-run")

    proc = subprocess.run(cmd)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
