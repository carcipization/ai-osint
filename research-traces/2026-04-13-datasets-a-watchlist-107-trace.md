# DATASETS_A trace — watchlist 107 (2026-04-13)

## Run metadata
- Slot: DATASETS_A
- UTC window: 2026-04-13 09:34–09:43
- Reuters usage: none (disallowed)

## Situational-awareness sweep (dual-trigger)
- World-state trigger: flood/coastal/weather spillover risks and household utility/service impacts.
- Anomaly trigger: looked for high-cadence public datasets enabling hazard -> infrastructure -> mobility consequence checks.

## Candidate overlap classification (against datasets-catalog.md)
- Environment Agency Flood Monitoring API — **net-new**
- Environment Agency Tide Gauge API — **net-new**
- NESO Open Data API (GB electricity system) — **net-new**
- UK DfT Road Traffic Statistics API — **net-new**

Rejected/held this cycle:
- Met Office DataPoint endpoints — rejected (service decommission notice; reliability risk for active intake).

## Consequence-first rationale
- Flood + tide APIs provide direct life-safety and local operations relevance.
- NESO API adds high-utility electricity-system evidence for household/service reliability checks.
- DfT road traffic API provides broad non-specialist mobility and logistics impact visibility.

## Publication output
- docs/2026-04-13-dataset-intel-uk-flood-grid-and-mobility-open-data-stack-watchlist-107.md
- docs/datasets-catalog.md updated with 4 additions.
