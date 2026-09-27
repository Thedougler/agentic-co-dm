---
name: development-beats
description: >-
  Write, edit, or create content for a Development — the non-combat "bump"
  that changes what players know, can reach, or choose between and sets the
  direction of action until the next Development: clues, revelations, talk
  scenes, alliances, betrayals, warnings. Card catalog (Pondsmith's
  Developments), fill steps, and table-ready check.
---

# Development beats

A Development is the **bump**: a scene where the plot moves without physical
conflict and sets the direction of action until the next Development changes
it. Gandalf's visit tells Frodo what the Ring is; Ilsa walking into Rick's
café forces Rick's hand. It gives the party a clue, a warning, a truth, an
ally, or an edge — and hands the next Cliffhanger stakes the table can read.

## Gates

**Session plan first.** Before reading further or loading any other skill,
find this session's filed plan (`Session-<NN>-00-*.md` in its session
folder). With none, stop here: load `plan-session` and plan with the DM;
this skill resumes from the plan's row once `session-beats` files it.

Prep only. Follow `docs/agents/work.md`. Follow AGENTS.md **HARD: entity-before-spoken** and **HARD: dm-facing-explicit**.
Cast and invent per `docs/agents/table-ready.md` § Cast before minting and § Fill the silence.

## Boundary contract

- **Input:** A named Development beat, its session-plan row (card, thread,
  trigger, next beat), the preceding carry-forward, and linked owner pages.
- **Session plan:** the short form of the DM's intent for the session; this
  beat is written from its row (see Gates).
- **Work:** Build one Development to the table-ready bar with the Development
  craft below; spoken text is filled through `theatre-of-the-mind`.
- **Done:** The cold read passes and the completion test holds.
- **Capability Handoff:** Return the Development page and its carry-forward to
  the next Cliffhanger, which opens from the revealed thread, the party's new
  direction, and the contest's entry conditions; a missing entry fact returns
  as a named gap.

## Copy-start

Copy `wiki/templates/development.md`. File after accept to `wiki/journal/sessions/<campaign-slug>/<session-number>/Session-<n>-<BB>-<Label>.md`; when the request names no session, list `wiki/journal/sessions/<campaign-slug>/`, take the next session to be played, and say so. Keep the sections the template marks `Required.` and every section this Development spends at the table; delete the rest (fact-only, `wiki/AGENTS.md` Layout). Add no section the template lacks: refiling an older page moves each old section's facts into the template section that owns them (fighter numbers and tactics into Actors, pressure into Situation or Pressure where the template has it).

## Fill a Development

1. **Ground.** Read the preceding beat's carry-forward, the session plan row,
   and the owner pages for every actor, place, item, and lore fact the scene
   touches (retrieve with `qmd`). Done when the party's position, condition,
   and current beliefs are stated, and each actor's current want is sourced or
   proposed (`docs/agents/table-ready.md` § Fill the silence).
2. **Choose the card.** Read
   [references/development-cards.md](references/development-cards.md) and pick
   the card the fiction calls for. Name the live thread it advances and the
   **turn**: the one fact or change that sets the new direction. The card goes in the beat's frontmatter `card:` and the thread in the session plan's Threads table; the page body carries only what they produce.
3. **Cast owners.** Every named NPC, place, item, faction, or lore fact the
   scene needs has an owner page before any text depends on it: cast from the
   wiki first, and mint with its owner skill (`npc-design` for a new speaker)
   only what nothing fits (`docs/agents/table-ready.md` § Cast before minting).
4. **Read the bar.** Read `docs/agents/table-ready.md`, then build every
   anatomy part the scene spends, applying the Development craft below.
   Write every DM-facing line with `writing-for-humans`: each fact on the
   page has a moment of use and one home, and what the wiki holds is embedded.
5. **Set rulings.** Load `dnd5e-mechanics` for Influence, Search, Study,
   Insight, and every other check, save, and DC.
