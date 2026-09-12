# Source ingest queue: ss-session-01

Source root: /Users/nick/ai-os/shattered-sea/wiki/sessions/session-01-recap.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — `session :: sessions/session-01-recap.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:11 "REVIEWED-BY-HUMAN: 2026-07-13 — per the user's handoff mission..."
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] sessions/session-01-recap.md — triage: session, skipped — hand off to transcript-label/transcript-ingest

## Claims — sessions/session-01-recap.md

- none — Hard Rule 5: chronological table-play material hands off rather than
  being decomposed here. No claims list opened.

## Flags

1. **Hard Rule 5 fired cleanly on this file's own frontmatter, no judgment
   call needed.** The source's frontmatter reads `type: session` /
   `subtype: recap` and its body is a linear prose account of one session's
   table-play (boarding of the Saltwright, the gangplank fight, Geoffrey's
   defection) closed by a `## State at Break` / `## Threads Left Open`
   structure. That is exactly the claim-buckets.md "Session chronology, even
   if never audio-recorded" row → "Hand off — Hard Rule 5". Triage was a
   frontmatter/structure match, not an inference.

2. **Hand-off target does not actually fit as stated — filed for the DM,
   not resolved unilaterally.** Read both destination skills'
   frontmatter/description before triaging as instructed:
   - `transcript-label` (`.claude/skills/transcript-label/SKILL.md`)
     description: "Turn raw speaker-diarized output into the frozen,
     speaker-labeled `transcript.md`... Use... when
     `transcript.raw.md` appears in `sessions/NN-slug/`". Its Gate check
     literally requires `sessions/NN-slug/transcript.raw.md` to exist
     (`ls sessions/NN-slug/audio/ sessions/NN-slug/transcript.raw.md`) — a
     file only produced from audio, via an audio-transcription step. This recap
     never passed through audio; there is no `transcript.raw.md` and never
     will be one for it. transcript-label's gate cannot pass for this
     source.
   - `transcript-ingest` (`.claude/skills/transcript-ingest/SKILL.md`)
     description: "Turn a frozen, speaker-labeled `transcript.md` into a
     reviewed session ledger... Use when... `sessions/NN-slug/transcript.md`
     exists". Its Gate check requires `transcript.md` plus a speaker-label
     line count (`**Name:**` pattern) ≥ 50 hits — i.e. a diarized,
     per-utterance dialogue transcript. This source is third-person prose
     recap text, not speaker-attributed dialogue; it has zero `**Name:**`
     lines and would fail the ≥50 gate even if renamed into place.
   - **Neither destination skill's contract accepts this file as-is.** Hard
     Rule 5's hand-off is correct in spirit (this is session-chronology
     content, not an NPC/location/faction/item claim this skill should
     decompose) but the literal skill it names doesn't have an intake path
     for a *prose recap with no underlying audio/transcript*. Not resolved
     here — resolving it would mean either inventing a synthetic
     `transcript.md` from prose (fabricating dialogue attribution that
     never existed) or writing a new ingestion path, both out of this
     skill's scope. Flagging for the DM: this session's actual
     `state-changes.md`-equivalent may need to be hand-authored/reviewed
     directly from the recap, bypassing transcript-label/transcript-ingest
     entirely, or a new "recap-only" intake needs to be designed.

3. **No wiki page written, no world/pcs/sessions/ touch.** Per the flag
   above, this queue entry closes as skipped. No claims were opened, no
   skeleton instantiated, no `world/`/`pcs/`/`sessions/` file created or
   modified.
