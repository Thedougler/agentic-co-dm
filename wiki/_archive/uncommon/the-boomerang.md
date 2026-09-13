---
type: item
status: pending
publish: false
aliases: []
summary: "An alchemical cigarette whose exhaled ring grants the wielder one reroll on a missed ranged weapon attack."
created: 2026-08-01
updated: 2026-08-11
tags: [intrigue]
tier: supporting
source: ""
rarity: uncommon
attunement: false
unique: false
form: consumable
found_at: ["[[la-brace|La Brace]]", "[[la-gatta|La Gatta]]"]
value: "100 gp"
campaigns: ["Shattered Sea"]
owner_skill: ".claude/skills/draft-content/references/item.md"
uid: cf9f7c0b-9d2a-4656-b5b1-3a0ec6da5c71
---

# The Boomerang

> [!read-aloud]
> A thin roll of paper. No longer than a finger, its wrapper printed with a ring inside a ring, over and over down its length.
>
> The paper gives slightly under your thumb, packed tighter at one end than the other.
>
> It smells of scorched citrus rind before you have even struck a match to it.
>
> The unlit end sits blunt and dark, waiting for a flame to give it a ring of its own.

_Consumable, Uncommon._

One of six alchemical cigarette blends sold in [[calveno|Calveno]]. Among the dock crews it goes by its own name for itself: didn't hear no bell.

| Field | Detail |
|---|---|
| `one_thing` | Once lit, it lets the wielder reroll their next missed ranged weapon attack against the same target. |
| `rarity_justification` | Uncommon, comparable to Potion of Fire Breath (Uncommon, single-use consumable, no attunement, guarantees an area of fire damage on use) and [[dust-of-disappearance\|Dust of Disappearance]] (Uncommon, single-use consumable, no attunement, guarantees invisibility for its duration). Both hand the user a certain combat benefit. The Boomerang only offers a second attempt at a roll that can still fail, so its power stays below both benchmarks. The repo's rarity budget puts anything with combat relevance at Uncommon or above, so this sits above Common despite the small effect. |
| `attunement_reason` | Single use, grants no bonus to attack, damage, saving throws, or AC, and carries one power. The decision tree's attunement branches don't trigger. |
| `pc_connection` | [[jean-claude-tabarnack\|Jean-Claude Tabarnack]] (the cheapest blend on the board, and the one he can buy without anyone reading anything into it). He buys it for cover as much as for backup. |
| `current_holder` | Sold from the shelf at [[la-brace\|La Brace]], a [[velo-quarter\|Velo Quarter]] smoking room run by [[rufio-segalla\|Rufio Segalla]], the only room in Calveno licensed to burn alchemical smoke in the open. Also sold at 60 percent price (60 gp) as an unreliable second off a vending board called [[la-gatta\|La Gatta]] on [[the-bridge\|the Bridge]]'s bottom tier, run by [[nicco-kettley\|Nicco Kettley]]. |
| `narrative_hook` | Bought openly at either counter, or found already in the pocket of a dock crew regular who smokes it before a job. |

## Mechanics

**[HB]** Single use, consumable. As a [[bonus-action|Bonus Action]], the wielder lights the cigarette and draws from it, exhaling a ring of smoke.

Once before the end of the wielder's next turn, the first time the wielder misses with a ranged weapon attack, they may reroll that attack roll against the same target. The wielder must use the second roll, even if worse than the first.

The cigarette burns out the instant the wielder uses the reroll, or at the end of the wielder's next turn if no ranged weapon attack misses in that window.

**Limitations.** Grants one reroll only. Applies only to ranged weapon attacks, not spell attacks, melee attacks, saving throws, or ability checks. Never rerolls damage. Does nothing if the second roll also misses.

## Provenance

[[rufio-segalla|Rufio Segalla]] finishes every blend himself in [[la-brace|La Brace]]'s back room, from base compound he buys by standing order from [[marta-orsini|Marta Orsini]] at [[studio-orsini|Studio Orsini]] in [[le-paludi|Le Paludi]]. [[nicco-kettley|Nicco Kettley]] resells Orsini's rejected batches of the same blend under the Bridge.
