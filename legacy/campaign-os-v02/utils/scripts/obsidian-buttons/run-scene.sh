#!/usr/bin/env bash
# Obsidian button target: run a scene — log a scene marker into the live
# recording's timeline.
#
# Called by the Shell Commands plugin from a scene note's ▶ Run Scene button:
#   run-scene.sh <session_number> <scene_number> <scene_file_abs_path>
# ({{yaml_value:session_number}} {{yaml_value:scene_number}} {{file_path:absolute}})
#
# The marker is one NDJSON line appended to the session's audio/markers.jsonl
# (single-line `>>` appends are O_APPEND-atomic); its t_offset_s is seconds
# since the recorder's started_at_epoch (see start-recording.sh's env file),
# i.e. the audio-timeline position. transcribe-session tags every utterance
# with its scene from these markers. Everything before the first marker is the
# pre-session segment by construction.
#
# No active recording → the marker is skipped, so scenes can be run in
# un-recorded prep/rehearsal without errors.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/dm-console.sh
source "$HERE/lib/dm-console.sh"
PID_FILE="${TMPDIR:-/tmp}/campaign-os-recording.pid"
ENV_FILE="${TMPDIR:-/tmp}/campaign-os-recording.env"
LOG_FILE="${TMPDIR:-/tmp}/campaign-os-scene.log"
exec > >(tee -a "$LOG_FILE") 2> >(tee -a "$LOG_FILE" >&2)
dm_console_watch scene "▶ Scene" "$LOG_FILE"

session="${1:-}"
scene_number="${2:-}"
scene_file="${3:-}"

# Frontmatter values arrive as raw text — only a plain number is usable.
[[ "$scene_number" =~ ^[0-9]+$ ]] || scene_number=0

marker_note="marker skipped"
recording_live=false
if [[ -f "$ENV_FILE" && -f "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
  recording_live=true
fi

if $recording_live; then
  # shellcheck source=/dev/null
  source "$ENV_FILE"
  if [[ -n "${START_EPOCH:-}" && -n "${SESSION_DIR:-}" && -d "$SESSION_DIR/audio" ]]; then
    now="$(date +%s)"
    offset=$((now - START_EPOCH))
    scene_slug="$(basename "${scene_file:-scene}" .md)"
    # Scene label: the note's H1 when present, else the slug.
    label=""
    if [[ -f "$scene_file" ]]; then
      label="$(grep -m1 '^# ' "$scene_file" | sed 's/^# //' || true)"
    fi
    [[ -n "$label" ]] || label="$scene_slug"
    # jq builds the line so slug/label are safely JSON-escaped.
    line="$(jq -nc \
      --arg slug "$scene_slug" \
      --arg label "$label" \
      --argjson num "${scene_number:-0}" \
      --argjson t "$offset" \
      --argjson epoch "$now" \
      --arg wall "$(date +%Y-%m-%dT%H:%M:%S)" \
      '{scene_slug:$slug, scene_number:$num, label:$label,
        t_offset_s:$t, epoch:$epoch, wall:$wall}')"
    printf '%s\n' "$line" >>"$SESSION_DIR/audio/markers.jsonl"
    marker_note="scene ${scene_number:-?} marked @ +${offset}s"
  else
    marker_note="marker skipped (no recording state)"
  fi
else
  echo "⚠ No active recording — marker skipped." >&2
fi

echo "▶ Scene: $marker_note"
