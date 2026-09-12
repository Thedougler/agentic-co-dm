---
type: rule
status: canon
publish: false
aliases: [Ship Operations, Sailing Rules]
summary: "Running a vessel: crew roles and pay, navigation checks and complications, weekly facility management, and a ship's standing in port."
created: 2026-08-03
updated: 2026-08-08
tags: [maritime, combat]
tier: core
subtype: subsystem
campaigns: [Shattered Sea]
uid: 2dcc5bfd-942e-4be2-8c1e-d27f7995ee77
---

# Ship Operations

*Crewing and sailing a vessel, for any hull afloat. Fighting one is on [[ship-combat|Ship Combat]].*

## Mechanics

A vessel's own page states its numbers, and [[ship-upgrades|Ship Upgrades]] carries the enhancements it can buy. Crew minimums come [RAW] from [[mounts-vehicles|Mounts and Vehicles]], everything below [HB].

### Crew Roles

A PC holds a role, a hireling fills it, or it stands open. An open role cannot function, or works at disadvantage.

| Role            | Function                                               | Key ability                                                              | Rate     | In action                                                                                                                                                                                                                  |
| --------------- | ------------------------------------------------------ | ------------------------------------------------------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Captain         | [[command\|Command]] decisions, crew direction, morale | [[charisma\|Charisma]]                                                   | —        | **[[action\|Action]]** *rallying order*. One creature within 60 ft gains advantage on its next check or attack.                                                                                                            |
| Quartermaster   | Stores, discipline, internal order                     | Charisma                                                                 | 10 gp/wk | **Action** *crew's voice*. One ally rerolls a failed check, attack, or save. **[[reaction\|Reaction]]** *fair witness*. A crew member within 60 ft rolls a death save or a [[frightened\|Frightened]] save with advantage. |
| Navigator       | Course-plotting, hazard avoidance                      | [[intelligence\|Intelligence]] ([[navigators-tools\|Navigator's Tools]]) | 10 gp/wk | **Action** a navigation check. **Reaction** *hazard warning*, declared first, and the vessel rolls with advantage.                                                                                                         |
| Lookout         | Masthead watch, sails and weather sighted first        | [[wisdom\|Wisdom]] (Perception)                                          | 6 gp/wk  | **Action** *sweep the horizon*. **Reaction** *cry warning*. The crew is not surprised by the sighted threat.                                                                                                               |
| Bosun           | Rigging, sails, deck crew                              | [[strength\|Strength]] or [[dexterity\|Dexterity]]                       | 8 gp/wk  | **Action** *trim sails*. **Reaction** *brace*. One creature aboard halves damage from a ram or collision.                                                                                                                  |
| Gunner          | Ordnance direction and maintenance                     | Dexterity                                                                | 8 gp/wk  | **Action** salvo, aimed shot, or reload.                                                                                                                                                                                   |
| Carpenter       | Hull repair, damage control                            | Intelligence ([[carpenters-tools\|Carpenter's Tools]])                   | 6 gp/wk  | **Action** emergency repair. **[[bonus-action\|Bonus Action]]** *plug the breach*.                                                                                                                                         |
| Cook            | Provisions, crew sustenance                            | [[wisdom\|Wisdom]]                                                       | 4 gp/wk  | Every crew member recovers an extra **1d6 HP** on a long rest aboard.                                                                                                                                                      |
| Surgeon         | Wounds and casualties                                  | Wisdom (Medicine)                                                        | 8 gp/wk  | **Action** stabilise a creature, or restore **1d6 + 4 HP** for one use of a [[healers-kit\|Healer's Kit]]. **Bonus Action** *field triage*.                                                                                |
| Marine          | Boarding, armed watch, security                        | Strength or Dexterity                                                    | 14 gp/wk | **Action** attack, seize, or shove. **Bonus Action** *hold the rail*.                                                                                                                                                      |
| Ordinary sailor | Everything else                                        | —                                                                        | 2 gp/wk  | **Action** help. One creature gains advantage on its next check or attack.                                                                                                                                                 |

Crewed below a vessel's stated minimum, every ship check falls to disadvantage and speed drops by a fifth.

| Role action | DC | Ability | Effect |
|---|---|---|---|
| Trim sails | 10 | Dexterity | The helm gains one extra band this turn |
| Plug the breach | 10 | Intelligence (Carpenter's Tools) | Fire stops spreading for one round |
| Stabilise a creature | 10 | Wisdom (Medicine) | One incapacitated creature stabilises |
| Field triage | 10 | Wisdom (Medicine) | One creature gains advantage on its next death save |
| Hold the rail | 13 | Strength (Athletics), by the boarder | A failure shoves the boarder back |

### Stations Underway

At the start of each leg every PC aboard calls a station — no two PCs the
same one, and any of the five left uncalled simply makes no roll, so the
leg takes that station's failure side unanswered. Each station rolls once
per leg against the navigation tier below (charted 10, unfamiliar 14,
storm water 18). A success banks its boon for the leg; a failure hands the
sea its complication — the trouble arrives *through* that station's watch,
never as a flat penalty.

| Station | Check | Success banks | Failure means |
|---|---|---|---|
| Navigator | Int (Navigator's Tools) | The passage runs true — on 18+, a day shaved | Off course per Navigation below |
| Lookout | Wis (Perception) | Whatever the leg brings is sighted early: the crew picks the range and posture it's met at | It's on top of you before the cry goes up |
| Quartermaster | Wis (Survival) | Stores hold: no supply toll this leg | A cask spoils, a ration short — one supply toll bites |
| Bosun | Str or Dex | Sails trimmed: the helm holds one band of advantage in the leg's first chase or storm round | Worn rigging — the first sail-order of the next trouble is at disadvantage |
| Captain | Cha | The crew holds: one station may reroll its leg check (once) | Grumbling below decks — the next morale or fear save is at disadvantage |

The Cook and Surgeon keep their standing effects underway; the Captain's
station may be held from any deck. A hireling in a role can hold its
station, rolling at +2 flat — but a station a PC holds is a station the
table plays, and that is the point.

### Passage and Navigation

> [!mechanic]
> **Navigation.** One check per leg, Intelligence ([[navigators-tools|Navigator's Tools]]). Charted and calm, DC 10. Unfamiliar water or a reef approach, DC 14. Storm, uncharted shallows, or the [[the-drowned-maw|Maw]], DC 18. A failure delays the voyage 1d4 days and lands one complication, never the same one twice.

Near shore a complication only inconveniences: a course deviation, a weather front, a sandbar costing half a day to warp off. In storm water they bite. Fog swallows every landmark for 1d4 days, a working sea opens 2d10 of hull, a hand goes over the rail. Charts grant advantage only where their survey covers, contradictory charts grant nothing, and within five miles of the Maw a compass is useless.

### Weekly Management

Each installed facility takes one order a week: craft, activate, harvest, maintain, recruit, research, or trade. A facility idle three weeks goes dormant, its staff walk, and recommissioning costs 100 gp and a week alongside. A recruit order hires up to twelve Defenders, who answer for the ship when no officer stands aboard.

> [!mechanic]
> **Facility event.** Roll d6 on a maintain order. **1** a hostile sail has been tracking the ship. **2** a passing vessel offers trade or intelligence. **3** storm damage, costing a Carpenter's check and a day. **4** a favourable current shortens the voyage 1d4 days. **5** a hireling needs an officer. **6** clear sailing.

An event that lands while the officers are ashore falls to whoever they left aboard.

> [!mechanic]
> **Defence of the vessel.** With no officer aboard and a hostile event landing, roll 6d6. Each 1 kills one [[defender|Defender]], and if every Defender falls, one facility goes dormant the following week. A stocked weapons locker upgrades those dice to d8. Underway with a full experienced crew, add 3 to each die. Below minimum complement, subtract 1. With officers aboard, play it out instead.

### Standing

Reputation tracks per faction and per port a vessel regularly calls at, never as a single number.

| Standing | Effect |
|---|---|
| Respected | Reduced berth fees, willing hires, faction contacts open |
| Known | Judged on actual deeds |
| Wanted | Port access restricted or denied, bounties posted |
| Notorious | Capable crew seek the ship out, and some targets strike rather than fight |

Flying no flag reads as suspicious, and flying a false one is common but costly where the deception is caught.

## Provenance

Crew minimums derive from the 5e SRD ([[mounts-vehicles|Mounts and Vehicles]]). Crew roles, navigation DCs, and facility management are homebrew built on that floor.
