---
name: region-design
description: >-
  Write, edit, or create named region pages for the campaign wiki. Use when a
  region, realm, province, frontier, wilderness, forest, mountains,
  archipelago, sea, valley, district, route-scale area, missing named region
  note, regional spoken look, geography, travel routes, active powers, existing
  pressure, or regional change log needs a persistent page. Fill
  wiki/templates/region.md. place-design is the place hub and defers region page
  work here.
---

# Region Design

Prep only. Follow `docs/agents/work.md`.

## Boundary contract

### Input

Take a named region owner, the caller's objective, and the relevant brief,
`wiki/templates/region.md`, and linked geography, route, place, faction, and
session notes. When the owner is a region, enter this skill directly rather
than a generic place or campaign orchestrator.

### Owner-specific Work

Work only the named region: preserve its scale and canon, fill the region
template, and apply the identity, route-choice, active-power, and pressure
craft below. Keep the caller's objective intact while retrieving local facts.

### Capability Handoff

City → `city-design`. Site → `place-design`. Faction → `faction-design`.
Off-screen motion → `world-tick`. The child does not re-plan the region.

### Done

Use the existing `## Done` checklist below. Completion is observable when the
named region page path, region template contract, route choices, active powers,
and any child return evidence are reported.

## Refuse gates

- **Work gate.** Show a chat proposal before writing under `wiki/`. Write only
  after DM acceptance. A missing named region is work to propose now — not out
  of scope. Workspace outputs allowed before acceptance.
- **Invention.** Never present invention as wiki fact. Set `invention: true` (or
  mark proposed), cite `[[pages]]`, show contradictions, and propose for
  acceptance. No silent canon.
- **No invented pressure.** Do not invent an ancient evil, warlord invasion,
  Crown occupation war, plague, front, clock, villain plan, or other
  macro-threat as established fact. Use `## Fronts and pressures` only for
  pressures already stated by wiki, session, or accepted brief — or omit / mark
  `None established yet` / proposed. A pressure-free region still passes.
- **No type: front.** Do not create or revive `type: front`. Pursuable pressure
  links or proposes a quest page.
- **Template lock.** Copy `wiki/templates/region.md` only. Keep `type: region`.
  No second template; do not retarget to place, quest, faction, lore, or front.
- **Narration.** `> [!narration] Narration` is traveler-perceivable only
  (horizon, terrain, weather, motion, sound, one unmistakable feature). No
  secrets, save DCs, hidden history, secret coordinates, or unearned names.
- **Identity first.** Before the page draft:

  > This is a [scale/kind] region known for [public identity], crossed by [route
  > choices], and changeable by [active powers].

  If that lacks route choices or who can change the region, keep retrieving or
  ask. Do not invent pressure to make the sentence dramatic.
- **Route choice space.** Travel/routes need concrete tradeoffs (time, cost,
  risk, advantage, discovery) across ≥2 viable approaches — refuse a single
  mandatory ordered corridor that erases keyed places.
- **No PC authorship.** Do not present PC travel outcomes, refused rules, or
  bound pressures as established Current state. Present options; leave choices
  to play.
- **Hub deferral.** `place-design` defers region page work here.

Also refuse: encyclopedia DM thesis with no table function; overwriting
established named links/hazards with invented crisis; treating taking-rule /
ecology hazards as safe without surfacing the contradiction.

## Region job

A region page makes an area runnable for travel and off-screen motion: first-
travel look, kind/scale, route choices, who can change it, and what changed
since the last stable state. Use when identity, travel structure, powers,
landmarks, routes, or nested places exceed a site-place page.

## Build the region

1. **Retrieve.** Brief, `wiki/templates/region.md`, and relevant parent region,
   subregion, city, place, route, faction, NPC, quest, lore, session, and prior
   region notes. Preserve established names, aliases, scale, kind, boundaries,
   routes, anchors, landmarks, powers, active pressure, party history, current
   state, and open questions.
2. **Identity sentence** before drafting (see refuse gate).
3. **Scaffold.** Copy `wiki/templates/region.md`. Frontmatter: `type: region`,
   reveal/campaign/visibility, parent `region`, `scale`
   (macro|regional|local), `kind`, `structure`, `as_of`, `summary`.
4. **Runnable fill.** Narration (perceivable); At a glance (scale, kind,
   character, anchor, known-for, feared-for, parent; DM thesis = table function:
   route choices / who can change the region — not encyclopedia lore); Current
   state (status quo now; link pressure only when already stated); Geography +
   Travel (boundaries, landmarks, route tradeoffs); Key places (table-ready
   durable places only); Active powers (few groups that can change it now: hold,
   want, next move, reveal — full agendas stay on faction pages).
5. **Pressure without creating it.** Link existing owner notes; omit or mark
   none when absent. Do not invent crisis for the template section.
6. **Omit by scale + change log.** MACRO/REGIONAL/LOCAL keep only headings that
   create choices. Current state = live status; Change log = deltas (fold
   normalized deltas into baseline).

Read `references/region-craft.md` for craft basis, section fill detail, omit-by-
scale, audit questions, and failure modes.

## Handoffs

Narration → `theatre-of-the-mind`; places → `place-design`; cities →
`city-design`; factions → `faction-design`; NPCs → `npc-design`; quests → quest
skill; off-screen → `world-tick`; vault lookup → `.agents/skills/qmd`.

## Done

- Fills `wiki/templates/region.md`; `type: region`; no second template / no
  retarget / no `type: front`.
- Identity sentence before draft; narration is `[!narration]` and
  perceivable-only.
- At a glance has scale, kind, character, anchor, parent when known; DM thesis
  is table function.
- Current state states status quo now; geography/travel offer real route
  choices (≥2 tradeoffs).
- Active powers name who can change the region and next visible moves.
- Existing pressure linked; absent pressure not invented and still passes.
- Extra headings omitted by scale; change log records deltas.
- Invention labeled, cited, proposed; wiki write only after accept.
- DM can describe arrival, offer routes, name who can change the region, and say
  what changed since the last stable state.
