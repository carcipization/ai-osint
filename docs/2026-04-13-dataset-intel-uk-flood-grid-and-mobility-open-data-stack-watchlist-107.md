# Datasets: UK flood, grid, and mobility open-data stack (watchlist 107)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-04-13-dataset-intel-uk-flood-grid-and-mobility-open-data-stack-watchlist-107.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-04-13-dataset-intel-uk-flood-grid-and-mobility-open-data-stack-watchlist-107.md)

**Dateline:** 2026-04-13 09:41 UTC

This DATASETS_A cycle adds four machine-readable UK datasets that improve fast consequence checks across flood exposure, coastal risk, electricity-system strain, and road-mobility pressure.

## Added in this run

- **[Environment Agency Flood Monitoring API](https://environment.data.gov.uk/flood-monitoring/doc/reference)** — open warning/alert and river-level API for England.
- **[Environment Agency Tide Gauge API](https://environment.data.gov.uk/flood-monitoring/doc/tidegauge)** — 15-minute UK coastal tide-level observations.
- **[NESO Open Data API (GB electricity system)](https://api.neso.energy/api/3/action/package_search)** — CKAN API gateway for Great Britain electricity demand/generation/system datasets.
- **[UK DfT Road Traffic Statistics API](https://roadtraffic.dft.gov.uk/api-docs)** — open road traffic counts and vehicle-mile series across Great Britain geographies.

## Why this stack matters

- **Direct household and municipal relevance:** flood and tide signals map to immediate safety, travel, and local-response decisions.
- **Cross-domain chain value:** grid-stress and road-flow datasets help test whether weather and hazard shocks are cascading into power reliability and mobility access.
- **Operational utility:** all four sources provide machine-readable access suitable for repeatable anomaly scans and baseline comparisons.

## Practical use pattern

1. Track flood warnings and gauge levels by area, then compare with prior-day/prior-week conditions.
2. Use tide gauges to monitor coastal surge persistence and validate local flood-risk context.
3. Pull NESO demand/generation/balancing series to test power-system stress during hazard windows.
4. Cross-check DfT traffic counts to see whether disruption is changing movement patterns at regional/local levels.

## Caveats

- Flood/tide data quality and timeliness vary by station and transfer intervals.
- NESO API coverage spans many datasets with differing publication cadences and definitions.
- DfT road traffic series include modeled annual estimates and count-point comparability limits.

## Appendix: Sources

- Environment Agency and UK government API/documentation pages linked above.
