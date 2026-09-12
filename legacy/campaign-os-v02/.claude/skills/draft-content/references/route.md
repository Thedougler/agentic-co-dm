
# Draft — Route

The leg between two or more places, not the places themselves — a road, a
sea lane, a rail line, an underground passage, a jump lane, any journey a
party actually takes to get from one point to another. Done means the DM
can run the crossing — its duration, its traffic, its hazards — from the
page alone.

Routes live in `vault/campaigns/*/locations/`, the same folder as the
places they connect: a route is filed among locations because it is
travelled the same way a location is visited, not because it is one.

## Template

`vault/_templates/_campaigns/_route.md` — copy it. Headings fixed and in
order: `## Path · ## Waypoints` (OPTIONAL — delete outright if no real
stop exists yet) `· ## Travel · ## Hazards`.

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — PC agency, NPC independence.
3. `vault/refs/vault/_common/hard-rules.md` — shared rules; bind this type, never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now, paste the output.

`DR1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **The Leg-vs-Place Boundary.** `.claude/skills/draft-content/references/location.md`
  (`vault/_templates/_campaigns/_location/_location.md` and its
  `vault/_templates/_campaigns/_location/_location_region.md` fork) owns a place the
  party arrives at and stands in — a settlement, a region, a building, a
  dungeon. A `route` owns the leg between those places: its hazards, its
  duration, its traffic, what can happen on the way. A page that
  describes somewhere the party stops and stays is `location`; a page
  that describes the crossing itself is `route`. Both are filed in the
  same `vault/campaigns/*/locations/` folder — the boundary is the
  content's shape, not its address.
- **No Route Without Two Ends.** `endpoints:` names at least two real
  `type: location` pages this leg actually connects — never a single
  endpoint, never an invented placeholder. A leg with only one known end
  isn't ready to ship; ask which page it terminates at.
- **Setting-Agnostic By Default.** `travel_modes:`, `distance:`, and
  `travel_time:` never assume a specific mode, scale, or unit — a route
  can be a road, a sea lane, an underground passage, or a jump lane, and
  its distance can be miles, hexes, watches, or parsecs. Fill them with
  whatever this campaign's setting actually uses; never default to a
  D&D-mechanical unit or terrain category that doesn't apply here.
- **The Encounter-Table Boundary.** `.claude/skills/draft-content/references/table.md` owns random
  encounter tables. `encounter_table:` holds the `[[wikilink]]` to the
  leg's `type: table` page when one exists, and `## Travel`/`## Hazards`
  link to it the same way — never restate its rows here. A route with no
  table yet deletes `encounter_table:` outright and still describes its
  hazards in prose; it doesn't invent a table inline to avoid the link.
- **Waypoints Resolve Or Spawn.** A named stop along the way is a
  wikilink or a spawned pending stub, never plain text — same discipline
  as a location's Notable NPCs
  (`vault/refs/vault/location/references/npcs.md`).
- **Share Situations.** `situations:` wikilinks the Situations that can
  surface on this leg. The same Situation may appear on more than one
  Route. Link the page; never copy it.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- The two (or more) endpoints — real `type: location` pages? Missing one
  -> stop, that page needs to exist first (the Leg-vs-Place Boundary).
- What mode(s) of travel use this leg (`travel_modes:`)? Never assume
  "ship" or "road" by default — ask.
- `distance:`/`travel_time:` in whatever unit this campaign actually
  uses — miles, hexes, watches, jumps. What changes it (weather, season,
  current, patrol schedule)?
- `traffic:` and `hazard_level:` right now? Template defaults are both
  `moderate`; correct if wrong.
- Does an encounter table already exist for this leg (the
  Encounter-Table Boundary)? Yes -> fill `encounter_table:` with its
  `[[wikilink]]`. None yet -> delete `encounter_table:` outright rather
  than inventing rows inline.

## How this relates to travel-events

This page is the **standing fact**: the route's duration, traffic, and
hazards as they exist whether or not the party is currently crossing it —
the same kind of durable record a `location` or `faction` page is.
`.claude/skills/travel-events/SKILL.md` is the **per-journey
prep**: it designs what actually happens on one specific crossing (event
count, type, the toy in the road) for a leg already in play. When a route
page already exists, travel-events reads it as the leg's baseline —
`travel_time:`, `traffic:`, `hazard_level:`, and `## Hazards` — never
re-inventing them. When a leg recurs, travel-events flags the gap and
hands the hazards, waypoints, and durations it surfaced to this guide,
which authors the `route` page (`.claude/skills/travel-events/references/route-escalation.md` §2);
travel-events never writes one itself, and never escalates to a `type:
location` page.

## Before you ship

- [[vault/refs/vault/_common/lifecycle|Lifecycle]]: `vault/refs/vault/_common/lifecycle.md`
- Gaps: `vault/refs/vault/_common/degrade.md`
- [[vault/refs/vault/_common/handoffs|Handoffs]]: `vault/refs/vault/_common/handoffs.md`
- Boundaries: `vault/refs/vault/_common/out-of-scope.md`
- Common checklist: `vault/refs/vault/_common/checklist.md`
- Route checklist: `vault/refs/vault/route/references/checklist.md`

## Reference files

| File | Read when |
|---|---|
| `.claude/skills/draft-content/references/location.md` | Confirming the Leg-vs-Place Boundary, or the endpoint page doesn't exist yet |
| `.claude/skills/draft-content/references/table.md` | This leg needs its own random encounter table |
| `.claude/skills/travel-events/SKILL.md` | Prepping one specific crossing of this route for play |
| `vault/refs/vault/route/references/checklist.md` | Route-only checklist additions |
