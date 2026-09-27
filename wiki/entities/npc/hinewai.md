---
title: Hinewai
aliases:
  - Hinewai
  - The Woman in the Woods
  - The Blight
  - Druid Lich
category: entities
tags: [shattered-sea, aruhe, npc]
sources:
  - "wiki/_archive/Hinewai.md"
  - "house (Monster-Brewer; legacy Fantasy Statblock import; Hinewai/Death Bloom ingest 2026-09-05)"
  - "wiki/_archive/arc-blight-of-aruhe.md"
  - "DM statement 2026-09-24 (Session 12 planning)"
  - "Session 12 refile (2026-09-27)"
created: 2026-09-12
updated: 2026-09-27
type: npc
reveal: unrevealed
campaign: shattered-sea
status: alive
role: rival
location: "[[memorial-grove]]"
faction: none
visibility: dm
invention: true
summary: "An elf archdruid who escaped Karath, fused herself to Aruhe, and died into it; her grief is the island's law. The party knows her only as the woman in the woods: a voice and a pair of orange eyes."
---
# Hinewai

![[hinewai-woman-in-the-woods-overview.png|Hinewai in the rainforest]]

````col
```col-md
flexGrow=2
===
## At a Glance

Hinewai is the island. To the party she is the woman in the woods: a voice in the dark and a pair of orange eyes between the trunks, who claims everyone who eats her fallen fruit.

- **Role.** The undead guardian bound to Aruhe, and the source of its law ([[taking-on-aruhe]]). Until the party reaches [[memorial-grove]], she appears only as the woman in the woods.
- **Nature.** A grieving elf archdruid whose love of living things lost every limit.
- **Wants.** Aruhe untaken, her graves unharmed, and her Calveno kept.
- **Home.** [[memorial-grove]], which is her body.
- **Hates.** The Grung, and anyone who takes from the island.
```

```col-md
flexGrow=1
===
> [!narration] Hinewai
> Hinewai is a tall, narrow elf with pale grey skin, pointed ears, and amber-orange eyes, with long black hair falling down her back over a dark, layered cloak. The cloak's ragged hem hangs almost to her boots, and its uneven sleeves hang from her long arms like strips of worn cloth. When she opens her mouth, small fangs show. She stands, walks, and crouches with the same slow, poised care. In the forest she is usually only a darker shadow between the trunks and two orange eyes.
```
````

## At the Table

- **How she appears.** As a voice from the dark, or a darker shadow between the trunks 30 feet away with two orange eyes and no body. She does not step out and does not attack. When the party comes to the Grove as guests, she stands in the open and receives them.
- **The Calveno.** Every Calveno who ate fallen fruit on Aruhe is hers, part of her garden. The island's responders never attack them, though ordinary animals still hunt them. She drew them inward to [[the-pantry]] with her voice. To her, anyone who leads them away is a kidnapper.
- **The Grung.** Every Grung she has seen on Aruhe wore a gold [[grung-authority-seal]] on the skin and truly wanted her graves destroyed. She assumes every Grung on her island is compelled and sent for them, and she names them for what their kind did to her: invader, manipulator, kidnapper, murderer.
- **Opens up when.** A Grung stands before her with no seal on the skin and no pull toward the graves. It is outside everything she knows, and it silences her.
- **Shuts down when.** Anyone takes from the island, or threatens fire.
- **Priority.** The Grove, then her Calveno.
- **Shares.** Contempt, and the truth about the graves if asked what the Grung want: "My graves. They always want my graves." Nothing about herself. She answers "why" with "Ask your gold masters."
- **Voice.** Low, calm, and old, in short sentences with long silences between them. She never raises it.
- **Lines.** "You may look. You may not take." · "Burn, then. Like them." · "Come and look upon my garden. You ate what my island gave you. You are already mine."

- **On the Burnt Road.** She speaks to any Grung who stands on [[the-burnt-road]]. What she says to Jean-Claude there is on [[Session-12-04-orders-in-the-ash]].

> [!narration] First meeting
> Between two trunks at the edge of the light, the dark is deeper than it should be, and two orange eyes open in it at the height of a tall woman's face. "You ate what my island gave you," a low voice says. "You are already mine."

## Statblock

Hinewai fights only at the [[memorial-grove]], when someone harms the Death Bloom. Then she sheds the woman in the woods for her Blight form. Pick the statblock by the Death Bloom's condition. Damage to her body alone never changes the stage.

> [!narration] Blight Form
> Hinewai's Blight form is a large ivory skeleton wrapped in moss, rotted bark, and long black hair. Green fire burns in its empty eye sockets, fruiting vines knot through the hair, and leafless branches rise from its shoulders. One forearm is sheathed in dark wood that narrows into a clawed hand, so that the whole upright shape looks like a dead tree forced into a person's form.

