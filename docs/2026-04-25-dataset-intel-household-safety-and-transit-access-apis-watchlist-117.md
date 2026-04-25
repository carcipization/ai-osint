# Datasets: household safety and transit access APIs (watchlist 117)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-04-25-dataset-intel-household-safety-and-transit-access-apis-watchlist-117.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-04-25-dataset-intel-household-safety-and-transit-access-apis-watchlist-117.md)

**Dateline:** 2026-04-25 14:24 UTC

This DATASETS cycle adds five net-new, direct-access API/data surfaces focused on broad non-specialist consequence areas: commute reliability, household safety recalls, neighborhood safety conditions, and disaster-response visibility.

## Added datasets (5)

1. [National Transit Database Complete Monthly Ridership (adjusted/estimated)](https://www.transit.dot.gov/ntd/data-product/monthly-module-adjusted-data-release)
2. [openFDA Food Enforcement API](https://api.fda.gov/food/enforcement.json)
3. [openFDA Drug Enforcement API](https://api.fda.gov/drug/enforcement.json)
4. [UK Police Data API](https://data.police.uk/docs/)
5. [OpenFEMA API](https://www.fema.gov/about/openfema/api)

## Why these matter now

- **Mobility access decisions:** NTD monthly ridership gives a nationally comparable transit-demand and service-pressure denominator for checking whether local commute strain is isolated or broad.
- **Household product/medicine safety:** openFDA food and drug enforcement feeds provide machine-readable recall/enforcement updates that can change consumer, clinic, and pharmacy decisions quickly.
- **Neighborhood-level safety context:** UK Police API adds street-level incident and outcome structure for rapid local safety trend checks beyond U.S.-only coverage.
- **Disaster operations transparency:** OpenFEMA API improves direct pull access across declarations, assistance, and mitigation entities, shortening evidence-to-publication latency during active hazard cycles.

## Consequence-first screening notes

- All five additions were checked as **net-new** by URL overlap against `docs/datasets-catalog.md` during this run.
- Selection favored direct API/query surfaces with practical household/public-service consequence rather than metadata-only catalogs.
- Cross-domain mix in this batch reduces over-concentration in a single source family and improves candidate breadth for future STORY cycles.
