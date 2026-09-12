---
type: craft
status: canon
publish: false
aliases: []
created: "2026-07-31"
updated: "2026-08-15"
tags: [craft]
summary: "Player-facing vs DM-facing prose register: which bar applies where, the REGISTER line, the fixed tense per register, and the failure modes for each direction."
uid: 2b4284ed-0056-4b3e-b747-02ce56287815
---

# Register — Player-Facing vs DM-Facing Prose

Every passage in campaign prose serves one of two audiences. Word-level
[[ai-tells|AI-tells]] (flat description, hedging, filler) are
[ai-tells.md](ai-tells.md)'s territory — this file owns which register
applies where, what each register's bar is, and the weight the material
sets.

## The weight is not the writer's choice

"Style is free" (`vault/CLAUDE.md` rule 10) frees *voice, structure,
imagery, and risk*. It never frees register. The weight of what is happening
on the page is a fact of the material, and the prose matches it or fails.

Before the first sentence of any narrative prose, name the weight in one line:

```text
REGISTER: <what happens> -> <the weight it carries>
```

("Halvard drowns saving her -> a death, and the loss of the person who taught
her the water.") Every sentence after that is written at that weight. A beat
carrying a death, a grief, a mutilation, a betrayal, or a terror is rendered
from inside the body and the present pressure — what the hands are doing, what
the lungs cost, what can and cannot be reached.

The failure this exists to stop: a charged beat arriving in a register
borrowed from somewhere lighter — the amused anecdote told safely afterward,
the procedural summary, the workplace vocabulary of ledgers, logistics,
capacity, and protocol. The prose says a tragedy occurred while sounding like
nothing much did. When a passage feels flat, the diagnosis is almost always
register, not word choice: check the weight first, then the sentence.
[banned-patterns.md](banned-patterns.md) records each specific instance of
this failure the GM has caught.

## The two registers

| Register | Applies to | Bar |
|---|---|---|
| Player-facing | `type: narration` files, `type: dialogue` files, recap prose, lore/quest text meant to reach the table | `.claude/skills/writing-player-prose/SKILL.md` owns the full bar — information boundary, agency, spoken standard, detail craft. |
| DM-facing | Setup paragraphs, branch points, tactic lines, `[!mechanic]` blocks, section intros, prep notes | Clear, concise, terse, instruction-first — built to be parsed mid-session under time pressure. |

## Failure modes

- **Player-facing below bar:** a flat or generic read-aloud ("you see a
  large room with enemies in it"), tell-not-show emotion ("it feels
  ominous"), stock fantasy filler with no anchored detail, or a scene the
  DM would still have to improvise the basic physical facts of.
- **DM-facing below bar:** hedging ("perhaps consider", "you might want
  to"), filler before the instruction, atmospheric padding where a number
  or name belongs, the same instruction restated in consecutive sentences,
  or a load-bearing mechanic buried inside narrative prose.
- **Negative-outcome padding:** stating what a check does *not* find or
  what stays unnoticed ("the character's eye passes over the stones but
  registers nothing unusual") costs words without giving the DM anything
  to run. State only the useful fact — the number, the name, the
  mechanism — never the absence.
- **Wall-of-prose DM text:** a `## What Happens`/body paragraph running
  180+ words with no bolded lead and a vague consequence buried mid-sentence
  ("the weather turns personal" — what weather, doing what?) instead of a
  stated mechanic. Caught instance: a moment's whole payoff — pay clean vs.
  debt sails — sat inside one undifferentiated paragraph with the NPC's
  in-character licking-the-pencil business interleaved between the two
  branches, so the DM had to parse fiction and consequence out of the same
  run-on. Fix: bold the fork (**Pay:**/**Refuse:**), state each branch's
  concrete result in its own clause, and move the in-character texture into
  the read-aloud box where it belongs — DM-facing prose states the fork, it
  doesn't perform it (`vault/refs/vault/_common/hard-rules.md` § Scan
  Structure).
- **Wrong register entirely:** DM mechanics (DCs, HP, roll numbers,
  encounter-design language) leaking into player-facing prose, or a terse
  DM-note register where evocative prose was needed.

## How to check

Identify each passage's intended audience, check it against that
register's bar in both directions, and quote the miss. A stylistic choice
that still serves its audience is not a finding — flag the register, not
the taste.

## Tense

Fixed per register so no writer picks at random:

- Stories (`vault/stories/**`, `vault/episodes/**/session-*.md`), recaps, retrospectives: **past tense**.
- Read-aloud boxes and player-facing moment text: **present tense**
  (`.claude/skills/writing-player-prose/references/depiction.md`,
  `.claude/skills/writing-player-prose/references/session-narration.md`).

A shape plan (draft-story DS4) may override for one piece by naming the
tense and the reason beside its REGISTER line; silence means the default.