6. **Fill the spoken layer.** Load `theatre-of-the-mind` and fill `Opening`;
   one `{NPC}` block per actor the party meets, titled with the name, ending
   on their first words; `Revelation` for the moment the Core clue lands
   (Revelation recipe); and the `_italic_` Narration cells in Outcomes. Put
   quoted lines for the actors who speak in their Actors bullets. Delete a
   slot that has no spoken text.
7. **Write the handoff.** The next beat is a Cliffhanger that tests what was
   just learned under cost. The carry-forward names the new knowledge, the
   party's new direction, and the entry conditions of that contest (who is
   where, what they carry, what they chose to prepare).
8. **Cold read.** Run the cold read from `docs/agents/table-ready.md` and the
   completion test. Fix every gap before filing.

## Development craft

- **The turn is one sentence.** State, DM-facing, the fact or change that
  reorients the party, and the direction of action it sets ("the order came
  from the Gold caste, so the answers are in the memorial grove"). A beat that
  only adds detail to what the party already knew has no turn; find the facet
  that changes a choice.
- **The story, not the solution.** Clue gives one piece; Revelation may give
  the whole story. Neither hands over the solution to the next contest —
  knowing where the villain sleeps still leaves his guards and his clock. When
  a request asks one Development to answer everything including how to win,
  reveal the story and a real facet of the solution, and leave the contest
  that tests it.
- **Actors run the scene.** Each actor has an Actors bullet: wants now,
  knows (the true facts), offers, withholds or lies about (and the lie's
  tell), price for help, and what shifts their posture. The DM plays the
  scene from these rows without improvising motive.
- **Something to do with your hands.** Give talk and investigation scenes a
  physical anchor: a site to search, a body to examine, a map to read, a meal
  to share, a ritual to witness. It goes in Situation's **Evidence**, and a
  place the party can search or watch gets its own Party Choices line. Each anchor
  surfaces at least one clue.
- **Truths with routes.** The Clues list states each truth as fact with
  where it surfaces. A conclusion the session depends on has three
  independent routes (person, place, object).
- **Information costs.** Getting the good part costs something — a favor, a
  promise, time on the clock, exposure, a check with a cost on failure. The
  Party Choices **Cost** line names it.
- **The truth waits for no one.** Situation's **If ignored** says what happens
  to the truth or the lead if the party walks past it.
- **Stall breaker.** Name what ends the beat if talk circles: an actor's
  deadline, an interruption, a pressure tick. When the party has a usable
  direction, cut.
- **Preparation beats map their states.** When the Development is the party
  preparing (watches, defenses, plans), list two or three distinct
  preparation states as Outcomes rows, each with the named consequence it
  gives the next Cliffhanger, and ask what they actually do.
- **Threads, not filler.** The Development advances a live thread. A request
  for an unrelated vignette or a revived abandoned thread becomes a facet of a
  live thread, or returns to `session-beats` as a chart question.

## Completion test

Players can name what they now know or can decide that they could not
before; the page states the direction of action that knowledge sets; and the
next Cliffhanger's stakes are legible from it. On the page:

- the turn sentence names the choice it changes and the direction it sets;
- the good part costs something, with the price named;
- a stall breaker names who or what ends the scene, and when;
- a physical anchor surfaces at least one revelation;
- every question the scene sends the party away with names where its answer
  lives (who knows, where, at what price), and the DM layer holds the answer.

Every section on the page is a section of the template; none is left over from an older layout, and no card, tier, or thread label appears in the body (the card goes in frontmatter `card:`). Each actor the party meets has its own `{NPC}` or `{Creature}` narration block, titled with its name; an NPC's block ends on their first words.

## Named seams

- **Chart question** → load `session-beats` for position, polarity, threads,
  or transition only.
- **An exit row names a next beat type** → load that type skill for the
  handoff only. Do not absorb the next beat's fill.

Chart assembly, polarity rules, time budget, thread planting, escalation,
recompute, and the session plan belong to `session-beats`. Spoken player text
belongs to `theatre-of-the-mind`. Wiki kind pages keep their owners; other
type-card catalogs load only through a seam above.
