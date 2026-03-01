#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from osintctl.prompts import cadence_prompt, oneoff_prompt
from osintctl.state import ROTATION, StatePaths, advance_slot, next_slot, read_slot, write_slot

DEFAULT_TO = "5694918526"
MAIN_CRON_JOB_ID = "68699ee6-9367-450c-a29c-d92b77c89539"


def _run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True, check=check)


def cmd_state(args: argparse.Namespace) -> int:
    paths = StatePaths(ROOT)
    if args.action == "show":
        cur = read_slot(paths)
        print(json.dumps({
            "currentSlot": cur,
            "nextSlot": next_slot(cur),
            "rotation": list(ROTATION),
            "stateFile": str(paths.cadence_slot_file),
            "legacyFile": str(paths.legacy_slot_file),
        }, indent=2))
        return 0

    if args.action == "set-slot":
        cur = write_slot(paths, args.slot)
        print(cur)
        return 0

    if args.action == "advance":
        cur, nxt = advance_slot(paths)
        print(json.dumps({"previous": cur, "current": nxt}, indent=2))
        return 0

    raise SystemExit("unknown state action")


def cmd_prompt(args: argparse.Namespace) -> int:
    paths = StatePaths(ROOT)

    if args.mode == "cadence":
        slot = args.slot or read_slot(paths)
        print(cadence_prompt(slot=slot, to=args.to, state_file=str(paths.cadence_slot_file)))
        return 0

    if args.mode == "oneoff":
        print(oneoff_prompt(slot=args.slot, to=args.to))
        return 0

    raise SystemExit("unknown prompt mode")


def cmd_enqueue_oneoff(args: argparse.Namespace) -> int:
    now = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    name = f"osint-oneoff-{args.slot.lower()}-{now}"
    msg = oneoff_prompt(slot=args.slot, to=args.to)
    cmd = [
        "openclaw", "cron", "add",
        "--agent", "main",
        "--name", name,
        "--at", "5s",
        "--delete-after-run",
        "--session", "isolated",
        "--wake", "now",
        "--channel", "telegram",
        "--to", args.to,
        "--message", msg,
        "--timeout-seconds", str(args.timeout_seconds),
        "--expect-final",
        "--json",
    ]
    if args.dry_run:
        print(" ".join(shlex.quote(x) for x in cmd))
        return 0
    out = _run(cmd)
    print(out.stdout.strip())
    return 0


def cmd_sync_cadence_cron(args: argparse.Namespace) -> int:
    bridge = "\n".join([
        "Run this cadence turn via repo CLI (code-first control):",
        "1) cd /home/pi/.openclaw/workspace/ai-osint",
        "2) python3 scripts/osintctl_cli.py prompt cadence > /tmp/osint_cadence_prompt.txt",
        "3) Follow /tmp/osint_cadence_prompt.txt exactly for this run",
        "4) After completing work and reporting to Telegram, advance slot: python3 scripts/osintctl_cli.py state advance",
    ])
    cmd = [
        "openclaw", "cron", "edit", args.job_id,
        "--name", "osint-mix-3h",
        "--message", bridge,
    ]
    if args.dry_run:
        print(" ".join(shlex.quote(x) for x in cmd))
        return 0
    out = _run(cmd)
    print(out.stdout.strip())
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="AI-OSINT control CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("state")
    sp_sub = sp.add_subparsers(dest="action", required=True)
    sp_sub.add_parser("show")
    setp = sp_sub.add_parser("set-slot")
    setp.add_argument("slot", choices=list(ROTATION))
    sp_sub.add_parser("advance")
    sp.set_defaults(func=cmd_state)

    pp = sub.add_parser("prompt")
    pp.add_argument("mode", choices=["cadence", "oneoff"])
    pp.add_argument("--slot", default=None)
    pp.add_argument("--to", default=DEFAULT_TO)
    pp.set_defaults(func=cmd_prompt)

    ep = sub.add_parser("enqueue-oneoff")
    ep.add_argument("slot", choices=["STORY", "DATASETS"])
    ep.add_argument("--to", default=DEFAULT_TO)
    ep.add_argument("--timeout-seconds", type=int, default=1800)
    ep.add_argument("--dry-run", action="store_true")
    ep.set_defaults(func=cmd_enqueue_oneoff)

    cp = sub.add_parser("sync-cadence-cron")
    cp.add_argument("--job-id", default=MAIN_CRON_JOB_ID)
    cp.add_argument("--to", default=DEFAULT_TO)
    cp.add_argument("--dry-run", action="store_true")
    cp.set_defaults(func=cmd_sync_cadence_cron)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
