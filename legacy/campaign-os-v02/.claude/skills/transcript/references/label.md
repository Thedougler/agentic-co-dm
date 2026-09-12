---
name: transcript-label
description: Turn raw speaker-diarized output into the frozen, speaker-labeled transcript.md a session pipeline ingests — Phase 3 (CAPTURE), in a Campaign OS repo (vault/ present). Use when transcript.raw.md exists with no sibling transcript.md, or for "label the transcript", "resolve speakers", "who is SPEAKER_00". Not CSV correction (transcript-correct) or ingest (transcript-ingest).
---

# Transcript Label

Phase 3 — CAPTURE, second half. `vault/episodes/NNN/transcript.raw.md` already exists
(`vault/refs/runbook-capture.md` § Interface contract); this skill
turns it into `vault/episodes/NNN/transcript.md`, the file every downstream phase cites by
line number. Once written, `vault/episodes/NNN/transcript.md` is frozen — `vault/episodes/` is
append-only (`vault/refs/runbook-wiki.md` § Single-source rules), and ledger lines, CONTRADICTION blocks, and
recaps all cite its L-numbers for the life of the campaign.

## Gate check

Paste before doing anything else:

```
ls vault/episodes/NNN/audio/ vault/episodes/NNN/transcript.raw.md 2>/dev/null
cat vault/episodes/NNN/speakers.yaml 2>/dev/null
```

