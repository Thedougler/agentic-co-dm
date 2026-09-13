# Data Model: Session Beat Skills

Entities are jobs and skills. No database.

## Composition skill

Name: `session-beats`. Primary when planning a session, one-shot, adventure arc, or expedition evening.

| Owns | Does not own |
|---|---|
| Beat Chart assembly | Type-card catalogs |
| One Hook; alternate D/C; Climax then Resolution | How to fill a typed beat |
| Polarity, ~30 min budget, 90 min core | Session 11 cockpit layout |
| Threads, escalation, transitions | Spoken player text (theatre of the mind) |
| Recompute / agency gates | Encounter/trap/place/monster math |
| Session plan (`kind: session-plan`) | Wiki write before accept; wiki kind pages |

## Type skill

One per Beat Chart type.

| Name | Type | Completes when |
|---|---|---|
| `hook-beats` | Hook | Party has committed to a response to the opening pressure. One Hook per session. |
| `development-beats` | Development | Players can name what they now know or can decide that they could not before. |
| `cliffhanger-beats` | Cliffhanger | The contest resolved; physical situation (position, resources, safety, time) changed. |
| `climax-beats` | Climax | Highest-stakes confrontation the middle made inevitable; threads harvested. |
| `resolution-beats` | Resolution | Players can name what is different and what they want next. |

Each owns: purpose, completion test, cards for that type, how to fill this beat from that type's draft template. Does not own Beat Chart assembly or another type's cards.

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
| Kind | `plan-session` \| `write-beat` \| `edit-beat` \| `fill-beat` \| `write-vehicle` \| `edit-vehicle` \| `write-spell` \| `edit-spell` \| `write-faction` \| `write-lore` \| `write-quest` \| `write-city` \| `write-region` \| `write-place` |
| Type | Empty on `plan-session`; beat type on beat jobs; empty on wiki-kind jobs |
| Primary skill | Composition if `plan-session`; beat type skill if beat job; see wiki-kind routing if wiki-kind job |
| Extra skills | Empty unless a named seam fires. `place-design` defers city → `city-design`, region → `region-design`. |

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

## Session-prep identity

Shared keys on every new live beat and session plan:

`title`, `category` (`journal`), `tags`, `sources`, `created`, `updated`, `type: session-prep`, `kind`, `lifecycle`, `reveal`, `campaign`, `session`, `visibility`, `summary`.

`kind` is `hook` | `development` | `cliffhanger` | `climax` | `resolution` | `session-plan`.

MUST NOT use `type: beat`, `type: session-beat`, or `type: session-plan`. Omit unused identity keys. Card, polarity, handoff, location, budget, and previous/next live in body jobs. Drop `intensity` and other draft extras that duplicate those jobs. Full map: [session-prep-pages.md](./contracts/session-prep-pages.md).

## Session plan

`type: session-prep`, `kind: session-plan`. Owner: `session-beats`. Scaffold: `wiki/templates/session-plan.md`. Not a live beat.

| Job | Done when |
|---|---|
| Compass | Opening situation; immediate pressure; session question; if the party does nothing; Now; On deck |
| Beat map | Hook first; alternating middle; Climax then Resolution; each row has trigger, what changes, hand-off, budget; links to typed beat pages |
| Floating beats | Optional beats with bring-in / job / drop — no mandatory slot |
| Pressure | Night-only steps without the party; not a second quest clock |
| PC touchpoints | What matters to each PC this session and which beat(s) touch it |

MUST NOT duplicate Scene ends when, Zones, or Be ready for. Optional draft sections (Branches & Skips, Critical Routes, Floating Secrets, Session Toolkit, Live Notes, After the Session, Prep Audit) omit when unused.

## Live beat

One ~thirty-minute slice. `type: session-prep` with `kind` matching the beat. Owner: that type skill. Scaffold: `wiki/templates/{hook,development,cliffhanger,climax,resolution}.md`. Session 11 is scan-quality evidence, not the heading spine. `run-guide` MUST NOT rewrite this page into a Session 11 cockpit.

