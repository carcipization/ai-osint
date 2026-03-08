# Research trace — TSA passenger volumes YTD comparison (2026 vs 2025)

## Testable question
Are U.S. TSA checkpoint passenger volumes in early 2026 running above the same calendar window in 2025, and is any difference uniform across weekdays and weekends?

## Evidence ledger

1. URL: https://www.tsa.gov/travel/passenger-volumes  
   Publisher: U.S. Transportation Security Administration (TSA)  
   Retrieved: 2026-03-08 ~09:07 UTC  
   What it proves: Daily checkpoint volume table for 2026 (current year page), including Jan 1–Mar 5 entries used for this run.  
   Limitations: Public page can revise; table updates are typically weekdays and can lag holiday operations.

2. URL: https://www.tsa.gov/travel/passenger-volumes/2025  
   Publisher: TSA  
   Retrieved: 2026-03-08 ~09:07 UTC  
   What it proves: Daily checkpoint volume table for 2025 used as same-day baseline (month/day alignment) against 2026 values.  
   Limitations: Year pages are snapshots and can still receive corrections.

3. URL: https://www.tsa.gov/travel/passenger-volumes/2024  
   Publisher: TSA  
   Retrieved: 2026-03-08 ~09:08 UTC  
   What it proves: Historical page structure consistency check (same date/number table format across years).  
   Limitations: Structural consistency does not validate every numeric field.

## Mechanical checks

- Parsed date/number rows from TSA HTML table for 2026 and 2025 pages.
- Aligned comparison window to 2026-01-01 through latest available 2026 date (2026-03-05).
- Mapped each 2026 date to same month/day in 2025.
- Recomputed totals and percentage changes.

Computed outputs:
- Window length: 64 matched days (2026-01-01 to 2026-03-05)
- 2026 total: 141,896,840
- 2025 same-day total: 139,504,389
- Difference: +2,392,451 (+1.71%)
- Weekday subtotal change: +2.89%
- Weekend subtotal change: -1.22%

## Contradiction pass

Sought disconfirming angle: does day-level volatility erase the aggregate signal?
- Observation: Several late-Feb/early-Mar days were below 2025 matches (e.g., 2026-02-28 and 2026-03-03).
- Result: Aggregate YTD still remained above 2025 due to stronger performance on many weekdays and select peak travel days.

## Could this be wrong because...

- TSA could revise one or more recent daily counts after publication.
- Same-month/day matching is not holiday-adjusted; calendar effects can influence weekend/weekday mix.
- The table reflects checkpoint throughput, not total U.S. travel demand (no direct load-factor or itinerary detail).

What evidence would invalidate the conclusion:
- Material TSA revisions that flip the 64-day cumulative total from +1.71% to below 0%.
- A corrected official TSA data extract showing different values for the compared date set.

Was that evidence found now?
- No. No contradictory official TSA dataset with conflicting totals was found during this run.
