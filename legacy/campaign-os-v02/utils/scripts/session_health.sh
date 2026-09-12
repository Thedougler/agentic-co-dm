#!/usr/bin/env bash
# SessionStart hook — repo-wide health readout. Two printed checks, each
# silent when clean, plus a silent background lint sweep:
#   (a) whole-repo lint sweep: runs in the background only, no print —
#       `npm run lint:sweep` (autofix + every producer — wiki-cli),
#       ratchet-syncs the baseline down, and refreshes the cache
#       (`.claude/.lint-sweep.summary`) for `npm run lint:drain`/`/drain`
#       to read on demand. Findings are no longer printed into session
#       context here — run `npm run lint -- <path>` yourself to see them.
#   (b) fix-on-discovery queue: pending-ticket count.
#   (c) dirty tree: uncommitted vault/ files whose mtime predates the
#       last commit (work a prior session left unsaved).
# Fails open: any error — swallowed, never blocks session start.
set -uo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/env_local.sh"
REPO_ROOT="$CAMPAIGN_ROOT"
cd "$REPO_ROOT" 2>/dev/null || exit 0
SUM=".claude/.lint-sweep.summary"

# SessionStart's stdin JSON payload carries session_id (same shape
# hook payloads carry tool_input in) — used only to cap auto-drain
# (REFACTOR-PLAN.md P2.5) to one wave per session below; a payload without
# jq or a parseable session_id degrades to "unknown", which still caps
# fine (a wave still fires at most once per marker value).
payload="$(cat 2>/dev/null || true)"
session_id="$(printf '%s' "$payload" | jq -r '.session_id // empty' 2>/dev/null || true)"

# Lint findings are not printed at session start — $SUM is still refreshed
# below (background) for `npm run lint:drain`/`/drain` to read on demand;
# run `npm run lint -- <path>` yourself to see current findings.
# autofix + ratchet-sync + summary refresh in background for the next session
# — --fix only touches rules that declare themselves mechanically fixable
# (fixInfo); sync only ever lowers the committed floor; the JSON path
# wiki-cli's SQLite cache avoids the truncation issues the old
# piped-stdout approach was exposed to.
#
# This SessionStart hook fires on startup AND resume|clear|compact, so a long
# session with several compactions re-triggers it repeatedly. Without a lock,
# every trigger launched its own full lint pass (markdownlint + oxlint across
# the whole repo) regardless of whether a previous one was still running,
# stacking up overlapping node processes that starved CPU from every other
# hook's foreground work (measured: qmd_session_update.sh's normally-~5s
# `qmd update`+`qmd embed` ballooned to 25s+ under this contention). The
# pidfile below skips launching a duplicate refresh while one is still in
# flight — the next trigger picks it up once the lock clears.
#
# File-flag gate (user ruling 2026-08-02, dev-mode speed): touch
# .claude/.dev-mode-skip-lint-sweep to skip this background sweep entirely —
# (b)/(c) below still run. rm the file to restore the sweep. Env vars are
# not used here per .claude/rules/scripts.md — a spawned hook process
# doesn't inherit mid-session exports.
LOCK=".claude/.lint-sweep.lock"
if [ -f ".claude/.dev-mode-skip-lint-sweep" ]; then
  : # dev-mode: background lint sweep disabled, see flag comment above
elif [ -f "$LOCK" ] && kill -0 "$(cat "$LOCK" 2>/dev/null || echo 0)" 2>/dev/null; then
  : # a refresh is already running — skip, don't stack another one
else
  (
    npm run lint:sweep >/dev/null 2>&1 || true
    uv run --directory utils/wiki-cli wiki debt accept --force >/dev/null 2>&1 || true
    npm run lint:sweep -- --quiet > "$SUM" 2>/dev/null || true
    node utils/scripts/auto-drain.mjs "$session_id" >/dev/null 2>&1 || true
    rm -f "$LOCK"
  ) >/dev/null 2>&1 &
  echo $! > "$LOCK"
  disown 2>/dev/null || true
fi

# (b) fix-on-discovery pending tickets — name a manageable sample, cap the rest
tickets=$(grep -lE '^status:[[:space:]]*pending' .claude/fix-on-discovery/*.md 2>/dev/null || true)
q=$(printf '%s\n' "$tickets" | grep -c . || true)
if [ "${q:-0}" -gt 0 ]; then
  sample=$(printf '%s\n' "$tickets" | head -3 | xargs -n1 basename | paste -sd, -)
  restq=$((q - 3))
  more=""
  [ "$restq" -gt 0 ] && more=" (+$restq more)"
  echo "FIX-ON-DISCOVERY: $q pending ticket(s) in .claude/fix-on-discovery/ — start with: $sample$more."
fi

# (c) dirty files older than the last commit — name a manageable sample, cap the rest
last=$(git log -1 --format=%ct 2>/dev/null || echo 0)
old_files=""
old=0
while IFS= read -r f; do
  [ -f "$f" ] || continue
  m=$(stat -f %m "$f" 2>/dev/null || echo 0)
  if [ "${m:-0}" -lt "$last" ]; then
    old=$((old + 1))
    old_files="$old_files$f"$'\n'
  fi
done < <(git status --porcelain -- vault/ 2>/dev/null | sed 's/^...//')
if [ "$old" -gt 0 ]; then
  sample=$(printf '%s' "$old_files" | grep -v '^$' | head -5 | paste -sd, -)
  resto=$((old - 5))
  more=""
  [ "$resto" -gt 0 ] && more=" (+$resto more)"
  echo "DIRTY TREE: $old uncommitted vault/ file(s) predate the last commit — commit or discard them (vault/refs/runbook-wiki.md). Sample: $sample$more."
fi

exit 0
