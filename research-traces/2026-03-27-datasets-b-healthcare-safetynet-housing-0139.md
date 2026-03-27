# DATASETS_B trace — healthcare safety-net + housing affordability stack

**Run slot:** DATASETS_B  
**Timestamp (UTC):** 2026-03-27 01:40 UTC

## Discovery sweep (representative queries)
- `site:catalog.data.gov dataset medicaid and chip enrollment performance indicators`
- `site:catalog.data.gov dataset nursing home compare providers API`
- `site:catalog.data.gov dataset nursing home staffing data care compare`
- `site:catalog.data.gov dataset opioid treatment program locations`
- `site:catalog.data.gov dataset fair market rents county`
- `site:catalog.data.gov dataset unemployment insurance weekly claims state`
- `site:catalog.data.gov dataset SNAP participation by state monthly`

## Candidate triage

Promoted (net-new):
1. State Medicaid and CHIP Applications, Eligibility Determinations, and Enrollment Data
2. Nursing Home Compare
3. Payroll Based Journal Daily Nurse Staffing
4. Opioid Treatment Program Providers
5. Fair Market Rents lookup tool

Deferred/rejected examples:
- Unemployment Insurance Weekly Claims & Extended Benefits Trigger Data (ETA-539): deferred as adjacent/duplicate family overlap (already represented in catalog by labor and claims baselines).
- SNAP participation/cost datasets: deferred this cycle due existing SNAP representation in catalog (duplicate family signal).
- Child-care local/non-federal datasets: deprioritized in this run window to keep federal comparability and broad baseline coherence.

## Overlap pass (required)
- Checked promoted URLs against `docs/datasets-catalog.md` before insertion.
- Classification: all 5 promoted entries = **net-new**.

## Endpoint reliability checks
- 200 OK for all 5 promoted URLs on direct fetch.
- Blocked/error list: none in selected set.

## Output
- New dataset-intel publication draft:
  - `docs/2026-03-27-dataset-intel-healthcare-safety-net-and-housing-affordability-stack-watchlist-57.md`
- Catalog updates:
  - `docs/datasets-catalog.md` (metadata + five entries)
