---
name: run-guide
description: >-
  Assemble a table-ready, DM-only cockpit for one session or one 30-minute beat
  from existing prep and owner pages in the vault's lean style: flat, direct,
  and only as sectioned as play requires. Use for "run tonight", "build a run
  guide", or a session-prep document that is hard to scan. Four passes, each
  loading only its skills: pass 1 (dnd5e-mechanics) writes the mechanical card
  plus empty [!narration] stubs; pass 2 (copy-writer) edits DM-facing copy;
  pass 3 (theatre-of-the-mind) fills every spoken stub; pass 4 checks Reading
  view. Do not load a later pass's skill early. Not beat composition, canon
  invention, or session reconciliation.
---

# Run Guide
## Work gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Reject leaves no page. Invention is required when the wiki lacks the fact: set `invention: true` and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]` for wiki claims. Show the DM any contradiction with an existing page. Never present invention as a wiki fact. Never write silent canon. A craft `type` becomes `canon` only after DM accept.

Players see nothing until the DM accepts and presents.

Done when: the page is inspectable Work, `lifecycle: proposed`, invention flagged, grounding named.

Remap durable session-prep to `wiki/journal/sessions/<campaign-slug>/<session-number>/`. Owners stay under `wiki/`. Templates live in `wiki/templates/`. Replace knowledge-bank terminology with wiki terminology, but do not change geographic river-bank language. Point at `docs/agents/work.md` rather than restating the glossary.


Build one **cockpit** the DM can run from Reading view without hunting the vault.
Owners stay canon. Full statblocks **embed** at the bottom (the DM scrolls).
Scene *procedure*, zones, tells, action cards, and how the scene resolves are written here.
A missing owner is a diagnostic, not permission to invent canon or math.

**Four passes, each loading only its skills.** Pass 1 (`dnd5e-mechanics`) writes the mechanical card and **empty titled `[!narration]` stubs** — no prose skills loaded. Pass 2 (`copy-writer`) edits DM-facing copy for usability, readability, and table usefulness — stubs stay empty. Pass 3 (`theatre-of-the-mind`; TUI **copy-writer**, Grok Bots **Visualizer**) fills every spoken stub — loaded only after DM copy is clean. Pass 4 checks Reading view. Do not load a later pass's skill early.

**Sole-authority:** a tired DM at minute 90 can roll and speak this slice
without opening another note. Every default-mode *ruling* lives on the card.
Combat-mode owners are heading-embedded below. A bare `[[Monster]]` with no
embed and no action-card numbers fails.

One opposition want, said once. One *procedure*, named. Nothing restated later
as a second framework.

**Session 11 cockpit.** Required job order is the Session 11 beat cards (`wiki/_raw/Session-11-01-Angry-Birds.md` through `wiki/_raw/Session-11-10-Aftermath.md`). Those files illustrate quality; do not photocopy a named Session 11 title. Omit a section only when that job is absent — no empty heading. Preserve heading spine, section names, and order when editing.

**Image anchors.** If the beat has an overview or identity image, keep it near
the top of the file as the visual first look. If the beat has battlemap art,
keep it fixed at the bottom of the file after the runnable card. These anchors
are placement rules for existing art, not permission to add unused sections.

**Concrete measure.** Spatial and travel notes use concrete units: north,
south, east, west, feet for tactical 5.5e distances, and days, hours, or
minutes for travel time. Do not use distance bands, range bands, or abstract
labels such as near, far, close, inner, outer, nearby, or distant as the
measurement. A label may name a place only when the concrete direction,
distance, or travel time is also present.

**Recap boundary.** Only the first beat of a session may recap the previous
session. Every later beat starts from the immediate current situation and does
not summarize earlier beats, prior-session events, or how the party got here.

**No coy DM text.** The card is for the DM. If the DM needs to know who or what
is present, name it plainly in DM-facing text. If the players have not earned
that knowledge, keep it out of `[!narration]`; do not write vague placeholders
such as "a figure may be there" or instructions such as "do not call that out."