The real precondition is session dir + `vault/episodes/NNN/transcript.raw.md` existing.
(`vault/refs/runbook-capture.md`'s Phase 3
gate row also lists `speakers.yaml` as a precondition; read literally that
would make this pass unable to ever run on a session's first transcript,
since `vault/refs/runbook-capture.md` specs `speakers.yaml` as something *this pass
creates*. Treat a missing/partial `speakers.yaml` as this step's own output,
not a blocker — flagged REVIEW-for-human in this skill's refactor report.)

No `vault/episodes/NNN/transcript.raw.md` → stop, tell the user transcription hasn't finished
or hasn't run. Never invent transcript content from thin air.

A written legacy session log (prose recap, no audio) skips this skill
entirely — no speakers to resolve. Place it directly at
`vault/episodes/NNN/transcript.md` with a first-line `LEGACY-SOURCE:` header
and hand straight to `transcript-ingest`'s legacy gate.

## Standard queries

Speaker identities are usually stable across sessions — check history and
the character sheets before asking the human to re-identify someone already
on record:

```
find vault/campaigns/shattered-sea/episodes -name "speakers.yaml" -exec cat {} \; 2>/dev/null
grep -rn "^player:" vault/campaigns/shattered-sea/pcs/ 2>/dev/null
```

Empty output on the first query is informative (session 1 — nothing to
carry forward); resolve fresh via the method below.

## Workflow

1. **Gate check** (above), paste evidence.
2. **Read `vault/episodes/NNN/transcript.raw.md` in full** — `[hh:mm:ss] SPEAKER_NN: text`
   segments (`utils/tools/audio/README.md` § Output formats).
3. **Resolve every `SPEAKER_NN` to an identity.** Run the standard queries
   first — an ID that matches a name already in `speakers.yaml` history or
   a `vault/campaigns/shattered-sea/pcs/*.md` `player:` field is resolved without asking. For any ID with
   no match:
   - **Diarization present** (the file has `SPEAKER_NN` labels): sample 3
     utterances for that ID across the file and weigh, in order of signal
     strength:
     1. **Conversational context** — who responds to them, who they respond
        to.
     2. **Process of elimination** — known participants minus already-
        identified IDs.
     3. **Speech pattern / vocabulary** — a phrase or topic only one player
        engages with.
     4. **Temporal clustering** — an ID active exactly when a known
        player's ID goes quiet is very likely the same mic drifting
        profiles; same-second interleaving with a known speaker is
        near-certain evidence of the same person.
     5. **Mechanical context** — a line that self-identifies a specific PC
        ("I'm at 12 HP", "Bardic, yeah").
     A segment that reads as non-game audio entirely (a phone call,
     background conversation, no game-world content at all) resolves to
     `Background (non-game audio)` instead of a person — low confidence,
     and it never gets a `**Name:**` line in `vault/episodes/NNN/transcript.md` (see step 4).
   - **No diarization** (pyannote wasn't configured — `vault/episodes/NNN/transcript.raw.md`
     has no `SPEAKER_NN` structure): label from address patterns in the
     text ("Chad, what do you do?") using the same five signals; anything
     you can't pin down gets `**?:**`.
   - **Assign a confidence**: `high` (multiple signals converge), `medium`
     (one strong signal, nothing contradicts it), `low` (best guess),
     `unknown` (can't determine). Never write `high`/`medium` without
     naming the evidence that earned it.
4. **Write every resolution to `speakers.yaml`** — including ones inherited
   from the standard queries:
   ```yaml
   SPEAKER_00: "Nick (DM)"
   SPEAKER_01: "Kaitlin (as Catarina)"       # medium — carried from s11 speakers.yaml
   SPEAKER_02: "Background (non-game audio)" # low — real-world phone call, lines 340-355
   ```
5. **Degrade by asking — never silently ship a guess.** Any `low` or
   `unknown` confidence resolution: surface it to the human with the
   evidence you have and the specific question ("SPEAKER_03 talks about
   buying whip shark eggs and nobody else's ID goes quiet in that window —
   is this Jean-Claude?"), never "need more info." Persist their answer in
   `speakers.yaml` before moving on.
6. **Format `vault/episodes/NNN/transcript.md`.** One utterance per line:
   `**Name:** utterance text [hh:mm:ss]` — the resolved name from
   `speakers.yaml`, then the text, then a trailing bracketed timestamp on
   every line (satisfies `vault/refs/runbook-capture.md`'s "a timestamp at minimum every
   speaker change" as a floor, and keeps `**Name:**` as the literal line
   start, which the INGEST gate check greps for — see transcript-ingest).
   Mechanical cleanup only:
   - Merge a sentence split across consecutive same-speaker segments (same
     speaker, no intervening speaker, small time gap) into one line; keep
     the earliest timestamp.
   - Fix an obvious speaker-tag glitch (a one-word interjection
     mis-assigned mid-sentence to the wrong known ID).
   - **Never rephrase, never drop "boring" table talk, never summarize.**
     INGEST decides what's worth extracting; this pass only decides who
     said it and where the line breaks fall. A "cleaned" transcript is a
     corrupted evidence trail.
7. **Check `**?:**` density**: `grep -c '^\*\*?:\*\*' vault/episodes/NNN/transcript.md`
   over total utterance-line count. Over 20% → this transcript isn't
   evidence-grade — say so and ask the human: hand-fix the worst offenders
   now, or accept a degraded INGEST that will emit more `REVIEW` lines than
   usual.
8. **Freeze.** Once written, `vault/episodes/NNN/transcript.md`'s line numbers are permanent.
   A flaw discovered later — a mis-transcribed word, a missed speaker —
   gets a footnote appended at the bottom of the file, never an inline
   edit. An inline edit shifts every downstream `Lnnn` citation.
9. Paste the `CAPTURE:` marker: `CAPTURE: transcript.md written, N lines,
   M speakers resolved (K at low/unknown confidence)`.

## Lint before done

`vault/episodes/NNN/transcript.md` and `vault/episodes/NNN/transcript.raw.md` are **not** wiki pages. The
`_templates/*.md` frontmatter schema applies only to pages under `vault/`
and `vault/campaigns/shattered-sea/pcs/`, and `vault/refs/runbook-capture.md`'s Interface contract defines
`vault/episodes/NNN/transcript.md`'s format as plain `**Name:** text` lines with no YAML
block.

**Never add a fake frontmatter block to `vault/episodes/NNN/transcript.md`** — that would
violate the file's real interface contract and corrupt every downstream
L-number citation by shifting line 1.

## Owned paths

Writes `vault/episodes/NNN/speakers.yaml` (create or update) and
`vault/episodes/NNN/transcript.md` (create once; corrections are
footnote-appends only, per Freeze above). Never touches
`vault/episodes/NNN/transcript.raw.md`,
`vault/episodes/NNN/ingest-review.md`, or anything under `vault/`, `vault/campaigns/shattered-sea/pcs/`. This
skill never sets `status: canon` or `publish: true` — trivially true, since
it never opens a `vault/` or `vault/campaigns/shattered-sea/pcs/` file at all (same pattern as `campaign-handoff`).

## Degrade by asking

- Any speaker resolution at `low` or `unknown` confidence → ask, with the
  specific evidence and question, before writing it to `speakers.yaml`.
- `**?:**` density over 20% → ask whether to hand-fix or accept a degraded
  INGEST; never ship silently either way.
- `vault/episodes/NNN/transcript.raw.md` missing → say transcription hasn't produced output
  yet; never fabricate a transcript.

## Craft carried from the legacy skill (session-ingest)

Summary disposition (see this skill's refactor report for the full list
with one-line reasons):

- **Kept-rewritten**: the five-signal speaker resolution method
  (conversational context, elimination, speech patterns, temporal
  clustering, mechanical context) and the confidence-level/escalation
  discipline — the load-bearing craft, retargeted from CSV `Speaker N`
  labels to `SPEAKER_NN` diarization IDs; same underlying problem.
- **Kept-rewritten**: external-audio-artifact handling (phone calls,
  background noise) — folded into the speaker map as a low-confidence
  `Background (non-game audio)` resolution instead of a separate note.
- **Dropped, moved to transcript-ingest**: DM-as-NPC-voice /
  player-voicing-NPC attribution. Labeling only assigns the *physical*
  speaker; whether that speaker is voicing an NPC in the moment is a
  content-attribution judgment the session loop assigns to INGEST, not
  CAPTURE.
- **Flagged as future enhancement, not built** (per dispatch instruction):
  voice-profile retraining (legacy Pass 1b) — this system's
  `vault/refs/runbook-capture.md` Interface contract has no live-capture/cold-pass
  concept to retrain against; would need a new spec first.
- **Dropped**: CSV part-file chunking and progress/handoff-file
  checkpointing — `vault/episodes/NNN/transcript.raw.md` arrives as one file per
  session (`utils/tools/audio/README.md`), not incrementally-arriving part files; no
  chunk-checkpoint machinery is needed for a single-pass labeling job.
- **Dropped**: the legacy "migrating in-progress sessions" section —
  repo-specific to the old Shattered Sea CSV pipeline, not this skill's job.
