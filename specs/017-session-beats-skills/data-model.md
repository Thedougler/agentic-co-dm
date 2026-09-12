# Data Model: Session Beat Skills

Entities are jobs and skills. No database.

## Composition skill

Name: `session-beats`. Primary when planning a session, one-shot, adventure arc, or expedition evening.

| Owns | Does not own |
|---|---|
| Beat Chart assembly | Type-card catalogs |
| One Hook; alternate D/C; Climax then Resolution | How to fill a typed beat |
| Polarity, ~30 min budget, 90 min core | Session 11 cockpit layout (`run-guide`) |
| Threads, escalation, transitions | Spoken player text (theatre of the mind) |
| Recompute / agency gates | Encounter/trap/place/monster math |
| Filed spine jobs (007) | Wiki write before accept; vehicle and spell pages |

## Type skill

One per Beat Chart type.

| Name | Type | Completes when |
|---|---|---|
| `hook-beats` | Hook | Party has committed to a response to the opening pressure. One Hook per session. |
| `development-beats` | Development | Players can name what they now know or can decide that they could not before. |
| `cliffhanger-beats` | Cliffhanger | The contest resolved; physical situation (position, resources, safety, time) changed. |
| `climax-beats` | Climax | Highest-stakes confrontation the middle made inevitable; threads harvested. |
| `resolution-beats` | Resolution | Players can name what is different and what they want next. |

Each owns: purpose, completion test, cards for that type, how to fill this beat. Does not own Beat Chart assembly or another type's cards.

## Card

A proven shape under one type (Discovery, Chase, Clue, Final Battle, Happy Ending, and the rest already in campaign use).

| Field | Rule |
|---|---|
| Type | Exactly one of the five |
| Trigger | When fiction calls for it — not to fill a slot |
| Stakes | Visible |
| Player options | At least two viable responses |
| Agency note | Ignoring, failing, or redirecting updates the world |

Play a Cliffhanger as Hook and Play a Development as Hook are Hook cards that load the borrowed type skill only for that opening shape.

## Job

One act of planning, writing, editing, or filling.

| Field | Rule |
|---|---|
| Kind | `plan-session` \| `write-beat` \| `edit-beat` \| `fill-beat` \| `write-vehicle` \| `edit-vehicle` \| `write-spell` \| `edit-spell` |
| Type | Empty on `plan-session`; beat type on beat jobs; empty on vehicle/spell jobs |
| Primary skill | Composition if `plan-session`; beat type skill if beat job; `vehicle-design` if vehicle job; `spell-design` if spell job |
| Extra skills | Empty unless a named seam fires |

## Named seam

A job that may load a second skill.

| Seam | Loads |
|---|---|
| Composition filling a typed slot | That type skill; type becomes primary for the fill |
| Typed-beat job needs chart position, polarity, threads, or transition | Composition, not as primary for writing the beat |
| Play a Cliffhanger as Hook | `cliffhanger-beats` for opening shape; beat remains the session's one Hook |
| Play a Development as Hook | `development-beats` for opening shape; beat remains the session's one Hook |
| How the Scene Resolves names the next type | That next type skill for the handoff only |

Any other extra type-card catalog is a defect.

## Beat Chart

Order: Hook → alternating Development/Cliffhanger pairs → Climax → Resolution.

| Rule | Check |
|---|---|
| One Hook | First live beat only |
| Alternate middle | No two Developments or two Cliffhangers consecutive |
| Polarity after Hook | Action Hook → next is Development; cerebral Hook → next is Cliffhanger |
| Polarity before Climax | Action Climax ← Development; cerebral Climax ← Cliffhanger |
| End | Climax then one Resolution |
| Budget | ~30 min per beat; Hook+Climax+Resolution ~90 min |
| Threads | Every prepared beat advances a live thread; Climax harvests; Resolution shows final state |
| Agency | Situations not required outcomes; recompute; chart may shrink/branch/pause/end early |

## Relationships

- `plan-session` → composition skill → spine (007)
- fill slot → type skill → live beat (007 cockpit via `run-guide`)
- type skill → cards of that type only
- type skill → existing crafts (theatre of the mind, encounter-prep, traps-trials, place, monster, vehicle, spell) by handoff
- `write-vehicle` / `edit-vehicle` → `vehicle-design` → vehicle page
- `write-spell` / `edit-spell` → `spell-design` → spell page
- Work remains Work until DM accept

## Vehicle page

`type: vehicle`. Owner: `vehicle-design`. Scaffold: `wiki/templates/vehicle.md`.

| Job | Done when |
|---|---|
| Spoken look | `[!narration]` a body can picture at distance |
| Sheet | Size, type, speed, crew (min), passengers, cargo filled so the craft can enter play |
| Components | Hull AC/HP/DT; helm; movement; weapons when armed |
| Crew & stations | Named stations and current vs minimum complement |
| Handling | Conditions, maneuvers, limits that change a choice |
| Combat | Initiative, ramming, boarding, destruction when the craft fights |

Theatre of the mind owns `[!narration]`. Omit unused sections.

## Spell page

`type: spell`. Owner: `spell-design`. Scaffold: `wiki/templates/spell.md`.

| Job | Done when |
|---|---|
| Spoken look | `[!narration]` of what a bystander sees, hears, and feels at the casting |
| Classification | Level, school, ritual line |
| Effect | 2024 runnable block: time, range, components, duration, saves, damage, conditions; scaling when it scales |
| Discovery | Filled when the spell needs a scroll, book, teacher, or patron |
| Lore | Filled when the spell needs history |

Theatre of the mind owns `[!narration]`. Omit unused sections.

## Dispatch prompt

Claude Code skill-update jobs: model `claude-opus-4-6`, `--effort medium`. Prompt names Outcome, Files, Bounds, Job, deliverables, completion criteria.
