---
type: item
status: pending
publish: false
aliases: []
created: 2026-08-01
updated: 2026-08-11
tags: [intrigue]
summary: "A single-use alchemical cigarette that reveals a creature's compass direction for one hour when lit with a fresh trace of blood, hair, or tracks."
tier: supporting
source: ""
rarity: uncommon
attunement: false
unique: false
form: consumable
found_at: ["[[la-brace|La Brace]]", "[[la-gatta|La Gatta]]"]
value: "150 gp"
campaigns: [Shattered Sea]
uid: 10b90640-2d58-47e3-9c21-8b5ca1179096
---

# Hunter's Blend

> [!read-aloud]
> The wrapper is the deep red of old blood, twisted tight at both ends, a small compass rose stamped near the filter.
>
> It weighs more in the hand than a paper cigarette should. The smell reaches you first, char and a thread of something like wet iron.
>
> Dark fibers run through the leaf in a pattern that never repeats. The leaf packs so dense it takes a hard pull to loosen.
>
> A brass pin through the tip holds the whole thing shut. A single arrow marks its head, and the metal is already warm against your thumb.

_Consumable, Uncommon._

One of six blends of alchemical cigarettes sold in [[calveno|Calveno]]. Hunter's Blend is a bounty hunter's tool, built to turn a dropped trace into a heading.

| Field | Detail |
|---|---|
| `one_thing` | Studied against a fresh physical trace and lit, it shows the compass direction of the marked creature for the next hour. |
| `rarity_justification` | Uncommon, comparable to [[wand-of-secrets\|Wand of Secrets]] (no attunement, divination utility, points toward a hidden target within its own range) and [[bag-of-tricks\|Bag of Tricks]] (no attunement, charge-limited, one bounded effect per use). Hunter's Blend trades their repeatable charges for a single burn, and its direction-only readout with no distance and no line of sight keeps it well under the 4th-level [[locate-creature\|Locate Creature]] spell. |
| `attunement_reason` | Single use, grants no bonus to attack, damage, saving throws, or AC, and carries one power. The attunement decision tree's branches don't trigger. |
| `pc_connection` | [[jean-claude-tabarnack\|Jean-Claude Tabarnack]] already reads the [[grung\|Grung]] handler cell's stances in Calveno's crowds but can never follow one home. Hunter's Blend turns a single dropped trace into an hour of knowing which way a handler went. |
| `current_holder` | Sold from the shelf at [[la-brace\|La Brace]], the [[velo-quarter\|Velo Quarter]] smoking room [[rufio-segalla\|Rufio Segalla]] runs, the only room in Calveno licensed to burn alchemical smoke in the open. Also sold at 60% price as an unreliable second off [[la-gatta\|La Gatta]], a vending board on [[the-bridge\|the Bridge]]'s bottom tier run by [[nicco-kettley\|Nicco Kettley]]. |
| `narrative_hook` | Bought openly at either counter, or found already rolled in the coat of a courier or enforcer who tracks people for a living. |

## Mechanics

**[HB]** Single use, consumable. Before lighting Hunter's Blend, the wielder spends 1 minute with a fresh trace of the target. Blood, hair, nail clippings, or tracks all work, taken within the last 24 hours.

Lighting the cigarette takes an Action. For the next hour, the wielder knows the compass direction of the marked creature, as long as it stays within 1 mile and on the same plane. The smoke gives direction only, never distance, and never what stands along the way.

The effect ends early if the marked creature dies or leaves the plane. It also ends if the creature moves more than 1 mile away. Once lit, Hunter's Blend burns away for good, with no recharge and no recovery.

**Limitations:** gives a heading only, with nothing about distance or sightline and nothing about the creature's condition. It cannot track a creature the wielder never gathered a trace from, and a trace older than 24 hours does nothing. The smoke fails silently against a creature warded by [[nondetection|Nondetection]] or a similar effect.

## Provenance

[[rufio-segalla|Rufio Segalla]] finishes every blend himself in [[la-brace|La Brace]]'s back room, from a base compound he buys by standing order from [[marta-orsini|Marta Orsini]] at [[studio-orsini|Studio Orsini]] in [[le-paludi|Le Paludi]]. [[nicco-kettley|Nicco Kettley]] resells Orsini's rejected batches of the same blend under the Bridge.
