---
name: vehicle-design
description: >-
  Design named, playable vehicles for the campaign wiki, especially ships and
  boats. Use when a craft needs a persistent identity, travel role, ecology,
  topology, hooks, or a DM-ready vehicle note. Fill the Vehicle template and
  keep mechanics as play dials; hand player-facing [!narration] to
  theatre-of-the-mind / Visualizer. Do not use for generic transport,
  creature-only design, or invented vehicle CR/HP/speed tables.
---

# Vehicle design
## Work gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Reject leaves no page. Ground invention in wiki pages and/or D&D 5e rules; set `invention: true`, cite `[[pages]]`, and show the DM contradictions. Never present invention as wiki fact or write silent canon. Players see nothing until DM acceptance.

Output durable pages under `wiki/`; templates live in `wiki/templates/`. Point at `docs/agents/work.md`; keep the craft procedure.

---


A vehicle is a **recognizable craft + operational signature + usable access +
travel/ecology role + choices under pressure**. Design the craft as something
players can point to, approach, use, evade, protect, alter, or return to. Keep
DM truth and player-facing prose separate. This skill owns the vehicle note and
its playable structure; `theatre-of-the-mind` owns prose that crosses the
DM/player boundary.

## When to create a named craft note

Create a note when a ship, boat, or other craft has a name or durable identity
and at least one of these is true:

- it recurs as a travel anchor, berth, route, refuge, threat, or destination;
- players can make meaningful choices aboard it, from it, or because of it;
- its crew, owner, cargo, wake, route, or condition can change between visits;
- it carries clues, factions, NPCs, hazards, or consequences worth linking;
- its silhouette and operational behavior distinguish it from ordinary
  transportation.

Ships and boats are the first-class use case. Use `kind: ship` for a ship,
`kind: boat` for a boat, and `kind: other` for another persistent craft. Do not
create a named note for every cart, ferry ride, or one-line conveyance. If the
craft is only a scene prop, keep it in the owning place or session note until
it earns a durable identity.

Store the note under the Organizer-owned folder:

`wiki/<campaign>/vehicles/`

Link the note from the campaign vehicle MOC when one exists. Do not treat a
vehicle as a `location`, and do not migrate or rewrite existing craft notes
merely to apply this skill. Existing notes such as Saltwright and Red Lady /
Dead Lady are layout examples only.

## Procedure

### 1. Retrieve before inventing

Read the brief, relevant campaign notes, the Vehicle template, and linked place,
NPC, faction, hazard, and route notes. Preserve established names, aliases,
berths, conditions, and uncertainties. Mark an unresolved detail as a seed or
stub instead of filling it with genre default. Read Saltwright or Red Lady /
Dead Lady briefly only to understand the existing layout; do not rewrite their
narration or migrate more notes.

Write a one-sentence identity before expanding the page:

> This is a [ship/boat/other] that [travels/serves/blocks/carries] [role], is
> recognized by [silhouette or operational signature], and gives players
> [choice or pressure].

If that sentence does not imply a route, action, or consequence, the craft is
not ready for a named note.

### 2. Create the note from the exact template

Start from `templates/Vehicle.md`. Keep its frontmatter fields and section
names. Fill known values; leave genuinely unknown values blank or marked as a
DM seed rather than inventing them.

Use this frontmatter shape:

```yaml
---
type: vehicle
campaign: <campaign slug>
kind: ship # ship | boat | other
region: <known region or blank>
berth: <home port / mooring / linked place, or blank>
visibility: dm
tags: [vehicle]
---
```

`kind` must be exactly one of `ship`, `boat`, or `other`. `berth` is optional,
but fill it when the craft has a home port, mooring, linked place, or reliable
point of departure. Add no alternate type such as `location`.

Fill the body in the template's order and with its intent:

- `# {{name}}`: use the established craft name, including an established
  alias when needed.
- `[!narration] Narration`: leave empty for Visualizer, or provide a narrow
  handoff brief outside player prose. Do not independently author the final
  read-aloud block here.
- `## At a Glance`: one sentence naming the class of craft and its immediate
  playable identity, followed by a supported “feels like…” mood. Do not turn
  this into a history paragraph.
- `## Aspects`: exactly three playable traits in Lazy DM style. Make each one
  actionable or pressure-bearing, not a decorative adjective list.
- `## Vehicle surface / topology`: describe what the table can point to and
  how those parts relate. Name physical access such as rail, deck, hold, hatch,
  lines, tiller, rigging, cabin, or engine space only when supported. State
  what moves with the craft and what stays fixed relative to the deck. Give
  nodes and edges, including a route, a bypass when fiction permits, and a
  retreat or safe return. Use physical language, never interface jargon.
- `## Who is here`: link known NPCs, factions, crew, passengers, or a stated
  crew pattern. Distinguish current presence from a future or unresolved seed.
- `## Connections`: link berth, routes, linked places, and other vehicles.
  Record the travel relationship and its cost or exposure when that changes a
  choice.
- `## Hooks`: list things players can do, discover, protect, alter, follow, or
  decide aboard or from the craft. Prefer verbs and consequences over plot
  promises.
- `## Secrets (DM)`: record clues available here as their content and access
  vector, not only “roll Investigation.” Keep hidden cause, ownership, and
  unresolved canon private when appropriate.
- `## Mechanics`: include only play dials: cover, movement, routes, hazards,
  Search/Study/Influence/Utilize, exposure, supplies, crew pressure, or links
  to encounters and monsters. Do not invent CR, HP, speed, action, or vehicle
  stat tables. `Homebrewer` owns later numeric vehicle mechanics.
