# Contract: Session-prep pages

The interface is a new live beat or session plan. Co-DM is the author. Wrong `type`/`kind` is a fail. Session 11 heading order as the pass test is a fail. Missing a filled required job is a fail.

Skill routing, seams, and chart rules: [beat-skill-routing.md](./beat-skill-routing.md). Wiki kinds: [wiki-kind-pages.md](./wiki-kind-pages.md).

## Type and kind

| Page | `type` | `kind` | Scaffold | Owner |
|---|---|---|---|---|
| Session plan | `session-prep` | `session-plan` | `wiki/templates/session-plan.md` | `session-beats` |
| Hook | `session-prep` | `hook` | `wiki/templates/hook.md` | `hook-beats` |
| Development | `session-prep` | `development` | `wiki/templates/development.md` | `development-beats` |
| Cliffhanger | `session-prep` | `cliffhanger` | `wiki/templates/cliffhanger.md` | `cliffhanger-beats` |
| Climax | `session-prep` | `climax` | `wiki/templates/climax.md` | `climax-beats` |
| Resolution | `session-prep` | `resolution` | `wiki/templates/resolution.md` | `resolution-beats` |

MUST NOT add `type: beat`, `type: session-beat`, or `type: session-plan`. `wiki/templates/session-prep.md` is not copy-start for these pages.

`category` is `journal`. File after accept to `wiki/journal/sessions/<campaign-slug>/<session-number>/` as `Session-<n>-00-<Title>.md` (plan) or `Session-<n>-<BB>-<Label>.md` (live beat). Do not use the draft `{{title}} - B01 - Strong Start` filename scheme.

## Shared identity

Present on every new live beat and session plan:

| Key | Value |
|---|---|
| `title` | page title |
| `category` | `journal` |
| `tags` | list; omit empty |
| `sources` | list |
| `created` | `YYYY-MM-DD` |
| `updated` | `YYYY-MM-DD` |
| `type` | `session-prep` |
| `kind` | see table above |
| `lifecycle` | `draft` \| `proposed` \| `accepted` \| `rejected` \| `canon` |
| `reveal` | `unrevealed` \| `revealed` |
| `campaign` | campaign slug |
| `session` | session number |
| `visibility` | `dm` |
| `summary` | one sentence |

`type` and `kind` are never omitted. Other unused identity keys omit.

## Draft rewrite

Illegal draft `type` / `beat` / `beat_type` / `category` rewrite on install. Extra draft keys that duplicate body jobs or `kind` are dropped, not copied onto other pages.

| Draft | Becomes |
|---|---|
| `type: session-beat` / `type: beat` / `type: session-plan` | `type: session-prep` |
| `beat:` / `beat_type:` | `kind:` matching that page |
| `category: sessions` / `beats` / `session-beats` | `category: journal` |
| empty Cliffhanger `kind:` | drop — discriminator is `kind: cliffhanger` |
| `intensity`, `pacing`, `card` / `hook_kind` / `development_type` / `climax_kind`, `estimated_minutes` / `target_minutes` / `duration`, `order` / `sequence`, `location`, `previous` / `next` / `next_beat` / `next_beat_type` / `previous_beat` / `resolution_beat` / `follows`, `participants`, `status`, `date`, `planned_length`, `previous_session`, `next_session` | drop — body jobs or shared keys already cover them |

## Layout

Keep draft jobs. Shape into the current wiki-template family: `col` / `col-md` where a pair of scan jobs share a dashboard; tables; omit unused. DM-facing callouts stay. `[!narration]` is the only player-spoken surface. Pass is jobs plus readable scan, not heading-order match. Strip HTML design-basis comments and citation crumbs on install. Session-plan comment that treats alternation as optional MUST NOT ship — FR-010 still binds; FR-011 still allows skip/reorder after play.

`run-guide` MUST NOT rewrite a typed beat into a Session 11 cockpit. Work accept-gate stays Work. Theatre of the mind owns `[!narration]`. Existing Session 11 files are not rewritten to prove this contract.

## Session plan jobs — `wiki/templates/session-plan.md`

Required:

| Job | Done when |
|---|---|
| Compass | Opening situation; immediate pressure; session question; if the party does nothing; Now; On deck |
| Beat map | Hook first; alternating middle; Climax then Resolution; trigger, what changes, hand-off, budget; links to typed beat pages |
| Floating beats | Bring-in / job / drop; no mandatory slot |
| Pressure | Night-only steps without the party |
| PC touchpoints | What matters to each PC this session and which beat(s) touch it |

Omit-if-unused (still in the scaffold):

| Job | Done when |
|---|---|
| Branches & Skips | Meaningful routes only |
| Critical Routes | Chokepoints with three independent paths |
| Floating Secrets & Clues | Unattached facts until play places them |
| Session Toolkit | Places, people, opposition, rewards, rules |
| If play stalls | Advance pressure / surface information / floating beat / ask intent |
| Live Notes | State changes, questions, beat checklist |
| Prep Audit | Chart and agency checks |
| After the Session | Carry forward: actual ending, unresolved pressure, next opening |

MUST NOT duplicate Scene ends when, Zones, or Be ready for.

## Hook jobs — `wiki/templates/hook.md`

Required:

| Job | Done when |
|---|---|
| At the table | Something happens; why it matters; the decision; Hook lands when |
| Open on | `[!narration]` the DM can speak; first changed thing |
| Situation | Where, who, what changed, pressure, open question |
| Run the hook | Engages / hesitates / rejects / surprises |
| Decision handles | At least two materially different approaches |
| Handoff | Next Development or Cliffhanger; carry-forward; continuity change |

