#!/usr/bin/env bash
# Obsidian button target: enroll the stopped voice-profile capture as this
# page's character persona under its voice_actor. Auto-enrolls the actor
# profile from the same recording when it doesn't exist yet. Re-saving later
# with a fresh recording UPDATES the persona (embeddings blend).
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../../.." && pwd)"
# shellcheck source=lib/dm-console.sh
source "$HERE/lib/dm-console.sh"
AUDIO_BIN="$REPO/utils/tools/audio/.venv/bin/shattered-audio"
AUDIO_CFG="$REPO/utils/tools/audio/config.yaml"
WAV_FILE="${TMPDIR:-/tmp}/campaign-os-voice-profile.wav"
PID_FILE="${TMPDIR:-/tmp}/campaign-os-voice-profile.pid"
ENV_FILE="${TMPDIR:-/tmp}/campaign-os-voice-profile.env"
LOG_FILE="${TMPDIR:-/tmp}/campaign-os-voice-profile.log"
exec > >(tee -a "$LOG_FILE") 2> >(tee -a "$LOG_FILE" >&2)
dm_console_watch voice "⏺ Voice Profile" "$LOG_FILE"

note_path="${1:-}"
actor_raw="${2:-}"

if [[ -z "$actor_raw" ]]; then
  echo "voice_actor: frontmatter is empty on this page — set it to the first name of the person voicing this character (pc ⇒ the player, npc ⇒ usually nick)." >&2
  exit 1
fi
if [[ ! -f "$WAV_FILE" ]]; then
  echo "No captured recording to save — hit Record Voice Profile first." >&2
  exit 1
fi
if [[ -f "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
  echo "Capture still running — hit Stop before saving." >&2
  exit 1
fi
if [[ ! -x "$AUDIO_BIN" ]]; then
  echo "shattered-audio not installed — run: cd $REPO/utils/tools/audio && python3 -m venv .venv && .venv/bin/pip install -e '.[all]'" >&2
  exit 1
fi

# Guard: the recording was started from THIS page, not another character's.
character="$(grep -m1 '^# ' "$note_path" | sed 's/^# //' || true)"
[[ -n "$character" ]] || character="$(basename "$note_path" .md)"
recorded_for=""
[[ -f "$ENV_FILE" ]] && recorded_for="$(sed -n 's/^CHARACTER=//p' "$ENV_FILE")"
if [[ -n "$recorded_for" && "$recorded_for" != "$character" ]]; then
  echo "This recording was made for '$recorded_for', not '$character' — save it from that page, or Record again here." >&2
  exit 1
fi

# Too short a sample gives a junk embedding — refuse loudly.
if command -v ffprobe >/dev/null 2>&1; then
  duration="$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$WAV_FILE" 2>/dev/null | cut -d. -f1 || true)"
  if [[ -n "$duration" && "$duration" -lt 3 ]]; then
    echo "Recording is only ${duration}s — too short for a usable profile. Record at least a few sentences of the voice script." >&2
    exit 1
  fi
fi

# Title-case the actor to match config.yaml's speaker_map keys (Nick, Chad, …).
actor="$(python3 -c "import sys; s=sys.argv[1].strip(); print(s[:1].upper()+s[1:])" "$actor_raw")"

enroll_persona() {
  "$AUDIO_BIN" enroll "$character" --actor "$actor" --config "$AUDIO_CFG" "$WAV_FILE" 2>&1
}

if ! out="$(enroll_persona)"; then
  if grep -qi "not found" <<<"$out"; then
    # Actor has no profile yet — bootstrap it from the same recording.
    dm_flag=()
    [[ "$(tr '[:upper:]' '[:lower:]' <<<"$actor")" == "nick" ]] && dm_flag=(--dm)
    if ! actor_out="$("$AUDIO_BIN" enroll "$actor" "${dm_flag[@]}" --config "$AUDIO_CFG" "$WAV_FILE" 2>&1)"; then
      echo "Actor enrollment for '$actor' failed: $actor_out" >&2
      exit 1
    fi
    if ! out="$(enroll_persona)"; then
      echo "Persona enrollment failed after actor bootstrap: $out" >&2
      exit 1
    fi
    out="Enrolled actor '$actor' (new) + $out"
  else
    echo "Enrollment failed: $out" >&2
    exit 1
  fi
fi

rm -f "$WAV_FILE" "$PID_FILE" "$ENV_FILE"
echo "✔ Saved voice profile: $character (voiced by $actor). $out"
