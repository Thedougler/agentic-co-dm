---
title: "{{title}}"
category: journal
tags: ["{{campaign}}", session-prep]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: session-prep
kind: climax
reveal: unrevealed
campaign: "{{campaign}}"
session: ""
visibility: dm
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Keep a section only when this Climax spends it at the table; keep Final Battle or Final Revelation for the shape in play. Delete unused sections, bullets, rows, narration slots, and these comments. Completeness bar: docs/agents/table-ready.md. File as Session-<n>-<BB>-<label>.md. -->

# {{title}}

## At a Glance

<!-- Required. Lead sentence: the question this beat settles for good. Then labelled facts, one bullet each. -->

- **Entry state.** Positions, resources, allies, and what the party prepared.
- **Party objective.** What the characters can accomplish here.
- **Opposition wants.** What the opposition is trying to make true, and why it cannot wait.
- **Stakes.** What changes if the party wins, loses, bargains, or walks away.
- **If behind.** How to compress it (fewer phases, faster Pressure) and still settle the question.
- **Next.** [[Session-{{session}}-BB-label]]

> [!narration] Opening
> <!-- Spoken opening from theatre-of-the-mind (Climax opening recipe): one paragraph running toward 150 words, the opposition mid-act, the stakes, and the stage, ending on the escalation before it lands. The villain's speech stays out; taunts are short lines in Actors. -->

## Thread Harvest

<!-- One line per live thread: the lever it gives the party here. -->

- **[[thread]]** (planted in [[beat]]) — the lever it gives here.

## Actors

- **[[npc]].** The primary opposition.
  - **State.** HP when not full, spent resources and legendary uses, conditions. Its numbers arrive by the Statblocks embed.
  - **Wants.** What they are trying to make true, and why now.
  - **Leverage.** What they hold over the party or the stakes.
  - **Plays.** Opening move → response when countered → desperation.
  - **Line.** What they will not do, even to win.
  - **Morale.** When they surrender, bargain, or flee, and where.
- **[[creature]] × 4.** Role (henchman, minion, or hazard) and numbers.

> [!narration] {NPC}
> <!-- Optional: the person as the party meets them here, from theatre-of-the-mind (NPC first look recipe): their face from the NPC page, what they are doing, and one line of first words in their voice, about six seconds aloud. What they know beyond that line goes in Actors as separate points. Titled with their name; one per NPC. -->

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

| Feature | What characters can do | Ruling |
| ------- | ---------------------- | ------ |
| [[page]] |                       |        |

**Space.** The distances in feet that make positioning matter.

**Collateral.** Who or what nearby can be lost if the fight spills over.
```

```col-md
flexGrow=1
===
## Pressure

- [ ] **1. Warning.** What the players see coming.
- [ ] **2. Escalation.** The safety removed or opposition strengthened.
- [ ] **3. Crisis.** The hard choice.
- [ ] **4. Consequence.** The opposition gets what it wants.

**Ticks when.** A round passes, an action fails, or a threat is ignored.

**If it goes static.** The move that breaks a stalemate.
```
````

## Final Battle

- **Win by.** The objective beyond dropping every enemy.
- **Lose when.** The opposition gets what it wants.

| Phase | Trigger | What changes | Narration |
| ----- | ------- | ------------ | --------- |
| 1     | Opening |              | _…_       |

## Final Revelation

- **The truth.** What actually happened, stated as fact.
- **Proof on the table.** [[page]] — what it establishes, and the beat where the party got it.
- **Resistance.** [[npc]] — their claim, what breaks it, and their last move when cornered.
- **Wrong accusation.** What happens if the party names the wrong culprit.

> [!narration] Revelation
> <!-- The moment the truth lands, from theatre-of-the-mind (Revelation recipe): what the characters see or hear that makes it undeniable. -->

## Spotlight

- **[[pc]].** The thread, foe, or feature that calls on them here.

## Outcomes

<!-- Required. One row per way the climax can end: what becomes true and the cost paid. -->

| If the climax ends with… | What becomes true | Cost paid | Narration |
| ------------------------ | ----------------- | --------- | --------- |
| **Victory**              |                   |           | _…_       |
| **Costly victory**       |                   |           | _…_       |
| **Opposition wins**      |                   |           | _…_       |

**Carry forward.** Who and what remains active, and each state the Resolution inherits.
