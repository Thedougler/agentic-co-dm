---
title: "Ash Caldera Dragon"
aliases:
  - "Ash Caldera Dragon"
  - "Ashglass dragon"
category: entities
tags: [shattered-sea, creature]
sources:
  - "wiki/_archive/ash-caldera-dragon.md"
  - "wiki/entities/place/ashglass.md"
  - "aleksander-malone.md"
summary: "Young red dragon on a dead volcanic island in the eastern Midchain; ash-slope approach, glowing crater lair, slag-fused hoard, lethal for a level 5 party."
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
tier: supporting
created: 2026-09-14
updated: 2026-09-27
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: "Eastern Midchain"
role: lair boss
cr: "10"
invention: true
relationships:
  - target: "[[ashglass]]"
    type: related_to
  - target: "[[midchain-east]]"
    type: related_to
---
# Ash Caldera Dragon

> [!narration] Ash Caldera Dragon
> The island's crown is burned out. The lower jungle has gone to black glass and drifting ash, and the ground up the slope ticks as it cools. At the crater's lip the air tastes of sulfur and pumice. A young red dragon lies along the hot rim with its wings spread flat to the stone, smoke venting from its beaked snout, swept-back horns and spinal frill catching the glow. It is already awake.

## At a Glance

The crater of the dead volcano at [[ashglass]] holds a young red dragon and a hoard fused into slag. It is an optional pull, not a job: scouting it and walking away is correct play for a party that is not yet ready.

- **Habitat.** A dead volcanic island in the eastern [[midchain-east|Midchain]]; ash slopes, heat vents, and a glowing crater lair.
- **Treasure.** Gold and gems half-melted into rock on the crater floor, with one item at the center that the heat never touched.
- **Threat.** CR 10 solo. Lethal for a level 5 party and genuinely costly for a level 10 one — the source means it to be telegraphed hard enough that backing off reads as good play.
- **Approach.** Poor visibility, unstable footing, unmapped heat vents, and gear left by earlier treasure hunters on the slope.

## Statblock

A 2024 young red dragon, unchanged.

```statblock
layout: Basic 5e Layout
name: "Ash Caldera Dragon"
size: Large
type: dragon
alignment: chaotic evil
ac: "18 (natural armor)"
hp: 178
hit_dice: "17d10 + 85"
speed: "40 ft., climb 40 ft., fly 80 ft."
stats: [23, 10, 21, 14, 11, 19]
saves:
  - dexterity: 4
  - constitution: 9
  - wisdom: 4
  - charisma: 8
skillsaves:
  - perception: 8
  - stealth: 4
damage_immunities: "Fire"
senses: "Blindsight 30 ft., Darkvision 120 ft., Passive Perception 18"
languages: "Common, Draconic"
cr: "10"
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks."
  - name: "Rend"
    desc: "Melee Attack Roll: +10, reach 10 ft. Hit: 13 (2d6 + 6) Slashing damage plus 3 (1d6) Fire damage."
  - name: "Fire Breath (Recharge 5–6)"
    desc: "Dexterity Saving Throw: DC 17, each creature in a 30-foot Cone. Failure: 56 (16d6) Fire damage. Success: Half damage only."
```

## Tactics

- **Opening.** It fights on the ground, not in the air, because the crater is its lair. It spends Fire Breath the moment two or more party members stand in a line on the crater floor.
- **Signature.** Fire Breath, 56 damage on a failed DC 17 save. Its tell is the same smoke that vents from its snout at rest — before the breath, the venting stops for one heartbeat and its throat glows.
- **Adapts.** When a target keeps distance or spreads out, it uses the terrain instead: it slams its tail into unstable rock to drop a ledge, or drives a wingbeat that throws ash across the caldera and blinds everyone but itself.
- **Weaknesses.** It will not leave the crater to chase. A party that fights from the rim, around cover, and spreads out denies the cone. Cold damage halves the value of its best turn, and it cannot fly through its own ash cloud any better than the party can.
- **Morale.** It fights to the death over the hoard. It never surrenders, and it never retreats past the crater lip.

> [!narration] In action
> The dragon stops venting smoke, and the glow climbs its throat. Then fire rolls across the caldera floor in a wave that curls the rock and leaves the air shimmering.

## Behavior

- **Habits.** It sleeps along the hot rim through the day and hunts the lower slope at night, which is why a passing ship sees the crater pulsing and nothing else.
- **Diet.** Goats, seabirds, and whatever comes into the caldera: the remains of earlier salvage crews lie fused into the ash near its hoard.
- **Group.** Alone. It is young, unmated, and holds the crater against everything.
- **Body.** It can squeeze its bulk down the throat of the vent it hatched in, so there is no side passage it cannot follow the party into.
- **Signs.** Heat shimmer on the slope, a roar that carries offshore, and ash that falls upward once before the dragon shows.
- **Aftermath.** A killed dragon leaves the crater cooling, the ash still falling inward, and the hoard's slag hardening around whatever the heat never touched.

## Secrets

- **What happened to the salvage crews.** They came for the glint on the crater floor and never left. Their boat still sits at anchor on the island's south shore, and one crew's gear is scattered up the lower slope. The dragon killed them at the rim and their remains are in the ash by the hoard.
- **The hoard's one keepsake.** The slag took the gold and gems, but one magic item at the hoard's center survived the heat unmarked. That item is the real reason to make the pull.

## Connections

- [[ashglass]] — the island. The dragon is its crater occupant and the whole of its danger.
- [[midchain-east]] — the water it sits in; the rumor circulates among Midchain pilots and salvagers.
- [[midchain]] — where the treasure rumor travels.
- [[aleksander-malone]] — his note names the same eastern dead volcano as a young red dragon's lair that does not overlap [[blackrule]].
