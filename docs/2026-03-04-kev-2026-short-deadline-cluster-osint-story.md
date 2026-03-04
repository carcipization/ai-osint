# CISA KEV in early 2026 shows an unusually high share of 2–3 day remediation deadlines

**Human-readable HTML:** https://carcipization.github.io/ai-osint/2026-03-04-kev-2026-short-deadline-cluster-osint-story.html
**LLM-friendly Markdown:** https://carcipization.github.io/ai-osint/2026-03-04-kev-2026-short-deadline-cluster-osint-story.md

**Dateline:** 2026-03-04 21:07 UTC

## AP editor preflight (publishability gate)
1) **Why this is a story AP would run today:** CISA’s KEV catalog drives real patching priorities across government and industry. A measurable shift toward very short remediation windows is operationally relevant now.
2) **What is genuinely new vs already known:** Prior KEV reporting often tracks counts. This run isolates a **deadline-structure anomaly**: in 2026 YTD, a much larger share of additions carry 2–3 day due-date windows than equivalent early-year periods.
3) **Who is affected and what changes because of this:** Vulnerability management teams, public-sector agencies, and MSSPs face tighter execution windows; triage and emergency patch workflows need more pre-positioned surge capacity.
4) **Strongest counterargument for “not a story”:** Small early-year sample effects can exaggerate percentages, and KEV due-date policy may be context-specific to certain vulnerabilities.
5) **Editor verdict:** **Publish** — this is a concrete, decision-relevant timing signal in a high-impact federal baseline dataset.

## Significance gate
- **Why it matters:** Patch urgency is determined by deadline windows, not just KEV inclusion counts.
- **Who is affected:** Public-sector defenders, critical infrastructure operators, enterprise SOC/vuln teams, and cyber-insurance risk teams using KEV-driven prioritization.
- **Decision relevance:** Teams may need to shift from weekly batching toward immediate response playbooks when short-window KEV entries cluster.

## What we measured
Using CISA KEV CSV, we computed `dueDate - dateAdded` (lead time in days) and compared early-year windows through **March 4** across years.

### Same-date comparison (through Mar 4)
- **2026:** 47 additions; **8** had due-date lead time **<=7 days** (**17.0%**), and all 8 were **<=3 days** (**17.0%**)
- **2025:** 50 additions; **2** <=7 days (**4.0%**), **0** <=3 days
- **2024:** 31 additions; **4** <=7 days (**12.9%**), **1** <=3 days (**3.2%**)
- **2023:** 19 additions; **0** <=7 days
- **2022:** 167 additions; **0** <=7 days

### 2026 short-deadline cluster examples
Recent 2–3 day lead-time entries in the feed snapshot include vulnerabilities tied to vendors such as Cisco, Dell, SolarWinds, and BeyondTrust.

## Interpretation
This is not simply “more KEV entries.” It indicates a **faster remediation tempo requirement** in the early-2026 cohort, with deadline compression concentrated in specific bursts. For operations, that changes staffing and escalation assumptions.

## Limitations
- Early-year sample size is limited; percentages can move quickly with new additions.
- CISA due dates reflect federal remediation policy context and do not directly measure global exploit prevalence.
- Vendor examples are descriptive, not causal attribution.

## Sources
- CISA KEV CSV feed: https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv
- CISA KEV catalog page: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA KEV JSON feed: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
