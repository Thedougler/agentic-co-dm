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
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Keep a section only when this Cliffhanger spends it at the table; delete unused sections, bullets, rows, narration slots, and these comments. Completeness bar: docs/agents/table-ready.md. File as Session-<n>-<BB>-<label>.md. -->

# {{title}}

## At a Glance

<!-- Required. Lead sentence: the contest, and what the party can lose. Then labelled facts, one bullet each. -->

- **Entry state.** Positions, conditions, and resources the party carries in.
- **Party objective.** The result that ends this contest besides surviving.
- **Opposition wants.** What [[npc]] or [[creature]] is trying to do.
- **Ends when.** The condition that ends the beat, in about three to five rounds.
- **Next.** [[Session-{{session}}-BB-label]]

> [!narration] Opening
> <!-- Spoken opening from theatre-of-the-mind (Cliffhanger opening recipe): one paragraph of 60–90 words, the threat in sentence one, ending on the reaction point. File immediate-fact bullets instead when the entrance, light, or who is present can still change. Responses to the party, other approaches, and checks go in the DM prose beside it. -->

## Actors

- **[[creature]] × 4.** This beat's state (HP when not full, spent resources) and the trait that changes tactics. Its numbers arrive by the Statblocks embed.
- **Wants.** What the opposition is here to do, beyond killing the party.
- **Tactics.** Opening move → adapts when countered → break point → exit, and how the party can close it.

> [!narration] {Creature}
> <!-- Optional: the creature as the party meets it here, from theatre-of-the-mind (Creature in scene recipe): three to five sentences of silhouette, movement, dangerous parts, scale, and what it was already doing, ending on its windup before contact. Its response to the party goes in Actors. Titled with its name; one per creature kind. -->

## Statblocks

<!-- Only when the party could fight someone here: every side's owner statblock, embedded, never retyped. It sits directly under Actors so the DM runs the fight from the top of the page. -->

![[creature#Statblock]]

````col
```col-md
flexGrow=1
===
## Stage

- **Space.** Distances in feet, zones, and routes.
- **Feature.** What a character can do with it, and the ruling (cover, DC, damage).
- **Hazard.** What hurts anyone who stands in it, and the ruling.
- **Change.** How the space transforms, and on which round.
```

```col-md
flexGrow=1
===
## Pressure

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

## Spotlight

- **[[pc]].** The job their abilities fit here, or the stake it touches.

## Clues

- **Clue.** A short usable fact the contest can surface, and how.

## Outcomes

<!-- Required. One row per outcome the beat can plausibly produce: what changes and the beat it hands to. -->

| Outcome | What changes | Next | Narration |
| ------- | ------------ | ---- | --------- |
| **Objective gained** |  | [[Session-{{session}}-BB-label]] | _…_ |
| **Costly success** |  | [[Session-{{session}}-BB-label]] | _…_ |
| **Lost** |  | [[Session-{{session}}-BB-label]] | _…_ |
| **Broken off** |  | [[Session-{{session}}-BB-label]] | _…_ |

**Carry forward.** Each state the next beat inherits: positions, injuries, resources, who holds what.

> [!narration] If the session ends here
> <!-- The last words of the night when the session stops on this beat: one concrete image that makes the changed situation unmistakable, ending on the unanswered moment, one event, before anyone can act. -->
