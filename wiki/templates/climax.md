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
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Keep a section only when this Climax spends it at the table; keep Final Battle or Final Revelation for the shape in play. Delete unused sections, bullets, rows, narration slots, and these comments. Completeness bar: docs/agents/table-ready.md. File as Session-<n>-<BB>-<label>.md. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

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
> <!-- Read first: one paragraph, or immediate-fact bullets when the arrival is not fixed (theatre-of-the-mind: Climax opening). -->

## Thread Harvest

<!-- One line per live thread: the lever it gives the party here. -->

- **[[thread]]** (planted in [[beat]]) — the lever it gives here.

## Actors

<!-- Statblocks live in Roster; each line here carries only this fight's state (HP when not full, spent resources) and what the actor does. Add Wants, Leverage, or Line only when it changes what they do at the table. -->

- **[[npc]].** The primary opposition, at its HP and resources this fight.
  - **Plays.** Opening move → response when countered → desperation → exit, and how the party can close the exit.
- **[[creature]] × 4.** Role (henchman, minion, or hazard) and what they do.

> [!narration] {NPC}
> <!-- Optional, one per NPC, titled with their name, in the order the party meets them: their first look and first words (theatre-of-the-mind: NPC first look, Dialogue). -->

> [!narration] {Creature}
> <!-- Optional, one per creature kind, titled with its name, in the order the party meets them: a few sentences; its response to the party stays in Actors (theatre-of-the-mind: Creature in scene). -->

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

<!-- Narration cells: a line or two in `_italic_` per phase of what the party sees and hears change (theatre-of-the-mind: Tick cell). -->

| Phase | Trigger | What changes | Narration |
| ----- | ------- | ------------ | --------- |
| 1     | Opening |              | _…_       |

## Final Revelation

- **The truth.** What actually happened, stated as fact.
- **Proof on the table.** [[page]] — what it establishes, and the beat where the party got it.
- **Resistance.** [[npc]] — their claim, what breaks it, and their last move when cornered.
- **Wrong accusation.** What happens if the party names the wrong culprit.

> [!narration] Revelation
> <!-- Only with Final Revelation: the moment the truth lands, one short paragraph (theatre-of-the-mind: Revelation). -->

## Spotlight

- **[[pc]].** The thread, foe, or feature that calls on them here.

## Outcomes

<!-- Required. One row per way the climax can end: what becomes true and the cost paid. Narration cells: a line or two in `_italic_` that lets that ending land (theatre-of-the-mind: Outcome cell). -->

| If the climax ends with… | What becomes true | Cost paid | Narration |
| ------------------------ | ----------------- | --------- | --------- |
| **Victory**              |                   |           | _…_       |
| **Costly victory**       |                   |           | _…_       |
| **Opposition wins**      |                   |           | _…_       |

**Carry forward.** Who and what remains active, and each state the Resolution inherits.

## Roster

<!-- One embed per fighter kind the party could face, from its owner page. -->

![[creature#Statblock]]
