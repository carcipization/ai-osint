# Datasets: UNICEF SDMX API expands child-risk and service-access monitoring (watchlist 95)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-04-10-dataset-brief-unicef-sdmx-child-risk-and-service-access-watchlist-95.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-04-10-dataset-brief-unicef-sdmx-child-risk-and-service-access-watchlist-95.md)

**Dateline:** 2026-04-10 05:49 UTC

No standard STORY candidate in this slot cleared anomaly, mechanism, and broad-importance gates after a data-first sweep, so this run publishes the mandatory dataset fallback as a dataset brief.

UNICEF’s SDMX API provides direct machine-readable access to cross-country child-wellbeing indicators that can sharpen early warning on broad public consequences: child mortality, immunization coverage, nutrition stress, school participation, water and sanitation access, and social protection reach. For non-specialists, this matters because it helps answer practical questions faster: where service access is weakening, where child health risk is rising, and where public systems may need support before pressure compounds.

The dataset is especially useful right now because many high-impact risks (infectious disease bursts, food affordability stress, climate shocks, and displacement) show up first in child-facing indicators before they are fully visible in slower annual reports. The API structure also supports reproducible cross-country comparison instead of one-off screenshot narratives.

## Dataset intel

- **Source:** UNICEF Indicator Data Warehouse (SDMX)
- **Base API:** [https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/](https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/)
- **Discovery endpoint:** `dataflow`
- **Example working pull (latest observations):**
  - `[https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/UNICEF,GLOBAL_DATAFLOW,1.0/..../?lastNObservations=1`](https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/UNICEF,GLOBAL_DATAFLOW,1.0/..../?lastNObservations=1`)
- **Evidence of live availability in this run:** `dataflow` and sample `data` endpoint returned HTTP 200.

## How to use it

1. Pull available dataflows via `/dataflow` to identify relevant indicator families (for example: immunisation, nutrition, child mortality, WASH, education).
2. Retrieve selected series through `/data/{flowRef}/{key}` with a fixed extraction template per indicator group.
3. Compare latest observation against prior period and a 3–5 year baseline where available.
4. Pair with one independent consequence-family source (for example WHO DON, HDX/OCHA, or local ministry releases) before drawing strong causal conclusions.

## Scope and limits

- Coverage is global but not uniform; country cadence and reporting lag vary.
- Indicator definitions are not interchangeable across all series; each metric needs denominator checks.
- Some high-frequency shocks will appear with delay in official child-indicator systems.

## Why this is important now

This dataset improves consequence-first OSINT: it can connect upstream shocks to household-level outcomes (health access, nutrition pressure, school participation) that matter to families, aid planners, and local operators. It is a high-utility addition for runs that need public-interest signals beyond market-only or specialist telemetry.

## Appendix: Sources

- UNICEF SDMX API documentation: [https://data.unicef.org/sdmx-api-documentation/](https://data.unicef.org/sdmx-api-documentation/)
- UNICEF SDMX API root: [https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/](https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/)
