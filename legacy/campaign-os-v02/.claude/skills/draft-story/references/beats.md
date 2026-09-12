# Beats — sequencing a fixed pile into a journey

Reached from [SKILL.md](../SKILL.md)'s `DS4`. The exploring is done and the
pile is fixed; commit to a path through it and mine the pile to fill each
beat. The pile is a quarry — paraphrase, split, recombine, quote.

## What is a beat

One move in the journey. It does one thing — sets a scene, lands a point,
raises a question, twists the angle — then stops, leaving the reader where
the next beat can pivot. Sized by what it needs: a single sentence ("And then
nothing happened for three weeks."), a short paragraph, or a self-contained
vignette. Needs five paragraphs and three subheadings? That is two beats
glued together — split it.

## Grounding — the discipline that shapes the journey

Every **concept** must be grounded before a beat can lean on it: the audience
either walked in knowing it (**prerequisite**) or met it in an earlier beat
(**introduced**). In campaign terms: **a beat never reveals or relies on lore
the players haven't earned.** The unit is the concept, not the word for it — a
beat can leak an idea with no proper noun in sight. Where a concept has a
name, ground the idea and the name together.

- Settle prerequisites with the GM before the first beat: what does the
  audience (players, or the DM for DM-only sections) already know? For
  player-facing journeys, canon revealed at the table is grounded;
  `status: pending` and DM-only material is not.
- Each beat **requires** grounded concepts and **grounds** new ones. Keep a
  running list; update it as each beat lands.
- A candidate beat is reachable only if everything it requires is grounded.
  Picking a beat that grounds X unlocks every beat waiting on X — say what
  each candidate grounds, so the GM sees which paths it opens.
- A tempting beat requires an ungrounded concept -> either insert a grounding
  beat before it, or ask the GM to promote the concept to a prerequisite.

## The loop

1. **Pick a shape before the first beat** —
   `.claude/skills/draft-story/references/story-structures.md`. The shape constrains which
   candidates make sense. Session-scale journeys also check the arc in
   `.claude/skills/composing-beats/references/rhythm-and-pacing.md`.
2. **Gather the pile**: the fragments/seed/ledger material, plus a grep for
   every established entity the journey touches. Check
   `vault/ideas/lines.md` for a reserved line the
   journey could place — never force one.
3. **Establish prerequisites** with the GM (§ Grounding) — one message, all
   questions at once.
4. **Offer 2-3 candidate starting beats** from the pile, each a different
   entry point, each reachable, each noting what it grounds.
5. **GM picks -> write that beat only.** Preview what the pick unlocks. Stop
   at the pivot.
6. **Loop**: re-read the target from disk, offer 2-3 next beats, write the
   pick. Pacing sagging mid-journey ->
   `.claude/skills/composing-beats/references/rhythm-and-pacing.md` § Pacing tools (ticking clock,
   breather, dramatic cut, information drip).
7. **End when the journey completes, not when the pile is empty.** Leftover
   fragments are the point of having more raw material than you need — leave
   them in the fragments file.

## Rules

1. **One beat per write. Never write ahead.** Candidates are genuine options
   with a preview of what each unlocks — never a gotcha, never a decoy you
   have already decided against.
2. **Re-read the target file from disk before every write.** GM edits are
   sacrosanct — preserve them absolutely, and let a substantial edit to an
   earlier beat change what you offer next. "Rewrite beat 3" -> edit in place,
   leave the rest alone.
3. **Grounding binds every beat.** No lore the players haven't earned in
   player-facing prose; no campaign fact stated from memory.

## When the beats serve a page instead of the chapter

`DS4` normally sequences the story itself. When another skill has already
designated a target section, the beats land there and this file never creates
the page:

| The journey is... | Target | Owning skill |
|---|---|---|
| A quest line (party objective) | quest page `## Beats` | `.claude/skills/draft-content/references/quest.md` (its Hard Rule 8 hands off here) |
| A faction arc (Front advancing) | `## Goals & Fronts` | `.claude/skills/draft-content/references/faction.md` |
| An NPC arc (hidden motive unfolding) | `## DM Only` | `.claude/skills/draft-content/references/npc.md` |
| A season throughline | season page | `.claude/skills/draft-content/references/season.md` |
| A recap's structure | `vault/episodes/NNN/recap-draft.md` | `recap-writer` (promotes the draft) |
| A session/scene sequence | run-guide scene order | `draft-run-guide` |
| Not yet tied to any page | `vault/ideas/<topic>.md` | staged here; ask once where |

Everything written to a designated target ships at that target's existing
`status:`. Which structural pattern a *quest page* takes is picked by
`.claude/skills/draft-content/references/quest.md` Hard Rule 3 before the handoff — inherit it, never re-pick it.
