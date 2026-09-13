# Contract: Wiki kind pages

The interface is a campaign wiki page job. Co-DM is the author. Naming the wrong primary skill is a fail. A page that cannot be run at the table is a fail. Pass is jobs, not heading-order match. Omit unused sections.

## Routing table

| Job | Primary skill |
|---|---|
| Write, edit, or create a named vehicle page | `vehicle-design` |
| Write, edit, or create a named spell page | `spell-design` |
| Write, edit, or create a named faction page | `faction-design` |
| Write, edit, or create a named lore page | `lore-design` |
| Write, edit, or create a named quest page | `narrative-islands` |
| Write, edit, or create a named city page | `city-design` |
| Write, edit, or create a named region page | `region-design` |
| Write, edit, or create a site place | `place-design` |

`place-design` is the hub for all places. It defers to `city-design` for `kind: city` and to `region-design` for region jobs. It writes site places from `wiki/templates/place.md`.

A beat that needs a named craft, spell, faction, lore note, quest, city, or region hands off to that owner. The beat skill stays primary for the beat.

`faction-prep` is removed. Jobs that would have loaded it load `faction-design`.

## Classification jobs

| # | Job | Primary |
|---|---|---|
| 21 | Write a named ship or other vehicle | `vehicle-design` |
| 22 | Edit an existing vehicle page | `vehicle-design` |
| 23 | Write or edit a spell page | `spell-design` |
| 24 | Write or edit a faction page | `faction-design` |
| 25 | Write or edit a lore page | `lore-design` |
| 26 | Write or edit a quest page | `narrative-islands` |
| 27 | Write or edit a city page | `city-design` |
| 28 | Write or edit a region page | `region-design` |
| 29 | Write a site place (not a city or region) | `place-design` |
| 30 | Start at `place-design` for a city | defers to `city-design` |
| 31 | Start at `place-design` for a region | defers to `region-design` |

## Page rules

1. Start from the matching `wiki/templates/` scaffold provided for this feature.
2. `wiki/AGENTS.md` lists `type` values and Layout jobs. Pass is those jobs.
3. Theatre of the mind owns `[!narration]`.
4. Skills that teach these pages state what to write and when the page is done.
5. Existing pages are not rewritten solely to prove a new template.

### Vehicle — `wiki/templates/vehicle.md`

Spoken look; filled 5e sheet (size, type, speed, crew); hull/component figures. Armed craft include weapons. Handling and combat when the craft enters play.

### Spell — `wiki/templates/spell.md`

Spoken look; classification; runnable 2024 effect block. Discovery/Lore headings on a spell page are spell-owned, not `type: lore`.

### Faction — `wiki/templates/faction.md`

Public face; DM thesis; current state; one active agenda; table-relevant assets, people, places, and relationships; faction-turn log. `faction-design` writes Current Turn with no roll. `world-tick` runs the turn and appends the log. Agenda clock lives on the faction page. `hot.md` may point; it must not store a second clock.

### Lore — `wiki/templates/lore.md`

One durable question per note. At a Glance (core truth + why it matters); Current Truth; At the Table (notice / explains / enables / warns). Not `canon` until players interact or witness. Until then the DM may change it freely and Canon Log is omitted. After that, `session-wrapup` or `reconciling-session-evidence` updates Current Truth and appends the Canon Log. Ingest MUST NOT map `lore` to `item`. Actual items stay `item`.

### Quest — `wiki/templates/quest.md`

Summary (objective, why now, deadline); Situation; Stakes including walk-away; World in motion (driver and next move if uninterrupted); at least two independent leads. No required sequence of party actions. Resolution omitted while unresolved. `narrative-islands` owns later updates including rolls and the Quest log. `world-tick` does not advance quest portents. `type: front` and `type: encounter` are retired; those situations are quests. Encounter-prep still owns fight math.

### City — `wiki/templates/city.md`

`type: place`, `kind: city`. Arrival; At a glance including current pressure; Orientation (districts and getting around); Gazetteer enough to seek a place; rules that matter at the table; at least one active situation with if-nobody-intervenes. Faction full agendas stay on faction pages. A pursuable situation is a linked quest. Change log stays on the city page under `city-design`.

### Region — `wiki/templates/region.md`

`type: region`. Spoken look; At a glance; Current state; geography/travel enough to choose a route; active powers; change log. Scale (macro / regional / local) omits extra headings. MUST NOT invent pressure. If a pressure is already stated, link that wiki note. Do not revive `type: front`.

## Claude Code skill updates

Claude Code only for novel `faction-design`, `lore-design`, `city-design`, `region-design`, and a `narrative-islands` redesign (quest template; stop minting front/encounter). Dispatch: `claude -p --model claude-opus-4-6 --effort medium`. Prompt is minimal; names deliverables and a completion test.

Session-agent work: templates; `wiki/AGENTS.md` type enum and Layout; `AGENTS.md` routing rows; delete `faction-prep` and retarget callers; `place-design` hub defer pointers; `world-tick` faction-turn log; wrapup/reconcile Canon Log pointers; `vehicle-design` sheet fill if not already done.

Usage limit: defer the Claude job on `tasks.md`; complete independent tasks. Codex CLI at ChatGPT 5.5 medium MAY take the same prompt only when every remaining open task is blocked, no other work can be done, and the retry time is more than one hour away. Re-check those gates before each remaining blocked job.

## Out of contract

Foundry staging. How the designated writer phrases a skill. Beat Chart assembly (see [beat-skill-routing.md](./beat-skill-routing.md)).
