# DATASETS_A trace — 2026-03-19 17:39 UTC

## Situational-awareness sweep (dual-trigger)

World-state queries run:
1. `site:catalog.data.gov dataset FEMA disaster declarations summaries`
2. `site:catalog.data.gov openfema public assistance funded projects details`
3. `site:catalog.data.gov openfema individuals and households program valid registrations`
4. `site:catalog.data.gov openfema housing assistance owners renters`
5. `site:catalog.data.gov emergency rental assistance program data`

Anomaly-oriented checks:
- Prioritized datasets with direct consequence chain coverage (trigger -> household demand -> recovery finance -> mitigation investment).
- Rejected local-only eviction datasets in this run due weaker national comparability and higher policy/schema heterogeneity.

## Selected additions (4)

1. Disaster Declarations Summaries (FEMA)
2. Individuals and Households Program (IHP) – Valid Registrations (FEMA)
3. Public Assistance Funded Projects Details (FEMA)
4. Hazard Mitigation Assistance Projects (FEMA)

Reason for selection:
- Broad non-specialist consequence relevance (housing displacement, infrastructure recovery, disaster assistance pace).
- Decision-useful for local operators and households.
- Strong chain completeness when used together.

## Endpoint verification snapshots

- Disaster Declarations Summaries — reachable (HTTP 200); metadata updated Jun 7, 2025.
- IHP Valid Registrations — reachable (HTTP 200); metadata updated Jun 7, 2025.
- Public Assistance Funded Projects Details — reachable (HTTP 200); metadata updated Aug 11, 2025.
- Hazard Mitigation Assistance Projects — reachable (HTTP 200); metadata updated Jun 7, 2025.

## Rejections/misses

- CPI/PPI and JOLTS catalog pages were considered but deprioritized this cycle because existing catalog already has strong macro baseline coverage (BLS API + labor/cost datasets) and this run prioritized disaster-response gap filling.
- City-specific eviction datasets were not selected due limited national comparability in this slot.

## Output actions

- Added 4 datasets to `docs/datasets-catalog.md`.
- Published watchlist explainer: `2026-03-19-dataset-intel-disaster-response-and-recovery-finance-watchlist-41.md`.
