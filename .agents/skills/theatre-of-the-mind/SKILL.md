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

Load `.agents/skills/writing-for-humans/SKILL.md` if not already read this
session — it owns DM-facing prose standards that player-facing prose inherits.

File what constitution X makes canon. Follow `docs/agents/work.md`.

Apply **HARD: entity-before-spoken** and **HARD: dm-facing-explicit** from
`AGENTS.md`. Mint owner pages before writing prose that names them; make DM
layers concrete, never coy.

Show a chat proposal; write a wiki page only after DM accept. Set
`invention: true` and ground in wiki pages and/or 5e rules when the wiki
lacks the fact. Cite `[[pages]]` for wiki claims. Show contradictions. Never
present invention as wiki fact. Never write silent canon. `lifecycle: proposed`
until accepted.

All spoken copy is Work for the DM and player-safe; `[!narration]` is the
spoken slot.

## Process

### 1. Choose the mode

Decide **situated moment** or **standalone portrait** before anything else.

**Cold portrait gate:** when no party, encounter, or table state is supplied,
the mode is **standalone cold portrait**. Read
[references/cold-portraits.md](references/cold-portraits.md) for the matching
contract:

| Subject | Covers | Excludes |
|---|---|---|
| Creature / monster | Silhouette, scale, parts, ordinary habit | Tactics, resolved attacks, time-skip scripts |
| Location / site | Body-scale size, spine, affordance | Kernel fields, Aspects, mystery closers |
| Hazard | Form, material, one warning | Contact film, valley camera, aftermath |
| Faction | Method footprint, shared title, Tell signs | Secret agenda, hunt clocks, DM pressure |
| Technique | Breath, stance, form-in-use | Venue, mysticism, resolved hit |
| Object / weapon | Noun, scale, material, one sense/behavior | Lore closers, rarity, DCs, catalog gloss |

- **Situated moment:** write from supplied table state and viewpoint. Route by
  surface contract. On a creature first look, stop at the **reaction point**:
  visible telegraph only, before resolved contact. A hidden or ambushing
  creature is not narrated directly — describe the environment so discovery
  happens in play; "waits" or "lies in ambush" spoils the scene.
- **Standalone portrait:** self-contained player reference for one subject.
  Hierarchically cover established player-visible identity: whole/silhouette,
  scale, defining parts or material — lead with the most unusual or
  distinguishing feature (extra limbs, missing parts, an anomalous proportion)
  — ordinary behavior when canon supplies it, and one signature sensory fact
  when supported. The default knowledge scope is
  the public appearance layer, even when the parent is addressed to `[agent, dm]`.
  Render identified properties separately only when explicitly granted. Choose
  the organizing spine independently of source order. The portrait's completion
  test: a player can recognize, picture, and distinguish the subject after one
  reading.

**Workshop vocabulary stays out of player prose.** `[!narration]` uses plain
language, never `telegraph`, `tell ends`, `reaction point`, `cold portrait`,
`hookline`, or `at the table` as labels. Stop by omission — the last image is
the windup.

### 2. Read the references

Read [references/surfaces.md](references/surfaces.md) for the surface contract
and natural stop. Then read [references/examples.md](references/examples.md)
and [references/voice.md](references/voice.md). Read the matching specialist
reference and one other:

| Job | Primary | Also read |
|---|---|---|
| Spatial (place, encounter, travel, vehicle) | [places.md](references/places.md) | one of the others |
| Object, item, landmark | [humans.md](references/humans.md) | places.md if in a scene |
| Creature, monster, combat | [experts.md](references/experts.md) | places.md if spatial |
| Person, NPC, dialogue | [npcs.md](references/npcs.md) | humans.md for an object cue |

A business/shop/tavern uses the Business row in surfaces.md; no other
reference authorizes filling missing stock or layout.

### 3. Read the parent and gather facts

Read the owning parent and current table state. Preserve established and locked
canon. Distinguish beliefs from facts. If the parent lacks a usable signature,
first-sight facts, or affordance, invoke the owning craft skill before drafting.

**Already-spoken gate (session-beat stubs):** read the previous beat's spoken
prose and this beat's own Initial Narration before drafting stubs. Facts already
spoken do not reappear as discovery unless the scene has physically changed.

**Pixels.** When the job is `[!narration]`, a portrait, a first look, or
scene-setting, and related images exist: read
[references/vision.md](references/vision.md) and open the image files before
drafting. Skip for hit lines, recaps, dialogue, and jobs with no related art.

**Access gate.** Run evidence-of-access and hidden-truth checks in
[references/boundary.md](references/boundary.md). Every player-facing detail
needs a legitimate channel. An uncertainty marker cannot create access.

**Standalone composition.** For a portrait, compose before enumerating: make a
private thumbnail (whole + one dominant distinction), then a private unordered
coverage checklist as an audit, not an outline. Choose an organizing spine
independently of both source and checklist order. Draft around the spine; audit
coverage afterward.

**Fresh phrasing.** Use the structural gate in
[references/boundary.md](references/boundary.md). Make a fragmentary fact
inventory, set source architecture aside, then draft fresh.

### 4. Draft

Choose the branch, select the facts that pass the boundary, and draft to its
natural stop. Draft connected prose first — whole picture, then trim — rather
than starting from a stub and padding. Keep a signature property tied to an
affordance, not floating as decoration.

