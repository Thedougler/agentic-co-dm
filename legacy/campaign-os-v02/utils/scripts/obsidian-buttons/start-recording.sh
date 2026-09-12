#!/usr/bin/env bash
# Obsidian button target: start session audio recording in the background.
# Called by the Shell Commands plugin with the active run guide's
# `session_number:` frontmatter value. Detaches record.sh (which execs
# shattered-audio) and remembers its PID for stop-recording.sh.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../../.." && pwd)"
# shellcheck source=lib/dm-console.sh
source "$HERE/lib/dm-console.sh"
RECORD="$REPO/.claude/skills/record-session-audio/scripts/record.sh"
PID_FILE="${TMPDIR:-/tmp}/campaign-os-recording.pid"
LOG_FILE="${TMPDIR:-/tmp}/campaign-os-recording.log"
ENV_FILE="${TMPDIR:-/tmp}/campaign-os-recording.env"

# A dead start mid-prep is easy to miss in an Obsidian notice — raise a modal
# alert too so the session never silently goes unrecorded.
alert() {
  osascript -e "display alert \"Recording failed to start\" message \"$1\" as critical" \
    >/dev/null 2>&1 || true
}

session="${1:-}"
if [[ ! "$session" =~ ^[0-9]+$ ]]; then
  echo "session_number missing or not a number: '$session'" >&2
  exit 1
fi

if [[ -f "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
  echo "Recording already running (PID $(cat "$PID_FILE")) — use the Stop Recording button first." >&2
  exit 1
fi

# Surface the setup error here instead of letting it die silently in the log.
if [[ ! -x "$REPO/utils/tools/audio/.venv/bin/shattered-audio" ]]; then
  echo "shattered-audio not installed — run: cd $REPO/utils/tools/audio && python3 -m venv .venv && .venv/bin/pip install -e '.[all]'" >&2
  exit 1
fi

cd "$REPO"
# --strict: a session must never silently record on a partial rig — a missing
# aggregate device or unplugged mic aborts loudly instead of degrading.
nohup "$RECORD" --session "$session" --strict >"$LOG_FILE" 2>&1 &
pid=$!
echo "$pid" >"$PID_FILE"
dm_console_watch recording "⏺ Recording" "$LOG_FILE"

# Give ffmpeg a moment to fail fast (no mics, permission denied, strict
# device check) so the button reports a dead start instead of a false success.
sleep 3
if ! kill -0 "$pid" 2>/dev/null; then
  rm -f "$PID_FILE"
  tail_msg="$(tail -3 "$LOG_FILE" | tr '\n' ' ' | tr '"' "'")"
  alert "$tail_msg"
  echo "Recording died on startup — $tail_msg" >&2
  exit 1
fi

out_dir="$(grep -m1 '^  Output: ' "$LOG_FILE" | sed 's/^  Output: //' | sed 's|/$||')"

# State file for the Run-Scene button: scene markers are timestamped relative
# to the recorder's started_at_epoch (manifest.json), the audio-timeline zero.
start_epoch=""
if [[ -n "$out_dir" ]]; then
  manifest="$REPO/$out_dir/audio/manifest.json"
  for _ in $(seq 1 10); do
    if [[ -f "$manifest" ]]; then
      start_epoch="$(jq -r '.started_at_epoch // empty' "$manifest" 2>/dev/null || true)"
      [[ -n "$start_epoch" ]] && break
    fi
    sleep 0.5
  done
fi
if [[ -n "$start_epoch" ]]; then
  {
    echo "SESSION=$session"
    echo "SESSION_DIR=$REPO/$out_dir"
    echo "START_EPOCH=${start_epoch%.*}"
  } >"$ENV_FILE"
else
  echo "⚠ Could not read started_at_epoch from manifest — Run-Scene markers disabled for this session." >&2
fi

echo "⏺ Recording session $session (PID $pid) → ${out_dir:-sessions/}"
