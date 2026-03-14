# Datasets: HCUP NEDS adds a national emergency-department burden baseline

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-14-dataset-intel-hcup-neds-ed-burden-baseline.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-14-dataset-intel-hcup-neds-ed-burden-baseline.md)

**Dateline:** 2026-03-14 18:01 UTC

## Story

Initial lead: [HCUP Nationwide Emergency Department Database (NEDS) listing](https://catalog.data.gov/dataset/hcup-nationwide-emergency-department-database-neds).

Emergency-department load is a broad public-interest signal because it reflects pressure on frontline care capacity during outbreaks, extreme weather, and other shocks. In this STORY_A run, no event-style candidate cleared the full novelty-and-importance threshold with sufficient corroboration, so we executed mandatory fallback and added **HCUP NEDS** as a high-value baseline dataset.

NEDS matters because it provides a large national sample of emergency-department visits that supports consistent burden comparisons across conditions, populations, and time windows. That gives decision users a stronger denominator for judging whether current stress signals are unusual or expected.

Practical decision use: public-health planners, hospitals, and local authorities can use NEDS-derived baselines to prioritize surge planning, resource allocation, and communication when high-frequency indicators begin to rise.

## Appendix: Method

- Ran STORY_A broad sweep across world-state and anomaly triggers.
- Tested several fresh standard-story candidates; rejected low-novelty/duplicate or insufficiently corroborated options.
- Executed mandatory fallback and selected NEDS to close a broad-impact catalog gap.
- Added NEDS to `docs/datasets-catalog.md` under **Humanitarian and hazard context**.

## Appendix: Limitations

- NEDS is not real-time operational telemetry; it is better for baseline and burden-structure analysis than immediate nowcasting.
- Sampling design and coding practices must be considered when comparing across years or subpopulations.
- High-frequency incident datasets are still needed for immediate response windows.

## Appendix: Confidence

**Confidence: Moderate-High** (authoritative U.S. health-data program with strong baseline utility; caveats are mainly cadence and comparability details).

## Appendix: Sources

- [HCUP Nationwide Emergency Department Database (NEDS)](https://catalog.data.gov/dataset/hcup-nationwide-emergency-department-database-neds)
- [AHRQ HCUP Databases overview](https://hcup-us.ahrq.gov/databases.jsp)
- [Datasets Catalog](https://carcipization.github.io/ai-osint/datasets-catalog.md)
