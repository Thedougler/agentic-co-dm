---
type: item
status: pending
publish: false
aliases: []
summary: "A red-papered consumable that transforms a single ranged hit into a ricochet chain targeting up to two more targets."
created: 2026-08-01
updated: 2026-08-11
tags: [intrigue]
tier: supporting
source: ""
rarity: uncommon
attunement: false
unique: false
form: consumable
found_at: ["[[la-brace|La Brace]]"]
value: "150 gp"
campaigns: [Shattered Sea]
uid: 5a4f6f17-860d-4301-98d8-c27c908dd056
---

# Ricochet Red

> [!read-aloud]
> Red paper, waxed to a shine under the room's lamps, wound tight enough to hold its shape between two fingers.
>
> The tip flares orange the moment it catches. Hotter, sharper, a whiff of scorched copper.
>
> Ash falls from the first draw in one long unbroken curl, red flaking through the grey.
>
> The last inch glows steady, waiting on your next shot.

_Consumable, Uncommon._

One of six blends sold as alchemical cigarettes in [[calveno|Calveno]]. Ricochet Red turns one solid hit into a chain. The shot passes from target to target across a crowd.

| Field | Detail |
|---|---|
| `one_thing` | A hit with a [[weapon-attack\|ranged weapon attack]] lets the shot ricochet on to two more nearby targets, using the same attack bonus. |
| `rarity_justification` | Matches Potion of Fire Breath, Dust of Disappearance. |
| `attunement_reason` | Single use, one power, no bonus to attack, damage, saving throws, or AC. No branch of the attunement decision tree fires. |
| `pc_connection` | [[jean-claude-tabarnack\|Jean-Claude Tabarnack]] knows a [[grung\|Grung]] handler cell won't move on him alone. It sends a crew. Ricochet Red answers three of them with one shot. It costs enough that he needs a real reason to buy it. |
| `current_holder` | [[rufio-segalla\|Rufio Segalla]], rolled to order at [[la-brace\|La Brace]]. |
| `narrative_hook` | Getting one means booking the hour at [[la-brace\|La Brace]] and waiting on Rufio Segalla's price at the end of it, never picking it off a shelf. |

**Rarity:** like Potion of Fire Breath and [[dust-of-disappearance|Dust of Disappearance]], this is Uncommon. Single-use, it always works once used. Ricochet Red's chain can stop on the first hit, and each ricochet skips the wielder's bonus. Its power stays at or below both of those items.

Fio's own stock stays cosmetic. Rufio Segalla's smoking room sells the real thing.

[[rufio-segalla|Rufio Segalla]] rolls this one to order at [[la-brace|La Brace]], a [[velo-quarter|Velo Quarter]] smoking room in Calveno. He never keeps it on the shelf. Getting one means an hour in the room first, with the price coming only after. It never appears on [[la-gatta|La Gatta]]'s board.

## Mechanics

> [!mechanic]
> **Ricochet Red [HB].** Single use, consumable, with no recharge. Lighting it and drawing from it takes a Bonus Action. Once before the end of your next turn, when you hit a creature with a ranged weapon attack, the shot ricochets.
>
> Make a ranged weapon attack with the same weapon against a different creature within 20 feet of the first target, using your same attack bonus. On a hit, it ricochets again to a third creature within 20 feet of the second. Each ricochet deals the weapon's damage dice alone, with no ability modifier added. The chain reaches no farther than that third creature.
>
> **Edge cases:** the ricochet attacks are part of the triggering attack and cost no action of their own. Each ricochet needs a target you can see within range of the last hit, and a ricochet can never return to a creature already hit in this chain. The chain stops the moment a ricochet attack misses. The effect ends when the chain stops, or at the end of your next turn, whichever comes first.
>
> **Limitations:** the triggering attack itself gains no bonus, and ricochet damage never adds an ability modifier. The chain cannot reach a fourth target, and it never returns to a creature it already struck.

## Provenance

[[rufio-segalla|Rufio Segalla]] finishes every blend himself in [[la-brace|La Brace]]'s back room. He buys the base compound by standing order from [[marta-orsini|Marta Orsini]] at [[studio-orsini|Studio Orsini]] in [[le-paludi|Le Paludi]].
