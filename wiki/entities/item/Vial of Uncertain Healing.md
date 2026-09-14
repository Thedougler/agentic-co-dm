---
title: "Vial of Uncertain Healing"
category: entities
tags: ["shattered-sea", "item", "comedy", "uncommon"]
sources:
  - "campaign-os:vial-of-uncertain-healing.md"
created: 2026-09-13
updated: 2026-09-13
type: item
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "A potion that always heals, and always does one other random thing too."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Vial of Uncertain Healing

> [!narration] Narration
> A small glass vial, corked and waxed shut, holding a liquid whose color shifts subtly depending on the light it catches (amber in a candle's glow, faintly green under open sky). The weight and viscosity feel exactly right for a healing draught, the cork releasing with the same soft pop any potion vial makes. And yet an unease settles in the hand, faint and sourceless, the way a smile held a beat too long stops looking friendly.

*Potion, Uncommon.*

| Field | Value |
|---|---|
| One thing | Drinking this potion always heals 1d6 hit points and always leaves the drinker talking uncontrollably for 1 hour. A failed Constitution save also triggers one random potion effect rolled fresh from a d6 table. Every dose is a guaranteed heal wrapped in an unpredictable gamble, never just a plain healing potion. |
| Rarity justification | Uncommon: the guaranteed 1d6 healing alone would be closer to Common (matching [[Potion of Healing]] (Common)), but the attached random effect draws from a table that includes real Uncommon-tier potion effects ([[Potion of Growth]], [[Potion of Poison]], and others), so the item as a whole sits at Uncommon to match its strongest possible outcome. |
| Attunement reason | Potions never require attunement per SRD convention (single-use items, applied and spent immediately). This matches every potion in the vault. |
| PC connection | [[Delmar Fisk]] carries one, slipped into his coat by [[Lavinia Sordi]] along with a way to reach her directly. Each future use is a 1d6 gamble, not just a guaranteed heal. |
| Current holder | [[Lavinia Sordi]] keeps vials stocked at [[La Cenere]]; [[Delmar Fisk]] carries one in his coat. |
| Narrative hook | Still available to buy at [[La Cenere]] for 75 gp. Lavinia doesn't test her own stock, so nobody but the drinker ever finds out what a given vial actually does. |

## Mechanics

> [!mechanic]
> **Uncertain Draught [HB].** Drinking this potion is a Bonus Action, consumed on use. It always restores 1d6 hit points, and the drinker immediately starts talking, unable to stop, for 1 hour: harmless, constant, and impossible to suppress.
>
> **Edge cases:** the healing and the talking always happen, save or no save on the check below. A creature can roll the same d6 result twice in separate uses. The table doesn't track what a creature has already gotten.
>
> **Limitations:** the drinker cannot choose or reroll the random effect, and cannot suppress the hour of compulsive talking once it starts. The potion doesn't scale with the drinker's level. Nothing about this potion reads as anything other than a plain healing draught before it's drunk.

> [!check] [[Constitution]] Save — The Second Effect
> DC 11. The drinker rolls immediately after drinking.
> **Success:** the drinker gets the healing and the talking, nothing else.
> **Failure:** roll a d6 and apply the matching potion effect in full, exactly as written on that potion's own page (table below).

1. [[Potion of Climbing]]
2. [[Potion of Animal Friendship]]
3. [[Potion of Growth]]
4. [[Potion of Resistance]] (roll or choose the damage type per that potion's own text)
5. [[Potion of Water Breathing]]
6. [[Potion of Poison]], whose own save never re-triggers, since rolling this result already counts as the failure.

## Provenance

[[Lavinia Sordi]] stocks these from her rack at [[La Cenere]] in [[Le Paludi]], [[Calven and Calveno]], for 75 gp. Her pitch: "Correct color, correct consistency. Probably Greater. I say probably because I don't drink my own stock."

[[Delmar Fisk]] drank one as a free sample in Session 8. Con save of 11 meant no adverse effect. He gained 1d6 healing and talked non-stop for an hour. Lavinia then slipped a second vial into his coat along with a note, winning a contested Sleight of Hand check.
