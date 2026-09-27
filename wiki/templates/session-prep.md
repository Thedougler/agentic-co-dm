---
title: "{{title}}"
category: journal
tags: ["{{campaign}}", session-prep]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: session-prep
reveal: unrevealed
campaign: "{{campaign}}"
session: ""
visibility: dm
status: ready
card: ""
summary: ""
---
<!-- Run-guide cockpit for one live slice; field rules live in run-guide references/lean-surface.md. New beats and plans copy hook, development, cliffhanger, climax, resolution, or session-plan instead. Fact-only: every line gives the DM a fact, ruling, or response. Keep a section only when this slice spends it; delete unused sections, bullets, rows, narration slots, and these comments. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

<!-- Required. The lines the DM runs the slice by, one fact each. The threat's numbers live in Statblocks; the card is a design note for agents and goes in the frontmatter. -->

**Ends when.** The end condition, then the time budget: about thirty minutes. **If running late:** what to cut. **If running early:** what to add.
**Party goal.** What ends the slice for the party, and what it can win or lose.
**Next beat.** [[Session-N-BB-label]]

> [!narration] Previously
> <!-- First beat of the session only: last session's events in order, read aloud as play starts to remind the players what happened, one paragraph ending where play stopped (theatre-of-the-mind: Recap, read aloud). -->

> [!narration] Opening
> <!-- Read first: one paragraph, or immediate-fact bullets when the arrival is not fixed (theatre-of-the-mind: the beat type's opening). -->

````col
```col-md
flexGrow=1
===
## Situation

Who starts where, in feet and compass directions, and what a move or Dash reaches.
```

```col-md
flexGrow=2
===
## Actors

**[[creature]] × 3.** HP or resources when not full, and the bloodied or break rule this slice; the statblock is in Statblocks.
```
````

## Scene Rules

**Mode.** The named rule this slice runs on (chase, siege, pursuit), and its trigger, once.

## Secondary Objective

<!-- Only when a second question runs in parallel: what it takes, what happens if ignored, and the later consequence. -->

## Terrain

<!-- Narration cells: a line or two in `_italic_` per place, the feature a player would act on there (theatre-of-the-mind: Zone cell). -->

| Place | Distance | Cover | Narration |
| ----- | -------- | ----- | --------- |
|       |          |       | _…_       |

## Pressure

<!-- Narration cells: a line or two in `_italic_` per tick of what the party sees and hears change (theatre-of-the-mind: Tick cell). -->

| Tick | What happens | Narration |
| ---- | ------------ | --------- |
| 1    |              | _…_       |

**Thresholds.** Bloodied, cover reached, and other thresholds that change the scene.

## Checks

| Intent | Approach | DC | Success | Partial | Failure |
| ------ | -------- | -- | ------- | ------- | ------- |
|        | **Ability (Skill)** | `DC 13` |  |  |  |

## Outcomes

<!-- Required. The changed situation and the beat each likely option hands to. -->

> [!narration] Outcomes
> <!-- The ending true for every option, a few sentences; an ending for one option goes in its table row (theatre-of-the-mind: Outcomes). -->

| If | Next | Narration |
| -- | ---- | --------- |
|    | [[Session-N-BB-label]] | _…_ |

## Statblocks

![[creature#Statblock]]

> [!narration] {Creature}
> <!-- One after each statblock embed, titled with its name: a few sentences; its response to the party stays in Actors (theatre-of-the-mind: Creature in scene). -->

## Links

[[owner]] · [[next beat]]

