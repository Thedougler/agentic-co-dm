---
title: "Eight Seconds"
category: entities
tags: ["shattered-sea", "item", "intrigue", "rare"]
sources:
  - "campaign-os:eight-seconds.md"
created: 2026-09-13
updated: 2026-09-13
type: item
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "An alchemical cigarette that burns for about eight seconds, granting one extra action per turn for two consecutive turns before dropping the smoker prone and unable to react."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Eight Seconds

> [!narration] Narration
> The cigarette lies thin and pale between two fingers, its paper wound tighter than anything else on Rufio's shelf.
>
> A struck match brings it to the tip, and the paper catches all at once, a bright line racing away from the fingers holding it.
>
> Smoke lifts off it in one steady ribbon and thins to nothing before it reaches shoulder height.
>
> The last third burns fast. The ember eats the final inch while the fingers still feel cool.


*Consumable, Rare.*

| Field | Detail |
|---|---|
| `one_thing` | For about eight seconds after lighting, the smoker gains one extra action on the current turn and on the next turn, then falls prone and loses reactions until their following turn ends. |
| `rarity_justification` | Rare, comparable to Potion of Invulnerability (resistance to all damage for 1 minute) and [[Potion of Heroism]] (10 temporary hit points plus a 1-hour [[Bless]] effect). None of the three requires attunement. Eight Seconds borrows [[Haste]]'s extra-action shape at a much smaller scale: it lasts two rounds where Haste lasts ten. Speed, AC, and [[Dexterity]] saves stay the same, and the burn ends by dropping the smoker prone with reactions gone for a turn. That smaller shape keeps Eight Seconds at Rare, below [[Potion of Speed]]'s Very Rare tier. |
| `attunement_reason` | No attunement required: a single-use consumable with one power, and no bonus to attack, damage, save, or AC rolls. |
| `pc_connection` | [[Jean-Claude Tabarnack]]. His cover holds only while nothing forces him to fight in the open, and Eight Seconds buys him two rounds to disappear before anyone works out what they just watched. |
| `current_holder` | [[Rufio Segalla]] rolls this one to order at [[La Brace]], a [[Velo Quarter]] smoking room in [[Calveno]]. He never keeps it on the shelf. |
| `narrative_hook` | Buying it requires an hour seated in the room first, and Rufio names the price only afterward. It never appears on [[La Gatta]]'s board. |

## Mechanics

**[HB]** Lighting Eight Seconds and taking its first breath costs a [[Bonus Action]]. It affects only the smoker, and it keeps burning through the end of the smoker's next turn. It has no recharge: this is a single-use item, gone the instant it burns out.

On the turn you light it and on your next turn, you gain one extra action. You can spend that extra action only on the [[Attack action]] (one weapon attack only), [[Dash]], [[Disengage]], [[Hide]], or [[Use an Object]]. It burns out. At the end of your second turn when it does, you fall [[prone]] and can't take [[reactions]] until the end of your following turn.

Edge cases:

- The extra action is not a bonus action. You can't spend it on a bonus action or on casting a spell.
- The single weapon attack it allows ignores Extra Attack.
- You fall prone when the cigarette burns out, used the extra actions or not.
- Lighting a second Eight Seconds while the first still burns does nothing, and wastes the second cigarette outright.

**Limitations.** Eight Seconds grants no bonus to attack rolls, damage rolls, saving throws, or AC, and its extra action can't fuel a bonus action, a spell, or a second weapon attack through Extra Attack.

## Provenance

Eight Seconds is one blend in a six-blend line. [[Rufio Segalla]] finishes it himself in the back room of [[La Brace]]. He buys the base compound by standing order from [[Marta Orsini]] at [[Studio Orsini]] in [[Le Paludi]].
