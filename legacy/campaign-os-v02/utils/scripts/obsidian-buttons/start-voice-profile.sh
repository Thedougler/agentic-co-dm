#!/usr/bin/env bash
# Obsidian button target: start capturing a voice-profile sample from the
# default mic for the active character page. Recording begins immediately;
# stop-voice-profile.sh finalizes the wav, save-voice-profile.sh enrolls it.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/dm-console.sh
source "$HERE/lib/dm-console.sh"

WAV_FILE="${TMPDIR:-/tmp}/campaign-os-voice-profile.wav"
PID_FILE="${TMPDIR:-/tmp}/campaign-os-voice-profile.pid"
ENV_FILE="${TMPDIR:-/tmp}/campaign-os-voice-profile.env"
LOG_FILE="${TMPDIR:-/tmp}/campaign-os-voice-profile.log"
SESSION_PID_FILE="${TMPDIR:-/tmp}/campaign-os-recording.pid"

alert() {
  osascript -e "display alert \"Voice capture failed to start\" message \"$1\" as critical" \
    >/dev/null 2>&1 || true
}

note_path="${1:-}"
if [[ -z "$note_path" || ! -f "$note_path" ]]; then
  echo "Active note path missing or not a file: '$note_path'" >&2
  exit 1
fi

# Character = the page's H1 title; slug basename as fallback.
character="$(grep -m1 '^# ' "$note_path" | sed 's/^# //' || true)"
[[ -n "$character" ]] || character="$(basename "$note_path" .md)"

if [[ -f "$SESSION_PID_FILE" ]] && kill -0 "$(cat "$SESSION_PID_FILE")" 2>/dev/null; then
  echo "A session recording is running — voice-profile capture would fight it for the mic. Stop the session first." >&2
  exit 1
fi
if [[ -f "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
  echo "A voice-profile capture is already running — use the Stop button first." >&2
  exit 1
fi

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "ffmpeg not found on PATH — install it (brew install ffmpeg)." >&2
  exit 1
fi

# Default mic, mono, 16 kHz — shattered-audio's enrollment format.
rm -f "$WAV_FILE"
nohup ffmpeg -hide_banner -nostdin -f avfoundation -i ":default" \
  -ac 1 -ar 16000 -y "$WAV_FILE" >"$LOG_FILE" 2>&1 &
pid=$!
echo "$pid" >"$PID_FILE"
{
  echo "CHARACTER=$character"
  echo "NOTE_PATH=$note_path"
} >"$ENV_FILE"
dm_console_watch voice "⏺ Voice Profile" "$LOG_FILE"

# Let ffmpeg fail fast (no mic, permission denied) so the button reports a
# dead start instead of a false success.
sleep 2
if ! kill -0 "$pid" 2>/dev/null; then
  rm -f "$PID_FILE" "$ENV_FILE"
  tail_msg="$(tail -3 "$LOG_FILE" | tr '\n' ' ' | tr '"' "'")"
  alert "$tail_msg"
  echo "Voice capture died on startup — $tail_msg" >&2
  exit 1
fi

echo "⏺ Recording voice profile for $character — read the voice script, then hit Stop."
