---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Concrete generation methods for item flavor, single-use relics, and checking a rarity target against the party's level."
created: "2026-08-03"
updated: "2026-08-03"
tags: [craft]
uid: 4200b0fc-e193-4a32-98b5-00ffa7511d8a
---

# Item flavor generation

Concrete generation methods for the parts of an item design that asking the
DM doesn't fully resolve — appearance flavor, single-use relic concepts,
and whether a rarity is plausible for the party to be finding right now.
Sourced from the Lazy GM Resource Document's generator tables. Use these to
sharpen a design already answered by the Interview — never as a substitute
for the PC-Connection Requirement or the One-Thing Discipline.

## Condition + Description + Origin (giving a plain item a distinct voice)

Three independent axes, mixed to avoid a generic flavor description:

- **Condition** — grimy, chipped, ancient, rune-scribed, pulsing, glowing,
  smoldering, crystalline...
- **Description** — ruined, decrepit, obsidian, haunted, unholy, forgotten,
  golden, towering, shattered...
- **Origin** — draconic, dwarven, elven, primeval, divine, unholy, abyssal,
  otherworldly, undead, goblinoid, elemental, gnomish...

Pick one from each (or roll, if the DM wants randomness) and let them
collide against the item's mechanical concept — a *rune-scribed, unholy,
draconic* dagger reads differently than a *smoldering, ancient, dwarven*
one, before a single mechanic is written. This is drafting fuel for the
read-aloud description, not a replacement for it.

## Single-use relics (mundane item + spell effect)

For a single-use magical trinket rather than a full item build: take a
mundane object (amulet, bell, bone, brooch, candle, dagger, figurine, key,
mask, orb, ring, wand, vial — the 50-item LGMRD list, or any object that
fits the scene) and pair it with a single bounded spell effect (magic
missile, cure wounds, guiding bolt, misty step, fireball, dispel magic —
the LGMRD spell lists, or any spell appropriate to the rarity target). This
is the concrete version of item-native design: "stored spell effects (X
charges, cast Y at Zth level)" is exactly this method, named. A relic built
this way is inherently bounded — it casts one spell, a fixed number of
times, then it's spent or recharges.

## Rarity-plausibility sanity check

Before finalizing `narrative_hook`/`current_holder`, check the item's
rarity against what a party at the current level would plausibly be
finding as treasure — the [Gold Per Level table](vault/refs/vault/item/references/treasure-generator.md#gold-per-level).

Uncommon items are the tier explicitly called out as "suitable for
characters of all levels" — if the interview's rarity target is Uncommon,
that's always plausible regardless of party level. A Rare-or-higher item
handed to a 1st-4th level party as an early, low-stakes find is the kind
of mismatch this check catches before the DM Review Gate, not after.

Consumable single-use magic (a bounded relic, per the method above) is a
lighter-weight alternative to a permanent item when the narrative moment
calls for a reward that doesn't need the full rarity-budget conversation —
worth naming to the DM as an option at the Interview stage, not just at
the DM Review Gate.
