---
type: monster
status: draft
publish: false
aliases: []
summary: "Blight-corrupted moth swarm generating a 30-foot silence field, suffocating prey in the deep Aruhe interior."
created: "2026-08-15"
updated: "2026-08-15"
tags: [combat, horror]
tier: supporting
found_at:
- "[[aruhe|Aruhe]]"
- "[[midchain-east|Midchain East]]"
habitat: [Forest]
statblock: inline
name: "Silence Moths"
cr: 8
ac: 13
hp: 105
str: 3
dex: 16
con: 12
int: 1
wis: 10
cha: 1
campaigns: [Shattered Sea]
source: ""
source_url: ""
reference_image: ""
owner_skill: ".claude/skills/draft-content/references/monster.md"
uid: 8cf67dec-f116-4c42-bbc3-46acdf273a67
---

# Silence Moths

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Silence Moths"
size: Huge
type: swarm of Tiny monstrosities
alignment: unaligned
ac: 13
hp: 105
hit_dice: "14d12 + 14"
speed: "0 ft., fly 40 ft. (hover)"
stats: [3, 16, 12, 1, 10, 1]
damage_resistances: "bludgeoning, piercing, slashing"
condition_immunities: "charmed, frightened, grappled, paralyzed, petrified, prone, restrained, stunned"
senses: "blindsight 30 ft. (blind beyond this radius), passive Perception 10"
languages: "—"
cr: 8
traits:
  - name: "Silence Aura"
    desc: "The swarm generates a 30-foot-radius sphere of magical silence centered on itself. No sound can be created within or pass through the area. Casting a spell that requires a verbal component is impossible within the area."
  - name: "Swarm"
    desc: "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny insect. The swarm can't regain hit points or gain temporary hit points."
  - name: "Suffocating Cloud"
    desc: "A creature that starts its turn in the swarm's space must succeed on a DC 14 Constitution saving throw or begin suffocating as moths fill its nose and mouth. A suffocating creature can hold its breath for a number of rounds equal to its Constitution modifier (minimum 1 round) before it drops to 0 hit points. Removing itself from the swarm's space ends the effect."
actions:
  - name: "Engulf"
    desc: "Melee Weapon Attack: +6 to hit, reach 0 ft., one target in the swarm's space. Hit: 21 (6d6) piercing damage, or 10 (3d6) piercing damage if the swarm has half its hit points or fewer."
```

## Description

A cloud of pale moths the size of a ship's sail, drifting through the canopy in absolute silence. The jungle's ambient noise dies a full thirty feet ahead of the swarm, so the first sign of approach is the absence of everything else. Individual moths are thumb-sized and colorless. Together they blot out the canopy light and fill the air thick enough to choke on.

## Ecology

Moths do not swarm like this. The [[blight|Blight]]'s corruption bound thousands of individuals into a single hunting body, coordinated without sound, steering by vibration alone. The silence is the hunting method. A party inside the aura cannot coordinate, cannot cast verbal spells, and cannot call for help when the cloud settles over them.

Home zones: [[aruhe-the-rot|the Rot]] into [[aruhe-the-hunger|the Hunger]]. The swarms drift the deep interior at dusk and dawn, following the same corridors through the canopy. Fire drives them off. They do not pursue prey that leaves the tree cover.
