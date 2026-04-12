# DATASETS_B trace — 2026-04-12 (watchlist 106)

## Run context
- Slot: DATASETS_B
- UTC window: 2026-04-12 17:40–17:45 UTC
- Reuters usage: none
- Requirement: datasets-only, add 3–10 datasets

## Discovery summary
Scanned Data.gov for fresh machine-readable datasets with direct non-specialist consequence relevance in public safety operations and household exposure risk.

## Selected additions (all net-new)
1. Call Data (Seattle police call-for-service)
2. Law Enforcement Dispatched Calls for Service: Closed (San Francisco)
3. Beach Water Quality Monitoring (San Francisco)
4. Beach Water Quality - Automated Sensors (Chicago)

## Overlap/skip notes
- Retained distinction between SF real-time vs closed dispatch feeds: real-time supports rapid detection; closed supports stable trend baselines.
- Skipped lower-relevance administrative inventories and non-operational/archived feeds in this slot.

## Consequence screen
All four selected datasets passed:
- direct household/public-safety or health-exposure relevance,
- practical decision utility,
- direct raw-access resources (CSV/JSON/XML/RDF).

## Artifacts
- Updated: `docs/datasets-catalog.md`
- Published: `docs/2026-04-12-dataset-intel-coastal-water-and-dispatch-operations-stack-watchlist-106.md`

## Blocked/errors
- None hard-fail during source checks.
