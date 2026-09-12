---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Running a ship as the party's bastion — facilities, space budget, and what each installed facility does."
created: "2026-08-03"
updated: "2026-08-03"
tags: [maritime]
uid: 0b8e4b36-d147-47c1-9c59-4d631077f85b
---

# The ship as a shared, mobile bastion

Mined from the archived `prep-ship` skill's ship-rules reference (no longer
present in this repo) § "The Ship as a Bastion." Read this only when the ship serves (or will serve) as the party's home
base — a Tier 0–1 one-off vessel with no bastion ambitions doesn't need it. Uses the
2024 DMG Bastion system as its foundation; every deviation below is marked
**[Homebrew]**. Reference from SKILL.md, don't restate.

---

## When bastion mechanics activate

Immediately, once the first facility is installed — no level requirement. The Bastion
Turn (once per in-game week) applies from the moment the first assignable facility is
operational, whether the ship is in port or underway.

## Ship tier and facility space

The 2024 bastion space-unit system, adapted to ship tier:

| Ship tier | Available space units | Special facility slots |
|---|---|---|
| 1 | 4 | 0 |
| 2 | 8 | 1 |
| 3 | 16 | 2 |
| 4 | 24 | 3 |

Upgrading to a larger ship expands the bastion. Facilities transfer from a smaller ship
to a larger one during a refit: same installation cost, half the time, requires a port
with a shipyard.

**Special facility slots** — the 2024 bastion's advanced options (normally unlocked at
character level 5+) are instead unlocked by ship tier: a Tier 2 ship can install one
special facility, Tier 3 can install two. Special facilities requiring a fixed location
(a teleportation circle, a greenhouse, a stable) stay excluded — they don't fit a
moving vessel.

## Facility list

Use the 2024 rules for each facility's benefit, cost, hireling slot, and Bastion Turn
action; rename it for shipboard tone.

| 2024 facility | Ship equivalent | Space |
|---|---|---|
| Arcane Study | Navigator's Chart Room | 1 |
| Armory | Weapons Locker | 1 |
| Barracks | Crew Berths | 1 |
| Gaming Den | Officer's Mess | 1 |
| Garden | Provisions Store | 2 |
| Guild Hall | Trading Post | 2 |
| Hospital | Surgeon's Berth | 1 |
| Laboratory | Tinker's Workshop | 2 |
| Library | Chart Archive | 2 |
| Pub | Ship's Galley | 1 |
| Reliquary | Trophy Room | 1 |
| [Sanctuary](vault/srd/spells/abjuration/sanctuary.md) | Shrine (of the party's chosen patron) | 1 |
| Smithy | [Carpenter's Shop](vault/srd/rules/carpenters-shop.md) | 1 |
| Storehouse | Expanded Cargo Hold | 2 |
| Trophy Room | Captain's Cabin | 1 |
| War Room | Helm and [Command](vault/srd/spells/enchantment/command.md) | 1 |
| Workshop | Rigger's Workshop | 1 |

2024 facilities with no nautical equivalent ([Demiplane](vault/srd/spells/conjuration/demiplane.md), Greenhouse, Stable,
[Teleportation Circle](vault/srd/spells/conjuration/teleportation-circle.md), Theater, Sacristy) are excluded — don't force them onto a hull.

**Sanctuary note:** if the party installs a shrine to a specific sea deity or patron,
that's a real propitiation arrangement worth a DM-Only line — name the actual
established deity/faction from this campaign's own wiki (grep `vault/` first), never
invent one from the archived source's flavor. The passive benefit is narrative
(the ship is treated as having made its departure offering) — not a guarantee of
safety, an appeasement.

## The Bastion Turn — moving-vessel adaptation **[Homebrew]**

The 2024 Bastion Turn assumes a stationary structure. Adaptations:

- **Frequency** — once per in-game week, same as 2024 RAW. It resolves at week's end
  regardless of whether the ship is in port or underway. Port weeks use the standard
  2024 Bastion Event table as written (§ below covers the underway replacement).
- **Facility function while underway** — every facility functions normally at sea
  provided the ship has its minimum crew filled (`vault/refs/vault/ship/references/tiers-and-crew.md` § 3). A
  hireling who is both crew and a facility's assigned hireling counts for both.

## Shared bastion direction **[Homebrew]**

2024 RAW gives each character their own separate bastion; a ship is one **shared**
bastion. Rules for five (or however many) players directing one structure:

- **The Captain is the Bastion Manager** — final authority over the Bastion Turn:
  assigns hirelings to facility actions, resolves disputes. A PC Captain makes these
  calls directly; an NPC Captain executes what the party decides collectively.
- **Each PC may personally direct one facility per turn** — claim it, direct its
  action, receive any personal benefit it grants its director (crafting results,
  research outcomes, downtime bonuses). The Captain can't override a PC's personal
  direction unless the facility is currently unclaimed.
- **Passive benefits go to everyone aboard** — the Cook's long-rest HP bonus, a
  Surgeon's-Berth healing option, a Chart Archive's navigation reference — no PC needs
  to have directed the facility to receive its passive effect.
- **Active directed benefits go to the director only.** If nobody directs a facility
  that week, the Captain assigns a hireling and the benefit is held in reserve or lost,
  per the 2024 facility rules.

## Bastion events — moving-vessel replacement table **[Homebrew]**

The 2024 Bastion Event table assumes a fixed location. Replace its location-based
entries with these when rolling for a ship underway (in port during the Bastion Turn:
use the 2024 table as written):

| 2024 event type | Shipboard equivalent |
|---|---|
| Local threat / attack | A hostile vessel has been tracking the ship — DM determines nature and timing |
| Beneficial contact | A passing ship offers information, trade, or an unexpected opportunity |
| Structural damage | A storm or incident has damaged a facility — repair cost per 2024 rules |
| Windfall | A current or wind shortens the current voyage — arrive 1d4 days early |
| Hireling issue | A hireling has a problem the party needs to resolve — 2024 hireling event rules |

Roll or assign this via a real roller, same no-invented-randomness principle
`travel-events` Hard Rule 2 and `roll-dice` enforce — never hand-pick the outcome.

## Bastion defense — moving-vessel adaptation **[Homebrew]**

2024 RAW assumes the party is absent from a stationary bastion. Adapted:

- **Party aboard** — no defense roll needed; threats resolve through play.
- **Party absent, ship in port** — 2024 Bastion Defense rules as written; the ship is
  effectively stationary.
- **Party absent, ship underway (hireling-crewed)** — treated as a stationary bastion
  for defense purposes, but substitute the ship's **crew quality** for a fixed
  location's defense rating: full crew of experienced hirelings +3, skeleton crew or
  poor hirelings +0, below minimum crew −2. The nature of "attacks" on an unattended
  underway ship is limited to piracy, patrol interception, or weather — narratively
  resolved from the defense outcome.
