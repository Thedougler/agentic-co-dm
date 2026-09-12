---
name: record-session-audio
description: >-
  Use at the START of a live session in a Campaign OS repo (vault/ present) to capture table
  audio. Triggers: "/record-session-audio", "record the session", "start recording", "start
  the session audio", "we're starting", "capture tonight's session", "begin recording the
  game". A fire-and-wait recorder that runs until told to stop.
---

# Record Session Audio

This is a keep-standalone CAPTURE-phase feeder, not unreplaced by any
pipeline script. It does not itself paste a `CAPTURE:` marker — that marker
belongs to the file-appearance trigger described in `vault/refs/runbook-capture.md`,
which fires once the label pass actually runs, not at recording start.

Start a multi-mic recording of a live D&D session. The preferred mode is one
ffmpeg process on the CoreAudio Aggregate Device (the `aggregate:` block in
`utils/tools/audio/config.yaml`) — all mics share one clock, so the tracks are
inherently sample-aligned; the recorder falls back to one ffmpeg process per
microphone when the aggregate device or config is absent (unless `--strict`,
which aborts instead — the run-guide button path). Either way the bundled
`shattered-audio` tool (not this skill's own script) writes an isolated,
chunked lossless FLAC track per mic under
`vault/episodes/NN-slug/audio/raw/{dm-mic,player-mic}/` — physically separating
the DM and
each player. Capture is 48 kHz FLAC with an 80 Hz highpass only: lossless
beats AAC for ASR/diarization accuracy, and denoise
(incl. Apple Voice Isolation) is deliberately absent at every stage — it
measurably hurts Whisper and speaker embeddings; raw is what gets transcribed.
The `aggregate.mics` config list scales 1..N (single table mic → per-player
mics); device checks, channel splits, and speaker priors all follow it.
`shattered-audio` resolves the session number to the existing
`vault/episodes/NN-slug/` dir automatically (falling back to `vault/episodes/session-NN/`
only if that session has no slugged dir yet).

The recorder is built to run untouched for 4+ hours and to stop cleanly on
command. **Your job is to start it, confirm it's healthy, then get out of the
way and wait.**

## The Protocol

1. **Get the session number.** Ask the DM if it isn't obvious. Check existing
   `vault/episodes/NN-slug/` dirs to pick the next number.
2. **Start the recorder in the background.** Run with the Bash tool's
   `run_in_background: true`:
   ```
   .claude/skills/record-session-audio/scripts/record.sh --session NN
   ```
3. **Confirm it's healthy** — read the background output ONCE. You should see
   "Recording session NN", `Mode: aggregate` (the preferred one-clock capture;
   a silent fallback to per-mic ffmpeg processes means the Aggregate Device is
   missing — surface that), and a line per mic (`mic00 [ch2] <name>`). If a
   mic the DM expects is missing, surface it now. If instead you see
   `shattered-audio not installed. Set it up with: ...`, stop and paste that
   setup command to the DM — do not attempt to install it yourself or improvise
   a substitute recording command (see Red Flags).
4. **Announce and wait.** Tell the DM recording has started, list the mics, and
   say you'll stop when they say so. Then **end your turn.** Do not poll, do not
   narrate, do not check on it. The session is being played.
5. **Stop only when told.** When the DM says "stop recording" / "end the
   session" / "we're done", kill the background shell. ffmpeg finalizes the
   current chunk on SIGTERM. Then report where the audio landed
   (`vault/episodes/NN-slug/audio/raw/`) and name the next step:
   `shattered-audio transcribe-session --session NN --audio-dir sessions`
   (transcribes the raw tracks directly; cross-mic ghost lines are deduped
   at merge — `utils/tools/audio/README.md` § Cross-mic ghost dedup). For a
   human-listenable copy of the whole session, `export-session --session NN
   --audio-dir sessions` writes one stereo m4a (dm-mic left, player-mic
   right) next to the manifest.

## Red Flags — STOP

| Thought | Reality |
|---|---|
| "I'll run it in the foreground" | That blocks your turn for 4 hours. **Always** `run_in_background: true`. |
| "Let me check the recording every few minutes" | Polling burns context and proves nothing. Confirm once at start, then wait. |
| "It's been a while, I'll wrap up the recording" | NEVER stop on your own. Only the DM ends the session. |
| "The test capture worked, so I'm done" | A short test is not the session. Start the real run and leave it. |
| "I'll write my own ffmpeg/sox command" | Use the bundled script. It handles per-mic isolation, chunking, and clean shutdown. |

## Quick Reference

| Flag | Purpose |
|---|---|
| `--session NN` | **Required.** Session number → resolved to `vault/episodes/NN-slug/` (or `vault/episodes/session-NN/` if no slugged dir exists yet). |
| `--segment-minutes N` | Chunk length (default 15). Smaller = more frequent flushes. |
| `--mics 0,1` | Restrict to specific avfoundation indices (default: all available). Forces per-mic capture. |
| `--no-aggregate` | Force per-mic capture even when the Aggregate Device is present. |
| `--strict` | Hard-fail (exit 2) when the aggregate device or any configured mic is absent — no degraded-rig fallback. The run-guide button always passes this. |
| `--audio-dir PATH` | Override output root (default `sessions`). |

List mics first if unsure: `utils/tools/audio/.venv/bin/shattered-audio devices`
(or `ffmpeg -f avfoundation -list_devices true -i ""`).

## How It Works

- **Aggregate mode (preferred, default):** one ffmpeg on the CoreAudio
  Aggregate Device pans each mic's channel (`aggregate:` block in
  `utils/tools/audio/config.yaml`) into its own mono 48 kHz FLAC part series
  (80 Hz highpass, no other processing) —
  `vault/episodes/NN-slug/audio/raw/dm-mic/part-000.flac` and `player-mic/...`.
  One shared clock means no inter-device drift and no calibration;
  `manifest.json` records `capture: aggregate` and each mic's `channel`.
