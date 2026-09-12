#!/usr/bin/env bash
# markdownlint-obsidian-wrapper.sh — thin passthrough for
# node_modules/.bin/markdownlint-obsidian that adds one unambiguous line on
# a clean run.
#
# The package's default text formatter deliberately prints nothing when
# there are no findings (markdownlint-obsidian's DefaultFormatter.js: "Clean
# results produce an empty string so the CLI prints nothing for a passing
# run"). That leaves an agent unable to tell "ran clean" from "didn't run"
# by output alone, so it ends up re-running the linter defensively to
# confirm. --output-formatter json/sarif/junit already print an unambiguous
# payload on a clean run (JSON prints "[]") and are untouched here — the
# success line only fires when stdout came back genuinely empty on exit 0.
#
# Usage: identical to node_modules/.bin/markdownlint-obsidian — same flags,
# a single path, many paths, or none (vault-wide sweep). Exit code and
# finding output are never altered; this only adds output on the clean path.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
BIN="$REPO_ROOT/node_modules/.bin/markdownlint-obsidian"

if [ ! -x "$BIN" ]; then
  echo "markdownlint-obsidian-wrapper: $BIN not found or not executable (broken/missing install)" >&2
  exit 127
fi

out="$("$BIN" "$@")"
code=$?

if [ -n "$out" ]; then
  printf '%s\n' "$out"
fi

if [ "$code" -eq 0 ] && [ -z "$out" ]; then
  if [ "$#" -gt 0 ]; then
    echo "✔ 0 findings: $*"
  else
    echo "✔ 0 findings (vault-wide scope)"
  fi
fi

exit "$code"
