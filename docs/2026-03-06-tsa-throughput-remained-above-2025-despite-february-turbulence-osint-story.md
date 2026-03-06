# U.S. airport checkpoint traffic stayed above 2025 levels in early 2026 despite February turbulence

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-06-tsa-throughput-remained-above-2025-despite-february-turbulence-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-06-tsa-throughput-remained-above-2025-despite-february-turbulence-osint-story.md)

**Dateline:** 2026-03-06 18:15 UTC

U.S. airport screening throughput in early 2026 remained higher than the same dates in 2025, even as policy and staffing turbulence in mid-to-late February appeared to soften the pace temporarily.

A matched-date comparison of Transportation Security Administration (TSA) daily checkpoint counts from Jan. 1 to Mar. 5 shows 2026 running about 3% above 2025 overall (mean +3.04%, median +3.24%).

The pattern was not smooth. In the Feb. 14–Feb. 28 window, year-over-year gains narrowed to +1.34% on average, then improved again in Mar. 1–Mar. 5 to about +7.00%.

The data suggests a short-lived soft patch rather than a sustained collapse in passenger screening volumes.

## Appendix: Method

- Pulled TSA daily checkpoint totals from:
  - current-year page (2026 dates)
  - 2025 archive page
- Extracted daily date/count pairs and built matched-date year-over-year comparisons for 2026-01-01 through 2026-03-05.
- Computed:
  - daily YoY percentage changes,
  - full-window mean/median,
  - sub-window means for Jan 1–Feb 13, Feb 14–Feb 28, and Mar 1–Mar 5.

## Appendix: Limitations

- TSA counts measure screened throughput, not wait times or traveler experience quality.
- Year-over-year daily comparisons can be affected by weekday/holiday composition.
- The February turbulence context is policy/operations reporting; this analysis only tests whether a broad throughput collapse appears in daily counts.

## Appendix: Confidence

**Medium.** The primary count series is direct and reproducible, but causal attribution (policy shock vs normal demand composition) remains uncertain without additional operational datasets.

## Appendix: Sources

1. [TSA checkpoint travel numbers (current)](https://www.tsa.gov/travel/passenger-volumes) — retrieved 2026-03-06 15:27 UTC
2. [TSA checkpoint travel numbers (2025 archive)](https://www.tsa.gov/travel/passenger-volumes/2025) — retrieved 2026-03-06 15:27 UTC
3. [NPR report on TSA PreCheck operational messaging during shutdown](https://www.npr.org/2026/02/22/nx-s1-5722770/homeland-security-suspends-tsa-precheck-and-global-entry-airport-security) — retrieved 2026-03-06 15:27 UTC
