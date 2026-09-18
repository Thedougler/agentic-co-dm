---
name: theatre-of-the-mind
description: >-
  Write all player-facing prose for TTRPG play. Use for descriptions, spoken
  narration, boxed or read-aloud text, NPC dialogue, recaps, combat updates,
  handouts, rendered player text, scenes, rooms, wilderness, travel, vehicles,
  businesses, objects, creatures, people, visions, transitions, reveals, and
  live table, chat, or play-by-post output. Use whenever text crosses the
  DM/player boundary, including `[!narration]` and player-safe renderer
  surfaces. When filling `[!narration]` or a first look, open related owner,
  session, or user-attached images and ground the spoken picture in the
  pixels. Prefer complete, natural flowing prose that paints a drawable
  picture — not telegram stubs and not verbose padding. Reader `players` →
  theatre of the mind. Does not own DM procedure, hidden truth, or agent
  instruction.
---

# Theatre of the mind
## Work gate

Prep only. Follow `docs/agents/work.md`.

## HARD: entity-before-spoken (Nick 2026-09-14)

**Production session content** (session-prep beats, TotM/`[!narration]`, action cards, spoken text) is **complete or it does not ship**. Vague/non-specific descriptions of unnamed people/things because the entity page is missing = **critical error**.

**Dependency order (recursive):** If a beat/scene names or requires an NPC, item, creature, place, faction, vehicle, spell, quest, or other entity — **mint/file that owner page first** (current standards: kebab basename, matching `wiki/templates/`, land under `wiki/_staging/` when `WIKI_STAGED_WRITES=true`), **then** write/update the session/TotM text that depends on it. Even when Nick asks for a session that introduces new names — create the entities first. The DM cannot describe what does not exist.

