#!/usr/bin/env bash
set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() {
  printf '%s\n' "$1" >&2
  exit 1
}

embed_mode=0
max_embed_docs=128
max_embed_mb=16

usage() {
  cat <<'EOF'
Usage: ./scripts/qmd-maintain.sh [--embed] [--max-embed-docs N] [--max-embed-mb N]

Routine maintenance updates the index, reports embedding backlog, and probes
wiki search. Use --embed explicitly for a foreground embedding pass.

Examples:
  ./scripts/qmd-maintain.sh
  ./scripts/qmd-maintain.sh --embed --max-embed-docs 64 --max-embed-mb 8
EOF
}

while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --embed)
      embed_mode=1
      shift
      ;;
    --max-embed-docs)
      [[ "$#" -ge 2 ]] || fail "--max-embed-docs requires a value"
      max_embed_docs="$2"
      embed_mode=1
      shift 2
      ;;
    --max-embed-mb)
      [[ "$#" -ge 2 ]] || fail "--max-embed-mb requires a value"
      max_embed_mb="$2"
      embed_mode=1
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage >&2
      fail "unknown option: $1"
      ;;
  esac
done

[[ "$max_embed_docs" =~ ^[1-9][0-9]*$ ]] || fail "--max-embed-docs must be a positive integer"
[[ "$max_embed_mb" =~ ^[1-9][0-9]*$ ]] || fail "--max-embed-mb must be a positive integer"

command -v qmd >/dev/null 2>&1 || fail "qmd missing from PATH; install @tobilu/qmd"

errf="$(mktemp)"
outf="$(mktemp)"
cleanup() { rm -f "$errf" "$outf"; }
trap cleanup EXIT

qmd_ok() {
  # Agent harnesses export CI=true; qmd then refuses local LLM (embed/query).
  if ! env -u CI qmd "$@" >"$outf" 2>"$errf"; then
    msg="$(tr '\n' ' ' <"$errf" | sed 's/  */ /g')"
    case "$msg" in
      *NODE_MODULE_VERSION*|*better-sqlite3*|*ERR_DLOPEN*)
        fail "qmd sqlite ABI load failed (better-sqlite3); rebuild qmd for this Node"
        ;;
    esac
    fail "qmd $* failed: ${msg:0:240}"
  fi
}

read_pending() {
  docs="$(printf '%s' "$status" | sed -n 's/.*Total:[[:space:]]*\([0-9]*\) files indexed.*/\1/p' | head -1)"
  vecs="$(printf '%s' "$status" | sed -n 's/.*Vectors:[[:space:]]*\([0-9]*\) embedded.*/\1/p' | head -1)"
  pending="$(printf '%s' "$status" | sed -n 's/.*Pending:[[:space:]]*\([0-9]*\) need embedding.*/\1/p' | head -1)"
  if [[ -z "$pending" && "${docs:-0}" =~ ^[0-9]+$ && "${vecs:-0}" =~ ^[0-9]+$ && "$vecs" -lt "$docs" ]]; then
    pending=$((docs - vecs))
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
ensure_collection archive "${ROOT}/wiki/_archive"

qmd_ok update
qmd_ok status
status="$(cat "$outf")"
printf '%s' "$status" | grep -q "wiki (qmd://wiki/)" || fail "required collection wiki missing after status"
printf '%s' "$status" | grep -q "shattered-sea (qmd://shattered-sea/)" || fail "required collection shattered-sea missing after status"
printf '%s' "$status" | grep -q "legacy-ss (qmd://legacy-ss/)" || fail "required collection legacy-ss missing after status"

read_pending

if [[ "$embed_mode" -eq 1 && "${pending:-0}" -gt 0 ]]; then
  qmd_ok embed -c wiki --max-docs-per-batch "$max_embed_docs" --max-batch-mb "$max_embed_mb"
  qmd_ok status
  status="$(cat "$outf")"
  read_pending
fi

qmd_ok search Hinewai -c wiki --format files
probe="$(cat "$outf")"
printf '%s' "$probe" | grep -qi 'Hinewai' || fail "probe search -c wiki missed existing wiki page Hinewai"

printf 'index: %s/.qmd/index.sqlite\n' "$ROOT"
printf 'collections: wiki, shattered-sea, legacy-ss\n'
printf 'last update: ok\n'
printf 'probe: Hinewai\n'
if [[ "${pending:-0}" -gt 0 ]]; then
  printf 'embeddings: pending %s (use --embed for an explicit batch)\n' "$pending"
else
  printf 'embeddings: current\n'
fi