Pass is the type's draft jobs plus readable scan (columns where a dashboard pair shares the scan). DM-facing callouts stay. `[!narration]` is the only player-spoken surface. Theatre of the mind owns `[!narration]`. Encounter, trap, place, and monster crafts keep their math and sites.

### Hook — `wiki/templates/hook.md`

| Job | Done when |
|---|---|
| At the table | Something happens; why it matters; the decision; Hook lands when |
| Open on | `[!narration]` the DM can speak; first changed thing |
| Situation | Where, who, what changed, pressure, open question |
| Run the hook | Engages / hesitates / rejects / surprises — world response, not a required sequence |
| Decision handles | At least two materially different approaches |
| Handoff | Next Development or Cliffhanger; carry-forward; continuity change |

Optional omit: Character pull, Leads, Checks, Action setup.

### Development — `wiki/templates/development.md`

| Job | Done when |
|---|---|
| Abstract | Purpose, trigger, turn, exit, ~30 min |
| Opening | `[!narration]` of what characters immediately perceive |
| Run the beat | Present → engage → make the turn → hand back the choice |
| Situation | Where, present, immediate want, friction, pressure, if ignored |
| Revelations | Core truth that changes what they know, want, or can do |
| Exits | Pursue / refuse / other — next page, not a required sequence |

Optional omit: Actors, Checks & Costs, Player Levers, required-conclusion redundancy, stall box, After Play.

### Cliffhanger — `wiki/templates/cliffhanger.md`

| Job | Done when |
|---|---|
| At a Glance | Trigger, PC objective, opposition objective, stakes, ends when |
| Open on Action | `[!narration]` of immediate danger; end on a decision |
| Run the beat | Opposition, default motion, pressure, leverage, danger, ways out (2+) |
| Resolution | Objective gained / costly success / withdrawal / unexpected |
| Handoff | Changed state; next Development |

Optional omit: Battlefield/Chase/Hazard, Discoveries, References.

### Climax — `wiki/templates/climax.md`

| Job | Done when |
|---|---|
| Run this | Party goal, opposition goal, stakes, pressure, end when, next Resolution |
| Opening image | `[!narration]` of the decisive situation |
| Situation | What is true now; if nobody interferes; visible levers |
| Pressure | Ticks that change the situation without dictating a response |
| Opposition | Wants, opening move, response, desperation, exit |
| Outcome | Possible state changes; hand off to Resolution |

Optional omit: Final Battle, Final Revelation, Stage, Payoffs, Live notes.

### Resolution — `wiki/templates/resolution.md`

| Job | Done when |
|---|---|
| Abstract | Follows Climax; purpose; one-sentence outcome |
| Run the beat | Confirm outcome → show consequence → pay stakes → let them react → end on an image |
| Closing image | `[!narration]` of the new status quo; no PC feelings or future |
| What is true now | Climax result, objective, opposition, stakes, price, reward, new status quo |
| Consequences | Party earned/paid/changed access; world people/places/power/evidence |

Optional omit: Payoffs, Character Epilogues, Loose Ends, Rewards, Stinger.

## Relationships

- `plan-session` → composition skill → session plan (`kind: session-plan`)
- fill slot → type skill → live beat (typed template)
- type skill → existing crafts (theatre of the mind, encounter-prep, traps-trials, place, monster, vehicle, spell, faction, lore, quest, city, region) by handoff
- `run-guide` may assemble hard-to-scan existing prep; it does not rewrite a typed beat into a Session 11 cockpit
- `write-vehicle` / `edit-vehicle` → `vehicle-design` → vehicle page
- `write-spell` / `edit-spell` → `spell-design` → spell page
- `write-faction` → `faction-design` → faction page; `world-tick` appends faction-turn log
- `write-lore` → `lore-design` → lore page; wrapup/reconcile append Canon Log after table witness
- `write-quest` → `narrative-islands` → quest page (owns later updates)
- `write-city` → `city-design` → city page; `place-design` defers
- `write-region` → `region-design` → region page; `place-design` defers
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

