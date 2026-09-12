---
type: npc
status: draft
publish: false
aliases: [Quackers]
created: "2026-08-05"
updated: "2026-08-09"
tags: [faith]
summary: "A duck-shaped celestial guardian of Yssenmoor, centuries removed from his life as a wizard's familiar, one accidental step from godhood he refuses to notice."
subtype: minor
location: "[[yssenmoor|Yssenmoor]]"
role: [ally]
campaigns: [Shattered Sea]
reference_image: "_assets/reference/sir-quackers-the-fowl-reference.jpg"
voice_id: ""
voice: ""
voice_actor: ""
uid: de69868a-56e3-4c2b-8ddd-9ea05dafb329
---

# Sir Quackers the Fowl

**Wants:** to watch over Yssenmoor and anyone weak enough to need it, though nothing has answered his challenge in longer than he can recall.

*Sir Quackers*: "State your name, your business, and whether you mean to leave this marsh the way you found it."

![[sir-quackers-the-fowl-narration-appearance]]

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

**Roleplay Concept.** A small-town herald crossed with a demigod paladin who still doesn't know which one he actually is.

**Lore Sheet.**

- **Sir Quackers** was once the familiar of RTLB: master of duomancy, transfiguration, and conjuration, rescuer of the dragon clans, tamer of faeries, and two gnomes in a trenchcoat. RTLB sent Quackers ahead to spring every trap meant for someone else, and Quackers died to them over and over, reformed each time.
- RTLB eventually freed him, gave him his own life, will, and sentience, and left him this island. RTLB vanished long ago, whereabouts unknown. No wizard Quackers has met since has matched the might of his original creator.
- If asked about RTLB, Quackers talks at length and happily. He recites the titles, the feats, the reckless genius, and lands on the same quiet admission every time: RTLB cried whenever Quackers came back from dying, and Quackers never worked out whether that made the sending worse or better.
- Centuries of a hidden ley line's power have fed his single, honest desire to protect until it edged him into something close to a demigod. He has no idea.
- [[yssenmoor|Yssenmoor]]'s permanent fog and its habit of announcing visitors before they arrive are his own unconscious hallowing of the ground, not a natural feature.

**Toy Chest.**

| Field | Detail |
|---|---|
| `primary_goal` | Watch over [[yssenmoor\|Yssenmoor]]'s marsh and protect anything living weak enough to need it. |
| `consistent_method` | Challenges every visitor with an absurdly formal recitation, names, titles, business, and whether they mean to leave the marsh as they found it, before he'll even consider raising a weapon. |
| `active_problem` | The last three ships that anchored off Yssenmoor left without answering his challenge, and he's started reciting it to empty water. |
| `performance_hooks` | A small-town herald crossed with a knight who never got the memo the war ended. Taps the flat of his blade twice against the ground before he speaks, like punctuation. |
| `link_of_relevance` | [[crissdalynn-khinriss\|Crissdalynn]]: the [[fate-spinner\|Fate Spinner]] reacts to the ley line beneath [[yssenmoor\|Yssenmoor]], old magic recognizing old magic. Quackers does not know why it responds to her. |

**Voice & Delivery.**

*Sir Quackers*: "*(formal)* I am Sir Quackers the Fowl, Blade of the Wetlands, Guardian of the Marsh, and Defender of the Weak. State your business."

*Sir Quackers*: "*(quieter)* You may go. Or you may stay. That part's still yours to choose."

*Sir Quackers*: "*(low, almost to himself)* He used to cry, you know. Every single time."

*Sir Quackers*: "*(warming up, the formal stiffness dropping)* Two gnomes. In a coat. The greatest wizard I have ever known, and half of him couldn't reach the top shelf."

*Sir Quackers*: "*(reciting, proud)* Master of duomancy, the art of two acting as one. Tamer of faeries. Rescuer of the dragon clans. He could turn a thing into another thing entirely and call a thing from nothing, and he never once used either trick to make my deaths stop hurting."

Taps the flat of his blade twice against the ground before he speaks. Otherwise stands unnervingly still. Emotional default: formal warmth, guarded underneath. On the subject of RTLB: the warmth wins. He will talk as long as anyone listens.

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Sir Quackers the Fowl"
size: Large
type: celestial
alignment: "Neutral Good"
ac: 20
hp: 275
hit_dice: "22d10 + 154"
speed: "45 ft., Fly 135 ft. (hover)"
stats: [25, 21, 25, 22, 24, 28]
saves:
  - str: 13
  - con: 13
  - wis: 13
  - cha: 15
