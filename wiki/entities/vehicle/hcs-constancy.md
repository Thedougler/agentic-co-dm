---
title: "HCS Constancy"
aliases:
  - HCS Constancy
category: entities
tags: [shattered-sea, vehicle]
sources:
  - "campaign-os:hcs-constancy.md"
created: 2026-09-13
updated: 2026-09-13
type: vehicle
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "A Crown patrol ship that enforces inspections and takes ships into custody."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# HCS Constancy

> [!narration] Narration
> A two-masted frigate on a grey hull, twelve cannon ports per side on the main gun deck and eight more above on the upper deck. The white stripe runs bow to stern at the upper deck rail. Crown pennant at the mainmast. A rating officer is already visible at the rail before the ship finishes its turn into your wind. She is not threatening you. She is waiting for you to make the next move.

A two-masted heavy frigate, 140 feet on the waterline, built at the [[Harwick]] Naval Yard. The Admiralty uses this class for enforcement rather than mere inspection. It carries enough guns to discourage resistance. It holds enough cargo for seized goods and prisoners. It has the range to patrol [[verdant-scatter|the Scatter]] for months.

*Heavy Frigate · Tier 3 · [[calders-tooth-and-port-tidefall]].*

The hull is grey with a white stripe at the upper rail. A brass plate marks the bow. The Crown pennant hangs at the mainmast. The stern cabin is the captain's office with locked drawers, a record book, and a tube down to the gun deck.

The ship inspects vessels in Crown waters. It checks hull records, cargo lists, crew papers, and charters. It stops and seizes ships by court order. It guards Crown trade convoys and stops illegal privateers. It cannot run from threats. But it stops them by being there.

**Weather deck**: helm, compass, signal flags, Crown lamp array, captain's cabin, swivel mounts, and marine station.

**Upper gun deck**: eight guns per side. Holds the Inspection Office plus officer and crew dining facilities.

**Main gun deck**: twelve guns per side. This main fighting deck holds crew quarters and an armorer's station.

**Below decks**: brig and holding cells alongside surgeon's quarters and supplies.

**Hold**: ammunition and shot. The ship also carries 75 tons of cargo.

## Stats & Combat

| | |
|---|---|
| **Type** | Heavy Frigate |
| **Tier** | 3 |
| **Variant** | Armed |
| **Decks** | 2 gun decks + weather deck |
| **Hull Points** | 390 |
| **Hull AC** | 13 |
| **Condition** | Good |
| **Speed (good wind)** | 65 miles/day |
| **Speed (poor wind)** | 30 miles/day |
| **Maneuverability** | Average |
| **Profile** | Large |
| **Crew (min/full)** | 20 / 85 |
| **Cargo** | 75 tons |
| **Gun Mounts** | 52 (12 per side main gun deck; 8 per side upper deck; 4 bow chasers; 4 stern chasers) |
| **Weapons** | 40 × 18-lb Long Cannon; 8 × 12-lb Chaser; 4 × Swivel (weather deck) |
| **Upkeep** | ~360 gp/week |
| **Available Space** | 16 units (Tier 3 max) |
| **Special Facility Slots** | 2 |

**Facilities:**

| Facility | Space | Hireling | Effect |
|---|---|---|---|
| Inspection Office | 2 | Rating Officer (specialist) | *Active:* once/Bastion Turn, formally inspects a named vessel or individual, producing a valid Crown-certified rating in Crown proceedings. *Passive*: flagged Crown vessels in the same harbour count as inspected for the week. Non-Crown captains formally rated make Deception checks at disadvantage against Crown officials with registry access. |
| Brig and Holding Deck | 2 | Marine Sergeant (double-role: bosun) | *Active:* once/Bastion Turn, processes one prisoner per holding compartment (deposition, extraction, transfer). *Passive:* holds and transports persons under Crown warrant at no extra cost. Escape attempts are at disadvantage due to cells below waterline. The brig accommodates up to twelve prisoners in four compartments. |

## Crew

The source provides no captain or crew. The facility hirelings include a Rating Officer (Inspection Office) and a Marine Sergeant (Brig and Holding Deck). The Marine Sergeant also serves as bosun.

## Connections

- [[dravosi-crown]] (operating authority)
- [[crown-islands]] (patrol waters)
- [[calders-tooth-and-port-tidefall]] (home waters, unnamed as literal home port in source). Resolved (R33 close-out): the earlier "no page yet" note was stale. `vault/campaigns/shattered-sea/locations/calders-tooth/tidefall.md` carries `aliases: [Port Tidefall]` in its own frontmatter.
- [[Harbourmaster's Office]] (issuing and enforcing civil authority for Impound Orders). This appears in the source's Purpose section but not as an explicit Connections-list entry, though named in body text.
- [[hcs-sovereign]] (named in source's own Connections list)
