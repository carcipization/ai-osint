# Datasets: UK operational monitoring refresh (watchlist 121)

**Dateline:** 2026-05-17

This cadence run refreshes UK-focused operational data surfaces used for public-risk monitoring across health and flooding signals, while noting a material weather-data service transition.

## What changed in this cadence window

- UKHSA dashboard confirms active machine-readable public health topic surfaces (including outbreaks and vaccination coverage sections).
- Environment Agency flood-monitoring API reference confirms near-real-time warning, level, and flow feeds with open-licence access.
- Met Office confirms the legacy DataPoint service is decommissioned, requiring migration to newer data-service pathways.

## Verification notes

1. UKHSA dashboard pages enumerate health-topic data products and update contexts.
2. EA API reference documents frequency and coverage for flood alerts, areas, and measurements.
3. Met Office DataPoint endpoint explicitly states retirement status.

## Caveats

- Dashboard pages are partly navigational; ingestion pipelines should pin endpoint-level contracts where available.
- Flood telemetry transfer frequency varies by site and risk state.
- DataPoint retirement notices do not by themselves provide complete replacement schema mapping.

## Bottom line

Publication outcome: **UK monitoring stack remains usable for health + flood signals, with a confirmed weather-data migration dependency due to DataPoint decommissioning.**

## Sources

1. https://ukhsa-dashboard.data.gov.uk/
2. https://environment.data.gov.uk/flood-monitoring/doc/reference
3. https://www.metoffice.gov.uk/services/data/datapoint
