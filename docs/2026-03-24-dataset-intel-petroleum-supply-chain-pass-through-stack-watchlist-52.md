# Datasets: petroleum supply-chain pass-through stack expands fuel-shock monitoring

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-24-dataset-intel-petroleum-supply-chain-pass-through-stack-watchlist-52.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-24-dataset-intel-petroleum-supply-chain-pass-through-stack-watchlist-52.md)

**Dateline:** 2026-03-24 17:39 UTC

This DATASETS_A run adds six U.S. Energy Information Administration petroleum APIs that strengthen end-to-end monitoring of how geopolitical supply disruptions move through refinery operations into household and freight fuel costs.

The stack is decision-relevant for non-specialists because it links upstream flow stress (imports/exports/movements), midstream conversion constraints (refining and processing), and downstream burden (prices plus consumption/sales). That makes it easier to separate short-term market noise from actionable consumer-cost pressure.

## Added datasets (6)
- Petroleum Data Application Programming Interface (API)  
  [https://catalog.data.gov/dataset/petroleum-data-application-programming-interface-api](https://catalog.data.gov/dataset/petroleum-data-application-programming-interface-api)
- Petroleum Data: Summary Application Programming Interface (API)  
  [https://catalog.data.gov/dataset/petroleum-data-summary-application-programming-interface-api](https://catalog.data.gov/dataset/petroleum-data-summary-application-programming-interface-api)
- Petroleum Data: Prices Application Programming Interface (API)  
  [https://catalog.data.gov/dataset/petroleum-data-prices-application-programming-interface-api](https://catalog.data.gov/dataset/petroleum-data-prices-application-programming-interface-api)
- Petroleum Data: Refining and Processing Application Programming Interface (API)  
  [https://catalog.data.gov/dataset/petroleum-data-refining-and-processing-application-programming-interface-api](https://catalog.data.gov/dataset/petroleum-data-refining-and-processing-application-programming-interface-api)
- Petroleum Data: Imports/Exports and Movements Application Programming Interface (API)  
  [https://catalog.data.gov/dataset/petroleum-data-imports-exports-and-movements-application-programming-interface-api](https://catalog.data.gov/dataset/petroleum-data-imports-exports-and-movements-application-programming-interface-api)
- Petroleum Data: Consumption/Sales Application Programming Interface (API)  
  [https://catalog.data.gov/dataset/petroleum-data-consumption-sales-application-programming-interface-api](https://catalog.data.gov/dataset/petroleum-data-consumption-sales-application-programming-interface-api)

## Why this stack matters now
- **Households:** improves early warning on gasoline/diesel pass-through risk to transport and food prices.
- **Operators:** helps logistics and procurement teams distinguish true physical shortage from pricing volatility.
- **Policy/public-service users:** provides tighter evidence for fuel-pressure communication and contingency planning.

## Quick-use pattern
1. Use **Imports/Exports and Movements** plus **Summary** to identify regional supply strain.
2. Test mechanism with **Refining and Processing** (utilization/yield bottlenecks).
3. Confirm consumer burden trajectory using **Prices** and **Consumption/Sales**.

## Caveats
- Most series require EIA API key access and can revise after initial release windows.
- Weekly signals can be noisy; strongest conclusions should triangulate across at least two series families.
- Product definitions and geographic groupings can differ by table, so comparison keys must be explicit.

## Sources
- U.S. Data.gov EIA petroleum API listings (links above)
- EIA Open Data portal context: [https://www.eia.gov/opendata/](https://www.eia.gov/opendata/)
