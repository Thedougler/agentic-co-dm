---
title: "{{title}}"
category: entities
tags: ["{{campaign}}", creature]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: creature
reveal: unrevealed
campaign: "{{campaign}}"
visibility: dm
region: ""
role: ""
cr: ""
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. The default page is At a Glance, narration, and Statblock. Add Tactics, Behavior, Secrets, Connections, or Art only when you have facts for them. Delete unused sections and these comments. -->

# {{title}}

````col
```col-md
flexGrow=2
===
## At a Glance

<!-- Required. Lead sentence: what this creature is for at the table. Then labelled facts, one bullet each. -->

- **Habitat.** [[place]] or terrain where it lives.
- **Treasure.** What it carries or guards.
```

```col-md
flexGrow=1
===
> [!narration] {{title}}
> <!-- Player-safe look: size and shape, its strangest feature, one sound or smell, what it does at rest, a visible tell for each signature ability. -->
```
````

## Statblock

<!-- Required. At most one overview image directly above the fence: ![[{subject-slug}-overview.png|{{title}}]] -->
```statblock
layout: Basic 5e Layout
name: "{{title}}"
size: Medium
type: monstrosity
alignment: unaligned
ac: 13
hp: 11
hit_dice: "2d8 + 2"
speed: "30 ft."
stats: [10, 10, 10, 10, 10, 10]
senses: "passive Perception 10"
languages: "—"
cr: "1/4"
traits:
  - name: "Trait Name"
    desc: "What it does, in 2024 rules language."
actions:
  - name: "Bite"
    desc: "*Melee Attack Roll:* +2, reach 5 ft. *Hit:* 4 (1d6 + 1) Piercing damage."
```

## Tactics

<!-- How it fights: opening move, how it adapts when countered, when it flees or surrenders. -->

> [!narration] In action
> <!-- Optional: the creature mid-fight, from theatre-of-the-mind (Creature in scene recipe), "you" address: how it closes, strikes, and what each signature ability looks and sounds like when it lands. -->

## Behavior

<!-- What it does outside a fight: habits, diet, pack or lair, signs trackers find. -->

## Secrets

<!-- Hidden truths about it, each with how the party can learn it. -->

## Connections

- [[page]] — what this tie does at the table.

## Art

### Token

![[{subject-slug}-token.png|{{title}} token]]
