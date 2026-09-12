#!/usr/bin/env bash
set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() {
  printf '%s\n' "$1" >&2
  exit 1
}

command -v qmd >/dev/null 2>&1 || fail "qmd missing from PATH; install @tobilu/qmd"

errf="$(mktemp)"
outf="$(mktemp)"
cleanup() { rm -f "$errf" "$outf"; }
trap cleanup EXIT

qmd_ok() {
  if ! qmd "$@" >"$outf" 2>"$errf"; then
    msg="$(tr '\n' ' ' <"$errf" | sed 's/  */ /g')"
    case "$msg" in
      *NODE_MODULE_VERSION*|*better-sqlite3*|*ERR_DLOPEN*)
        fail "qmd sqlite ABI load failed (better-sqlite3); rebuild qmd for this Node"
        ;;
    esac
    fail "qmd $* failed: ${msg:0:240}"
  fi
}

[[ -d .qmd ]] || qmd_ok init

qmd_ok collection list
listed="$(cat "$outf")"
ensure_collection() {
  name="$1"
  path="$2"
  if ! printf '%s\n' "$listed" | grep -q "^${name} "; then
    [[ -d "$path" ]] || fail "required collection ${name} cannot be added; path missing: ${path}"
    qmd_ok collection add "$path" --name "$name" --mask '**/*.md'
  fi
}

ensure_collection wiki "${ROOT}/wiki"
ensure_collection shattered-sea "/Users/nick/Documents/ai-co-dm/campaigns/shattered-sea"
ensure_collection legacy-ss "/Users/nick/shattered-sea/wiki/shattered-sea"

qmd_ok update
qmd_ok status
status="$(cat "$outf")"
printf '%s' "$status" | grep -q "wiki (qmd://wiki/)" || fail "required collection wiki missing after status"
printf '%s' "$status" | grep -q "shattered-sea (qmd://shattered-sea/)" || fail "required collection shattered-sea missing after status"
printf '%s' "$status" | grep -q "legacy-ss (qmd://legacy-ss/)" || fail "required collection legacy-ss missing after status"

docs="$(printf '%s' "$status" | sed -n 's/.*Total:[[:space:]]*\([0-9]*\) files indexed.*/\1/p' | head -1)"
vecs="$(printf '%s' "$status" | sed -n 's/.*Vectors:[[:space:]]*\([0-9]*\) embedded.*/\1/p' | head -1)"
if [[ "${docs:-0}" -gt 0 && "${vecs:-0}" -eq 0 ]]; then
  qmd_ok embed
fi

qmd_ok search Hinewai -c wiki --format files
probe="$(cat "$outf")"
printf '%s' "$probe" | grep -qi 'Hinewai' || fail "probe search -c wiki missed existing wiki page Hinewai"

printf 'index: %s/.qmd/index.sqlite\n' "$ROOT"
printf 'collections: wiki, shattered-sea, legacy-ss\n'
printf 'last update: ok\n'
printf 'probe: Hinewai\n'
