# DATASETS_B trace — 2026-04-10 (watchlist 98)

## Run metadata
- Slot: DATASETS_B
- UTC window: 2026-04-10 17:39–18:03 UTC
- Reuters usage: none

## Preflight and hygiene
- Re-checked `PRECEPTS.md` and `skills/osint-journalism/SKILL.md` before substantive actions.
- Working tree had unrelated generated HTML drift; stashed before sync:
  - `git stash push -u -m "pre-datasets-b-2026-04-10-1839-unrelated-html-drift"`
- Synced repository:
  - `git fetch origin && git pull --rebase origin main`

## Discovery process
- Ran broad CKAN/Data.gov search sweeps across consequence-first classes:
  - eviction/housing strain, child-care systems, hospital capacity, maternal-health, utility outage, food inspection, unemployment insurance, school meals, homelessness, airfare/mobility cost.
- Used `package_search` and `package_show` checks to confirm machine-readable raw access and metadata recency.

## Overlap pass (net-new / adjacent / duplicate)

### Promoted (5)
1. **Licensed and Certified Healthcare Facility Bed Types and Counts**
   - URL: https://catalog.data.gov/dataset/licensed-and-certified-healthcare-facility-bed-types-and-counts-ad4df
   - Class: net-new
   - Raw access: CSV/Excel endpoints (California CHHS data portal)
   - Metadata updated: 2026-03-23

2. **Consumer Airfare Report: Table 1a - All U.S. Airport Pair Markets**
   - URL: https://catalog.data.gov/dataset/consumer-airfare-report-table-1a-all-u-s-airport-pair-markets
   - Class: net-new
   - Raw access: CSV/JSON/XML/RDF (data.transportation.gov)
   - Metadata updated: 2026-04-03

3. **Consumer Airfare Report: Table 6 - Contiguous State City-Pair Markets That Average At Least 10 Passengers Per Day**
   - URL: https://catalog.data.gov/dataset/consumer-airfare-report-table-6-contiguous-state-city-pair-markets-that-average-at-least-1
   - Class: net-new
   - Raw access: CSV/JSON/XML/RDF (data.transportation.gov)
   - Metadata updated: 2026-04-03

4. **DHS Daily Report**
   - URL: https://catalog.data.gov/dataset/dhs-daily-report
   - Class: net-new
   - Raw access: CSV/JSON/XML/RDF (NYC Open Data)
   - Metadata updated: 2026-04-05

5. **Opioid EMS Calls**
   - URL: https://catalog.data.gov/dataset/opioid-ems-calls-ac2fc
   - Class: net-new
   - Raw access: ArcGIS API + CSV download
   - Metadata updated: 2026-03-29

### Not promoted / deprioritized examples
- Child-care licensing variants (multiple local slices): useful but highly overlapping and less cross-domain than selected set in this cycle.
- School meal administrative-review shards: adjacent to existing meal participation/reimbursement coverage.
- Utility outage county feeds: already substantial outage/utility complaint coverage; lower marginal breadth gain this run.

## Selection rationale
- Satisfies DATASETS_B batch requirement (3–10 adds): **5 promoted**.
- Breadth-first mix across health-system capacity, household mobility affordability, homelessness service pressure, and overdose emergency burden.
- Preference given to directly queryable raw-data endpoints and recent metadata updates.

## Blocked/error fetch log
- No material endpoint block after initial stash+sync hygiene step.
