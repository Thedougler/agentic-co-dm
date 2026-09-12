---
type: creature
status: canon
publish: false
aliases:
  - Blue-Caste Handler
  - Purple-Caste Warrior
created: legacy
updated: legacy
tags: [grung, combat]
campaigns: [Shattered Sea]
---

# Grung Elite Warrior

CR 2 humanoid grung. Blue-caste handlers and purple-caste warriors — the operational backbone of [[simone-tabarnack|Simone]]'s raid infrastructure. The dungeon they garrison, [[calveno-sewers-grung-magazines|Calveno Sewer Magazines]], is itself `status: pending`.

Elite warriors serve two roles in the [[calveno-sewers-grung-magazines|Calveno sewer network]]: Blue-caste handlers (secondary sites) coordinate sentry teams of 2 green-caste laborers with standing orders to hide-and-report; the handler fights only to cover the laborers' escape, then retreats, opening with shortbow from concealment and using Standing Leap to reposition across water channels. Purple-caste warriors (primary site) are shoot-on-sight security who open from concealment with hand crossbow (use shortbow stats), use Mesmerizing Chirr if two or more targets cluster within 15 ft, then focus fire on stunned targets, fighting from elevated positions (scaffolding, ledges) to exploit ranged advantage. Blue-caste breaks at half HP or if the magazine is compromised; purple-caste at the primary site fights to the death to protect the summoning circle.

Mesmerizing Chirr is a stun — one of the most powerful conditions. At DC 12 and Recharge 6, it fires once per fight on average. In the primary chamber with 4 Elite Warriors, the party faces up to 4 Chirr attempts if the fight lasts long enough. Stagger their use: the first warrior Chirrs on round 1, others hold theirs. The party's concentration-dependent controller ([[vault/shattered-sea/pcs/perrin-black-jaw|Perrin]]) is particularly vulnerable to the stun — if he loses concentration on Tasha's Hideous Laughter, the tactical landscape shifts hard.

Related:

- [[grung|Grung (Lore)]]
- [[grung-clans|Grung Clans (Faction)]]
- [[calveno-sewers-grung-magazines|Calveno Sewer Magazines]] — Room 3 carries an inline stat excerpt of this creature (`e484ffa` precedent); this page is the canonical statblock home.
- [[vault/shattered-sea/monsters/grung-npc|Grung (Green-Caste NPC)]] and Grung Wildling — sibling bestiary/NPC entries named in the source's own related section. Grung (Green-Caste NPC) landed R36; live-linked per finalize-time forward-linking. Grung Wildling has no page yet in this wiki (see queue file `archive/2026-07/ss11-creature-grung-elite.md`).
- Calveno — Beffa Grung Raid — source session/encounter page named in the source's own related section. No page exists for it yet in this wiki (see queue file above).

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

## Session Log

None.
