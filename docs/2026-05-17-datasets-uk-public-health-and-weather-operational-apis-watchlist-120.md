# Datasets: UK public health and weather operational APIs (watchlist 120)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-05-17-datasets-uk-public-health-and-weather-operational-apis-watchlist-120.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-05-17-datasets-uk-public-health-and-weather-operational-apis-watchlist-120.md)


**Dateline:** 2026-05-17

This cadence run publishes a fresh dataset-intel packet for UK-facing operational monitoring, focused on machine-readable feeds that can support near-real-time public-risk triage.

## Included feeds

- UKHSA data dashboard API portal (infectious disease indicators and methodology context).
- UK Met Office DataHub catalogue (weather and forecast API surfaces).
- UK Environment Agency flood-monitoring API (river/flood warning telemetry).

## Verification notes

1. All three endpoints are first-party government/public-agency domains.
2. Each source exposes structured or catalogued machine-consumable access.
3. The mix supports cross-domain checks (health + weather + hydrology) for event correlation.

## Caveats

- API products and schemas can change; consumers should pin versions where available.
- Some datasets are near-real-time while others are periodic snapshots.
- Availability, throttling, and key requirements differ by provider.

## Bottom line

Publication outcome: **new dataset watchlist entry landed** for UK operational OSINT ingestion, ready for downstream automation and anomaly scanning.

## Sources

1. [https://ukhsa-dashboard.data.gov.uk/](https://ukhsa-dashboard.data.gov.uk/)
2. [https://www.metoffice.gov.uk/services/data/datapoint](https://www.metoffice.gov.uk/services/data/datapoint)
3. [https://environment.data.gov.uk/flood-monitoring/doc/reference](https://environment.data.gov.uk/flood-monitoring/doc/reference)
