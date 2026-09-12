# Campaign OS

The engineering domain for this repo: the session pipeline, skills/hooks/linters,
and LLM-wiki conventions that produce and maintain a D&D campaign wiki — not the
campaign content itself. Campaign terminology and DM rulings live in
`vault/srd/rules/rules-glossary.md` + `docs/rulings/` instead (a separate domain,
owned by the `campaign-domain-modeling` skill, not this file).

## Language

**Product** (of Campaign OS):
The session pipeline, skills, hooks, linters, and LLM-wiki conventions
themselves — the process that authors and maintains the wiki. NOT the wiki
content (`vault/`, including `vault/campaigns/shattered-sea/pcs/` and `vault/episodes/`),
which is a live dogfooding artifact
the process produces, not the deliverable being engineered
(`vault/refs/domain.md:3`: "The domain is the process, not the campaign.").
_Avoid_: "the wiki" as a synonym for the product — it's an artifact, not the product.

**Shattered Sea**:
The reference campaign run inside Campaign OS — the developer's real, live-played
campaign, and this system's stress-test/scale artifact: it exercises the
LLM-wiki design against real play (thousands of pages, long-running canon) to
prove the process scales without unbounded context growth.
_Avoid_: "the campaign" alone (ambiguous with the generic concept), "the
content" (conflates artifact with product).

**Trigger** (agent-instruction sense):
An observable event the model detects while typing — never a judgment state,
prediction, or topic noun — that a rule, skill, or lint message opens on so it
fires at the moment of action (`docs/guardrails/_FORMAT.md` F2). Repo-wide,
per the `pattern-match` skill's contract — `_FORMAT.md` F1-F9/F14 is that
contract's guardrails-kit-scoped restatement, not a separate rule.
_Avoid_: unqualified "trigger" when a Front/clock condition is meant — see
Trigger condition below.

**Trigger condition** (Front sense):
The named world-state condition that advances or fires a faction Front's
clock (`vault/refs/vault/faction/GUIDE.md`). A TTRPG game-design
concept, unrelated to the agent-instruction Trigger above despite the shared
word.
_Avoid_: bare "trigger" in Front/clock context — always qualify as "trigger
condition" to avoid collision with the agent-instruction sense.

**Runbook**:
A governed content page (`vault/refs/runbooks/*.md`, `type: runbook`) that is an
agent's guide to a multi-step operation — orchestrates and cites the
skills/templates/linters that do each step's work, never restates them
(`vault/refs/README.md`; renamed from "playbook"
`docs/adr/0003-playbook-renamed-to-runbook.md`). Never a substitute for a
single skill's own internal `## Workflow` section — that's not cross-skill
orchestration and doesn't earn a runbook.
_Avoid_: "playbook" for this concept (renamed 2026-07-23) — except when
naming the unrelated external "Stories Playbook" fiction-writing
methodology (`vault/refs/stories/GUIDE.md`), a proper
noun this rename doesn't touch.

**Idea > Story > Content** (the content-creation spine):
The standardized three-stage vocabulary for how new campaign material reaches
a wiki page: **Idea** (`docs/guardrails/IDEA.md`, prefix `CB`) — brainstorming
a story idea, plot direction, or NPC/faction/quest concept with no target
page yet, ending in a synthesis and a named next step; **Story**
(`docs/guardrails/STORY.md`, prefix `WR`) — drafting or revising campaign
prose (the flowing chapter, lore, recap, handout) via `draft-story`; **Content** (`docs/guardrails/CONTENT.md`, prefix `CN`) —
authoring or expanding a `<type>-prep`-owned mechanical page from its
template. Renamed from COLAB/WRITE/CONTENT (`docs/adr/0016`) — CONTENT kept
its name, IDEA and STORY were renamed to carry the spine's own vocabulary.
_Avoid_: "COLAB"/"WRITE" for the Idea/Story stages (renamed 2026-07-30) —
except when reading `docs/history/guardrails-MIGRATION-LOG.md` or an ADR narrating
the rename's own history.

