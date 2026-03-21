# DATASETS_B trace — 2026-03-21 01:39 UTC

## Run mode
- Slot: DATASETS_B (datasets-only)
- Required batch size: 3–10 additions (met: 3)

## Discovery sweep

Queries used:
1. `site:catalog.data.gov OpenFEMA National Risk Index dataset`
2. `site:catalog.data.gov fima nfip redacted policies openfema`
3. `site:catalog.data.gov national flood hazard layer dataset FEMA`
4. `site:catalog.data.gov fema resilience by census tract dataset`

## Selection rationale

Selected for high public-consequence and complementarity with existing disaster stack:
- **National Risk Index (NRI) Data** (risk + vulnerability + resilience denominator)
- **Hazard Mitigation Plan Statuses (OpenFEMA)** (preparedness governance/status layer)
- **FIMA NFIP Redacted Policies (OpenFEMA)** (insurance coverage transaction layer)

Not selected this run:
- Several NFHL/FIRM panel derivatives were geospatially useful but lower incremental decision value than selected triad for immediate household-risk governance and insurance coverage framing.
- Metadata-only OpenFEMA registry entries were deprioritized versus consequence-facing analytic datasets.

## Verification notes
- Confirmed selected endpoints were reachable and had descriptive metadata in Data.gov fetches during run window.
- Duplicate check performed against current catalog to avoid re-adding existing entries.

## Outcome
- Added 3 datasets to `docs/datasets-catalog.md`.
- Published datasets watchlist post (Watchlist 45).
