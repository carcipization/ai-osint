# OSINT Journalism Skill

Purpose: produce high-quality automated OSINT journalism: fast, clear, evidence-based reporting that reads like publishable wire copy.

## Editorial north star

- Optimize for: **story quality**, **reporting reliability**, **publication speed**.
- Rules are tools, not outcomes.
- If a checklist step does not materially improve journalism, skip or shorten it.

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

## Story format (AP style, mandatory)

Write story posts in AP-style narrative flow first, then append technical notes.

Plain-language rule (mandatory):
- Assume an informed general reader, not a specialist.
- Define acronyms and specialist terms at first mention (e.g., KEV, CVE, EPSS, BOD).
- Prefer concrete language over insider shorthand.

Required order:
1. Headline
2. Dateline
3. **Story** (clean narrative: lead, nut graf, key findings, implications)
4. **Appendix: Method**
5. **Appendix: Limitations**
6. **Appendix: Confidence**
7. **Appendix: Sources**

Do **not** include editorial throat-clearing in the story body (e.g., “why this is publishable”, “AP preflight”, internal gate checklists). If editorial justification is needed, store it in `research-traces/`.

## Method notes for internet-shutdown stories

When checking outage-duration claims:
- Separate **ordering conclusion** (A longer than B) from **exact-hour precision**.
- Treat decimal-hour values as method outputs unless independently recomputed.
- Look for partial-allowlist phases; “near zero” traffic can still coexist with whitelisted access.
- Triangulate at least two independent measurement families when possible:
  - routing/visibility signals
  - traffic/application-layer signals

## Follow-up slot discipline

- Sample recent high-impact stories (target 3–10, based on available time).
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
