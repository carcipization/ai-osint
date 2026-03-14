# Datasets: added wildfire-smoke vulnerability, drought indices, and ED burden baselines (Watchlist 33)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-14-dataset-intel-wildfire-drought-ed-pressure-watchlist-33.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-14-dataset-intel-wildfire-drought-ed-pressure-watchlist-33.md)

**Dateline:** 2026-03-14 12:01 UTC

## Story

This DATASETS_C cycle adds three cross-domain public-risk baselines to improve fast corroboration for climate-health and service-pressure reporting:

- **Indicators of Health Vulnerability to Wildfire Smoke Exposure** (EPA)
- **United States Climate Reference Network (USCRN) Drought Indices** (NOAA)
- **Estimates of Emergency Department Visits in the United States (2016–2022)** (HHS)

These additions strengthen a practical impact chain: environmental stress (drought and wildfire smoke exposure) to likely human impact (health vulnerability and emergency-care burden). The goal is better early context in runs where broad public consequences matter more than specialist-only metrics.

For non-specialist decision users, these datasets support clearer near-term questions: where smoke exposure may hit vulnerable populations harder, whether drought stress is deepening or easing, and whether emergency-care burden signals are moving outside seasonal expectations.

## Appendix: Method

- Ran datasets-only discovery pass focused on broad consequence classes (climate hazard + public health load).
- Prioritized official/public machine-readable sources with reusable baseline value.
- Added 3 datasets (within required 3–10 range) to `docs/datasets-catalog.md`.

## Appendix: Limitations

- Wildfire smoke vulnerability indicators are contextual risk measures, not direct incident counts.
- USCRN drought indices depend on station distribution and index construction choices.
- ED visit estimates are not real-time and should be paired with higher-frequency surveillance when available.

## Appendix: Confidence

**Confidence: Moderate-High** (all three are authoritative public-source baselines; limitations are primarily interpretive and cadence-related).

## Appendix: Sources

- [Indicators of Health Vulnerability to Wildfire Smoke Exposure](https://catalog.data.gov/dataset/indicators-of-health-vulnerability-to-wildfire-smoke-exposure)
- [United States Climate Reference Network (USCRN) Drought Indices](https://catalog.data.gov/dataset/united-states-climate-reference-network-uscrn-drought-indices)
- [Estimates of Emergency Department Visits in the United States from 2016–2022](https://catalog.data.gov/dataset/estimates-of-emergency-department-visits-in-the-united-states-from-2016-2019-faa2a)
- [Datasets Catalog](https://carcipization.github.io/ai-osint/datasets-catalog.md)
