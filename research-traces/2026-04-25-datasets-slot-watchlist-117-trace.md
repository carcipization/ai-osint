# DATASETS Slot Trace — 2026-04-25 14:24 UTC

## Run metadata
- Slot: DATASETS
- Operator: OpenClaw cadence run (Jon)

## First-principles question
Which net-new direct-access datasets most improve near-term decision utility for non-specialists on household safety, mobility access, and disaster-response readiness?

## Candidate search + overlap checks
Initial candidate pool built from open government API surfaces and direct data endpoints (transport, safety enforcement, policing, disaster operations).

Net-new URL checks against `docs/datasets-catalog.md`:
- https://www.transit.dot.gov/ntd/data-product/monthly-module-adjusted-data-release -> net-new
- https://api.fda.gov/food/enforcement.json -> net-new
- https://api.fda.gov/drug/enforcement.json -> net-new
- https://data.police.uk/docs/ -> net-new
- https://www.fema.gov/about/openfema/api -> net-new

Reachability checks this run window:
- NTD monthly ridership page: HTTP 200
- openFDA food enforcement endpoint (`?limit=1`): HTTP 200
- openFDA drug enforcement endpoint (`?limit=1`): HTTP 200
- UK Police API docs endpoint: HTTP 200
- OpenFEMA API docs endpoint: HTTP 200

## Promotion decisions (5)
Promoted because they add broad consequence coverage and decision-useful raw access:
1. National Transit Database Complete Monthly Ridership (adjusted/estimated)
2. openFDA Food Enforcement API
3. openFDA Drug Enforcement API
4. UK Police Data API
5. OpenFEMA API

## Rejected/held examples
- IATA commercial data surfaces (not open raw access for this workflow).
- Generic portal/search pages without stable queryable endpoint structure.
- Region-specific datasets with narrow consequence utility in this cycle versus selected cross-domain additions.

## Blocked/error fetch log
- None that blocked selected additions in this run window.

## Output actions
- Updated `docs/datasets-catalog.md` dateline and metadata count.
- Added 5 catalog entries across Aviation/Mobility, Economy/Governance, Domestic Public Safety, and Disaster Response sections.
- Added publication candidate: `docs/2026-04-25-dataset-intel-household-safety-and-transit-access-apis-watchlist-117.md`.
