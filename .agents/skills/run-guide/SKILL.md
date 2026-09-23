---
name: run-guide
description: >-
  Assemble a table-ready, DM-only cockpit for one session or one 30-minute beat
  from existing prep and owner pages. Four passes, each loading only its skills:
  pass 1 (dnd5e-mechanics) writes the mechanical card plus empty [!narration]
  stubs; pass 2 (writing-for-humans) edits DM-facing copy; pass 3
  (theatre-of-the-mind) fills every spoken stub; pass 4 checks Reading view.
  Use for "run tonight", "build a run guide", or session-prep that is hard to
  scan. Not beat composition, canon invention, or session reconciliation.
---

# Run Guide

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Workflow — four passes

Each pass loads only its listed skills. The pass boundary is a skill-load
boundary — loading a later pass's skill early pulls attention away from the
current pass's job before it is done.

### Boundary contract

- **Input:** A named session or 30-minute beat cockpit, its existing prep and
  owner pages, the session plan's Beat Map and entry state, and the evidence
  needed to run this slice.
- **Work:** Preserve the four-pass contract: pass 1 keeps the mechanical card
  and empty narration stubs; pass 2 keeps DM-facing procedure; pass 3 keeps
  spoken-text craft; pass 4 keeps the Reading-view/table gate. Each pass stays
  within its named seam.
- **Done:** The existing pass completions hold: mechanical, DM-facing, and
  spoken returns are complete; every required narration slot is filled; and the
  pass-4 table gate holds in Reading view. Return the ready cockpit and those
  checks as downstream evidence.
- **Handoff:** Pass 1 → `writing-for-humans`, pass 2 → `theatre-of-the-mind`,
  pass 3 → pass-4 ready check. Missing owner page → blocker, not advance.

Each pass re-observes its own completion evidence before the next pass begins.
An unchanged incomplete pass takes a materially different sanctioned action or
returns a specific blocker naming the missing owner, path, section, evidence,
and parent session objective. Never advance a later pass from an assertion.

### Pre-pass: Ground and Diagnose

**Load:** `.agents/skills/qmd` plus
`specs/004-qmd-search-default/contracts/retrieval-precedence.md`.

1. **Ground.** Read `hot.md`, tonight's session prep, the latest log, the
   previous beat card when one exists, and only the linked owners needed to
   interpret this slice. Read each working file end-to-end before editing it;
   summaries, snippets, truncated output, and range reads may help target the
   file but are not grounding. The previous beat's How the Scene Resolves is
   this beat's entry state — the situation, position, and changed world the
   party walks in with. Verify beat identity: filename number matches its Beat
   Map row (`Session-<session>-<NN>-Label.md` = beat NN), purpose and
   dramatis personae match that row, hand-off targets the next row's
   beat. Mismatch → rename the file. Completion: beat identity confirmed;
   entry state known; every working file read end-to-end; every named actor,
   place, and item has an owner path or is marked unknown.

2. **Diagnose.** Mark each beat `ready`, `missing owner`, `missing prep`, or
   `proposal`. Run the cold read from `docs/agents/table-ready.md` on each
   source beat: an undefined consequence term, opposition without numbers or
   a tactics line, or an outcome with no world response is `missing prep` —
   define it in pass 1 from the owner that already states it, otherwise route
   the beat back to its type skill. Identify the central element — the
   Beat Map row and the beat page's purpose name it. That element and its
   dramatis personae have owners before the card is written; create via the
   appropriate craft skill (`npc-design`, `place-design`, `vehicle-design`).
   Missing chart → `session-beats`. Missing live beat of a type → that type
   skill (`hook-beats`, `development-beats`, `cliffhanger-beats`,
   `climax-beats`, `resolution-beats`). Missing mechanical stock → `encounter-prep`. Missing player-visible scene stock →
   owning page or craft skill before TotM fill. Empty `[!narration]` stubs are
   expected; TotM fill is pass 3. A creature you will roll that has no owner →
   `monster-design`. Choose live beats. Completion: the central element
   has an owner; every actionable hazard, loot, monster, route, clue, lore
   sign, and world detail has an owner or is marked unknown; no invented canon.

