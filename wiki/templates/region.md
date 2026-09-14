---
title: "{{title}}"
category: entities
tags: [region]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: region
lifecycle: proposed
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: ""
scale: regional
kind: wilderness
structure: ""
as_of: ""
summary: ""
---
<!--
Copy-start scaffold. Fractal region page for a massive evolving sandbox.

region = parent region.
scale examples: macro, regional, local.
kind examples: realm, province, frontier, wilderness, forest, mountains, archipelago, sea, valley, district.
structure examples: hexcrawl, pointcrawl, routes, abstract.

MACRO — continent, nation, great sea:
Keep Current state, Geography, Subregions, major Routes, Active powers, Fronts, Stakes, and Change log.
Usually omit the encounter table and individual minor sites.

REGIONAL — province, island chain, large wilderness:
Default use. Most sections should earn their place.

LOCAL — valley, island, district, hex-cluster:
Focus on routes, key places, immediate powers, rumors, encounters, and discoveries.
Omit Subregions when they add no useful choice.

Keep persistent geography separate from ephemeral events. Give a detailed site its own [[place]] note once its key no longer fits comfortably here. Keep only the few factions and pressures currently capable of changing this region. Let actual play determine where additional detail is added.
-->

# {{title}}

<!-- Add region art when available. -->

> [!narration] Narration
> Describe the region as a traveler first experiences it: horizon, terrain, weather, movement, sound, and one unmistakable feature. Complete sentences. No secrets, DCs, or unearned names.

## At a Glance

|                   |                                                                |
| ----------------- | -------------------------------------------------------------- |
| **Scale**         |                                                                |
| **Kind**          |                                                                |
| **Character**     | What makes travel or life here unlike the neighboring regions. |
| **Anchor**        | [[place]]                                                      |
| **Known for**     |                                                                |
| **Feared for**    |                                                                |
| **Parent region** | [[region]]                                                     |

> **DM thesis:** One sentence stating what this region is *for at the table*: the choices, pressures, or kind of adventure it creates.

## Current state

> [!summary] Status quo — as of `{{in-world date}}`
> Describe what is normal here *right now* in 2–4 sentences. This is the state to assume until play or an active power changes it.

* **Recent change.** What has broken, arrived, vanished, awakened, or shifted.
* **Pressure.** What is presently getting worse.
* **Opportunity.** What has become newly possible or valuable.
* **Next visible change.** What people will notice next if nobody interferes.

<!-- Keep this section aggressively current. Move obsolete states to Change log instead of accumulating paragraphs here. -->

## Regional truths

<!-- 2–4 durable facts that repeatedly matter during play. Prefer facts that change decisions over encyclopedia lore. -->

* **Truth.**
* **Truth.**
* **Truth.**

## Geography

### Shape and boundaries

Describe the physical logic of the region: what contains it, divides it, feeds it, or makes its edges recognizable.

| Edge | Neighbor   | Crossing / boundary | What changes across it |
| ---- | ---------- | ------------------- | ---------------------- |
|      | [[region]] |                     |                        |

### Subregions

<!-- Use for nested regions with their own identity or play structure. Omit at local scale when unnecessary. -->

| Subregion  | Character | Current pressure | Why go there |
| ---------- | --------- | ---------------- | ------------ |
| [[region]] |           |                  |              |

### Landmarks

<!-- Visible, navigational, culturally dominant, or otherwise reusable landmarks. Detailed locations belong on their own pages. -->

* **[[place]].** What travelers can use it to recognize, navigate, or decide.

## Travel

### Structure

* **Map:** Add a region map when available.
* **Travel structure:** Hexcrawl / pointcrawl / known routes / abstract
* **Scale:** One hex, leg, or travel turn represents …
* **Procedure:** [[travel procedure]]
* **Navigation:** What makes staying on course easy, difficult, or unnecessary.
* **Weather / season:** What routinely alters travel.
* **Rest / supply:** Where travelers can reliably recover or resupply.
* **Regional rule:** One exceptional rule worth remembering at the table; omit when none exists.

### Routes and connections

<!-- Give alternate routes genuinely different tradeoffs. Record only enough information for the players to make a meaningful travel decision. -->

| Route                 | Connects              | Time | Cost / requirement | Risk | Advantage | Known |
| --------------------- | --------------------- | ---: | ------------------ | ---- | --------- | ----- |
| [[route or landmark]] | [[place]] ↔ [[place]] |      |                    |      |           | Yes   |

### Hidden and broken connections

<!-- Secret trails, seasonal passes, teleport circles, washed-out bridges, blockades, newly opened roads, and other connections whose discovery changes the map. -->

* **Connection.** [[place]] ↔ [[place]] — condition for discovering or restoring it.

## Key places

<!-- Curated table-ready places only. Geography persists here; encounters and temporary events do not. -->

| Place     | Kind | Current state | What it offers or threatens | Lead                               |
| --------- | ---- | ------------- | --------------------------- | ---------------------------------- |
| [[place]] |      |               |                             | How the party can learn it exists. |