**Tense and person.** Session-beat situated narration: second person, present
tense. Cold portraits: third person. Dialogue: quoted. Recaps: past tense.
Handouts: diegetic owner's voice. Staging cards, analysis labels, and routing
labels stay off the player-facing page.

### 5. Review

Read the result aloud. Ask the branch's questions from surfaces.md, then run
the slop gate, repetition and specificity scan, and thin gate in
[references/voice.md](references/voice.md). Kill any phrase you cannot
physically picture — if the words don't map to a shape, material, or motion,
they are slop.

**Fail** if a player hearing it once cannot sketch or distinguish the subject.
**Fail** a situated Initial Narration if the Layer 1 frame gives no stable
shared picture or nothing live to respond to. Cut telegram lists, private
metaphors, premature labels, unsupported mechanics, future outcomes, and purple
register that adds no drawable fact. Add the missing noun, relationship, sense,
or opening when the picture is incomplete.

## Beat jobs

Every situated scene opening names a Beat type and job:

- **Hook** — immediate interest with minimal orientation first.
- **Development** — changed information unmistakable.
- **Cliffhanger** — danger or instability front-loaded.
- **Climax** — opposition, stakes, features, in-motion consequences clear.
  Outcomes stay open: no victory, defeat, sacrifice, or escape narrated.
- **Resolution** — visible consequences only. Conditional variants when the
  Climax can end substantially differently.

Beat job is one sentence. Required when Beat is set. Decorative prose with no
job is incomplete. Portraits and short updates do not take a Beat type.

## Authoring standards

Player-facing prose for a prepared Beat is complete before the session so the DM
can read it without inventing the opening picture. Spoken look that depends on
runtime player decisions (turn-by-turn combat, top-of-round summaries) is not
prewritten.

**Agency.** Player-facing narration describes the world. Show the resolved
stimulus, behavior, and consequence, then leave the response open. Incomplete:
PC action, thought, emotion, intent, choice, or unresolved outcome in the spoken
block. Involuntary reactions go through the environment (`heat rolls from the
furnace`), never assigned to a PC body (`sweat on your neck`).

**State independence.** Blocks remain usable regardless of party formation,
position, resources, or approach — unless the Beat guarantees the resulting
state. Important elements relate to one another (beneath, beyond, blocking).
Isolated inventories are incomplete.

**Interactive problems.** Traps, hazards, and trials expose a visible symptom or
usable clue so a solution is available in play. Betrayal and sabotage remain
detectable opportunities, not predetermined outcomes.

**Wiki portrait.** A standalone wiki portrait remains valid across sessions: no
party state, no encounter, no unlabeled transient facts. Completeness is
recognizable identity anchors for the target contract.

Every sentence changes the picture, attention, risk, route, relationship, or
possible action. Draft the full picture first; trim only sentences that add no
drawable fact. A complete block paints a scene a player can sketch — truncating
to a stub is worse than an extra sentence of grounded detail.

## Session-beat specifics

**Pass 3.** Pass 1 (`run-guide`) leaves empty prose slots; pass 2
(`writing-for-humans`) edits DM-facing copy. Load this skill when pass 3
begins, then fill every spoken slot.

**Scene-setting (`Initial Narration`):** address the party as **you**, present
tense. Layer 1 seats the party in the space at body scale (size, ground, air,
light) before listing furniture. Open **pixels** so the spoken look matches the
art. Stop on a live situation.

**Callout stubs:**
- `Initial Narration` — Layer 1 immediate frame
- `How the Scene Resolves` — one unconditional end state
- `{Creature}` — after each roster embed
- `Exit` — only when the next cockpit is on this file

Most-likely options sit in a table beside the callout (`run-guide`).

**Beat-type stubs:** second person, present tense, end on a live situation. The
Beat job above governs what each type must accomplish. Smaller stubs (zone,
tick, How the Scene Resolves, creature-in-scene) are one to three sentences,
one job per slot, no restage of Initial Narration. Intensity comes from
concrete specificity, not purple language.

**Table Narration columns:** when Zones, Threat clock, or How the Scene Resolves
tables include a Narration column, write conditional spoken prose as
`==_italic_==` — one to three sentences per cell. These replace `{Place}` and
`Tick {n}` stubs. When the column is absent, fill callout stubs after the table.

**Prepared scene facts** use existing beat-card slots: `[!narration]` for spoken
look, Now for fixed truths, Zones for spatial relationships, zone/tick Narration
cells for reveals, Be ready for for adjudication. Omit empty sections.

## Ingest

When `wiki-ingest` loads this skill, named ingest is DM approval for those
sources (`docs/agents/work.md`). Write player-facing `[!narration]` on the
chosen destination. Keep settled look and facts. Polish stubs into flowing
spoken prose. Do not invent a scene the source does not support.

**Complete when:** spoken blocks on the destination are player-safe TotM for
their mode, meaning unchanged.

## Cinematic framing gate

Cinematic framing is a **shot**, not an inventory: choose one striking,
supported image and make visible energy or movement legible when the table state
supports it. The `[!narration]` surface remains player-safe: no secrets, DCs,
hidden mechanics, or unearned identities. Keep dramatic pressure in what can be
perceived and acted on.