### Pass 1: Mechanical cockpit

**Load:** `dnd5e-mechanics`. Also `session-beats` when the chart is missing;
the matching type skill when a live beat of that type is missing;
`encounter-prep` when encounter stock is missing.

Read [`references/lean-surface.md`](references/lean-surface.md) for the field
catalog, column layout, and beat-type trimming. Read
[`references/cockpit-rules.md`](references/cockpit-rules.md) for ruling,
partial, procedure, and position conventions.

3. **Write mechanics.** Load `dnd5e-mechanics` before writing or auditing any
   player-interaction mechanics: checks, saves, DCs, Hide/Search/Study/
   Influence/Utilize resolution, grapples, shoves, attacks, damage, quality
   ladders, or player actions mapped to a roll. Completion: every player
   interaction is a 5.5e ruling with a consequence that changes play, or it
   stays ordinary fiction with no roll language.

4. **Write one cockpit per live beat** in play order. Keep only sections that
   this beat spends at the table. Place **empty titled `[!narration]` stubs**
   at the required TotM slots (see [TotM stubs](#totm-stubs) below). Embed an
   existing owner identity image (`![[attachments/…]]`) when the owner page
   already lists one. Action cards carry the opposition loop — opening move,
   adaptation when countered, break point, exit — beside the compact
   numbers. Completion: every mechanical field this slice uses is present;
   every consequence the card names is defined where it is named (who acts,
   trigger, numbers, duration, what the players perceive); unused sections
   are absent; clock and Be ready for are one *procedure*; every
   `[!narration]` body is empty; every Narration table column cell is empty.

### Pass 2: DM copy

**Load:** `writing-for-humans`.

This pass edits the DM-facing text that pass 1 wrote — Scene ends when,
Glance, Now, Procedure, Be ready for, clocks, action cards, How the Scene
Resolves — for usability, readability, and signal density. The `[!narration]`
stubs stay empty. `writing-for-humans` owns the prose quality bar; this skill
owns the cockpit structure. If a structural gap surfaces (missing section,
wrong field order), fix it before polishing copy.

5. **Edit DM copy.** Read the mechanical cockpit end-to-end, then edit every
   DM-facing heading and body for table usefulness. Apply the earn-it test:
   remove a line; if no choice, ruling, risk, resource, route, clock, NPC
   response, or spoken picture changes, cut it. Completion: Scene ends when,
   Glance, Now, Procedure, Be ready for, clocks, and How the Scene Resolves
   are complete sentences the DM can scan and use without inventing missing
   rulings. Every `[!narration]` body and Narration column cell is still empty.

### Pass 3: Spoken fill

**Load:** `theatre-of-the-mind` and follow its steps: `references/scenes.md`
for the slot recipes, `references/examples.md` for the quality bar,
`references/boundary.md` when a slot involves hidden truth or a handled
object, and `references/vision.md` with the related images opened before
drafting.

Read [`references/cockpit-rules.md`](references/cockpit-rules.md) § Scene-setting
for what the Initial Narration carries.

6. **Fill narration.** Fill `Initial Narration` first — the Layer 1 immediate
   frame: what is obvious without deliberate investigation, with features that
   matter now already in the fiction. Salient features and discoverable
   information are separate reveal blocks or zone/tick Narration cells. Then
   fill remaining stubs and Narration cells in reading order. Completion: every
   `[!narration]` body is filled; every Narration column cell is filled as
   `==_italic_==`; the Initial Narration gives the table a stable shared
   picture and something live to respond to without hidden truth, DCs,
   mechanics talk, or padded mood; no stub restages Initial Narration.

### Pass 4: Ready check

**Load:** nothing new. `obsidian-markdown` for filing.

Read [`references/table-gate.md`](references/table-gate.md) and check every
item against this card in Reading view.

7. **Table gate.** One downward pass. Completion: every item in
   `references/table-gate.md` holds.

8. **File.** `obsidian-markdown` (wikilinks, real newlines, at-table scan,
   codeblock columns). The only callout on the card is `[!narration]`. Layout
   uses `col` / `col-md` fences.

## TotM stubs

Pass 1 places the player-facing prose slots this beat can actually use. Pass 3
fills every placed slot. The DM may skip a block at the table; construction
places slots only for outcomes the beat can produce.

**Callout stubs** (empty titled `> [!narration]` blocks):
- `Initial Narration` — before the first player choice.
- `How the Scene Resolves` — one unconditional spoken state for what is always true when this beat ends.
- `{Creature}` — after each combat-mode roster embed. Situated look for this scene, not the owner-page cold portrait.
- `Exit` — only when the next cockpit is already on this file.

**Table Narration columns** (conditional spoken as `==_italic_==`, not a callout):
- Zones table — one cell per zone row.
- Threat clock table — one cell per tick row.
- How the Scene Resolves options table — one cell per likely option.

Callouts inside table cells are not rendered by Obsidian. Conditional spoken in
a cell is `==_italic_==` (`obsidian-markdown`).

## Whole-session branch

When rendering a **full** 3–5 hour night (not a single 30-minute beat), write
one lean card per live beat in likely-play order. Overflow material after the
live cards as owner links or short bullets only when it saves table hunting.

## Untyped cockpit assembly

When assembling from untyped or hard-to-scan prep (not a typed beat rewrite),
jobs are: identity; optional first-beat recap; overview art if it exists; Scene
ends when + At a Glance; Now; Action cards; Initial Narration; Procedure +
Secondary objective if a second question exists; Zones; Be ready for; Threat
clock + dials if a fuse exists; How the Scene Resolves; Roster if combat-mode
sheets will be rolled; Backup; Battlemap at bottom if art exists. Omit a job
only when it is absent.

At a Glance scans as stakes, goal or exit, danger, silence, situation magnets.
Scene ends when states the stop condition, a roughly thirty-minute budget, and
behind/ahead cuts when pacing is not obvious. Now states positions in feet and
compass directions where tactical distance matters. Action cards carry the
creature's or NPC's stat numbers (AC, HP, key attacks, saves) from their wiki
owner page — enough for the DM to run the encounter without opening another
note. How the Scene Resolves hands to a beat on this session's Beat Map with
an options table covering each resolution path's distinct world-state change.
Default-mode action-card numbers MAY sit on the beat; the beat stays a cockpit,
never a second full owner page.

## Handoffs

`session-beats` owns missing beat charts and *cut line* pacing. A missing live
beat of a type → that type skill. `encounter-prep` owns reusable encounter
stock. This skill owns pass 1 (mechanical card + empty stubs).
`writing-for-humans` owns pass 2 DM copy. `theatre-of-the-mind` owns pass 3
spoken fill. Pass 4 is the ready check. `visual-aids` assembles an
already-listed owner image onto the card. Monster math →
`monster-design`. Check, save, DC, and player-interaction mechanics →
`dnd5e-mechanics`.

## Attribution

Cockpit order and sole-authority: Colville prep; Arcane Library (write for the DM).
*Procedure* / one adjudication cycle, *scene-setting*: Angry GM (Inviting PCs to Act; Art of Narration).
Intention/approach: Angry GM; Alexandrian *Art of Rulings*.
Information sequence / boxed completeness: Alexandrian *Art of the Key*.
Progress clocks and *cut lines*: Mike Shea / Sly Flourish (CC BY-NC) — Watch the Time; Harper clocks via Shea.
Action-oriented monsters: Colville via Sly Flourish (CC BY-NC).
Tells: Alexandrian Three Clue Rule. Zones: Runehammer. Strong start / silence: Lazy DM.
