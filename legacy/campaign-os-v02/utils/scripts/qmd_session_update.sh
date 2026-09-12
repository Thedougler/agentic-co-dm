#!/usr/bin/env bash
# SessionStart hook (startup|resume|clear|compact) — keeps this repo's qmd
# collections (world, pcs, sessions, external, wiki, campaign-docs, archive,
# inbox) in sync with what's on disk, so `qmd search`/`qmd query` never serve
# stale results from a prior session's edits. `qmd update` re-indexes text
# content; `qmd embed` generates vectors for anything update left pending —
# both run unconditionally across all collections since a full pass is fast
# enough here to not need per-collection scoping. Fails open: no qmd binary,
# no network, any error — swallowed, never blocks session start. Only
# output: one timing line on success; otherwise silent.
#
# `qmd embed` only warms the embedding model — a first `qmd query`/`vsearch`
# this session still lazily downloads the ~600MB-1GB reranker model
# on-demand, blocking whatever guardrail step triggered it (discovered
# 2026-07-29 verifying docs/guardrails/PROJECT.md PJ13's example command).
# Backgrounded here via nohup+disown so a cold cache never blocks session
# start OR the first real query later in the session.
set -uo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/env_local.sh"
REPO_ROOT="$CAMPAIGN_ROOT"
cd "$REPO_ROOT" 2>/dev/null || exit 0

command -v qmd >/dev/null 2>&1 || exit 0

qmd update >/dev/null 2>&1

# Guard against stacked embed processes: every session/resume fires this hook,
# so without a lock, multiple qmd embed runs pile up and each loads a ~650MB
# model — measured 5 concurrent instances consuming ~3.5GB RAM and starving CPU.
EMBED_LOCK=".claude/.qmd-embed.lock"
if [ -f "$EMBED_LOCK" ] && kill -0 "$(cat "$EMBED_LOCK" 2>/dev/null || echo 0)" 2>/dev/null; then
  exit 0  # embed already running — skip; next session picks up any remaining vectors
fi

nohup bash -c "
  qmd embed >/dev/null 2>&1
  rm -f '$REPO_ROOT/$EMBED_LOCK'
  qmd -c wiki query 'campaign' -n 1 >/dev/null 2>&1
" &
echo $! > "$EMBED_LOCK"
disown

exit 0
