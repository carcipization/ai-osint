# Research trace — one-off DATASETS run

**Run type:** DATASETS (one-off, out-of-cadence)
**UTC timestamp:** 2026-04-03 02:50

## Constraints honored
- Did not read or write cadence state files.
- Did not alter cadence rotation/schedules.

## Candidate selection notes
- Discovery source family: Data.gov CKAN API package search across housing instability / eviction / homelessness terms.
- Overlap check against `docs/datasets-catalog.md` performed before promotion.

## Promoted datasets (net-new)
1. coc-homeless-populations-and-subpopulations-reports — **net-new**
2. ahar-part-1-pit-estimates-of-homelessness — **net-new**
3. mckinney-vento-act-performance-participation-and-funding-data — **net-new**
4. landlord-tenant-monthly-caseload-cy-2023 — **net-new**
5. lahd-property-look-up-for-eviction-cases — **net-new**

## Importance/consequence screen
- Passed: all five datasets map to non-specialist consequences (housing stability, homelessness burden, school access, legal-aid targeting).
- Convenience override check: rejected unrelated easy-to-query technical datasets that lacked broad public consequence for this slot.

## Blockers/errors
- HDX web fetch attempts returned 406 bot-block responses; switched discovery source family to Data.gov CKAN API for this run.
