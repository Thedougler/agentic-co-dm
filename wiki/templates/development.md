---
title: "{{title}}"
category: journal
tags: ["{{campaign}}", session-prep]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: session-prep
kind: development
reveal: unrevealed
campaign: "{{campaign}}"
session: ""
visibility: dm
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Keep a section only when this Development spends it at the table; delete unused sections and these comments. Completeness bar: docs/agents/table-ready.md. File as Session-<n>-<BB>-<label>.md. -->

# {{title}}

## At a Glance

<!-- Required. Lead sentence: the turn — the fact, warning, or complication that changes what the party knows. Then labelled facts, one bullet each. -->

- **Entry state.** What the party carries in: position, condition, what they believe.
- **Trigger.** What brings this situation on screen.
- **New direction.** What the party can now pursue that it could not before.
- **Next.** [[Session-{{session}}-BB-label]]

> [!narration] Opening
> <!-- Spoken opening from theatre-of-the-mind (Development opening recipe): what the characters perceive, ending on a moment they can act on. -->

````col
```col-md
flexGrow=1
===
## Situation

- **Where.** [[place]]
- **Hands on.** The thing to search, examine, or witness, and what it reveals.
- **Friction.** What makes a clean answer hard.
- **Pressure.** What ends the talking if it circles, and when.
```

```col-md
flexGrow=1
===
## Actors

- **[[npc]].** Wants now; knows; offers; lies about, and the tell; price for help; what shifts their posture.

> [!narration] {Actor}
> <!-- Optional: the moment a key actor enters, from theatre-of-the-mind (Creature in scene or NPC first look recipe), "you" address. One block per actor the party meets here, titled with the actor's name. -->
```
````

## Handles

- **[[npc]]** can be persuaded, pressured, or exposed because…
- **[[item]]** can be examined, used, or traded because…

## Checks

| Intent | Approach | DC | Success | Failure |
| ------ | -------- | -- | ------- | ------- |
|        | **Intelligence (Investigation)** | `DC 13` |  |  |

<!-- Sensible actions with no real doubt succeed automatically; say what they yield in Clues. -->

## Clues

<!-- Truths stated as facts, each with where it surfaces. A conclusion the session needs gets three independent routes. -->

- [ ] **Core.** The truth that changes what the party knows or can do → surfaces through [[page]].
- [ ] **Support.** A fact about motive, stakes, or history → surfaces through [[page]].

> [!narration] Revelation
> <!-- The moment the Core clue lands, from theatre-of-the-mind (Revelation recipe): what the characters see or hear that makes the truth undeniable. -->

## Outcomes

<!-- Required. One row per outcome the beat can plausibly produce: what changes and the beat it hands to. -->

| If the party… | What changes | Next | Narration |
| ------------- | ------------ | ---- | --------- |
| Follows the clearest lead |  | [[Session-{{session}}-BB-label]] | _…_ |
| Refuses or delays |  | [[Session-{{session}}-BB-label]] | _…_ |

**Carry forward.** Each state the next beat inherits: new knowledge, direction, who is where, what they prepared.
