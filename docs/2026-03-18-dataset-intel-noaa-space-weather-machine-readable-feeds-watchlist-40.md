# Datasets: NOAA space-weather machine-readable feed stack adds four operational endpoints (Watchlist 40)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-18-dataset-intel-noaa-space-weather-machine-readable-feeds-watchlist-40.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-18-dataset-intel-noaa-space-weather-machine-readable-feeds-watchlist-40.md)

**Dateline:** 2026-03-18 01:42 UTC

## Story

This DATASETS_B run adds four NOAA Space Weather Prediction Center machine-readable endpoints that improve short-horizon disruption monitoring across power, satellite, aviation-communications, and navigation-reliability workflows:

1. **NOAA SWPC Alerts JSON**
2. **NOAA Scales JSON**
3. **NOAA Solar Wind Magnetic Field 7-day JSON**
4. **NOAA Solar Wind Plasma 7-day JSON**

The reporting value is chain-complete context in one stack: alerts/watches provide official warning state, scale snapshots summarize severity posture, and solar-wind magnetic/plasma feeds provide mechanism-side evidence for whether geoeffective conditions are strengthening or weakening. That reduces reliance on static page checks and supports faster, reproducible verification during active space-weather windows.

For non-specialist decision users, this helps answer a practical question quickly: is risk posture changing now, and is the physical signal supporting a higher or lower disruption likelihood?

## Appendix: Method

- Ran DATASETS dual-trigger sweep:
  - world-state: ongoing SWPC G2 watch cycle remained active,
  - anomaly trigger: tested multiple machine-readable SWPC product endpoints for live availability and useful field structure.
- Confirmed endpoint accessibility (HTTP 200) and operationally relevant fields.
- Added 4 datasets (batch target met) under `Space weather and disruption context` in `docs/datasets-catalog.md`.

## Appendix: Limitations

- SWPC forecasts and scale probabilities can revise near event time.
- Minute-level solar-wind telemetry contains high-frequency variability and occasional gaps.
- Mechanism feeds indicate conditions, not guaranteed downstream impact magnitude.

## Appendix: Confidence

**Confidence: High** (all four datasets are first-party NOAA SWPC machine-readable endpoints and were reachable during this run).

## Appendix: Sources

- [NOAA SWPC Alerts JSON](https://services.swpc.noaa.gov/products/alerts.json)
- [NOAA Scales JSON](https://services.swpc.noaa.gov/products/noaa-scales.json)
- [NOAA Solar Wind Magnetic Field 7-day JSON](https://services.swpc.noaa.gov/products/solar-wind/mag-7-day.json)
- [NOAA Solar Wind Plasma 7-day JSON](https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json)
- [Datasets Catalog](https://carcipization.github.io/ai-osint/datasets-catalog.md)
