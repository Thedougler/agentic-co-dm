---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The stat-line format, category defaults, charge/recovery phrasing, and cursed/sentient item patterns the SRD's magic item rules establish."
created: "2026-08-03"
updated: "2026-08-03"
tags: [arcane]
uid: c008f6c5-50a2-4736-ad5d-8b5023f5f059
---

# Item SRD conventions

What the 5e SRD's magic item rules mean for how you write and stat a
homebrew item. Read this when drafting the stat line, choosing a category,
or writing a cursed/sentient item. Rarity/value/crafting-cost numbers stay
in `vault/refs/vault/item/references/rarity-budget.md` — this file doesn't
repeat them.

## Stat line format

Immediately after the read-aloud description, one line:

```text
_[Category] ([subtype, if any]), [Rarity] [(Requires Attunement[ by X])]._
```

Real SRD examples: `_Wondrous Item, Rare (Requires Attunement)._` ·
`_Weapon (Battleaxe, Greataxe, or Halberd), Rare (Requires Attunement)._` ·
`_Armor (Any Light, Medium, or Heavy), Rare (Requires Attunement)._` ·
`_Ring, Uncommon._` · `_Potion, Very Rare._` — the category and subtype
constrain the mechanics that follow; don't invent a category the item
doesn't fit (see below).

## Category defaults (skip stating these unless the item breaks them)

- **Armor** — magic version of mundane [armor](vault/srd/rules/armor-class.md) from Equipment;
  must be worn to function; specify the armor type or roll one if unstated.
- **Potions** — consumable; Bonus Action to drink or administer; takes
  effect immediately and is used up. Mixing two potions risks the Potion
  Miscibility table (SRD) — irrelevant for a single homebrew potion unless
  the scene calls for it.
- **Rings** — must be worn on a finger or similar digit.
- **Rods** — can be used as an
  [Arcane Focus](vault/srd/items/mundane/arcane-focus.md) unless stated
  otherwise.
- **Scrolls** — consumable; reading it activates and destroys it; any
  creature that can understand a written language can attempt to use one.
- **Staffs** — can be used as a nonmagical
  [Quarterstaff](vault/srd/items/mundane/quarterstaff.md) *and* an Arcane
  Focus unless stated otherwise.
- **Wands** — can be used as an Arcane Focus unless stated otherwise.
- **Weapons** — magic version of a mundane weapon; specify the weapon type
  or roll one if unstated; the Ammunition property (if any) makes fired
  ammunition count as magical.
- **Wondrous Items** — the catch-all: wearables (boots, belts, cloaks,
  amulets) and everything else (bags, instruments, figurines).

## Charges, recovery, and "the next dawn"

An item with limited uses states its charge count and recovery explicitly
(the "no bounds stated" mistake in `rarity-budget.md`). SRD
convention: "The [item] regains 1d[X] + [Y] expended charges daily at
dawn." Some items risk destruction on their last charge (SRD pattern: "If
you expend the last charge, roll 1d20. On a 1, the [item] crumbles/is
destroyed") — optional flavor, not required, but a way to make a powerful
charged item feel riskier without changing its rarity.

## Cursed items

A curse is never revealed by casual inspection — only Identify or the act
of attuning reveals it (SRD "Cursed Items"). Attunement to a cursed item
can't be voluntarily ended until the curse is broken
([Remove Curse](vault/srd/spells/abjuration/remove-curse.md) or similar);
removing the item physically does *not* end the curse on its own in most
SRD examples. Real patterns to reuse:

- **[Armor of Vulnerability](vault/srd/items/rare/armor-of-vulnerability.md)**
  — grants Resistance to one physical damage type, but attuning curses the
  wearer with Vulnerability to the other two, revealed only on
  Identify/attunement.
- **[Berserker Axe](vault/srd/items/rare/berserker-axe.md)** — a real
  combat bonus (+1 attack/damage, HP increase) paired with a behavioral
  curse (can't willingly part with the weapon, disadvantage with other
  weapons, forced berserk state on a failed save).
- **[Demon Armor](vault/srd/items/very-rare/demon-armor.md)** — a real
  bonus wrapped in an unremovable-without-magic curse plus a narrative
  drawback (disadvantage against a specific creature type).

The pattern: a cursed item's *upside* should read as genuinely worth
taking before the curse is known — never a trap with no real benefit.

## Sentient items

Only for an item whose PC-connection or narrative draw calls for a
personality of its own — most items are not sentient (single-use items
like potions and scrolls never are). When one is:

- **Abilities** — [Intelligence](vault/srd/rules/intelligence.md)/
  [Wisdom](vault/srd/rules/wisdom.md)/[Charisma](vault/srd/rules/charisma.md),
  either chosen or rolled 4d6 drop-lowest each.
- **Alignment** — pick one, or let it emerge from the item's origin/maker.
- **Communication** — emotion only, full language, or language +
  telepathy with its bearer.
- **Senses** — a fixed perception range (hearing + vision, 30-120 ft.;
  add Darkvision at the high end).
- **Special purpose** — one objective it pursues (aligned/bane/creator-
  seeker/destiny-seeker/destroyer/glory-seeker/lore-seeker/protector/
  soulmate-seeker/templar, SRD table) — this is the item's own toy vector,
  parallel to an NPC's `primary_goal`.
- **Conflict** — the bearer acting against the item's alignment or purpose
  triggers the check below.

> [!mechanic] Sentient item conflict
> Charisma save, DC 12 + the item's Charisma modifier. Failure triggers a
> demand: chase its goals, discard something it hates, give it to someone
> else, keep it close at all times. Refusal escalates to suppressed
> properties or an attempt to Charm the bearer.

Keep a sentient item's demands playable at the table in one sentence, the
same discipline `.claude/skills/composing-beats/references/runtime-surface.md` §3 requires for an
NPC's `consistent_method`.
