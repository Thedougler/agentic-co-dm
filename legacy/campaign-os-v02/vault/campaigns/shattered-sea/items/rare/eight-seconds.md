---
type: item
status: pending
publish: false
title: ""
aliases: []
summary: "An alchemical cigarette that burns for about eight seconds, granting one extra action per turn for two consecutive turns before dropping the smoker prone and unable to react."
created: 2026-08-01
updated: 2026-08-11
tags: [intrigue]
tier: supporting
source: ""
rarity: rare
attunement: false
unique: false
form: consumable
found_at: ["[[la-brace|La Brace]]"]
value: "700 gp"
campaigns: [Shattered Sea]
owner_skill: ".claude/skills/draft-content/references/item.md"
uid: 63e45ad6-7715-4f8d-aa51-b5faa7dde25b
---

# Eight Seconds

> [!read-aloud]
> The cigarette lies thin and pale between two fingers, its paper wound tighter than anything else on Rufio's shelf.
>
> A struck match brings it to the tip, and the paper catches all at once, a bright line racing away from the fingers holding it.
>
> Smoke lifts off it in one steady ribbon and thins to nothing before it reaches shoulder height.
>
> The last third burns fast. The ember eats the final inch while the fingers still feel cool.

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

*Consumable, Rare.*

| Field | Detail |
|---|---|
| `one_thing` | For about eight seconds after lighting, the smoker gains one extra action on the current turn and on the next turn, then falls prone and loses reactions until their following turn ends. |
| `rarity_justification` | Rare, comparable to Potion of Invulnerability (resistance to all damage for 1 minute) and [[potion-of-heroism\|Potion of Heroism]] (10 temporary hit points plus a 1-hour [[bless\|Bless]] effect). None of the three requires attunement. Eight Seconds borrows [[haste\|Haste]]'s extra-action shape at a much smaller scale: it lasts two rounds where Haste lasts ten. Speed, AC, and [[dexterity\|Dexterity]] saves stay the same, and the burn ends by dropping the smoker prone with reactions gone for a turn. That smaller shape keeps Eight Seconds at Rare, below [[potion-of-speed\|Potion of Speed]]'s Very Rare tier. |
| `attunement_reason` | No attunement required: a single-use consumable with one power, and no bonus to attack, damage, save, or AC rolls. |
| `pc_connection` | [[jean-claude-tabarnack\|Jean-Claude Tabarnack]]. His cover holds only while nothing forces him to fight in the open, and Eight Seconds buys him two rounds to disappear before anyone works out what they just watched. |
| `current_holder` | [[rufio-segalla\|Rufio Segalla]] rolls this one to order at [[la-brace\|La Brace]], a [[velo-quarter\|Velo Quarter]] smoking room in [[calveno\|Calveno]]. He never keeps it on the shelf. |
| `narrative_hook` | Buying it requires an hour seated in the room first, and Rufio names the price only afterward. It never appears on [[la-gatta\|La Gatta]]'s board. |

## Mechanics

**[HB]** Lighting Eight Seconds and taking its first breath costs a [[bonus-action|Bonus Action]]. It affects only the smoker, and it keeps burning through the end of the smoker's next turn. It has no recharge: this is a single-use item, gone the instant it burns out.

On the turn you light it and on your next turn, you gain one extra action. You can spend that extra action only on the [[attack|Attack action]] (one weapon attack only), [[dash|Dash]], [[disengage|Disengage]], [[hide|Hide]], or [[utilize-action|Use an Object]]. It burns out. At the end of your second turn when it does, you fall [[prone|prone]] and can't take [[reaction|reactions]] until the end of your following turn.

Edge cases:

- The extra action is not a bonus action. You can't spend it on a bonus action or on casting a spell.
- The single weapon attack it allows ignores Extra Attack.
- You fall prone when the cigarette burns out, used the extra actions or not.
- Lighting a second Eight Seconds while the first still burns does nothing, and wastes the second cigarette outright.

**Limitations.** Eight Seconds grants no bonus to attack rolls, damage rolls, saving throws, or AC, and its extra action can't fuel a bonus action, a spell, or a second weapon attack through Extra Attack.

## Provenance

Eight Seconds is one blend in a six-blend line. [[rufio-segalla|Rufio Segalla]] finishes it himself in the back room of [[la-brace|La Brace]]. He buys the base compound by standing order from [[marta-orsini|Marta Orsini]] at [[studio-orsini|Studio Orsini]] in [[le-paludi|Le Paludi]].
