---
type: monster
status: canon
publish: false
aliases:
- Blue-Caste Handler
- Purple-Caste Warrior
summary: "Blue-caste handlers and purple-caste warriors — the ranged security backbone of Simone Tabarnack's grung raid operations at the Calveno sewer magazines."
created: 2026-07-30
updated: 2026-08-09
tags: [combat]
tier: supporting
source: ""
found_at:
- "[[verdant-teeth|Verdant Teeth]]"
- "[[midchain-north|Midchain North]]"
habitat: [Forest, Urban]
statblock: inline
name: "Grung Elite Warrior"
cr: 2
ac: 13
hp: 49
str: 7
dex: 16
con: 15
int: 10
wis: 11
cha: 12
campaigns: [Shattered Sea]
owner_skill: ".claude/skills/draft-content/references/monster.md"
uid: f8e4bfa6-d6c0-4d7b-b6e8-e76a91993a1c
---

# Grung Elite Warrior

CR 2 humanoid grung. Blue-caste handlers and purple-caste warriors — the muscle and the eyes behind [[simone-tabarnack|Simone]]'s raids, holding the tunnels and the blackpowder she needs kept quiet until the day it isn't. The dungeon they garrison, [[calveno-sewers-grung-magazines|Calveno Sewer Magazines]], is itself `status: pending`.

Elite warriors serve two roles in the [[calveno-sewers-grung-magazines|Calveno sewer network]]: Blue-caste handlers (secondary sites) coordinate sentry teams of 2 green-caste laborers with standing orders to hide-and-report; the handler fights only to cover the laborers' escape, then retreats, opening with shortbow from concealment and using Standing Leap to reposition across water channels. Purple-caste warriors (primary site) are shoot-on-sight security who open from concealment with hand crossbow (use shortbow stats), use Mesmerizing Chirr if two or more targets cluster within 15 ft, then focus fire on stunned targets, fighting from elevated positions (scaffolding, ledges) to exploit ranged advantage. Blue-caste breaks at half HP or if the magazine is compromised; purple-caste at the primary site fights to the death to protect the summoning circle.

> [!mechanic]
> **Mesmerizing Chirr, staggered.** Recharge 6, DC 12 [[wisdom|Wisdom]] save; fail and the target is stunned until the grung's next turn. With 4 Elite Warriors in the primary chamber, up to 4 stun attempts are possible if the fight runs long — the first warrior fires it round 1, the rest hold theirs rather than stacking saves on one turn. [[perrin-black-jaw|Perrin]] loses concentration on [[hideous-laughter|Hideous Laughter]] on a failed save, which flips the fight's tempo hard.

Related:

- [[grung|Grung (Lore)]]
- [[grung-clans|Grung Clans (Faction)]]
- [[calveno-sewers-grung-magazines|Calveno Sewer Magazines]] — Room 3 carries an inline stat excerpt of this creature (`e484ffa` precedent); this page is the canonical statblock home.
- [[grung-npc|Grung (Green-Caste NPC)]] and Grung Wildling — sibling bestiary/NPC entries named in the source's own related section. Grung (Green-Caste NPC) landed R36; live-linked per finalize-time forward-linking. Grung Wildling has no page yet in this wiki (see queue file `archive/2026-07/ss11-creature-grung-elite.md`).
- [[calveno|Calveno]] — Beffa Grung Raid — source session/encounter page named in the source's own related section. No page exists for it yet in this wiki (see queue file above).

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Grung Elite Warrior"
size: Small
type: humanoid
subtype: grung
alignment: Typically Lawful Evil
ac: 13
ac_note: natural armor
hp: 49
hit_dice: 9d6 + 18
speed: "25 ft., Climb 25 ft."
stats: [7, 16, 15, 10, 11, 12]
saves:
  - dexterity: 5
skillsaves:
  - athletics: 2
  - perception: 2
  - stealth: 5
  - survival: 2
damage_immunities: "poison"
condition_immunities: "poisoned"
senses: "Passive Perception 12"
languages: "Grung"
cr: "2"
traits:
  - name: "Amphibious"
    desc: "The grung can breathe air and water."
  - name: "Poisonous Skin"
    desc: "Any creature that grapples the grung or otherwise comes into direct contact with the grung's skin must succeed on a DC 12 Constitution saving throw or become poisoned for 1 minute. A poisoned creature no longer in direct contact with the grung can repeat the saving throw at the end of each of its turns, ending the effect on a success."
  - name: "Standing Leap"
    desc: "The grung's long jump is up to 25 feet and its high jump is up to 15 feet, with or without a running start."
actions:
  - name: "Multiattack"
    desc: "The grung makes two attacks with its dagger or shortbow."
  - name: "Dagger"
    desc: "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage plus 5 (2d4) poison damage."
  - name: "Shortbow"
    desc: "Ranged Weapon Attack: +5 to hit, range 80/320 ft., one target. Hit: 6 (1d6 + 3) piercing damage plus 5 (2d4) poison damage."
  - name: "Mesmerizing Chirr (Recharge 6)"
    desc: "The grung makes a chirring noise to which grung are immune. Each humanoid or beast within 15 feet of the grung that can hear it must succeed on a DC 12 Wisdom saving throw or be stunned until the end of the grung's next turn."
```

```meta-bind-button
label: ⚔ Sim vs Party
style: primary
action:
  type: command
  command: obsidian-shellcommands:shell-command-simvsparty
```

## Description

Purple-caste warriors and blue-caste handlers stand out from a rank-and-file grung by weapon discipline and gear: hand crossbow or shortbow slung for ranged work, a venom-coated dagger for the follow-up, and hide harness cut for scaffolding and flooded tunnels alike. Their caste coloring marks the role at a glance — deep violet for warriors bred to fight, blue-grey for handlers who mind slave labor rather than lead it.

## Ecology

Elite warriors are drawn from the Purple and Blue lines of [[grung|grung]] caste society — the warrior and handler castes that traditionally police and administer [[grung-clans|Grung Clans]] territory. Like every grung, they're amphibious and must submerge for at least an hour every day or take on [[exhaustion|Exhaustion]], a habit that keeps them tethered to flooded channels and reef shallows even when posted far from the reef-fringed rainforest of the [[verdant-teeth|Verdant Teeth]]. Garrisoned in the [[calveno-sewers-grung-magazines|Calveno sewer magazines]], the same hierarchy holds: warriors take the exposed, elevated posts, handlers stay close to the laborers they're answerable for.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Sever a handler's escape route across the water channels | Handler is using Standing Leap to disengage after covering the laborers' retreat | Handler is boxed in and keeps fighting the covering action instead of disengaging, opening a window before it can retreat again | [[calveno-sewers-grung-magazines\|Calveno Sewer Magazines]] |
| Force a warrior off its elevated post | Warrior is firing from scaffolding or a ledge to keep ranged advantage | Warrior leaps down with Standing Leap to close the gap, trading its ranged edge for melee reach with the poisoned dagger | [[grung-clans\|Grung Clans]] |
