#!/usr/bin/env python3
"""Run one-off AI-OSINT slot jobs without touching cadence state.

This helper creates an ephemeral one-shot OpenClaw cron job that runs
independently of the cadence job (.cron_checkpoint_mode.txt is never read/written).
"""

from __future__ import annotations

import argparse
import json
import shlex
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEFAULT_TO = "5694918526"

SLOT_MESSAGES: dict[str, str] = {
    "STORY": """Run a ONE-OFF STORY task for AI-OSINT. This is out-of-cadence and must not modify cadence state.

Scope:
- Repo: /home/pi/.openclaw/workspace/ai-osint
- Do NOT read/write /home/pi/.openclaw/workspace/ai-osint/.cron_checkpoint_mode.txt
- This run is independent of scheduled slot rotation

Required workflow:
1) git fetch origin && git pull --rebase origin main
2) Produce one NEW story (not follow-up)
3) Enforce novelty gate: topic must not be covered in docs/ within last 14 days
4) Publish Markdown + HTML in docs/
5) Dateline format: **Dateline:** YYYY-MM-DD HH:MM UTC
6) Include source links and limitations
7) Commit + push (rebase/retry up to 2x)
8) Verify GitHub Pages build succeeded for latest commit
9) Send concise Telegram summary to 5694918526 with links + one-line why it matters

If no publishable new story survives verification, send a concise no-publish summary with candidates checked + rejection reasons.""",
    "DATASETS": """Run a ONE-OFF DATASETS task for AI-OSINT. This is out-of-cadence and must not modify cadence state.

Scope:
- Repo: /home/pi/.openclaw/workspace/ai-osint
- Do NOT read/write /home/pi/.openclaw/workspace/ai-osint/.cron_checkpoint_mode.txt
- This run is independent of scheduled slot rotation

Required workflow:
1) git fetch origin && git pull --rebase origin main
2) Add at least one genuinely NEW dataset source/stream to docs/datasets-catalog.md
3) Include: what it tracks, why it matters, caveats, source links
4) Rebuild docs HTML if needed
5) Dateline format: **Dateline:** YYYY-MM-DD HH:MM UTC
6) Commit + push (rebase/retry up to 2x)
7) Verify GitHub Pages build succeeded for latest commit
8) Send concise Telegram summary to 5694918526 with what was added and why it matters

If no high-quality candidate qualifies, send a concise no-add summary with candidates checked + rejection reasons.""",
}


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True, check=check)


def build_command(slot: str, to: str, timeout_seconds: int) -> list[str]:
    now = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    name = f"osint-oneoff-{slot.lower()}-{now}"
    return [
        "openclaw",
        "cron",
        "add",
        "--agent",
        "main",
        "--name",
        name,
        "--at",
        "5s",
        "--delete-after-run",
        "--session",
        "isolated",
        "--wake",
        "now",
        "--channel",
        "telegram",
        "--to",
        to,
        "--message",
        SLOT_MESSAGES[slot],
        "--timeout-seconds",
        str(timeout_seconds),
        "--expect-final",
        "--json",
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slot", choices=sorted(SLOT_MESSAGES.keys()))
    parser.add_argument("--to", default=DEFAULT_TO, help="Telegram chat id for summary")
    parser.add_argument("--timeout-seconds", type=int, default=1800)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    cmd = build_command(args.slot, args.to, args.timeout_seconds)
    if args.dry_run:
        print("DRY RUN")
        print(" ".join(shlex.quote(x) for x in cmd))
        return 0

    result = run(cmd)
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.stderr.strip():
        print(result.stderr.strip())

    # Best-effort parse for friendlier output in local logs.
    try:
        payload = json.loads(result.stdout)
        print(f"Queued one-off job: {payload.get('id', '<unknown>')}")
    except Exception:
        pass

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
