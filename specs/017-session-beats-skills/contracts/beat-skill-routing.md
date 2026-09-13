# Contract: Beat skill routing

The interface is a session-prep job. Co-DM is the author. Naming the wrong primary skill is a fail. Opening another type-card catalog off a named seam is a fail.

## Routing table

| Job | Primary skill |
|---|---|
| Plan a session, one-shot, adventure arc, or expedition evening | `session-beats` |
| Write, edit, or create content for a Hook | `hook-beats` |
| Write, edit, or create content for a Development | `development-beats` |
| Write, edit, or create content for a Cliffhanger | `cliffhanger-beats` |
| Write, edit, or create content for a Climax | `climax-beats` |
| Write, edit, or create content for a Resolution | `resolution-beats` |

Unknown typed-beat job → classify the type first; do not default to `session-beats` for filling a beat.

## Classification jobs

A second reviewer must name the same primary skill (SC-001). At least these fifteen:

| # | Job | Primary |
|---|---|---|
| 1 | Plan tonight's session / draw the Beat Chart | `session-beats` |
| 2 | Write a new Hook | `hook-beats` |
| 3 | Edit an existing Hook | `hook-beats` |
| 4 | Create content for a Hook (opening pressure, spoken start, landing) | `hook-beats` |
| 5 | Write a new Development | `development-beats` |
| 6 | Edit an existing Development | `development-beats` |
| 7 | Create content for a Development | `development-beats` |
| 8 | Write a new Cliffhanger | `cliffhanger-beats` |
| 9 | Edit an existing Cliffhanger | `cliffhanger-beats` |
| 10 | Create content for a Cliffhanger | `cliffhanger-beats` |
| 11 | Write a new Climax | `climax-beats` |
| 12 | Edit an existing Climax | `climax-beats` |
| 13 | Create content for a Climax | `climax-beats` |
| 14 | Write or edit a Resolution | `resolution-beats` |
| 15 | Create content for a Resolution | `resolution-beats` |

## Named-seam jobs

Reviewers must also agree which extra skill may load:

| # | Job | Primary | Extra |
|---|---|---|---|
| 16 | Chart is done; fill the Hook slot | `hook-beats` | composition already used for the chart |
| 17 | Writing a Development; polarity of the next beat is unclear | `development-beats` | `session-beats` for the chart question |
| 18 | Play a Cliffhanger as Hook | `hook-beats` | `cliffhanger-beats` for opening shape |
| 19 | Play a Development as Hook | `hook-beats` | `development-beats` for opening shape |
| 20 | How the Scene Resolves names a Chase next | current type | `cliffhanger-beats` for the handoff only |

## Chart rules (composition)

1. One Hook to start.
2. Developments and Cliffhangers only in alternating order.
3. One Climax followed by one Resolution.
4. Action Hook → next Development; cerebral Hook → next Cliffhanger.
5. Action Climax preceded by Development; cerebral Climax preceded by Cliffhanger.
6. About thirty minutes per beat; Hook + Climax + Resolution about ninety minutes.
7. Every prepared beat advances a live thread.
8. At least two viable player responses; recompute rather than force the next slot.

## Isolation rules

1. A `plan-session` job does not require any type-card catalog.
2. A typed-beat job with no named seam does not open the other four type-card catalogs.
3. Composition does not include the five type-card catalogs.
4. A type skill does not include the full Beat Chart or another type's cards.
5. After the split, no skill contains both the full Beat Chart and all five type-card catalogs.
6. Play a Cliffhanger/Development as Hook remains one Hook for the session.
7. Cockpit layout stays `run-guide`. Work accept-gate stays Work. Spoken text stays theatre of the mind. Wiki kind pages stay their owners in [wiki-kind-pages.md](./wiki-kind-pages.md).
8. Existing Session 11 beats are not rewritten to prove this contract.

## Out of contract

How the designated writer phrases a skill. One skill per subtype card. Campaign OS `composing-beats` / `writing-*-beats`. The article skill `writing-beats`. Foundry staging. Cold opens (not a Hook). Wiki kind page jobs ([wiki-kind-pages.md](./wiki-kind-pages.md)).
