# DATASETS_A trace — 2026-04-12 (watchlist 104)

## Run context
- Slot: DATASETS_A
- UTC window: 2026-04-12 09:40–09:50 UTC
- Reuters usage: none
- Objective: datasets-only run, add 3–10 qualified datasets

## Discovery and overlap pass
Scanned Data.gov package search results emphasizing emergency-service load, public safety dispatch, and short-cycle respiratory burden.

Selected (net-new vs current catalog):
1. Seattle Real Time Fire 911 Calls — net-new
2. LAPD Calls for Service 2024 to Present — net-new
3. Law Enforcement Dispatched Calls for Service: Real-Time (SF) — net-new
4. Respiratory Virus Hospital Admissions Over Time (SF) — net-new

Skipped examples (reason):
- Law Enforcement Dispatched Calls for Service: Closed — adjacent to selected real-time SF feed; lower immediacy for this cycle.
- Archived/retired respiratory dashboard variants — lower freshness/reliability than active admissions feed.
- Narrow administrative/property inventory feeds with weak immediate consequence signal for this slot.

## Consequence screen (non-specialist)
All selected datasets passed consequence-first checks:
- clear household/community safety or care-load relevance,
- practical decision utility for operators/residents,
- direct raw data access via Data.gov-linked resources.

## Added artifacts
- Catalog updated: `docs/datasets-catalog.md`
- Publication created: `docs/2026-04-12-dataset-intel-real-time-urban-emergency-demand-stack-watchlist-104.md`

## Blocked/error fetch log
- None (no hard endpoint failures during selection checks).