**Lint rule** (as law) vs **prose guardrail** (as guide):
A lint rule is a deterministic check wired to a hook — zero context cost
until its shape appears, then delivers the fix in imperative second person
at the moment of the break (`docs/adr/0002-lint-rules-as-just-in-time-prompt-delivery.md`).
A prose guardrail (a CLAUDE.md/skill "always/never" line) is a suggestion —
context cost every turn, fires only when attended to. New guidance for a
nameable code/content shape defaults to a lint rule; a taste call a checker
would false-positive on stays prose (`enforce-with-linters` skill's
PLACEMENT decision).
_Avoid_: "guardrail" as a synonym for either one specifically — a guardrail
is the general term; which delivery mechanism it uses is the load-bearing
distinction.

### Narrative Islands architecture

The campaign-prep architecture adopted by ADR-0054. It supersedes prep models
that treated episodes, moments, or dashboards as the primary design object.

**Narrative Island**:
A durable, runnable dramatic situation composed from existing campaign atoms.
The method is called Narrative Islands; the operational page/type name is
**Situation** so agents do not confuse the concept with literal islands in the
Shattered Sea.
_Avoid_: using "island" for the page type, "scene", "plot beat", "encounter",
"adventure script".

**Situation**:
The operational campaign-prep object for a Narrative Island: a live dramatic
condition with pressure, actors, discoverable or affectable material, an
if-ignored change, and links to the atoms it composes. A situation starts vague
and minimal, then sharpens only when current campaign state and player attention
make it useful to prepare for the table. When the Situation is on tonight's
menu it transcludes a **narration** sibling (the callout title is the section); checks stay
optional. The Situation page itself holds no spoken prose.
_Avoid_: literal-island assumptions, scene scripts, mandatory routes,
session-local clones whose only job is to hold those samples, inline
`[!read-aloud]`.

**Atom** (Narrative Islands sense):
Any smallest independently useful campaign element, implemented as an existing
typed wiki page or section such as an NPC, faction, location, item, clue,
secret, relationship, or Front. It is architecture terminology, not a page type.
_Avoid_: `type: atom`, a generic atom template, duplicating typed-page facts.

**World pressure**:
An active force already pushing the world: an NPC, faction, environment, hazard,
or external condition pursuing a goal with plausible escalation. A Front can
produce world pressure; a Narrative Island exposes pressure as a runnable
situation.
_Avoid_: "expected outcome", "next scene", "what the players do".

**Player attention**:
Evidence from play that a subject deserves deeper preparation: voluntary
investigation, repeated questions, resource commitment, emotional heat,
character promises, return visits, or cross-session references. Incidental
mentions and polite acknowledgment do not earn expansion by themselves.
_Avoid_: "mention count", "agent interest", "cool lore".

**Overview** (episode entry):
The pre-table briefing for one episode. Agents read it before writing or
opening a run-guide. Headings, in order: **Tonight**, **Run guides**.
File: `eNN-overview.md`. Names `session_shape:`.
_Avoid_: `eNN-index.md`, `subtype: index`, treating a run-guide as the episode
entry.

**Run-guide**:
A chronological at-table *walk* for one stretch. Episode file:
`eNN-run-guide-<slug>.md`. Situation how-to-run: `<situation-slug>-run-guide.md`
beside the Situation. Transcludes owners in document order. Exit is the only
heading that opens another file. Every `prep_depth: planned` Situation has one,
and so does every Situation *nearby* the party.
_Avoid_: one `eNN-run-guide.md` per episode, Suggested evening as pointer prose,
opening the Situation page to improvise the run, an overflow line as a substitute
for a situation run-guide, `## Next` on a beat.

**Nearby**:
The party's current location, every location on tonight's live routes, and one
wiki-link hop from those (same settlement, adjacent site, the water they occupy).
_Avoid_: the whole region page, a DM-named set each session.

**used_by**:
Frontmatter list of run-guides that transclude this owner. Replaces
`parent_run_guide`. The overview is never in the list.
_Avoid_: a single parent, putting the overview in `used_by`.

**Stretch**:
The span of play one run-guide owns — continuous until remaining play is
mutually exclusive, or one Situation walk entered from elsewhere.
_Avoid_: "scene", "act", equating a stretch to a session shape.

