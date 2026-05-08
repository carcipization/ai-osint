#!/usr/bin/env python3
"""Detect consecutive no-publish cadence traces.

Usage:
  python scripts/check_publish_drought.py [--threshold 6]

Exit codes:
  0 => below threshold
  10 => drought threshold met/exceeded
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re

TRACE_DIR = Path("research-traces")
NO_PUB_RE = re.compile(r"no-publish", re.I)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--threshold", type=int, default=6)
    args = ap.parse_args()

    traces = sorted(TRACE_DIR.glob("*.md"), key=lambda p: p.name)
    streak = 0
    for p in reversed(traces):
        if NO_PUB_RE.search(p.name):
            streak += 1
            continue
        break

    print(f"consecutive_no_publish={streak}")
    print(f"threshold={args.threshold}")
    if streak >= args.threshold:
        print("DROUGHT_BREAKER_REQUIRED=1")
        return 10
    print("DROUGHT_BREAKER_REQUIRED=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
