---
title: "{{title}}"
category: journal
tags: ["{{campaign}}", session-prep]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: session-prep
kind: hook
reveal: unrevealed
campaign: "{{campaign}}"
session: ""
visibility: dm
card: ""
memorable: ""
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Keep a section only when this Hook spends it at the table; delete unused sections, bullets, rows, narration slots, and these comments. Completeness bar: docs/agents/table-ready.md. File as Session-<n>-<BB>-<label>.md. Inline image: optional `![[attachments/{slug}-{role}.ext|{{title}}]]` immediately next to what it shows (after `# title` for identity; directly above a creature `statblock` fence for overview). Role from wiki/attachments/README.md (`overview` `portrait` `banner` `reference` `handout` `teaser` `battlemap`). Keep the embed only if the file exists, or this is next-session prep and this agent can generate images (then generate the file; missing look still stops — no invented faces). Never inside `[!narration]` or `col`. No `## Art`. Foundry token is YAML `token`, never a body embed. -->

# {{title}}

<!-- Required. The lines the DM runs the beat by, one fact each. The card and the memorable element are design notes for agents: they go in the frontmatter, never the body. -->

**Starting situation.** Where everyone is and what they carry in from last session.
**Ends when.** The commitment that ends the beat: they give chase, take the job, flee.
**Next beat.** [[Session-{{session}}-BB-label]]

> [!narration] Previously
> <!-- First beat of the session only: last session's events in order, read aloud as play starts to remind the players what happened, one paragraph ending where play stopped (theatre-of-the-mind: Recap, read aloud). -->

> [!narration] Opening
> <!-- Read first: one paragraph, or immediate-fact bullets when the arrival is not fixed (theatre-of-the-mind: Hook opening). -->

````col
```col-md
flexGrow=1
===
## Situation

- **Where.** [[place]] — the features that matter right now.
- **What changed.** The event that makes this moment different.
- **Pressure.** What worsens, escapes, or arrives, and when.
```

```col-md
flexGrow=1
===
## Actors

- **[[npc]].** What they want and what they do next if nobody interferes.
- **[[creature]] × 3.** Opening move → adapts → break point → exit; HP or resources only when not full. The statblock is in Statblocks.
```
````

> [!narration] {NPC}
> <!-- Optional, one per NPC, titled with their name, in the order the party meets them: their first look and first words (theatre-of-the-mind: NPC first look, Dialogue). -->

> [!narration] {Creature}
> <!-- Optional, one per creature kind, titled with its name, in the order the party meets them: a few sentences; its response to the party stays in Actors (theatre-of-the-mind: Creature in scene). -->

## Party Choices

<!-- What the world does for each way the party can respond. Narration cells: a line or two in `_italic_` of what the party sees change (theatre-of-the-mind: Outcome cell). -->

| If the party… | The world responds | Narration |
| ------------- | ------------------ | --------- |
| **Engages**   |                    | _…_ |
| **Hesitates** | The pressure advances one visible step. | _…_ |
| **Walks away** | What happens without them, and the door that stays open. | _…_ |

## Checks

| Intent | Approach | DC | Success | Failure |
| ------ | -------- | -- | ------- | ------- |
|        | **Wisdom (Perception)** | `DC 13` |  |  |

## PC Hooks

- **[[pc]].** Why this matters to them now, or their obvious first job.

## Leads

<!-- Each lead with how it enters play and where it points. Give any conclusion the session needs three independent leads. -->

- **Lead.** How it enters play → [[page]]

## Outcomes

<!-- Required. One row per outcome the beat can plausibly produce: what changes and the beat it hands to. Narration cells: a line or two in `_italic_` of the changed state (theatre-of-the-mind: Outcome cell). -->

| Outcome | What changes | Next | Narration |
| ------- | ------------ | ---- | --------- |
|         |              | [[Session-{{session}}-BB-label]] | _…_ |

**Carry forward.** Each state the next beat inherits: who holds what, who is hurt, where the opposition went, what the party committed to.

## Statblocks

<!-- Only when the Hook can become a fight: one embed per fighter kind, from its owner page. -->

![[creature#Statblock]]