Omit-if-unused:

| Job | Done when |
|---|---|
| Character pull | PC / existing tie and why it matters now |
| Leads | Three independent leads if play depends on reaching a conclusion |
| Checks | Uncertain outcomes with meaningful cost; failure does not erase the Hook |
| Action setup | Objective, opposition, terrain, escalation, end condition — only if the Hook opens in peril |

## Development jobs — `wiki/templates/development.md`

Required:

| Job | Done when |
|---|---|
| Abstract | Purpose, trigger, turn, exit, ~30 min |
| Opening | `[!narration]` of what characters immediately perceive |
| Run the beat | Present → engage → make the turn → hand back the choice |
| Situation | Where, present, immediate want, friction, pressure, if ignored |
| Revelations | Core truth that changes what they know, want, or can do |
| Exits | Pursue / refuse / other |

Omit-if-unused:

| Job | Done when |
|---|---|
| Required conclusion | Three independent routes when a conclusion must be reached |
| Actors | Beat-specific wants, leverage, posture |
| Checks & Costs | Automatic vs DC; failure still moves play |
| Player Levers | Person / thing / place / promise they can act on |
| If the Beat Stalls | Actor want / unrevealed fact / pressure / restated handles |
| After Play | What happened, revelations, decision, posture, resources, next node, unresolved thread |

## Cliffhanger jobs — `wiki/templates/cliffhanger.md`

Required:

| Job | Done when |
|---|---|
| At a Glance | Trigger, PC objective, opposition objective, stakes, ends when |
| Open on Action | `[!narration]` of immediate danger; end on a decision |
| Run the beat | Opposition, default motion, pressure, leverage, danger, ways out (2+) |
| Opposition | Intent, opening move, behavior, breaking point, resources |
| Pressure | Telegraph / escalate / breaking point when fiction calls for it |
| Resolution | Objective gained / costly success / withdrawal / unexpected |
| Handoff | Changed state; next Development |

Omit-if-unused:

| Job | Done when |
|---|---|
| Battlefield / Chase / Hazard | Space, hazard, interactive features, change, map |
| Discoveries | Portable secrets/clues |
| References | Place, NPC, creature, item, vehicle, spell needed to run this beat |

## Climax jobs — `wiki/templates/climax.md`

Required:

| Job | Done when |
|---|---|
| Run this | Party goal, opposition goal, stakes, pressure, end when, next Resolution |
| Opening image | `[!narration]` of the decisive situation |
| Situation | What is true now; if nobody interferes; what changed to make this the climax; known / uncertain |
| Visible levers | People / objects / features that support more than one approach |
| Pressure | Ticks that change the situation without dictating a response |
| Opposition | Wants, why now, leverage, opening move, response, desperation, line, morale/exit |
| Outcome | Possible state changes; hand off to Resolution |

Omit-if-unused:

| Job | Done when |
|---|---|
| Assets | Opposition tools, not scripted contingencies |
| Stage | Features, movement/zones, collateral stakes |
| Final Battle | Objective beyond 0 HP; forces; tactics; ending the fight; phase shift |
| Final Revelation | Decisive question, truth, proof on the table, resistance, when the truth lands |
| Payoffs | Earlier beats, relationships, items, threats cashed in here |
| Earned reveals | Cue and meaning |
| Live notes | Current pressure, opposition, objective, terrain, carry into Resolution |

## Resolution jobs — `wiki/templates/resolution.md`

Required:

| Job | Done when |
|---|---|
| Abstract | Follows Climax; purpose; one-sentence outcome |
| Run the beat | Confirm outcome → show consequence → pay stakes → let them react → end on an image |
| Closing image | `[!narration]` of the new status quo; no PC feelings or future |
| What is true now | Climax result, objective, opposition, stakes, price, reward, new status quo |
| Consequences | Party earned/paid/changed access; world people/places/power/evidence |

Omit-if-unused:

| Job | Done when |
|---|---|
| Payoffs | Original stake, personal stake, promise, reward, relationship |
| Character Epilogues | Ask; do not prescribe |
| Loose Ends | Close / carry / transform |
| Rewards & Accounting | Payment, advancement, items, reputation, injuries, owner states |
| Optional Stinger | Opens a door; does not erase the ending |

## Classification jobs

| # | Job | Pass |
|---|---|---|
| 32 | New session plan | `type: session-prep` `kind: session-plan`; compass, beat map, floating beats, pressure, PC touchpoints; no Scene ends when / Zones / Be ready for |
| 33 | New Hook | `type: session-prep` `kind: hook`; required Hook jobs |
| 34 | New Development | `type: session-prep` `kind: development`; required Development jobs |
| 35 | New Cliffhanger | `type: session-prep` `kind: cliffhanger`; required Cliffhanger jobs |
| 36 | New Climax | `type: session-prep` `kind: climax`; required Climax jobs |
| 37 | New Resolution | `type: session-prep` `kind: resolution`; required Resolution jobs |

Fail if any of 32–37 use `type: beat`, `type: session-beat`, or `type: session-plan`. Fail if `intensity` or other dropped draft keys are standing identity keys.

## Out of contract

How the designated writer phrases a skill. Beat Chart assembly and skill routing ([beat-skill-routing.md](./beat-skill-routing.md)). Wiki kind pages ([wiki-kind-pages.md](./wiki-kind-pages.md)). Foundry staging. Cold opens. Rewriting Session 11 files.
