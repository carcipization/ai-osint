#!/usr/bin/env bash
set -euo pipefail

# Purpose:
# Run publish.py with the repo virtualenv to avoid host-python dependency drift.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

VENV_PY="./.venv/bin/python"

if [[ ! -x "$VENV_PY" ]]; then
  echo "[publish-with-venv] .venv missing; creating via make venv"
  make venv
fi

echo "[publish-with-venv] using $VENV_PY"
"$VENV_PY" scripts/publish.py
