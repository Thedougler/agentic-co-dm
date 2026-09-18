#!/usr/bin/env bash
set -eu

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# Keep the hook cheap and predictable; successive writes drain the backlog.
max_embed_docs="${QMD_HOOK_MAX_DOCS:-128}"
max_embed_mb="${QMD_HOOK_MAX_MB:-16}"
lock_wait="${QMD_HOOK_LOCK_WAIT:-30}"
lock_dir="${QMD_HOOK_LOCK_DIR:-$ROOT/.qmd/qmd-hook.lock}"
cmd_timeout="${QMD_HOOK_TIMEOUT:-15}"


fail() {
  printf 'qmd-hook: %s\n' "$1" >&2
  exit 1
}

warn() {
  printf 'qmd-hook: %s\n' "$1" >&2
}

# CI environments may have no QMD installation; that is a silent no-op.
command -v qmd >/dev/null 2>&1 || exit 0

[[ "$max_embed_docs" =~ ^[1-9][0-9]*$ ]] || fail "QMD_HOOK_MAX_DOCS must be a positive integer"
[[ "$max_embed_mb" =~ ^[1-9][0-9]*$ ]] || fail "QMD_HOOK_MAX_MB must be a positive integer"
[[ "$lock_wait" =~ ^[1-9][0-9]*$ ]] || fail "QMD_HOOK_LOCK_WAIT must be a positive integer"


lock_parent="$(dirname "$lock_dir")"
mkdir -p "$lock_parent" 2>/dev/null || fail "cannot create lock parent: $lock_parent"
deadline=$((SECONDS + lock_wait))
while ! mkdir "$lock_dir" 2>/dev/null; do
  (( SECONDS < deadline )) || fail "lock busy: $lock_dir"
  sleep 0.05 || fail "lock wait interrupted"
done
cleanup() {
  rm -rf "$lock_dir" 2>/dev/null || :
}
trap cleanup EXIT
trap 'cleanup; exit 1' HUP INT TERM
if ! printf '%s\n' "$$" >"$lock_dir/pid" 2>/dev/null; then
  fail "cannot write lock owner: $lock_dir"
fi


qmd_run() {
  local errf msg fatal="${QMD_HOOK_FATAL:-1}"
  if [[ "${1:-}" == "--warn-only" ]]; then
    fatal=0; shift
  fi
  if ! errf="$(mktemp 2>/dev/null)"; then
    fail "cannot create temporary error file"
  fi
  if ! timeout "$cmd_timeout" env -u CI qmd "$@" >/dev/null 2>"$errf"; then
    msg="$(tr '\n' ' ' <"$errf" | sed 's/[[:space:]][[:space:]]*/ /g')"
    rm -f "$errf" 2>/dev/null || :
    if (( fatal )); then
      fail "qmd $* failed: ${msg:-timed out after ${cmd_timeout}s}"
    else
      warn "qmd $* skipped: ${msg:-timed out after ${cmd_timeout}s}"
      return 0
    fi
  fi
  rm -f "$errf" 2>/dev/null || :
}

qmd_run update
# Embed is best-effort; successive hooks drain the backlog.
qmd_run --warn-only embed -c wiki --max-docs-per-batch "$max_embed_docs" --max-batch-mb "$max_embed_mb"
