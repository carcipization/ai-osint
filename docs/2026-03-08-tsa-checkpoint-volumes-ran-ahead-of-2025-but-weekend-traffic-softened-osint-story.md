# TSA checkpoint volumes ran ahead of 2025 in early 2026, but weekend traffic softened

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-08-tsa-checkpoint-volumes-ran-ahead-of-2025-but-weekend-traffic-softened-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-08-tsa-checkpoint-volumes-ran-ahead-of-2025-but-weekend-traffic-softened-osint-story.md)

**Dateline:** 2026-03-08 09:12 UTC

U.S. airport security throughput was modestly higher in early 2026 than the same calendar stretch a year earlier, according to Transportation Security Administration (TSA) checkpoint data, but the gain was uneven.

A day-by-day parse of TSA’s public passenger-volume tables shows 141,896,840 travelers screened from Jan. 1 through March 5, 2026, versus 139,504,389 on the same month/day set in 2025. That is an increase of 2,392,451 passengers, or 1.71%.

The increase was concentrated on weekdays. Weekday throughput was 2.89% above year-ago levels across the matched window, while weekend throughput was 1.22% lower.

That split matters for how the trend is interpreted. The cumulative signal still points up, but it does not describe broad-based acceleration across all travel patterns. It is more consistent with uneven demand or calendar effects than with a uniform surge.

## Appendix: Method

- Pulled TSA’s daily passenger-volume table for 2026 and the year-specific archive page for 2025.
- Parsed date and count fields from the official TSA HTML tables.
- Set the comparison window from 2026-01-01 through the latest available 2026 date in the table (2026-03-05).
- Matched each 2026 date to the same month/day in 2025 and recomputed totals, deltas, and percentage changes.
- Split results into weekday and weekend subtotals using the 2026 calendar for classification.

## Appendix: Limitations

- TSA updates can be revised after initial posting, especially for recent days.
- Same month/day matching is not holiday-adjusted; shifting school-break and holiday timing can affect comparability.
- TSA checkpoint counts measure screened passengers, not total travel demand, fares, or airline capacity.
- This analysis is descriptive and does not isolate causal drivers.

## Appendix: Confidence

**Medium-high.** The calculations are directly reproducible from TSA’s first-party daily tables, and arithmetic checks were recomputed from parsed rows. Confidence is reduced for causal interpretation because holiday timing and calendar effects are not normalized.

## Appendix: Sources

1. [TSA passenger volumes (2026 page)](https://www.tsa.gov/travel/passenger-volumes) — retrieved 2026-03-08 09:07 UTC
2. [TSA passenger volumes (2025 archive page)](https://www.tsa.gov/travel/passenger-volumes/2025) — retrieved 2026-03-08 09:07 UTC
3. [TSA passenger volumes (2024 archive page)](https://www.tsa.gov/travel/passenger-volumes/2024) — retrieved 2026-03-08 09:08 UTC
