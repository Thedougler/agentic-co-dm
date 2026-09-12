
# Draft — Item

A homebrew or reskinned magic item. Done means one mechanic done excellently, balanced against real RAW benchmarks, tied to a PC's story.

## Template

`vault/_templates/_srd/_item.md` — copy it, never retype it from memory.
Confirmed, not reforked, against the Forgotten Realms Wiki's own
item-article shape (infobox/stat-line, Powers, ownership history) —
that's the stat-line paragraph, `## Mechanics`, and `## Provenance` below.
Fixed headings, both OPTIONAL per the template's own
conditions.

Before drafting a new item from scratch, check `find-item` for an
existing freely-licensed magic item to vendor instead of inventing one —
only write original mechanics once that check and the stub check below
come back empty.

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — an item never decides, feels, thinks, or wants (the Player Character Boundary).
3. `vault/refs/vault/_common/hard-rules.md` — the shared and mechanical-type rules bind this type, never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now and paste it; a same-effect RAW item always wins over homebrew.

`DI1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **The One-Thing Discipline.** Designing three things adequately instead of one thing excellently -> stop, pick the one; the rest are future items.
- **The Rarity Comes First.** Before mechanics -> read `vault/refs/vault/item/references/rarity-budget.md`, name the target rarity, design to fit it. Cite 2 RAW items at that rarity; clearly stronger -> raise the rarity, don't shrink the citation.
- **The Class-Feature Prohibition.** Reproducing a class-exclusive feature (Sneak Attack, Rage, Ki abilities, Bardic Inspiration, [[divine-smite|Divine Smite]], Extra Attack beyond the PC's class) -> redesign item-native: rest-recovering charges, stored spell effects, check bonuses, AC/resistance/immunity.
- **The Attunement Decision Tree.** Setting `attunement` -> run `vault/refs/vault/item/references/rarity-budget.md` § Attunement decision tree: any attack/damage/save/AC bonus, or 3+ distinct powers, requires it.
- **The DM Review Gate.** Flipping `status:` to `pending` -> present the one thing, rarity justification, and RAW benchmarks; wait for approval, else leave `status: draft`.
- **Inventions and Vehicles.** An invention or piece of technology is an item; a vehicle is a `ship` (`.claude/skills/draft-content/references/ship.md`), whatever it travels through.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- The **one thing** in one sentence? Can't answer -> not ready to generate.
- Rarity target — Common / Uncommon / Rare / Very Rare / Legendary?
- Found, gifted, bought, stolen, inherited — sold by a named NPC, or tied to a location?

Sharpen with `vault/refs/vault/item/references/flavor-generation.md`.

## Item Toy

Six fields, one table after the stat line, no heading of its own: `one_thing`, `rarity_justification`, `attunement_reason`, `pc_connection`, `current_holder`, `narrative_hook`. Fields: `vault/refs/vault/item/references/toy.md`; layout/handoffs: `vault/refs/vault/item/references/output.md`; frontmatter: `vault/refs/vault/item/references/frontmatter.md`.

## Before you ship

[[vault/refs/vault/_common/lifecycle|Lifecycle]] `vault/refs/vault/_common/lifecycle.md` · gaps `vault/refs/vault/_common/degrade.md` · handoffs `vault/refs/vault/_common/handoffs.md` · boundaries `vault/refs/vault/_common/out-of-scope.md` · then `vault/refs/vault/_common/checklist.md` and `vault/refs/vault/item/references/checklist.md`.

## Reference files

| File | Read when |
|---|---|
| `vault/refs/vault/item/references/rarity-budget.md` | Rarity, RAW benchmarks, attunement tree |
| `vault/refs/vault/item/references/srd-conventions.md` | Stat line, category, cursed/sentient items |
| `vault/refs/vault/item/references/flavor-generation.md` | Flavor, relics, rarity vs. party level |
| `vault/refs/vault/item/references/toy.md` | Filling any Item Toy field |
| `vault/refs/vault/item/references/output.md` | Headings, cross-skill handoffs |
| `vault/refs/vault/item/references/frontmatter.md` | `rarity`, `attunement`, `form`, `found_at`, `value` |
| `vault/refs/vault/item/references/example.md` | A full worked page |
| `vault/refs/vault/item/references/treasure-generator.md` | Random tables and gold-parcel guidelines for awarding coin, consumable magic items, and permanent magic items by character level in a fantasy RPG. |
