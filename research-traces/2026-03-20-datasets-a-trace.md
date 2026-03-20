# DATASETS_A trace — 2026-03-20 17:39 UTC

## Run mode
- Slot: DATASETS_A (datasets-only)
- Required batch size: 3–10 additions (met: 3)

## Discovery sweep

Queries used:
1. `site:catalog.data.gov fertilizer price dataset`
2. `site:catalog.data.gov consumer food price index dataset USDA ERS`
3. `site:catalog.data.gov FEMA flood insurance claims dataset`
4. `site:catalog.data.gov ocean freight rates dataset`
5. `site:catalog.data.gov trucking spot rates dataset`

## Selection rationale

Selected for broad non-specialist consequence and chain value:
- **Fertilizer Use and Price** (upstream food-input pressure baseline)
- **Price Spreads from Farm to Consumer** (farm-to-retail pass-through test layer)
- **FIMA NFIP Redacted Claims (OpenFEMA)** (recurring household flood-loss burden at claims level)

Rejected/deprioritized this run:
- Several transport/freight catalog hits were already in catalog or lower incremental value for current gap.
- Some fertilizer trade pages were stale-window or narrower coverage than selected pair.

## Verification notes
- Candidate pages fetched via Data.gov endpoints in run window and confirmed accessible.
- Existing-catalog duplicate check performed for selected entries before insertion.

## Outcome
- Added 3 datasets to `docs/datasets-catalog.md`.
- Published one datasets watchlist post (Watchlist 44).
