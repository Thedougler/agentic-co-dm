---
title: Solange Barret
aliases:
  - Solange Barret
category: entities
tags: [shattered-sea, npc]
sources:
  - "wiki/_raw/Grung clans.md"
  - "campaign-os:solange-barret.md"
summary: Red Grung operative named among the clans' current faces.
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
tier: supporting
created: 2026-09-12T00:00:00Z
updated: 2026-09-13
type: npc
reveal: revealed
campaign: shattered-sea
visibility: dm
relationships:
  - target: "[[grung-clans]]"
    type: related_to
  - target: "[[calven-and-calveno]]"
    type: related_to
---
# Solange Barret

|             |                                                        |
| ----------- | ------------------------------------------------------ |
| **Species** | [[Grung]] (Red Caste)                                      |
| **Role**    | Ritual specialist, warlock; direct subordinate of [[simone-tabarnack]] |
| **Location**| [[Calveno Sewer Magazines]], primary detonation chamber, [[Mercatura]] collector system |

> *"The circle is an invitation. What arrives cares nothing for your objections."*

A red-skinned Grung, small even for her kind, wears no armor, just a sleeveless leather harness with tools and chalk sticks hanging from her belt. Her hands stay stained with circle residue: limestone powder, charcoal, something iridescent. One wrong line ruins everything, and she knows this. She works with complete stillness, never speaking unless spoken to. Her voice is flat and certain.

She left seminary to become a demolitions engineer. Her arcane training is real but undervalued in her society. She respects the summoning circle deeply and understands what she calls. Her approach is professional. The circle is her craft.

Only Solange can summon [[otar-the-foul]]. She is the only one on [[simone-tabarnack|Simone]]'s team who knows how to run the summoning circle. The circle is beneath the Mercatura. It uses techniques the Grung didn't create.

Solange learned binding shapes from her patron. She calls this entity *le courant* (the current). She holds red caste rank, the top position below [[simone-tabarnack|Simone]]. [[simone-tabarnack|Simone]] plans. Solange runs the hard parts warriors can't. She joined [[simone-tabarnack|Simone]] at [[sorn]]. She alone knows the circle's activation code.

