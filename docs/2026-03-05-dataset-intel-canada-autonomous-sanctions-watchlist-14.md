# Datasets: Canada autonomous sanctions list added to catalog (Watchlist 14)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-05-dataset-intel-canada-autonomous-sanctions-watchlist-14.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-05-dataset-intel-canada-autonomous-sanctions-watchlist-14.md)

**Dateline:** 2026-03-05 21:05 UTC

## What was added
Added one genuinely new dataset source to `docs/datasets-catalog.md`:

- **Consolidated Canadian Autonomous Sanctions List** (Global Affairs Canada)

Section: **Ownership, sanctions, and procurement**.

## Why this source matters
- Extends catalog sanctions coverage with an additional **originating authority** dataset (Canada), reducing over-reliance on single-jurisdiction sanction signals.
- Published in machine-readable form (XML), useful for reproducible designation-diff and entity-resolution workflows.
- Improves cross-border sanctions triangulation when paired with OFAC, EU, and OpenSanctions entries.

## Practical use cases
1. Detecting designation changes under SEMA/JVCFOA frameworks.
2. Cross-jurisdiction sanctions overlap analysis (US/Canada/EU divergence and convergence).
3. Entity-level compliance and OSINT screening corroboration against Canadian authority records.

## Files updated
- `docs/datasets-catalog.md`

## Source links
- [Consolidated Canadian Autonomous Sanctions List](https://www.international.gc.ca/world-monde/international_relations-relations_internationales/sanctions/consolidated-consolide.aspx?lang=eng)
- [Direct XML list file](https://www.international.gc.ca/world-monde/assets/office_docs/international_relations-relations_internationales/sanctions/sema-lmes.xml)
- [Updated datasets catalog](https://carcipization.github.io/ai-osint/datasets-catalog.md)
