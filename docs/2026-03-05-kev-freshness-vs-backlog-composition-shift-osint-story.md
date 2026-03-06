# U.S. exploited-vulnerability list is moving faster on new CVEs in 2026, but older exploited bugs still matter

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-05-kev-freshness-vs-backlog-composition-shift-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-05-kev-freshness-vs-backlog-composition-shift-osint-story.md)

**Dateline:** 2026-03-05 09:05 UTC

The U.S. Cybersecurity and Infrastructure Security Agency’s Known Exploited Vulnerabilities (KEV) catalog appears to be adding newly published vulnerabilities faster in early 2026 than in the same window in 2025.

In matched Jan. 1 to Mar. 5 windows, catalog addition counts are similar (47 in 2026 versus 50 in 2025), but inclusion lag from CVE publication to KEV listing is shorter in 2026. The median lag in this analysis is 13 days in 2026 versus 36.5 days in 2025, and the share added within 30 days rises to 57.4% from 48.0%.

At the same time, older exploited vulnerabilities remain a substantial part of additions. Entries added more than one year after CVE publication are 23.4% in 2026 and 30.0% in 2025, including very old CVE identifiers.

The operational takeaway is dual-track: security teams cannot treat KEV as only a “fresh bug” stream, but they also cannot defer response on new exploit-confirmed CVEs because listing speed appears to be accelerating.

## Appendix: Method

- Pulled CISA KEV CSV for additions in two matched windows:
  - 2025-01-01 to 2025-03-05
  - 2026-01-01 to 2026-03-05
- Pulled CVE publication dates from MITRE CVE API.
- Computed lag as `dateAdded - datePublished`.
- Compared medians, 30-day inclusion share, and >365-day share.

## Appendix: Limitations

- Short-window snapshots can move with batch updates.
- CVE publication date is not the same as first exploitation date.
- Results describe catalog timing behavior, not total global exploitation timing.

## Appendix: Confidence

**Medium.** Directional shift is consistent across two primary data sources, but percentages can move as new entries are added.

## Appendix: Sources

1. [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
2. [CISA KEV CSV feed](https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv)
3. [MITRE CVE API](https://cveawg.mitre.org/api/)