![[hinewai-blight-overview-v2.png|Hinewai Blight form overview]]

**Death Bloom Whole.** The memorial is substantially intact.

```statblock
layout: Basic 5e Layout
name: "Hinewai, the Blight (Stage 1)"
size: Large
type: undead
alignment: "neutral"
ac: 18
hp: 275
hit_dice: "34d10 + 102"
speed: "30 ft., climb 30 ft."
stats: [20, 14, 16, 17, 20, 15]
saves:
  - constitution: 9
  - wisdom: 11
skillsaves:
  - nature: 10
  - perception: 11
  - survival: 11
damage_resistances: "Cold, Necrotic, Poison"
condition_immunities: "Charmed, Exhaustion, Frightened, Paralyzed, Poisoned"
senses: "Darkvision 120 ft., Passive Perception 21"
languages: "Druidic, Elvish"
cr: "19"
traits:
  - name: "Rooted Phylactery"
    desc: "While the Death Bloom holds, Hinewai reforms at the Grove's tree 1d10 days after her body is destroyed. Destroying the Death Bloom first makes her next death permanent."
  - name: "Corrupted Ground"
    desc: "Hinewai moves through plants without spending extra movement, and Difficult Terrain within 1 mile of the Death Bloom costs her no extra movement."
  - name: "Turn Resistance"
    desc: "Hinewai has Advantage on saving throws against any effect that turns Undead."
spells:
  - "Spellcasting. Hinewai casts spells using Wisdom as her spellcasting ability (spell save DC 19, +11 to hit with spell attacks), requiring no Material components."
  - "At will: Druidcraft, Produce Flame, Thorn Whip"
  - "3/day each: Entangle, Moonbeam, Plant Growth, Spike Growth"
  - "2/day each: Insect Plague, Wall of Thorns"
  - "1/day each: Circle of Death, Foresight, Sunburst"
actions:
  - name: "Multiattack"
    desc: "Hinewai makes two Rotten Claw attacks."
  - name: "Rotten Claw"
    desc: "Melee Attack Roll: +11, reach 10 ft. Hit: 16 (2d10 + 5) Slashing damage plus 10 (3d6) Poison damage."
  - name: "Acid Bloom (Recharge 5–6)"
    desc: "Dexterity Saving Throw: DC 19, each creature in a 20-foot-radius Sphere centered on a point Hinewai can see within 60 feet. Failure: 36 (8d8) Acid damage. Success: Half damage."
legendary_actions:
  - name: ""
    desc: "Legendary Action Uses: 3. Immediately after another creature's turn, Hinewai can expend a use to take one of the following actions. She regains all expended uses at the start of each of her turns."
  - name: "Grasping Roots"
    desc: "Strength Saving Throw: DC 19, each creature in a 10-foot Cube Hinewai can see within 60 feet. Failure: The target has the Restrained condition until the end of its next turn."
  - name: "Rotten Claw (Costs 2 Uses)"
    desc: "Hinewai makes one Rotten Claw attack."
  - name: "Spore Burst (Costs 2 Uses)"
    desc: "Constitution Saving Throw: DC 19, one creature Hinewai can see within 30 feet. Failure: The target has the Poisoned condition until the end of its next turn."
  - name: "Feed the Bloom (Costs 3 Uses)"
    desc: "Hinewai regains 20 Hit Points, drawn from the Death Bloom."
```

**Death Bloom Wounded.** The memorial is badly damaged but still holds her.

```statblock
monster: "Hinewai, the Blight (Stage 1)"
name: "Hinewai, the Blight (Stage 2)"
ac: 16
hp: 165
hit_dice: "22d10 + 44"
stats: [18, 12, 14, 15, 17, 12]
saves:
  - constitution: 6
  - wisdom: 7
skillsaves:
  - nature: 6
  - perception: 7
senses: "Darkvision 90 ft., Passive Perception 17"
cr: "13"
spells:
  - "Spellcasting. Hinewai casts spells using Wisdom as her spellcasting ability (spell save DC 15, +7 to hit with spell attacks), requiring no Material components."
  - "At will: Druidcraft, Produce Flame, Thorn Whip"
  - "2/day each: Entangle, Moonbeam, Spike Growth"
  - "1/day each: Insect Plague, Wall of Thorns"
actions:
  - name: "Multiattack"
    desc: "Hinewai makes two Rotten Claw attacks."
  - name: "Rotten Claw"
    desc: "Melee Attack Roll: +7, reach 10 ft. Hit: 11 (2d6 + 4) Slashing damage plus 7 (2d6) Poison damage."
  - name: "Acid Bloom (Recharge 6)"
    desc: "Dexterity Saving Throw: DC 15, each creature in a 15-foot-radius Sphere centered on a point Hinewai can see within 60 feet. Failure: 22 (4d10) Acid damage. Success: Half damage."
legendary_actions:
  - name: ""
    desc: "Legendary Action Uses: 2. Immediately after another creature's turn, Hinewai can expend a use to take one of the following actions. She regains all expended uses at the start of each of her turns."
  - name: "Grasping Roots"
    desc: "Strength Saving Throw: DC 15, each creature in a 10-foot Cube Hinewai can see within 60 feet. Failure: The target has the Restrained condition until the end of its next turn."
  - name: "Rotten Claw (Costs 2 Uses)"
    desc: "Hinewai makes one Rotten Claw attack."
```

