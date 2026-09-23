---
name: vehicle-design
description: >-
  Design named, playable vehicle pages for the campaign wiki, especially ships
  and boats. Use when a craft needs a persistent identity, travel role, crew,
  components, handling, combat, or a DM-ready vehicle note. Fill
  wiki/templates/vehicle.md, including the sheet and component figures.
---

# Vehicle Design
## Boundary contract

### Input

Take a named vehicle owner, the caller's objective, the relevant brief,
`wiki/templates/vehicle.md`, and linked canon/evidence for its route, berth,
owner, crew, components, and prior state. The owner is the craft's durable
identity, not a one-off travel description.

### Owner-specific Work

Work only the named craft: preserve its class and canon, write the
identity-first silhouette, and fill Sheet, Components, Crew stations, Handling,
and needed Combat fields. Keep Unknowns explicit, mark invention, and leave
crew or PC decisions as playable pressure rather than authored outcomes.

### Capability Handoff

Berth → `place-design`. Crew member → `npc-design`. Owner →
`faction-design`. Spoken look → `theatre-of-the-mind`.

### Done

Use the existing `## Done` checklist below. Completion is observable when the
named vehicle page path, vehicle-template and runnable-sheet checks, playable
handling/combat decision, and any child return evidence are reported.


Prep only. Follow `docs/agents/work.md`.

## Refuse gates

- **Work gate.** Show a chat proposal before writing under `wiki/`. Write only
  after DM acceptance. Workspace outputs allowed before acceptance. A missing
  named craft is work to propose now — not out of scope.
- **Invention.** Never present invention as wiki fact. Set `invention: true` (or
  mark proposed), cite `[[pages]]`, show contradictions, propose for acceptance.
  No silent canon — including invented weapons, sheet numbers, upgrades, merges,
  or undeclared conspiracies on existing craft.
- **Unknowns stay Unknown.** Blank sheet/component lines stay Unknown or fill
  only as labeled invention after the work gate — never unmarked established
  fact.
- **Template lock.** Copy `wiki/templates/vehicle.md` only. Fill narration,
  Sheet, Components, Crew stations, Handling (and Combat when needed) with
  substance — not empty headings.
- **Narration.** `> [!narration] Narration` is spoken look: silhouette, scale,
  body-scale access. No secrets, DCs, or unearned names in player-facing prose.
- **Identity first.** Before the page draft:

  > This is a [ship/boat/other] that [role], recognized by [silhouette or
  > operational signature], and it gives players [choice or pressure].

  If that lacks route, table action, or consequence, keep retrieving or ask.
- **No one-line ferry.** Refuse a durable vehicle note for a one-line ferry ride
  or prop. Keep it in the owning beat, place, or session note until the craft
  has a name or recurring consequence.
- **No overwrite.** Do not rewrite established chassis, crew, berth, role, or
  cover as a different craft class (flying dreadnought, etc.) and present that
  as wiki fact. Speculative upgrades are proposed/invention only.
- **No PC authorship.** Do not author PC orders, flight decisions, or feelings
  as completed facts. Present pressures and options; leave choices to play.
- **No silent merge/delete.** Refuse collapsing or deleting vehicle pages
  without a chat proposal, contradiction surfacing, and DM acceptance.

## Vehicle job

A named vehicle page is runnable look + filled sheet + components + crew
stations + handling (+ combat when attackable). Use when the craft has durable
identity players can use, approach, evade, protect, damage, crew, alter, follow,
or return to. Use `kind: ship`, `kind: boat`, or `kind: other`. Store under
`wiki/<campaign>/vehicles/`. Keep one-off ferry color on the owning beat until
named or recurring.

## Build the craft

1. **Retrieve.** Brief, `wiki/templates/vehicle.md`, and relevant place/NPC/
   faction/route/hazard/prior-vehicle notes. Preserve established names,
   aliases, berths, conditions, owners, cargo, and uncertainties.
2. **Identity sentence** before drafting (see refuse gate).
3. **Scaffold.** Copy `wiki/templates/vehicle.md`. Frontmatter: `type: vehicle`,
   lifecycle/reveal/campaign/visibility, `kind`, region/berth when known,
   `summary`.
4. **Runnable fill.** Narration (silhouette/scale/access); Sheet (Size, Type,
   Speed, Crew min, Passengers, Cargo — numeric or Unknown); Components (Hull
   AC/HP/DT; Helm and Movement AC/HP + disabled consequence; Weapons only when
   armed); Crew stations; Handling; Combat when the craft fights/is attackable
   (else omit with reason).
5. **Routes / hooks / return only when needed.** Access, connections, secrets
   with clue+vector, return state. Link existing notes; mark stubs instead of
   genre defaults.

Ground invention in wiki pages and/or D&D 5e vehicle rules; reskin a close
official craft when exact canon is silent; mark material changes as invention.

Read `references/vehicle-craft.md` for craft basis, section fill detail, audit
questions, and failure modes.

## Handoffs

Narration → `theatre-of-the-mind`; places/berths → `place-design`; crews/NPCs →
`npc-design`; factions/owners → `faction-design`; vault lookup →
`.agents/skills/qmd`.

## Done

- Fills `wiki/templates/vehicle.md` under `wiki/<campaign>/vehicles/` with
  `type: vehicle` and valid `kind`; no second template.
- Identity sentence before draft; narration perceivable-only.
- Sheet/Components minima filled (or Unknown); crew stations and handling
  runnable; combat present or omit-reason stated.
- Invention labeled/cited/proposed; Unknowns not silent canon; wiki write only
  after accept.
- DM can put the craft on the table tonight without a format guide.
