# CISA KEV deadline compression in early 2026: anomaly confirmed, likely a prioritization-shock signal (not just a count effect)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-04-kev-2026-short-deadline-cluster-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-04-kev-2026-short-deadline-cluster-osint-story.md)

**Dateline:** 2026-03-04 21:16 UTC

## Story
Using CISA KEV CSV, compute `dueDate - dateAdded` in days, then compare year-matched windows through **March 4**.

### Same-date comparison (through Mar 4)
- **2026:** 47 additions; **8/47 (17.0%)** had lead time **<=3 days**
- **2025:** 50 additions; **0/50 (0.0%)** <=3 days
- **2024:** 31 additions; **1/31 (3.2%)** <=3 days
- **2023:** 19 additions; **0/19 (0.0%)** <=3 days
- **2022:** 167 additions; **0/167 (0.0%)** <=3 days

### 2026 short-window cluster (<=3 days)
Eight entries cluster in late Jan–Feb, including Fortinet, Ivanti, SolarWinds (x2), BeyondTrust, Dell, and Cisco (x2).

## Hypotheses and adjudication
### H1 — Exploit urgency increased, forcing shorter remediation windows
- **Prediction:** short-window entries should co-occur with stronger urgency markers (e.g., active exploitation context, high operational risk products).
- **Test result:** **mixed support**. The cluster includes widely targeted enterprise edge/management products (supports urgency framing), but only **1/8** of <=3-day entries carried `knownRansomwareCampaignUse=Known` in the feed snapshot (weakens a ransomware-only explanation).
- **Status:** **mixed**.

### H2 — CISA process/policy normalization under BOD 22-01 is driving tighter timelines
- **Prediction:** short-window behavior can rise without broad ransomware tagging, and CISA framing should emphasize accelerated remediation for exploited vulns.
- **Test result:** CISA BOD 22-01 text explicitly frames KEV as accelerated mandatory remediation for federal agencies; CISA statements on retiring Emergency Directives indicate actions being folded into BOD 22-01 operations. This is consistent with process-driven compression.
- **Status:** **supported (moderate)**.

### H3 — Vendor-mix artifact (a few vendors/products created a temporary cluster)
- **Prediction:** <=3-day observations are concentrated in a handful of vendors/products and dates.
- **Test result:** supported. The 8 short-window entries are concentrated in a narrow time band (late Jan–Feb) and repeated vendor families (e.g., SolarWinds and Cisco each appear twice).
- **Status:** **supported**.

### H4 (null) — Pure random small-sample noise with no operational meaning
- **Prediction:** 2026 short-window share should be close to prior matched windows.
- **Test result:** not supported. 2026 is 17.0% vs 0.0% (2025), 3.2% (2024), 0.0% (2023), 0.0% (2022) in same-date windows.
- **Status:** **rejected for now** (though persistence still unproven).

## Provisional conclusion
The best current explanation is **H2 + H3**: a process-prioritization effect (accelerated federal remediation logic) interacting with a concentrated vendor/product wave, rather than a simple “more KEVs” pattern or a ransomware-only shift.

## What would confirm or falsify this in the next cycle
- **Confirm compression regime:** <=3-day share remains elevated over the next 30–60 days and spreads beyond current vendor concentration.
- **Falsify/soften:** metric mean-reverts quickly and new entries return to historical lead-time patterns.
- **Different mechanism signal:** sharp rise in `knownRansomwareCampaignUse=Known` among short-window entries would shift weight toward H1.

## Appendix: Method
- Pulled CISA KEV CSV snapshot.
- Computed lead time as `dueDate - dateAdded` for each entry.
- Compared same-date windows through March 4 across years.
- Flagged short-window entries (`<=3 days`) and inspected vendor/date concentration.

## Appendix: Limitations
- Early-year denominator is still modest; percentages can swing quickly.
- KEV due dates reflect federal policy obligations, not direct global exploit prevalence.
- This is an observational inference; no causal claim about internal CISA decision criteria.

## Appendix: Confidence
**Medium.** The anomaly is strong and reproducible; mechanism attribution is plausible but not yet definitive.

## Appendix: Sources
1. [CISA KEV CSV feed](https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv)
   - Retrieved: 2026-03-04 ~21:13 UTC
   - Parameters: full feed; filtered by `dateAdded <= MM-DD 03-04` per year; computed lead-time as `dueDate - dateAdded`.
2. [CISA BOD 22-01 page](https://www.cisa.gov/news-events/directives/bod-22-01-reducing-significant-risk-known-exploited-vulnerabilities)
   - Retrieved: 2026-03-04 ~21:14 UTC
   - Used for directive framing and accelerated remediation language.
3. [CISA Emergency Directives retirement note](https://www.cisa.gov/news-events/news/cisa-retires-ten-emergency-directives-marking-era-federal-cybersecurity)
   - Retrieved: 2026-03-04 ~21:14 UTC
   - Used for evidence that some directive actions were folded into BOD 22-01 operations.
