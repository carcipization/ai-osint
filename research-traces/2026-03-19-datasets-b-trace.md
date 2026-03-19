# DATASETS_B trace — 2026-03-19 01:41 UTC

## Run scope
- Slot: DATASETS_B
- Requirement: datasets-only run, add 3–10 datasets
- Added this run: 4 datasets

## Situational awareness + anomaly sweep

### World-state trigger
Searches run:
- `site:catalog.data.gov dataset unemployment insurance weekly claims state`
- `site:catalog.data.gov dataset SNAP participation monthly state`
- `site:catalog.data.gov dataset opioid overdose emergency medical services weekly`
- `site:catalog.data.gov dataset electricity interruptions county daily`
- supplementary: `site:catalog.data.gov dataset eviction filings monthly county`

Active consequence classes prioritized:
- labor-market stress and benefits pressure
- household affordability/safety-net load
- drug-overdose mortality burden

### Anomaly trigger
- Candidate scan prioritized datasets with recent metadata updates and direct public-decision relevance.
- Verified endpoint reachability and freshness metadata via Data.gov pages.

## Added datasets (4)
1. Historical Unemployment Insurance Seasonally Adjusted and Unadjusted Weekly Claims Data
   - URL: https://catalog.data.gov/dataset/historical-unemployment-insurance-seasonally-adjusted-and-unadjusted-weekly-claims-data
   - Metadata updated: 2026-01-20
2. Unemployment Insurance Weekly Claims & Extended Benefits Trigger Data (ETA-539)
   - URL: https://catalog.data.gov/dataset/unemployment-insurance-weekly-claims-extended-benefits-trigger-data-eta-539
   - Metadata updated: 2026-01-20
3. Supplemental Nutrition Assistance Program Participation and Cost Data
   - URL: https://catalog.data.gov/dataset/supplemental-nutrition-assistance-program-participation-and-cost-data
   - Metadata updated: 2025-04-21
4. Provisional drug overdose death counts for specific drugs
   - URL: https://catalog.data.gov/dataset/provisional-drug-overdose-death-counts-for-specific-drugs
   - Metadata updated: 2026-01-29

## Non-specialist consequence screen (pass)
- UI weekly + ETA-539: early labor stress signal and extended-benefit trigger context for households, employers, and local planners.
- SNAP participation/cost: direct affordability and safety-net pressure indicator.
- Provisional overdose deaths: high-consequence public-health burden monitoring across regions/drug classes.

## Rejected/held candidates
- Event-correlated outage dataset in America: high value but overlaps recent grid/outage additions; deferred for rotation balance.
- State/local eviction datasets (CT/NYC/SF): useful but geographically narrow versus this run’s federal baseline expansion objective.

## Blocked/error fetch log
- None. Selected endpoints returned HTTP 200 in this run window.

## Output actions
- Updated `docs/datasets-catalog.md` with 4 entries.
- Prepared publish post: `docs/2026-03-19-dataset-intel-labor-safety-net-and-overdose-pressure-baselines-watchlist-40.md`