A DM-facing line stays only if Nick will use it this slice to **place** someone,
**roll** something, **speak**, or decide a changed risk, route, clock, resource,
or NPC response. Distances, speeds, named *rulings*, the opposition want, and
the spoken block earn their keep. Default safety, ordinary permission, Partial
rules, 5e defaults, schema commentary, and notes to the writer stay out.
Negative facts earn space only when they change a current choice or ruling.
Use descriptive, specific, plain language on the DM card too. Use common,
normal human words unless the common word would be inaccurate. If a name or
field needs decoding, replace it with the ordinary thing and visible action.

## Workflow — four passes

Each pass loads only the skills it needs. Do not load a later pass's skill
early — loading `copy-writer` during mechanics writing pulls attention toward
prose polish before the structure exists; loading `theatre-of-the-mind` before
DM copy is clean fills spoken slots over broken scaffolding. The pass boundary
is a skill-load boundary.

### Pre-pass: Ground and Diagnose

**Load:** `.agents/skills/qmd` plus `specs/004-qmd-search-default/contracts/retrieval-precedence.md`. No other skills yet.

1. **Ground.** Read `hot.md`, tonight's session prep, the latest log, the
   previous beat card when one exists, and only the linked owners needed to
   interpret this slice. Read each working file end-to-end before editing it;
   summaries, snippets, truncated output, and range reads may help target the
   file but do not satisfy grounding. The previous beat's How the Scene
   Resolves is this beat's entry state — the situation, position, and changed
   world the party walks in with. Verify beat identity: the card filename's
   number matches its skeleton position (`Session-<session>-<NN>-Label.md` =
   beat NN), its purpose and dramatis personae match the skeleton, and its
   hand-off targets the skeleton's next beat. Mismatch → rename the file
   before writing. Completion: beat identity confirmed; entry state known from
   the previous beat; every working file has been read end-to-end; every named
   actor, place, and item has an owner path or is marked unknown.

2. **Diagnose.** Mark each beat `ready`, `missing owner`, `missing prep`, or
   `proposal`. Identify the central element the table will ask the DM to
   describe — the skeleton's Purpose and Table sees name it. That element and
   its dramatis personae must have owners before the card is written; create
   via the appropriate craft skill (`npc-design`, `place-design`,
   `vehicle-design`). Missing mechanical stock → owning skill (`encounter-prep`,
   `session-beats`). Missing player-visible scene stock → owning page or craft
   skill before TotM fill. Empty `[!narration]` stubs are expected on this pass;
   TotM fill is pass 3. A creature you will roll that has no owner →
   `homebrew-monsters-5e`. Choose live beats. Completion: no invented canon;
   the central element has an owner; every actionable hazard, loot, monster,
   route, clue, lore sign, and world detail has an owner or is marked unknown.

### Pass 1: Mechanical cockpit

**Load:** `dnd5e-mechanics`. Also `session-beats` when beat composition or
pacing is missing, `encounter-prep` when encounter stock is missing. Do **not**
load `copy-writer` or `theatre-of-the-mind` on this pass.

This pass builds the runnable structure: every section, table, ruling, DC,
action card, clock, zone, and procedure the DM will use, plus the empty prose
slots that later passes fill. Player-facing prose is not written here.

3. **Write mechanics.** Load `dnd5e-mechanics` before writing or auditing any
   player-interaction mechanics: checks, saves, DCs, Hide/Search/Study/Influence/
   Utilize resolution, grapples, shoves, attacks, damage, quality ladders, or
   player actions mapped to a roll. Completion: every player interaction is a
   5.5e ruling with a consequence that changes play, or it stays ordinary
   fiction with no roll language.

4. **Write one cockpit per live beat** in play order. Keep only sections that
   this beat spends at the table. Place **empty titled
   `[!narration]` stubs** at the required slots in **TotM stubs**. Embed an
   existing owner identity image (`![[attachments/…]]`) when the owner page
   already lists one; do not mint art. Completion: every mechanical field this
   slice will use is present; unused sections are absent; clock and Be ready for
   are one *procedure*, not two escalation tracks. Every `[!narration]` body is
   empty. Every Narration table column cell is empty.

### Pass 2: DM copy

