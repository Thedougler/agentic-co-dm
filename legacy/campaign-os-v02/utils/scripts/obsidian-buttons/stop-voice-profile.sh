#!/usr/bin/env bash
# Obsidian button target: stop the voice-profile capture started by
# start-voice-profile.sh. SIGINT lets ffmpeg finalize the wav header; the
# wav + env stay in place for save-voice-profile.sh to confirm.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/dm-console.sh
source "$HERE/lib/dm-console.sh"

WAV_FILE="${TMPDIR:-/tmp}/campaign-os-voice-profile.wav"
PID_FILE="${TMPDIR:-/tmp}/campaign-os-voice-profile.pid"
ENV_FILE="${TMPDIR:-/tmp}/campaign-os-voice-profile.env"
LOG_FILE="${TMPDIR:-/tmp}/campaign-os-voice-profile.log"
exec > >(tee -a "$LOG_FILE") 2> >(tee -a "$LOG_FILE" >&2)
dm_console_watch voice "⏺ Voice Profile" "$LOG_FILE"

if [[ ! -f "$PID_FILE" ]]; then
  echo "No voice-profile capture in progress (no PID file)." >&2
  exit 1
fi

pid="$(cat "$PID_FILE")"
if ! kill -0 "$pid" 2>/dev/null; then
  rm -f "$PID_FILE"
  echo "Capture already stopped (stale PID $pid cleaned up)." >&2
  exit 1
fi

kill -INT "$pid"
for _ in $(seq 1 10); do
  kill -0 "$pid" 2>/dev/null || break
  sleep 1
done
if kill -0 "$pid" 2>/dev/null; then
  echo "ffmpeg (PID $pid) still shutting down — try Stop again in a moment; not force-killing." >&2
  exit 1
fi
rm -f "$PID_FILE"

if [[ ! -s "$WAV_FILE" ]]; then
  rm -f "$ENV_FILE"
  echo "Capture produced no audio — check mic permissions and try again." >&2
  exit 1
fi

character="unknown"
[[ -f "$ENV_FILE" ]] && character="$(sed -n 's/^CHARACTER=//p' "$ENV_FILE")"
duration=""
if command -v ffprobe >/dev/null 2>&1; then
  duration="$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$WAV_FILE" 2>/dev/null | cut -d. -f1 || true)"
fi
echo "⏹ Stopped — ${duration:-?}s captured for $character. Hit Save Voice Profile to enroll, or Record again to redo."
