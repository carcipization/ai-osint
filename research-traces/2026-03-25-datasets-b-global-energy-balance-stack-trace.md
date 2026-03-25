# DATASETS_B trace — 2026-03-25 global energy-balance + stocks stack

UTC window: 2026-03-25 01:39–01:43

## Situational/anomaly sweep
- Active context: repeated policy and conflict-driven oil volatility in recent runs created need for stronger physical-balance and inventory mechanism coverage.
- Gap found: catalog had strong short-cycle U.S. petroleum APIs from prior run but thinner global-balance and forecast-risk layering.

## Selection rationale
Chosen additions prioritize broad non-specialist consequence (fuel/transport costs) and mechanism completeness:
1. Inventory pressure (stocks)
2. Upstream structural capacity (crude reserves/production)
3. Global denominator (international all-energy + natural gas)
4. Integrated petroleum context (petroleum/liquids hub)
5. Forward U.S. price-risk framing (STEO U.S. prices API)

## Added datasets (6)
1. https://catalog.data.gov/dataset/petroleum-data-stocks-application-programming-interface-api
2. https://catalog.data.gov/dataset/petroleum-data-crude-reserves-and-production-application-programming-interface-api
3. https://catalog.data.gov/dataset/international-energy-data-all-energy
4. https://catalog.data.gov/dataset/international-energy-data-natural-gas
5. https://catalog.data.gov/dataset/petroleum-other-liquids-data-and-statistics
6. https://catalog.data.gov/dataset/short-term-energy-outlook-u-s-prices-application-programming-interface-api

## Misses/deprioritized
- NOAA-focused candidates deprioritized under anti-convenience and domain-rotation constraints for this slot.
- Duplicate petroleum submodules already added in prior DATASETS_A run were skipped.

## Blocked/error fetch log
- None in this run.

## Outputs
- Updated `docs/datasets-catalog.md` metadata and Energy, trade, and maritime entries.
- Published dataset-intel post: `2026-03-25-dataset-intel-global-energy-balance-and-stocks-stack-watchlist-53.md`.
