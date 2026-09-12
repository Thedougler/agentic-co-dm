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
  picture — not telegram stubs and not verbose padding.
---

# Theatre of the mind
## Work gate

Prep only. Follow `docs/agents/work.md`. Load `wiki/AGENTS.md`, `copy-writer`, and `obsidian-markdown` on every vault write.

Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Reject leaves no page. Invention is required when the wiki lacks the fact: set `invention: true` and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]` for wiki claims. Show the DM any contradiction with an existing page. Never present invention as a wiki fact. Never write silent canon. A craft `type` becomes `canon` only after DM accept.

Players see nothing until the DM accepts and presents.

Done when: the page is inspectable Work, `lifecycle: proposed`, invention flagged, grounding named.

Remap durable output paths from `campaigns/<slug>/` to `wiki/` (entities/journal as appropriate). Templates live in `wiki/templates/`. Replace knowledge-bank terminology with wiki terminology, but do not change geographic river-bank language. Point at `docs/agents/work.md` rather than restating the glossary.

All spoken copy is Work for the DM and player-safe; `[!narration]` is the spoken slot.


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

**Complete picture, not pad.** Cover every relevant player-visible fact the
surface owes (subject, relationships, senses the viewpoint can use, motion or
stable behavior). Join those facts into connected sentences with plain nouns
and concrete verbs. Do not stop at a single encyclopedic clause when the
picture is still incomplete. Do not add purple adjectives, theme sentences, or
mood claims to fake completeness.

For a session beat, completeness means **scene stock**: every currently
perceivable thing the players can question, touch, take, fight, avoid, follow,
use as cover, learn from, or spend time on. Include hazards, loot, monsters,
routes, navigation handles, lore signs, world-building details, weather, light,
sound, smell, and changing pressure when they are present and accessible. Fold
them into the spoken picture by relationship and use: the idol beside the pit,
the smoke beyond the prints, the glass grass under the only dry route, the
priest's stained sleeve beside the missing coin box. Do not dump a catalog.
Omitting actionable scene stock is a failure; padding the block with
non-actionable color is also a failure.
Player-facing prose is signal-only too: every sentence must change the picture, attention, risk, route, relationship, or possible action. Cut ordinary defaults and no-effect reassurance. State a visible relation once in its strongest place; repeating the same line-of-sight, cover, route, or absence claim in both a table cell and the spoken prose is padding unless the second use changes the picture or choice.

Length still follows the moment: a hit, reveal, or dialogue turn may be one
tight line; a `[!narration]` portrait, room/place first look, creature first
sight, or recap is usually one coherent spoken block (often a short paragraph
of several connected sentences). **Item and creature page `[!narration]`** cold
portraits usually run about **three connected sentences** covering
silhouette/scale, material/parts/wear, and one stable sensory or physical
behavior — not a one- or two-line stub. **Session-beat `Initial Narration`** is
the long *scene-setting* block: typically **two to four short spoken
paragraphs** covering every currently perceivable subject, relationship,
cover/route, relative position, imminent action, drawable appearance, scene
stock, and at least one non-sight sense. Situational beat stubs (zone, tick,
How the Scene Resolves, creature-in-this-scene) are shorter: one to three sentences, one job,
no restage of Initial Narration. Fill missing visual nouns; do not pad with
purple, mood-by-negation, or cover-story similes. Do **not** use the hit-line
license to compress a creature first look or Initial Narration into a
resolved-snatch telegram. Stop at the next meaningful player opening — for a
creature first look or Initial Narration, that is the reaction point
(telegraph), never after the haul.
Do not force every surface into a spoken block, a fixed beat, or a located
change.

When the user requests a full or loaded first look, produce one coherent spoken
block containing every relevant subject and relationship currently perceivable:
locations and routes, NPCs, creatures, items, and current motion. Attention
hierarchy and fold keep that block drawable; the anchor ceiling is a selection
aid, never permission to omit relevant visible facts. Exclude hidden items,
unearned identities or mechanics, future action, and player choice. A partial
doorway snapshot is appropriate only when the user explicitly asks for that
limited view.

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
of **stable public geography** with **one spine that is already this place**
(not the concept of a lake/forest/room — Colville). Fold landmarks as dependents
of that spine. Fail **Strong-echo / checklist cadence** (one fact per sentence
in shore → depth → mouths → Grove → cool air order, or parroting a Strong
example’s architecture). Fail thin telegram openers (`The shore is wet stone.`).
Require body-scale size and at least one usable affordance cue as nouns/verbs
(wet stone underfoot, followable channel, climbable ledge) — never theme
(`rest`/`direction`). Ban place-design kernel fields and schema voice: Function,
Fantastic, Conflict, Promise, Trajectory, Aspects, Player verbs, Hunger /
possession metaphysics, and rule-talk like `unclaimed` / `claim`. Ban invented
mystery closers and staged located-change drama unless current table state
supplies that motion. Creature signs and encounter pressure belong to a
**situated** first look. Design kernels stay upstream (`place-design`); TotM
renders geography. Respect the owning note's `Where` ledger; do not invent
north/east/south/west neighbors or travel-day distances. Examples teach moves,
not sentence architecture to echo.

Cold-place sweep bans: never use the rigid definition -> smell hang-over -> use/closer formula. Do not close on a thesis (treated as a border), leak Aspects/secrets (charts get wrong, Hunger/free-flow ownership), or use opaque caste/jargon nouns (Purple watch, Unknown-quarry stone). Darts, a blue watcher, and similar staged hostility require current table state unless the parent explicitly establishes stable public ecology without encounter film. A dual-title note must publicly render both halves or be retitled. Keep vehicle access kitchen-table (lines, rail, hold), never boarding interface in player prose. Keep lore miracles such as the duck has died and reformed in Secrets/DM. The cold spine is already this place plus body-scale geography and a drawable affordance, and it stops on stable geography.

**Hard mode gate for hazard notes (`[!narration]` on a hazard page):** if no
current table state is supplied, write a **standalone cold hazard portrait**.
The hazard body or patch is the grammatical and attentional subject. Do not
route it through the creature contract (no Hookline/Reel-style contact film)
or the place contract (no invented valley camera and no lake/terrain spine).
Usually use about three connected sentences to make the patch drawable: form
and scale, positive material or construction, and one positive sensory or
physical warning. Prefer kitchen-table words: plain spoken nouns and concrete
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


**Hard mode gate for faction/organization notes (`[!narration]` on a faction or organization page):** when no current table state is supplied, use a standalone **cold faction portrait**. Give it a length floor of about **four connected sentences** (usually four to six), then stop; a one- or two-sentence telegram fails this mode. The public mask comes first, followed by one concrete, kitchen-table method footprint, one environmental **Tell** that a bystander could notice, and a shared title or face cue when the parent supplies one. These are coverage dimensions, not a rigid sentence order, and they must join into drawable prose rather than an abstract organization gloss. In the player-facing block, these are craft labels, not words to say: never use `mask`, `footprint`, `Tell`, or `face cue` in faction `[!narration]`; render the concrete signs directly.

Keep secret agenda, Rule of Two, hunt clocks, and other DM-only pressure out of faction Appearance. Ban workshop abstractions such as `martial reach`, `dropped the ledgers`, or ledger language used as a vague organizational label; use only supported concrete signs such as missing names or records, one-job hires, or a shared title. Do not invent a plot, venue, encounter, or hidden motive to meet the length floor. Stop once those public facts are shown, ending on the shared title as the name people hear.


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
Coverage (flowing prose, ~3 sentences — dimensions, not a checklist dump):
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

Use concrete measurement. Spatial and travel prose may use north, south, east,
west, feet for tactical 5.5e distance, and days, hours, or minutes for travel
time. Do not use range bands, distance bands, near, far, close, nearby,
distant, inner, or outer as measurements. If one of those words appears as
ordinary descriptive prose, pair it with a concrete direction, distance, or
travel time when orientation matters.

The spatial staging card is a private drafting aid: viewpoint, compass frame,
concrete distance or travel time, blocked paths, three to five anchors, and the
current opening. Audit visible entrances, exits, retreat, cover, blocked paths,
and traversable hazards whenever those facts affect a decision. Introduce each
landmark once, then reuse it.

For a requested full or loaded spatial first look, complete the current visible
state in that one block before stopping: include every relevant visible subject,
relationship, route, and motion, while leaving hidden items and future outcomes
out. Stop after that complete state at its pressure or opening. Only an
explicitly requested doorway-only snapshot may be intentionally partial.

**Scene-setting (session-beat `Initial Narration`):** address the party as
**you**. Present tense. Lead with sensory verbs: **you see**, **you hear**,
**you feel** (physical: wind, current, heat, mud), **you smell** when the
viewpoint supports it. Do not say "the crew". Do not narrate a feeling,
thought, or choice (`you feel afraid`, `you decide`). The spoken block must
already contain the facts the table needs for the first decision (Angry GM:
goal, obstacle, tools on hand). Currently perceivable cover, routes, relative
position, who is being hunted, imminent action, drawable appearance, and at
least one non-sight sense join as flowing spoken prose. Weave look and sound
into the sentences. Do not park them as a DM catalog under the callout. An owner identity image on the run
card is a DM glance; it does not replace the spoken look. Open those **pixels**
so the spoken look matches the art. An adult striking
other prey may be visible windup; do not resolve PC injury. Visible grass,
river, or shipward sky that is already under or beside them belongs in this
block, not on a later clock tick. Then stop at the reaction point and ask.

**Session-beat spoken fill is pass 3.** Pass 1 (`run-guide`) leaves empty prose
slots, and pass 2 (`copy-writer`) edits DM-facing copy first. Load this skill
only when pass 3 begins, then fill every spoken slot. The DM may skip a block
at the table; the writer fills all of them.

**Callout stubs:** `Initial Narration` (mandatory, long scene-setting),
one `How the Scene Resolves` for the unconditional end state, `{Creature}` after each roster embed,
`Exit` only when the next cockpit is on the same file. Most-likely options sit in a table beside that callout (`run-guide`).

**Cliffhanger beat narration:** a Cliffhanger stub carries the same contracts
as other session-beat stubs with a physical-pressure focus. Initial Narration
front-loads the visible danger, the contested position or resource, the
available routes/tools, the relevant scene stock, and the cost already in
motion. The natural stop is the reaction point: the danger is visible and the
outcome is unresolved. Smaller Cliffhanger stubs are short combat, chase,
escape, or pressure updates that show what physically changed and what can be
acted on next.

**Climax beat narration:** a climax stub carries the same contracts as other
session-beat stubs (second person, present tense, sensory verbs, reaction
point) with three additions. First, make costs and stakes **perceivable**: if
the sacrifice, defense, negotiation, or catastrophe has visible consequences,
those consequences belong in the spoken block as concrete nouns — not as DM
summary after the fact. Second, **echo prior choices**: things the party did
in earlier beats should be visible in the environment, NPC behavior, or
available options — the climax narration connects the session's thread. Third,
the **resolution transition**: the final climax stub (How the Scene Resolves or last tick)
describes the changed world in present tense before the DM asks what the party
does next. A climax stub is still one to three sentences per slot; intensity
comes from concrete specificity, not from longer blocks or purple language.

**Development beat narration:** a Development stub uses the same tense and
viewpoint contracts as other session-beat stubs (second person, present tense,
sensory verbs) with a different focus. Initial Narration shows who is present
and what they are doing, the social or environmental atmosphere, discoverable
details, relevant scene stock, and at least one non-sight sense. The spoken
picture carries what the players can perceive, question, or act on in a
conversation or investigation — make discoverable details concrete and
drawable. The natural stop is the **decision point**: enough visible information
is on the table for players to choose what to ask, propose, or do. Smaller
Development stubs (an NPC's visible reaction, a revealed object, a pressure
moment) are one to three sentences, one job per slot. Intensity in a
Development comes from specificity of detail and social tension, not physical
danger language.

**Hook beat narration:** a Hook stub uses the same contracts as other
session-beat stubs (second person, present tense, sensory verbs, reaction
point) with a **strong-start** focus. Initial Narration is the most critical
spoken block of the session — it must land the situation in one continuous
delivery and leave the party ready to act. Lead with the immediate pressure:
what is happening, who is at stake, what demands attention right now. Make
the opening problem perceivable and actionable within the first paragraph:
visible danger, an urgent offer, a discovery with consequences, or a crisis
already in motion. Weave drawable appearance and at least one non-sight sense
into the opening picture, including the scene stock needed for the first real
choice. The reaction point for a Hook is the first player decision of the
session — stop when the party has enough to choose a response, not after the DM
has described every prepared element. Smaller Hook stubs (zone, tick, How the Scene Resolves)
stay one to three sentences, one job. Intensity in a Hook comes from immediacy
and concrete stakes, not volume or purple urgency.

**Resolution beat narration:** a Resolution stub shows the aftermath at the
same scale as the Climax. Initial Narration shows what changed, what remains
usable or lost, who is present, what costs are visible, what rewards or routes
are now accessible, and which unresolved pressure is still perceivable. The
natural stop is a renewed choice: players can name what is different and what
they want next. Do not smuggle in DM conclusions, future montage, or moral
summary.

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
[references/surfaces.md](references/surfaces.md), then run the slop and thin
gates in [references/voice.md](references/voice.md). Fail the draft if a
player hearing it once cannot sketch or distinguish the subject. Fail a
situated session-beat Initial Narration if the table is asked to act before
they have currently visible cover, routes, relative position, imminent action,
relevant scene stock, drawable look, and a non-sight sense, or if
look/sound/scene stock were left as a DM list under the callout.
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
