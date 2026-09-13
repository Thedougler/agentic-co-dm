---
type: pc
subtype: character-sheet
pc: "jean-claude-tabarnack"
alias: "jc"
pc_level: 5
class_levels: "Ranger (Gloom Stalker) 5"
last_synced: "2026-07-25"
summary: "RAW-baseline derivation of Jean-Claude Tabarnack, Ranger 5 (Gloom Stalker), with satellite pages for stats, abilities, spells, and inventory."
tags: [nature]
uid: d041802b-436e-44fe-a0ee-b9effad0954a
---

No player sheet exists. This is a Ranger 5 (Gloom Stalker) built from official rules (DM updated 2026-07-22). Spells are DM-approved.

Labels: `[theoretical]` = derived, `[assumed]` or `[srd]` = sourced. **Replace this file when a real sheet arrives**.

## What lives here, and what does not

Character details live on separate pages:

| Topic | Page |
|---|---|
| Stats | [[jean-claude-tabarnack-stats\|Stats]] |
| Abilities | [[jean-claude-tabarnack-abilities\|Abilities]] |
| Spells | [[jean-claude-tabarnack-spells\|Spells]] |
| Gear | [[jean-claude-tabarnack-inventory\|Inventory]] |
| Profile | [[jean-claude-tabarnack\|Main page]] |

This file holds only the source notes and the statblock below.

The Arc Note mentions "Level 5 Tongue Lash," but we cannot verify it. No Gloom Stalker or [[grung-npc|Grung]] feature matches it in the SRD or his [[jean-claude-tabarnack-abilities|Abilities]] page.

## Combatant Block

```statblock
# THEORETICAL BASELINE. No character sheet on file; full RAW Ranger 5
# (Gloom Stalker) kit checked this turn against
# vault/srd/classes/ranger.md and
# 5e-srd-ranger-gloom-stalker.md (not memory), plus DM-approved default
# spell picks. The +1 silent shortbow is session-sourced (session 04
# purchase). Replace wholesale when a real sheet lands.
layout: Basic 5e Layout
name: Jean-Claude Tabarnack
size: Small
type: humanoid
alignment: unaligned
ac: 16
hp: 44
speed: "25 ft., climb 25 ft."
stats: [10, 16, 14, 10, 14, 8]
saves: { str: 3, dex: 6 }
damage_immunities: "poison"
condition_immunities: "poisoned"
actions:
  - name: "+1 Silent Shortbow"
    # [assumed Archery] +2 fighting-style bonus baked in here only. Engine
    # flat_to_hit is global, and Archery is ranged-only (Dagger below is
    # unaffected). DEX+3, prof+3, +1 item, +2 Archery = +9.
    desc: "Ranged Weapon Attack: +9 to hit, range 80/320 ft., one target. Hit: 7 (1d6 + 4) piercing damage."
    sim: { id: silent-shortbow }
  - name: "Dagger"
    desc: "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage."
    sim: { id: dagger }
sim:
  side: party
  level: 5
  initiative: 5 # [calculated] DEX +3 + WIS +2 (Gloom Stalker Initiative Bonus, 5e-srd-ranger-gloom-stalker.md)
  resources:
    - { id: ranger_slot_1, max: 4, recharge: long_rest } # [srd] 5e-srd-ranger.md level-5 table
    - { id: ranger_slot_2, max: 2, recharge: long_rest } # [srd] 5e-srd-ranger.md level-5 table
    - { id: dread_ambusher_uses, max: 2, recharge: long_rest } # [srd] = WIS mod (min 1), 5e-srd-ranger-gloom-stalker.md
  abilities:
    # [srd 5e-srd-ranger.md] Level 5: Extra Attack. Standing feature, no rounds key
    - { kind: extra_attack_count, value: 1 }
    # [srd 5e-srd-ranger-gloom-stalker.md] Level 3: Dread Ambusher. Dreadful
    # Strike. Not round-gated (corrects the prior compile's "+1d8, round 1
    # only" guess). A resource-limited on-hit rider, once per turn.
    - { kind: extra_damage, id: dreadful-strike, dice: 2d6, type: psychic, when: on_hit,
        once_per_turn: true, cost: { resource: dread_ambusher_uses, spend: 1 } }
  spellcasting:
    # DC/attack_bonus/ability_mod all derive from WIS mod +2 (8+3+2=13 DC;
    # 3+2=5 attack). Dice come from each spell's own SRD page [srd]; the
    # picks are DM-approved defaults [assumed]. Favored Enemy's 3 free
    # Hunter's Mark casts/long rest aren't modeled. Every cast here costs
    # a 1st-level slot instead (see [[jean-claude-tabarnack-spells|Spells]]).
    - { ability: wis, dc: 13, attack_bonus: 5, level: 5, ability_mod: 2,
        slots: { 1: ranger_slot_1, 2: ranger_slot_2 },
        known: ["Hunter's Mark", "Cure Wounds", "Magic Weapon"] }
  routine:
    action: [silent-shortbow]
```

**Not modeled in the sim:**
Ambusher's Leap speed boost, Umbral Sight, Weapon Mastery, Toxic Secretion, Mortis, Favored Enemy free casts, [[ensnaring-strike|Ensnaring Strike]], [[longstrider|Longstrider]], [[pass-without-trace|Pass without Trace]], [[spike-growth|Spike Growth]] (see [[jean-claude-tabarnack-spells|Spells]] for DM-approved picks).
