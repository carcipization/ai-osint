# Research trace — one-off DATASETS run

- Run type: DATASETS (one-off, out-of-cadence)
- UTC window: 2026-03-25 02:01–02:18
- Constraint check: no cadence state files read/written; no cadence schedule edits.

## Candidate/overlap pass (catalog dedup)

Checked against `docs/datasets-catalog.md` for prior inclusion and favored net-new coverage:

- USGS Water Services API — **net-new**
- BTS Airline On-Time Performance — **net-new**
- Census Household Pulse API — **net-new**
- HUD Fair Market Rents — **net-new**
- NHTSA Crash API (FARS/CRSS) — **net-new**

Skipped/held examples:
- Additional NOAA-centric feeds — held due to NOAA-specific constraint unless stronger immediate broad-consequence rationale.
- Adjacent transport feeds already represented by current aviation/mobility inventory — deprioritized for breadth.

## Importance/consequence screen

All promoted datasets passed non-specialist consequence relevance:
- cost/access/safety/service reliability/housing burden impacts are directly observable.
- each supports concrete decision utility for general readers and operators.

## Publication output

- Updated catalog entries in existing sections.
- Published dataset-intel summary post:
  - `docs/2026-03-25-datasets-public-consequence-watchlist-28.md`
