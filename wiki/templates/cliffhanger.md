---
title: "{{title}}"
category: journal
tags: ["{{campaign}}", session-prep]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: session-prep
kind: cliffhanger
reveal: unrevealed
campaign: "{{campaign}}"
session: ""
visibility: dm
card: ""
tier: ""
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Keep a section only when this Cliffhanger spends it at the table; delete unused sections, bullets, rows, narration slots, and these comments. Completeness bar: docs/agents/table-ready.md. File as Session-<n>-<BB>-<label>.md. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

<!-- Required. The lines the DM runs the beat by, one fact each. What the opposition wants lives in Actors; the card is a design note for agents and goes in the frontmatter. -->

**Starting situation.** Positions, conditions, and resources the party carries in.
**Party goal.** The result that ends this contest for the party besides surviving.
**Ends when.** The condition that ends the beat, in about three to five rounds.
**Next beat.** [[Session-{{session}}-BB-label]]

> [!narration] Opening
> <!-- Read first: one paragraph, or immediate-fact bullets when the arrival is not fixed (theatre-of-the-mind: Cliffhanger opening). -->

## Actors

- **[[creature]] × 4.** How many, and HP or resources when not full; the statblock is in Statblocks.
- **Goal.** What the opposition is here to do, beyond killing the party.
- **Tactics.** Opening move → adapts when countered → break point → exit, and how the party can close it.

> [!narration] {Creature}
> <!-- Optional, one per creature kind, titled with its name, in the order the party meets them: a few sentences; its response to the party stays in Actors (theatre-of-the-mind: Creature in scene). -->

````col
```col-md
flexGrow=1
===
## Terrain

- **Distances.** Distances in feet, zones, and routes.
- **Feature.** What a character can do with it, and the ruling (cover, DC, damage).
- **Hazard.** What hurts anyone who stands in it, and the ruling.
- **Change.** How the space transforms, and on which round.
```

```col-md
flexGrow=1
===
## Pressure

<!-- Narration cells: a line or two in `_italic_` per round of what the party sees and hears change (theatre-of-the-mind: Tick cell). -->

| Round | What happens | Narration |
| ----- | ------------ | --------- |
| 1     |              | _…_       |
| 2     |              | _…_       |
| 3     |              | _…_       |
```
````

## Checks

| Intent | Approach | DC | Success | Failure |
| ------ | -------- | -- | ------- | ------- |
|        | **Strength (Athletics)** | `DC 15` |  |  |

## PC Hooks

- **[[pc]].** The job their abilities fit here, or the stake it touches.

## Clues

- **Clue.** A short usable fact the contest can surface, and how.

## Outcomes

<!-- Required. One row per outcome the beat can plausibly produce: what changes and the beat it hands to. Narration cells: a line or two in `_italic_` of the changed state (theatre-of-the-mind: Outcome cell). -->

| Outcome | What changes | Next | Narration |
| ------- | ------------ | ---- | --------- |
| **Objective gained** |  | [[Session-{{session}}-BB-label]] | _…_ |
| **Costly success** |  | [[Session-{{session}}-BB-label]] | _…_ |
| **Lost** |  | [[Session-{{session}}-BB-label]] | _…_ |
| **Broken off** |  | [[Session-{{session}}-BB-label]] | _…_ |

**Carry forward.** Each state the next beat inherits: positions, injuries, resources, who holds what.

> [!narration] If the session ends here
> <!-- The last words of the night if play stops on this beat, a few sentences (theatre-of-the-mind: If the session ends here). -->

## Statblocks

<!-- One embed per fighter kind the party could face, from its owner page. -->

![[creature#Statblock]]
