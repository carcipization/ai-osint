# DATASETS_OPTIMIZE trace — cache maintenance + catalog hygiene

**Run slot:** DATASETS_OPTIMIZE  
**Run window (UTC):** 2026-03-25 09:39–09:41 UTC

## Mandatory cache maintenance steps

1. Ran cache sync:
   - `ai_osint_ctl.py discovery cache-sync`
   - Result: ok=true; activeDatasets=252; totalEntries=257.

2. Pulled maintenance batch:
   - `ai_osint_ctl.py discovery cache-next`
   - Batch returned 25 queued entries; scanned top 10 in this run.

3. Recorded outcomes:
   - Used `ai_osint_ctl.py discovery cache-mark` for all 10 scanned entries.
   - Marked `--changed` on 6 reachable entries with live 200 responses.

## Cache stats (post-mark)

- Active entries: **257**
- Scanned this run: **10**
- Changed flagged: **6**
- Blocked/errors: **4**

## Scanned entries summary

### Reachable (200)
- FEMA Web Disaster Declarations (changed)
- FEMA Web Disaster Summaries (changed)
- Hazard Mitigation Grant Program - Disaster Summaries (changed)
- Housing Assistance Program Data – Owners (changed)
- International Energy Data - All Energy (changed)
- International Energy Data - Natural Gas (changed)

### Blocked/errors (with one retry)
- **Airline On-Time Performance Data**  
  URL: https://catalog.data.gov/dataset/airline-on-time-performance-data  
  Status: HTTP 404 at 2026-03-25 09:40 UTC  
  Retry: fail (HTTP 404) at 2026-03-25 09:40 UTC  
  Action: logged as catalog-quality issue; queue replacement-source search in next DATASETS slot.

- **Fair Market Rents**  
  URL: https://catalog.data.gov/dataset/fair-market-rents  
  Status: HTTP 404 at 2026-03-25 09:40 UTC  
  Retry: fail (HTTP 404) at 2026-03-25 09:40 UTC  
  Action: logged as catalog-quality issue; queue replacement-source search in next DATASETS slot.

- **Household Pulse Survey Public Use File and API**  
  URL: https://www.census.gov/data/developers/data-sets/household-pulse-survey.html  
  Status: HTTP 404 at 2026-03-25 09:40 UTC  
  Retry: fail (HTTP 404) at 2026-03-25 09:40 UTC  
  Action: likely moved/retired path; queue replacement-source search in next DATASETS slot.

- **NHTSA Crash Data API (FARS/CRSS)**  
  URL: https://crashviewer.nhtsa.dot.gov/CrashAPI  
  Status: HTTP 403 at 2026-03-25 09:40 UTC  
  Retry: fail (HTTP 403) at 2026-03-25 09:40 UTC  
  Action: environment access-blocked; queue alternate source/access-method review.

## Catalog-structure hygiene pass (lightweight)

Flagged repetitive title-bloat pattern for canonical cleanup in next DATASETS_A/B slot:
- Petroleum Data Application Programming Interface (API)
- Petroleum Data: Consumption/Sales Application Programming Interface (API)
- Petroleum Data: Crude Reserves and Production Application Programming Interface (API)
- Petroleum Data: Imports/Exports and Movements Application Programming Interface (API)
- Petroleum Data: Prices Application Programming Interface (API)
- Petroleum Data: Refining and Processing Application Programming Interface (API)
- Petroleum Data: Stocks Application Programming Interface (API)
- Petroleum Data: Summary Application Programming Interface (API)

Planned cleanup direction: normalize naming to concise canonical forms (drop repeated "Application Programming Interface (API)" suffix) and review for near-duplicate overlap consolidation.
