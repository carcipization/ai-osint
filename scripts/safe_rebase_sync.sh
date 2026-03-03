#!/usr/bin/env bash
set -euo pipefail

# Purpose:
# Keep cadence runs resilient when repo has tracked local runtime state
# (notably .cron_checkpoint_mode.txt) that would otherwise block pull --rebase.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

RUNTIME_FILES=(
  ".cron_checkpoint_mode.txt"
)

echo "[safe-sync] fetch origin"
git fetch origin

if git diff --quiet -- "${RUNTIME_FILES[@]}"; then
  echo "[safe-sync] runtime files clean; pull --rebase"
  git pull --rebase origin main
  exit 0
fi

STAMP="safe-sync-$(date -u +%Y%m%dT%H%M%SZ)"
echo "[safe-sync] stashing runtime files: ${RUNTIME_FILES[*]} ($STAMP)"
git stash push -m "$STAMP" -- "${RUNTIME_FILES[@]}" >/dev/null

restore_needed=1
cleanup() {
  if [[ "$restore_needed" -eq 1 ]]; then
    git stash pop >/dev/null || true
  fi
}
trap cleanup EXIT

echo "[safe-sync] pull --rebase origin main"
git pull --rebase origin main

echo "[safe-sync] restoring stashed runtime files"
git stash pop >/dev/null || true
restore_needed=0
trap - EXIT

echo "[safe-sync] done"