> [!mechanic]
> [[otar-the-foul|Otar]]'s summoning is Solange's work product, not a direct threat from her (she doesn't fight). Everything under **Stats & Combat** below describes what occurs when the crew reaches her mid-ritual. She becomes a channeling caster protected by Elite Warriors and a detonation trigger, functioning as an atypical encounter.

If the circle stands, Solange won't leave, knowing she is the key piece. If enemies break the circle, she runs, but if caught before the blast, she gives only her name and caste. **When she escapes:** she leaves only if the circle breaks before the blast (two rounds of chanting, or the garrison drops to 2). She blows the ceiling. She uses Dimension Door to reach the surface. She tells [[simone-tabarnack|Simone]] that enemies hit the main site, [[jean-claude-tabarnack|Jean-Claude]] helped them, and the summoning failed, so [[simone-tabarnack|Simone]] now knows someone works against her. If the ritual finishes, Solange stays and the entity takes her, and no one tells [[simone-tabarnack|Simone]] that [[jean-claude-tabarnack|Jean-Claude]] helped.

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Solange Barret"
size: Small
type: humanoid
subtype: grung
alignment: Lawful Evil
ac: 13
ac_note: "natural armor (15 within 10 ft. of summoning circle)"
hp: 66
hit_dice: 12d6 + 24
speed: "25 ft., Climb 25 ft."
stats: [7, 16, 14, 14, 12, 16]
saves:
  - wisdom: 3
  - charisma: 5
skillsaves:
  - arcana: 4
  - deception: 5
  - stealth: 5
damage_immunities: "poison"
condition_immunities: "poisoned"
senses: "Darkvision 60 ft., Passive Perception 11"
languages: "Grung, Common, Deep Speech"
cr: "3"
traits:
  - name: "Amphibious"
    desc: "Solange can breathe air and water."
  - name: "Poisonous Skin"
    desc: "Any creature that grapples Solange or comes into direct contact with her skin must succeed on a DC 12 Constitution saving throw or become poisoned for 1 minute. A poisoned creature can repeat the saving throw at the end of each of its turns, ending the effect on a success."
  - name: "Standing Leap"
    desc: "Solange's long jump is up to 25 feet and her high jump is up to 15 feet, with or without a running start."
  - name: "Circle Ward"
    desc: "While within 10 feet of the summoning circle, Solange has advantage on Constitution saving throws to maintain concentration and her AC increases by 2 (to AC 15). The active circle sheds bright light in a 10-foot radius and dim light for an additional 10 feet."
  - name: "Pact Magic"
    desc: "Solange is a 5th-level warlock. Her spellcasting ability is Charisma (spell save DC 13, +5 to hit with spell attacks). She has the following spells:\n\nCantrips (at will): Eldritch Blast (2 beams), Minor Illusion, Poison Spray\n3rd level (2 slots): Hex, Hold Person, Misty Step\n1/day each: Dimension Door, Mirror Image"
actions:
  - name: "Eldritch Blast"
    desc: "Ranged Spell Attack: +5 to hit, range 120 ft., two beams. Hit: 8 (1d10 + 3) force damage per beam."
  - name: "Dagger"
    desc: "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage plus 5 (2d4) poison damage."
reactions:
  - name: "Counterspell (Pact Magic Slot)"
    desc: "When Solange sees a creature within 60 feet casting a spell, she can expend a Pact Magic slot to attempt to interrupt it. The spell fails if it is 3rd level or lower. For higher-level spells, she must succeed on a DC 10 + spell level Charisma check (+5)."
```

When the crew reaches Solange, she's almost done. One hand rests on stone, the other traces shapes after hours of work. Only minutes remain. She doesn't fight but chants using her turn each round, unable to attack or cast spells. The four [[grung-elite-warrior|Elite Warriors]] protect her, meant to die in her defense.

After two full rounds of chanting or when the garrison drops to 2, she triggers the blast by speaking a magic word. Counterspell can't stop it. The circle shields Solange while others take fire. She finishes the ritual in the dust. [[otar-the-foul|Otar]] comes through her body and takes her.

**Channeling:** Mirror Image is up (3 copies, each blocks one hit). She stays 10 ft from the circle (AC 15, good saves). Bright light spreads 10 ft.

> [!mechanic]
> **Reaction:** cast Counterspell or blast. If a caster hits the circle or her mind, Solange casts Counterspell (blocks level 3 or less, check for higher). She has two level 3 slots. Each spell costs half her power and this turn's blast. **Blast:** after two rounds of chanting or when the garrison hits 2, Solange says the word. Magic fuses blow. Counterspell can't stop it. The circle keeps her safe. Others take 8d6 fire and 4d6 crush (DEX/STR save, DC 16 to halve).

**[[Arrival]]:** after the blast, Solange finishes the chant as [[otar-the-foul]] comes through her with darkness and ice and change. The entity takes her and can't be undone.

**If enemies disrupt the circle before detonation:** Solange loses the summoning but still detonates as a diversion. She escapes via Misty Step (break line of sight), then uses [[Dimension Door]] (to the surface). She won't die for a failed ritual.

## Connections

- [[simone-tabarnack]]: commander, the only person whose orders Solange follows without question
- [[otar-the-foul]]: the entity Solange's circle summons
- [[Calveno Sewer Magazines]]: the primary detonation chamber where Solange operates
- [[calven-and-calveno]]: the site of Beffa Grung Raid, the operation Solange's ritual anchors
- [[jean-claude-tabarnack]]: if Solange escapes, she identifies him to [[simone-tabarnack|Simone]]
- [[grung-elite-warrior|Elite Warriors]]: her expendable shield during the ritual
- [[solanges-authority-seal]]: a red-caste command signet found on her, salvaged from the Primary Chamber rubble

## Session Log

**Session 06** (`vault/episodes/006/`). Solange chanted in the Primary Chamber, hands on stone. [[crissdalynn-khinriss|Crissdalynn]]'s Read the Current said, “the big one… Solange,” with low strength. [[ozzeth-the-twiceborn|Ozzeth]] (called Ozzy in play) protected her, warding the ritual. She spoke once: “I will not have my princesses stopped.”

Mid-fight, [[ozzeth-the-twiceborn|Ozzeth]] held her shoulder, saying “you can do this,” and poured his red-and-blue power into her. Misty Step and Greater Invisibility flowed to her, keeping her from harm. Crissdalynn hit and poisoned her. Ozzeth fell in combat, his last act grabbing her shoulder again, saying “do it now.” (See [[ozzeth-the-twiceborn|Ozzeth]]'s own Session Log.)

After his death she moved to [[catarina-davirelli|Catarina]] and spoke “Agni,” blowing the ceiling and finishing the ritual. Catarina tried to stop her and failed. The ritual's end brought [[otar-the-foul|Otar]]'s arrival.
