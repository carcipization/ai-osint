# DATASETS_A trace — 2026-04-09

- Slot: DATASETS_A
- UTC run window: 2026-04-09 09:40–09:58

## Situational-awareness sweep (short)

Consequence classes prioritized this cycle:
- Urban mobility reliability and service-access risk
- Public-safety trend baselines with operational decision utility
- Governance/accountability signals with non-specialist relevance

## Discovery/anomaly sweep

Bulk intake command:
- `python3 scripts/bulk_dataset_intake.py --pages 2 --rows 200 --top 80`

Artifacts:
- `research-traces/20260409T094008Z-bulk-dataset-intake.json`
- `research-traces/20260409T094008Z-bulk-dataset-intake.csv`
- `research-traces/20260409T094008Z-bulk-dataset-intake-summary.md`

Blocked/error item:
- Source: HDX CKAN package_search
- URL: `https://data.humdata.org/api/3/action/package_search?rows=200&start=0`
- Error: `HTTP 406 Not Acceptable`
- UTC timestamp: `2026-04-09 09:40`
- Retry outcome: failed (same 406); run proceeded using qualifying non-HDX candidates.

## Overlap pass and selection

Selected 5 net-new datasets (target 3–10 met):
1. Corporations and Other Entities: All Filings
2. MTA Subway Major Incidents: Beginning 2015
3. MTA Bus Speeds: Beginning 2015
4. Index Crimes by County and Agency: Beginning 1990
5. APD Arrests

Rejected/held examples:
- Already in catalog: FOIA Logs, Skilled Nursing Facility All Owners, QCEW, Recalls Data.
- Low consequence/noise for this cycle: lottery datasets, narrow recreational/admin-only feeds.

## Output decision

- Published dataset-intel post:
  - `docs/2026-04-09-dataset-intel-transparency-mobility-and-local-safety-signals-watchlist-92.md`
- Updated catalog:
  - `docs/datasets-catalog.md` (5 new entries)
