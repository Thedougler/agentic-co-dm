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

## Work Gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal before writing a campaign wiki page. Write under `wiki/`
only after DM acceptance. If a needed named city is missing, that city page is
work to do now: propose it instead of treating the missing note as out of
scope. Ground invention in wiki pages and/or D&D urban-play patterns; set
`invention: true`, cite `[[pages]]`, and show contradictions. Never present
invention as wiki fact or write silent canon.

## City Job

A city page makes a named city runnable: how the party arrives, how the DM
orients them, where deliberate travel can take them, which local rules change
choices, what pressure is active now, and what changes if nobody intervenes.

Create or edit a named city page when the place has districts, public authority,
services, factions, routes, laws, or ongoing urban pressure broad enough that a
site-place page cannot hold it cleanly. Store the note under the campaign wiki
folder that owns cities and places.

`place-design` is the hub for places. It defers `kind: city` page work to this
skill. This skill writes the city page.

## Procedure

### 1. Retrieve The City

Read the brief, `wiki/templates/city.md`, and relevant region, route, district,
landmark, faction, NPC, quest, lore, session, and prior city notes. Preserve
established names, aliases, ruler, controlling faction, public laws, districts,
routes, landmarks, services, pressure, rumors, party history, and open
questions.

Write one identity sentence before the page:

> This is a [kind/scope] city known for [public identity], pressured by [current
> instability], and it gives players [choice or opportunity].

If that sentence has no current pressure or player opening, keep retrieving or
ask for the missing premise before drafting the page.

### 2. Start From The Template

Copy `wiki/templates/city.md`. Keep its frontmatter and headings unless an
unused template section says it may be omitted. Fill these frontmatter fields:

```yaml
type: place
lifecycle: proposed
reveal: unrevealed
campaign: <campaign slug>
visibility: dm
kind: city
region: "<known region or blank>"
status: active
population: "<scale or useful approximation>"
government: "<public form of rule or blank>"
ruler: "<linked ruler or blank>"
controlling_faction: "<linked faction or blank>"
summary: "<one runnable sentence>"
```

Do not add a second city template. Do not change the page to `type: region`,
`type: faction`, `type: lore`, or `type: quest`.

### 3. Fill The Runnable City

Fill `> [!narration] Arrival` through theatre of the mind. It says what the
party can perceive when entering or overlooking the city: scale, silhouette,
motion, sound, smell, and one unmistakable landmark. Keep secrets, hidden
history, and unearned names out of player-facing prose.

Fill `## At a glance` with character, known-for, visible power, current
pressure, opportunity, and population. The pressure is what makes the city
unstable right now. Fill the DM thesis with one sentence about the city's
function in play.

Fill `## Orientation` so the DM can answer where the party goes next:

- Districts residents actually recognize, each with a street-level read, known
  draw, and current pressure.
- Landmarks that help orientation.
- Getting around: cross-city travel, after-dark changes, restricted movement,
  and useful shortcuts.

Fill `# Gazetteer` so players can intentionally seek a place without the DM
inventing the basic city interface at the table. Include arrive/leave, stay,
buy/sell/commission, and services when they matter. Link durable places, NPCs,
districts, and routes; leave incidental entries unlinked until play makes them
durable.

Fill `## Rules that matter at the table` with only local realities that can
change a choice: law, weapons, magic, violence, status, commerce, rest, death,
or other city-specific constraints. Omit generic laws no one will act on.

Fill `# Power` with city-local posture only. Faction histories, full agendas,
and clocks stay on faction pages. The city page records each faction's public
position, local objective, leverage, and current move in this city now.

### 4. Write Active Situations And Motion

Create at least one `# Active situations` entry. A situation is active when a
named actor wants a concrete change, visible signs can surface it, opposition
exists, and the city changes if the party never interferes.

Each active situation includes:

- involved factions, NPCs, districts, or places;
- visible signs the party can encounter before investigation;
- what the active side wants;
- what opposes them;
- **If nobody intervenes:** the next meaningful change;
- trigger or date when timing matters.

If a situation is pursuable as an objective, link a quest page. If the quest page
is missing, propose that quest page; do not bury a full quest in the city note.

Use exploration layers, hidden nodes, rumors, secrets, street encounters, routes,
dependencies, pressure clocks, upcoming events, and local faction moves only
when they help run current play. Omit unused sections.

### 5. Maintain Current State And Change Log

Use `# Current state` for the handful of deltas the DM must remember now:
campaign date, last party visit, visible changes, headlines, pressure clocks,
upcoming events, and local faction moves.

Keep the city change log on the city page under this skill. Record deltas
instead of rewriting the whole city after every visit. When a delta becomes the
new normal, fold it into the relevant baseline section and archive the old
delta in `# Change log`.

## Craft Basis

Use city prep as a table interface, not an encyclopedia: arrival image,
recognized districts, deliberate-travel gazetteer, meaningful local rules,
visible pressure, and changed-state logs. Practical inputs: Justin Alexander's
urbancrawl layers and situation-based prep, Mike Shea's monuments and secrets
for city play, Kevin Crawford's sandbox faction pressure, progress clocks from
Blades in the Dark, and campaign-status practice that tracks current deltas
instead of rewriting the whole setting.

## Done

The page is done when:

- It fills `wiki/templates/city.md` without adding another template.
- It has `type: place` and `kind: city`.
- Arrival is `[!narration]` and contains only immediately perceivable city
  experience.
- At a glance includes current pressure and opportunity.
- Orientation includes districts and getting around.
- The gazetteer lets the party intentionally seek at least one relevant place,
  route, service, or source without blind exploration.
- Rules that matter at the table name local realities that can change a player
  choice.
- At least one active situation names actors, visible signs, want, opposition,
  and if-nobody-intervenes.
- Every pursuable situation links a quest page or proposes the missing quest.
- Faction full agendas and clocks stay on faction pages.
- Current state records only live deltas the DM must remember now.
- Change log stays on the city page and records deltas.
- The DM can arrive, find a district, seek a place, name a local rule, and say
  what happens if nobody intervenes.
- Invention is labeled, cited, and proposed for DM acceptance.
