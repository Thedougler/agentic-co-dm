---
type: npc
status: pending
publish: false
aliases: []
created: 2026-08-05
updated: 2026-08-09
tags: [mystery, combat, recurring]
summary: "Talon Vantyrus's apprentice, openly scheming to kill him, who tests the crew by stooping out of the sun to steal Crissdalynn's Fate Spinner."
owner_skill: ".claude/skills/draft-content/references/npc.md"
subtype: major
role: [villain, recurring]
has_active_front: false
campaigns: [Shattered Sea]
reference_image: ""
voice_id: ""
voice: ""
voice_actor: ""
uid: 81f8fe51-25cb-44c8-a28c-596750a57b56
---

# Talon Skarn

**Wants:** best [[master-kyzil|Master Kyzil]] in a fight the Sentinels can't dismiss as a fluke, and every move toward it still has to look like [[talon-vantyrus|Talon Vantyrus]]'s plan until Skarn is ready to make it his own.

> [!read-aloud]
> A speck against the sun, gone the instant you notice it. Then he isn't.
>
> You hear it before you place it: a thin whistle of wind, gone as fast as it came.
>
> He's just *there*, mid-strike, no beat between: a lean, knife-folded [[aarakocra|Aarakocra]] barely five feet tall, blue-grey crest feathers slicked flat by the dive.
>
> A black stripe cuts down through fierce amber eyes like warpaint under a hood.
>
> A notch of missing barbs mars his left primary, three feathers that never grew back, a jagged gap in an otherwise perfect wing.
>
> His harness rides close, no cloak, nothing loose enough to catch the wind wrong.
>
> Twin daggers reverse-grip at his hips, already drawn before you register the movement.
>
> His talons, scarred and banded in old white lines, close on [[fate-spinner|the dreidel]] at your belt before the strike even finishes landing.
>
> He's climbing back into the sun before you can call it a fight.
>
> *Talon Skarn*: You didn't even see me coming. That's the whole lesson.

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

## Stats & Combat

```statblock
layout: Basic 5e Layout
dice: true
columns: 2
forceColumns: true
name: Talon Skarn
size: Medium
type: humanoid
subtype: aarakocra
alignment: chaotic neutral
ac: "19 (evasive reflexes)"
hp: 97
hit_dice: "13d8 + 39"
speed: "50 ft., fly 90 ft."
stats: [14, 24, 16, 12, 16, 14]
saves:
  - Dex: +10
  - Con: +6
skillsaves:
  - Acrobatics: +10
  - Stealth: +10
  - Perception: +6
senses: "passive Perception 16"
languages: "Common, Aarakocra, Auran"
cr: 7
traits:
  - name: Keen Sight
    desc: "Skarn has advantage on Wisdom (Perception) checks that rely on sight."
  - name: Evasion
    desc: "When Skarn is subjected to an effect that allows a Dexterity saving throw for half damage, he takes no damage on a success and half damage on a failure."
  - name: Countless Strikes
    desc: "Skarn's unarmed strikes and weapon attacks are magical."
  - name: Windborn Gust (1/Day)
    desc: "Skarn can cast Gust of Wind (spell save DC 14), requiring no material components."
actions:
  - name: Multiattack
    desc: "Skarn makes two Skysplitter Dagger attacks."
  - name: Skysplitter Dagger
    desc: "Melee or Ranged Weapon Attack: +10 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 10 (1d4 + 7) piercing damage plus 4 (1d8) force damage. The dagger returns to Skarn's hand immediately after a ranged attack."
  - name: Stoop (Recharge 5-6)
    desc: "Skarn flies up to his flying speed in a straight line toward a creature he can see, then makes one attack against it. Melee Weapon Attack: +10 to hit, one target. Hit: 21 (4d6 + 7) slashing damage. Skarn can also attempt to seize one item the target is holding or wearing: the target must succeed on a DC 19 Dexterity saving throw or the item is torn free into Skarn's talons. Whether or not the grab succeeds, Skarn immediately flies up to his flying speed away from the target without provoking opportunity attacks."
bonus_actions:
  - name: Windshear Retreat
    desc: "Skarn takes the Disengage or Dash action. When he does, his flying speed increases by 30 feet until the end of the turn."
reactions:
  - name: Downdraft Ward (3/Day)
    desc: "When a creature Skarn can see hits him with an attack, Skarn adds 4 to his AC against that attack, potentially causing it to miss. If the attack misses, Skarn can fly up to 10 feet without provoking opportunity attacks."
```

