# shattered-audio

The table-audio toolchain: record a session, transcribe it, and hand the
pipeline a per-part CSV. Driven by `record-session-audio` (capture) and
`vault/refs/runbook-capture.md` (Phase 3). Config: `config.yaml` in this
directory; secrets in repo-root `.env.local`.

## Audio layouts

Audio arrives in either of two layouts under `vault/episodes/NNN/audio/`:

1. **Flat** — `partX.m4a`, sequential parts of one recording (a phone
   recorder, an internal laptop mic, any manually-dropped single feed).
2. **Multi-track** — `raw/dm-mic/part-NNN.flac` and
   `raw/player-mic/part-NNN.flac` (`.m4a` in legacy sessions; both are
   discovered), one subdirectory per physically isolated input, named by
   table role (a third+ mic falls back to `mic-02`, `mic-03`, …). Sibling
   `manifest.json` carries mic metadata including `started_at_epoch`, the
   audio-timeline zero; `markers.json` carries scene markers.

Multi-track wins outright when `audio/raw/` holds any mic directory with
audio in it — stray flat files directly in `audio/` are then ignored, not
merged. Capture is lossless 48 kHz FLAC with an 80 Hz highpass only; no
denoise at any stage (it measurably hurts ASR and speaker embeddings), and
raw parts are the sole transcription and playback-export source.

Audio files are gitignored either way — they are huge and the transcript is
the durable artifact. Back audio up outside git until the session's
`ingest(sNN)` commit lands; retention after that is the DM's call.

## Scene markers

The Run Scene button on a scene page appends one NDJSON line to the live
session's `audio/markers.jsonl` — `scene_slug`, `scene_number`, `label`,
and `t_offset_s` (seconds since the recorder's `started_at_epoch`).
The recorder adds `recording-started`/`recording-ended` sentinels and folds
the log into a sorted `audio/markers.json` on stop; `transcribe-session`
reads the finalized file, falling back to the `.jsonl` if the recorder died
hard. Recording is continuous — markers never split the audio.

Each utterance's scene is the last marker at or before its start; everything
before the first marker is the **pre-session** segment. Outputs carry the tag
as a trailing `Scene` CSV column, a `scene` JSON field, and
`## Scene NN — <label>` / `## Pre-session` heading lines in the MD on scene
change. A session with no markers keeps the exact 5-column shape.

## Cross-mic ghost dedup (multi-track only)

The two room mics bleed into each other acoustically, and ASR transcribes
loud bleed as a garbled ghost copy on the mic that did not own it.
`transcribe-session` dedups at merge time — an overlapping cross-mic pair
whose word sequences nearly contain each other is one physical utterance;
the fuller rendering wins, word-count ties go to the close DM mic.
`--no-dedup` opts out. No audio-mutating pass exists or is wanted.

## Engines

`transcribe-session --engine <name>` (or `engine:` in `config.yaml`); the
default is `parakeet-v3`.

- `parakeet-v3` — local NVIDIA Parakeet-TDT 0.6b v3 via `parakeet-mlx`
  (`pip install "shattered-audio[parakeet]"`). Faster than Whisper on
  M-series, 25 European languages, word timestamps. The model loads once per
  process and decodes in 120 s chunks (15 s overlap) — unchunked decode of a
  long track runs slower, costs gigabytes, and silently drops most speech.
- `whisper` — local MLX Whisper large-v3; `--model` overrides the model id.
- `elevenlabs` — ElevenLabs Scribe v2 (`scribe_v2`, diarization on, word
  timestamps). Needs `ELEVENLABS_API_KEY` in the environment or
  `.env.local`; billed per audio hour — run a 120 s excerpt before a full
  session. Its diarization speaker ids feed a majority-vote backfill for
  utterances the local voice-profile pass could not identify (profile
  matches are never overwritten).

## Output formats

Per-part transcripts default to CSV
(`transcripts/raw/session-NN-part-MM.csv`, columns
`ID,Start,End,Speaker,Text`) — the canonical artifact downstream tooling
reads; sessions recorded with scene markers append a sixth `Scene` column.
Repeatable `--format csv|jsonl|md` (or `output_formats:` in `config.yaml`)
additionally writes sibling `.jsonl` / `.md` files; the CSV is always
written regardless.

## Autocorrect dictionary

`autocorrect.csv` in this directory (or `autocorrect_path:` in
`config.yaml`) maps recurring mistranscriptions to corrections — header
`wrong,right,mode`, `#` comments allowed. Matching is word-boundary and
case-insensitive with case-preserving replacement; a `wrong` containing
spaces matches as a phrase, and longer entries pre-empt shorter ones. The
pass runs on merged rows after cross-mic dedup, so engine output is never
mutated; every applied correction is audited to a sidecar
`session-NN-part-MM.autocorrect.jsonl`. `--no-autocorrect` disables the
pass; a missing dictionary is a silent no-op.

`shattered-audio correct promote` proposes single-token Text fixes recurring
across sessions as new dictionary rows (human-gated append).

## Timing

Transcription runs roughly 0.1–0.3× realtime on decent hardware — the
slowest phase. Kick it off right after the session so INGEST can happen the
next day. A session with audio but no `transcript.md` after 3 days is
pipeline rot; surface it at session start.
