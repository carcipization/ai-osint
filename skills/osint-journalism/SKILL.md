# OSINT Journalism Skill

Purpose: produce verification-first OSINT outputs that are reproducible, source-linked, and publication-safe under cadence pressure.

## Quick operating mode

1. **Classify the task first**
   - Claim-check (specific claim + provenance URL)
   - OSINT story (new analysis, not a claim-check)
   - Follow-up (re-check prior posts; publish only material changes)
   - Dataset task (catalog addition/optimization)

2. **Pick evidence tiers**
   - Tier 1: official registry/agency/primary release
   - Tier 2: structured monitoring systems (Cloudflare Radar, IODA, OONI, PortWatch, etc.)
   - Tier 3: media/social/aggregators (lead generation)

3. **Set publication confidence**
   - Supported / Not supported / Partly supported / Inconclusive
   - Add explicit caveats for model-derived metrics and method-sensitive estimates

## Claim-check minimum standard

A claim-check must include all of the following before publication:

- `## Claim provenance`
- Direct post URL(s) being checked
- Dateline in exact format: `**Dateline:** YYYY-MM-DD HH:MM UTC`
- Source links in evidence section
- Limitation notes (measurement and update-lag risks)

If no concrete claim-source URL exists, **do not publish in claim-check format**.

## Anti-pattern filter (important)

Avoid weak “mainstream-wire-only + regulator page” checks unless a novel OSINT angle exists.

A piece is novel when it adds at least one of:
- Primary data pull or time-series reconstruction
- Cross-source synthesis that changes the conclusion
- Geospatial or registry linkage not present in headline coverage
- Non-obvious inference that materially extends public reporting

## Publishability gate (AP editor test)

Before publishing a STORY, include a `## AP editor preflight (publishability gate)` section as a **proper Markdown ordered list** (`1.` to `5.`), covering:
1. Why AP would run this today (clear peg + broad relevance)
2. What is genuinely new versus already known
3. Who is affected and what changes because of this
4. The strongest argument that this is **not** a story
5. Editor verdict: publish/hold with one-sentence rationale

If any item is weak or hand-wavy, hold and pick another candidate.

### Fast preflight template (copy/paste)

1. **AP peg now:**
2. **New information in this run:**
3. **Affected parties + decisions impacted:**
4. **Best “not a story” argument:**
5. **Editor verdict (publish/hold + one sentence):**

## Method notes for internet-shutdown stories

When checking outage-duration claims:
- Separate **ordering conclusion** (A longer than B) from **exact-hour precision**.
- Treat decimal-hour values as method outputs unless independently recomputed.
- Look for partial-allowlist phases; “near zero” traffic can still coexist with whitelisted access.
- Triangulate at least two independent measurement families when possible:
  - routing/visibility signals
  - traffic/application-layer signals

## Follow-up slot discipline

- Sample 5–10 recent high-impact stories.
- Publish only if there is a **meaningful update**:
  - new primary data
  - official revision
  - materially changed conclusion
- If no material updates, explicitly say so for sampled items.

## Publication header format (mandatory)

At the top of every published markdown post, include clickable short links in this exact style:

- `**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/<slug>.html)`
- `**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/<slug>.md)`

Also require dateline exact format:

- `**Dateline:** YYYY-MM-DD HH:MM UTC`

## Cadence safety checks before push

- Run required local validators (`validate_claim_checks.py`, `validate_post_headers.py` when relevant)
- Confirm new output has working source links
- Keep commit scope tight (avoid unrelated HTML churn)
- Verify GitHub Pages endpoint reflects latest commit before reporting success
