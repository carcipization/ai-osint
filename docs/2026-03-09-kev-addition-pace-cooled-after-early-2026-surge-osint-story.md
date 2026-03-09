# CISA KEV addition pace cooled after an early-2026 surge, with no new entries since 2026-03-05

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-09-kev-addition-pace-cooled-after-early-2026-surge-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-09-kev-addition-pace-cooled-after-early-2026-surge-osint-story.md)

**Dateline:** 2026-03-09 16:48 UTC

## Story
CISA’s Known Exploited Vulnerabilities (KEV) catalog still shows a strong year-to-date start in 2026, but the near-term addition tempo has cooled in early March.

Using CISA’s machine-readable feed, 52 KEVs were added between 2026-01-01 and 2026-03-09, which remains above the same calendar-window totals in prior years (50 in 2025, 36 in 2024, and 22 in 2023). But only 7 of those 52 additions were posted in March through March 9, and the most recent `dateAdded` in the feed is 2026-03-05.

The practical read is that 2026 is still running ahead on cumulative additions, while short-window momentum has eased after a faster January-February period. For defenders using KEV as a workload signal, this supports separating cumulative pressure from week-to-week flow before reprioritizing patch operations.

## Appendix: Method
- Pulled CISA KEV JSON feed on 2026-03-09 UTC.
- Counted records by `dateAdded`.
- Computed cumulative additions for 2023-2026 in the same window (`MM-DD <= 03-09`).
- Computed 2026 monthly split (Jan, Feb, and Mar 1-9) and checked latest `dateAdded` in current feed.

## Appendix: Limitations
- KEV additions are event-driven and can arrive in bursts; short windows can reverse quickly.
- This is a catalog-flow analysis, not a direct measure of exploitation prevalence outside KEV scope.
- Feed updates can change near-term counts after publication time.
- What would change this conclusion: a new batch of post-2026-03-05 entries that restores March run-rate toward January-February levels.

## Appendix: Confidence
**Confidence: Medium-high.**

High confidence in feed-state counting and date-window arithmetic; medium-high confidence in interpretation because short-window pace signals are inherently volatile.

## Appendix: Sources
- CISA KEV machine-readable feed (JSON): [https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
- CISA KEV catalog landing page: [https://www.cisa.gov/known-exploited-vulnerabilities-catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
