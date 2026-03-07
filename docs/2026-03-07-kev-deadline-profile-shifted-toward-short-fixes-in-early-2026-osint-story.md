# CISA’s exploited-vulnerability list shifted toward shorter federal fix deadlines in early 2026

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-07-kev-deadline-profile-shifted-toward-short-fixes-in-early-2026-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-07-kev-deadline-profile-shifted-toward-short-fixes-in-early-2026-osint-story.md)

**Dateline:** 2026-03-07 23:21 UTC

The U.S. Cybersecurity and Infrastructure Security Agency’s Known Exploited Vulnerabilities (KEV) catalog has opened 2026 with a noticeably higher share of very short federal remediation deadlines than recent years.

A parse of CISA’s public KEV JSON feed shows 52 catalog additions through March 7. Of those, 44 carried the standard 21-day remediation window, while eight carried 2- or 3-day windows. That means 15.4% of 2026 year-to-date entries were assigned ultra-short deadlines.

At the same calendar point in 2025, the feed showed 50 additions and no 2- or 3-day windows. In that period, almost all entries used 21 days, with only two at seven days.

The shift does not, by itself, prove exploitation is rising across the full internet. It does indicate that, inside the KEV-driven federal patch workflow, CISA is using accelerated deadlines more often this year than in the recent baseline.

For defenders that mirror KEV as a prioritization signal, the operational implication is straightforward: teams should expect more cases where patching windows collapse from weeks to days.

## Appendix: Method

- Pulled CISA’s KEV machine-readable JSON feed and parsed each item’s `dateAdded` and `dueDate`.
- Computed remediation-window length as calendar days between `dateAdded` and `dueDate`.
- Built year-to-date slices through March 7 for 2025 and 2026 to keep cutoff dates aligned.
- Recomputed count shares from raw totals (e.g., 8 short-window entries out of 52 total in 2026 YTD).

## Appendix: Limitations

- KEV is a curated operational catalog, not a full census of all exploited vulnerabilities.
- Due-date selection is policy- and risk-informed; deadline length is not a direct severity score.
- Results are sensitive to feed revisions and future backfills.
- This analysis describes federal remediation scheduling patterns, not global victim impact.

## Appendix: Confidence

**Medium-high.** The deadline calculations are directly reproducible from CISA’s primary feed. Confidence is lower for broader ecosystem inference because KEV scope and due-date policy are purpose-built for federal operations.

## Appendix: Sources

1. [CISA Known Exploited Vulnerabilities Catalog (JSON feed)](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) — retrieved 2026-03-07 23:15 UTC
2. [CISA Known Exploited Vulnerabilities Catalog landing page](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — retrieved 2026-03-07 23:16 UTC
3. [Binding Operational Directive 22-01](https://www.cisa.gov/news-events/directives/binding-operational-directive-22-01) — retrieved 2026-03-07 23:16 UTC
