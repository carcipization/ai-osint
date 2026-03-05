# DATASETS_A: OFAC Sanctions List Service added to catalog (Watchlist 13)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-05-dataset-intel-ofac-sanctions-list-service-watchlist-13.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-05-dataset-intel-ofac-sanctions-list-service-watchlist-13.md)

**Dateline:** 2026-03-05 15:04 UTC

## What was added
Added one genuinely new dataset source to `docs/datasets-catalog.md`:

- **OFAC Sanctions List Service (SLS)** ([link](https://ofac.treasury.gov/sanctions-list-service))

Placed under **Ownership, sanctions, and procurement**.

## Why this source matters
- Provides a direct **originating-authority** feed for U.S. sanctions lists (SDN and consolidated non-SDN), reducing dependence on downstream aggregators alone.
- Strengthens sanctions-wave and entity-screening OSINT work where designation timing and official list provenance are decision-critical.
- Complements (not replaces) existing catalog entries like OpenSanctions by improving primary-source triangulation.

## Practical use cases
1. Detecting fresh designation bursts and program-level shifts.
2. Verifying entity-list presence/absence directly against Treasury-distributed data.
3. Cross-matching sanctioned entities with ownership/procurement datasets (OpenCorporates, GLEIF, USAspending).

## Files updated
- `docs/datasets-catalog.md`

## Source links
- [OFAC Sanctions List Service](https://ofac.treasury.gov/sanctions-list-service)
- [OFAC list file format/download FAQ (topic 1641)](https://ofac.treasury.gov/faqs/topic/1641)
- [Updated datasets catalog](https://carcipization.github.io/ai-osint/datasets-catalog.md)
