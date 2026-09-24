---
name: city-design
description: >-
  Write, edit, or create named city pages for the campaign wiki. Use when a
  city, metropolis, capital, port city, districted settlement, missing named
  city note, city arrival, urban orientation, gazetteer, local table rules,
  city pressure, active urban situation, or city change log needs a persistent
  page. Fill wiki/templates/city.md. place-design is the place hub and defers
  kind: city page work here.
---

# City Design

Prep only. Follow `docs/agents/work.md`.

## Boundary contract

### Input

Take a named city owner, the caller's objective, and the relevant brief, city
template, and linked region/place/faction notes. When the owner is a city,
enter this skill directly; do not route through a generic place planner.

### Owner-specific Work

Work only the named city: preserve its canon, fill `wiki/templates/city.md`,
and apply the arrival, orientation, gazetteer, local-rule, and active-situation
craft below. Keep the caller's session or situation objective intact.

### Capability Handoff

Faction → `faction-design`. Non-city place → `place-design`. Off-screen
motion → `world-tick`. The child does not re-plan the city.

### Done

Use the existing `## Done` checklist below. Completion is observable when the
named city page path, city template contract, playable urban choices, and any
child return evidence are reported.

## Refuse gates

- **Work gate.** Show a chat proposal before writing under `wiki/`. Write only
  after DM acceptance. A missing named city is work to propose now — not out of
  scope.
- **Invention.** Never present invention as wiki fact. Set `invention: true`,
  cite `[[pages]]`, show contradictions, and propose for acceptance. No silent
  canon.
- **No invented crisis.** Do not invent plague, siege, invasion, or disaster as
  established pressure. Derive **If-nobody-intervenes** only from established
  pressure — or state none / labeled invention.
- **Closed canon stays history.** Preserve closed Season threads as history, not
  live crisis. Do not reopen them as forced sequences.
- **Template lock.** Copy `wiki/templates/city.md` only. Keep `type: place` and
  `kind: city`. No second template; do not retarget to region, faction, lore, or
  quest.
- **Arrival.** `> [!narration] Arrival` is immediately perceivable only
  (scale, silhouette, motion, sound, smell, landmark). No secrets, DCs, hidden
  history, or unearned names.
- **Faction agendas/clocks** stay on faction pages. City `# Power` is local
  posture only (public position, local objective, leverage, current move here).
- **Hub deferral.** `place-design` defers `kind: city` page work here.

Also refuse: single mandatory plot rails; authoring PC civic outcomes as page
fact; clue-less single-lever situations; combat-only district rails. Keep
Orientation/Gazetteer as choice space (≥2 viable responses or ignore/fail/
redirect costs).

## City job

A city page makes a named city runnable: arrival, orientation, deliberate
travel, local rules that change choices, active pressure, and what changes if
nobody intervenes. Use when districts, public authority, services, factions,
routes, laws, or urban pressure exceed a site-place page.

## Build the city

1. **Retrieve.** Read the brief, `wiki/templates/city.md`, and relevant region,
   route, district, landmark, faction, NPC, quest, lore, session, and prior city
   notes. Preserve established names, aliases, districts, routes, laws,
   pressure, rumors, party history, and open questions.
2. **Identity sentence** before drafting:

   > This is a [kind/scope] city known for [public identity], pressured by
   > [current instability], and it gives players [choice or opportunity].

   If there is no current pressure or player opening, keep retrieving or ask.
3. **Scaffold.** Copy `wiki/templates/city.md`. Fill frontmatter: `type: place`,
   `kind: city`, reveal/campaign/visibility, region, status,
   population, government, ruler, controlling_faction, summary.
4. **Runnable fill.** Arrival (perceivable); At a glance (character, known-for,
   visible power, **current pressure**, opportunity, population, one-sentence DM
   thesis of play function — not closed-history summary); Orientation
   (districts + getting around); Gazetteer (arrive/leave, stay, buy/sell,
   services); Rules that matter (only choice-changing local realities); Power
   (city-local posture only).
5. **Active situations.** Use plain `## Situation` headings for active situation cards; keep the heading unlinked because it is a structural slot, not an entity. Establish at least one when pressure exists: actors, visible signs, want, opposition, **If nobody intervenes**, trigger/date. Link quest pages for pursuable objectives; propose missing quests — do not bury full quests here. If no established pressure, say so; do not invent crisis.
6. **Current state + change log.** Live deltas only on the city page; fold normalized deltas into baseline and archive in `# Change log`.

Read `references/city-craft.md` for craft basis, section fill detail, audit
questions, and failure modes.

## Handoffs

Narration → `theatre-of-the-mind`; places → `place-design` (non-city);
factions → `faction-design`; NPCs → `npc-design`; quests → quest skill;
off-screen → `world-tick`; vault lookup → `.agents/skills/qmd`.

## Done

- Fills `wiki/templates/city.md`; `type: place` + `kind: city`; no second
  template / no retarget.
- Arrival is `[!narration]` and perceivable-only.
- At a glance has current pressure + opportunity; DM thesis is play-function.
- Orientation has districts + getting around; gazetteer supports intentional
  seek; rules name choice-changing local realities.
- ≥1 active situation with actors, signs, want, opposition, if-nobody-intervenes
  from established pressure (or none / labeled invention).
- Faction full agendas/clocks stay on faction pages.
- Current state = live deltas; change log on the city page.
- Invention labeled, cited, proposed; wiki write only after accept.
- DM can arrive, find a district, seek a place, name a local rule, and say what
  happens if nobody intervenes — without a single mandatory rail.