**Load:** `copy-writer`. Do **not** load `theatre-of-the-mind` on this pass.

This pass edits the DM-facing text that pass 1 wrote — Scene ends when, Glance,
Now, Procedure, Be ready for, clocks, action cards, How the Scene Resolves — for
usability, readability, and signal density. The `[!narration]` stubs stay empty.
`copy-writer` owns the prose quality bar; this skill owns the cockpit structure.
If a structural gap surfaces (missing section, wrong field order), fix it before
polishing copy.

5. **Edit DM copy.** Read the mechanical cockpit end-to-end, then edit every
   DM-facing heading and body for table usefulness. Apply the `copy-writer`
   earn-it test: remove a line; if no choice, ruling, risk, resource, route,
   clock, NPC response, or spoken picture changes, cut it. Completion: Scene
   ends when, Glance, Now, Procedure, Be ready for, clocks, and How the Scene
   Resolves are complete sentences the DM can scan and use without inventing
   missing rulings. Every `[!narration]` body and Narration column cell is
   still empty.

### Pass 3: Spoken fill

**Load:** `theatre-of-the-mind`. Read its references before drafting:
`references/surfaces.md` for surface routing, `references/voice.md` for the
slop gate, the matching specialist reference, and
`references/boundary.md` for the access and hidden-truth checks. Open related
owner, session, or user-attached images with the vision tool and ground the
spoken picture in the pixels.

This pass fills every empty `[!narration]` stub and every empty Narration table
cell. The DM copy is already clean — spoken prose is built on solid scaffolding.
The DM may skip a block at the table; the writer fills all of them.

6. **Fill narration.** Fill `Initial Narration` first — the Layer 1 immediate
   frame for the players: what is obvious without deliberate investigation,
   with features that matter now already in the fiction. Salient features and
   discoverable information are separate reveal blocks or zone/tick Narration
   cells. Then fill remaining stubs and Narration cells in reading order.
   Completion: every `[!narration]` body is filled; every Narration column cell
   is filled as `==_italic_==`; the Initial Narration gives the table a stable
   shared picture and something live to respond to without hidden truth, DCs,
   mechanics talk, or padded mood; no stub restages Initial Narration.

### Pass 4: Ready check

**Load:** nothing new. `obsidian-markdown` for filing.

One downward pass of the cockpit in Reading view.

7. **Table gate.** Completion: every item in **Table gate** below holds for
   this pass.

8. **File.** `obsidian-markdown` (wikilinks, real newlines, at-table scan, codeblock columns).
   The only callout on the card is `[!narration]`. Layout uses `col` / `col-md` fences, not `[!col]`.
   `./scripts/after-write` on named paths.

## Lean Surface

Frontmatter: `type: session-prep` (or `encounter`),
`visibility: dm`.

Required order: identity; optional first-beat recap; overview art if it exists; Scene ends when + At a Glance; Now; Action cards; Initial Narration; Procedure + Secondary objective if a second question exists; Zones; Be ready for; Threat clock + dials if a fuse exists; How the Scene Resolves; Roster if combat-mode sheets will be rolled; Backup; Battlemap at bottom if art exists. Omit a job only when it is absent.

Filename: `Session-<number>-<beat-number>-<Label>.md` with two-digit beat numbers (`01`, `02`, …) matching skeleton position. File after accept to `wiki/journal/sessions/<campaign-slug>/<session-number>/`. Copy-start: `wiki/templates/session-prep.md`.

At a Glance scans as stakes, goal or exit, danger, silence, situation magnets. Scene ends when states the stop condition, a roughly thirty-minute budget, and behind/ahead cuts when pacing is not obvious. How the Scene Resolves hands to a beat on this session’s skeleton. Default-mode action-card numbers MAY sit on the beat; the beat MUST NOT become a second full owner page.

**Columns.** Session cards use obsidian-columns **codeblock** syntax
(`col` / `col-md`) so `[!narration]` stays a real callout. Syntax:
`obsidian-markdown` [references/COLUMNS.md](../obsidian-markdown/references/COLUMNS.md).
Each row appears only when both sides exist. The right side of Mode and
Clock rows may be a short paragraph, not a heading.

