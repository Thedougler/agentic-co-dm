---
title: "Hierarch"
category: entities
tags: [shattered-sea, creature]
sources:
  - "campaign-os:hierarch.md"
created: 2026-09-13
updated: 2026-09-13
type: creature
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "CR 19 sorcerer lich that binds its soul to its own bloodline, so every living descendant becomes a phylactery. Aldric Drave and Shepherd Grigori are the campaign's two confirmed Hierarchs."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Hierarch

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Hierarch"
size: Medium
type: undead
alignment: Any Alignment
ac: 17
hp: 263
hit_dice: 31d8 + 124
speed: "30 ft."
stats: [11, 18, 18, 16, 15, 21]
saves:
  - constitution: 10
  - charisma: 12
skillsaves:
  - arcana: 9
  - deception: 12
  - history: 9
  - intimidation: 12
  - persuasion: 12
damage_resistances: "Cold, Necrotic, Poison; Bludgeoning, Piercing, and Slashing from Nonmagical Attacks"
condition_immunities: "Charmed, Exhaustion, Frightened, Paralyzed, Poisoned"
senses: "Darkvision 120 ft., Passive Perception 12"
languages: "The languages it knew in life"
cr: "19"
traits:
  - name: "Blood Phylactery"
    desc: "A destroyed Hierarch gains a new body as long as any bloodline descendants still act as phylacteries. 10+ phylacteries: 1d10 days to reform. 5+: 1d10 weeks. Fewer than 5: 1d10 months. The new body appears near the closest phylactery in the family tree."
  - name: "Family Reunion"
    desc: "For each conscious bloodline phylactery within 10 feet, the Hierarch gains +1 to melee and spell attack rolls."
  - name: "Turn Resistance"
    desc: "Advantage on saving throws against any effect that turns undead."
  - name: "Metamagic"
    desc: "At will: Careful Spell, Subtle Spell. 5/day: Distant Spell, Extended Spell. 3/day: Quickened Spell, Seeking Spell, Transmuted Spell. 2/day: Heightened Spell, Twinned Spell."
spells:
  - "Spellcasting. CHA-based (spell save DC 19, +11 to hit). Requires no material components."
  - "At will: Alter Self, Chill Touch, Fire Bolt, Hold Person, Message"
  - "3/day each: Blur, Counterspell, Fear, Hypnotic Pattern, Scorching Ray (3rd level)"
  - "2/day each: Sleet Storm, Blight, Dominate Person"
  - "1/day each: Circle of Death, Disintegrate, Finger of Death"
actions:
  - name: "Might of the Bloodline"
    desc: "Ranged Spell Attack: +11 to hit, range 60 ft., one creature. Hit: 10 (3d6) Necrotic damage. If either the Hierarch or the target is within 10 feet of one of the Hierarch's phylacteries, the damage increases by 1d6."
  - name: "Reanimate Family"
    desc: "The Hierarch targets the corpse of a bloodline creature that died within the last minute. It rises immediately as a wight under the Hierarch's control."
  - name: "Blood Sacrifice"
    desc: "One bloodline creature must succeed on a DC 19 Constitution saving throw or take 3d10 Necrotic damage. The Hierarch regains HP equal to the damage dealt and regains one expended spell slot or Metamagic use."
legendary_actions:
  - name: "Cantrip"
    desc: "Cast a cantrip."
  - name: "Might of the Bloodline (Costs 2 Actions)"
    desc: "Make one Might of the Bloodline attack."
  - name: "Reanimate Family (Costs 2 Actions)"
    desc: "Use Reanimate Family."
  - name: "Blood Sacrifice (Costs 2 Actions)"
    desc: "Use Blood Sacrifice."
  - name: "Family Influence (Costs 3 Actions)"
    desc: "One bloodline creature within 30 feet gains +2 to all weapon and spell attack rolls until the end of its next turn."
```

### Lair Actions

On initiative count 20, the Hierarch can use one of the following (no repeat in consecutive rounds):

- [[Bloodied]] floor: spilled blood covers the area as magical difficult terrain until initiative count 20 on the next round.
- Ancestral surge: all bloodline creatures (including the Hierarch) gain +1 to attacks and saving throws until initiative count 20 on the next round.
- Family rally: all bloodline creatures move up to their speed immediately without provoking opportunity attacks.
- Bloodline metamagic: the Hierarch can apply one metamagic option to any spell cast in the lair without expending uses until initiative count 20 on the next round.

Source: Pointy Hat.

## Description

*A CR 19 undead sorcerer lich that binds its soul to its own bloodline, so every living descendant is a phylactery.*

A Hierarch is a sorcerer who has bound their soul to their own blood. Every living descendant becomes a phylactery. The bloodline is both the immortality mechanism and the power source: each generation extends the network of anchors, and the Hierarch gains control over every person carrying their cursed blood. The mechanism has a structural weakness. Blood thins across generations, and a Hierarch who has not refreshed their line in centuries loses coherence. The solution is the Heir ritual: possessing a sufficiently powerful descendant and beginning the process again.

## Ecology

A Hierarch does not hunt; it cultivates. It seeds its bloodline into a family or office positioned to keep records of its own descendants — a crown's officer corps, a trading house's inheritance ledgers — because a genealogical archive doubles as a census of its own phylacteries. It rarely strays from whatever body holds those records: the same network of living blood that keeps it alive also anchors where it can safely operate. Binding your own soul to your own blood is by design a solitary act, so a Hierarch never imagines a second one exists and never checks for company. [[aldric-drave]] built the [[dravosi-crown]]'s entire genealogical bureaucracy on this instinct over three centuries; [[shepherd-grigori]] is quietly building a matching network across two rival crowns, and neither has noticed the other's resemblance to himself.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Trace a name through a Crown's genealogical archive | The searcher has access to the ledgers and binding contracts | Surfaces a living phylactery — and a request that draws Aldric Drave's attention to whoever asked | [[aldric-drave]] |
| Kill or convert a bloodline descendant | The descendant is isolated from the Hierarch's notice long enough to act | Permanently severs one phylactery anchor; the Hierarch feels the loss and answers with Blood Sacrifice or Reanimate Family | [[aldric-drave]] |
| Offer to cure an "incurable" illness in a noble line | The Hierarch has already recruited that family as fresh phylacteries | Exposes the illness as engineered rather than natural, marking the searcher as a threat to the network | [[shepherd-grigori]] |

## Notable Individuals

The campaign has two confirmed Hierarchs:

**[[aldric-drave]]** founded the [[dravosi-crown]] before the colonial project began, seeding his bloodline into every noble family the Crown would produce. The Crown's genealogical archives are an inadvertent map of his phylactery network. He has been running this cycle for at least three centuries.

**[[shepherd-grigori]]** is a CR 19 Hierarch. He traveled aboard the [[Uncertainty|HCS Surety]] before parting ways with its crew at [[La Vasca]] to pursue business of his own in [[calven-and-calveno]]. His current status and location live on his own page. His phylactery network is a collection of noble heirs whose incurable illnesses he cured. As long as any of them live, he cannot be permanently killed. His magic type remains unidentified (red viscous light, no components, Arcana 18 failed). His connection to the [[Khlysty]] is DM truth.
