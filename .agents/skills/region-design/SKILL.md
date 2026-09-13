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

## Work Gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal before writing a campaign wiki page. Write under `wiki/`
only after DM acceptance. If a needed named region is missing, that region page
is work to do now: propose it instead of treating the missing note as out of
scope. Ground invention in wiki pages and/or D&D region-play patterns; set
`invention: true`, cite `[[pages]]`, and show contradictions. Never present
invention as wiki fact or write silent canon.

## Region Job

A region page makes an area runnable for travel and off-screen motion: what the
party perceives on first travel, what kind of area it is, how routes differ,
which powers can change it, and what changed since the last stable state.

Create or edit a named region page when the area has enough identity, travel
structure, active powers, landmarks, routes, or nested places that a site-place
page cannot hold it cleanly. Store the note under the campaign wiki folder that
owns regions and places.

`place-design` is the hub for places. It defers region page work to this skill.
This skill writes the region page.

## Procedure

### 1. Retrieve The Region

Read the brief, `wiki/templates/region.md`, and relevant parent region,
subregion, city, place, route, faction, NPC, quest, lore, session, and prior
region notes. Preserve established names, aliases, scale, kind, boundaries,
routes, anchors, landmarks, powers, active pressure, party history, current
state, and open questions.

Write one identity sentence before the page:

> This is a [scale/kind] region known for [public identity], crossed by [route
> choices], and changeable by [active powers].

If the sentence cannot name route choices or who can change the region, keep
retrieving or ask for the missing premise before drafting the page. Do not invent
pressure to make the sentence more dramatic.

### 2. Start From The Template

Copy `wiki/templates/region.md`. Keep its frontmatter and headings unless an
unused template section says it may be omitted. Fill these frontmatter fields:

```yaml
type: region
lifecycle: proposed
reveal: unrevealed
campaign: <campaign slug>
visibility: dm
region: "<parent region or blank>"
scale: <macro|regional|local>
kind: <realm|province|frontier|wilderness|forest|mountains|archipelago|sea|valley|district>
structure: "<hexcrawl|pointcrawl|routes|abstract or blank>"
as_of: "<in-world date or blank>"
summary: "<one runnable sentence>"
```

Do not add a second region template. Do not change the page to `type: place`,
`type: quest`, `type: faction`, `type: lore`, or the retired `type: front`.

### 3. Fill The Runnable Region

Fill `> [!narration] Narration` through theatre of the mind. It says what a
traveler first experiences: horizon, terrain, weather, movement, sound, and one
unmistakable feature. Keep secrets, DCs, hidden history, and unearned names out
of player-facing prose.

Fill `## At a glance` with scale, kind, character, anchor, known-for,
feared-for, and parent region. The DM thesis states what the region is for at
the table: route choices, pressures already established elsewhere, or the kind
of exploration it enables.

Fill `## Current state` with the status quo now. Use pressure only when a source
already states it; link that pressure's owner note. If no pressure is already
stated, write `Pressure: None established yet` or omit the bullet when the
template section can stay clear without it. A pressure-free region still passes
when geography, travel, active powers, and change log are runnable.

Fill geography and travel so the DM can answer "which way do you go?":

- shape, boundaries, and what changes across edges;
- subregions only when they create real choices or identity;
- landmarks that help navigation or decisions;
- travel structure, route scale, navigation, weather, rest, supply, and any
  regional rule that changes choices;
- routes with different time, cost, risk, advantage, or discovery state;
- hidden or broken connections only when discovery changes the map.

Fill `## Key places` with table-ready places only. Link durable places; keep
temporary events in Current state, Fronts and pressures, or Change log.

Fill `## Active powers` with the few groups that can change the region now.
Record hold or presence, want now, next move, and what reveals that move. Full
faction agendas, clocks, and histories stay on faction pages.

### 4. Handle Pressure Without Creating It

Use `## Fronts and pressures` only for pressures already stated by a wiki note,
session note, or accepted brief. Link the owner note in the heading or first
line. Summarize only what matters regionally: impulse or goal, impending
consequence, affected places/routes/powers, visible signals, and portents if
they already exist or are accepted as invention.

When no pressure is already stated, omit `## Fronts and pressures` or leave a
short "None established yet" note if the DM needs that explicit absence. Do not
create a front, threat, plague, war, clock, villain plan, or crisis just because
the template has a pressure section.

If the pressure is pursuable as an objective, link a quest page or propose the
missing quest page. Do not revive `type: front`; those jobs belong to quests.

### 5. Omit By Scale

Keep only headings that help run the named region at its scale:

- **MACRO:** keep Current state, Geography, Subregions, major Routes, Active
  powers, linked pressures when they exist, Stakes, and Change log. Usually omit
  encounter ecology, individual minor sites, and detailed finds.
- **REGIONAL:** default use. Keep most sections when they create choices,
  signals, routes, powers, or table prep.
- **LOCAL:** focus on routes, key places, immediate powers, rumors, encounters,
  and discoveries. Omit Subregions when they add no useful choice.

Persistent geography belongs in Geography, Travel, Key places, and Regional
truths. Ephemeral events belong in Current state, linked pressure notes, or
Change log. Promote a detailed site to its own `[[place]]` note when it no
longer fits comfortably here.

### 6. Maintain Current State And Change Log

Use `## Current state` for what the DM should assume now: status quo, recent
change, opportunity, next visible change, and linked pressure when one exists.
Keep it short and current.

Use `## Change log` for deltas. Record in-world date when available, change,
cause, and affected pages. When a delta becomes the new normal, fold it into the
baseline section and leave the old event in Change log.

## Craft Basis

Use region prep as a route-and-motion interface, not an encyclopedia: persistent
keyed geography, meaningful routes, active powers, visible signals, and current
deltas. Practical inputs: Justin Alexander's hexcrawl documents and campaign
status practice, pointcrawl route thinking, Mike Shea's landmarks, secrets, and
clues, Kevin Crawford's sandbox faction pressure, and Dungeon World's fronts for
goal, portent, and consequence structure when a pressure already exists.

## Done

The page is done when:

- It fills `wiki/templates/region.md` without adding another template.
- It has `type: region`.
- Narration is `[!narration]` and gives a spoken first-travel look with only
  immediately perceivable region experience.
- At a glance states scale, kind, character, anchor, and parent region when
  known.
- Current state states the status quo now.
- Geography and travel let players choose a route or direction.
- Active powers name the few groups that can change the region and their next
  visible moves.
- Existing pressure is linked to its owner note; absent pressure is not
  invented and still passes.
- No `type: front` page is created or revived.
- Extra headings are omitted by MACRO, REGIONAL, or LOCAL scale when they do not
  add table value.
- Change log records deltas instead of rewriting the whole region.
- The DM can describe arrival, offer route choices, name who can change the
  region, and say what changed since the last stable state.
- Invention is labeled, cited, and proposed for DM acceptance.
