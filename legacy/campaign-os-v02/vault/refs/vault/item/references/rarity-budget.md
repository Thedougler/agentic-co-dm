---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Power benchmarks by item rarity tier, the attunement decision tree, common balance mistakes, and the commodity/guarded/speculative pricing reference."
created: "2026-08-03"
updated: "2026-08-06"
tags: [arcane]
uid: 1cf02932-b2e5-490b-a58c-3270727f2245
---

# Item rarity budget

Power benchmarks for homebrew item rarity. Read this before finalizing any
item's mechanics — set rarity first, design mechanics to fit it, never the
reverse (the Rarity Comes First rule).

Always cite 2 RAW items at the target rarity before finalizing mechanics.
If you cannot name two, read the SRD or ask the DM; guessing a rarity from
vibes is how table balance drifts.

---

## Tier benchmarks

### Common

- No combat relevance whatsoever.
- Cosmetic, quality-of-life, or trivially situational.
- Requires no attunement.
- **RAW examples:** Cloak of Many Fashions, Orb of Direction, Pipe of Smoke Monsters.
- **Power test:** Does this item affect combat at all? If yes, it is at least Uncommon.

### Uncommon

- One meaningful benefit — situational skill advantage, or a minor/conditional
  combat boost.
- Attunement required if: grants attack/damage bonus, negates a combat condition,
  or provides an AC benefit.
- **RAW examples:**
  [Cloak of Elvenkind](vault/srd/items/uncommon/cloak-of-elvenkind.md)
  (advantage on Stealth, no attunement), +1 weapon (attunement),
  [Bag of Tricks](vault/srd/items/uncommon/bag-of-tricks.md) (8 charges,
  one useful random creature/day).
- **Power test:** Is the benefit available every combat round with no resource
  cost? If yes, add attunement or raise to Rare.

### Rare

- One strong benefit useful in most sessions, OR two meaningfully situational
  benefits.
- Always requires attunement if combat-relevant.
- **RAW examples:** +2 weapon,
  [Necklace of Adaptation](vault/srd/items/uncommon/necklace-of-adaptation.md)
  (breathe any atmosphere + [immunity](vault/srd/rules/immunity.md) to the
  Concentration-breaking effect of taking damage),
  [Ring of Evasion](vault/srd/items/rare/ring-of-evasion.md) (1/day negate
  a failed [Dexterity](vault/srd/rules/dexterity.md) save),
  [Periapt of Proof Against Poison](vault/srd/items/rare/periapt-of-proof-against-poison.md)
  (immune to poison damage + advantage on poison saves).
- **Power test:** Does this change how the PC approaches core challenges? →
  Rare. Does it eliminate whole threat categories? → Very Rare.

### Very Rare

- Game-changing; the item redefines the PC's approach to encounters.
- Always requires attunement.
- **RAW examples:** +3 weapon,
  [Cloak of Displacement](vault/srd/items/rare/cloak-of-displacement.md)
  (attackers have disadvantage until you take damage — resets each turn),
  [Ring of Regeneration](vault/srd/items/very-rare/ring-of-regeneration.md)
  (1d6 HP per turn).
- **Power test:** Would removing this item significantly change how the
  character plays encounters? If no, it is not Very Rare.

### Legendary / Artifact

- Campaign-altering; the item IS a campaign thread, not a drop.
- Always requires attunement; always has deep in-world history.
- **RAW examples:** [Vorpal Sword](vault/srd/items/legendary/vorpal-sword.md),
  [Robe of the Archmagi](vault/srd/items/legendary/robe-of-the-archmagi.md).
- **Design rule:** Do not homebrew at this tier without a dedicated DM design
  session — every item this powerful needs a narrative reason the DM signs off
  on beyond "loot," and the standard interview isn't enough scaffolding for
  that conversation.

---

## Attunement decision tree

```text
Does the item grant a bonus to attack rolls, damage rolls, saving throws, or AC?
  -> YES: attunement required.

Does the item have 3 or more distinct powers?
  -> YES: attunement required.

Is the item useful in most combats without consuming a resource (charge/spell slot)?
  -> YES: attunement required.

Is the benefit purely social, travel, or utility with no plausible combat application?
  -> Usually no attunement. But ask: could a creative player weaponize this?
```

## Common balance mistakes

| Mistake | Fix |
|---|---|
| Free attack or damage die with no conditions | Attunement required; likely Rare not Uncommon |
| Three separate mechanics on one item | Pick one; the others are future items (the One-Thing Discipline) |
| "Advantage on all [skill]" with no qualifier | Add "in specific circumstance" or "X/long rest" |
| No range, duration, or charge count stated | Always add explicit bounds |
| Class feature reproduced on a generic item | Use item-native design instead (the Class-Feature Prohibition) |
| Unlimited charges, no recharge | Add "X charges, regains Y charges at dawn" |
| "Immune to [condition]" on Uncommon | Immunity reads as Rare or higher |
| Benefit stacks with itself if carried twice | Add "only one can be attuned at a time" |

## Pricing reference

[Magic as Commodity](vault/campaigns/shattered-sea/cultures/magic-as-commodity.md) is the governing fact: value tracks
manufacturability and market demand, not the item's rarity label. Two tracks
cut across the standard rarity ladder:

- **Commodity** — mass-produced, mechanically simple, no scarce power
  source, real everyday demand. Roughly 1-25 gp. This is most of the magic
  in the world, and it still gets its own item page the moment a story
  names it (the same atomicity rule that governs every other entity).
- **Guarded** — needs a scarce or unique power source, carries real combat
  or political weight, or otherwise resists mass production. Approximate
  gp range by rarity:

| Rarity | Approximate gp range |
|---|---|
| Uncommon | 60-300 |
| Rare | 500-2,000 |
| Very Rare | 5,000-50,000 |
| Legendary | 50,000+ |

Artifact and any nominally "priceless" item still get a real, speculative
`value:` — what the one buyer who wants it badly enough would pay, never
left blank or set to the literal word "priceless."

Set the mandatory `value:` frontmatter key (`vault/_templates/_srd/_item.md`) to the
item's worth in gold whether or not it's actively for sale — it's not
conditional on being listed at a named vendor the way `found_at:` is.
