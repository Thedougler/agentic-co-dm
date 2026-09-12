---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "CR 5 construct with berserk behavior when bloodied, lightning absorption, and aversion to fire."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Flesh Golem"
found_at:
- "[[shelfworks|Shelfworks]]"
- "[[the-drowned-maw|The Drowned Maw]]"
uid: cd61d2af-1a67-4db9-a1c7-beea67724025
---

# Flesh Golem

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Flesh Golem"
size: Medium
type: construct
alignment: "Neutral"
ac: 9
hp: 127
hit_dice: "15d8 + 60"
speed: "30 ft."
stats: [19, 9, 18, 6, 10, 5]
damage_immunities: "Lightning, Poison"
condition_immunities: "Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned"
senses: "darkvision 60 ft.; Passive Perception 10"
languages: "Understands Common plus one other language but can't speak"
cr: 5
traits:
  - name: "Aversion to Fire"
    desc: "If the golem takes Fire damage, it has Disadvantage on attack rolls and ability checks until the end of its next turn."
  - name: "Berserk"
    desc: "Whenever the golem starts its turn Bloodied, roll 1d6. On a 6, the golem goes berserk. On each of its turns while berserk, the golem attacks the nearest creature it can see. If no creature is near enough to move to and attack, the golem attacks an object. Once the golem goes berserk, it remains so until it is destroyed or it is no longer Bloodied. The golem's creator, if within 60 feet of the berserk golem, can try to calm it by taking an action to make a DC 15 Charisma (Persuasion) check; the golem must be able to hear its creator. If this check succeeds, the golem ceases being berserk until the start of its next turn, at which point it resumes rolling for the Berserk trait again if it is still Bloodied."
  - name: "Immutable Form"
    desc: "The golem can't shape-shift."
  - name: "Lightning Absorption"
    desc: "Whenever the golem is subjected to Lightning damage, it regains a number of Hit Points equal to the Lightning damage dealt."
  - name: "Magic Resistance"
    desc: "The golem has Advantage on saving throws against spells and other magical effects."
actions:
  - name: "Multiattack"
    desc: "The golem makes two Slam attacks."
  - name: "Slam"
    desc: "*Melee Attack Roll:* +7, reach 5 ft. 13 (2d8 + 4) Bludgeoning damage plus 4 (1d8) Lightning damage."
```
