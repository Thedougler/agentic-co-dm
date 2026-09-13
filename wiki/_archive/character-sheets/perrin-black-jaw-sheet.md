---
type: pc
subtype: character-sheet
pc: "perrin-black-jaw"
alias: "pbj"
pc_level: 5
class_levels: "Bard 3 (College of Lore) / Warlock 2 (Pact of the Blade)"
last_synced: "2026-07-23"
summary: "D&D Beyond character sheet export for Perrin Black-Jaw at level 5, with source citation and combatant block."
tags: [arcane]
uid: 574044a1-b608-4b7b-a648-54f61306b040
---

Source: `_assets/character-sheets/perrin-black-jaw-character-sheet.pdf` (D&D Beyond export, level 5, replaces the prior level-4 export). Every number below is `[sheet]`, extracted directly from the PDF's fillable form fields (not vision-read text), superseding the earlier DM-directed "safe assumption" compile ([[bard|Bard]] 4/[[warlock|Warlock]] 1) that stood in for this real sheet.

`[verify]` Sheet header lists player as "nickdavenock"; `vault/campaigns/shattered-sea/pcs/perrin-black-jaw.md` frontmatter states `player: Kaden`. Transcribed as printed, contradiction not resolved here (not this skill's territory).

`[verify]` Proficiencies box lists known languages as "Common, Dwarvish, Gnomish"; the [[rattkin|Rattkin]] species trait text on the same sheet describes "Common, Skitter-cant, and one language you choose", which don't match. Transcribed as printed, not reconciled here.

## What lives here, and what does not

The Human-readable transcription lives in `vault/campaigns/shattered-sea/pcs/`, one governed page per
facet, each instantiated from its own Template:

| Facet | Page | Template |
|---|---|---|
| Ability scores, saves, skills, speeds, proficiencies | [[perrin-black-jaw-stats]] | `_templates/pc-stats.md` |
| Traits, features, actions, bonus actions, reactions, feats | [[perrin-black-jaw-abilities]] | `_templates/pc-abilities.md` |
| Spellcasting, cantrips, known/prepared, slots | [[perrin-black-jaw-spells]] | `_templates/pc-spells.md` |
| Attunement, carried gear, caches, currency | [[perrin-black-jaw-inventory]] | `_templates/pc-inventory.md` |
| AC, max HP, class levels, total level | `vault/campaigns/shattered-sea/pcs/perrin-black-jaw.md` frontmatter | `_templates/pc.md` |

This file carries only what those pages cannot: the source citation, the
`[verify]` flags, and the machine-parseable Combatant Block. Restating a
table that already exists on one of the pages above is a duplication defect;
link to it instead.

## Combatant Block

```statblock
layout: Basic 5e Layout
name: Perrin Black-Jaw
size: Small
type: humanoid
alignment: chaotic good
ac: 18
hp: 49
hit_dice: "2d8 + 3d8"
speed: "30 ft., swim 30 ft."
stats: [6, 18, 15, 11, 11, 20]
saves: { str: -1, dex: 5, con: 3, int: 1, wis: 4, cha: 9 }
damage_resistances: "poison"
actions:
  - name: "Longsword (Pact-bonded)"
    desc: "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) slashing damage."
    sim: { id: longsword }
  - name: "Green-Flame Blade"
    desc: "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) slashing damage plus 4 (1d8) fire damage."
    sim: { id: green_flame_blade } # level-5 primary fire rider [sheet+srd vault/srd/spells/evocation/green-flame-blade.md]; splash to a 2nd creature unmodeled
  - name: "Cure Wounds"
    desc: "Perrin touches a creature, restoring 9 (1d8 + 5) hit points."
    sim: { id: cure_wounds, heal: { dice: 1d8+5 }, cost: { resource: bard_slot_1, spend: 1 } }
bonus_actions:
  - name: "Healing Word"
    desc: "Perrin speaks a word of power, restoring 7 (1d4 + 5) hit points to a creature within 60 feet."
    sim: { id: healing_word, heal: { dice: 1d4+5 }, cost: { resource: bard_slot_1, spend: 1 } }
reactions:
  - name: "Cutting Words"
    desc: "When a creature Perrin can see within 60 feet makes an attack roll, ability
      check, or damage roll, he expends a Bardic Inspiration die to subtract it from the roll."
    sim: { id: cutting_words, kind: damage_reduction, die: 1d6, trigger: self_or_ally_hit,
           cost: { resource: bardic_inspiration, spend: 1 } }
  - name: "Pack Tactics Strike"
    desc: "When an enemy hits an ally adjacent to Perrin, he makes one Longsword attack."
    sim: { id: pack_tactics_reaction, kind: extra_attack, attack: longsword,
           trigger: enemy_hits_adjacent_ally, cost: { resource: pack_tactics_reaction, spend: 1 } }
sim:
  side: party
  level: 5
  initiative: 4
  concentration_save: 3
  save_advantage:
    - { vs: poisoned, mode: advantage }
    - { vs: disease, mode: advantage }
    - { vs: str, mode: disadvantage } # Mortis "The Small" — carried from vault/campaigns/shattered-sea/pcs/perrin-black-jaw.md
  resources:
    - { id: bardic_inspiration, max: 5, recharge: long_rest }
    - { id: bard_slot_1, max: 4, recharge: long_rest }
    - { id: bard_slot_2, max: 2, recharge: long_rest }
    - { id: pact_slot_1, max: 2, recharge: long_rest }
    - { id: pack_tactics_reaction, max: 3, recharge: short_rest }
  spellcasting:
    # Two independent pools — bard slots and pact slots never mix.
    # Dice/DCs come from each spell's own SRD page ([srd]); the picks are
    # the sheet's. Heals stay hand-coded above: the sheet's 2014-era
    # export states 1d4+5/1d8+5 and the sheet wins over the 2024 page.
    - { ability: cha, dc: 16, attack_bonus: 8, level: 5, ability_mod: 5,
        source: bard,
        slots: { 1: bard_slot_1, 2: bard_slot_2 },
        known: ["Hideous Laughter"] }
    - { ability: cha, dc: 16, attack_bonus: 8, level: 5, ability_mod: 5,
        source: warlock,
        slots: { 1: pact_slot_1 },
        known: ["Eldritch Blast", "Hex", "Armor of Agathys"] }
  routine:
    action: [longsword]
    bonus: []
    reaction: [cutting_words]
```

Not modeled (listed rather than guessed): Green-Flame Blade's fire splash to a SECOND creature (the engine models the primary target's level-5 fire rider above. The splash needs a two-target-per-swing primitive the engine lacks, and the `[verify]` on the export resolved against [[green-flame-blade|the spell page]]: 1d8 to the target, 1d8+5 to the second creature); [[protection-from-evil-and-good|Protection from Evil and Good]] (narrow creature-type-conditional defense, no general combat-math value); [[silent-image|Silent Image]] (no default mechanical combat effect); [[minor-illusion|Minor Illusion]], [[mage-hand|Mage Hand]] (no combat application); Magical Cunning (out-of-combat slot recovery, irrelevant to a single-encounter sim). Bardic Inspiration granted to allies (a cross-combatant pool grant the engine lacks. Cutting Words models the same 5-die pool) and Scurry positioning. Newly modeled by the v6 engine + spell library: [[eldritch-blast|Eldritch Blast]]'s two level-5 beams, [[armor-of-agathys|Armor of Agathys]]' retaliation clause, Hex and [[hideous-laughter|Hideous Laughter]] as name-referenced library spells with the pact/bard slot economy enforced.
