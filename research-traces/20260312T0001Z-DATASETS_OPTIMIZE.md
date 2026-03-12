# DATASETS_OPTIMIZE trace — 2026-03-12 00:01 UTC

## Scope
Catalog quality/structure improvements only (no dataset publication post).

## Changes made to `docs/datasets-catalog.md`
1. Added retrieval alias token:
   - `humanitarian-risk-shards` for country-level risk indicator dataset families.
2. Expanded **Catalog maintenance rules** with two structure controls:
   - template consistency requirement for country-sharded datasets,
   - trace family-label requirement for multi-shard intake cycles.
3. Added **Country-shard dedup protocol (DATASETS_OPTIMIZE)** section:
   - emphasizes coverage-gap-driven shard selection,
   - discourages recency-only shard additions,
   - requires documenting selected vs intentionally skipped shard families.

## Why this improves catalog quality
- Reduces duplicate-pattern bloat from large country-shard families.
- Improves retrievability by introducing a stable alias for this recurring dataset type.
- Makes future dataset-intake decisions more auditable and repeatable.

## No-publish note
Per DATASETS_OPTIMIZE slot policy, no docs/GitHub Pages publication performed.
