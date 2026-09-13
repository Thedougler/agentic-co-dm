---
type: pc
subtype: character-sheet
pc: "crissdalynn-khinriss"
alias: "ck"
pc_level: 5
class_levels: "Monk (Way of the Kensei) 5"
last_synced: "2026-07-25"
summary: "Character sheet for Crissdalynn Khinriss, a Kensei Monk, exported from D&D Beyond."
tags: [combat]
uid: 0053a40b-c88e-41b6-91b1-2c7eb5206a6a
---

Source: `_assets/character-sheets/crissdalynn-khinriss-character-sheet.pdf`
(D&D Beyond export, player name "PyonPyonPichu", matches `vault/campaigns/shattered-sea/pcs/players/courtney.md`).
Replaces the prior RAW-baseline theoretical derivation wholesale, per that
file's own instruction. Every `[theoretical]` figure below is now `[sheet]`.

`[verify]` flags on values the sheet prints inconsistently with its own
formulas, transcribed as printed, not silently corrected:

- Unarmed Strike / Flurry of Blows show +8 to-hit, 1d8+5 damage. This is one
  higher than the DEX(+4)+prof(+3)=+7 / +4 the [[quarterstaff|Quarterstaff]] and [[shortbow|Shortbow]]
  lines use. No feature on the sheet explains this bonus. Tavern Brawler's Enhanced Unarmed
  Strike replaces the damage die with 1d4+1, a different damage die rather than a flat modifier.
- Speed prints 35 ft walking / 45 ft flying. [[aarakocra|Aarakocra]] base walk is 30 ft
  and Unarmored Movement adds +10 ft at this level (40 ft expected); the species trait
  states fly speed equals walking speed, so 45 ft doesn't match 35 ft either. Transcribed as printed.
- Faith prints "Great Old Crow" on this sheet. `vault/campaigns/shattered-sea/pcs/crissdalynn-khinriss.md`
  states [[syranita|Syranita]] and [[aerdrie-faenya|Aerdrie Faenya]]
  "in the margins" with [[remnis|Remnis]] primary. This is not necessarily
  contradictory (a folk epithet for one of the above, or an unlinked
  fourth), but flagged for the DM/pcs-page owner rather than silently
  reconciled; this skill doesn't touch `vault/campaigns/shattered-sea/pcs/` content.
- Age prints "5". Not reconciled against her stated backstory (banished at
  14, served a year and ten months aboard the Red Lady). This is likely an
  Aarakocra maturity-scale entry on the D&D Beyond form, not years lived;
  transcribed as printed, not corrected.

## What lives here, and what does not

The Human-readable transcription lives in `vault/campaigns/shattered-sea/pcs/`, one governed page per
facet, each instantiated from its own Template:

| Facet | Page | Template |
|---|---|---|
| Ability scores, saves, skills, speeds, proficiencies | `vault/campaigns/shattered-sea/pcs/stats/crissdalynn-khinriss-stats.md` | `_templates/pc-stats.md` |
| Traits, features, actions, bonus actions, reactions, feats | `vault/campaigns/shattered-sea/pcs/abilities/crissdalynn-khinriss-abilities.md` | `_templates/pc-abilities.md` |
| Spellcasting, cantrips, known/prepared, slots | `vault/campaigns/shattered-sea/pcs/spells/crissdalynn-khinriss-spells.md` | `_templates/pc-spells.md` |
| Attunement, carried gear, caches, currency | `vault/campaigns/shattered-sea/pcs/inventory/crissdalynn-khinriss-inventory.md` | `_templates/pc-inventory.md` |
| AC, max HP, class levels, total level | `vault/campaigns/shattered-sea/pcs/crissdalynn-khinriss.md` frontmatter | `_templates/pc.md` |

This file carries only what those pages cannot: the source citation, the
`[verify]` flags, and the machine-parseable Combatant Block. Restating a
table that already exists on one of the pages above is a duplication
defect; link to it instead.

## Combatant Block

