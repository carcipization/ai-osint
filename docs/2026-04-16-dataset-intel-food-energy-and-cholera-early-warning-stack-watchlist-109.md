# Datasets: food, energy, and cholera early-warning stack (watchlist 109)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-04-16-dataset-intel-food-energy-and-cholera-early-warning-stack-watchlist-109.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-04-16-dataset-intel-food-energy-and-cholera-early-warning-stack-watchlist-109.md)

**Dateline:** 2026-04-16 17:44 UTC

This DATASETS_B cycle adds five machine-readable datasets to improve fast monitoring of household affordability pressure (food + fuel) and outbreak-risk conditions (cholera), with direct non-specialist consequence relevance.

## Added in this run

- **[Global - Real Time Food Prices](https://data.humdata.org/dataset/global-real-time-food-prices)** — rapid commodity price updates for short-cycle food-access stress checks.
- **[WFP Global Market Monitor](https://data.humdata.org/dataset/global-market-monitor)** — monthly cross-country market stress context (prices, purchasing power, and related indicators).
- **[World Health Organization (WHO) Cholera Data](https://data.humdata.org/dataset/world-health-organization-who-cholera-data)** — cross-country cholera reporting series for outbreak acceleration tracking.
- **[Global - Real Time Energy Prices](https://data.humdata.org/dataset/global-real-time-energy-prices)** — near-operational energy/fuel price signals for transport and utility cost-pressure monitoring.
- **[Central America - Fuel Prices](https://data.humdata.org/dataset/central-america-fuel-prices)** — regional fuel-cost tracking for mobility and supply-chain pass-through risk checks.

## Why this stack matters

- **Broad household consequence:** food and fuel inflation pressures are immediately decision-relevant for families, local operators, and aid planning.
- **Cross-domain chain value:** pairing food and energy pricing with cholera outbreak reporting helps test whether affordability stress is co-moving with public-health risk in vulnerable settings.
- **Operational cadence fit:** all five sources are machine-readable and suitable for repeated anomaly scans, baseline comparisons, and follow-up story seeding.

## Practical use pattern

1. Pull latest food and energy series by country/market and compare against 30/90-day baselines.
2. Flag places where both food and fuel costs are rising in the same window.
3. Overlay WHO cholera updates to test whether rising household stress and outbreak activity are co-occurring.
4. Escalate only where cross-source movement is persistent and decision consequences are concrete.

## Caveats

- Country and market coverage differ across WFP/WHO series, so gaps should be treated as missingness, not absence of risk.
- “Real-time” feeds may still include publication lag and occasional backfill revisions.
- Cholera surveillance completeness and reporting delay vary by national reporting systems.

## Appendix: Sources

- HDX dataset pages linked above (WFP and WHO sources).