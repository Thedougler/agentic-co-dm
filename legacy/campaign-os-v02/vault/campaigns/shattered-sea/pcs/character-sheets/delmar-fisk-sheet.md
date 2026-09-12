---
type: pc
subtype: character-sheet
pc: "delmar-fisk"
alias: "df"
pc_level: 5
class_levels: "Rogue 5 (Swashbuckler)"
last_synced: "2026-07-26"
summary: "Character sheet for Delmar Atticus Fisk, a Swashbuckler Rogue, exported from D&D Beyond."
tags: [stealth]
uid: b5f94c37-1a64-4918-a037-4ae1f92d699a
---

Source: `_assets/character-sheets/delmar-fisk-character-sheet.pdf` (D&D Beyond
export, 6 pages). This is the first real sheet on file for Delmar, replacing the
prior low-fidelity RAW-derived compile. The PDF has no AcroForm fields
(`pypdf.get_fields()` → none) and each page's filled data is a single
embedded raster image, not selectable text (`pdfplumber` → 0 text values,
1 image per page). Every number below comes from the rendered
page image, not vision-guessed. Skill modifiers cross-check exactly against
their stated Passive scores (Perception/Insight/Investigation 14/14/16 =
10 + the modifier printed for each skill) and against expected math
(prof only vs. Expertise), so the read is arithmetic-confirmed, not
just visual.

`[verify]` The four [[pistol|Pistol]] attack lines print **+5** to hit, 3 lower than
the Blunderbuss/[[dagger|Dagger]] lines' **+8** (all should share DEX +5 + prof
+3 if equally proficient). Transcribed as printed, not silently
corrected; possibly Pistol falls outside whatever specific firearm
prof grants the other three their bonus.

`[verify]` The Weapon Mastery section names [[rapier|Rapier]] (Vex) and [[musket|Musket]]
(Slow) mastery properties, and both a Rapier and a Musket appear under
Equipment, but neither has its own line in the Weapon Attacks & Cantrips
table (only Blunderbuss, 2× Dagger, and 4× Pistol do). Transcribed as
printed, not reconciled.

## What lives here, and what does not

The Human-readable transcription lives in `vault/campaigns/shattered-sea/pcs/`, one governed page per
facet, each instantiated from its own Template:

| Facet | Page | Template |
|---|---|---|
| Ability scores, saves, skills, speeds, proficiencies | [[delmar-fisk-stats]] | `_templates/pc-stats.md` |
| Traits, features, actions, bonus actions, reactions, feats | [[delmar-fisk-abilities]] | `_templates/pc-abilities.md` |
| Spellcasting, cantrips, known/prepared, slots | none ([[rogue\|Rogue]], no spellcasting) | `_templates/pc-spells.md` |
| Attunement, carried gear, caches, currency | [[delmar-fisk-inventory]] | `_templates/pc-inventory.md` |
| AC, max HP, class levels, total level | [[delmar-fisk\|Delmar Atticus Fisk]] frontmatter | `_templates/pc.md` |

This file carries only what those pages cannot: the source citation, the
`[verify]` flags, and the machine-parseable Combatant Block.

## Combatant Block

```statblock
layout: Basic 5e Layout
name: Delmar Fisk
size: Medium
type: humanoid
alignment: chaotic good
ac: 16
hp: 38
hit_dice: "5d8"
speed: "30 ft., fly 30 ft. (Winged Boots), swim 60 ft. (Cloak of the Manta Ray)"
stats: [10, 20, 14, 11, 12, 15]
saves: { dex: 8, int: 3 } # [srd] Core Rogue Traits PHB-2024 129 (Dex/Int) + [calculated]
actions:
  - name: "Blunderbuss (Exandria)"
    desc: "Ranged Weapon Attack: +8 to hit, range 15/60 ft., one target. Hit: 14 (2d8 + 5) piercing damage."
    sim: { id: blunderbuss-exandria }
  - name: "Dagger"
    desc: "Melee or Ranged Weapon Attack: +8 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 7 (1d4 + 5) piercing damage."
    sim: { id: dagger }
  - name: "Pistol"
    desc: "Ranged Weapon Attack: +5 to hit, range 30/90 ft., one target. Hit: 10 (1d10 + 5) piercing damage." # [verify] +5 printed vs. +8 on other DEX weapons
    sim: { id: pistol }
reactions:
  - name: "Uncanny Dodge"
    desc: "When an attacker Delmar can see hits him with an attack roll, he can take a Reaction to halve the attack's damage against him (round down)."
    sim: { id: uncanny-dodge, kind: damage_reduction_pct, fraction: 0.5, trigger: self_hit } # [sheet+srd] PHB-2024 131
sim:
  side: party
  level: 5
  initiative: 7 # [sheet+calculated] DEX +5 + CHA +2 (Rakish Audacity)
  resources:
    - { id: luck_points, max: 3, recharge: long_rest } # [sheet] Lucky feat
  abilities:
    # [sheet+srd] Rogue table, Rogue 5 = 3d6. Rakish Audacity's solo-adjacent
    # Sneak Attack condition (no Advantage needed within 5 ft of an isolated
    # target) is why this stays modeled as always-on/once-per-turn.
    - { kind: extra_damage, id: sneak-attack, dice: 3d6, type: piercing, when: on_hit, once_per_turn: true }
    # [calculated] DC = 8 + DEX mod (5) + prof (3) = 16
    - { kind: trade_dice_for_rider, id: cunning-poison, from: sneak-attack, dice_cost: 1d6,
        save: { ability: con, dc: 16 },
        on_fail: { effects: [{ effect: poisoned, save_ends: { save: con, dc: 16, timing: end_of_turn } }] } }
    - { kind: trade_dice_for_rider, id: cunning-trip, from: sneak-attack, dice_cost: 1d6,
        save: { ability: dex, dc: 16 },
        on_fail: { effects: [{ effect: prone }] } }
    - { kind: movement_boost, id: cunning-action, grants: both } # [srd] PHB-2024 130: Cunning Action (Dash/Disengage)
    - { kind: reroll_take_best, pool: luck_points } # [sheet] Lucky: spend a Luck Point to reroll a missed attack
  routine:
    action: [blunderbuss-exandria]
    reaction: [uncanny-dodge]
```

Not modeled: cunning Strike's Withdraw option (movement rider, no
primitive); Steady Aim (no self-advantage-one-shot primitive); Fancy
Footwork (no per-target Opportunity-Attack-immunity primitive. This sim
has no Opportunity Attack mechanic to suppress at all); Weapon Mastery's
Slow/Vex properties (neither mastered weapon has its own attack line,
`[verify]` above); Tavern Brawler (irrelevant to his real-weapon kit);
Firearm Specialist's misfire reroll and free reload (no misfire mechanic
in this engine). Lucky's other use (impose Disadvantage on an attack
roll against him) isn't modeled. Only the reroll-a-miss half is
(`reroll_take_best`).
