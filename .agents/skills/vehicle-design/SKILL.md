---
name: vehicle-design
description: >-
  Design named, playable vehicle pages for the campaign wiki, especially ships
  and boats. Use when a craft needs a persistent identity, travel role, crew,
  components, handling, combat, or a DM-ready vehicle note. Fill
  wiki/templates/vehicle.md, including the sheet and component figures.
---

# Vehicle Design

## Work Gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal before writing a campaign wiki page. Write under `wiki/`
only after DM acceptance. If a needed named craft is missing, that craft is work
to do now: propose the vehicle page instead of treating the missing note as
out of scope. Ground invention in wiki pages and/or D&D 5e vehicle rules; set
`invention: true`, cite `[[pages]]`, and show contradictions. Never present
invention as wiki fact or write silent canon.

## Vehicle Job

A vehicle page makes a named craft runnable: a spoken look, a filled sheet,
component figures, crew stations, handling, and combat when the craft can fight
or be attacked. The craft is done when a DM can put it on the table without
another format guide.

Create or edit a named craft page when a ship, boat, or other vehicle has a
durable identity and players can use, approach, evade, protect, damage, crew,
alter, follow, or return to it. Use `kind: ship`, `kind: boat`, or
`kind: other`. Store the note under:

`wiki/<campaign>/vehicles/`

Do not create a durable vehicle note for a one-line ferry ride or prop. Keep
that in the owning beat, place, or session note until the craft has a name or
recurring consequence.

## Procedure

### 1. Retrieve The Craft

Read the brief, `wiki/templates/vehicle.md`, and relevant place, NPC, faction,
route, hazard, and prior vehicle notes. Preserve established names, aliases,
berths, conditions, owners, cargo, and uncertainties.

Write one identity sentence before the page:

> This is a [ship/boat/other] that [role], recognized by [silhouette or
> operational signature], and it gives players [choice or pressure].

If that sentence has no route, table action, or consequence, keep retrieving or
ask for the missing premise before drafting the page.

### 2. Start From The Template

Copy `wiki/templates/vehicle.md`. Keep its frontmatter and headings unless an
unused template section says it may be omitted. Fill these frontmatter fields:

```yaml
type: vehicle
lifecycle: proposed
reveal: unrevealed
campaign: <campaign slug>
visibility: dm
kind: ship # ship | boat | other
region: "<known region or blank>"
berth: "<home port / mooring / linked place, or blank>"
summary: "<one runnable sentence>"
```

The page body follows the template's jobs. Do not invent a second vehicle
template.

### 3. Fill The Playable Page

Fill `> [!narration] Narration` with the spoken look or a precise
theatre-of-the-mind handoff. It must give silhouette, scale, and body-scale
access from the supplied viewpoint in complete sentences. Keep secrets, DCs,
and unearned names out of player-facing prose.

Fill `## Sheet` so the craft can enter play:

- **Size.** Use a 5e size category or table-usable footprint.
- **Type.** State the craft class in ordinary language.
- **Speed.** Give the movement rate used in play, with mode when needed.
- **Crew (min).** Minimum crew required to operate it.
- **Passengers.** Safe passenger capacity.
- **Cargo.** Cargo capacity, or `none` for a craft that cannot carry cargo.

Fill `## Components` with AC and HP for each relevant component:

- **Hull.** AC, HP, damage threshold.
- **Helm.** AC, HP, and what control is lost when disabled.
- **Movement.** AC, HP, and what speed or maneuver is lost when disabled.
- **Weapons.** For armed craft only: each weapon's AC, HP, attack, range, hit
  effect, crew needed, and reload or use limit. Omit this row when unarmed.

Use official 5e vehicle columns as the numeric anchor: speed, crew, passengers,
cargo, AC, HP, and damage threshold. Reskin a close official craft when exact
canon is silent; mark material changes as invention.

Fill `## Crew stations` with named stations and current vs minimum complement.
A station is done when the DM knows who can operate it, what check or action it
supports, and what happens when it is empty.

Fill `## Handling` with conditions, maneuvers, limits, and environmental
pressures that change choices: wind, current, tight channels, reefs, repairs,
turning room, launch time, exposed approach, cover, noise, or route cost.

Fill `## Combat` when the craft can fight, ram, be boarded, be chased, or be
destroyed. State initiative, movement on its turn, ramming, boarding access,
component targeting, destruction, sinking/crashing, and crew exposure. Omit the
section only when the craft will not enter play as a fighting or attackable
craft.

### 4. Add Routes, Hooks, And Return State

Add only the extra material the page needs to run:

- Physical access: approach, rail, deck, hold, hatch, lines, tiller, rigging,
  cabin, engine space, launch, retreat, and bypasses.
- Connections: berth, routes, linked places, owners, passengers, cargo,
  factions, hazards, and other vehicles.
- Hooks and secrets: things players can do, discover, protect, alter, follow,
  or decide, with clues recorded as content plus access vector.
- Return state: berth, route exposure, crew status, damage, cargo, evidence,
  changed links, and the next safe handoff.

Keep links pointed at existing notes. Mark unresolved facts as seeds/stubs
instead of genre defaults.

## Done

The page is done when:

- It lives in `wiki/<campaign>/vehicles/` with `type: vehicle` and a valid
  `kind`.
- Narration, or an explicit TotM handoff, gives silhouette, scale, and
  body-scale access.
- `Size, type, speed, crew (min), passengers, cargo` are filled so the craft
  can enter play.
- Hull has AC, HP, and damage threshold.
- Helm, movement, and every weapon present have AC/HP and a play consequence
  when disabled.
- Crew stations, handling, and combat contain enough procedure for the DM to
  run travel, pursuit, boarding, damage, and destruction.
- Invention is labeled, cited, and proposed for DM acceptance.