damage_resistances: "Radiant"
damage_immunities: "Charmed, Exhaustion, Frightened"
senses: "truesight 120 ft.; Passive Perception 23"
languages: "All; telepathy 120 ft."
cr: 18
traits:
  - name: "Divine Awareness"
    desc: "Sir Quackers knows if he hears a lie."
  - name: "Undying Guardian"
    desc: "If Sir Quackers dies, his body dissolves into marsh-fog and reforms a day later somewhere on [[yssenmoor|Yssenmoor]], reviving with all his Hit Points. He remembers every death."
  - name: "Legendary Resistance (2/Day)"
    desc: "If Sir Quackers fails a saving throw, he can choose to succeed instead."
  - name: "Magic Resistance"
    desc: "Sir Quackers has advantage on saving throws against spells and other magical effects."
actions:
  - name: "Multiattack"
    desc: "Sir Quackers makes two Radiant Wingblade attacks. He can replace one attack with a use of Marshbane Arrow."
  - name: "Radiant Wingblade"
    desc: "*Melee Attack Roll:* +14, reach 10 ft., one target. 18 (3d6 + 8) Slashing damage plus 27 (6d8) Radiant damage."
  - name: "Marshbane Arrow"
    desc: "*Dexterity Saving Throw:* DC 20, one creature Sir Quackers can see within 600 feet. *Failure:* If the target has 85 Hit Points or fewer, it dies. It otherwise takes 19 (3d8 + 6) Piercing damage plus 27 (6d8) Radiant damage."
  - name: "Wetland's Wrath (Recharge 5–6)"
    desc: "Sir Quackers calls up a 20-foot-radius Sphere of radiant marsh-light centered on a point he can see within 120 feet. *Dexterity Saving Throw:* DC 20, each creature in that area. *Failure:* 27 (7d6) Radiant damage. *Success:* Half damage."
  - name: "Spellcasting"
    desc: "Sir Quackers casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 23): - **At Will:** *Detect Evil and Good* - **1/Day Each:** *Commune*, *Control Weather*, *Dispel Evil and Good*, *Raise Dead*"
bonus_actions:
  - name: "Divine Aid (2/Day)"
    desc: "Sir Quackers casts *Cure Wounds* (level 2 version), *Lesser Restoration*, or *Remove Curse*, using the same spellcasting ability as Spellcasting."
legendary_actions:
  - name: ""
    desc: "Sir Quackers can take 2 legendary actions, choosing from the options below. Only one legendary action can be used at a time, and only at the end of another creature's turn. He regains spent legendary actions at the start of his turn."
  - name: "Blinding Gaze"
    desc: "*Constitution Saving Throw:* DC 23, one creature Sir Quackers can see within 120 feet. *Failure:* The target has the Blinded condition for 1 minute. *Failure or Success:* Sir Quackers can't take this action again until the start of his next turn."
  - name: "Radiant Teleport"
    desc: "Sir Quackers teleports up to 60 feet to an unoccupied space he can see. *Dexterity Saving Throw:* DC 23, each creature in a 10-foot Emanation originating from him at his destination space. *Failure:* 11 (2d10) Radiant damage. *Success:* Half damage."
lair_actions:
  - desc: "On initiative count 20 (losing initiative ties), Sir Quackers takes a lair action to cause one of the following effects; he can't use the same effect two rounds in a row. These options exist only while he fights on yssenmoor: his hallowed ground."
  - name: "Fog Thickens"
    desc: "Fog rolls across a 60-foot-radius Sphere centered on a point Sir Quackers can see. That area is heavily obscured until initiative count 20 on the next round."
  - name: "The Voice Arrives First"
    desc: "A voice (Sir Quackers' own) calls out from a point he designates within 120 feet, seconds before he actually moves there. Each creature within 10 feet of that point must succeed on a DC 18 Wisdom saving throw or have the Frightened condition until the end of its next turn."
  - name: "The Marsh Grasps"
    desc: "One creature Sir Quackers can see within 60 feet must succeed on a DC 18 Strength saving throw or have the Restrained condition until it uses an action to break free (escape DC 18)."
```

Stats blend [[solar|Solar]] and [[planetar|planetar]], deliberately positioned between the two (CR 18). Sir Quackers stands far above this level 5 party's reach by design: an obstacle the party cannot defeat.

## Relationships

- [[yssenmoor|Yssenmoor]] is the island he watches over, hallowed ground under his own unconscious protection.
