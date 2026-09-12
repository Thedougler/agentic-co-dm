#!/usr/bin/env bash
# PostToolUse hook (Read) — appends a JSONL record to the rolling agent-reads
# log whenever a Read resolves to a vault/ path. Never blocks the turn.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/lib/env_local.sh"
REPO_ROOT="$CAMPAIGN_ROOT"
cd "$REPO_ROOT" || exit 0

payload="$(cat)"
file="$(printf '%s' "$payload" | jq -r '.tool_input.file_path // empty' 2>/dev/null)" || exit 0
[ -z "$file" ] && exit 0
[ -f "$file" ] || exit 0
rel="${file#"$REPO_ROOT"/}"

case "$rel" in
  vault/*.md) ;;
  *) exit 0 ;;
esac

LOG_DIR="$REPO_ROOT/.wiki-cli"
LOG_FILE="$LOG_DIR/agent-reads.jsonl"
mkdir -p "$LOG_DIR"

session_id="${CLAUDE_SESSION_ID:-unknown}"
ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

printf '%s\n' "$(jq -nc \
  --arg page "$rel" \
  --arg session_id "$session_id" \
  --arg tool_type "Read" \
  --arg timestamp "$ts" \
  '{page:$page, session_id:$session_id, tool_type:$tool_type, query_position:null, timestamp:$timestamp}')" \
  >> "$LOG_FILE"

exit 0