## Active powers

<!-- Track roughly 3–4 groups with the greatest ability to change this region. Other organizations can exist without occupying active prep. -->

| Power       | Hold / presence | Wants now | Next move | What reveals that move |
| ----------- | --------------- | --------- | --------- | ---------------------- |
| [[faction]] |                 |           |           |                        |

## Fronts and pressures

<!-- Use for forces that keep moving when ignored: villains, wars, plagues, migrations, storms, curses, ecological collapse, etc. Usually 1–3 active fronts are enough. Do not pre-script how the party responds. -->

### [[front or threat]]

* **Impulse / goal.** What drives it.

* **Impending consequence.** What becomes true if it ultimately succeeds.

* **Affected.** [[place]], [[faction]], people, route, or resource placed under pressure.

* **Signals.** What the characters can actually see, hear, discover, or hear rumored.

* [ ] **Portent 1.** First meaningful change.

* [ ] **Portent 2.** Escalation that alters choices.

* [ ] **Portent 3.** Point of crisis.

<!-- Add another front only when it is independently active. -->

## Rumors and leads

<!-- Every entry should give the party something they can investigate, seek, avoid, exploit, or ask about. -->

| d6 | Rumor / lead | Truth behind it | Points toward |
| -: | ------------ | --------------- | ------------- |
|  1 |              |                 | [[place]]     |
|  2 |              |                 | [[place]]     |
|  3 |              |                 | [[faction]]   |
|  4 |              |                 | [[place]]     |
|  5 |              |                 | [[creature]]  |
|  6 |              |                 | [[region]]    |

## Encounter ecology

<!-- Keep encounters separate from the geographic key. Favor reusable procedural ingredients tied to creatures, factions, lairs, routes, and current regional conditions. Change this table when the region changes. -->

**Encounter procedure:** [[encounter procedure]]

| d6 | Encounter | Sign / track / warning | Source or destination |
| -: | --------- | ---------------------- | --------------------- |
|  1 |           |                        | [[place]]             |
|  2 |           |                        | [[place]]             |
|  3 |           |                        | [[faction]]           |
|  4 |           |                        | [[place]]             |
|  5 |           |                        | [[creature]]          |
|  6 |           |                        | [[place]]             |

### Regional signs

<!-- Clues that can foreshadow encounters or let explorers deliberately pursue something instead of meeting it blindly. -->

* **[[creature or faction]].** Tracks, spoor, smoke, songs, refugees, patrol marks, damaged vegetation, abandoned camps, or other evidence.
* **[[front or threat]].** Observable evidence of its current stage.

## What can be found

<!-- Rewards exploration without requiring a fully keyed encyclopedia. These can become places or hooks when discovered. -->

* **Resource.** What is valuable here and who cares about it.
* **Shelter.** Where safety can be found and what it costs.
* **Wonder.** A fantastic feature worth seeking for its own sake.
* **Secret.** A discoverable fact that changes how the region is understood.
* **Shortcut.** A discovery that changes future movement through the region.

## History still in play

<!-- Record the past only when it leaves something usable in the present. -->

| Past fact | Present consequence | Evidence in the world |
| --------- | ------------------- | --------------------- |
|           |                     | [[place or object]]   |

## Stakes

<!-- 1–3 concrete questions whose answers should emerge through play. Do not decide the answers here. -->

* Will …
* Who will …
* What becomes of …

## Change log

<!-- Preserve consequences without burying the current state. Use in-world dates when available. -->

| Date | Change | Cause | Fallout / pages affected |
| ---- | ------ | ----- | ------------------------ |
|      |        |       | [[page]]                 |

## Regional index

<!-- Optional Dataview. Assumes child pages use `region: "{{title}}"` or the region note's filename. -->

```dataview
TABLE
  type AS "Type",
  kind AS "Kind",
  summary AS "Summary"
FROM ""
WHERE region = this.file.name OR region = this.title
SORT type ASC, file.name ASC
```

> [!check]- Between-session maintenance
>
> * [ ] Rewrite **Current state** if play changed the status quo.
> * [ ] Record permanent consequences in **Change log**.
> * [ ] Advance only the active powers or fronts that had reason and opportunity to act.
> * [ ] Turn those off-screen actions into a visible **signal, rumor, encounter, or changed place**.
> * [ ] Update routes, encounter ecology, or faction presence when the fiction changed them.
> * [ ] Promote any newly important site, NPC, creature, faction, or subregion to its own linked note.
> * [ ] Add detail only along the directions the players are actually pursuing.

<!--
Research basis: region material is organized around persistent keyed geography plus separate encounters and a current campaign-status layer; rumors expose actionable regional information; pointcrawl structures can mix scales and nest fractally; meaningful routes differ by consequential tradeoffs; spiral development expands outward from actual player interest; fronts encode active dangers through goals, portents, and unresolved stakes; large sandboxes benefit from limiting active factions to the few currently relevant movers.
Project metadata and presentation conventions aligned with the existing place entity scaffold.
-->
