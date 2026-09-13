---
name: faction-design
description: >-
  Write, edit, or create named faction pages for the campaign wiki. Use when a
  faction, organization, order, guild, cult, polity, crew, movement, or cell
  needs a persistent page, missing named faction note, public face, DM thesis,
  current state, active agenda, agenda clock, faction-turn log, assets, people,
  places, or relationships. Fill wiki/templates/faction.md.
---

# Faction Design

## Work Gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal before writing a campaign wiki page. Write under `wiki/`
only after DM acceptance. If a needed named faction is missing, that faction page
is work to do now: propose it instead of treating the missing note as out of
scope. Ground invention in wiki pages and/or D&D 5e campaign patterns; set
`invention: true`, cite `[[pages]]`, and show contradictions. Never present
invention as wiki fact or write silent canon.

## Faction Job

A faction page makes a named group runnable: what people can observe, what the
DM knows it wants, what it can actually do, what it will try next, and how the
party can notice or interfere. The page is done when the DM can answer:

- What does the faction want?
- What can it do?
- What will it do next?
- What changes if it succeeds?
- How can the party notice or interfere?

Create or edit a named faction page when the group has a durable identity and
players can recognize, join, oppose, bargain with, investigate, steal from,
protect, expose, sabotage, support, or return to it. Store the note under:

`wiki/<campaign>/factions/`

Keep one-off crowds, guards, rumor sources, or unnamed opposition in the owning
beat, place, NPC, or session note until the group has a name or recurring
consequence.

## Procedure

### 1. Retrieve The Faction

Read the brief, `wiki/templates/faction.md`, and relevant NPC, place, quest,
city, region, vehicle, item, spell, prior faction, and session notes. Preserve
established names, aliases, symbols, leaders, territory, resources, public
claims, secret motives, relationships, standing with the party, clocks, and
open questions.

Write one identity sentence before the page:

> This is a [kind/scope] faction that [wants concrete change], acts through
> [signature method], and gives players [choice or pressure].

If that sentence has no concrete change, method, or player opening, keep
retrieving or ask for the missing premise before drafting the page.

### 2. Start From The Template

Copy `wiki/templates/faction.md`. Keep its frontmatter and headings unless an
unused template section says it may be omitted. Fill these frontmatter fields:

```yaml
type: faction
lifecycle: proposed
reveal: unrevealed
campaign: <campaign slug>
visibility: dm
kind: organization
status: active # active | dormant | dissolved
scope: <local|regional|realm|world>
region: "<known region or blank>"
base: "<linked base or blank>"
summary: "<one runnable sentence>"
```

Do not add a second faction template.

### 3. Fill The Playable Page

Fill `> [!narration] Public face` through theatre of the mind. It must state
what an informed person can observe or reasonably know: symbols, reputation,
customs, territory, visible work, and public purpose. Keep secret motives,
hidden leaders, unrevealed plans, DCs, and unearned names out of narration.

Fill `## At a Glance` and the `DM thesis`. The thesis is one sentence of
campaign pressure: what this faction is fundamentally about and why it matters
now.

Fill `## At the Table` with table-useful handles:

- **They want:** what they usually want from outsiders.
- **They offer:** the concrete benefit they can provide.
- **They pressure with:** their characteristic leverage.
- **They will not:** the boundary they rarely compromise.
- **Their tell:** the visible behavior, phrase, symbol, or practice that marks
  them.

Fill `## Current State` with status quo, recent change, pressure, strength,
vulnerability, and opportunity. Add the internal fracture only when it changes
play.

### 4. Write One Active Agenda

Keep one primary agenda whenever possible. Use a second only when the faction can
genuinely sustain an independent second project.

Fill `## Active Agenda` on the faction page:

- **Goal:** a concrete world change.
- **Why:** why it matters now.
- **Clock:** a 4- or 6-segment agenda clock on this faction page.
- **Next move:** what they are preparing or attempting next.
- **Needs:** the enabling person, place, object, permission, resource, or event.
- **Opposition:** who or what stands in the way.
- **Next signal:** what the party can see, hear, suffer, discover, or hear
  rumored.
- **Player opening:** what the party can influence, protect, expose, steal,
  negotiate, sabotage, support, or refuse.
- **If completed:** the concrete new world state if the agenda succeeds.

`hot.md` may point at this agenda, but the clock lives only on the faction page.
Do not store a second clock in `hot.md`.

### 5. Add Only Table-Relevant Structure

Fill only entries that currently change play:

- `## Assets`: forces, money, influence, information, magic, access, strongholds,
  offices, tools, or other resources that enable action.
- `## People & Structure`: leader, lieutenants, agents, cells, blocs, loyalty,
  fractures, and chain of action.
- `## Territory & Touchpoints`: places where the party can encounter the faction
  or its consequences.
- `## Relationships`: actionable stances, leverage, debt, friction, and party
  standing.
- `## Signals & Rumors`: visible signs, rumors, direct signals, and quiet clues
  that surface off-screen motion.
- `## Running the Faction`: what happens when encountered, helped, opposed,
  ignored, or broken.

Link owner pages for table-relevant NPCs, places, assets, rival factions, and
relationships. Mark unresolved facts as seeds or stubs instead of genre
defaults.

### 6. Prepare The Faction Turn

Fill `## Faction Turn > ### Current Turn` at creation. Name the current turn
state with no roll:

- **Want:** the specific result before the next meaningful campaign interval.
- **Move:** the plausible attempt using current resources.
- **Mark:** the fact that changes if the move proceeds.
- **Signal:** how the party can learn about the change.
- **Collision:** what other faction, person, place, resource, or deadline it
  intersects.
- **Player opening:** what remains unresolved and actionable.

Do not roll the Current Turn at create. `world-tick` later resolves turns and
appends `### Turn Log` rows. The turn log records changed canon, newest first;
this skill creates the log table but does not invent resolved future rows.

## Craft Basis

Use faction/front craft for concrete motives, visible portents, and consequences
if unchecked; campaign-status practice for changed state over repeated rewrite;
progress clocks for uncertain long-term change; and sandbox faction turns for
goals, assets, moves, and changed world state. Practical inputs: Dungeon World
fronts by Sage LaTorra and Adam Koebel, Justin Alexander's campaign status
documents, Kevin Crawford's faction turns in Stars Without Number, progress
clocks from Blades in the Dark, and Mike Shea's faction-list advice.

## Done

The page is done when:

- It lives in `wiki/<campaign>/factions/` with `type: faction`.
- It fills `wiki/templates/faction.md` without adding another template.
- Public face is `[!narration]` and contains only informed observable knowledge.
- DM thesis is one sentence of campaign pressure.
- Current state states status quo, recent change, pressure, strength,
  vulnerability, and opportunity.
- One active agenda has goal, why, clock, next move, need, opposition, signal,
  player opening, and completion consequence.
- The agenda clock lives on the faction page; `hot.md` has no duplicate clock.
- Assets, people, places, and relationships include only entries that currently
  change play.
- Current Turn is filled with no roll or resolved future result.
- Turn Log exists for `world-tick` to append later.
- Invention is labeled, cited, and proposed for DM acceptance.
