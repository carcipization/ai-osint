# CISA KEV entries kept rising in 2026, while ransomware-tagged share stayed below prior years

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-08-kev-ransomware-tag-share-remained-below-prior-years-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-08-kev-ransomware-tag-share-remained-below-prior-years-osint-story.md)

**Dateline:** 2026-03-08 21:10 UTC

## Story
CISA’s Known Exploited Vulnerabilities (KEV) catalog reached 1,536 entries in the 2026-03-05 release, and 52 of those entries have been added so far in 2026, according to CISA’s machine-readable feed.

But the feed’s ransomware-labeled share has remained materially lower in the newest additions than in earlier years. In the same feed, only 3 of the 52 vulnerabilities added in 2026 are currently marked `knownRansomwareCampaignUse=Known` (about 5.8%), versus roughly 22% to 24% in 2021-2024 and about 10% in 2025.

The directional read is clear: catalog growth and ransomware-tag growth are not moving in lockstep right now. That does not mean ransomware risk is falling overall; it means the subset of KEV entries explicitly tied to known ransomware campaigns is growing more slowly than total KEV additions at this point in the year.

For operators using KEV as a patch-priority signal, the practical implication is to avoid treating the ransomware tag as a complete severity proxy. CISA’s Binding Operational Directive (BOD) 22-01 remediation deadlines still apply to all listed KEVs for federal civilian agencies, whether or not a ransomware campaign flag is present.

## Appendix: Method
- Pulled CISA KEV JSON feed (`known_exploited_vulnerabilities.json`) on 2026-03-08 UTC.
- Counted all vulnerabilities and grouped by `dateAdded` year.
- Computed yearly share of records where `knownRansomwareCampaignUse == "Known"`.
- Compared 2026 year-to-date share against prior-year baselines from the same feed.

## Appendix: Limitations
- The ransomware flag is a catalog attribute, not a full census of all ransomware exploitation in the wild.
- Recently added KEVs can receive additional context later; therefore year-to-date shares can revise.
- This analysis is KEV-internal and does not measure broader threat activity outside catalog scope.
- What would change this conclusion: a large wave of retrospective 2026 tag updates to `Known` that lifts the 2026 share toward prior-year ranges.

## Appendix: Confidence
**Confidence: Medium.**

High confidence in arithmetic and current feed-state counts; medium confidence in interpretation because the ransomware flag is update-sensitive and method-dependent as a policy/attribution field.

## Appendix: Sources
- CISA KEV machine-readable feed (JSON): [https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
- CISA KEV catalog landing page: [https://www.cisa.gov/known-exploited-vulnerabilities-catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- CISA BOD 22-01 directive page: [https://www.cisa.gov/binding-operational-directive-22-01](https://www.cisa.gov/binding-operational-directive-22-01)