```statblock
layout: Basic 5e Layout
name: Crissdalynn Khinriss
size: Medium
type: humanoid
alignment: neutral
ac: 17
hp: 35
hit_dice: "5d8"
speed: "35 ft., fly 45 ft."
stats: [12, 19, 12, 11, 16, 10]
saves: { str: 4, dex: 7 }
actions:
  - name: "Quarterstaff"
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) bludgeoning damage."
    sim: { id: quarterstaff }
  - name: "Shortbow"
    desc: "Ranged Weapon Attack: +7 to hit, range 80/320 ft., one target. Hit: 8 (1d8 + 4) piercing damage."
    sim: { id: shortbow }
  - name: "Unarmed Strike"
    # [verify] +1 above the Quarterstaff/Shortbow to-hit and damage. See
    # Source note above (Tavern Brawler's Enhanced Unarmed Strike is an
    # alternate 1d4+1 die, not a flat +1; gap unaccounted for on the sheet).
    desc: "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) bludgeoning damage."
    sim: { id: unarmed }
  - name: "Talons"
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage."
    sim: { id: talons }
reactions:
  - name: "Deflect Attacks"
    desc: "When Crissdalynn is hit by a bludgeoning, piercing, or slashing attack,
      she reduces the damage by 1d10 + 9. If she reduces the damage to 0, she can
      spend 1 Focus Point to redirect the force, dealing 2d8 + 4 damage of the
      same type to a creature within 5 feet (melee) or 60 feet (ranged, no total
      cover); that creature can attempt a Dexterity save against DC 14 to avoid
      the redirected damage."
    sim: { id: deflect-attacks, kind: damage_reduction, die: 1d10+9,
           trigger: self_hit, damage_types: [bludgeoning, piercing, slashing],
           redirect: { cost: { resource: ki, spend: 1 },
                       damage: [{ dice: 2d8+4, type: same_as_triggering }],
                       save: { ability: dex, dc: 14 },
                       range_ft: { melee: 5, ranged: 60 } } }
  - name: "Agile Parry"
    desc: "After making an Unarmed Strike as part of the Attack action while
      holding a Kensei weapon and not incapacitated, Crissdalynn gains a +2
      bonus to AC until the start of her next turn."
    sim: { id: agile-parry, kind: ac_bonus, bonus: 2, trigger: after_unarmed_strike_in_attack_action }
sim:
  side: party
  level: 5
  initiative: 4
  resources:
    - { id: ki, max: 5, recharge: short_rest }
  abilities:
    - { kind: bonus_attack, id: flurry-of-blows, attack: unarmed, cost: { resource: ki, spend: 1 } }
    # Stunning Strike [sheet]: spend 1 Focus Point after hitting with a
    # Monk weapon/Unarmed Strike; DC 14 CON or Stunned until the start of
    # her next turn; on a successful save, half speed and the next attack
    # against the target has advantage. The engine's spend decision is the
    # same-turn pool lookahead vs. Flurry (README § Post-hit riders).
    - { kind: post_hit_rider, id: stunning-strike,
        cost: { resource: ki, spend: 1 },
        applies_to: [quarterstaff, unarmed, talons],
        save: { ability: con, dc: 14 },
        once_per_turn: true,
        on_fail: { effects: [{ effect: stunned, duration: { until: start_of_source_next_turn } }] },
        on_success: { effects: [{ effect: speed_halved, duration: { until: start_of_source_next_turn } },
                                { effect: grants_advantage_next_attack }] } }
  routine:
    action: [quarterstaff]
    bonus: [unarmed]
```

Not modeled by the sim (listed rather than guessed): read the Current
(information rider, no damage), [[grappler|Grappler]]/Tavern Brawler's Punch-and-Grab/
Push riders, Slow Fall (falling damage only), Kensei's Shot's extra 1d4
(a ranged-only bonus-action rider. Mutually exclusive with Flurry, it has no
attack-augment-as-bonus-action primitive), Wind Caller's Gust of Wind
(positional shove. The band model has no push primitive; unsourced fence,
awaiting a modelable shape). Newly modeled by the v6 engine: stunning
Strike (both save branches, spend decided by the pool lookahead) and
Deflect Attacks' full redirect chain (damage, save, and range already
specified in the Combatant Block above).
