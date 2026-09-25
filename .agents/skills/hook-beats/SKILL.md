---
name: hook-beats
description: >-
  Write, edit, or create content for a Hook — the session's strong start: one
  opening pressure that wakes the table and commits the party within minutes.
  Card catalog (Pondsmith's Hooks), fill steps, and table-ready check for Hook
  beats, including resuming a session that ended mid-scene.
---

# Hook beats

A Hook exists to **reel in the line**: wake the players up and get them moving
before anyone fumbles for direction. Like the tomb run that opens *Raiders of
the Lost Ark*, it shows the characters doing interesting things, puts the
opposition or an ally in front of them, and sets the pace and tone of the
night. One Hook per session, about thirty minutes of table time, and it ends the moment the
party is committed.

## Gates

**Session plan first.** Before reading further or loading any other skill,
find this session's filed plan (`Session-<NN>-00-*.md` in its session
folder). With none, stop here: load `plan-session` and plan with the DM;
this skill resumes from the plan's row once `session-beats` files it.

Prep only. Follow `docs/agents/work.md`. Follow AGENTS.md **HARD: entity-before-spoken** and **HARD: dm-facing-explicit**.
Cast and invent per `docs/agents/table-ready.md` § Cast before minting and § Fill the silence.

## Boundary contract

- **Input:** A named Hook beat, its session-plan row (card, thread, trigger,
  next beat), the entry state (last session's ending or the plan's opening
  situation), and linked owner pages.
- **Session plan:** the short form of the DM's intent for the session; this
  beat is written from its row (see Gates).
- **Work:** Build one Hook to the table-ready bar with the Hook craft below;
  spoken text is filled through `theatre-of-the-mind`.
- **Done:** The cold read passes and the completion test holds: the party can
  commit within the beat, and the page states what changed and the next
  beat's trigger.
- **Capability Handoff:** Return the Hook page and its carry-forward. The next
  beat's skill (Development after an action Hook, Cliffhanger after a cerebral
  Hook) opens from that carry-forward; a missing entry fact returns as a named
  gap.

## Copy-start

Copy `wiki/templates/hook.md`. File after accept to `wiki/journal/sessions/<campaign-slug>/<session-number>/Session-<n>-<BB>-<Label>.md`; when the request names no session, list `wiki/journal/sessions/<campaign-slug>/`, take the next session to be played, and say so. Keep the template's jobs; omit a section only when this Hook never spends it.

## Fill a Hook

1. **Ground.** Read the entry state: last session's recap or final beat, the
   session plan row, and the owner pages for every actor, place, and item the
   Hook touches (retrieve with `qmd`). When last session stopped mid-scene,
   record the exact state — positions in feet, HP and conditions, initiative,
   spent resources, who holds what. Done when every fact the opening depends
   on is sourced or proposed (`docs/agents/table-ready.md` § Fill the silence).
2. **Choose the card.** Read [references/hook-cards.md](references/hook-cards.md)
   and pick the card the fiction calls for. A session that stopped mid-action
   resumes as **Play a Cliffhanger** at the recorded state — the tension is
   already there. Done when the card, its key (action or cerebral), and the
   thread it opens are named.
3. **Cast owners.** Every named actor, place, item, or creature the Hook
   needs has an owner page before any text depends on it: cast from the wiki
   first, and mint with its owner skill only what nothing fits
   (`docs/agents/table-ready.md` § Cast before minting).
4. **Read the bar.** Read `docs/agents/table-ready.md`, then build every
   anatomy part the Hook spends, applying the Hook craft below.
   Write every DM-facing line with `writing-for-humans`: lead with the
   point, name everything, conditionals in tables, secrets stated plainly.
5. **Set rulings.** Load `dnd5e-mechanics` for every check, save, and DC. When
   the Hook is a fight, pull the opposition's numbers from its owner
   statblock; `encounter-prep` sets the difficulty when no encounter exists. Done when everyone who could fight carries numbers: from the owner
   statblock, or a proposed standard 5e statblock filed on the owner.
6. **Fill the spoken layer.** Load `theatre-of-the-mind` and fill `Open on`.
   The opening starts inside the changed moment and ends on something a
   player can act on.
7. **Write the handoff.** Action Hook → next Development; cerebral Hook → next
   Cliffhanger. The carry-forward names each state variable the next beat
   inherits, one line per variable with its possible values.
8. **Cold read.** Run the cold read from `docs/agents/table-ready.md` and the
   Hook completion test. Fix every gap before filing.

## Hook craft

- **Start in motion.** The first spoken sentence is already inside the
  trouble: the grab, the scream, the stranger with the letter. Nothing happens
  before it except an optional one-to-three-sentence "previously" — the only
  recap the session gets.
- **Everyone moves in five minutes.** Each PC present has an obvious first
  thing to do or a personal pull (Character pull table). A PC with nothing to
  do in the opening becomes a spectator for the whole beat.
- **Show the night.** The Hook demonstrates the session's tone and pace and
  introduces at least one piece the session uses later: the opposition, an
  ally, the object, the question the Climax answers. A self-contained Hook
  still plants one such piece.
- **Obvious and interesting moves.** Build one obvious first move and at least
  one non-obvious move the space or cast rewards (a feature to exploit, an NPC
  to bargain with, a thing to grab).
- **Short and committed.** The Hook resolves fast. "Hook lands when" names the
  observable commitment — the party gives chase, accepts the job, flees the
  city — and the beat cuts there. Longer stretches of travel or investigation
  are the next beat.
- **Hesitation and refusal are rows.** Hesitating advances the pressure once,
  concretely (the kidnappers reach the boat; the fire takes the stairs).
  Refusing or walking away has a stated world response and leaves another
  door open; the slot does not replay.
- **The Climax's question starts here.** Name the question this Hook opens
  that the Climax will answer, transformed by the middle's costs.

## Completion test

The party can commit to a response within the beat, every approach on the
page has a world response, and the page states what changed and the next
beat's trigger. The Hook is the session's only Hook. On the page:

- the first spoken sentence is already inside something in motion;
- hesitation advances that motion once, concretely, with what the party sees;
- the Hook plants at least one piece a later beat uses;
- every boundary, demand, or taboo the scene states has a row for breaking
  it, with the full consequence copied from its owner page.

## Named seams

- **Chart question** → load `session-beats` for position, polarity, threads,
  or transition only.
- **Play a Cliffhanger as Hook** → load `cliffhanger-beats` for the opening
  shape only. The beat remains the session's one Hook.
- **Play a Development as Hook** → load `development-beats` for the opening
  shape only. The beat remains the session's one Hook.

Chart assembly, polarity rules, time budget, thread planting, escalation,
recompute, and the session plan belong to `session-beats`. Spoken player text
belongs to `theatre-of-the-mind`. Wiki kind pages keep their owners; other
type-card catalogs load only through a seam above.
