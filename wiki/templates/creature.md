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
<!-- Fact-only: every line gives the DM a fact, ruling, or response. The default page is At a Glance, narration, and Statblock. Add Tactics, Behavior, Secrets, Connections, or Art only when you have facts for them. Delete unused sections, bullets, rows, narration slots, and these comments. -->

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

<!-- How it fights. Weaknesses are things the party can do. -->

- **Opening.** Its first move and the conditions it picks a fight in.
- **Signature.** The move that makes it this creature and no other, and its tell.
- **Adapts.** What it does when that move is countered.
- **Weaknesses.** Terrain, formations, or tools that shut it down.
- **Morale.** When it flees or surrenders, and where it goes.

> [!narration] In action
> <!-- Optional: the creature mid-fight, from theatre-of-the-mind (Outcome cell recipe), "you" address: one short block per signature move, read after the DM resolves it, showing how the move looks and sounds and the state it leaves, with each target's reaction left to its player. -->

## Behavior

<!-- What it does outside a fight, as facts a DM can play or a tracker can find. -->

- **Habits.** What it does when nothing bothers it.
- **Diet.** What it eats and what feeding leaves behind.
- **Group.** Alone, pair, pack, colony, or court; young and leaders.
- **Body.** Anatomy that matters at the table: what it breathes, where it is soft, what it can squeeze through.
- **Signs.** Tracks, spoor, and the trace each signature ability leaves before anyone sees it.
- **Aftermath.** What a place looks like after it has been there.

## Secrets

<!-- Hidden truths about it, each with how the party can learn it. -->

## Connections

- [[page]] — what this tie does at the table.

## Art

### Token

![[{subject-slug}-token.png|{{title}} token]]
