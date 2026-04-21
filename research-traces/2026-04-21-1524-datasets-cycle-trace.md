# DATASETS Cadence Trace — 2026-04-21 14:24 UTC

## Run context
- Slot: DATASETS
- User/target: Jon (5694918526)
- Reuters: not used
- Goal: add 3–10 datasets (batch-first)

## Discovery and overlap pass
Candidate pool focused on direct-access APIs with broad non-specialist consequences (service reliability, household costs, weather-linked disruption context).

Selected (URL overlap status against `docs/datasets-catalog.md`):
1. USDA ERS Data APIs (`https://www.ers.usda.gov/developer/data-apis`) — net-new
2. Open-Meteo API (`https://open-meteo.com/en/docs`) — net-new
3. Chicago 311 Service Requests (`https://data.cityofchicago.org/Service-Requests/311-Service-Requests/v6vf-nfxy`) — net-new
4. MyLA311 Service Request Data (2016 to Present) (`https://data.lacity.org/A-Well-Run-City/MyLA311-Service-Request-Data-2016-to-Present/rq3b-xjk8`) — net-new

Deferred/rejected examples:
- NYC 311 2020-present endpoint variant: adjacent to already cataloged NYC 311 entry; deprioritized for breadth.
- FAA/NHTSA/BTS/NREL repeats: already added in previous cycle; duplicate risk.

## Consequence-first rationale
- **Household-facing municipal services:** 311 streams surface practical service access friction before slower official summaries.
- **Food spending pressure:** ERS APIs strengthen ability to map inflation and supply stress into household budget impact pathways.
- **Weather amplification context:** Open-Meteo provides rapid baseline/context for disruption interpretation across transport/utilities/service demand.

## Catalog updates
- Added 4 entries across domains:
  - Humanitarian/hazard context: +1 (Open-Meteo)
  - Economy/governance/structural risk: +1 (USDA ERS Data APIs)
  - Domestic public safety / local operations: +2 (Chicago 311, MyLA311)
- Updated catalog metadata count: 155 -> 159
- Updated dateline to current run UTC.

## Publication artifact
- New DATASETS post:
  - `docs/2026-04-21-dataset-intel-urban-service-friction-and-household-consequence-signals-watchlist-114.md`
- Required top links + UTC dateline included.