- `## Do not`: retain the template guardrails. In particular, keep the note in
  `wiki/<campaign>/vehicles/`, ban “boarding interface” in narration, do
  not dump a full keyed deck map unless play needs short subsections, and do
  not invent CR/HP/speed tables without Homebrewer.

Do not add a location kernel, monster stat block, or a full keyed map merely to
make the page look complete. The template's sections are the deliverable.

### 3. Design ecology and travel role

Give the craft a role in the living travel network, not just a destination.
Answer the smallest useful set of questions:

- What waters, roads, skies, routes, weather, traffic, or hazards does it use?
- Who uses, services, watches, avoids, hunts, taxes, shelters, or follows it?
- What does its movement change for nearby places, factions, and other craft?
- What visible trace identifies its operation: wake, smoke, bell, sail, rigging,
  cargo pattern, route mark, silence, smell, or repeated timing?
- What happens when it is delayed, damaged, diverted, exposed, abandoned, or
  returned?

Use ecology as playable context: traffic patterns, berth relationships,
seasonal or environmental pressure, crew routines, and consequences of route
choice. Do not assert a complete maritime economy or hidden crew roster when
the vault is silent. Link to a place, faction, NPC, hazard, or route instead of
repeating that note's lore.

### 4. Build topology without ship math

Represent the craft and its approach as compact physical edges, for example:

`approach lane -- exposed approach --> wake / rail`

`rail -- line or ladder --> deck`

`deck -- hatch --> hold`

`deck -- turn / cover --> tiller or rigging`

Each edge should say what it costs or changes: exposure, evidence, cover,
position, time, separation, noise, or a route opportunity. Include, where the
fiction supports it:

- a primary approach and a less obvious or costly approach;
- one loop or return route through the craft;
- one bypass that gives up information, access, or leverage;
- one retreat, launch, cast-off, or safe return;
- a relation to water, current, weather, traffic, terrain, or a moving hazard.

Topology is not a keyed deck plan. Short subsections are enough when a specific
choice needs them. Never use topology to smuggle in numeric ship statistics.
Describe what characters can do and observe; hand CR, HP, speed, resistance,
vehicle actions, and balance to `homebrew-monsters-5e` only for creatures and to
`Homebrewer` for vehicle mechanics.

### 5. Use the vehicle TotM bar path

When the note needs a player-facing first look, choose one existing accepted
TotM bar sample before drafting. The choice is a quality bar, not a prose
pattern: a place sample such as Clear Lake can test drawable body-scale access,
and a hazard sample such as Razer-Grass can test a concrete operational danger.
For a vehicle, route to the existing **Vehicle** surface in
`.agent/skills/theatre-of-the-mind/references/surfaces.md` and the vehicle rules
in `.agent/skills/theatre-of-the-mind/SKILL.md`. Do not invent a new TotM skill,
vehicle renderer, or boarding workflow.

Audit the vehicle spine through four gates:

1. **Silhouette:** the whole craft, its scale, and its distinguishing shape are
   drawable from the supplied viewpoint.
2. **Kitchen-table access:** at least one supported physical relation is clear,
   such as a line to the rail, a hatch into the hold, a deck underfoot, a
   tiller, or a visible route around the hull. Use plain nouns players can
   point at.
3. **Operational signature:** one supported motion, sound, wake, working part,
   traffic effect, or stable behavior shows how this craft operates.
4. **Stop:** stop at the supported access point, operating problem, arrival, or
   player opening. Do not resolve the boarding, search, escape, or consequence
   in the first look.

The player-facing bar must never say **“boarding interface.”** Use `line`,
`rail`, `deck`, `hold`, `hatch`, `tiller`, `rigging`, `cabin`, `wake`, or another
established physical noun. “Boarding interface” is banned from `[!narration]`
and player-facing prose even when the DM note discusses access.

Hand the `[!narration]` block to **Visualizer/WE** with the note path, viewpoint,
supported facts, and the four-gate constraints. Visualizer/WE must use the
existing TotM vehicle surface; do not duplicate or fork TotM guidance inside a
vehicle note. Keep private topology, secrets, mechanics, and unsupported
absence outside the player-facing block.

### 6. Add pressure and return state

Give the craft a small state change that matters between visits: for example,
recognized → watched → compromised, or sound → delayed → damaged. For each
move, state trigger, visible result, player opportunity, and lasting
consequence. Keep it interruptible; the craft does not run a cutscene.

Record a return state when useful: berth, route exposure, crew status, physical
evidence, damage, cargo, changed links, or the next safe handoff. Failure
should change position, time, trust, safety, resources, or route access, not
silently erase a required clue.

## Review checklist

Before handing off or shipping the note, verify:

- The note is named, recurring or consequential, and in
  `wiki/<campaign>/vehicles/`.
- Frontmatter has `type: vehicle`, a valid `kind`, and `berth` when known.
- Every template heading is present and filled only with supported, useful
  information.
- The craft has three playable Aspects, a travel/ecology role, and a physical
  topology with access, bypass, retreat, and consequences where supported.
- Mechanics are play dials only. No invented CR/HP/speed/action tables appear.
- `[!narration]` is empty or explicitly handed to Visualizer/WE.
- The TotM Vehicle surface is referenced, not duplicated; the four bar gates
  pass; “boarding interface” does not appear in player prose.
- Unknowns are labeled as seeds/stubs, links point to existing notes, and the
  page does not become a location, monster, or full deck-map rewrite.