## Faction page

`type: faction`. Owner: `faction-design`. Scaffold: `wiki/templates/faction.md`. `faction-prep` removed.

| Job | Done when |
|---|---|
| Public face | `[!narration]` an informed person can observe |
| DM thesis | One sentence of campaign pressure |
| Current state | Status quo, recent change, pressure, strength, vulnerability |
| Active agenda | One concrete goal, next move, player opening |
| Table-relevant assets/people/places/relationships | Only what currently changes play |
| Faction-turn log | Current Turn named with no roll at create; `world-tick` appends resolved rows |

Agenda clock lives on the page. `hot.md` may point; no second clock.

## Lore page

`type: lore`. Owner: `lore-design`. Scaffold: `wiki/templates/lore.md`.

| Job | Done when |
|---|---|
| One question | Unrelated truths are split into linked notes |
| At a Glance | Core truth + why it matters |
| Current Truth | What is actually true now |
| At the Table | Notice / explains / enables / warns |

Not `canon` until players interact or witness. Canon Log omitted until then; wrapup/reconcile append. Not an `item`.

## Quest page

`type: quest`. Owner: `narrative-islands`. Scaffold: `wiki/templates/quest.md`. Replaces `type: front` and `type: encounter`.

| Job | Done when |
|---|---|
| Summary | Objective, why now, deadline |
| Situation | Unstable present; no prescribed party sequence |
| Stakes | Includes walk-away |
| World in motion | Driver and next move if uninterrupted |
| Leads | At least two independent routes |
| Resolution | Omitted while unresolved |

`narrative-islands` owns later updates including rolls and the Quest log.

## City page

`type: place`, `kind: city`. Owner: `city-design`. Hub: `place-design`. Scaffold: `wiki/templates/city.md`.

| Job | Done when |
|---|---|
| Arrival | `[!narration]` of entering or overlooking |
| At a glance | Includes current pressure |
| Orientation | Districts and getting around |
| Gazetteer | Enough to intentionally seek a place |
| Table rules | Law/weapons/magic/violence that change a choice |
| Active situation | At least one with if-nobody-intervenes; pursuable situations link a quest |

Faction full agendas stay on faction pages.

## Region page

`type: region`. Owner: `region-design`. Hub: `place-design`. Scaffold: `wiki/templates/region.md`.

| Job | Done when |
|---|---|
| Spoken look | `[!narration]` of first travel |
| At a glance | Scale, kind, character, anchor |
| Current state | Status quo now |
| Geography / travel | Enough to choose a route |
| Active powers | Few groups that can change the region |
| Change log | Deltas, not a rewrite |

MUST NOT invent pressure. If already stated, link that note. Scale omits extra headings.

## Place hub

`place-design` writes site places (`wiki/templates/place.md`). Defers `kind: city` to `city-design` and region jobs to `region-design`.

## Dispatch prompt

Claude Code runs only for novel skill design, skill redesign, or a major skill-file change. Model `claude-opus-4-6`, `--effort medium`. Prompt names Outcome, Files, Bounds, Job, deliverables, completion criteria. One designated writer at a time. Usage limit: defer that job on `tasks.md` with a retry time; complete remaining independent tasks; carry deferred tasks forward. Codex CLI at ChatGPT 5.5 medium MAY run the same prompt only when every remaining open task is blocked, no other work can be done, and that retry time is more than one hour away. Re-check those gates before each remaining blocked skill job; prefer Claude Code if it is usable again. If Codex is also usage-limited and Claude Code remains so, the session agent MAY write the design-impact change (constitution XI).

Novel this feature: `faction-design`, `lore-design`, `city-design`, `region-design`, `spell-design`. Redesign: `narrative-islands` (quest template); `session-beats` (fill session-plan draft, not Session 11-00 spine); `vehicle-design` (sheet fill). Session agent: templates, Layout, routing tables, type-skill template pointers, `run-guide` no-rewrite line, `faction-prep` deletion.
