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
token: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. The default page is At a Glance, narration, and Statblock. Add Tactics, Behavior, Secrets, or Connections only when you have facts for them. Delete unused sections, bullets, rows, narration slots, and these comments. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

## At a Glance

<!-- Required. Lead sentence: what this creature is for at the table. Then labelled facts, one bullet each. -->

- **Habitat.** [[place]] or terrain where it lives.
- **Treasure.** What it carries or guards.

> [!narration] {{title}}
> <!-- One third-person paragraph, true every time it is met: size and shape, its strangest feature, one sound or smell, what it does at rest, a visible tell for each signature ability (theatre-of-the-mind: Creature portrait). -->

## Statblock

<!-- Required. At most one overview image directly above the fence: `![[attachments/{subject-slug}-overview.ext|{{title}}]]` -->
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
> <!-- Optional: the creature mid-fight, "you" address, a few sentences showing each signature ability as it lands (theatre-of-the-mind: Creature in scene, In action). -->

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

