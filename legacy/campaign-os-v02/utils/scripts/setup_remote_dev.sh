#!/usr/bin/env bash
# Provisions a fresh checkout (cloud VM, Codespace, CI runner, or a second
# machine) with everything campaign-os needs to run its scripts, hooks, and
# skills: root + utils/site Node deps, the dndsim Python env (uv), qmd on
# PATH (session hooks call it directly, not through `npm run`), and the
# pre-commit git gate. Idempotent — safe to re-run after a `git pull`.
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/env_local.sh"
cd "$CAMPAIGN_ROOT"

log() { printf '\n==> %s\n' "$1"; }
need() { command -v "$1" >/dev/null 2>&1; }

# pnpm's build-approval supply-chain gate exits 1 when a dep's install
# script isn't on the workspace's allowlist, even though the deps
# themselves installed fine — advisory, not a real failure. Treat it as
# one; anything else is a real install failure and re-raised.
pnpm_install() {
  local out status
  out="$(pnpm "$@" 2>&1)" && return 0
  status=$?
  echo "$out"
  if echo "$out" | grep -q 'ERR_PNPM_IGNORED_BUILDS'; then
    echo "note: build scripts ignored by pnpm's supply-chain gate — deps are installed; re-run with 'approve-builds' in place of 'install' to review/allow them if something's missing at runtime." >&2
    return 0
  fi
  return "$status"
}

log "Node / pnpm"
need node || { echo "node not found — install Node 20+ first: https://nodejs.org" >&2; exit 1; }
if ! need pnpm; then
  echo "pnpm not found — enabling via corepack"
  corepack enable pnpm 2>/dev/null || npm install -g pnpm
fi
pnpm_install install
pnpm_install --dir utils/site install

log "qmd (search CLI — session hooks call it directly, needs to be on PATH)"
qmd_version="$(node -p "require('./package.json').devDependencies['@tobilu/qmd']" | tr -d '^')"
if ! need qmd; then
  npm install -g "@tobilu/qmd@${qmd_version}"
else
  echo "qmd already on PATH: $(qmd --version 2>/dev/null || echo unknown version)"
fi

log "uv / dndsim (Python combat engine)"
if ! need uv; then
  echo "uv not found — installing"
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
fi
uv sync --project utils/dndsim

log "pre-commit + yamllint (git commit gate, .pre-commit-config.yaml)"
need pre-commit || { uv tool install pre-commit; export PATH="$HOME/.local/bin:$PATH"; }
need yamllint || { uv tool install yamllint; export PATH="$HOME/.local/bin:$PATH"; }
pre-commit install

log ".env.local"
if [ ! -f .env.local ]; then
  cp .env.example .env.local
  echo "Created .env.local — fill in only the API keys the subsystems you use need."
else
  echo ".env.local already exists, leaving it alone."
fi

log "Done"
echo "Next: read CONFIG.md (which subsystems to enable), then CONTEXT.md or the campaign-os skill for orientation."
