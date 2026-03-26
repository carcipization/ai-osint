# DATASETS_A trace — medicine access + transit mobility stack

**Run slot:** DATASETS_A  
**Timestamp (UTC):** 2026-03-26 17:42 UTC

## Run framing
- Slot type is datasets-only; target was 3–10 additions with breadth-first selection.
- Consequence screen emphasized public decision surfaces: healthcare access continuity + everyday mobility access.

## Discovery sweep (selected queries)
- `site:catalog.data.gov dataset pharmacy shortage drug shortages FDA API`
- `site:catalog.data.gov dataset transit ridership monthly`
- `site:catalog.data.gov dataset hospital bed occupancy by state API`
- `site:catalog.data.gov dataset eviction filings`
- `site:catalog.data.gov dataset drinking water violations county`

## Candidate triage

Promoted (net-new, consequence-relevant):
1. Current and Resolved Drug Shortages and Discontinuations Reported to FDA
2. Monthly Prescription Drug Plan Formulary and Pharmacy Network Information
3. Hospitals (HIFLD)
4. Transit Ridership - Urban Rail
5. Transit Ridership - Fixed Route Bus
6. Transit Ridership - Other Transit Modes

Rejected/deferred examples:
- NTD Monthly Module Data Set — endpoint returned repeatable 404 in this run window (deferred pending URL/slug verification).
- Retired/archival hospital COVID occupancy variants — deprioritized due stale-update caveats already represented in catalog.
- City-only eviction feeds — deferred this cycle to avoid overfitting to localized non-federal schemas when stronger federal breadth candidates were available.

## Overlap check
- Catalog overlap pass against `docs/datasets-catalog.md` showed all six promoted URLs absent before insertion (classified as **net-new**).

## Endpoint checks (quick)
- Successful 200 fetch: 6/6 promoted URLs.
- Blocked/error sampled item:
  - source: Data.gov
  - URL: https://catalog.data.gov/dataset/ntd-monthly-module-data-set
  - error: repeatable 404 (page script/error response)
  - first seen: 2026-03-26 17:40 UTC
  - retry outcome: fail (same 404)

## Output
- Published dataset-intel markdown:
  - `docs/2026-03-26-dataset-intel-medicine-access-and-transit-mobility-stack-watchlist-56.md`
- Updated catalog entries in:
  - `docs/datasets-catalog.md`
