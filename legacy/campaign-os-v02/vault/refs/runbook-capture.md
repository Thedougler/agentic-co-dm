---
type: runbook
status: canon
publish: false
aliases: []
created: "2026-07-23"
updated: "2026-08-08"
tags: [craft]
summary: "Phase 3: turn session audio into the frozen, speaker-labeled transcript.md the pipeline ingests."
phase: 3
uid: 06de6ced-bef7-4415-b50e-803f2add7750
---

# Capture runbook (Phase 3)

Trigger: an audio file appears in `vault/episodes/NNN/audio/`.

GATE: session dir exists and audio has landed. Run `ls vault/episodes/NNN/
vault/episodes/NNN/audio/ 2>/dev/null`, paste. No session dir -> STOP (PREP
(Phase 1) hasn't created it yet). No audio -> STOP (the session hasn't
recorded yet (`record-session-audio` skill)).

## Interface contract

The only part downstream phases depend on:

1. `sessions/NNN/transcript.raw.md`: engine output with timestamps, unedited.
2. `sessions/NNN/transcript.md`: speaker-labeled, mechanically cleaned, stable
   L-numbers, `**Name:** utterance` (one utterance per line, an
   `[hh:mm:ss]` timestamp at least every speaker change).

Everything below is one way to meet that contract. Swapping the
recorder or the STT service changes the steps, never these two outputs.

## Steps

1. Record the session audio: `record-session-audio` skill, run live at the
   table (`utils/tools/audio/README.md` § Audio layouts for output layout).
2. Transcribe: `shattered-audio transcribe-session --session NN --audio-dir
   sessions` (`utils/tools/audio/README.md` § Engines, § Output formats).
   Produces the canonical per-part CSV and a `sessions/NNN/transcript.raw.md` sibling.
3. Optionally run the corrector pass: `transcript-correct` skill, over the
   CSV, before labeling. Follow its own split -> 4-parallel-fixer -> merge
   shape, don't restate it. The dictionary
   (`utils/tools/audio/README.md` § auto-correct dictionary) handles *known*
   recurring fixes automatically; this pass *discovers* new ones.
4. Label speakers: `transcript-label` skill, turns `sessions/NNN/transcript.raw.md` into
   the frozen `vault/episodes/NNN/transcript.md` per the Interface contract
   above (`vault/refs/runbook-ingest.md` decides relevance, not this pass).
   Paste the skill's own `CAPTURE:` marker.

Done = `CAPTURE: transcript.md written, N lines, M speakers resolved (K at
low/unknown confidence)`, `**?:**` density < 20% (transcript-label workflow
step 7), commit `capture(sNN): ...`
