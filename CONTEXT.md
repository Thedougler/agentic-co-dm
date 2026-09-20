# Agentic Co-DM

Prep-and-wrap co-DM for a human table. Agents author playable Work before a session and compile outcomes after. The DM is the only runtime while players are present. This file is the reusable glossary for campaign play and Co-DM operations; it does not record work packets, ingest grain, or failure catalogs.

## Language

**DM**:
The human who runs the session. Sole table runtime. Players hear and see only what the DM presents.
_Avoid_: live agent at the table; GM as a second in-session operator

**Co-DM**:
Agent work in the prep window and the wrapup window. It addresses the DM, never the players, and does not run during a session.
_Avoid_: live co-GM; table-facing agent; autonomous GM

**Session**:
Table time with only humans present.
_Avoid_: agent-attended play; in-session proposals

**Campaign**:
The shared fictional world and ongoing play established by the DM and players across sessions.
_Avoid_: plot; setting bible; sequence of planned scenes

**Season**:
A major phase of a campaign containing multiple sessions and a coherent change in direction.
_Avoid_: arbitrary session batch; immutable storyline

**Arc**:
A shorter connected run of situations or sessions organized around one major pressure or question.
_Avoid_: predetermined plot; mandatory sequence

**Quest**:
A named objective or organized situation that gives play a direction without prescribing its outcome.
_Avoid_: scripted mission; guaranteed plot

**Prep**:
The before-session window where the Co-DM authors playable Work for the DM (spoken beats, mechanics, staged play-surface artifacts).
_Avoid_: in-session assistance; treating prep as what happened

**Wrapup**:
The after-session window where the Co-DM ingests the transcript and updates the wiki to match play.
_Avoid_: live agent note-taking; leaving prep as canon after play contradicts it

**Situation**:
The arrangement of people, places, pressures, resources, and choices that play can change.
_Avoid_: scene script; plot outline

**Active Situation**:
The situation currently demanding attention and offering actionable choices; the campaign's present point of play.
_Avoid_: open handle; current opening; plot summary

**Thread**:
An unresolved concern, objective, relationship, or consequence that may draw future play.
_Avoid_: required quest; scripted subplot

**Front**:
An independently advancing faction or threat agenda that creates pressure and changes the situation without waiting for the party.
_Avoid_: villain monologue; static backstory; scripted encounter

**Pressure**:
A force, deadline, danger, demand, or consequence that makes a situation require a response.
_Avoid_: railroading; arbitrary urgency

**Clock**:
A prep model for representing how a Front or pressure advances toward a consequence. It belongs in prep and skills, not production-facing content.
_Avoid_: player-facing progress meter; required UI

**State change**:
A fact about the situation that becomes different because of play.
_Avoid_: planned beat; authorial outcome

**Handoff**:
The changed situation and available options that carry play into the next beat, scene, or session.
_Avoid_: scripted transition; forced next scene

**Objective**:
A concrete result the party or an actor can accomplish. State the result, not the method.

**Want**:
The result an actor is pursuing.

**Stakes**:
What materially changes when an outcome differs.

**Danger**:
Credible immediate harm or loss in the current situation.

**Goal**:
Avoid as a generic label. Use **Objective** for an accomplishable result or **Want** for an actor's pursued result.

_Avoid_: treating objective, want, stakes, and danger as interchangeable.

## Wiki and table knowledge

**Canon**:
The wiki is the complete current campaign account shared by the DM and Co-DM. It is not split into separate DM and agent versions of reality.

**Revealed**:
Whether play has exposed a fact to the players. `unrevealed`, `null`, or an absent value means the players have not encountered it yet; it does not limit the DM's or Co-DM's knowledge. When a transcript establishes that players encountered it, record the session that exposed it.

**Hidden**:
A fact the DM may withhold from players during play while it remains fully available in the wiki to the DM and Co-DM. Hidden describes table presentation, not an agent knowledge boundary.

**Category**:
A storage and index bucket such as `entities`, `journal`, or `lore`. It is not a layout name and does not replace the campaign page **Type**.

**Type**:
The campaign page kind, such as `quest`, `npc`, or `session-prep`.

**Status**:
The current state label for a page's subject. Values depend on the page kind and may reuse words such as `active`, `offered`, or `ready`; do not create parallel status axes for the same subject.

**Scope**:
Describe scale where it changes play, but do not treat it as universal frontmatter.

