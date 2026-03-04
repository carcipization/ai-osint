# Dataset intel: GLEIF LEI Golden Copy for cross-border entity-resolution baselines (Watchlist #11)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-04-dataset-intel-gleif-lei-golden-copy-watchlist-11.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-04-dataset-intel-gleif-lei-golden-copy-watchlist-11.md)

**Dateline:** 2026-03-04 15:04 UTC

## Addition made (DATASETS_A)
Added one genuinely new source to the catalog:

- **Global Legal Entity Identifier Foundation (GLEIF) LEI Golden Copy**
  - URL: https://www.gleif.org/en/lei-data/gleif-golden-copy/download-the-concatenated-file
  - Cadence: daily file publication
  - Format: open CSV (concatenated + delta)

## Why this source is high-value
This adds a stronger cross-jurisdiction entity-resolution baseline for OSINT investigations where names alone are ambiguous (sanctions, procurement, ownership chains, shell-company reuse, and affiliate mapping).

Practical impact for future stories:
- Reduce false positives from same-name entities across countries.
- Improve linkage quality when combining OpenSanctions/OpenCorporates/Companies House with procurement awards.
- Support repeatable "who is the legal counterparty" checks before publication.

## Catalog updates
- Updated fast taxonomy line to include **GLEIF LEI** in ownership/procurement.
- Added full entry under **Ownership, sanctions, and procurement** with access/format, revision risk, operational role, and caveats.

## Source links
- GLEIF LEI Golden Copy download page: https://www.gleif.org/en/lei-data/gleif-golden-copy/download-the-concatenated-file
- GLEIF data-quality and formats overview: https://www.gleif.org/en/lei-data/gleif-concatenated-file
- Updated catalog: https://carcipization.github.io/ai-osint/datasets-catalog.md
