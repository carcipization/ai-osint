# Datasets: sanctions-provenance guardrail added to catalog

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-06-datasets-optimize-sanctions-provenance-guardrail.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-06-datasets-optimize-sanctions-provenance-guardrail.md)

**Dateline:** 2026-03-06 03:09 UTC

## What changed
This optimization run improved catalog quality without adding/removing datasets:

1. Added an explicit **sanctions provenance rule** in the Ownership/sanctions/procurement section.
2. Refreshed catalog dateline after structural-quality edit.

## Why this matters
The sanctions section mixes source classes (originating authorities and aggregators). Without a clear hierarchy, follow-on story work can over-rely on aggregator data for final claims.

The new guardrail makes the intended workflow explicit:
- Aggregators for discovery and graphing
- Authority feeds for final evidentiary confirmation

## Files updated
- `docs/datasets-catalog.md`

## Source links
- [Updated datasets catalog](https://carcipization.github.io/ai-osint/datasets-catalog.md)
- [OFAC Sanctions List Service](https://ofac.treasury.gov/sanctions-list-service)
- [Consolidated Canadian Autonomous Sanctions List](https://www.international.gc.ca/world-monde/international_relations-relations_internationales/sanctions/consolidated-consolide.aspx?lang=eng)
- [OpenSanctions datasets index](https://www.opensanctions.org/datasets/)
