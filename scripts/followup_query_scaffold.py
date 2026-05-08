#!/usr/bin/env python3
"""Generate structured FOLLOWUP query variants.

Usage:
  python3 scripts/followup_query_scaffold.py --event "Red Sea shipping" --actor "insurers" --timeframe "2026-05" --consequence "insurance rates"
"""

import argparse
import json


def build_queries(event: str, actor: str, timeframe: str, consequence: str):
    return {
        "bluesky": [
            f"site:bsky.app {event} {actor} {timeframe} {consequence}",
            f"site:bsky.app {event} update {timeframe} {consequence}",
            f"site:bsky.app {actor} {event} {timeframe} policy operations",
        ],
        "polymarket": [
            f"Polymarket {event} {actor} {timeframe}",
            f"Polymarket {event} odds {timeframe} {consequence}",
            f"Polymarket {consequence} probability {timeframe}",
        ],
        "crosscheck": [
            f"{event} official update {timeframe}",
            f"{event} primary source data {timeframe} {consequence}",
        ],
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--event", required=True)
    p.add_argument("--actor", required=True)
    p.add_argument("--timeframe", required=True)
    p.add_argument("--consequence", required=True)
    args = p.parse_args()
    print(json.dumps(build_queries(args.event, args.actor, args.timeframe, args.consequence), indent=2))


if __name__ == "__main__":
    main()
