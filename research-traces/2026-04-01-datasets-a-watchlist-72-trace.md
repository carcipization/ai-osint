# DATASETS_A trace — 2026-04-01 (watchlist 72)

**UTC:** 2026-04-01 21:45

## Run classification
- Slot: DATASETS_A
- Mode: datasets-only
- Publish target: dataset batch brief

## Candidate sweep and overlap pass

Selected candidates (all net-new vs `docs/datasets-catalog.md`):
1. Weatherization Assistance Program and Low Income Home Energy Assistance Program for Solar Survey Responses and Plan — https://catalog.data.gov/dataset/wap-liheap-for-solar-survey-responses-and-plan-analyses-40d0c
2. Mental Health Care in the Last 4 Weeks — https://catalog.data.gov/dataset/mental-health-care-in-the-last-4-weeks
3. Post-COVID Conditions — https://catalog.data.gov/dataset/post-covid-conditions-89bb3

Overlap classification:
- WAP/LIHEAP survey+plan: net-new
- Mental Health Care in the Last 4 Weeks: net-new
- Post-COVID Conditions: net-new

## Consequence/decision screen
- Broad non-specialist consequence: PASS (energy affordability, care access, functional health burden)
- Decision utility: PASS (household assistance planning, local health/support prioritization)
- Cross-domain chain value: PASS (energy burden + health capacity + labor/household continuity)

## Rejected/held candidates
- 801 - Monthly Child Care Data Report (https://catalog.data.gov/dataset/801-monthly-child-care-data-report): held this run due retrieval failure in tool environment (404 + script payload returned); revisit in later cycle.
- Child Care Compliance & Complaint Reports (Iowa): high local utility, but deprioritized for this batch to keep broader national consequence coverage balance.

## Error logging (structured)
- source: Data.gov | url: https://catalog.data.gov/dataset/801-monthly-child-care-data-report | status/error: fetch returned 404 with JS payload | utc: 2026-04-01T21:40:22Z | retry outcome: fail (same 404/script payload at 2026-04-01T21:40:34Z)