- **Per-mic fallback:** one ffmpeg per microphone, same output layout
  (`capture: per-mic`); a mic listed in `stereo_mics:` is captured
  2-channel, and each manifest mic entry records its `channels`.
- **Strict mode (`--strict`, the button path):** the aggregate device and
  every configured mic must be visible as devices at start, else exit 2
  naming what's missing — never a silent degraded rig.
- **Disconnect watchdog:** after a 30 s startup grace (a waking USB mic
  can briefly re-enumerate), the recorder polls the device list every 5 s;
  a configured mic gone for 3 consecutive polls ends the session cleanly
  (chunks + markers finalized), posts a macOS notification, and records
  `reason: device-disconnect` in the markers file.
- **Scene markers:** `audio/markers.jsonl` (appended by the Run Scene
  button, plus `recording-started`/`recording-ended` sentinels) is folded
  into `audio/markers.json` on stop; `transcribe-session` tags each
  utterance with its scene — see `utils/tools/audio/README.md` § Scene markers.
- `manifest.json` at `vault/episodes/NN-slug/audio/manifest.json` records the
  mic→speaker mapping (set mic priors via `channel_priors` in
  `utils/tools/audio/config.yaml` so the DM's mic is labeled "DM") plus
  `started_at_epoch` — the audio-timeline zero the scene markers are
  measured from.
- Chirp calibration is a **manual fallback for per-mic capture only**
  (aggregate mode auto-skips it): `record --calibrate` adds a
  `chirp_calibration` field — a chirp-measured inter-device clock offset,
  observational only. Sweep bands are per-leg configurable via
  `chirp_bands:` in `utils/tools/audio/config.yaml`
  (`utils/tools/audio/scripts/chirp_band_probe.py` measures which bands a given
  speaker/mic pair actually couples on before changing them).
- Chunks are flushed as they finish, so a crash at hour 3 still leaves hours 0–3.
- If `vault/episodes/NN-slug/` doesn't exist yet when recording starts (the slug
  hasn't been created), audio lands in `vault/episodes/session-NN/` instead — move
  it into the slugged session dir once that dir exists.

## Troubleshooting

- **No devices / empty mic list** → the terminal lacks microphone permission
  (System Settings → Privacy → Microphone) or ffmpeg isn't installed.
- **A mic vanished mid-session** → the watchdog stops the recording cleanly
  and posts a macOS notification; chunks up to the unplug are finalized.
  Plug the mic back in and start again — the recorder appends new part
  numbers to the same session.
- **`Mode: aggregate` missing / strict abort at start** → the Aggregate
  Device isn't present (rebuild it in Audio MIDI Setup: all mics as
  sub-devices, Drift Correction on) or the `aggregate:` block is gone from
  `utils/tools/audio/config.yaml`. With `--strict` (the button path) this aborts
  loudly; without it recording degrades to per-mic capture and loses the
  shared clock — surface it to the DM before a long session.
- **Setup error** → the script prints the one-line `pip install -e '.[all]'`
  command to provision `utils/tools/audio/.venv`. This is expected in a fresh
  campaign-os checkout — `utils/tools/audio/` does not ship with this repo; it is
  a separate install the DM provisions locally (same shape as any other
  local toolchain prerequisite, e.g. ffmpeg itself).

## Degrade by asking

`CONFIG.md` sets `feature_record_session_audio: false` → this subsystem is
turned off on this installation: stop, point the DM at `CONFIG.md`, do not
start a recording.

Missing session number, missing mic permissions, `shattered-audio` not
installed, or a session with no slugged dir yet (see How It Works) — in
every case, surface the exact error/state and ask the DM what they want,
rather than guessing a session number, inventing a workaround command, or
silently reorganizing files to make the pipeline "look" connected.