**Death Bloom Near Ruin.** The memorial barely holds, and she is close to permanent death.

```statblock
monster: "Hinewai, the Blight (Stage 1)"
name: "Hinewai, the Blight (Stage 3)"
ac: 14
hp: 75
hit_dice: "10d10 + 20"
speed: "20 ft., climb 10 ft."
stats: [15, 10, 12, 12, 13, 10]
saves: []
skillsaves:
  - nature: 3
damage_resistances: "Poison"
condition_immunities: "Charmed, Exhaustion, Frightened, Poisoned"
senses: "Darkvision 60 ft., Passive Perception 11"
cr: "7"
spells: []
traits:
  - name: "Rooted Phylactery"
    desc: "While the Death Bloom holds, Hinewai reforms at the Grove's tree 1d10 days after her body is destroyed. Destroying the Death Bloom first makes her next death permanent."
  - name: "Corrupted Ground"
    desc: "Hinewai moves through plants without spending extra movement."
actions:
  - name: "Rotten Claw"
    desc: "Melee Attack Roll: +4, reach 5 ft. Hit: 7 (1d8 + 3) Slashing damage plus 4 (1d8) Poison damage."
  - name: "Acid Seep (Recharge 6)"
    desc: "Dexterity Saving Throw: DC 12, each creature in a 10-foot-radius area of ground Hinewai can see within 30 feet. Failure: 10 (3d6) Acid damage. Success: Half damage. The area stays acid for 1 minute; a creature that enters it or starts its turn there for the first time on a turn makes the same save."
legendary_actions: []
```

## Secrets

- **The Death Bloom is her body.** The Grove's tree, her companion's grave, her own grave, the black-flower ring, and the bound soil together are her place-bound phylactery. There is nothing to carry off and smash. The Bloom's edges are uncertain, so damage that looks complete may leave enough for her to return. The party learns it from the two graves, from the roots that all point home, and from [[two-grave-orders]].
- **The two graves.** Her companion's grave is the reason for the law. Her own grave is the mechanism. No root crosses either.
- **Her roots.** Luminous roots, wrist-thick to thigh-thick, run from the shelf above [[clear-lake]] through [[the-marshes]], all pointing toward the Grove.
- **Her curse on the Grung.** No Grung who sets foot on Aruhe ever leaves it again. When the Calveno captives' fleet wrecked on the island, the three Grung guards who reached shore alive were dead within hours, killed by the island's creatures ([[the-aruhe-wreck]]).
- **The Calveno are hers.** Wherever they go on Aruhe, the island's responders spare them. Beppe Sarti at the Pantry believes her protection ends at the clearing, and he is wrong.

## Connections

- [[memorial-grove]] — her body, memorial, and phylactery.
- [[the-unnamed-companion]] — the drowned man whose grave is the reason for the law.
- [[karath]] — the island that captured her, and the source of her hatred.
- [[grung-and-the-making-of-aruhe]] — the full history of the crime and what followed.
- [[celia-parel]] — a survivor who records the dead and will not let an expedition treat them as scenery.
- [[oren-vask]] — a survivor who follows the law by choice and stays wary of her hatred of the Grung.

## History

Hinewai was an elf from a small private island village, and an immensely powerful druid who counted the land as kin. [[karath]] captured her and worked her in its hatcheries, where dosed captive casters push ordinary vermin into giants. Most of her memory rotted away there. Her hatred of the Grung and of those who take survived, and so did her love of living things. She escaped with one companion, and he drowned on the half-mile swim to Aruhe. She carried him inland and buried him beneath a fruit tree, and the island offered the fruit he loved. She took it as a vow. Years later she fused her soul and body to the land, and the ritual killed her. Her body became the Grove, her grief became the law, and Aruhe's living things lost their ordinary limits.

## Log

- **[[Session-11-Recap]]** — Her voice asked the party, in the dark at the Slack Basin, to admire her garden.
- **Session 12 prep** — She speaks to Jean-Claude on the Burnt Road and calls him a kidnapper.

## Art

![[hinewai-reference-sheet.jpg|Hinewai identity reference sheet]]
![[hinewai-woman-in-the-woods-token.jpg|Hinewai woman-in-the-woods token]]
![[hinewai-moonlit-harp.jpg|Hinewai playing harp in the moonlit jungle]]
