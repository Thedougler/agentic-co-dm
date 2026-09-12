# Spell Design Reference

Read this when `rule-prep`'s interview establishes a homebrew spell (a
`subtype: subsystem` rule page — spells have no dedicated skeleton subtype
of their own; see `.claude/skills/rule-prep/SKILL.md` § Subtype routing). Mined from the legacy
`dnd5e-homebrew` skill's spells.md (since removed from the repo).

## The three axes

Every spell balances across three axes — strong on one means weaker on the
others:

1. **Output** — damage, healing, conditions applied.
2. **Scope** — single target vs. area, self vs. others, range.
3. **Cost** — action type, concentration, material cost, range limits.

## Damage benchmarks

| Slot | Instant (no conc) | Concentration (per turn) | Non-concentration |
|---|---|---|---|
| Cantrip | 1d10 (scales at 5/11/17) | — | — |
| 1st | 4d6 (Magic Missile-tier, guaranteed) | 2d6 | 2d8 |
| 2nd | 5d6 | 3d6 | 3d8 |
| 3rd | 8d6 | 4d6 | 5d8 |
| 4th | 10d6 | 6d6 | 7d8 |
| 5th | 12d6 | 8d6 (rare) | 9d8 |
| 6th | 14d6 | — | 11d8 |
| 7th | 16d6 | — | 13d8 |
| 8th | 18d6 | — | 15d8 |
| 9th | 10d12 / 20d6 | — | 17d8 |

Area-of-effect damage discounts per the number of targets it plausibly
hits: a 20-ft radius divides by ~1.5 (assume ~4 targets), a 60-ft cone by
~1.3 (assume ~3), a line by ~1.2. Target 60–70% of the equivalent
single-target spell at the same slot. Fireball (3rd, 8d6, 20-ft radius,
Dex save) is the gold-standard AoE comparable — cite it directly when
justifying a new AoE spell's slot.

## Control/CC benchmarks

Hard CC (the target can't act) must be concentration, short duration, or
limited-target — never all three absent at once:

| Effect | Appropriate slot | Note |
|---|---|---|
| Prone | 1st | Trivially broken by standing; weak |
| Restrained | 2nd | Strong, often paired with damage |
| Stunned | 3rd+ | Very strong, usually concentration |
| Incapacitated | 2nd–3rd | Depends on duration/repeat-save |
| Paralyzed | 5th | Concentration, auto-crit on melee hits |
| Petrified | 6th+ | Extremely strong; reserve for high level |
| Dominated | 4th+ | Using an enemy's own turn is strong on its own |
| Sleep-style auto-incapacitate | 1st | HP ceiling is the balance lever |

Save type shapes power: Wisdom saves are weak for most monsters (strong
choice for a PC-facing spell); Constitution saves are common and monsters
are decent at them (use for damage/DoT); Intelligence saves are weak for
most monsters (fine for low-slot control). **Any CC lasting past 1 minute
needs a repeat save at the end of each of the target's turns.**

## Utility benchmarks

| Effect | Slot equivalent | Note |
|---|---|---|
| Detect magic / Identify | Ritual 1st | Weak; ritual tag compensates |
| Invisibility (1 min, conc) | 2nd | Breaks on attack |
| Fly (10 min, conc) | 3rd | Strong mobility, concentration-taxed |
| Greater Invisibility | 4th | Strong — attacking doesn't break it |
| Teleport | 7th | No combat use; huge campaign-scale utility |
| True Seeing | 6th | Niche but powerful, 10-min concentration |

The ritual tag adds ~10 min casting time but removes the slot cost — a
non-combat effect can be stronger than its slot equivalent suggests when
ritual-tagged, since it's never competing for a combat-round action.

## Healing benchmarks

Healing runs weak relative to damage by design in 5e:

| Slot | Immediate | Note |
|---|---|---|
| 1st | 1d8+mod, or 2d4 as a bonus action (Healing Word-tier) | Bonus-action healing is strong enough that action-cost Cure Wounds-tier spells are mostly obsolete at most tables — factor this into any new healing spell's value |
| 2nd | 1d4+mod to 6 targets as a bonus action | |
| 3rd | 3d8+8, or 2d6/turn for 1 min (aura-style) | |
| 4th | 4d8+mod | |
| 5th | 3d8+mod to 6 targets | |

## Upcast scaling

Every damage spell needs an "at higher levels" entry: +1 slot ≈ +1d6/+1d8
damage, or +1 target, or +10 ft range. Control spells scale by +1 target
per slot, or an extended duration interval. Healing scales +1d8 per slot.

## Concentration tax

Concentration is worth roughly 30% less raw power than the equivalent
non-concentration effect would be, because damage can end it, it competes
with a caster's other concentration spells, and a competent opponent
targets the concentrating caster directly. **A spell that is
non-concentration, ongoing, AND strong on all three at once is almost
certainly overtuned** — cut one axis.

## Spell school expectations

| School | Expected theme |
|---|---|
| Evocation | Direct damage — should excel here, nothing else |
| Conjuration | Summoning/teleportation — summons are balanced by the action cost to command them |
| Abjuration | Protection/dispelling — defensive power, weaker offensively |
| Enchantment | Mind effects — CC, usually Wisdom saves |
| Illusion | Fakery — should require an Insight/Investigation check to disbelieve, circumventable |
| Divination | Information — low combat power, high table impact |
| Necromancy | Death/undead — DoT, debuffs, undead summons |
| Transmutation | Shape-change/buffs — broad; watch for a spell that "does everything" |

## Red flags

- Non-concentration + long duration + strong condition (a non-concentration
  Banishment-tier effect is broken).
- Ritual tag stacked with a strong combat effect — ritual means free;
  combat power shouldn't be.
- "Reroll any d20" at a low spell slot — already a very strong feat-tier
  effect (Lucky), doesn't belong at 1st–2nd level.
- Damage + hard CC in the same instance at low levels — pick one.
- An AoE with no save and no attack roll at low levels.
- Stacking with itself across multiple castings.
- "All willing creatures within 30 ft" for a strong buff — trivially
  maximized at most tables, treat as a much larger action than it looks.
