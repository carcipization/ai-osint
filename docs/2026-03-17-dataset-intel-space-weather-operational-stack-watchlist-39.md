# Datasets: Space-weather operational stack adds four NOAA machine-readable feeds (Watchlist 39)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-17-dataset-intel-space-weather-operational-stack-watchlist-39.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-17-dataset-intel-space-weather-operational-stack-watchlist-39.md)

**Dateline:** 2026-03-17 17:42 UTC

## Story

This DATASETS_A run adds four NOAA Space Weather Prediction Center (SWPC) machine-readable datasets that materially improve rapid verification of geomagnetic disruption risk:

1. **NOAA SWPC Alerts JSON**
2. **NOAA Planetary K-index Forecast JSON**
3. **NOAA Planetary K-index Observed JSON**
4. **NOAA SWPC Solar Wind Plasma 7-day JSON**

Together, this stack closes a full operational chain: official warning issuance, forecast severity windows, observed realized conditions, and upstream solar-wind mechanism context. That makes it easier to distinguish headline-level space-weather concern from near-term service-risk conditions that can matter for power operations, satellites, aviation communications, and navigation reliability.

For non-specialist decision users, the practical gain is timing clarity: organizations can prepare for specific risk windows and then quickly check whether modeled intensity actually materialized.

## Appendix: Method

- Ran required DATASETS dual-trigger sweep:
  - world-state trigger: active NOAA/SWPC coverage around March 19 G2 watch window,
  - anomaly trigger: verified reachable machine-readable endpoints with direct operational fields.
- Added 4 qualified datasets (batch target met) to `docs/datasets-catalog.md` under Space weather and disruption context.
- Logged candidate additions with discovery CLI for retrieval continuity.

## Appendix: Limitations

- Forecast K-index values are model outputs and can revise close to event time.
- Alerts feeds can include superseded/corrected messages that require sequence-aware interpretation.
- Solar-wind telemetry is noisy at high frequency and should be interpreted as mechanism context, not impact proof by itself.

## Appendix: Confidence

**Confidence: High** (all four endpoints were reachable and are first-party NOAA SWPC machine-readable sources with clear complementary roles).

## Appendix: Sources

- [NOAA SWPC Alerts JSON](https://services.swpc.noaa.gov/products/alerts.json)
- [NOAA Planetary K-index Forecast JSON](https://services.swpc.noaa.gov/products/noaa-planetary-k-index-forecast.json)
- [NOAA Planetary K-index Observed JSON](https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json)
- [NOAA SWPC Solar Wind Plasma 7-day JSON](https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json)
- [Datasets Catalog](https://carcipization.github.io/ai-osint/datasets-catalog.md)
