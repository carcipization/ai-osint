# Datasets: UK operational early-warning mix (watchlist 124)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-05-18-datasets-uk-operational-early-warning-mix-watchlist-124.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-05-18-datasets-uk-operational-early-warning-mix-watchlist-124.md)

**Dateline:** 2026-05-18

This dataset run adds a UK early-warning bundle spanning healthcare pressure, flood operations, and weather-data dependency risk.

## Added datasets (3)

1. **ONS inflation and price indices (UK)**  
   URL: [https://www.ons.gov.uk/economy/inflationandpriceindices](https://www.ons.gov.uk/economy/inflationandpriceindices)  
   Why it matters: tracks household cost pressure that can quickly alter public-service demand and policy response priorities.  
   **Anomaly trigger:** CPI/CPIH monthly acceleration above the recent trend (or a sharp component spike) that implies near-term affordability stress.

2. **Environment Agency flood-monitoring API reference and latest readings surface (England)**  
   URL: [https://environment.data.gov.uk/flood-monitoring/doc/reference](https://environment.data.gov.uk/flood-monitoring/doc/reference)  
   Why it matters: near real-time flood warning, station, and level/flow infrastructure for operational disruption detection.  
   **Anomaly trigger:** sudden growth in warning/alert counts or synchronized level spikes across multiple nearby stations within 24–72 hours.

3. **Met Office DataPoint status page (decommissioned service risk monitor)**  
   URL: [https://www.metoffice.gov.uk/services/data/datapoint](https://www.metoffice.gov.uk/services/data/datapoint)  
   Why it matters: confirms a still-relevant migration risk for legacy weather-ingestion pipelines.  
   **Anomaly trigger:** any official status or retirement-guidance update that changes migration deadlines, replacement pathways, or service continuity assumptions.

## Verification notes

- All three pages were reachable at run time.
- The flood API documentation still states near-real-time coverage and typical transfer frequency behavior.
- Met Office DataPoint page still states the service is decommissioned.

## Caveats

- ONS is lower cadence than emergency feeds; strongest for step-change detection rather than intraday alerts.
- Flood transfer frequency varies by site/risk conditions.
- DataPoint status is a dependency-risk signal, not an operational weather observation feed itself.

## Bottom line

Publication outcome: **three UK-relevant operational datasets were added with explicit short-horizon anomaly triggers to improve next-slot story candidate discovery.**

## Sources

1. [https://www.ons.gov.uk/economy/inflationandpriceindices](https://www.ons.gov.uk/economy/inflationandpriceindices)
2. [https://environment.data.gov.uk/flood-monitoring/doc/reference](https://environment.data.gov.uk/flood-monitoring/doc/reference)
3. [https://www.metoffice.gov.uk/services/data/datapoint](https://www.metoffice.gov.uk/services/data/datapoint)
