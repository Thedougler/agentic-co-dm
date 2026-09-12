# Data Model: Theatre of the Mind Authoring

Entities are jobs and spoken surfaces. No database.

## TotM job

One act of authoring player-facing theatre of the mind.

| Field | Rule |
|---|---|
| Reader | Players (spoken or shown by the DM). Never the wiki's DM bands. |
| Mode | Situated moment (table or Beat state supplied) \| wiki portrait (standalone; no party/encounter) |
| Surface | Scene opening \| reveal \| combat opening \| escalation \| portrait \| recap/hit/update |
| Beat | Hook \| Development \| Cliffhanger \| Climax \| Resolution, or none (portraits and short updates) |
| Beat job | One sentence. Required when Beat is set. Decorative prose with no job is incomplete. |
| Runtime | Prep only. Incomplete if it can only be written after players act. |

Incomplete: PC action/thought/emotion/intent/choice/success/unresolved outcome; secrets, DCs, unearned names, hidden causes, agent-process language in the spoken block.

## Narration block

One complete player-facing spoken picture.

| Field | Rule |
|---|---|
| Layer | 1 immediate frame \| 2 salient reveal \| 3 discoverable reveal |
| State independence | Usable if approach changes, unless the Beat guarantees the world state |
| Hierarchy | Most important perceptible thing first. Not an architectural inventory. |
| Relationships | Important elements related (beneath, beyond, between, blocking, …) |
| Live ending | Openings end on danger, contradiction, question, opportunity, demand, objective, or change — not a chosen response |
| Length | Shortest block that makes a stable picture and performs the job. Not a word-count pass/fail. |

Layer 1 is the opening. Layers 2–3 are separate complete reveal blocks (discovery, not method). Actionable features that matter now belong in Layer 1 before a player would need them.

## Wiki portrait

Standalone first-impression of an owner.

| Field | Rule |
|---|---|
| Subject | Place, person, creature, ship, artifact, faction, landmark, region, or equivalent owner |
| Validity | Across sessions. No current party state. No assumed encounter. |
| Transient facts | Omitted or clearly labeled |
| Completeness | Recognizable identity anchors. Not every parent heading. |

Not a Beat. Not a scene script.

## Combat package

Situated Work when violence is imminent.

| Field | Rule |
|---|---|
| Opening | Spoken. Threats, relationships, objectives, relational distance, terrain, cover, hazards, opportunities, routes, exceptional conditions. Clarity over flourish. |
| Distance | Melee \| Near \| Far in player-facing look. Exact measure only if a rule or encounter requires it. |
| Cluster | Grouping legible enough to answer a reasonable area-effect question. |
| Tactical reference | DM-only. Lives on the existing beat-card slots (zones, action cards, procedure). Not a TotM parallel card. |
| Escalation / reveal | World-triggered. Complete. Does not assume PC behavior. |
| Forbidden | Turn-by-turn script; top-of-round summary; hidden-grid coordinates in spoken look. |

## Interactive problem

Trap, hazard, trial, betrayal, or sabotage the party can engage.

| Field | Rule |
|---|---|
| Visible symptom or clue | In this scene's fiction or an earlier one |
| Solution | Available in play. Not announced in the spoken look. |
| Betrayal / sabotage | Detectable, preventable, or respondable before irreversible |

Incomplete: solvable only by omitted information; predetermined betrayal with no chance to notice.

## Prepared scene facts

What the DM must have. Shape follows the host surface.

| Fact | Beat card home | Other host |
|---|---|---|
| Beat + job | Spine / glance | Named when the job is a scene |
| Player-facing narration | `[!narration]` | The spoken block |
| Fixed scene truths | Now | Short DM list if needed |
| Actionable features | Zones / scene stock | Named in or beside the block |
| Spatial relationships | Zones (feet/compass OK for DM) | Relational bands in spoken look |
| Reveals | Zone / tick / stub Narration cells | Separate reveal blocks |
| Hidden / adjudication | Be ready for, procedure | DM notes, never inside spoken look |

Omit empty sections. Do not add a second cockpit.

## Relationships

- TotM job → one or more narration blocks
- Situated Beat job → Beat type + job + Layer 1 opening; reveals as needed
- Wiki portrait job → standalone portrait; no Beat required
- Combat package → opening (TotM) + tactical reference (existing DM slots) + optional escalations
- Interactive problem → symptom/clue in fiction; reveal may deepen it
- 010 authorities still stack; this model does not reassign them
- 007 cockpit still hosts FR-032 facts; this model does not replace it
