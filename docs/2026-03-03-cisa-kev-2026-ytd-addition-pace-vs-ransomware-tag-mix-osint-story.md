# CISA KEV early-2026 signal: faster YTD additions, lower ransomware-tag share

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-03-cisa-kev-2026-ytd-addition-pace-vs-ransomware-tag-mix-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-03-cisa-kev-2026-ytd-addition-pace-vs-ransomware-tag-mix-osint-story.md)


**Dateline:** 2026-03-03 21:10 UTC

## Executive summary

A fresh pull of CISA’s Known Exploited Vulnerabilities (KEV) catalog shows a mixed signal:

- **2026 YTD additions (through Mar 3): 47 CVEs**
- Equivalent-date comparison: **2025 had 46** by Mar 3
- But the share tagged **known ransomware campaign use** is currently lower in 2026 (**6.4%**) than prior years (~22–24% in 2021–2024; 10.2% in 2025)

This is not a “risk is down” conclusion. It is a **composition shift** signal: exploit-confirmed additions are continuing at pace, while ransomware-tag labeling is currently less prevalent in the newly added set.

## Significance gate

- **Why this matters:** KEV is one of the highest-signal public baselines for “exploited in the wild.” A pace/mix shift changes how defenders should prioritize patching and how analysts interpret threat narratives.
- **Who is affected:** Enterprise vulnerability management teams, MSSPs, public-sector cyber defenders, and policy teams that use KEV for prioritization mandates.
- **Decision relevance:** Teams relying heavily on ransomware tags for triage may underweight non-ransomware exploitation pathways; patch prioritization should continue to anchor on KEV inclusion itself, not just ransomware annotation.

## What we checked

1. Pulled CISA KEV CSV and JSON feeds.
2. Counted total entries and grouped `dateAdded` by year.
3. Computed same-calendar-date YTD comparisons (through March 3) across years.
4. Calculated yearly share where `knownRansomwareCampaignUse == known`.

## Findings

### 1) Early-2026 KEV addition pace is slightly above same-date 2025

- 2026 YTD through Mar 3: **47**
- 2025 through Mar 3 equivalent: **46**
- 2024: **30**
- 2023: **19**
- 2022: **167** (outlier surge year)

### 2) Ransomware-tag share in 2026 entries is currently low

From the catalog snapshot used in this run:

- 2026: **3 / 47 (6.4%)**
- 2025: **25 / 245 (10.2%)**
- 2024: **42 / 186 (22.6%)**
- 2023: **43 / 187 (23.0%)**
- 2022: **123 / 555 (22.2%)**
- 2021: **76 / 311 (24.4%)**

### 3) Most recent additions in this pull

Latest `dateAdded` observed: **2026-03-03** (2 entries), including Broadcom and Qualcomm ecosystem items in the feed snapshot.

## Interpretation

The catalog currently suggests defenders should avoid overfitting to ransomware-labeled exploitation as the sole urgency heuristic. KEV growth in early 2026 remains active, but attribution/tactic mix in labels can vary over time and may lag broader exploitation reality.

## Limitations

- KEV reflects CISA’s inclusion and update process, not all exploitation globally.
- Ransomware flag coverage depends on available reporting/attribution and may change after publication.
- Year-to-date comparisons are sensitive to calendar cutoffs and update timing.

## Source links

- CISA KEV JSON feed: [https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
- CISA KEV CSV feed: [https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv](https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv)
- CISA KEV catalog page: [https://www.cisa.gov/known-exploited-vulnerabilities-catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

## Bottom line

**New OSINT story finding:** early-2026 KEV additions are running at least as fast as last year’s same-date pace, while ransomware-tagged share in the 2026 cohort is notably lower so far. Prioritization should stay anchored on KEV inclusion first, with ransomware labeling treated as a secondary attribute.