Agents MUST complete **all** recursive dependency steps to finish the goal — not only top-level, intermediary, or initial steps — in dependency order. This is a completeness gate; do **not** thin narrative craft to satisfy it.


Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Reject leaves no page. Invention is required when the wiki lacks the fact: set `invention: true` and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]` for wiki claims. Show the DM any contradiction with an existing page. Never present invention as a wiki fact. Never write silent canon. A craft `type` becomes `canon` only after DM accept.

Players see nothing until the DM accepts and presents.

Done when: the page is inspectable Work, `lifecycle: proposed`, invention flagged, grounding named.

Remap durable output paths from `campaigns/<slug>/` to `wiki/` (entities/journal as appropriate). Templates live in `wiki/templates/`. Replace knowledge-bank terminology with wiki terminology, but do not change geographic river-bank language. Point at `docs/agents/work.md` rather than restating the glossary.

All spoken copy is Work for the DM and player-safe; `[!narration]` is the spoken slot.

## HARD: dm-facing-explicit (Nick 2026-09-14)

**DM-facing content** (`visibility: dm`, action cards, Be ready for, secrets, situation facts, Wiki facts, owner pages): **no vagueness, non-specific placeholders, coy narration, or invented mystery.** The DM must have **all** scene/world facts available immediately. Making the DM decode coy agent writing = **critical error**.

**Clarify vs player-safe TotM:** Player-facing `[!narration]` may withhold from *players*; it must still be grounded in named entities that exist (**HARD: entity-before-spoken**). DM layers must state who/what/where/why concretely — names, wants, true stakes — with a DM answer on the page for every planted mystery.

**FAIL:** “a woman in the woods,” “unnamed survivors,” “something watches,” mystery with no DM answer on the page.
**PASS:** Named `[[npc]]` with look/want/voice; named place; stated true invitation/threat.

Pairs with entity-before-spoken. Completeness/explicitness gates — do **not** thin narrative craft.

## Ingest

When `wiki-ingest` loads this skill, named ingest is DM approval for those sources (`docs/agents/work.md`). Write player-facing `[!narration]` on the chosen destination. Do not re-route ideas, chat-propose the same page, or put secrets, DCs, or unearned names in spoken text.

Polish stubs into flowing spoken prose. Keep settled look and facts. Do not invent a scene the source does not support.

**Complete when:** spoken blocks on the destination are player-safe TotM for their mode, meaning unchanged.

## Authoring outcomes

Player-facing theatre of the mind for a prepared Beat MUST be complete before
the session so the DM can read or paraphrase it without an agent and without
inventing the opening picture. Spoken look that depends on runtime player
decisions (including turn-by-turn combat and top-of-round battlefield
summaries) MUST NOT be prewritten.

**Named entities + DM layers.** Spoken/`[!narration]` MUST NOT hand-wave missing owners (vague “a figure”, “some item”) when the beat requires a specific entity — mint the owner page first (HARD entity-before-spoken). Player narration may withhold secrets from players; **DM-facing** slots (Be ready for, secrets, situation facts, action cards) MUST name who/what/where/why with a DM answer on the page — no coy mystery (HARD dm-facing-explicit). Incomplete also includes:

**Agency.** Player-facing narration MUST describe the world. Incomplete:
PC action, thought, emotion, intent, choice, success, or unresolved outcome;
secrets, DCs, unearned names, hidden causes, or agent-process language in the
spoken block. Involuntary or emotional reactions MUST be expressed through the
environment when they appear, not assigned to a PC.

**Beat job.** Every situated scene opening names a Beat type and job:

- **Hook** — immediate interest with minimal orientation first.
- **Development** — changed information unmistakable.
- **Cliffhanger** — danger or instability front-loaded.
- **Climax** — opposition, stakes, features, in-motion consequences clear.
  MUST NOT narrate victory, defeat, sacrifice, surrender, escape, or any other
  player-controlled outcome.
- **Resolution** — visible consequences only. Conditional variants when the
  Climax can end substantially differently.

Beat job is one sentence. Required when Beat is set. Decorative prose with no
job is incomplete. Portraits and short updates do not take a Beat type.

**State independence and layering.** Blocks remain usable regardless of party
formation, position, resources, drawn weapons, speaking order, investigation
order, intended approach, mood, or character-specific reactions — unless the
Beat guarantees the resulting world state. Important elements MUST be related to
one another (beneath, beyond, between, blocking, …). Isolated inventories
without relationships are incomplete.

Opening narration is the **Layer 1 immediate frame**: where the party stands,
how large the space is at body scale, what the ground/air/light is doing, and
what is obvious without deliberate investigation. Frame and body-scale
environment seat the party before furniture; see
[references/places.md](references/places.md) for the moves. Salient features
and discoverable information are separate complete reveal blocks (Layers 2–3)
that describe the discovery, not the method. Features that matter tactically or
interactively MUST be in Layer 1 before a player would need them. Sensory
information is selective: one or two defining details suffice; do not cycle
every sense. An opening block MUST end on a live situation (danger,
contradiction, question, opportunity, demand, objective, or changing
circumstance) and MUST NOT choose the party's response.

**Combat.** When violence is imminent, combat opening narration MUST make
threats, threat relationships, objectives, relative distance, major terrain,
cover, hazards, interactable opportunities, routes, and obvious exceptional
conditions understandable. Clarity outranks literary flourish. Player-facing
distance defaults to relational bands: **Melee** (immediately interactable),
**Near** (reachable with normal movement this turn), **Far** (not meaningfully
interactable in melee without extra movement). Exact measurements appear in
spoken look only when a rule or encounter requires them. Coordinates disguised
as prose are incomplete. Enemy grouping MUST be legible enough for the DM to
answer how many a reasonable area effect can catch. Combat Work includes a
complete opening and concise DM-only tactical facts on existing beat-card slots
(zones, action cards, procedure). It MUST NOT include a turn-by-turn script or
top-of-round summary. World-triggered changes (ritual phase, collapse,
reinforcements) MUST have complete escalation or reveal blocks that do not
assume PC behavior.

**Wiki portrait.** Mode is situated moment (table or Beat state supplied) or
wiki portrait (standalone; no party/encounter). A wiki portrait MUST remain
valid across sessions. It MUST NOT reference current party state, assume an
encounter, or include unlabeled transient facts. Completeness: recognizable
identity anchors. Not every parent heading. Not a Beat. Not a scene script.

**Interactive problems.** Traps, hazards, and trials MUST expose a visible
symptom or usable clue in the current or earlier fiction so a solution is
available in play. A challenge solvable only by omitted information is
incomplete. Betrayal and sabotage MUST remain detectable, preventable, or
respondable opportunities — not predetermined outcomes with no chance to notice.
Reasonable player-created details that fit the established fiction MUST be
permitted. Prep MUST NOT be treated as a closed inventory.

**Prepared scene facts** use existing Session 11 slots when on a beat card:
`[!narration]` for spoken look, Now for fixed truths, Zones for spatial
relationships, zone/tick Narration cells for reveals, Be ready for for
adjudication. Omit empty sections. Do not add a second cockpit for the same
Beat. How those facts appear on a Session 11 beat card remains that card's
layout.

These are outcomes, not a single sentence architecture, word count, or expert
process as the only valid method. Do not rewrite legacy wiki pages solely to
match this standard.

This is the default and sole authority for prose that crosses the DM/player
boundary. It covers a live sentence, a boxed passage, a chat reply, a recap,
a combat update, a handout, and player-safe rendered text. Keep DM procedure
and hidden truth outside that prose in `[!mechanic]` and collapsed
`[!secret]-` callouts.

Narration controls attention. Give the player a concrete thing, body, or
change they can point at and act on, and write it as **natural flowing prose**
that paints a complete picture for that surface, not a telegram of facts.
Descriptive, specific, plain language is the default everywhere: the ordinary
noun plus the visible difference beats a coined label, poetic shorthand, or
private campaign term.
Use common, normal human words unless the common word would be inaccurate. The
goal is clear table communication, not literary display. A line that sounds like
it is trying to impress an English professor is failing the table.

**Complete picture, not pad.** Join supported facts into connected sentences
with plain nouns and concrete verbs. Do not stop at a single encyclopedic
clause when the picture is still incomplete. Do not add purple adjectives,
theme sentences, or mood claims to fake completeness.

Every sentence must change the picture, attention, risk, route, relationship,
or possible action. Cut ordinary defaults and no-effect reassurance. State a
visible relation once in its strongest place; repeating the same claim in both
a table cell and the spoken prose is padding unless the second use changes the
picture or choice. Omitting actionable scene stock is a failure; padding with
non-actionable color is also a failure.

Length is the shortest block that makes a stable shared picture and performs the
job. Not a word-count pass/fail. A hit or dialogue turn may be one tight line;
a portrait or scene opening is usually a short paragraph or more of connected
sentences. Situational beat stubs (zone, tick, How the Scene Resolves,
creature-in-this-scene) are shorter: one to three sentences, one job, no
restage of the opening. Do not force every surface into a spoken block, a fixed
beat, or a located change.

## Choose the mode

Before surface routing, decide whether the request is a **situated moment** or a
**standalone portrait**:

**Hard mode gate for creature/monster owning-page `[!narration]`:** if the
request is filling or rewriting `[!narration]` on a creature or monster note
and no party position, initiative, declared action, or other current table
state is supplied, the mode is **standalone cold portrait** (body, scale,
parts, ordinary stable behavior). Signature moves, tactics, Hookline/Reel,
Stoop steal, Grubnade burst, ambush scripts, time-skip tactics ("minutes
later"), and "open with…" running notes stay in `[!mechanic]` / `[!secret]-` /
At the table / DM sections. They must not become a resolved attack film or
encounter cutscene inside the callout. "Ordinary observable behavior" is
idle/species habit (chews a flower, stands over a carcass), not playing the
tactic script to completion and not inventing a disturb stimulus ("When the
branch moves…") when no table state supplies it. Inventing a trailing PC,
ankle/boot contact, completed haul, completed item tear, or full detonation is
a fail. Do not end cold portraits in **telegram stubs** — fragment sentences
that isolate a minor fact (`Chin drips.` / `Antlers.`) or stare; fold chin,
blood, eyes, claws onto the body in flowing prose.

**Hard mode gate for location/site `[!narration]`:** if the request is filling
or rewriting `[!narration]` on a location note and no party position or other
current table state is supplied, the mode is **standalone cold place portrait**
of **stable public geography**. Choose an organizing spine independently.
Require body-scale size and at least one usable affordance cue as nouns/verbs
(wet stone underfoot, followable channel, climbable ledge). Ban place-design
kernel fields and schema voice: Function, Fantastic, Conflict, Promise,
Trajectory, Aspects, Player verbs, Hunger / possession metaphysics, and
rule-talk like `unclaimed` / `claim`. Ban invented mystery closers and staged
located-change drama unless current table state supplies that motion. Creature
signs and encounter pressure belong to a **situated** first look. Design
kernels stay upstream (`place-design`); TotM renders geography. Respect the
owning note’s `Where` ledger; do not invent north/east/south/west neighbors or
travel-day distances.

Do not close on a thesis, leak Aspects/secrets, or use opaque caste/jargon
nouns. Staged hostility requires current table state unless the parent
explicitly establishes stable public ecology without encounter film. A
dual-title note must publicly render both halves or be retitled. Keep vehicle
access kitchen-table (lines, rail, hold), never boarding interface in player
prose. Keep lore miracles in Secrets/DM. The cold spine is body-scale geography
and a drawable affordance, stopping on stable geography.

**Hard mode gate for hazard notes (`[!narration]` on a hazard page):** if no
current table state is supplied, write a **standalone cold hazard portrait**.
The hazard body or patch is the grammatical and attentional subject. Do not
route it through the creature contract (no Hookline/Reel-style contact film)
or the place contract (no invented valley camera and no lake/terrain spine).
Coverage: form and scale, positive material or construction, and one positive
sensory or physical warning. Prefer kitchen-table words: plain spoken nouns and concrete
verbs over ecology or workshop compounds. For Razer-Grass, keep the positive
glass and cut danger telegraph, but describe it in player-ready terms rather
than relying on `colonies`, `opaline`, or `cut-ready`; a thin glass sound and
fixed sparkle are concrete signals when the parent supports them.

Hazard cold narration must not use frost-mystery or absent-flash riddles (such
as `no frost` or `rather than glitter`), an em dash, an italic underscore
wrapper, or a sweeping landscape camera. A supported plain hardness contrast,
such as sparkles staying fixed instead of swaying like soft grass, is allowed;
do not treat every negative construction as a ban. Stop at the visible hazard
and its player-facing affordance or danger. Do not narrate resolved contact,
Shatter, Glass Bloom, or a scripted aftermath; those belong to the table state
or mechanic layer.


**Hard mode gate for faction/organization notes (`[!narration]` on a faction or organization page):** when no current table state is supplied, use a standalone **cold faction portrait**. Coverage dimensions (not a rigid sentence order): public mask, one concrete kitchen-table method footprint, one environmental Tell a bystander could notice, and a shared title or face cue when the parent supplies one. These must join into drawable prose rather than an abstract organization gloss. In the player-facing block, these are craft labels, not words to say: never use `mask`, `footprint`, `Tell`, or `face cue` in faction `[!narration]`; render the concrete signs directly.

Keep secret agenda, Rule of Two, hunt clocks, and other DM-only pressure out of faction Appearance. Ban workshop abstractions such as `martial reach`, `dropped the ledgers`, or ledger language. Do not invent a plot, venue, encounter, or hidden motive. Stop once those public facts are shown.


**Hard mode gate for technique notes (`kind: technique` or technique tags):** if
the request is filling or rewriting `[!narration]` on a technique note and no
current table fight state is supplied, use a **non-object tell contract** — not
the Fate Spinner object silhouette/material/wear bar. Cold `[!narration]` states
immediately perceivable training tells as **stable facts**: breath, stance, wing
set, and how the form looks when used (e.g. a strike past ordinary wingspan) —
without inventing a current venue, terrace duel, gust-peak scene, or held gear.
Fail object-silhouette forced onto techniques; fail invented venue ("On a
wind-open terrace…"); fail mysticism/theme ("the blow answers that measure",
"answers" as magic tone); fail meta closers ("the tell ends before…"); fail resolved hit film. Training location and order
lore stay in Fiction / Training. Mechanical package stays Mechanics.

**Hard mode gate for object/weapon cold Appearance (Fate Spinner bar +):** cold
item `[!narration]` must read aloud as a drawable object, not a catalog gloss.
Coverage (flowing prose — dimensions, not a checklist dump):
1. **Concrete noun** (musket, long gun, carbine, blade) — not inventory jargon as
   the whole sentence.
2. **Scale vs body** (shoulder stock, barrel past the forearm).
3. **Material + wear** (dark wood, blued steel, brass bright at the trigger).
4. **One non-sight sense or ordinary physical behavior** (weight forward, lever
   clicks, cool in the palm) — not magic tone.
Fail closed: `carries as`, `ordinary X for Y`, naming lore/biography closers
("He named it for…") unless a **visible mark** on the object (engraved plate),
rarity/attunement/DCs, technique-as-abstract-strike. Layering: Appearance ≠
Identified Properties ≠ Fiction/Secret. Owner dedication stays Story hooks.


**Hard ban — craft/process words in player prose:** `[!narration]` and any
player-facing spoken block must never contain workshop vocabulary. Banned in
output (non-exhaustive): `telegraph`, `the tell ends`, `tell ends`, `reaction
point`, `Appearance`, `cold portrait`, `standalone portrait`, `hookline` as a
label, `at the table` as meta. Stop by **omission** — the last image is the
windup — never by naming the stop ("and the telegraph ends there"). Keep those
words in skill/reference/DM notes only.

- **Situated moment:** write from the supplied table state and viewpoint. Route
  by surface below, preserve the current environment and motion, and stop at
  that surface's natural player opening. On a creature first look, the opening
  is the **reaction point**: visible telegraph or buildup only — not resolved
  contact, haul, or PC injury (see [references/surfaces.md](references/surfaces.md)
  and [references/boundary.md](references/boundary.md)).
- **Standalone portrait:** describe one item, creature, place, vehicle,
  business, person, or other subject as a self-contained player reference. Do
  not invent a party, encounter, specific environment, viewer or camera,
  current motion, interaction, dialogue, pressure, handoff, or “what do you
  do?” It is not scene staging and does not need a located change. Hierarchically
  convey all relevant established player-visible identity: recognizable whole
  or silhouette and scale; defining parts, material, or body; ordinary visible
  behavior, function, or use when canon supplies it; and one signature sensory
  fact when the supplied canon supports one. Places add neutral form, topology,
  landmarks, and approaches; businesses add established purpose, interface, and
  service signature; people add a stable
  Face and established characteristic behavior; vehicles add stable silhouette,
  scale, components, and operational character. Omit hidden truth, private
  mechanics, unearned lore, and absent or contradictory facts. Use a public or
  earned name only when known; an unknown name stays unknown. These are
  coverage dimensions, not a required output sequence; choose the portrait's
  organizing spine independently.

The default standalone portrait is a cold player-appearance and observable-state
layer, even when the owning parent is addressed to `[agent, dm]`. Include all
established descriptive states needed for recognition, but omit exact effects,
durations, speeds, actions, DCs, rarity, attunement, curses, private biology or
history, tactics, hidden causes, learned route rules, and secret identities.
If the user explicitly requests identified or player-known properties, render
those mechanics separately after the description and only within that granted
knowledge state. “Complete” means complete for the target portrait contract,
never every heading in the parent.

After one reading of a standalone portrait, a player should be able to
recognize, picture, and distinguish the subject, and know its ordinary
observable function or behavior when the supplied canon supports one. The
wrapper follows the host or page request; do not force an encounter question.

## Before drafting

1. Identify the mode and surface, then read
   [references/surfaces.md](references/surfaces.md) before writing. It is the
   routing contract and defines the natural stop. A standalone portrait uses
   its portrait contract rather than a situated spatial camera.
2. Read [references/examples.md](references/examples.md) and
   [references/voice.md](references/voice.md). Read the matching specialist
   reference and one other: [places.md](references/places.md) for spatial jobs,
   [humans.md](references/humans.md) for objects, [experts.md](references/experts.md)
   for creatures or fights, and [npcs.md](references/npcs.md) for people or
   dialogue.
   A business, shop, tavern, or service request uses the Business row in
   [surfaces.md](references/surfaces.md); no other reference authorizes filling
   missing stock or layout.
3. Read the owning parent and current table state. Preserve established and
   locked canon, distinguish beliefs from facts, and do not add canon in this
   prose pass. If the parent lacks a usable signature, first-sight facts, or
   affordance, invoke the owning craft skill before drafting.
   **Already-spoken gate (session-beat stubs):** before drafting any stub, read
   the previous beat's spoken prose and this beat's own Initial Narration (for
   non-Initial stubs). Do not restate facts already spoken to the players unless
   the scene has physically changed since they were spoken. Grass, river,
   smoke, sky, and terrain the party already stands in do not reappear as
   discovery. New prose shows what is **new, changed, or newly actionable**.
4. **Pixels.** When the job is `[!narration]`, a portrait, a first look, or
   scene-setting, and related images exist on the parent, run card, roster
   owners, or as user attachments, read
   [references/vision.md](references/vision.md) and open those files with the
   host vision tool before drafting. Filename and alt text are not a substitute.
   Completion: every related image is seen or marked unavailable, and
   pixel-supported drawable facts that pass the access gate are in the fact
   inventory. Skip this step for hit lines, recaps, dialogue, and jobs with no
   related art.
5. Run the evidence-of-access and hidden-truth checks in
   [references/boundary.md](references/boundary.md). Every player-facing
   detail needs a legitimate access channel. An uncertainty marker may label
   only an inference grounded in named evidence; it cannot create access.
   Without a channel, cut the detail or route to the owning content-stock
   skill.
6. For a standalone portrait, compose before you enumerate: make a private
   thumbnail of the whole or type plus one dominant supported visible
   distinction. Keep a private, unordered coverage checklist of supported
   portrait facts; it is an audit, not an outline. Choose an organizing spine
   independently of both source order and checklist order — a dominant
   supported relationship, contrast, or use when the subject supplies one — and
   draft around that spine and thumbnail. Relate remaining facts through
   supported relationships among the subject's parts, material, habitat, and
   behavior. Check the unordered checklist afterward so the hierarchy does not
   omit a required fact; never turn its sequence into the prose order.
7. Before drafting from an owning parent or reference, use the structural
   fresh-phrasing gate in [references/boundary.md](references/boundary.md).
   Make the fragmentary fact inventory there, then set source architecture and
   wording aside before drafting. Expert examples in references are analysis
   examples, not lines to echo into generated prose.

## Invariants across surfaces

- Use a common noun and a concrete verb first (**kitchen-table** language on
  places, creatures, and items alike: river mouths, not river cuts; body, not
  lobed mantle). Use a specialist term only when the common word would be wrong
  or too vague for a table decision. Add at most one unusual comparison when it
  makes the thing clearer. Give one setting-specific signature property
  (material, practice, sound, behavior, or contradiction) to a usable noun or
  affordance. Generic mood must come from evidence. A signature or camouflage claim must be
  **drawable evidence** (named color, material, edge, mismatch a looker could
  miss), not a purple merge (`takes branch and leaf`, `becomes the canopy`,
  `merges with the green`). Do not fake completeness with **mood-by-negation**
  (`rather than glitter`, `not flashy`, `without dazzle`) or a **cover-story
  simile** that replaces a drawable physical behavior (`spins like a meditation
  focus`).
- **No em dashes** (`—`) or en-dash stand-ins in player-facing prose. Use a
  period, comma, or parenthesis. Examples teach moves, not punctuation or
  sentence architecture to echo.
- Prefer flowing prose over bullet-shaped sentences. Fold color, material,
  posture, and minor anatomy onto the body or place that owns them. A portrait
  or first look should leave a drawable whole after one hearing; a single dry
  identifying sentence is usually too thin unless the surface is a hit, reveal,
  or dialogue turn.
- Characters perceive; players interpret. Never narrate a PC's feeling,
  thought, choice, route, conclusion, or unresolved outcome. Show the resolved
  stimulus, behavior, and consequence, then leave the next player response
  open. For a standalone creature response state, use the terminal pattern
  `observable stimulus → observable response → stop`; do not explain what is
  unseen or what the response means. See [references/boundary.md](references/boundary.md)
  for the structural and creature-response gates.
- Keep facts within the current viewpoint, established automatic knowledge,
  a declared and resolved interaction, or earned public canon. A permissible
  inference must follow from named perceivable evidence or established
  knowledge; “maybe” does not make an invented detail safe. Source silence is
  not permission to fill a gap with genre defaults. Do not let vivid language
  smuggle in an unearned interior, history, function, magic, motive, or rule.
- Source wording is not player-facing canon. Preserve supported facts while
  materially rephrasing parent and reference prose; retain only proper names,
  necessary measurements, and irreducible game terms when paraphrase would
  change identity or accuracy. Explicitly requested in-world quotations are the
  sole narrow exception.
- Use the branch's tense, wrapper, and shape. A player-safe surface contains no
  `[!secret]-` material, hidden certainty, DC, HP, condition, or other private
  procedure. Reread it as a player who cannot rewind.

## Spatial work

Place, encounter, travel, and vehicle writing use the spatial camera and
staging method in [references/surfaces.md](references/surfaces.md) and
[references/places.md](references/places.md). Within that branch, seat one
camera, choose one frame, relate landmarks to it, and keep distances and
units consistent. For a spatial first look, a stranger should be able to say
where they are, what they see, what is moving, and what matters now. A located
change is a useful live handle, not a mandatory ending when the scene has no
current movement.

Use cardinal direction words when they clarify player orientation. If a
battlemap is present, use the shared map frame: top is north, right is east,
bottom is south, and left is west. Fold only the relevant directions into the
spoken block as natural geography; do not recite all four compass entries
unless the scene is a true survey.

Use concrete measurement on DM-facing zones and positioning. Spatial and travel
prose may use north, south, east, west, feet for tactical 5.5e distance, and
days, hours, or minutes for travel time. Player-facing spoken distance defaults
to relational bands (Melee, Near, Far); exact measurements appear in spoken
look only when a rule or encounter makes them perceptible and
decision-constraining. Coordinates disguised as prose are incomplete.

The spatial staging card is a private drafting aid: viewpoint, compass frame,
concrete distance or travel time, blocked paths, three to five anchors, and the
current opening. Audit visible entrances, exits, retreat, cover, blocked paths,
and traversable hazards whenever those facts affect a decision. Introduce each
landmark once, then reuse it.

**Scene-setting (session-beat `Initial Narration`):** address the party as
**you**. Present tense. Do not say "the crew". Do not narrate a feeling,
thought, or choice (`you feel afraid`, `you decide`). Do not assign PC body
reactions (`sweat on the neck`, `your nose crinkles`); body-scale environment
comes from the space. Layer 1 seats the party in the space before listing
furniture; the criterion is in Authoring outcomes and the moves are in
[references/places.md](references/places.md). An owner identity image on the
run card is a DM glance; it does not replace the spoken look. Open those
**pixels** so the spoken look matches the art. Then stop on a live situation
and ask.

**Session-beat spoken fill is pass 3.** Pass 1 (`run-guide`) leaves empty prose
slots, and pass 2 (`writing-for-humans`) edits DM-facing copy first. Load this skill
only when pass 3 begins, then fill every spoken slot. The DM may skip a block
at the table; the writer fills all of them.

**Callout stubs:** `Initial Narration` (Layer 1 immediate frame),
one `How the Scene Resolves` for the unconditional end state, `{Creature}` after each roster embed,
`Exit` only when the next cockpit is on the same file. Most-likely options sit in a table beside that callout (`run-guide`).

**Beat-type stubs:** all session-beat stubs use second person, present tense,
and end on a live situation. The Beat job in Authoring outcomes above governs
what each type must accomplish. Smaller stubs (zone, tick, How the Scene
Resolves, creature-in-scene) are one job per slot. Intensity comes from
concrete specificity, not purple language or longer blocks.

**Table Narration columns:** when Zones, Threat clock, or How the Scene Resolves
options tables include a Narration column, write conditional spoken prose in
that cell as `==_italic_==` — one to three sentences, one job per cell. These
replace `{Place}` and `Tick {n}` stubs, and they replace stacked variant
callouts. When a Zones or Threat clock column is absent, fill callout stubs
after the table instead.

Smaller blocks (zone, tick, How the Scene Resolves, creature-in-scene) do not restage
Initial Narration. Each stub shows only what is **new, changed, or newly
actionable** at that moment — not a second pass over facts already spoken.

## Draft and review

Choose the branch, select the facts that pass the boundary, and draft only to
its natural stop. Keep a signature property tied to an affordance, not floating
as decoration. Draft in connected prose first — whole picture, then trim —
rather than starting from a one-line stub and padding.

Read the result aloud once. Ask the branch's questions from
[references/surfaces.md](references/surfaces.md), then run the slop gate,
repetition and specificity scan, and thin gate in [references/voice.md](references/voice.md). Fail the draft if a
player hearing it once cannot sketch or distinguish the subject. Fail a
situated session-beat Initial Narration if the Layer 1 immediate frame does not
give the table a stable shared picture and something live to respond to, or if
scene stock was left as a DM list under the callout.
Cut telegram lists, isolated details, private metaphors, premature labels,
unsupported mechanics, future outcomes, and repeated line-of-sight, cover,
route, or absence claims. Cut purple register that adds no drawable fact. Add
the missing noun, relationship, second sense, access, or opening when the
picture or agency is incomplete — never by stacking synonyms.

For **session-beat** situated narration, use second person and present tense:
**you see**, **you hear**, **you feel** (physical), **you smell**. Owner-page
cold portraits stay third person (no party in frame). Dialogue can be quoted.
Recaps use past tense. Handouts retain their diegetic owner's voice. Draft
layers, staging cards, analysis, and routing labels stay off the player-facing
page.

## Cinematic framing gate

Cinematic framing is a **shot**, not an inventory: choose one striking,
supported image and make visible energy or movement legible when the table state
supports it. Do not enumerate every object, narrate mood as instruction, or use
cinematic language to manufacture drama. The `[!narration]` surface remains
player-safe: no secrets, DCs, hidden mechanics, unearned identities, or private
stakes. Keep dramatic pressure in what can be perceived and acted on; put the
rest in DM procedure or secret callouts.
