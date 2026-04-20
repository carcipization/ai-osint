# DATASETS Cadence Trace — 2026-04-20 14:27 UTC

## Run context
- Slot: DATASETS
- User/target: Jon (5694918526)
- Reuters: not used
- Goal: add 3–10 datasets (batch-first)

## Discovery and overlap pass
Candidate set screened for direct raw-data access and broad non-specialist consequence coverage.

Selected (all net-new URL overlap status against `docs/datasets-catalog.md`):
1. NREL Alternative Fuel Stations API — net-new
2. USDA FoodData Central API — net-new
3. FAA NAS Status — net-new
4. BTS Airline On-Time Statistics (TranStats) — net-new
5. NHTSA Public API — net-new

Rejected/deferred examples:
- EIA Open Data API: duplicate (already in catalog).
- Generic transportation landing pages: excluded when not direct query surfaces.

## Consequence-first rationale
- Mobility and passenger/cargo reliability impacts (FAA NAS + BTS on-time).
- Household transport access under fuel and charging constraints (NREL stations).
- Household food substitution and nutrition-quality monitoring under cost pressure (USDA FDC API).
- Vehicle-safety context and model-level risk checks (NHTSA API).

## Catalog updates
- Added 5 entries across domains:
  - Humanitarian/hazard: +1 (USDA FDC)
  - Energy/trade/maritime: +1 (NREL alt-fuel stations)
  - Aviation/mobility: +2 (FAA NAS, BTS on-time)
  - Domestic public safety: +1 (NHTSA)
- Updated metadata counters and checksum:
  - datasets: 150 -> 155
  - section balance/checksum adjusted accordingly.

## Publication artifact
- New DATASETS post:
  - `docs/2026-04-20-dataset-intel-mobility-food-and-vehicle-safety-consequence-signals-watchlist-113.md`
- Required top links + UTC dateline included.