**Exit**:
The only run-guide heading that opens another file. Numbered play H2s are next
inside this file. A beat's branch conditions stay on its situation's Live
Branches; their landings are the next H2 or a row here.
_Avoid_: `## Next` on a beat, Pass/Fail as evening destinations.

**DM reference**:
The high-density at-table surface. During play it is the current run-guide.
The DM stays on that page until an exit link.
_Avoid_: "AI runtime", "procedure for running play", "dashboard because it can
be generated", whole-file `![[beat-…]]` embeds of the beat page,
`eNN-index.md` as the table page.

**Route** (page type, also a session-menu object):
The durable leg between places (`type: route` under `locations/`). A session
may select one or more routes; routes may overlap. Tonight's travel is
selected routes plus the Situations that can surface on them.
_Avoid_: `type: passage`, "the crossing file", treating a route as tonight-only.

**Passage**:
The historical session-local journey container. The durable object is Route.
_Avoid_: using passage as a session unit.

**Session plan**:
The night's shape, map, and which run-guides exist. Lives on the overview.
Together the night's run-guides must be enough to play a complete ~4-hour
session in which the party can progress and the world is reactive, not flat.
The overview names one primary **Session shape**; a night may mix.
_Avoid_: mermaid or suggested-evening/overflow as the run-guide's job,
"3–5 beats required", treating one shape as the type system.

**Session shape**:
The kind of night, not a page type. Closed set: **crossing**, **site**,
**town**, **intrigue**, **investigation**, **set-piece**, **hunt**,
**downtime**, **climax**. Catalogue and menu rules:
`.claude/skills/composing-beats/references/runtime-surface.md`.
_Avoid_: inventing a tenth shape as a page type, treating
combat/social/exploration as the night's kind.

**Goal** (performative):
The story or world fact a `type: narration`, `dialogue`, or `handout`
tells the party so they can progress. Fewest words. The body is graded
against it.
_Avoid_: texture as the goal, a purpose essay, a goal the body never lands.

**Check table**:
The body of a `[!check]` callout after a spoken picture. Columns Check / DC /
Failure / Pass. Skills, saves, contests, and group rolls are rows.
_Avoid_: a bare table outside `[!check]`, a check table under Prep, a second
system for "mandatory" vs "suggested" rolls, one `[!check]` per row.

**Sample** (table furniture):
A prepared table object — narration, dialogue, a Checks heading, an
encounter — transcluded into a run-guide in play order.
_Avoid_: "file the DM opens", Suggested-evening wikilink as the sample,
`#Read-aloud`, `#Narration` section embeds, inline `[!read-aloud]`,
default Metabind run buttons, Ran checkboxes on templates.

**Last Time**:
The once-per-session recap narration (`mode: recap`). Only the opening
run-guide embeds it.
_Avoid_: repeating it on later path guides, putting it on the overview,
inline recap prose on a play page.

### Beat composition

The default prep method (ADR-0060): `composing-beats` orchestrates atomic
beats into playable structures; the type skills own each beat's craft.

**Beat**:
An atomic playable page with one dramatic function — `type: beat`,
`beat_type: hook | development | cliffhanger | climax | resolution`, one
template per beat type. Carries entry state, Link of Relevance, pressure,
possible state changes, and handoff. Episode-scoped beats live in
`vault/episodes/NNN/`; situation-scoped beats in
`vault/campaigns/shattered-sea/beats/`.
_Avoid_: "scene", a beat as a scripted player action, a signal-only beat
(that is Drip), `beat_function:` frontmatter on other types.

**Beat Chart**:
The composition surface on a `type: situation` page: Dramatic Question,
Player Gravity, Current State, Beat Spine, Live Branches, Climax
Readiness, Unused Possibilities — wikilinking atomic beat pages. Belongs
to the playable situation or adventure, not the calendar.
_Avoid_: a `type: beat-chart` page, putting the chart on the episode
overview, duplicating beat bodies into the chart.