| Row | Left | Right | flexGrow |
|---|---|---|---|
| Overview art | First overview/identity image | Second image | equal |
| Dashboard | `## Scene ends when` | `## At a Glance` | Glance `flexGrow=2` |
| Situation | `## Now` | `## Action cards` | Action cards `flexGrow=2` |
| Mode | `## Procedure` | `## Secondary objective` | Procedure `flexGrow=3` |
| Clock | `## Threat clock` table | Bloodied / cover / dials | Clock `flexGrow=3` |
| Roster | Monster `![[Name#Statblock]]` (two columns max) | Second monster, or omit | equal |

**Full width:** `[!narration]` callouts, Zones table, Be ready for table,
How the Scene Resolves body + options, Backup, Battlemap. Monster roster rows
never exceed two `![[Name#Statblock]]` columns; a leftover odd monster sits
full width. The two-column cap is for monster statblocks only.

| Field | Keep when | Shape |
|---|---|---|
| **Scene ends when** | Every live beat needs a stop condition. | Heading is `## Scene ends when`. First line is the end condition. Then the time budget. Add **If behind:** and **If ahead:** only when the pacing choice is not obvious. |
| **Glance** | Every live beat needs a short at-table scan. | Heading is `## At a Glance`. Bullets: stakes, goal or exit, danger, Silence, and situation magnets. Not a recap except on the session's first beat. |
| **Overview image** | An exact overview or identity image exists. | Embed the image near the top of the file before the runnable sections, usually just after the title or frontmatter. Omit if none exists. |
| **Now** | Positions, distances, speeds, current possession, or starting state would otherwise clutter Glance. | One paragraph. Who starts where, in **feet** when tactical distance matters. Use north, south, east, and west for orientation. Speeds that matter. What a move vs Dash reaches. Current situation once. Do not add a separate Starting state heading. |
| **Action cards** | The DM will roll compact default-mode numbers or follow an opposition loop. | Heading `## Action cards` when paired beside Now. The operational loop and compact numbers you will roll in default mode: AC, hit points when needed, one attack, thresholds, grab, scatter, or bloodied rule. Use owner action names. |
| **Initial Narration** | Every live beat needs the first spoken look. | Empty `> [!narration] Initial Narration` stub on pass 1. Pass 2 fills scene-setting, accessible scene stock, and the first real choice. If the owner already has an identity image, embed `![[attachments/…]]` near this block. |
| **Battlemap** | A battlemap or exact-scene image exists. | Heading `## Battlemap` at the bottom of the file after the runnable card. Embed existing battlemap art from `attachments/`. Use the shared compass: top north, right east, bottom south, left west. Omit if none exists. |
| **Procedure** | The beat has a named mode, fuse, clock trigger, combat switch, pursuit rule, or repeated resolution loop. | Heading `## Procedure`. Name the mode and this slice's trigger once. Not 5e turn order. Not a `[!mechanic]` callout. |
| **Zones** | Positions, routes, cover, distance, search areas, or scene stock matter. | Table: place \| distance in feet \| cover \| narration. Same concrete distances and compass directions as Now. Each row names decision-useful scene stock in that zone. The **Narration** column carries conditional spoken prose as `==_italic_==`, not a callout. When the Narration column is absent, one empty `> [!narration] {Place}` stub per row after the table instead. |
| **Be ready for** | Players are likely to attempt consequential actions, checks, tactics, or negotiations. | Selective ruling table — include only intents that change a ruling, risk, route, clock, resource, NPC response, or information the party gains. Omit ordinary, boring, or redundant actions; unforeseen approaches are ruled from procedure, zones, and clock. Table: intent \| approach \| DC \| success \| partial \| failure. Approach is **Ability (Skill)** when a check applies. DC column is `` `DC 14` ``. Dice and damage in cells are inline code. Applied conditions are **bold**. Name the creature, item, and place in every cell. Every cell is a *ruling*. Include **Assess the situation** only when success and failure both say what changes. No Partial definition on the card. |
| **Threat clock** | A fuse or opposition turn changes the situation. | Heading `## Threat clock`. Table: tick \| what happens \| narration. Named ticks. 3-4 ticks. Each tick states what newly becomes visible, usable, threatened, blocked, or changed. The **Narration** column carries conditional spoken prose as `==_italic_==`. When the column is absent, one empty `> [!narration] Tick {n}` stub per tick after the table instead. Bloodied, cover-reached, and scene dials sit in the right `col-md` beside the clock table. |
| **Secondary objective** | A second question runs in parallel and changes outcome or later consequence. | Heading `## Secondary objective`. One paragraph: beats required, ignore outcome, later consequence. Omit when there is no second objective. |
| **How the Scene Resolves** | Every live beat needs the next state. | Heading is `## How the Scene Resolves`. Write only the most likely options, usually one or two. Each option hands off to a beat on this session's skeleton — it advances the scene, not exits it. Next state, damage already applied, relevant conditions, and what follows. One empty `> [!narration] How the Scene Resolves` for the unconditional spoken state, plus a table for those likely options (`If` \| `Next` \| `Narration`). Narration cells use `==_spoken_==`. Do not stack a titled callout per option. |
| **Exit narration** | The next cockpit is already on this file. | Empty `> [!narration] Exit` on pass 1. Spoken transition on pass 2. Omit until that beat is ready. |
| **Roster embeds** | The DM will roll a creature or item in this beat. | Heading `## Roster`. `![[Monster#Statblock]]` for opposition you will roll in combat mode. Monster statblocks use at most two columns per row; a third monster starts a new row or sits full width. Keep the full fences; the DM scrolls. After each embed: empty `> [!narration] {Creature}`. Item embeds only if this slice spends charges or the item is the pressure. |
| **Backup** | Extra owner links would save table hunting. | Heading `## Backup`. Extra wikilinks only. Omit when all required owners are already embedded or linked above. |
| **Previous-session recap** | Only this file is the first beat of the session. | Keep it brief and player-facing. Omit from every other beat file. |

