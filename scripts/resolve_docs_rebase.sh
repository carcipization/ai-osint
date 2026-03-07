#!/usr/bin/env bash
set -euo pipefail

# Purpose:
# Resolve the common cadence rebase conflict pattern where generated docs
# files (especially docs/index.html and docs/latest.html) diverge.
#
# Safe scope:
# - Regenerates docs deterministically from markdown
# - Stages docs/
# - Continues rebase non-interactively

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[resolve-docs-rebase] rebuilding docs via publish_with_venv.sh"
bash scripts/publish_with_venv.sh

echo "[resolve-docs-rebase] staging docs/"
git add docs

echo "[resolve-docs-rebase] continuing rebase"
GIT_EDITOR=true git rebase --continue

echo "[resolve-docs-rebase] done"
