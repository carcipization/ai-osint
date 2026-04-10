# DATASETS_A trace — 2026-04-10 (watchlist 96)

## Run metadata
- Slot: DATASETS_A
- UTC window: 2026-04-10 09:39–09:53 UTC
- Reuters usage: none

## Preflight
- Re-checked PRECEPTS.md and osint-journalism SKILL.md before edits.
- Resolved dirty working tree per hygiene rule by stashing unrelated generated drift:
  - `git stash push -u -m "pre-datasets-a-2026-04-10-1039-unrelated-html-drift"`
- Synced repo after stash:
  - `git fetch origin && git pull --rebase origin main`

## Discovery sweep (batch-first)

Broad query families used:
- `site:catalog.data.gov WARN notices dataset`
- `site:catalog.data.gov hospital bed occupancy dataset API`
- `site:catalog.data.gov school meal participation dataset`
- `site:catalog.data.gov rent burden dataset API metro`
- plus CKAN package_search term sweeps across eviction/water/child-care/maternal/transit/utility/food-insecurity/layoffs/overdose.

## Overlap pass (net-new / adjacent / duplicate)

### Promoted (4)
1. **VSRR Provisional Maternal Death Counts and Rates**
   - URL: https://catalog.data.gov/dataset/vsrr-provisional-maternal-death-counts
   - Class: net-new
   - Raw access confirmed: CSV/JSON/XML/RDF endpoints (data.cdc.gov)
   - Metadata modified: 2026-01-29

2. **COVID-19 Reported Patient Impact and Hospital Capacity by Facility -- RAW**
   - URL: https://catalog.data.gov/dataset/covid-19-reported-patient-impact-and-hospital-capacity-by-facility-raw
   - Class: net-new
   - Raw access confirmed: CSV/JSON/XML/RDF endpoints (healthdata.gov)
   - Metadata modified: 2025-07-04

3. **Utility Company Customer Service Response Index (CSRI): Beginning 2005**
   - URL: https://catalog.data.gov/dataset/utility-company-customer-service-response-index-csri-beginning-2005
   - Class: net-new
   - Raw access confirmed: CSV/JSON/XML/RDF endpoints (data.ny.gov)
   - Metadata modified: 2026-04-04

4. **HHS - Food Inspection Data from July 2024 and onward**
   - URL: https://catalog.data.gov/dataset/hhs-food-inspection-data-from-july-2024-and-onward
   - Class: net-new
   - Raw access confirmed: CSV/JSON/XML/RDF endpoints (data.montgomerycountymd.gov)
   - Metadata modified: 2026-04-05

### Rejected / not promoted examples
- Oregon `WARN` dataset: adjacent to existing WARN-notice coverage; deprioritized for breadth this cycle.
- School meal participation candidates: duplicate/adjacent to already-cataloged NSLP/SBP/Summer Food Service entries.
- Stale/archival hospitalization variants: deprioritized when active or higher-utility alternatives already available.

## Selection rationale (consequence-first)
- Chosen set improves cross-domain consequence coverage: maternal mortality, facility load, utility service quality, and local food safety.
- Avoided convenience-only adds and duplicate school-meal/WARN variants.
- Meets DATASETS_A batch rule (3–10 adds): **4 adds**.

## Blocked/error fetch log
- None material after initial repository sync blocker was resolved via stash+pull.
