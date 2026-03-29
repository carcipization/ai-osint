# DATASETS_A trace — 2026-03-29 — food/energy/mobility household stack

**Run window (UTC):** 2026-03-29 13:39–13:42  
**Slot:** DATASETS_A

## Situational awareness + anomaly sweep (datasets mode)

World-state scan terms:
- `site:catalog.data.gov energy burden household utility arrears dataset`
- `site:catalog.data.gov eviction filings dataset monthly`
- `site:catalog.data.gov transit ridership by agency monthly data`
- `site:catalog.data.gov school meal participation data set`

Observed consequence classes:
1. Household food access and nutrition program dependence.
2. Household utility affordability risk under elevated energy price pressure.
3. Daily commuting access reliability for large metro systems.

Anomaly/coverage trigger:
- Catalog overlap check against `docs/datasets-catalog.md` to identify net-new vs adjacent vs duplicate.
- Existing overlap found for `Transit Ridership - Urban Rail`, `Transit Ridership - Fixed Route Bus`, `Monthly Modal Time Series`, `Eviction Notices`, and `Housing Landlord-Tenant Disputes` (not selected as net-new).

## Selected net-new datasets (5)
1. National School Lunch Assistance Program Participation and Meals Served Data
2. School Breakfast Participation and Meals Served Data
3. Summer Food Service Participation, Meals, and Costs Data
4. Department of Energy - Low-Income Energy Affordability Data (LEAD Tool) - 2022 Update
5. Daily Transit Ridership

## Why selected
- Passes non-specialist consequence screen (food access, utility burden, commuting reliability).
- Adds breadth beyond recent overdose/childcare/eldercare-heavy additions.
- Forms a cross-domain household stress chain (nutrition support reliance + utility-cost burden + transport access).

## Rejected/held candidates
- District Court of Maryland Eviction Case Data: adjacent to existing eviction/dispute coverage; deferred for later if housing stack needs state court depth.
- Connecticut Weekly Evictions by Census Tract: useful but similar domain already represented this week; deprioritized for breadth rotation.
- Additional transit monthly variants: mostly duplicate with existing monthly-modal and fixed-route entries.

## Blockers/errors
- No blocking endpoint errors for selected five catalog pages in this run window.

## Sources used
- https://catalog.data.gov/dataset/national-school-lunch-assistance-program-participation-and-meals-served-data
- https://catalog.data.gov/dataset/school-breakfast-participation-and-meals-served-data
- https://catalog.data.gov/dataset/summer-food-service-participation-meals-and-costs-data
- https://catalog.data.gov/dataset/low-income-energy-affordability-data-lead-tool-2022-update
- https://catalog.data.gov/dataset/daily-transit-ridership
