from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROTATION: tuple[str, ...] = (
    "STORY_A",
    "SELF",
    "DATASETS_A",
    "FOLLOWUP",
    "STORY_B",
    "SKILL",
    "DATASETS_B",
    "DATASETS_OPTIMIZE",
)


@dataclass(frozen=True)
class StatePaths:
    root: Path

    @property
    def state_dir(self) -> Path:
        return self.root / "state"

    @property
    def cadence_dir(self) -> Path:
        return self.state_dir / "cadence"

    @property
    def cadence_slot_file(self) -> Path:
        return self.cadence_dir / "current_slot.txt"

    @property
    def legacy_slot_file(self) -> Path:
        return self.root / ".cron_checkpoint_mode.txt"

    @property
    def followup_state_file(self) -> Path:
        return self.state_dir / "followup" / "checkpoint_state.json"


def ensure_dirs(paths: StatePaths) -> None:
    paths.cadence_dir.mkdir(parents=True, exist_ok=True)
    paths.followup_state_file.parent.mkdir(parents=True, exist_ok=True)


def _normalize(slot: str) -> str:
    v = slot.strip().upper()
    if v not in ROTATION:
        raise ValueError(f"Invalid slot '{slot}'. Expected one of: {', '.join(ROTATION)}")
    return v


def read_slot(paths: StatePaths, default: str = "STORY_A") -> str:
    ensure_dirs(paths)

    if paths.cadence_slot_file.exists():
        txt = paths.cadence_slot_file.read_text(encoding="utf-8").strip()
        if txt:
            return _normalize(txt)

    if paths.legacy_slot_file.exists():
        txt = paths.legacy_slot_file.read_text(encoding="utf-8").strip()
        if txt:
            slot = _normalize(txt)
            write_slot(paths, slot)
            return slot

    slot = _normalize(default)
    write_slot(paths, slot)
    return slot


def write_slot(paths: StatePaths, slot: str, *, sync_legacy: bool = True) -> str:
    ensure_dirs(paths)
    v = _normalize(slot)
    paths.cadence_slot_file.write_text(v + "\n", encoding="utf-8")
    if sync_legacy:
        paths.legacy_slot_file.write_text(v + "\n", encoding="utf-8")
    return v


def next_slot(slot: str, rotation: Iterable[str] = ROTATION) -> str:
    r = list(rotation)
    cur = _normalize(slot)
    idx = r.index(cur)
    return r[(idx + 1) % len(r)]


def advance_slot(paths: StatePaths) -> tuple[str, str]:
    cur = read_slot(paths)
    nxt = next_slot(cur)
    write_slot(paths, nxt)
    return cur, nxt
