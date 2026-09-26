# Lean Surface

Field catalog, column layout, beat-type trimming, and scene stock for the
run-guide cockpit. Read during pass 1 when building the mechanical card.

## Filing

Frontmatter: `type: session-prep` (or `encounter`), `visibility: dm`.

Typed live beat: keep that type's draft jobs from
`wiki/templates/{hook,development,cliffhanger,climax,resolution}.md`. Session
plan: `wiki/templates/session-plan.md`. `wiki/templates/session-prep.md` is
not copy-start for new beats or plans.

Filename: `Session-<number>-<beat-number>-<Label>.md` with two-digit beat
numbers (`01`, `02`, …). File after accept to
`wiki/journal/sessions/<campaign-slug>/<session-number>/`.

## Field catalog

Each field earns its place only when this beat spends it at the table.

| Field | Keep when | Shape |
|---|---|---|
| **At a Glance** | Every live beat. | `## At a Glance`. First bullet **Ends when**: end condition, then time budget; **If behind:** and **If ahead:** only when the pacing choice is non-obvious. Then stakes, objective, danger, magnets, next. Recap only on the session's first beat. |
| **Overview image** | An exact overview or identity image exists. | Embed near the top, before runnable sections. |
| **Situation** | Positions, distances, speeds, or starting state would clutter Glance. | One paragraph. Who starts where, in **feet** when tactical distance matters. North/south/east/west for orientation. Speeds that matter. What a move vs Dash reaches. |
| **Actors** | The DM will roll compact default-mode numbers or follow an opposition loop. | `## Actors` when paired beside Situation. Operational loop, compact numbers: AC, HP when needed, one attack, thresholds, grab, scatter, or bloodied rule. Use owner action names. |
| **Opening** | Every live beat. | Empty `> [!narration] Opening` stub on pass 1. Pass 3 fills the Layer 1 immediate frame. Embed `![[attachments/…]]` near this block when the owner already has an identity image. |
| **Procedure** | A named mode, fuse, clock trigger, combat switch, pursuit rule, or repeated resolution loop. | `## Procedure`. Name the mode and this slice's trigger once. |
| **Stage** | Routes, cover, distance, search areas, or scene stock matter. | Table: place \| distance in feet \| cover \| narration. Same distances and compass as Now. Each row names decision-useful scene stock. **Narration** column: conditional spoken as `_italic_`. When the column is absent, one empty `> [!narration] {Place}` stub per row after the table. |
| **Checks** | Players are likely to attempt consequential actions. | Selective ruling table — only intents that change a ruling, risk, route, clock, resource, NPC response, or information. Table: intent \| approach \| DC \| success \| partial \| failure. Approach is **Ability (Skill)** when a check applies. DC column: `` `DC 14` ``. Dice and damage: inline code. Applied conditions: **bold**. Name creature, item, place in every cell. Every cell is a *ruling*. Include **Assess the situation** only when success and failure both say what changes. |
| **Pressure** | A fuse or opposition turn changes the situation. | `## Pressure`. Table: tick \| what happens \| narration. Named ticks. 3–4 ticks. Each tick states what newly becomes visible, usable, threatened, blocked, or changed. **Narration** column: `_italic_`. When absent, `> [!narration] Tick {n}` stubs after the table. Bloodied, cover-reached, and scene dials sit in the right `col-md` beside the clock table. |
| **Secondary objective** | A second question runs in parallel and changes outcome or later consequence. | `## Secondary Objective`. One paragraph: beats required, ignore outcome, later consequence. |
| **Outcomes** | Every live beat. | `## Outcomes`. Most likely options, usually one or two. Each option hands off to a beat on this session's Beat Map. Next state, damage applied, relevant conditions, what follows. One empty `> [!narration] Outcomes` for the unconditional spoken state, plus an options table (`If` \| `Next` \| `Narration`). Narration cells: `_spoken_`. |
| **Exit narration** | The next cockpit is already on this file. | Empty `> [!narration] Exit` on pass 1. Spoken transition on pass 3. |
| **Roster** | The DM will roll a creature or item. | `## Roster`. `![[Monster#Statblock]]` for opposition in combat mode. At most two columns per row; a third monster starts a new row or sits full width. After each embed: empty `> [!narration] {Creature}`, titled with the creature's name. Item embeds only if this slice spends charges or the item is the pressure. |
| **Backup** | Extra owner links save table hunting. | `## Backup`. Extra wikilinks only. |
| **Previous-session recap** | Only the first beat of the session. | Brief, player-facing. |
| **Battlemap** | Exact-scene battlemap art exists. | `## Battlemap` at the bottom. Embed from `attachments/`. Compass: top north, right east, bottom south, left west. |

## Column layout

Session cards use obsidian-columns **codeblock** syntax (`col` / `col-md`).
Syntax reference: `obsidian-markdown`
[references/columns.md](../obsidian-markdown/references/columns.md). Each row
appears only when both sides exist.

| Row | Left | Right | flexGrow |
|---|---|---|---|
| Overview art | First overview/identity image | Second image | equal |
| Situation | `## Situation` | `## Actors` | Actors `flexGrow=2` |
| Mode | `## Procedure` | `## Secondary Objective` | Procedure `flexGrow=3` |
| Pressure | `## Pressure` table | Bloodied / cover / dials | Pressure `flexGrow=3` |
| Roster | Monster `![[Name#Statblock]]` (two columns max) | Second monster, or omit | equal |

**Full width:** `[!narration]` callouts, Stage table, Checks table,
Outcomes body + options, Backup, Battlemap.

## Beat type trimming

Beat type changes which fields earn space.

**Resolution:** aftermath state, Opening, Outcomes,
actionable Stage or Checks rows. Cut combat sections when opposition is
resolved.

**Development:** information pressure — what can be learned, who wants what,
consequential approaches. Procedure or Pressure only when there is a named
mode or external fuse. Cut combat-only sections.

**Hook:** immediate pressure, first response paths, Outcomes.
Combat sections only when the hook is itself a combat encounter. A hook with a
cover endpoint stays on this beat; the next stretch is the next cockpit.

**Cliffhanger:** threat up front — Actors for every opposing side,
Stage with terrain rulings, a Pressure ticking by round or named trigger,
and Outcomes rows for won, lost, and broken-off outcomes.

**Climax:** every combatant on Actors; phase triggers as Pressure
ticks; each harvested thread's lever written inline where it changes a ruling
(the Checks row, the actor entry, the zone); Outcomes
rows carry each thread's final state for the Resolution.

**Travel:** use run-guide only when travel is the live slice. Inline one
specific complication, travel time in days/hours/minutes, every number needed
to run it, and a failure endpoint.

## Scene stock

Before pass 3, the card answers follow-up questions without opening the vault
cold. Record actionable player-visible stock wherever the leanest surface holds
it: a paragraph, table row, clock tick, how the scene resolves, or backup link.

Completion: every stock item in the spoken first look has an access channel, an
owner or local ruling, and a player use. Required first-look details live on
the card, not only in Backup links.

Distinct things need distinct text and media. Existing narration, art, tokens,
and battlemaps are valid only for the exact same owner/site/moment.
