---
type: rule
status: canon
publish: false
aliases: [Ship Combat, Ship-to-Ship Combat, Naval Combat]
summary: "Ship-to-ship combat for any vessel: range bands, gunnery and shot types, chase complications, crew casualties, and hull repair."
created: 2026-08-03
updated: 2026-08-08
tags: [maritime, combat]
tier: core
subtype: subsystem
campaigns: [Shattered Sea]
uid: 1cfdef4c-d6dd-4e24-96f5-80cf5ec53e70
---

# Ship Combat

*What happens once two hulls mean each other harm. Crew, navigation, and upkeep are on [[ship-operations|Ship Operations]].*

## Mechanics

Ships roll initiative and act as creatures do. A vessel's own page states its hull, armament, and modifications. Every PC aboard fights from a station: the role actions on [[ship-operations|Ship Operations]] § Crew Roles are the menu — helm, guns, rigging, repair, the rail — and nobody aboard is without a job.

| Band | Position | What it allows |
|---|---|---|
| Boarding | Alongside, locked, or grappled | Crew cross over. Cannon hit automatically. Swivels bear. |
| Cannon | Standard engagement | Cannon fire normally. Swivels cannot reach. |
| Distant | Extreme range | Cannon fire at disadvantage. Swivels cannot reach. |

The helm spends its [[action|Action]] to change one band, and Dash buys a second. After two consecutive rounds with both vessels at Distant, the quarry is gone.

### Gunnery

Gunnery rolls **[[dexterity|Dexterity]] plus the gunner's bonus** against the target's Hull AC: a hit deals full [[damage|damage]], a miss half, a [[critical-hit|critical hit]] maximum. *Salvo* fires every gun bearing on one side under a single attack roll, and all of them reload after. *Aimed shot* takes a penalty of 2 to disable a named component. *Reload* readies every gun while nothing fires.

| Shot | Hit | Miss |
|---|---|---|
| Round shot | Full hull damage | Half |
| Chain shot | Target [[speed\|speed]] drops one band. Three reductions leave it dead in the water | Half reduction |
| Grapeshot | Deck crew scatter, per the block below | PCs save with advantage |

> [!mechanic]
> **Grapeshot.** Boarding range only, and it cannot touch a hull. Every exposed deck crew makes a DC 14 Dexterity save or falls incapacitated. A PC instead takes 2d6, halved on a success. Any PC who sees it coming drops below deck as a [[reaction|Reaction]] first.

### Chases

Call one complication per chase, at the moment it costs most.

| Complication | DC | Ability | On a failure |
|---|---|---|---|
| Fog bank | 14 | [[wisdom\|Wisdom]] (Perception) | Both vessels move to Distant regardless of speed, and the quarry may break away |
| Reef channel | 14 | [[intelligence\|Intelligence]] ([[navigators-tools\|Navigator's Tools]]) | The pursuer drops one band for 1d4 rounds |
| Wind shift | 12 | Dexterity, by the bosun | The pursuer loses one band of movement |
| Shoaling water | 14 | Intelligence (Navigator's Tools) | The deeper hull grounds. Pursuit ends, or carries on by boat |

### Damage, Casualties, and Repair

Hull Points work as hit points, a hull at zero goes down, and Hull AC is how hard the thing is to hit at all.

> [!mechanic]
> **Crew casualties.** Each threshold fires once per fight, as the hull first drops past it. Three-quarters, one crew member down. Half, 1d4 down. One-quarter, 2d4 down or dead. Name every one of them. PCs never roll on this table.

What the carpenter manages underway and what a yard does alongside are different jobs at different prices.

> [!mechanic]
> **Repair.** At sea, the carpenter makes a DC 15 Intelligence ([[carpenters-tools|Carpenter's Tools]]) check over a short rest to recover 2d8 Hull Points. [[mending|Mending]] Resin restores 2d8 over eight hours with no roll. Neither touches structural damage. **[RAW]** in port, 1 gp per Hull Point at 25 points a workday.

## Provenance

Hull points, repair cost, and the Damage Threshold anchor derive from the 5e SRD ([[mounts-vehicles|Mounts and Vehicles]], [[damage-threshold|Damage Threshold]]). Range bands, shot types, chase complications, and casualty thresholds are homebrew built on that floor.
