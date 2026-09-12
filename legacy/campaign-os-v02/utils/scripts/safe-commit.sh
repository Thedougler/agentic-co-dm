#!/usr/bin/env bash
# safe-commit.sh — commit staged files without pre-commit's stash/restore cycle.
#
# pre-commit stashes unstaged tracked changes before running hooks and
# re-applies them after. When a background agent writes a file inside that
# window, the restore can clobber or revert the agent's write. This wrapper
# closes the race: it runs the same checks the pre-commit hooks run — on the
# STAGED copies only, via a temporary index checkout — then commits with
# --no-verify. Same gate, no stash.
#
# Usage: utils/scripts/safe-commit.sh -m "message" [-m "more"] <path>...
# Paths are `git add`ed, checked, committed. Any check failure aborts the
# commit; --fix-style findings must be fixed in the working tree and re-run
# (mirrors pre-commit's own fail-then-restage model).

set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

MSG_ARGS=()
PATHS=()
while [ $# -gt 0 ]; do
  case "$1" in
    -m) MSG_ARGS+=(-m "$2"); shift 2 ;;
    *) PATHS+=("$1"); shift ;;
  esac
done
[ ${#MSG_ARGS[@]} -gt 0 ] || { echo "safe-commit: -m required" >&2; exit 2; }
[ ${#PATHS[@]} -gt 0 ] || { echo "safe-commit: at least one path required" >&2; exit 2; }

git add -- "${PATHS[@]}"

STAGED=$(git diff --cached --name-only --diff-filter=ACMR)
[ -n "$STAGED" ] || { echo "safe-commit: nothing staged" >&2; exit 2; }

# Export the staged copies to a scratch tree so checks see exactly what will
# be committed, never the (possibly agent-owned) working-tree versions.
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
git checkout-index --prefix="$TMP/" -- $STAGED

fail=0
in_staged() { grep -qxF "$1" <<<"$STAGED"; }

# Mirror .pre-commit-config.yaml hook-for-hook (checks only; --fix variants
# run as plain checks here — a fix belongs in the working tree, not the tmp copy).
PY=$(grep -E '^utils/scripts/.*\.py$' <<<"$STAGED" || true)
if [ -n "$PY" ]; then
  (cd "$TMP" && ruff check --force-exclude $PY) || fail=1
  (cd "$TMP" && ruff format --check --force-exclude $PY) || fail=1
  (cd "$TMP" && python3 -m py_compile $PY) || fail=1
fi

# Markdown lint needs the real vault as cwd (wikilink/embed resolution), so
# tmp copies can't be linted. Lint the working-tree copy — identical to the
# staged copy at wave close; if they diverge (an agent wrote mid-commit),
# skip that file with a warning rather than lint content we aren't committing.
MD=$(grep -E '^vault/.*\.md$' <<<"$STAGED" | grep -Ev '/transcript(\.raw|-.*)?\.md$' || true)
if [ -n "$MD" ]; then
  LINTABLE=""
  while IFS= read -r f; do
    if git diff --quiet -- "$f" 2>/dev/null; then
      LINTABLE="$LINTABLE $f"
    else
      echo "safe-commit: WARNING — $f has unstaged changes; md lint skipped for it (staged copy commits as-is)" >&2
    fi
  done <<<"$MD"
  if [ -n "${LINTABLE// /}" ]; then
    utils/scripts/markdownlint-obsidian-wrapper.sh $LINTABLE || fail=1
  fi
fi

YML=$(grep -E '\.(ya?ml)$' <<<"$STAGED" | grep -Ev '^(site|node_modules|docs/campaign/legacy-skills|\.agents)/|(^|/)pnpm-lock\.yaml$|\.lock$' || true)
if [ -n "$YML" ]; then
  (cd "$TMP" && yamllint -c "$OLDPWD/.yamllint.yml" $YML) || fail=1
fi

if [ "$fail" -ne 0 ]; then
  echo "safe-commit: checks failed — fix in the working tree, re-run" >&2
  exit 1
fi

git commit --no-verify "${MSG_ARGS[@]}"
