#!/usr/bin/env bash
set -eu

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# Keep the hook cheap and predictable; successive writes drain the backlog.
max_embed_docs="${QMD_HOOK_MAX_DOCS:-128}"
max_embed_mb="${QMD_HOOK_MAX_MB:-16}"
lock_dir="${QMD_HOOK_LOCK_DIR:-$ROOT/.qmd/qmd-hook.lock}"

fail() {
  printf 'qmd-hook: %s\n' "$1" >&2
  exit 1
}

[[ "$max_embed_docs" =~ ^[1-9][0-9]*$ ]] || fail "QMD_HOOK_MAX_DOCS must be a positive integer"
[[ "$max_embed_mb" =~ ^[1-9][0-9]*$ ]] || fail "QMD_HOOK_MAX_MB must be a positive integer"

# CI environments may have no QMD installation; that is a silent no-op.
command -v qmd >/dev/null 2>&1 || exit 0

lock_parent="$(dirname "$lock_dir")"
mkdir -p "$lock_parent" 2>/dev/null || fail "cannot create lock parent: $lock_parent"
while ! mkdir "$lock_dir" 2>/dev/null; do
  sleep 0.05
done
cleanup() {
  rm -rf "$lock_dir"
}
trap cleanup EXIT HUP INT TERM
printf '%s\n' "$$" >"$lock_dir/pid"

qmd_run() {
  local errf msg
  errf="$(mktemp)"
  if ! env -u CI qmd "$@" >/dev/null 2>"$errf"; then
    msg="$(tr '\n' ' ' <"$errf" | sed 's/[[:space:]][[:space:]]*/ /g')"
    rm -f "$errf"
    fail "qmd $* failed: ${msg:-unknown error}"
  fi
  rm -f "$errf"
}

qmd_run update
qmd_run embed -c wiki --max-docs-per-batch "$max_embed_docs" --max-batch-mb "$max_embed_mb"