There is no peer **Round script**. Clock ticks *are* the old R1–R3. The only `> [!` on the card is `[!narration]`.

## TotM stubs

Pass 1 places the player-facing prose slots this beat can actually use. Pass 3
fills every placed slot. The DM may skip a block at the table; construction
should not create slots for outcomes the beat cannot produce.

**Callout stubs** (empty titled `> [!narration]` blocks):
- `Initial Narration` — before the first player choice.
- `How the Scene Resolves` — one unconditional spoken state for what is always true when this beat ends.
- `{Creature}` — after each combat-mode roster embed. Situated look for this scene, not the owner-page cold portrait.
- `Exit` — only when the next cockpit is already on this file.

**Table Narration columns** (conditional spoken as `==_italic_==` in the cell, not a callout):
- Zones table — one cell per zone row. Replaces `{Place}` stubs.
- Threat clock table — one cell per tick row. Replaces `Tick {n}` stubs.
- How the Scene Resolves options table — one cell per most likely option, usually one or two. This table sits with the one unconditional How the Scene Resolves callout.

When a Zones or Threat clock table has no Narration column, use callout stubs after the table instead: `{Place}` per zone, `Tick {n}` per tick.

Do not put `> [!narration]` inside a table cell. Obsidian does not render callouts there. Conditional spoken in a cell is `==_italic_==` (`obsidian-markdown`).

## Scene stock

Before pass 3, make the card able to answer follow-up questions without opening
the vault cold. Record actionable player-visible stock wherever the leanest
surface can hold it: a paragraph, table row, clock tick, how the scene
resolves, or backup link.

Completion: every stock item that belongs in the spoken first look has an access
channel, an owner or local ruling, and a player use. TotM weaves those items
into narration by relationship and affordance. Required first-look details live
on the card, not only in Backup links.

Distinct things need distinct text and media. Existing narration, art, tokens,
and battlemaps are valid only for the exact same owner/site/moment. For new
content, use prior assets as vibe reference and make or request a distinct
asset.

## Beat Type Trimming

Beat type changes which catalog sections earn space. It does not create a
second template.

