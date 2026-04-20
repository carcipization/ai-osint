# Datasets: mobility, food, and vehicle safety consequence signals (watchlist 113)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-04-20-dataset-intel-mobility-food-and-vehicle-safety-consequence-signals-watchlist-113.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-04-20-dataset-intel-mobility-food-and-vehicle-safety-consequence-signals-watchlist-113.md)

**Dateline:** 2026-04-20 14:27 UTC

This DATASETS cycle adds five net-new sources focused on broad non-specialist consequences: transport disruption, household fuel access, food-quality/cost trade-offs, and consumer vehicle safety context.

## Added datasets (5)

1. [NREL Alternative Fuel Stations API](https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/)
2. [USDA FoodData Central API](https://fdc.nal.usda.gov/api-guide/)
3. [FAA National Airspace System (NAS) Status](https://nasstatus.faa.gov/)
4. [BTS Airline On-Time Statistics (TranStats)](https://www.transtats.bts.gov/ONTIME/)
5. [NHTSA Public API](https://api.nhtsa.gov/)

## Why these matter now

- **Mobility resilience:** FAA NAS status and BTS on-time records give both immediate and baseline views of travel disruption that affects household itineraries and time-sensitive cargo.
- **Fuel and charging access:** NREL station data helps check where alternative-fuel access can absorb transport stress during outages, price spikes, or route disruptions.
- **Food and health trade-offs:** FoodData Central supports ingredient and nutrient checks when households substitute toward lower-cost foods under inflation pressure.
- **Consumer safety relevance:** NHTSA machine-readable endpoints improve rapid model-level safety context checks for drivers and fleets.

## Consequence-first screening notes

- All five additions provide direct raw-data/API access suitable for repeatable queries.
- Overlap pass against `docs/datasets-catalog.md` classified all five candidates as **net-new** (no URL duplicates).
- Selection prioritized cross-domain chain value (mobility operations -> access/cost -> household decision impacts) over specialist-only telemetry.
