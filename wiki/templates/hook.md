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
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Keep a section only when this Hook spends it at the table; delete unused sections, bullets, rows, narration slots, and these comments. Completeness bar: docs/agents/table-ready.md. File as Session-<n>-<BB>-<label>.md. -->

# {{title}}

## At a Glance

<!-- Required. Lead sentence: what happens right now and the choice it puts in front of the party. Then labelled facts, one bullet each. -->

- **Entry state.** Where everyone is and what they carry in from last session.
- **Stakes.** What changes if the party acts, and what changes if it does not.
- **Memorable.** The one image, object, or line the players will carry out of this beat.
- **Ends when.** The commitment that ends the beat: they give chase, take the job, flee.
- **Next.** [[Session-{{session}}-BB-label]]

> [!narration] Previously
> <!-- On the session's first beat only: the recap read aloud as play starts, from theatre-of-the-mind (Recap mode). -->

> [!narration] Opening
> <!-- Spoken opening from theatre-of-the-mind (Hook opening recipe): what the characters perceive, ending on a moment they can act on. -->

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
- **[[creature]] × 3.** AC, HP, Speed, the attack or save DC the DM rolls; opening move → adapts → break point → exit.

> [!narration] {NPC}
> <!-- Optional: the person as the party meets them here, from theatre-of-the-mind (NPC first look recipe): their face from the NPC page, what they are doing, and their first words in their voice. Titled with their name; one per NPC. -->

> [!narration] {Creature}
> <!-- Optional: the creature as the party meets it here, from theatre-of-the-mind (Creature in scene recipe): silhouette, movement, dangerous parts, scale, what it is doing now, ending before contact. Titled with its name; one per creature kind. -->
```
````

## Handles

| If the party… | The world responds | Narration |
| ------------- | ------------------ | --------- |
| **Engages**   |                    | _…_ |
| **Hesitates** | The pressure advances one visible step. | _…_ |
| **Walks away** | What happens without them, and the door that stays open. | _…_ |

## Checks

| Intent | Approach | DC | Success | Failure |
| ------ | -------- | -- | ------- | ------- |
|        | **Wisdom (Perception)** | `DC 13` |  |  |

## Spotlight

- **[[pc]].** Why this matters to them now, or their obvious first job.

## Leads

<!-- Each lead with how it enters play and where it points. Give any conclusion the session needs three independent leads. -->

- **Lead.** How it enters play → [[page]]

## Outcomes

<!-- Required. One row per outcome the beat can plausibly produce: what changes and the beat it hands to. -->

| Outcome | What changes | Next | Narration |
| ------- | ------------ | ---- | --------- |
|         |              | [[Session-{{session}}-BB-label]] | _…_ |

**Carry forward.** Each state the next beat inherits: who holds what, who is hurt, where the opposition went, what the party committed to.
