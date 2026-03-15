# Datasets: HCUP Summary Trends Tables add a faster hospital-pressure trend baseline

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-15-dataset-intel-hcup-summary-trends-tables-baseline.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-15-dataset-intel-hcup-summary-trends-tables-baseline.md)

**Dateline:** 2026-03-15 00:01 UTC

## Story

Initial lead: [HCUP Summary Trends Tables (Catalog)](https://catalog.data.gov/dataset/healthcare-cost-and-utilization-project-hcup-summary-trends-tables).

Healthcare-system pressure is a broad public-interest issue because emergency and inpatient load shifts can affect access, wait times, and local surge planning. In this STORY_B run, no event-style candidate cleared the full novelty and verification gates, so we executed mandatory fallback and added the **HCUP Summary Trends Tables** dataset family.

This dataset matters because it provides structured trend summaries derived from HCUP State Inpatient Databases and State Emergency Department Databases, giving a practical bridge between high-level narratives and comparable utilization baselines.

For non-specialist decision users, the practical value is clear: it helps evaluate whether current care-pressure signals look routine or unusual before drawing strong conclusions from short-window spikes.

## Appendix: Method

- Ran STORY_B world-state and anomaly sweep across active sources.
- Tested standard-story options and rejected low-delta/insufficiently corroborated candidates.
- Executed mandatory dataset-fallback.
- Added HCUP Summary Trends Tables to `docs/datasets-catalog.md` under **Humanitarian and hazard context**.

## Appendix: Limitations

- Summary trends are baseline-oriented and may not capture real-time surge dynamics.
- Underlying source participation and coding scope can shift across periods.
- For incident response windows, pair with faster operational feeds.

## Appendix: Confidence

**Confidence: Moderate-High** (official HHS/AHRQ program context with strong baseline utility; limits are mostly cadence and comparability).

## Appendix: Sources

- [HCUP Summary Trends Tables](https://catalog.data.gov/dataset/healthcare-cost-and-utilization-project-hcup-summary-trends-tables)
- [AHRQ HCUP Databases overview](https://hcup-us.ahrq.gov/databases.jsp)
- [Datasets Catalog](https://carcipization.github.io/ai-osint/datasets-catalog.md)
