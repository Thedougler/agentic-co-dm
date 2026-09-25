---
name: cliffhanger-beats
description: >-
  Write, edit, or create content for a Cliffhanger — a short, dangerous contest
  whose outcome stays in doubt, changing position, resources, safety, or time
  and testing what the last Development revealed. Card catalog (Pondsmith's
  Cliffhangers), escalation ladder, fill steps, and table-ready check.
---

# Cliffhanger beats

A Cliffhanger is **a contest whose outcome is in doubt up to the very end**.
It speeds up the plot and wakes the table with a note of danger: the monster
guarding the secret is a better problem than the secret. Keep it short and
deadly, put the threat of defeat right up front, and save the best for last.
It tests what the preceding Development revealed, and its result is the
changed physical situation the next Development must deal with.

## Gates

Prep only. Follow `docs/agents/work.md`. Follow AGENTS.md **HARD: entity-before-spoken** and **HARD: dm-facing-explicit**.
Cast and invent per `docs/agents/table-ready.md` § Cast before minting and § Fill the silence.

## Boundary contract

- **Input:** A named Cliffhanger beat, its session-plan row (card, thread,
  escalation tier, trigger, next beat), the preceding carry-forward, and
  terrain and opposition owner pages.
- **Session plan first:** The session plan is the short form of the DM's intent
  for the session, and this beat is written from its row. When the session has
  no filed plan, make one before writing the beat: load `plan-session` to shape
  the DM's intent together, then `session-beats` to file the plan.
- **Work:** Build one Cliffhanger to the table-ready bar with the Cliffhanger
  craft below; spoken text is filled through `theatre-of-the-mind`.
- **Done:** The cold read passes and the completion test holds for every
  outcome row.
- **Capability Handoff:** Return the Cliffhanger page and its carry-forward
  per outcome. The next Development (or a Retreat or Hesitation Development
  when the outcome names one) opens from that carry-forward; a missing entry
  fact returns as a named gap.

## Copy-start

Copy `wiki/templates/cliffhanger.md`. File after accept to `wiki/journal/sessions/<campaign-slug>/<session-number>/Session-<n>-<BB>-<Label>.md`; when the request names no session, list `wiki/journal/sessions/<campaign-slug>/`, take the next session to be played, and say so. Keep the template's jobs; omit a section only when this Cliffhanger never spends it.

## Fill a Cliffhanger

1. **Ground.** Read the preceding beat's carry-forward, the session plan row,
   and the owner pages for the opposition, place, and any item or vehicle in
   play (retrieve with `qmd`). Done when positions, conditions, resources, and
   the knowledge the party carries in are stated.
2. **Choose the card and tier.** Read
   [references/cliffhanger-cards.md](references/cliffhanger-cards.md). Pick the
   card the fiction calls for and the escalation tier this slot holds on the
   session's ladder. Name the thread under test — what the last Development
   revealed that this contest proves or disproves.
3. **Cast owners.** Every creature, NPC, place, vehicle, or item the contest
   needs has an owner page before any text depends on it: cast from the wiki
   first, and mint only what nothing fits (`docs/agents/table-ready.md` § Cast before minting); a creature the
   party could fight that has no owner goes to `monster-design` (its Reskin
   path fits rank-and-file: a standard statblock with this fiction).
4. **Read the bar.** Read `docs/agents/table-ready.md`, then build every
   anatomy part the contest spends, applying the Cliffhanger craft below.
   Write every DM-facing line with `writing-for-humans`: lead with the
   point, name everything, conditionals in tables, secrets stated plainly.
5. **Set numbers and rulings.** `encounter-prep` sets the difficulty for the
   tier and the live party; `dnd5e-mechanics` sets every check, save, and DC.
   Copy the opposition's compact numbers from its owner statblock onto the
   page. Done when everyone who could fight carries numbers: from the owner
   statblock, or a proposed standard 5e statblock filed on the owner.
6. **Fill the spoken layer.** Load `theatre-of-the-mind` and fill `Open on
   Action` to its Cliffhanger opening recipe.
7. **Write the outcomes.** Won → the next Development opens new options.
   Lost → the next Development opens with new constraints, or the opposition
   plays Retreat or Hesitation. Each outcome row states the changed physical
   situation and the carry-forward.
8. **Cold read.** Run the cold read from `docs/agents/table-ready.md` and the
   completion test. Fix every gap before filing.

## Cliffhanger craft

- **Short.** About three to five rounds of combat, or twenty to thirty
  minutes of table time for a non-combat contest. The page states the end condition, and the
  pressure makes the contest end if nobody else does.
- **Threat up front.** The danger is visible in the opening narration and
  real by round one: the opposition's first move lands, or the hazard bites.
- **Objectives beyond killing.** Each side wants something concrete — seize
  the idol, cross the bridge, drag the prisoner to the boat. Reaching an
  objective, breaking off, surrendering, or escaping each end the contest.
- **Opposition plays to win.** Every opposing side has its compact numbers
  and a tactics line: opening move, how it adapts when the party counters,
  its break point, and its exit (retreat route, escape trick, surrender
  terms). With several factions present, each has its own objective and
  ignores the party unless the party gets in its way.
- **Terrain acts.** Two or three features with rulings (cover, climb DC,
  difficult terrain, a thing that falls or burns) and one change that lands
  mid-contest on a named trigger or round.
- **Escalate each round.** A pressure tick per round or on a named trigger
  moves the objective, narrows an exit, or adds a threat, so the contest
  sharpens instead of grinding.
- **Losing is interesting.** A lost contest changes the situation — captured,
  separated, the item taken, the route cut, the ally hurt — and hands the
  next Development a problem. Death is on the table when the fiction and the
  table's tone put it there, and the page says when.
- **One at a time.** A Cliffhanger hands off to a Development. When a request
  stacks contests back to back, write one Cliffhanger and hand off to a
  Development that makes the next contest's stakes legible.

## Completion test

The contest's result is decided by the party's tactics, choices, and rolls on
the page's rulings; every outcome row changes the physical situation; and the
page states the next beat's trigger for each row. A result fixed before the
party acts is narration — rewrite it as a contest.

## Named seams

- **Chart question** → load `session-beats` for position, polarity, threads,
  or transition only.
- **An outcome row names a next beat type** → load that type skill for the
  handoff only.
- **A named entity (vehicle, spell, faction, lore, quest, city, region)** →
  hand off to its wiki-kind owner.

Chart assembly, polarity rules, time budget, thread planting, escalation
across the session, recompute, and the session plan belong to
`session-beats`. Spoken player text belongs to `theatre-of-the-mind`. Other
type-card catalogs load only through a seam above.
