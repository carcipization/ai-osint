# CISA KEV 2026 addition pace lost its year-to-date lead after a March 9 update, matching 2025 at the same point osint-story

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-10-kev-2026-addition-pace-lost-its-ytd-lead-after-march-9-update-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-10-kev-2026-addition-pace-lost-its-ytd-lead-after-march-9-update-osint-story.md)

**Dateline:** 2026-03-10 00:44 UTC

## Story
CISA’s Known Exploited Vulnerabilities (KEV) catalog added three more entries dated 2026-03-09, lifting 2026 year-to-date additions to 55 and eliminating the small lead 2026 previously held over 2025 in the same calendar window.

Using CISA’s machine-readable feed through March 10, both years now show 55 additions by this point in the calendar (Jan. 1 through Mar. 10), while earlier years remain lower (36 in 2024 and 24 in 2023). The newest feed state therefore shifts the trend from “2026 ahead of 2025” to “2026 tracking 2025 pace.”

The composition signal remains mixed. The ransomware-tagged share in 2026 additions is still low (3 of 55, about 5.5%), but the share of short remediation windows in 2026 rose with the latest additions: 11 of 55 entries now have due dates within 14 days of `dateAdded` (20.0%), up from the prior 8 of 52.

For patch-priority operations, the update matters because it changes the comparative pace narrative without changing the broader implication that KEV flow can quickly reprice short-window workload assumptions.

## Appendix: Method
- Pulled CISA KEV JSON feed on 2026-03-10 UTC.
- Counted additions by `dateAdded` year and compared same-window totals (`MM-DD <= 03-10`) for 2023-2026.
- Counted March 2026 additions by day to identify the latest update cluster.
- Recomputed two composition indicators for 2026 additions:
  - `knownRansomwareCampaignUse == Known` share
  - share of entries where `dueDate - dateAdded <= 14 days`

## Appendix: Limitations
- KEV updates are batch-driven; same-window comparisons can change materially after a single release.
- Catalog tags (including ransomware-use labeling) can revise after initial posting.
- Due-date-window share is policy/timing metadata, not a direct measure of exploit severity.
- What would change this conclusion: another near-term batch that puts 2026 clearly above or below the 2025 same-window count.

## Appendix: Confidence
**Confidence: Medium-high.**

High confidence in feed-state arithmetic; medium-high confidence in directional interpretation because short-window comparisons are update-sensitive.

## Appendix: Sources
- CISA KEV machine-readable feed (JSON): [https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
- CISA KEV catalog landing page: [https://www.cisa.gov/known-exploited-vulnerabilities-catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