**Beat Spine / Beat Field**:
Spine — the most plausible current dramatic sequence when player direction
is clear. Field — candidate beats connected by state-dependent transitions
when several directions stay live. Branch only on materially different
world states.
_Avoid_: branches per player method (attack/negotiate/sneak), spines that
predict player decisions.

**Link of Relevance**:
The established player investment (goal, fear, relationship, debt,
history) that makes a beat worth engaging. Every prepared beat records
one.
_Avoid_: "the party is nearby" as relevance, minting new backstory to
justify prep.

**Climax gate**:
The readiness test before decisive play: question, investment, opposition,
understanding, leverage, stakes, possibility, convergence. A Climax is
earned, not scheduled.
_Avoid_: scheduling a climax by session count, filler beats to delay one.

### Performative prose

**Performative prose**:
A typed wiki file the DM speaks or shows verbatim (`type: narration` or
`type: dialogue`). Co-located sibling of its parent; no H1; italic body;
whole-file `![[slug]]`.
_Avoid_: "read-aloud" as a type, "boxed text" as a page type, `-c0N`
callout fragments.

**Narration**:
Subject-focused picture of one entity or visible condition, spoken at the
table. `mode: establish | continue | transition | recap`.
_Avoid_: `[!read-aloud]`, mixing spoken character lines into the file.

**Dialogue**:
Spoken character lines only. A file exists when the parent needs a line,
not on every NPC.
_Avoid_: stage direction, scene description, `[!dialogue]` on a play page.

**Default depiction**:
Reusable narration on an entity page (location, NPC, item, monster, ship).
Present tense, any-context, focused on the thing. Required when the page is
authored or next-touched.
_Avoid_: "generic description", second-person arrival, `you` / `your`,
pacing prompts.

**Scene narration**:
What is true in the world now, on a beat that will be seen tonight.
Follows the default-depiction camera; a beat's narration may take a
pacing prompt.
_Avoid_: using the entity default as a script for a later beat; narrating
what the PCs do.

**Pacing prompt**:
Optional closer on session-local narration (a beat, a recap hook) that
directs the table — "What do you do?", "How do you stay ahead of it?".
_Avoid_: putting one on an entity default or a Situation portrait.

**Creative-writer**:
The agent that fills performative stubs after the mechanical draft. Loads
`writing-player-prose` (picks the branch internally). Does not write the
parent page.
_Avoid_: content-drafter writing spoken sentences.

**Drip** (pacing texture):
A rumour, secret presentation, NPC line, or environmental detail that
carries a clue or future hook as ordinary world texture. The party should
not clock it as a hook when it lands. Existing types already own the
facts (`type: lore` subtype rumour, `type: secret`, NPC pages, location
prose). The session job is to weave them into samples, not to mint a
skippable event file for each one.
_Avoid_: `type: hook`, labeled "foreshadowing" in player-facing prose,
beat files whose only job is to deliver a signal.

### Retired units (ADR-0061)

`type: moment`, `type: fork` ("Decision"), `type: sequence`,
`type: passage`, and the dm-screen assembly are retired — W143 rejects new
instances; episodes 001–008 and 009's allowlist stay valid. One term per
concept: a divergence is a **Live Branches** row, an ordered chain is a
**Beat Spine**, the mid-play surface is the **run-guide**, the skip
consequence is **`if_ignored:`**, and a cold open is a Hook beat from a
borrowed perspective (`writing-cold-opens`).

**Session** — the real-world play event (the session loop PREP→RUN→CAPTURE→INGEST→RECAP→PUBLISH, "session zero", the `sNN-` file prefix).

**World reactivity**:
NPCs, places, Routes, and Situations have independent motion — pressure,
if-ignored change, Fronts, toys that act without the party. The world is
not a flat backdrop. Not a page type, and not tied to a specific party deed.
_Avoid_: `if_engaged` scripts of their success, "how the town feels tonight"
overlays, treating one aftermath (they killed Otar, therefore X) as the
architecture.

**Episode** — the content unit one session produces, stored at `vault/episodes/NNN/`. Paths always say `episodes/`; the event stays a "session". (DM ruling 2026-08-09.)
