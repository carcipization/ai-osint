from __future__ import annotations

from .state import ROTATION


def cadence_prompt(*, slot: str, to: str, state_file: str) -> str:
    return f"""Run the 3-hour AI-OSINT cycle using the current slot from state.

State + rotation:
- Slot source of truth: {state_file}
- Current slot for this run: {slot}
- Rotation: {' -> '.join(ROTATION)} -> repeat
- At end of run: advance to next slot in the rotation and persist.

Global requirements:
- Work in /home/pi/.openclaw/workspace/ai-osint
- Before publishing/editing: git fetch origin && git pull --rebase origin main
- Dateline format: **Dateline:** YYYY-MM-DD HH:MM UTC
- Include source links for datasets/stories
- Commit + push (rebase/retry up to 2x)
- Verify GitHub Pages build succeeded for latest commit before reporting success
- Always send Jon a concise Telegram summary to {to}

Slot rules:
- STORY_A/STORY_B: one NEW story (not follow-up), novelty gate 14 days
- DATASETS_A/DATASETS_B: add >=1 genuinely new dataset source to catalog, or explicit no-add with rejected leads
- DATASETS_OPTIMIZE: improve catalog structure/quality without churn
- FOLLOWUP: weighted sample of prior stories (5-10), publish only meaningful updates
- SKILL: improve skills/osint-journalism/SKILL.md
- SELF: one useful maintenance/automation task with explicit why

If Telegram send fails, report failure reason in final output."""


def oneoff_prompt(*, slot: str, to: str) -> str:
    return f"""Run a ONE-OFF {slot} task for AI-OSINT. This is out-of-cadence.

Hard constraints:
- Do NOT read/write cadence state files
- Do NOT alter scheduled cadence/rotation

Requirements:
- Repo: /home/pi/.openclaw/workspace/ai-osint
- Before edits: git fetch origin && git pull --rebase origin main
- Dateline format: **Dateline:** YYYY-MM-DD HH:MM UTC
- Include source links + limitations
- Commit + push (rebase/retry up to 2x)
- Verify GitHub Pages success for latest commit
- Send concise Telegram summary to {to}

Task-specific:
- STORY: publish one NEW story (not follow-up), novelty gate (not covered last 14 days)
- DATASETS: add >=1 genuinely new dataset source to catalog (or explicit no-add report)
"""