**Resolution:** keep the aftermath state, Initial Narration, How the Scene Resolves, and any
Zones or Be ready for rows the players can still act on. Cut combat sections
when the opposition is resolved.

**Development:** keep the information pressure: what can be learned, who wants
what, and the consequential approaches. Keep Procedure or Threat clock only
when there is a named mode or external fuse. Cut combat-only sections.

**Hook:** keep the immediate pressure, first response paths, and How the Scene Resolves into
the next state. Keep combat sections only when the hook is itself a combat
encounter. A hook with a cover endpoint does not also run unbounded Travel.

**Travel:** use this skill only when travel is the live slice. Inline one
specific complication, travel time in days, hours, or minutes, every number
needed to run it, and a failure endpoint. Otherwise omit Travel entirely.

## Procedure

Name the mode. Default for a hunt/chase/escape slice is *escape mode*:

1. Failures impose the Be ready for *ruling* only. They never advance the clock.
2. After everyone has acted, if anyone remains exposed (the card’s magnets), advance the threat clock **once** and resolve that tick. Freeze or “we watch” still ticks once at end of round, not per failed check.
3. Several failed checks in one round still produce **one** tick.

On the card, write this slice's trigger (who counts as exposed) and the combat-mode switch. Do not paste 5e turn order or this list.

*Combat mode:* if the party abandons escape and commits to killing the opposition, stop the clock and run the embedded statblocks. Write that switch on the card.

A skill-challenge or social slice uses the same rule: one clock, filled by the card’s named trigger, never by both a table failure *and* a separate tick for the same action.

## Partial

Ruling convention for this skill, not text for the card:

- **Success:** meet or exceed the DC.
- **Partial:** miss by 1–4; the player may accomplish the intent at the listed cost.
- **Failure:** miss by 5 or more, or reject the partial cost.

Table cells assume that. A row may say “binary — no partial” when the fiction has no middle.

## Ruling

A *ruling* is a 5.5e (2024) action, movement in feet, opportunity attack, named condition, ability check, save, or damage; or a **named feature already on a vault owner**. Partial success is defined here, not restated on the card. Check, save, and DC choice → `dnd5e-mechanics`. The written mark → `obsidian-markdown` at-table scan.

5.5e actions: Attack, Dash, Disengage, Dodge, Help, Hide, Influence, Magic, Ready, Search, Study, Utilize. Conditions include Prone, Grappled, Restrained.

An evocative label (`scattered`, `crash-landed`) is a name for a *ruling* already stated (lands 30 feet away; 2d6 bludgeoning and Prone). New action types, conditions, or resolution systems are a brew-skill job (`homebrew-monsters-5e`), not a line on this card.

## Now (positions)

Write where people are, the distances in **feet**, the compass directions that
matter, the speeds that matter, and what a move or Dash reaches from here, in
the Now paragraph. Reuse those distances and directions in the zone table. Do
not invent a second movement model later. Place labels do not replace concrete
measurements. There is no separate Starting state heading.

## Scene-setting (Initial Narration)

`theatre-of-the-mind` owns the prose. This skill owns **what must already be in the spoken block** before the question.

Pass 1 leaves `> [!narration] Initial Narration` empty. Pass 3 fills the
**Layer 1 immediate frame**: what is obvious without deliberate investigation,
joined as flowing spoken prose. Salient features, discoverable information, and
deeper facts are separate complete reveal blocks or zone/tick Narration cells
(Layers 2–3) that describe the discovery, not the method. Features that matter
tactically or interactively belong in Layer 1 before a player would need them.
Those facts are not a DM catalog under the callout. If the owner already has an
identity or overview image, keep it as the top visual anchor; the image does
not replace the spoken look.
If a battlemap is present, orient routes, zones, cover, and exits with the same
compass used by the map: top north, right east, bottom south, left west. Use
cardinal words where they help the table hold the scene; do not turn Initial
Narration into a compass checklist.

Stop on a live situation, then “What do you do?”

## Time and cut lines

A 30-minute beat states expected minutes and two *cut lines* (Sly Flourish: Watch the Time). Do not paste a minute-by-minute script of how to spend the half hour. A climax beat's "If behind" compresses the confrontation (fewer zones, faster clock) rather than skipping it; the central question still resolves on this card.

