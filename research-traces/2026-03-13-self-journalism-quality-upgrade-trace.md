# SELF trace — journalism quality upgrade

**Date:** 2026-03-13
**Slot:** SELF
**Scope:** Improve OSINT journalism quality workflow (no publication)

## Starting with humility: weakest gaps identified first

Current weak spots I targeted:
1. Leads can still open with a strong claim before clearly anchoring attribution.
2. "Multiple sources" can still mask dependence on a single upstream origin.
3. Counter-evidence/uncertainty is sometimes present but not structurally guaranteed in opening paragraphs.

## External guidance reviewed (credible references)

1. Reuters Journalistic Standards (accuracy/sourcing)
   - https://reutersagency.com/about/standards-values/
   - Key points used: cross-check information; named sources preferred; be explicit about what is not known; "try to disprove as well as prove" initiative reporting.

2. AP behind-the-news note on anonymous sources and attribution discipline
   - https://www.ap.org/the-definitive-source/behind-the-news/when-is-it-ok-to-use-anonymous-sources/
   - Key points used: disputable secondhand facts must be attributed; attribution should be in the same sentence or immediately adjacent; anonymous sourcing needs strong justification and extra corroboration.

3. Bellingcat toolkit structure (evidence-family mindset for verification)
   - https://bellingcat.gitbook.io/toolkit
   - Key point used: investigations require combining different verification families (maps/geolocation/image-video/social/archive) rather than relying on one surface.

## What I learned

- Attribution placement is not a cosmetic style rule; it materially changes trust and falsifiability at read-time.
- Source count is a poor proxy for confidence unless upstream-origin independence is checked explicitly.
- Counter-evidence belongs early, not buried in later appendices, when claims are high impact or developing.

## Changes made

### 1) Added "Attribution-first paragraph protocol" to SKILL.md
- Forces the first two paragraphs to carry immediate attribution and explicit uncertainty/counterpoint.
- Evidence mapping:
  - AP attribution proximity requirement (same or adjacent sentence).
  - Reuters emphasis on source transparency and challenge-resilience.

### 2) Added "Corroboration independence ledger" to SKILL.md
- Introduces explicit `upstream_origin` + `independent_of` fields in private trace.
- Adds hard cap: if <2 independent evidence families remain after deduplication, verdict capped at provisional/inconclusive.
- Evidence mapping:
  - Reuters/AP corroboration rigor and source-credibility principles.
  - Bellingcat-style multi-family verification framing.

## Why these changes improve journalism outcomes

- Reduces unsupported lead framing and improves immediate reader provenance clarity.
- Prevents false confidence from circular sourcing.
- Increases reliability under fast-cycle OSINT conditions without adding heavy infrastructure overhead.
