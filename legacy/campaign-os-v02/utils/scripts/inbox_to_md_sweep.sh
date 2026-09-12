#!/usr/bin/env bash
# SessionStart hook (startup|resume|clear|compact) — creates a markdown
# companion for every inbox/ file that doesn't already have one, so a fresh
# session never has to remember to run inbox:to-md by hand before ingesting.
# Fails open: no node binary, any error — swallowed, never blocks session
# start. Silent when there's nothing to convert.
set -uo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/env_local.sh"
REPO_ROOT="$CAMPAIGN_ROOT"
cd "$REPO_ROOT" 2>/dev/null || exit 0

command -v node >/dev/null 2>&1 || exit 0

node utils/scripts/inbox/sweep-to-markdown.mjs

exit 0
