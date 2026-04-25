# EVOLVE fallback trace (from FOLLOWUP no-publish)

**Run UTC:** 2026-04-25 20:24 UTC
**Trigger:** FOLLOWUP cycle found no materially conclusion-changing update.

## Hypothesis

FOLLOWUP cycles repeatedly lose time on ad hoc command glue for mandatory context checks (Bluesky query list + Polymarket scans). A single helper that records query bundles and Polymarket outputs in one structured artifact should improve consistency and speed over the next 7-14 days.

## High-leverage change made (repo-level)

Added executable helper:
- `scripts/followup_cycle_probe.py`

What it does:
- Accepts repeatable `--bluesky-query` and `--poly-term` inputs.
- Runs all requested Polymarket searches via existing `scripts/polymarket_cli.py`.
- Emits normalized JSON with:
  - run UTC,
  - query strings,
  - executed Polymarket commands,
  - exit codes/results/stderr.

## Before/after checks

Before:
- FOLLOWUP mandatory context checks were manually stitched per run.
- Query capture format varied between traces.

After:
- Ran:
  - `./scripts/followup_cycle_probe.py --repo-root . --bluesky-query "site:bsky.app CDC respiratory illnesses April 2026 update" --bluesky-query "site:bsky.app FAO food price index April 2026 update" --poly-term "rsv" --poly-term "food prices" --poly-term "geomagnetic storm"`
- Output file `/tmp/followup_probe_2124.json` produced deterministic structured records and successfully executed all three Polymarket scans (all `[]`, exit code 0).

## Expected impact (7-14 day window)

- Faster, more consistent FOLLOWUP trace assembly.
- Lower risk of missing mandatory query evidence in no-publish cycles.
- Better reproducibility for audit/replay of context checks across cadence runs.