Skarn only enters a fight once the crew actually travels into or reaches [[midchain|the Midchain]], never before, wherever they currently stand.

He's built at the effective-class-level tier, not a full CR-built monster, still the apprentice proving himself. He tests an opponent with a strike he can walk away from. He never commits to one he can't. The scene plays out as that testing strike, not a fight to the finish.

Calibrated against the crew's real level-5 numbers: [[crissdalynn-khinriss|Crissdalynn]], [[catarina-davirelli|Catarina]], [[delmar-fisk|Delmar]], [[jean-claude-tabarnack|Jean-Claude]], and [[perrin-black-jaw|Perrin]]. His +10 to hit lands often, not automatically.

Neither his Skysplitter Daggers (10 average) nor his Stoop (21 average) drop any one of them in a single hit. AC 19 with 97 HP lets him absorb one or two real exchanges without folding.

The Downdraft Ward reads as him shrugging off blows clean, until its third use runs out and the limit finally shows. The grab save on Stoop sits high enough to favor him without guaranteeing the theft.

The Windshear Retreat carries him out of the fight every round, grab or no grab. He never lingers long enough to monologue. The one line on his way out is the entire performance.

> **Personality.** Hotshot ace-pilot swagger, always keeping score, never explaining a move twice. If you didn't catch it the first time, that was the point. He cleans a blade with a whetstone between exchanges, never once during them. His tell: the swagger drops and he goes silent the instant a hit lands.
> **Motivation.** Right now, this encounter: test what the crew and [[fate-spinner|the Fate Spinner]] can do, and take the item if the opening is there. Then he leaves before it costs him anything.
> **Escape Condition.** After one or two exchanges, or the moment Stoop resolves, grab or no grab. Windshear Retreat carries him out either way.

## Relationships

- [[talon-vantyrus|Talon Vantyrus]]: master and rival under [[the-countless|the Countless]]'s sharpened Rule of Two. The doctrine is an open contest to kill his own master. Vantyrus defends against it as proof he still deserves what he holds, and the contest stays locked to the two of them. The hired blades and disposable minions Skarn spends on [[the-countless|the Countless]]'s business never learn what they're actually serving. Skarn trained under Vantyrus, who marked him with [[the-countless|the Countless]]'s taken name in place of whatever the [[high-eyrie|High Eyrie]] called him. He abandoned that old name. Nobody has claimed it since. What he fears most is dying an apprentice, his claimed name folded back into someone else's doctrine before it ever stood as his own. That fear is why he never explains a move twice.
- [[master-kyzil|Master Kyzil]]: the fight Skarn actually wants, and Vantyrus's own former student. Skarn was in [[midchain|the Midchain]] with Vantyrus the night Master Kyzil named a "foul wind from the south" (Session 03-04). That instinct was them.
- [[crissdalynn-khinriss|Crissdalynn Khinriss]]: target of the Fate Spinner theft. Her [[fate-spinner|Fate Spinner]] is the one edge that makes her worth watching, and the one [[the-countless|the Countless]] want gone before the Sentinels notice it moving.
- [[fate-spinner|Fate Spinner]]: the object of the ambush.
- [[the-countless|The Countless]]: the order Skarn and Vantyrus broke away to form.
- [[sentinels-of-the-eyrie|Sentinels of the Eyrie]]: the order they left.
- [[midchain|The Midchain]]: where the ambush triggers.
