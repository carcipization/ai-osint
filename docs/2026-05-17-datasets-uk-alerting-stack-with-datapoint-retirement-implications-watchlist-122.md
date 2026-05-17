# Datasets: UK alerting stack with DataPoint retirement implications (watchlist 122)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-05-17-datasets-uk-alerting-stack-with-datapoint-retirement-implications-watchlist-122.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-05-17-datasets-uk-alerting-stack-with-datapoint-retirement-implications-watchlist-122.md)


**Dateline:** 2026-05-17

This cadence run verifies that UK operational alerting inputs remain available for outbreaks and flood response, while confirming a live dependency risk from Met Office DataPoint decommissioning.

## What changed in this cadence window

- UKHSA Outbreaks page remains active and explicitly lists a measles stream with weekly updates.
- Environment Agency flood-monitoring API continues to document near-real-time warning and hydrology data delivery.
- Met Office DataPoint endpoint still returns a decommissioned status notice, indicating legacy clients must migrate.

## Verification notes

1. UKHSA outbreaks surface provides topic-level monitoring entry points suitable for cadence tracking.
2. EA API reference confirms core objects (warnings, areas, measurements, stations) and variable transfer frequency.
3. Met Office notice is unambiguous about DataPoint retirement status.

## Caveats

- UKHSA web surfaces are not a substitute for pinned endpoint-level schemas in production pipelines.
- EA data latency can increase outside heightened-risk windows.
- DataPoint retirement notice does not include one-to-one field mapping for older integrations.

## Bottom line

Publication outcome: **UK alerting stack is still operational for outbreak and flood monitoring, but weather-ingestion migration away from DataPoint remains an active technical requirement.**

## Sources

1. https://ukhsa-dashboard.data.gov.uk/outbreaks
2. https://environment.data.gov.uk/flood-monitoring/doc/reference
3. https://www.metoffice.gov.uk/services/data/datapoint
