---
name: writing-player-prose
description: >-
  Write or revise player-facing prose in a Campaign OS repo — narration
  siblings, dialogue siblings, depictions, scene models, read-aloud,
  transitions, reveals, combat narration, consequences, recaps. The sole
  authority for prose that crosses the DM/player boundary: information
  boundary, agency, spoken standard, detail craft, scene procedures. Not
  DM-facing parent mechanics (draft-content) and not flowing narrative
  chapters (draft-story).
---

# Player-Facing Prose

Game-state communication through fiction. The prose lets players
understand the situation, notice what their characters would notice,
and decide what to do. Imagery, rhythm, and tone make that information
alive — they never replace it.

Priority order: **clarity > playability > imagination > emotion > style**.

## The human runtime

The DM speaks this prose, improvises around it, and reads the table.
The file is a *score* — complete enough to perform cold, loose enough
to riff on. One breath per sentence. Italic body, no H1, no callout.

## Scene model

Every file opens on one of two models. Pick before drafting:

| Model | Lens | Use when |
|---|---|---|
| **Scenic** (Mercer) | Camera on the world — the thing in motion, the wrong detail, the smell | Entity defaults, Situation portraits, establish/continue/transition narration |
| **Dramatic** (Mulligan) | Camera on the stakes — what just changed and what it costs | Reveals, consequences, combat narration, cliffhanger moments |

Both models serve clarity first. The scenic lens builds a picture the
table can act on; the dramatic lens names what just shifted so the table
knows the new situation. See [scene-model.md](references/scene-model.md).

## Choose the branch

| Branch | Trigger | Reference |
|---|---|---|
| **Establish** | `mode: establish` — first picture of a thing or place | [depiction.md](references/depiction.md) |
| **Continue** | `mode: continue` — what changed in the world | [depiction.md](references/depiction.md) |
| **Transition** | `mode: transition` — the crossing itself as a thing | [depiction.md](references/depiction.md) |
| **Session open** | `type: beat` or run-guide narration | [session-narration.md](references/session-narration.md) |
| **Recap** | `mode: recap` — Last Time | [session-narration.md](references/session-narration.md) |
| **Dialogue** | `type: dialogue` — spoken lines | [dialogue-forms.md](references/dialogue-forms.md) |
| **Scene model** | Building a full scenic or dramatic beat | [scene-model.md](references/scene-model.md), [scene-procedures.md](references/scene-procedures.md) |
| **General** | Any other player-facing prose | [prose-quality.md](references/prose-quality.md) |

## Workflow

1. **Read the parent** for scene context and `goal:`. The goal is the
   story or world fact this file tells the party
   ([goal.md](references/goal.md)).
2. **Pick the branch** from the table above. Read its reference.
3. **Write goal** — fewest words naming the fact the party learns.
4. **Draft A** — write the body following the branch reference, the
   [information boundary](references/information-boundary.md), and the
   [spoken standard](references/spoken-standard.md). Hook by sentence
   two. Italic. Present tense (recap: past tense).
5. **Draft B** — cut. Apply [prose-quality.md](references/prose-quality.md)
   and [detail-and-imagery.md](references/detail-and-imagery.md). Run the
   [checklist](references/checklist.md). Check word count against band.
6. **Write the file.** Lint: `npm run lint -- <path>`.

Full pipeline for complex scenes:
[writing-pipeline.md](references/writing-pipeline.md).

## Hard rules

1. Present tense, third person. Recap is past tense.
2. No hidden information crosses the boundary
   ([information-boundary.md](references/information-boundary.md)).
3. No prescribed player action or feeling
   ([player-agency.md](references/player-agency.md)).
4. Entity depictions: no `you`/`your`, no arrival, no pacing prompt
   ([depiction.md](references/depiction.md)).
5. Beat/run-guide narration: `you` stays off the picture; one earned
   CTA is allowed as a separate sentence after the picture.
6. Dialogue: speaker in italics (single) or bold (exchange). No
   quotation marks. No stage direction. First line is a question or
   demand ([dialogue-forms.md](references/dialogue-forms.md)).
7. Spoken standard: ≤ 30 seconds aloud per file. Word bands per mode
   ([spoken-standard.md](references/spoken-standard.md)).
8. One non-visual sense per depiction. One toy the table can touch.
9. Hook in the first two sentences — the thing in motion, the wrong
   detail, the smell that names the place.
10. The check's object is the toy. The picture never names the skill or
    DC. The DM speaks the picture, then calls the roll.
11. Every metaphor concrete and sensory. No abstractions as subjects.
12. Avoid every pattern in
    [anti-patterns.md](references/anti-patterns.md).

## Reference files

| File | Contents |
|---|---|
| [information-boundary.md](references/information-boundary.md) | What crosses DM/player boundary and what stays hidden |
| [player-agency.md](references/player-agency.md) | Agency contract — no prescribed actions or feelings |
| [spoken-standard.md](references/spoken-standard.md) | Word bands, breath test, timing |
| [scene-model.md](references/scene-model.md) | Scenic vs dramatic lens, when to use each |
| [scene-procedures.md](references/scene-procedures.md) | Step-by-step procedures for each scene type |
| [detail-and-imagery.md](references/detail-and-imagery.md) | Sensory detail, metaphor, imagery craft |
| [prose-quality.md](references/prose-quality.md) | Inflation filter, adjective/metaphor/cliché tests, Orwell |
| [depiction.md](references/depiction.md) | Entity/condition picture: camera, bound, modes |
| [session-narration.md](references/session-narration.md) | Beat opens, run-guide steps, recaps |
| [goal.md](references/goal.md) | Goal frontmatter: what fact the party learns |
| [dialogue-forms.md](references/dialogue-forms.md) | Single line vs exchange, word caps, formatting |
| [checklist.md](references/checklist.md) | Self-review checklist and fast quality heuristic |
| [anti-patterns.md](references/anti-patterns.md) | 13 named failure modes to avoid |
| [writing-pipeline.md](references/writing-pipeline.md) | Full 10-step pipeline for complex scenes |
| [exemplary-player-facing-prose.md](references/exemplary-player-facing-prose.md) | Worked examples: Mercer scenic, Mulligan dramatic |
