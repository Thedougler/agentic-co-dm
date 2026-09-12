---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "A CR 7 construct bound to an amulet, regenerates every turn, and can store spells to cast later."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[shelfworks|Shelfworks]]"
- "[[crown-islands|Crown Islands]]"
statblock: inline
name: "Shield Guardian"
uid: 571b367f-04d8-4a63-916c-8226cb311c32
---

# Shield Guardian

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Shield Guardian"
size: Large
type: construct
alignment: "Unaligned"
ac: 17
hp: 142
hit_dice: "15d10 + 60"
speed: "30 ft."
stats: [18, 8, 18, 7, 10, 3]
damage_immunities: "Poison"
condition_immunities: "Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned"
senses: "blindsight 10 ft., darkvision 60 ft.; Passive Perception 10"
languages: "Understands commands given in any language but can't speak"
cr: 7
traits:
  - name: "Bound"
    desc: "The guardian is magically bound to an amulet. While the guardian and its amulet are on the same plane of existence, the amulet's wearer can telepathically call the guardian to travel to it, and the guardian knows the distance and direction to the amulet. If the guardian is within 60 feet of the amulet's wearer, half of any damage the wearer takes (round up) is transferred to the guardian."
  - name: "Regeneration"
    desc: "The guardian regains 10 Hit Points at the start of each of its turns if it has at least 1 Hit Point."
  - name: "Spell Storing"
    desc: "A spellcaster who wears the guardian's amulet can cause the guardian to store one spell of level 4 or lower. To do so, the wearer must cast the spell on the guardian while within 5 feet of it. The spell has no effect but is stored within the guardian. Any previously stored spell is lost when a new spell is stored. The guardian can cast the spell stored with any parameters set by the original caster, requiring no spell components and using the caster's spellcasting ability. The stored spell is then lost."
actions:
  - name: "Multiattack"
    desc: "The guardian makes two Fist attacks."
  - name: "Fist"
    desc: "*Melee Attack Roll:* +7, reach 10 ft. 11 (2d6 + 4) Bludgeoning damage plus 7 (2d6) Force damage."
```
