---
type: monster
status: canon
publish: false
aliases: []
summary: "A CR 7 fey hag whose supernatural charm turns victims into loyal, permanent thralls."
created: 2026-07-30
updated: "2026-08-09"
tags: [horror]
tier: supporting
source: ""
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[midchain-west|Midchain West]]"
habitat: [Coastal, Forest]
statblock: inline
name: "Gentle Hag"
cr: 7
ac: 16
hp: 102
str: 14
dex: 16
con: 18
int: 17
wis: 15
cha: 19
campaigns: [Shattered Sea]
owner_skill: ".claude/skills/draft-content/references/monster.md"
uid: b372e094-687a-4d08-a751-962d50ce46d1
---

# Gentle Hag

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Gentle Hag"
size: Medium
type: fey
alignment: Typically Chaotic Neutral
ac: 16
hp: 102
hit_dice: 12d8 + 48
speed: "30 ft."
stats: [14, 16, 18, 17, 15, 19]
saves:
  - charisma: 7
skillsaves:
  - deception: 7
  - insight: 5
  - perception: 5
  - persuasion: 7
damage_resistances: "Necrotic, Psychic; Bludgeoning, Piercing, and Slashing from Nonmagical Attacks"
condition_immunities: "Charmed"
senses: "Darkvision 120 ft., Passive Perception 15"
languages: "Common, Halfling, Sylvan"
cr: "7"
traits:
  - name: "Fey Clarity"
    desc: "Immune to all Enchantment school spells."
  - name: "Persistent Charm"
    desc: "A creature that has been Charmed by the Gentle Hag for 24 or more hours cannot make saving throws to end the charm. It lasts until the hag dies or Greater Restoration is cast on the target."
  - name: "Joyous Loyalty"
    desc: "A creature Charmed by the hag within 5 feet of the hag or an attacker can redirect any attack meant for the hag to itself."
  - name: "Magic Resistance"
    desc: "Advantage on saving throws against spells and other magical effects."
spells:
  - "CHA-based spellcasting (spell save DC 15, +7 to hit). Requires no material components."
  - "At will: Command, Guiding Bolt, Sleep"
  - "3/day each: Blur, Hold Person, Misty Step, Suggestion"
  - "2/day each: Counterspell, Slow"
actions:
  - name: "Painful Glamor"
    desc: "Ranged Spell Attack: +7 to hit, range 60 ft. Hit: 11 (2d6+4) Psychic damage, plus 1 additional Psychic damage per charmed creature within 120 feet of the hag."
  - name: "Gentle Charm"
    desc: "One creature within 30 feet that can see the hag makes a DC 15 Charisma saving throw or is Charmed until the hag dies or the target reaches 0 HP. At the end of each of its turns, the target can repeat the save (DC increases by 1 for each prior failure, resets if target takes damage). After 24 hours, Persistent Charm applies."
  - name: "Gentle Push"
    desc: "Grant one Charmed creature 5 (1d10) temporary HP and an additional weapon attack on its next turn."
  - name: "Summon Happiness (1/Day)"
    desc: "Choose up to 1d6+1 Charmed creatures anywhere. Teleport them to within 60 feet of the hag."
```

**Wants:** to grow her household of charmed thralls without ever raising a hand herself, letting Gentle Charm and Persistent Charm do the patient work while she plays the grateful host.
**Morale:** never breaks and runs; past half HP she leans on Siphon Joy, spending thralls to heal, and only disengages once every thrall present is spent or dead.

### Coven Actions (requires 2 other hags within 30 ft.)

- **Shared Spellcasting:** 3/day: [[alarm|Alarm]], [[bless|Bless]], [[calm-emotions|Calm Emotions]], [[charm-person|Charm Person]]; 2/day: [[beacon-of-hope|Beacon of Hope]], [[counterspell|Counterspell]], [[hallucinatory-terrain|Hallucinatory Terrain]], [[haste|Haste]]; 1/day: [[dominate-person|Dominate Person]], [[heroes-feast|Heroes' Feast]], [[mass-cure-wounds|Mass Cure Wounds]], [[modify-memory|Modify Memory]].
- **Gentle Gaze:** Create a magic item (10,000 gp, 1 hour). User can see through it to read a target's deepest desire.

> [!mechanic]
> **Siphon Joy.** Sacrifice a [[charmed|Charmed]] thrall: DC 15 [[constitution|Constitution]] save (disadvantage if charmed 24+ hours). Deals half the thrall's max HP as force damage; each coven hag heals for one-third of this.

## Description

A fey hag that specializes in persistent charm. Once the initial resistance is worn down, the Gentle Hag's victims become permanent retainers — joyful, loyal, and impossible to free without high-level magic. She tends her charmed household herself, warm meals and real comfort, offering genuine protection to those she has already caught. The horror is not that she is cruel. It is that she is not. A related variant, the Haunt Hag, comes from the same fey lineage, though none has turned up in the [[shattered-sea|Shattered Sea]] yet.

## Ecology

The Gentle Hag keeps to deep forest interior, well back from patrolled anchorages — the forested highlands behind [[crown-islands|Crown Islands]]' coastal forts, or the tangled tree cover of [[midchain-west|Midchain West]]. She settles near a freshwater spring or tidal creek close enough to shore to draw in castaways, deserters, and anyone separated from a crew, but far enough inland that no fort's cannon range reaches her door. She does not hunt; she waits, and she keeps every charmed thrall fed, sheltered, and safe from the forest's other predators, tallying each one's comfort the way she'd tally coin. Other hags of her kind, the Haunt Hag chief among them, are drawn to the same quiet, unpatrolled corners of the world, though a coven only forms where the surrounding ground can feed and hide all its members at once.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Break a thrall's charm mid-fight ([[remove-curse\|Remove Curse]], [[greater-restoration\|Greater Restoration]], or the hag's death) | Thrall still within 5 ft. of the hag when the charm breaks | The thrall's borrowed devotion collapses into real terror; it flees or turns on the hag outright, and Joyous Loyalty can no longer redirect attacks through it | [[jean-claude-tabarnack\|Jean-Claude Tabarnack]] |
| Question a charmed thrall about the coven before Persistent Charm locks in | Thrall has been charmed under 24 hours | It answers warmly and completely, naming the other hags' haunts, before its borrowed loyalty catches up with what it just did | [[midchain-west\|Midchain West]] |
