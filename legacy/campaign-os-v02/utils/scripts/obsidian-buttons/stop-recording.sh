#!/usr/bin/env bash
# Obsidian button target: stop the background session recording started by
# start-recording.sh. SIGTERM lets shattered-audio finalize the current
# audio chunk (record.sh's documented contract).
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/dm-console.sh
source "$HERE/lib/dm-console.sh"

PID_FILE="${TMPDIR:-/tmp}/campaign-os-recording.pid"
ENV_FILE="${TMPDIR:-/tmp}/campaign-os-recording.env"
LOG_FILE="${TMPDIR:-/tmp}/campaign-os-recording.log"
# Tee both streams into the log the DM Console tails, keeping stdout/stderr
# on their own fds so the Shell Commands plugin's separate notification
# handlers still see them independently.
exec > >(tee -a "$LOG_FILE") 2> >(tee -a "$LOG_FILE" >&2)
dm_console_watch recording "⏺ Recording" "$LOG_FILE"

if [[ ! -f "$PID_FILE" ]]; then
  echo "No recording in progress (no PID file)." >&2
  exit 1
fi

pid="$(cat "$PID_FILE")"
if ! kill -0 "$pid" 2>/dev/null; then
  rm -f "$PID_FILE"
  echo "Recording already stopped (stale PID $pid cleaned up)." >&2
  exit 1
fi

kill -TERM "$pid"
# Wait for the chunk to finalize before declaring success.
for _ in $(seq 1 20); do
  kill -0 "$pid" 2>/dev/null || break
  sleep 1
done
if kill -0 "$pid" 2>/dev/null; then
  echo "Recorder (PID $pid) still shutting down — chunk finalization can take a moment; not force-killing." >&2
  exit 1
fi

rm -f "$PID_FILE" "$ENV_FILE"
echo "⏹ Session ended — audio + scene markers finalized under the session's sessions/NN-slug/audio/ dir."
