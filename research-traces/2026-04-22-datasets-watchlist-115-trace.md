# DATASETS trace — watchlist 115

**Run UTC:** 2026-04-22 14:27 UTC
**Slot:** DATASETS

## Candidate discovery summary

- Discovery tooling check: `bulk_dataset_intake.py` returned 0 candidates due to source errors.
  - data.gov: HTTP 404
  - HDX: HTTP 406
- Fallback discovery path used: direct catalog/API retrieval via Data.gov and CMS Provider Data catalog pages.

## Overlap pass (net-new vs existing catalog)

Checked current `docs/datasets-catalog.md` for duplicate URLs/titles before promotion.

### Promoted (net-new)
1. `https://data.cms.gov/provider-data/dataset/yv7e-xc69` — Timely and Effective Care - Hospital
2. `https://data.cms.gov/provider-data/dataset/apyc-v239` — Timely and Effective Care - State
3. `https://catalog.data.gov/dataset/household-debt-by-state-county-and-msa` — Household Debt by State, County, and MSA
4. `https://catalog.data.gov/dataset/unemployment-insurance-weekly-claims-data-for-california-2c315` — Unemployment Insurance Weekly Claims Data for California

### Rejected / already present examples
- `https://catalog.data.gov/dataset/daily-transit-ridership` — duplicate (already in catalog)
- `https://catalog.data.gov/dataset/monthly-modal-time-series` — duplicate (already in catalog)
- `https://catalog.data.gov/dataset/transit-ridership-urban-rail` — duplicate (already in catalog)
- `https://catalog.data.gov/dataset/evictions` — duplicate (already in catalog)
- `https://catalog.data.gov/dataset/eviction-notices` — duplicate (already in catalog)

## Selection rationale (consequence-first)

- Added a cross-domain mix (health service performance + household balance sheet + labor stress) to avoid narrow domain repetition.
- Prioritized datasets with direct public consequence: care access, household income security, debt strain.
- Avoided NOAA-centric additions this cycle.
