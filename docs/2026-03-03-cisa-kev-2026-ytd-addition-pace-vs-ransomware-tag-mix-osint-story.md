# CISA KEV in early 2026: addition pace holds while ransomware-labeled share is lower

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-03-cisa-kev-2026-ytd-addition-pace-vs-ransomware-tag-mix-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-03-cisa-kev-2026-ytd-addition-pace-vs-ransomware-tag-mix-osint-story.md)

**Dateline:** 2026-03-03 21:10 UTC

A fresh pull of CISA’s Known Exploited Vulnerabilities (KEV) catalog shows steady early-year addition pace with a different tag mix than recent years.

Through March 3, 2026, the catalog shows 47 additions, slightly above the same-date total of 46 in 2025 and above 30 in 2024 and 19 in 2023. The 2022 window remains an outlier at 167.

The share marked as known ransomware campaign use is lower in the 2026 snapshot: 3 of 47 entries (6.4%), versus 10.2% in 2025 and roughly 22–24% in 2021–2024.

That does not imply lower exploitation risk overall. It indicates composition change in currently labeled entries: exploit-confirmed additions remain active while ransomware-tag prevalence in the newly added set is lower in this snapshot.

For defenders, that means triage should not over-index on ransomware labels alone when evaluating KEV urgency.

## Appendix: Method

- Pulled CISA KEV CSV and JSON feeds.
- Counted yearly additions and same-calendar-date windows through March 3.
- Calculated yearly share where `knownRansomwareCampaignUse == known`.

## Appendix: Limitations

- KEV reflects CISA inclusion and update timing, not all exploitation globally.
- Ransomware labels depend on available attribution and may be updated later.
- Same-date YTD comparisons are sensitive to snapshot timing.

## Appendix: Confidence

**Medium.** The pace and mix signal is clear in the current snapshot, but composition can shift as entries are updated.

## Appendix: Sources

1. [CISA KEV JSON feed](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
2. [CISA KEV CSV feed](https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv)
3. [CISA KEV catalog page](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
