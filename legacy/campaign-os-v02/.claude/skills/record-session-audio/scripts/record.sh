#!/usr/bin/env bash
# Fire-and-wait multi-mic session recorder.
#
# Thin wrapper over `shattered-audio record` — records every available mic to
# its own isolated, chunked m4a track under sessions/NN-slug/audio/raw/. Built to
# run for 4+ hours and stop cleanly on SIGTERM/SIGINT (finalizing the current
# chunk), so the controlling agent can end the session on command.
#
# Run it with the Bash tool's run_in_background:true, then STOP and wait. Do not
# poll it. To end recording, kill the background shell — ffmpeg shuts down
# gracefully.
#
# The underlying shattered-audio tool writes
# NN-slug/audio/raw/{dm-mic,player-mic}/part-NNN.m4a
# (per-mic, nested) — it resolves the session number to an existing
# sessions/NN-slug/ dir automatically (falling back to sessions/session-NN/
# only if no slugged dir exists yet), so recordings land alongside the rest
# of that session's files without a manual rename.
#
# Usage: record.sh --session 7 [--segment-minutes 15] [--mics 0,1]
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../../../.." && pwd)"   # scripts → skill → skills → .claude → repo root
SA="$REPO/utils/tools/audio/.venv/bin/shattered-audio"

if [[ ! -x "$SA" ]]; then
  echo "shattered-audio not installed. Set it up with:" >&2
  echo "  cd $REPO/utils/tools/audio && python3 -m venv .venv && .venv/bin/pip install -e '.[all]'" >&2
  exit 1
fi

cd "$REPO"
# Default --audio-dir to the real campaign tree (sessions/), not the
# upstream tool's own default (.raw/sessions) — .raw/ has no home in this
# repo's directory contract and, unlike sessions/*/audio/,
# is NOT covered by .gitignore, so recordings left there risk an accidental
# multi-GB commit. --config is pinned to the rig config: Config.load's
# cwd-relative "config.yaml" lookup misses it from the repo root, which
# silently drops aggregate mode and records every device per-mic (including
# the Aggregate Device itself as a phantom mic). A caller-supplied
# --audio-dir/--config later in "$@" still wins (click/typer keep the last
# occurrence of a repeated option).
exec "$SA" record --audio-dir sessions --config "$REPO/utils/tools/audio/config.yaml" "$@"