DM-facing summaries state sourced campaign facts and runnable procedures. They do not invent unsupplied DM intent.

_Avoid_: treating hidden content as inaccessible to the DM or Co-DM; inventing DM intent; tying categories to layouts.

## Beat model

**Beat**:
A bounded unit of play with a trigger, a meaningful change, and an open player response.
_Avoid_: scripted scene; cutscene

**Hook**:
The strong start that presents immediate pressure and demands a response.

**Development**:
A beat that changes what the players know, can reach, or can choose.

**Cliffhanger**:
A beat that changes position, resources, safety, or time while leaving the outcome uncertain.

**Climax**:
The highest-stakes confrontation made inevitable by the preceding play.

**Resolution**:
The aftermath that shows what changed, closes the current pressure, and establishes what comes next.

## Infrastructure language

**Wiki**:
The current, compiled campaign source of truth: citable pages the DM browses and the Co-DM retrieves from. Written in complete sentences a human can read.
_Avoid_: knowledge bank; the bank; unaudited chat memory; a second store beside the vault; AI shorthand; telegraphic agent-speak

**Search index**:
A derived retrieval layer over the wiki (commonly QMD). The wiki remains the source of truth.
_Avoid_: treating the index as a second canon store

## Agent execution language

**Capability**:
An existing skill or deterministic wiki operation that owns a bounded kind of work.
_Avoid_: node; generic worker; interchangeable tool

**Owner capability**:
The capability with authority over a specific artifact or operation and its completion criteria.
_Avoid_: generic author; fallback owner; shared ownership

**Capability handoff**:
The transfer of bounded work when ownership changes, after which control returns to the parent operation.
_Avoid_: handoff; task drift; permanent delegation

**Parent operation**:
The capability that retains the user's original objective while owner capabilities complete dependencies.
_Avoid_: orchestrator; supervisor skill; workflow engine

**Capability dependency**:
An artifact or state that must be valid before dependent work can proceed.
_Avoid_: procedural step; speculative prerequisite

**Completion guard**:
An observable condition that closes a capability branch or permits dependent work to begin.
_Avoid_: prose exists; agent says done; implicit completion

**Context projection**:
The minimum sufficient canon and operational evidence retrieved for one capability's current work.
_Avoid_: inherited full context; whole-vault loading; incidental context

**Observation surface**:
Compact query, lint, or health evidence that identifies relevant knowledge, invalid output, or the next attention target.
_Avoid_: planner; workflow ledger; second source of truth

**Output contract**:
The combined owner conventions, template, and validation rules that define a valid artifact.
_Avoid_: prose-only completion; optional shape

**Knowledge graph**:
Campaign pages and their semantic relationships.
_Avoid_: execution graph; workflow state

**Execution graph**:
The ephemeral capability routes, dependencies, completion guards, observations, and capability handoffs for the current request.
_Avoid_: knowledge graph; persistent workflow ledger; graph runtime

## Presentation language

**Theatre of the mind**:
Spoken, sensory language the DM can read aloud. The mouth surface.
_Avoid_: treating TotM as a VTT mode; putting mechanics or unspoken facts in spoken text

**Play surface**:
Player-visible Foundry artifacts staged during prep from accepted Work (maps, tokens, handouts). The screen surface.
_Avoid_: an agent pushing to Foundry during a session

## Work and canon

**Work**:
Mutable prep the DM may accept, edit, or reject before it is eligible for the table.
_Avoid_: treating unaccepted drafts as canon or as player-visible

**ai-co-dm**:
The current Co-DM project containing reusable prep-and-wrapup practice and the campaign's canonical wiki.
_Avoid_: a separate campaign store; a candidate canon; a third full copy of the campaign

**Canon proposal**:
A suggested change to wiki facts. The Co-DM never silently edits canon. Fun may shape Work; facts change only when the DM accepts.
_Avoid_: fun-as-silent-override; inventing lore or mechanics into the wiki as silent canon

**Redesign**:
A clean rebuild around best practice. It is not a patch list of current-vault failures.
_Avoid_: user-corrections as spec; documenting operational grain as domain language

**Prose wiki**:
Obsidian markdown pages with a `type` and templates. The vault is the campaign product the DM opens. Copy is ordinary human prose.
_Avoid_: Campaign OS compilers as this product; a type-less dump of notes; pages that read like agent notes