A hook with a cover endpoint does not also run unbounded travel. “Smoke to camp” belongs on the next cockpit.

## Action cards and embeds

Put the operational loop and default-mode compact numbers in the first section
that needs them. Hidden intent, opposition wants, and canon constraints are
ordinary DM-facing facts; write them inline where they change a ruling or
choice. Do not create a `DM truth` section.

Keep full `![[Name#Statblock]]` (optional `![[Name#At the table]]`, or `![[Name#Tactics]]` for monster notes) at the bottom. Do not retype an owner’s full Multiattack/HP table into prose above the embed. Do not embed the ecology essay. How the party already moves (flight, swim, mounts, boats) is not roster.

If the owner lacks `## Statblock`, add that heading above the fence on the owner (no math rewrite), then embed. If no owner exists for a creature you will roll, stop and packet `homebrew-monsters-5e`.

## Be ready for and the clock

A selective ruling table, not a catalog. Include only intents that change a ruling, risk, route, clock, resource, NPC response, or information. Omit ordinary or boring actions — unforeseen approaches are ruled from procedure, zones, and clock (intention / approach). The spoken Initial Narration shows the situation and ends on the question, then wait.

Clock ticks are pressure **actions**: what fills the clock, what happens, and
what completion changes. Visible geography the viewpoint already has does not
wait for tick 1. When the table has a Narration column, that cell is the spoken
update slot as `==_italic_==`; otherwise use `Tick {n}` callout stubs.

**Tells.** Any conclusion the table must be able to reach gets three independent visible tells in Initial Narration or Now (Three Clue Rule).
Tells are for actionable conclusions, not hidden teaser content. If a clue has
no clear success result, failure result, and player use, cut it.

**Exit narration.** Player-facing handoff into the next live card. Empty stub on pass 1 only when that card exists on this file. It does not ask what they do.

**Travel.** Omit on a 30-minute hook. When this slice *is* travel: one
complication, travel time in days, hours, or minutes, every number needed to
run it, and a failure endpoint. Wikilink further tables only as backup, not as
required procedure.

## Table gate

Completion — all of these hold, or the draft is not done:

