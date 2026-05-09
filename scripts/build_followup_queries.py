#!/usr/bin/env python3
from __future__ import annotations

import argparse
from typing import List


def build_queries(event: str, actor: str, timeframe: str, consequence: str) -> List[str]:
    freshness = "latest OR new OR update"
    consequence_tail = f"{consequence} cost OR access OR safety OR services"
    return [
        f"site:bsky.app {event} {actor} {timeframe} {consequence}",
        f"site:bsky.app {event} {actor} {freshness} {timeframe} {consequence}",
        f"site:bsky.app {event} update {timeframe} {consequence}",
        f"site:bsky.app {actor} {event} {timeframe} {consequence_tail}",
        f"site:bsky.app {event} location update {timeframe} {consequence}",
        f"Polymarket {event} {actor} {timeframe}",
        f"{event} official update {timeframe}",
        f"{event} {actor} official bulletin {timeframe} {consequence}",
    ]


def main() -> int:
    p = argparse.ArgumentParser(description="Generate structured FOLLOWUP queries")
    p.add_argument("--event", required=True)
    p.add_argument("--actor", required=True)
    p.add_argument("--timeframe", required=True)
    p.add_argument("--consequence", required=True)
    args = p.parse_args()

    for q in build_queries(args.event, args.actor, args.timeframe, args.consequence):
        print(q)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
