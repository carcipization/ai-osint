# Microsoft accounted for about one-fifth of CISA KEV additions in early 2026, in line with recent years

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-09-microsoft-share-of-kev-additions-remained-elevated-in-early-2026-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-09-microsoft-share-of-kev-additions-remained-elevated-in-early-2026-osint-story.md)

**Dateline:** 2026-03-09 17:44 UTC

## Story
Microsoft vulnerabilities made up about one-fifth of CISA’s Known Exploited Vulnerabilities (KEV) additions in early 2026, according to CISA’s machine-readable catalog feed.

In the January 1 to March 9 window, 11 of 52 newly added KEVs list `vendorProject` as Microsoft (about 21.2%). That share is close to the same-window pattern seen in recent years: about 20.0% in 2025 (10 of 50), 16.7% in 2024 (6 of 36), and 22.7% in 2023 (5 of 22).

The main signal is concentration stability rather than a fresh spike: Microsoft remains the largest single vendor bucket in this slice, but the current share is not materially outside the recent range for the same point in the calendar. For defenders, that supports sustained patch focus on Microsoft-exposed estates while avoiding over-interpreting this as a new structural break.

## Appendix: Method
- Pulled CISA KEV JSON feed on 2026-03-09 UTC.
- Filtered entries by `dateAdded` using same-window cutoff (`MM-DD <= 03-09`) for years 2023-2026.
- Grouped by `vendorProject` and calculated Microsoft share for each year-window.
- Compared 2026 share against prior same-window values for directional context.

## Appendix: Limitations
- `vendorProject` naming is catalog metadata and may not map cleanly to product-family exposure in enterprise environments.
- KEV additions are release-batch driven; short windows can shift quickly after new postings.
- This analysis does not estimate exploit prevalence by vendor outside KEV scope.
- What would change this conclusion: a near-term KEV batch dominated by non-Microsoft vendors or a sharp Microsoft-only surge that moves share outside the recent same-window band.

## Appendix: Confidence
**Confidence: Medium-high.**

High confidence in feed-state counts and share arithmetic; medium-high confidence in interpretation because catalog composition can change abruptly with batch updates.

## Appendix: Sources
- CISA KEV machine-readable feed (JSON): [https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
- CISA KEV catalog landing page: [https://www.cisa.gov/known-exploited-vulnerabilities-catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
