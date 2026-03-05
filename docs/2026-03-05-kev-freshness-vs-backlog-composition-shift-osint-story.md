# U.S. exploited-vulnerability list is adding newer bugs faster in 2026, but old high-risk flaws still keep getting added

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-05-kev-freshness-vs-backlog-composition-shift-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-05-kev-freshness-vs-backlog-composition-shift-osint-story.md)

**Dateline:** 2026-03-05 09:05 UTC

## Story
CISA’s **Known Exploited Vulnerabilities** list (usually called the **KEV catalog**) is a U.S. government list of software security flaws that are confirmed to be used by attackers in real-world intrusions.

Each flaw is tracked by a **CVE** ID (Common Vulnerabilities and Exposures), which is the standard public identifier for a specific software bug.

In early 2026, the KEV catalog appears to be picking up newly published CVEs faster than it did in the same period of 2025. But older bugs are still being added at meaningful levels. In plain terms: defenders still need to do two jobs at once — respond quickly to newly exploited bugs and keep grinding through older exploited backlog.

## Key findings
1. **Catalog activity is similar year over year in the matched window.**
   - KEV additions from Jan. 1 to Mar. 5:
     - **2026: 47**
     - **2025: 50**

2. **Time from CVE publication to KEV inclusion got shorter in 2026.**
   - Median lag:
     - **2026: 13 days**
     - **2025: 36.5 days**
   - Added within 30 days of CVE publication:
     - **2026: 57.4%**
     - **2025: 48.0%**

3. **Older exploited bugs are still a substantial part of the list.**
   - Entries added more than a year after CVE publication:
     - **2026: 23.4%**
     - **2025: 30.0%**
   - Some 2026 additions trace back to very old CVEs (including 2008–2009-era IDs).

## Hypotheses and adjudication
- **H1 (faster fresh intake):** KEV is now pulling in newly published CVEs faster.  
  **Status: Supported.**

- **H2 (still mostly backlog):** KEV additions are mainly old CVEs.  
  **Status: Not supported as the main pattern.** Backlog is still material, but not dominant.

- **H3 (single-vendor artifact):** This shift is mostly one vendor’s release behavior.  
  **Status: Mixed.** Vendor concentration exists, but the faster pattern is visible at overall portfolio level.

## One-line significance
If teams treat KEV as only a “new bug” feed, they will miss a meaningful share of actively exploited older vulnerabilities.

## Appendix: Method
- Pulled CISA KEV CSV data.
- Filtered two matched windows: 2025-01-01..2025-03-05 and 2026-01-01..2026-03-05.
- Pulled CVE publication dates from MITRE CVE API.
- Computed lag in days (`dateAdded - datePublished`) and compared medians and threshold shares.
- Checked vendor concentration as a confounder test.

## Appendix: Limitations
- This is a short matched-window snapshot and can move with batch updates.
- CVE publication date is an anchor, not the same as first observed exploitation.
- Results describe **catalog timing**, not total global exploitation timing.

## Appendix: Confidence
**Medium.** The direction of change is clear in two primary-source datasets, but short-window composition effects can still shift percentages.

## Appendix: Sources
- [CISA Known Exploited Vulnerabilities catalog page](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [CISA KEV CSV feed](https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv)
- [MITRE CVE API](https://cveawg.mitre.org/api/)
