---
type: item
status: pending
publish: false
title: ""
aliases: []
summary: "Rare attuned armor that lets the wearer detonate a self-centered Fireball they're immune to."
created: "2026-08-06"
updated: "2026-08-06"
author: hb
tags: [combat, arcane]
tier: supporting
rarity: rare
attunement: true
unique: false
form: armor
found_at: ["[[vask-reclaimed-goods|Vask's Reclaimed Goods]]"]
value: "2,000 gp"
campaigns: []
reference_image: ""
uid: 4a0bc3d8-5871-4107-b378-7fd096f7c869
---

# Armor of Fireballs

> [!read-aloud]
> Glowing orange spirals mark the shoulders and the center of the chest, three coiled sigils warm to the touch while the plate around them stays cool. Press a palm to the breastplate and something answers with a slow, banked warmth, like a hearth-coal that never fully cools.

*Armor (Light, Medium, or Heavy), Rare (Requires Attunement).*

**Item Toy**

| Field | Value |
|---|---|
| `one_thing` | Action-activated [[Fireball]] centered on the wearer, who is immune to it. The armor's own fire resistance makes triggering it survivable. |
| `rarity_justification` | Rare, comparable to [[periapt-of-proof-against-poison\|Periapt of Proof against Poison]] (passive damage-type immunity paired with a linked benefit) and [[ring-of-evasion\|Ring of Evasion]] (a strong, recharge-gated combat action, not at-will). Both are Rare and both require attunement. |
| `attunement_reason` | Rare tier default: always requires attunement if combat-relevant (item-rarity-budget.md). This item is combat-relevant on both its passive and active powers. |
| `pc_connection` | None. World flavor, not tied to a specific PC's arc (DM ruling, 2026-08-06). |
| `current_holder` | [[vask-reclaimed-goods\|Vask's Reclaimed Goods]], on the rack near the counter. |
| `narrative_hook` | On sale at [[sorin-vask\|Sorin Vask]]'s shop in [[kalowe\|Kalowe]] for 4,000 gp, its origin left to whoever buys it. |

## Mechanics

**[HB] Fire Resistance.** The wearer has resistance to fire damage. The wearer keeps this benefit as long as they remain attuned to the armor and keep it on.

> [!mechanic]
> **[HB] Armor Fireball.** Trigger: the wearer takes an action to activate the armor. Effect: a [[Fireball]] erupts centered on the wearer. Every creature in the 20-foot-radius sphere, including allies, makes a DC 15 [[Dexterity]] save, taking 8d6 fire damage on a failure or half as much on a success. The wearer takes no damage from this blast. Recharge: the ability recharges once the wearer takes 15 or more fire damage in a single instance, or at dawn.

**Edge cases.** The sphere always centers on the wearer, not a point they choose. Anyone standing close, ally or enemy, faces the same save and damage as a foe would. The armor's own power casts this Fireball directly, so the wearer spends no spell slot, component, or concentration on it. The DC stays fixed at 15 no matter the wearer's own stats.

**Limitations.** The armor grants only the two powers above, adding no bonus to AC or to weapon attacks. The Fireball always centers on the wearer, who cannot redirect it to another point. Fire Resistance protects only against ordinary fire damage, and full immunity applies solely to the armor's own triggered Fireball. Once triggered, the wearer cannot activate the ability again until it recharges.

## Provenance

No one has claimed to have made it. It sits on the rack at [[vask-reclaimed-goods|Vask's Reclaimed Goods]] in [[kalowe|Kalowe]] now, folded into the salvage trade there like everything else on the shelves.
