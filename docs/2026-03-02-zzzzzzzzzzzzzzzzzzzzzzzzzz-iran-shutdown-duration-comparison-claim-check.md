# Claim check: Did Iran’s January 2026 internet shutdown outlast June 2025 and rival/beat November 2019?

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-02-zzzzzzzzzzzzzzzzzzzzzzzzzz-iran-shutdown-duration-comparison-claim-check.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-02-zzzzzzzzzzzzzzzzzzzzzzzzzz-iran-shutdown-duration-comparison-claim-check.md)


**Dateline:** 2026-03-02 18:02 UTC

## Verdict

**Partly supported (directionally strong, exact-hour precision unverified independently in this pass).**

An IODA Bluesky post claims comparative shutdown durations in Iran, including:
- Jan 2026: 171.477 hours
- June 2025: 48.5 hours
- Nov 2019: 164 hours

Cross-source evidence supports the **ordering** (January 2026 clearly much longer than June 2025 and in the same multi-day range as/above 2019), but this pass did not independently reproduce IODA’s exact decimal-hour values from raw time-series export.

## Claim provenance

- Platform: Bluesky
- Account: @ioda.live (IODA — Internet Outage Detection and Analysis)
- Post URL: [https://bsky.app/profile/ioda.live/post/3mcigxurkms2w](https://bsky.app/profile/ioda.live/post/3mcigxurkms2w)
- Post timestamp: 2026-01-15 20:40 (as displayed on Bluesky)

## What we checked

1. Whether independent monitoring/reporting confirms a major nationwide January 2026 shutdown beginning on Jan 8.
2. Whether independent sources indicate January 2026 duration was substantially longer than a short multi-day event.
3. Whether historical references for 2019 and 2025 are consistent with IODA’s comparative framing.

## Evidence

- IODA-linked country view from related thread context (primary monitoring context):
  [https://ioda.inetintel.cc.gatech.edu/country/IR?from=1767472578&until=1768509378&view=view1](https://ioda.inetintel.cc.gatech.edu/country/IR?from=1767472578&until=1768509378&view=view1)

- Cloudflare Radar analysis (Jan 13, 2026): reports traffic collapse on Jan 8 and near-zero national connectivity state, with discussion of prolonged disruption behavior.
  [https://blog.cloudflare.com/iran-protests-internet-shutdown/](https://blog.cloudflare.com/iran-protests-internet-shutdown/)

- BBC (Jan 28, 2026): describes shutdown as “nearly three weeks” after Jan 8, indicating a duration broadly consistent with very long, multi-day interruption windows.
  [https://www.bbc.com/news/articles/cz7y2ddgl23o](https://www.bbc.com/news/articles/cz7y2ddgl23o)

## Analysis

This is a **data-method** claim, where exact numbers depend on measurement definitions (what counts as “shutdown,” thresholds, and partial allow-list periods). In this check:

- Independent reporting strongly corroborates the Jan 2026 event as prolonged and severe.
- The comparative shape in the post (Jan 2026 >> June 2025; Jan 2026 around or above Nov 2019 duration scale) is plausible and supported directionally.
- Exact values like 171.477 hours should be treated as model/measurement outputs unless independently recomputed from raw outage intervals.

## Limitations

- No raw interval recomputation was performed in this pass.
- Source methods differ (traffic-based, routing-based, and journalistic summaries), so exact-hour parity is not expected.
- Access constraints prevented retrieval of one cited comparative IODA report URL variant during this run.

## Bottom line

The claim is **partly supported**: its comparative conclusion is well supported, but the exact decimal-hour figures remain unverified here and should be cited as IODA-specific estimates.
