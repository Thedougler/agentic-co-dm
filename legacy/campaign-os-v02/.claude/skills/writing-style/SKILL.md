---
name: writing-style
description: >-
  Steer player-facing prose to the DM's voice in a Campaign OS repo
  (vault/refs/stories/ present). Use when writing narration, dialogue,
  recap, Last Time, a depiction, or a sequence-step picture. Also when
  the DM names a favourite book, author, or film, hands over a writing
  sample, or asks to set, extend, or correct the voice.
---

# writing-style

Calibrate player-facing prose to the DM's voice, and grow the profile
when new evidence arrives.

## Choose the branch

| You are about to… | Branch | Go |
|---|---|---|
| Write narration, dialogue, recap, Last Time, a depiction, or a sequence-step picture | Apply | Apply below |
| Set, extend, or correct the voice — a named work, a sample, a sit-down | Build | Build below |

Apply writes no file; the caller writes the prose. Build writes only the four profile files.

Build is **additive**: append new entries and leave every existing one standing. A run that would rewrite or delete an entry stops and asks instead.

## Apply

1. **Route.** Name the file in hand and Read the owning craft skill. Register, tense, word-band, and elicit live there.

   | File in hand | Read |
   |---|---|
   | `type: narration` depiction — entity, Situation, continue, transition | `narration` → depiction |
   | `type: narration` moment, Sequence open or continue, Last Time | `narration` → session |
   | `type: dialogue` | `dialogue` |
   | session recap page | `recap-writer` |

   Done when `A1: <usage> → <craft file>` is written.
2. **Calibrate.** Read `vault/refs/stories/prose-aesthetic.md` and `vault/refs/stories/banned-patterns.md`. Moves are techniques toward award-winning table prose, not a closed vocabulary. Invent; the profile sets rhythm, distance, and never-dos.
   Done when `A2: profile loaded` is written.
3. **Write.** Draft the picture at that rhythm and distance. Style is how it sounds. Known facts are seeds — read the other player-facing files in this session first. Invent texture on the expansion. What the party does, feels, or chooses, and how a check resolves, stay on the owning craft skill (`narration`, `dialogue`, `.claude/skills/composing-beats/references/audits.md` §1).
   Done when `A3: draft exists; seeds at natural size; texture on the expansion; no PC act, feeling, choice, or check resolution stated as fact`.
4. **Confirm.** Read the draft aloud against the craft skill's band and register, and against the profile's never-dos.
   Done when `A4: in band, register held, no banned-pattern hit`.

## Build

### The two inputs

| Input | Branch | Reference |
|---|---|---|
| A work the DM loves — book, author, film | Media | [references/media-analysis.md](references/media-analysis.md) |
| A sample of the DM's own writing | Sample | [references/sample-analysis.md](references/sample-analysis.md) |

Both branches produce the same unit: a **move** — one technique, named, stated so it can be applied
to material with no connection to where it came from. A move is what goes in the files; the source
work never does.

### Workflow

1. **Elicit.** Run [references/interview.md](references/interview.md). The DM named a work or handed
   over a sample already → skip straight to its branch and ask only that file's follow-ups.
   Done when every named work has the DM's own answer to *what they loved about it* on record —
   their answer outranks any critic's.
2. **Analyse.** Media branch → research each work externally (`WebSearch`) before writing anything
   about it; a move sourced from recall is not a finding. Sample branch → extract patterns from the
   prose itself, one quoted example per pattern.
   Done when every named work and every sample has produced at least one move, and any that produced
   none is recorded as such with the reason.
3. **Apply the transfer test.** Every move, one at a time: *could this be applied to material with
   zero relationship to its source?* Pass → it is a technique, keep it. Fail → it is borrowed
   content, cut it.
   Done when every move has been tested individually, not as a batch.
4. **Write.** Append each surviving move to the file the routing table names, in the section that
   already exists for it — add a new heading only when none fits.
   Done when every move from step 3 is on a page and the source note carries a provenance line for it.
5. **Report.** Give the DM the list of what landed, grouped by file, so they can strike anything
   that misreads them.

## Where each finding lands

| Finding | File |
|---|---|
| A positive preference — rhythm, narrative distance, narrator stance, structure | `vault/refs/stories/prose-aesthetic.md`, under its matching section |
| A never-do | `vault/refs/stories/banned-patterns.md` |
| A move absorbed from a named work, and what about that work is *not* an influence | `vault/refs/stories/influences.md` |
| Provenance for any entry above — the work or sample, the date, the DM's own words | `vault/refs/stories/prose-aesthetic-source-note.md` |

`vault/refs/stories/prose-aesthetic.md`'s section set is fixed by the skeleton at
`vault/refs/stories/writing-style-profile.md`: Core Aesthetic, Prose Style, Narrator and Voice,
Structure, What You Do Not Do, Influences, Developmental Feedback Calibration, Source Note. A move
that fits none of those is a sign the move is really two moves — split it.

`vault/refs/stories/writing-style-profile.md` is a recreation of an external source
(`source_url:`) and stays read-only here: it is the completeness check, never a destination.

## Recording an influence honestly

An influence entry carries both halves or it misleads:

- **What transferred** — the moves, each stated as craft.
- **What did not** — the parts of that work the DM does not want reaching their prose. A beloved
  book whose diction, era, or furniture would wreck the register still contributes its structural
  moves; naming the excluded half is what makes the entry safe to apply.

A work the DM enjoyed but that shapes nothing gets one line saying exactly that, so later runs and
drafting agents stop reaching for it.

## Boundaries

- Voice, technique, and calibration. Campaign facts → `llm-wiki-query`; canon → `canon-review`; register and elicit → the owning craft skill in the Apply route table.
- Apply writes no page. Build writes only the four files in the routing table.
- A correction the DM makes mid-draft is captured by the standing CLAUDE.md routing row without invoking Build; both write to the same profile files.

## Reference files

| File | When |
|---|---|
| [references/interview.md](references/interview.md) | Build step 1 |
| [references/media-analysis.md](references/media-analysis.md) | Build, media input |
| [references/sample-analysis.md](references/sample-analysis.md) | Build, sample input |
