#!/usr/bin/env bash
# PreToolUse hook (Edit|Write|MultiEdit) — REFACTOR-PLAN.md P1.1.
#
# MIGRATION-LOG (2026-07-29): five uncoached Haiku subagents scored 0/3
# routing compliance after three prose-rewording rounds; conclusion was that
# prose-only routing (CLAUDE.md's TRIGGER table) had hit a ceiling and needs
# a mechanical enforcement layer. This is that layer, for the two rows of
# CLAUDE.md's table that are mechanically path-determinable (WIKI.md,
# CODE.md — see the case statement below). The other rows
# (IDEA.md, PLAN.md, DEBUG.md, VERIFY.md, EFFICIENCY.md) trigger on session
# state or event shape, not target path alone, and stay prose-only.
#
# Mechanism: guardrailsDoc(rel) says which doc a target path requires: if
# the transcript has no prior Read of that doc this session, deny the edit
# with a self-prompting message ("Read <doc> first — then retry"); if it
# does, allow silently. A doc read anywhere earlier in the session satisfies
# this check for the rest of the session — this hook does not try to detect
# a compaction boundary and re-require the read after one (the transcript
# JSONL keeps pre-compaction entries; CLAUDE.md's own "since the last
# compaction" nuance is a stricter bar than this hook enforces). Ponytail:
# this is a known relaxation, not a bug — upgrade path is detecting a
# compaction marker in the transcript if false negatives (edits allowed on
# a stale pre-compaction read) prove to matter in practice.
#
# Bypass: the plan asked for an env-var bypass. Confirmed against official
# Claude Code hook docs that a PreToolUse hook has no path to receive a
# mid-session `export` — CLAUDE_ENV_FILE (the one documented mechanism for
# persisting env vars into a session) is only available to SessionStart/
# Setup/CwdChanged/FileChanged hooks, explicitly not PreToolUse. Using a
# file-flag bypass instead: touch .claude/.routing-guard-bypass to disable
# this hook for the rest of the session (rm it to re-enable).
#
# Fails open (allows the edit) on any hook-internal problem — a broken
# transcript read, jq failure, or missing node — so a malfunctioning hook
# never blocks real work; it only ever denies on a confirmed missing Read.
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/env_local.sh"
REPO_ROOT="$CAMPAIGN_ROOT"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

[ -f "$REPO_ROOT/.claude/.routing-guard-bypass" ] && exit 0

payload="$(cat)"
file="$(printf '%s' "$payload" | jq -r '.tool_input.file_path // empty' 2>/dev/null)" || exit 0
[ -z "$file" ] && exit 0
transcript="$(printf '%s' "$payload" | jq -r '.transcript_path // empty' 2>/dev/null)" || exit 0
[ -z "$transcript" ] && exit 0
[ -r "$transcript" ] || exit 0

rel="${file#"$REPO_ROOT"/}"
[ "$rel" = "$file" ] && exit 0   # target outside the repo — not this hook's concern

# Subagent edits: `transcript_path` and `session_id` both carry the PARENT
# session's values, not the subagent's (measured 2026-08-01, REFACTOR-PLAN.md
# P6.1 — a probe recorded agent_id=<id>, agent_type=general-purpose, and the
# parent's transcript path in the same payload). Checking the parent's
# transcript is worse than useless here: the orchestrator has almost always
# read WIKI.md already, so every subagent it dispatches inherits that read and
# sails through — and an uncoached subagent is precisely the population this
# hook exists to gate (MIGRATION-LOG 2026-07-29 measured five of them at 0/3).
#
# The subagent's own transcript is derivable from the payload: the harness
# writes it to <tmp>/claude-<uid>/<project-slug>/<session-id>/tasks/
# <agent-id>.output, where project-slug is the parent transcript's own parent
# directory name. Derived, not hardcoded, and verified readable before use.
agent_id="$(printf '%s' "$payload" | jq -r '.agent_id // empty' 2>/dev/null)" || agent_id=""
if [ -n "$agent_id" ]; then
  slug="$(basename "$(dirname "$transcript")")"
  session="$(basename "$transcript" .jsonl)"
  sub_transcript="${TMPDIR:-/tmp}/claude-$(id -u)/$slug/$session/tasks/$agent_id.output"
  [ -r "$sub_transcript" ] || sub_transcript="/private/tmp/claude-$(id -u)/$slug/$session/tasks/$agent_id.output"
  # Fails open when the path can't be resolved — same philosophy as the rest
  # of this hook. Denying on an unresolvable path would block every subagent
  # edit the moment the harness renames a directory, which is a far worse
  # failure than the one it would prevent.
  [ -r "$sub_transcript" ] || exit 0
  transcript="$sub_transcript"
fi

case "$rel" in
  vault/*|_templates/*) doc="docs/guardrails/WIKI.md" ;;
  *.mjs|*.js|*.ts|*.tsx|*.py|*.sh|*.json|*.jsonc|*.yml|*.yaml|*.css|*.scss|*.toml) doc="docs/guardrails/CODE.md" ;;
  *) exit 0 ;;
esac

doc_abs="$REPO_ROOT/$doc"

# Every prior Read tool_use's input.file_path, across the whole transcript
# (pre- and post-compaction alike — see header note). Absolute paths only;
# the Read tool always receives an absolute path, so a plain substring
# match against doc_abs is exact, no normalization needed.
already_read="$(jq -r '
  select(.type == "assistant")
  | .message.content[]?
  | select(.type == "tool_use" and .name == "Read")
  | .input.file_path // empty
' "$transcript" 2>/dev/null | grep -qxF "$doc_abs" && echo yes || echo no)" || already_read=no

[ "$already_read" = "yes" ] && exit 0

reason="Read $doc first — then retry. This edit targets a path CLAUDE.md's routing table gates on that doc, and no Read of it appears yet in this session's transcript. (Bypass for emergencies: touch .claude/.routing-guard-bypass)"
jq -n --arg reason "$reason" '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"deny",permissionDecisionReason:$reason}}'
exit 0