- One named *procedure*; Be ready for failures do not also tick the clock. Be ready for is selective — no ordinary, boring, or redundant rows.
- Beat identity: the card filename's number matches its skeleton position; the card's purpose, dramatis personae, and hand-off match the skeleton.
- This beat's opening follows from the previous beat's How the Scene Resolves — no state reset, teleport, or unexplained jump between cards.
- The central element the table will ask about has an owner and appears on the card. Background detail may be marked unknown; the central element may not.
- No Partial lecture, 5e-default lecture, or writer note on the card.
- `dnd5e-mechanics` was loaded for every check, save, DC, grapple, shove, attack, damage, quality ladder, or player action mapped to a roll.
- Previous-session recap appears only on the first beat of the session. Every later beat starts from the immediate current situation.
- `## Scene ends when` is the first cockpit heading in Reading view (it may live inside a `col-md` fence); the end condition is the first line of that section.
- Time budget is present. Cut lines appear only when they change a pacing choice.
- If `## Now` is present, it states positions and speeds in feet; the zone table uses those distances.
- Spatial and travel measurements use north, south, east, west, feet for tactical 5.5e distance, and days, hours, or minutes for travel time; no range bands or abstract distance labels stand in for measurement.
- No `DM truth` section. Hidden intent, opposition wants, and canon constraints live inline where the DM uses them.
- No coy placeholders, mystery hedges, or "do not reveal this" notes in DM-facing text. Name the DM fact plainly or omit it.
- No naked checks. Every check says what success reveals or changes, what failure changes, and why the result matters now.
- Pass 1: `dnd5e-mechanics` loaded; `copy-writer` and `theatre-of-the-mind` not loaded. Empty callout stubs and empty Narration-column cells at the TotM slots this beat can actually use; no player-facing prose in those bodies. How the Scene Resolves is one unconditional stub plus an options table, not a stack of variant callouts. Each option hands off to a beat on the skeleton, not off-scene.
- Pass 2: `copy-writer` loaded after pass 1 completes; `theatre-of-the-mind` not loaded. DM-facing copy is usable, readable, useful, complete, and signal-only before spoken prose is filled. Every `[!narration]` body and Narration column cell is still empty.
- Pass 3: `theatre-of-the-mind` loaded after pass 2 completes. Initial Narration is the Layer 1 immediate frame — a stable shared picture and something live to respond to. Salient features and deeper facts are separate reveal blocks or zone/tick Narration cells (Layers 2–3). Every stub is filled. Every Narration cell that is spoken is `==_italic_==`.
- Pass 4: Reading view was checked top to bottom; no `[!narration]` body or Narration table cell that should be spoken is empty.
- Action cards sit near the procedure or ruling they support. Bloodied, cover-reached, and scene dials sit beside the Threat clock table when a Threat clock exists.
- Every consequence is a *ruling* (see Ruling).
- Optional sections stay absent unless this beat spends them at the table.
- Secondary objective, How the Scene Resolves, Roster, and Backup use `##` headings when present.
- Combat-mode owners are heading-embedded under Roster when the DM will roll them. Default-mode rolls have numbers on the action cards. Monster `![[Name#Statblock]]` rows never exceed two columns.
- Existing overview or identity image is embedded near the top when exact art exists. Omit if none exists.
- Battlemap art is embedded at the bottom when exact-scene art exists. Omit if none exists.
- Travel omitted, or one inlined complication with a failure endpoint.
- One cockpit: Glance once, no second Run-now, no separate Ask callout, no Scene menu, no peer Round script.
- The only `> [!` on the card is `[!narration]`. Do not use `[!col]` / `[!col-md]` on session cards. Conditional spoken in Narration table columns is `==_italic_==`, not a callout in the cell.
- Every pair in the column layout table is fenced in `col` / `col-md` when both sides exist; `flexGrow` ratios match the table. Spoken `[!narration]` callouts, Zones, Be ready for, How the Scene Resolves, Backup, and Battlemap stay full width.
- Every DM-facing line is signal-only: it changes placement, a roll, spoken words, risk, route, clock, resource, or NPC response.
- Every ruling, DC, and design choice on this card serves **fun** first. Change a DC, drop a constraint, or reshape a beat when the alternative is more fun — consistency, symmetry, and prior-beat precedent yield to fun.

## Whole-session branch

When rendering a **full** 3-5 hour night (not a single 30-minute beat), write
one lean card per live beat in likely-play order. Put overflow material after
the live cards as owner links or short bullets only when it will save table
hunting. Do not add a second card schema or prep-management menu.

## Handoffs

`session-beats` owns missing beat charts and *cut line* pacing. `encounter-prep`
owns reusable encounter stock that fits this cockpit. This skill owns pass 1
(mechanical card + empty stubs). `copy-writer` owns pass 2 DM copy.
`theatre-of-the-mind` owns pass 3 spoken fill (TUI copy-writer; Grok Bots Visualizer).
Pass 4 is the ready check. `visual-aids` assembles an already-listed
owner image onto the card. Monster math → `homebrew-monsters-5e`. Check, save,
DC, and player-interaction mechanics → `dnd5e-mechanics`. Do not invent canon,
copy owner essays, or write player decisions.

Finish with `./scripts/after-write "add run guide" -- path1 [path2…]`.

## Attribution

Cockpit order and sole-authority: Colville prep; Arcane Library (write for the DM).
*Procedure* / one adjudication cycle, *scene-setting*: Angry GM (Inviting PCs to Act; Art of Narration).
Intention/approach: Angry GM; Alexandrian *Art of Rulings*.
Information sequence / boxed completeness: Alexandrian *Art of the Key*.
Progress clocks and *cut lines*: Mike Shea / Sly Flourish (CC BY-NC) — Watch the Time; Harper clocks via Shea.
Action-oriented monsters: Colville via Sly Flourish (CC BY-NC).
Tells: Alexandrian Three Clue Rule. Zones: Runehammer. Strong start / silence: Lazy DM.
No WotC paste.
