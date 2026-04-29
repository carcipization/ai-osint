# EVOLVE slot trace — 2026-04-29

## Hypothesis
Recent slots show no-publish outcomes caused partly by diffuse early-stage lead handling: too much effort is spent on low-consequence candidates before hard publishability checks are applied. A strict early triage architecture should raise publish hit-rate and reduce wasted depth work.

## Change made
Added a new **STORY candidate triage architecture** section to `skills/osint-journalism/SKILL.md` that introduces:
- a two-pass board (`candidate queue` -> `publish-ready queue`),
- explicit timeboxed challenge tests per candidate,
- hard abandon triggers for low-importance/low-decision-utility candidates,
- and a forced rotate rule to next candidate when verification stalls.

## Before/after checks
- Before: guidance encouraged candidate board usage but left escalation/de-escalation thresholds relatively open, which can cause over-investment in weak leads.
- After: triage now has deterministic escalation criteria and abort rules, pushing effort toward publishable-now candidates.

## Expected impact (next 7–14 days)
- Faster elimination of weak leads.
- More slot time spent on high-consequence candidates with better publishability odds.
- Higher STORY publication rate without lowering evidence/importance standards.
