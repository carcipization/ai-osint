# KEV 2026 is faster at ingesting newly published CVEs, but backlog clean-up still drives a meaningful share

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-05-kev-freshness-vs-backlog-composition-shift-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-05-kev-freshness-vs-backlog-composition-shift-osint-story.md)

**Dateline:** 2026-03-05 09:05 UTC

## AP preflight (publishability gate)
1. AP would run this now because KEV drives federal remediation deadlines and heavily influences enterprise patch triage; a composition shift in what gets added (newly published vs long-known flaws) changes immediate operational prioritization.
2. New here: matched-window evidence that 2026 KEV additions skew materially fresher than 2025 (median lag from CVE publication to KEV inclusion fell), while a non-trivial long tail of old CVEs remains.
3. Affected: US federal agencies, critical-infrastructure defenders, and enterprise vulnerability-management teams deciding between emergency patching and backlog burn-down.
4. Strongest “not a story” counterargument: this could be short-window noise caused by a few batch disclosure days or vendor clustering.
5. **Editor verdict: Publish** — this is decision-relevant now, methodologically reproducible, and adds a distinct insight beyond simple KEV count tracking.

## What changed and why this matters now
In a matched Jan 1–Mar 5 window, KEV additions in 2026 look **faster-moving** than in 2025 when measured as lag from CVE publication date to KEV date-added. But KEV still includes older CVEs at meaningful rates, which means defenders cannot treat the catalog as purely “new-threat feed.”

**Decision relevance:** triage policies should keep a dual-track posture (rapid-response for fresh KEV items + structured backlog reduction for older exploited flaws).

## Evidence
1. **CISA KEV catalog (primary):** 47 additions in 2026-01-01..2026-03-05 versus 50 in 2025-01-01..2025-03-05.  
   Source: [CISA KEV CSV](https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv)  
   Retrieval: 2026-03-05 09:04 UTC  
   Parameters: dateAdded filtered to matched windows above.

2. **MITRE CVE publication dates (independent primary source class):** datePublished fetched for each KEV CVE in both windows; lag computed as `dateAdded - datePublished` in days.  
   Source: [MITRE CVE API](https://cveawg.mitre.org/api/)  
   Retrieval: 2026-03-05 09:04 UTC  
   Parameters: per-CVE lookups for all KEV entries in both matched windows.

3. **Distribution shift toward fresher KEV additions:**
   - Median lag: **13 days (2026)** vs **36.5 days (2025)**
   - Share added within 30 days of CVE publication: **57.4% (2026)** vs **48.0% (2025)**
   - Same-year publication share: **53.2% (2026)** vs **48.0% (2025)**

4. **Backlog still material in 2026:**
   - Share older than 365 days at KEV inclusion: **23.4% (2026)** (vs **30.0%** in 2025 matched window)
   - Extreme examples in 2026 include CVEs originally published in 2009 and 2008 (e.g., CVE-2009-0556, CVE-2008-0015) entering KEV during this period.

## Method (reproducible)
- Pull KEV CSV from CISA.
- Filter entries by `dateAdded` in two matched windows: 2025-01-01..2025-03-05 and 2026-01-01..2026-03-05.
- Query MITRE CVE API for each CVE’s `datePublished`.
- Compute lag in days and compare medians/quantiles and threshold shares (`<=30`, `>365`).
- Sanity-check vendor concentration for each window to test whether one vendor alone explains the shift.

## Hypotheses and adjudication
- **H1 (fresh-intake shift):** 2026 KEV is ingesting more newly published CVEs faster than 2025.  
  Prediction: median lag falls and short-lag share rises.  
  **Status: Supported.**

- **H2 (pure backlog cycle):** 2026 KEV additions are mostly older CVEs, similar to backlog-dominant behavior.  
  Prediction: high `>365 day` share with no short-lag improvement.  
  **Status: Rejected.** Backlog remains but does not dominate as strongly.

- **H3 (vendor-batch artifact):** observed lag change is mostly one-vendor release behavior.  
  Prediction: shift disappears once vendor mix is inspected.  
  **Status: Mixed.** Vendor concentration exists (Microsoft remains top contributor), but lag improvement appears at portfolio level, not only one-vendor effect.

## Limitations
- Matched-window snapshot is short and can be affected by batch disclosure dynamics.
- MITRE `datePublished` is a useful anchor but does not capture private exploitation lead-time.
- This analysis measures **catalog inclusion timing**, not true first exploitation date.

## Confidence
**Medium.** Evidence uses two independent primary datasets with full-coverage per-CVE joins in-window, but interpretation is still sensitive to short-window composition effects.

## One-line significance
KEV currently signals both rapid exploitation response and ongoing legacy-risk exposure, so patch programs that optimize only for “new CVEs” are likely to miss a consequential share of exploited backlog risk.

## Source links
- [CISA Known Exploited Vulnerabilities catalog page](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [CISA KEV CSV feed](https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv)
- [MITRE CVE API](https://cveawg.mitre.org/api/)
