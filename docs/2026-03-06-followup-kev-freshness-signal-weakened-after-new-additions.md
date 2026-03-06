# FOLLOWUP: KEV “faster freshness” signal persists but weakened after March 6 additions

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-06-followup-kev-freshness-signal-weakened-after-new-additions.html)  
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-06-followup-kev-freshness-signal-weakened-after-new-additions.md)

**Dateline:** 2026-03-06 15:09 UTC

## What changed / why this update now

A same-method rerun of the March 5 KEV timing analysis with one additional day of data (through March 6) materially revised effect size.

The direction of the original claim still holds (2026 additions remain faster than 2025 in matched windows), but the gap narrowed substantially after newly added entries.

## Evidence

1. Matched windows (Jan 1–Mar 6):
   - **2025 additions:** 50
   - **2026 additions:** 52  
   Source: [CISA KEV CSV feed](https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv) (retrieved 2026-03-06 15:04 UTC)

2. Inclusion lag (`dateAdded - datePublished`) recomputed from KEV + MITRE CVE metadata:
   - **2025 median lag:** 35.5 days
   - **2026 median lag:** 24.0 days
   - **2025 share <=30 days:** 48.0%
   - **2026 share <=30 days:** 51.9%  
   Source: [MITRE CVE API](https://cveawg.mitre.org/api/) (queried 2026-03-06 15:03–15:07 UTC)

3. Compared with prior March 5 snapshot in this repo:
   - prior 2026 median lag estimate: **13 days**
   - prior <=30-day share estimate: **57.4%**
   - new values moved to **24 days** and **51.9%** respectively.  
   Source: [Prior story (2026-03-05)](https://carcipization.github.io/ai-osint/2026-03-05-kev-freshness-vs-backlog-composition-shift-osint-story.md)

## Method (reproducible)

- Pulled KEV CSV and filtered `dateAdded` into two matched windows:
  - 2025-01-01 to 2025-03-06
  - 2026-01-01 to 2026-03-06
- For each CVE in-window, pulled `datePublished` from MITRE CVE API.
- Calculated lag days as `dateAdded - datePublished`.
- Recomputed median lag and share added within 30 days.

## Why this is a meaningful follow-up

This update meets the follow-up publication gate because a **core quantitative result changed beyond prior uncertainty framing** (effect-size revision), even though directionality did not reverse.

## Limitations

- Daily additions can move early-year medians and shares quickly.
- CVE publication date is not exploitation start date.
- KEV reflects federal remediation prioritization timelines, not total global exploitation prevalence.

## Confidence

**Medium (revised toward caution).** The 2026-vs-2025 freshness edge remains, but this rerun shows the magnitude is more volatile and less extreme than yesterday’s snapshot suggested.

## Decision relevance

Defenders should still treat KEV as relatively faster on newer CVEs in 2026 than 2025, but planning assumptions should use **wide uncertainty bands** and daily refreshes rather than single-day effect-size estimates.
