---
name: obsidian-markdown
description: >-
  Format every campaign wiki `.md` with Obsidian Flavored Markdown (wikilinks,
  embeds, callouts, properties) and the at-table scan grammar (one Markdown
  treatment = one meaning; checks/saves as **Ability (Skill) — `DC n`**;
  `DC n` and dice in inline code). Vault `true` → obsidian-markdown. Format
  for wiki vault notes only. Not required for writing that is not a wiki
  vault note. Skill files and repository docs are not wiki vault notes.
---

# Obsidian markdown

Vault: `$OBSIDIAN_VAULT_PATH` (this repo's `wiki/`). Schema: `wiki/AGENTS.md`.
Load this `SKILL.md` before every vault `.md` write; open `references/` only when stuck.
Every wiki write must preserve vault wikilinks, `[!narration]` for spoken text, and
`wiki/AGENTS.md` properties (`type`, `lifecycle`, `reveal`, `campaign`, `visibility` plus llm-wiki required fields).

## Hard rules

- **Wikilinks in-vault:** `[[Note]]` / `[[Note|text]]` / `[[Note#Heading]]`. Markdown links only for external `https://` URLs. In a Markdown table cell, write the alias or size pipe as `\|` so the cell stays one cell: `[[Note\|text]]`, `![[image.png\|400]]`. Bare `[[Note]]` needs no escape.
- **Frontmatter (`wiki/AGENTS.md`):** include `title`, `category`, `tags`, `sources`, `created`, `updated`, plus campaign `type`, `lifecycle`, `reveal`, `campaign`, and `visibility`. `type` enum: `npc` | `pc` | `place` | `faction` | `item` | `creature` | `session` | `recap` | `work`. `lifecycle`: `draft` | `proposed` | `accepted` | `rejected` | `canon`. `reveal`: `unrevealed` | `revealed`. `visibility` defaults to `dm` and is distinct from `reveal`. Prefer those fields over generic `title`-only notes.

- **`summary` frontmatter:** one sentence — what the note is and anything non-obvious or unexpected. Use it to assess a note without reading the full file. Create on every new note; update whenever the note changes. Keep it concise, specific, and direct. Quote the value when it contains `: ` (colon-space) — unquoted `: ` breaks YAML.
- **Player prose:** owner pages use leading `> [!narration] Narration` (empty until TotM fill). Session/run beats use mandatory `> [!narration] Initial Narration` plus titled stubs per `run-guide` TotM slots. Unconditional spoken stays in `[!narration]`. Conditional spoken lives in a table cell as `==_italic_==`. Empty on mechanical pass 1; fill on pass 2. No secrets/DCs/unearned names inside `[!narration]` or those highlighted cells.
- **Live session surfaces:** In run-guide, session-prep, session, and beat notes, never use collapsed callouts (`[!…]-`); keep DM information open so session cards do not hide it. Collapsed secrets remain allowed on long-lived owner pages (NPC/PC/faction) when useful.
- **Real body newlines:** Prose, lists, and callout bodies must use real line breaks, never a literal backslash followed by `n`. This is especially strict for run-guide, session-prep, session, and beat notes. The only exemptions are YAML frontmatter and fenced code/statblocks (including YAML string values inside a statblock fence); outside those regions, a literal `\n` is a FAIL.
- **Complete sentences on live surfaces:** Every DM-facing line on a run guide, session prep, or beat card must be a **complete grammatical sentence** (or a short list of complete sentences). Telegram shorthand, letter-code-only clauses, and slash-stacks that need a decoder are presentation fails. Wikilinks, bold field labels, compact tables, and the **at-table check/save grammar** below are allowed when cells remain readable sentences or clear subject-bearing fragments.
- **Owner-page section jobs (signal):** Do not triple-tell the same fact across body / At a Glance / Provenance / Secrets / Connections. At the Table is playable consequence only — not design diary or balance commentary. No agent-process asides on DM owner pages. Vehicle/item numbers live in one headed home.
- **Signal-only lines:** Every wiki line must earn table attention by changing a choice, ruling, risk, resource, route, clock, NPC response, or words to speak. Cut default, normal, and no-effect statements; mention safety, permission, ordinary water, weather, or light only when that fact changes play. Campaign and session notes state what to run, say, or know; agent-process bans stay in skills, AGENTS, and templates-for-agents.
- **At-table scan:** each Markdown treatment has exactly one meaning (table under Syntax). `DC 15` is inline code. Private DM notes are headings on session/run surfaces, and `[!secret]` / `[!mechanic]` on owner pages.
- **Creatures:** Fantasy Statblocks fence (```` ```statblock ````) immediately after frontmatter, or after a single `## Statblock` heading so run cards can `![[Name#Statblock]]`. See `wiki/templates/creature.md`. Never a prose AC/HP table instead of the fence. No WotC book paste. The fence keeps 5e YAML phrasing (`DC 15 Constitution saving throw`); at-table scan is for wiki body, not the fence. Column density is allowed. Pass is creature jobs in `wiki/AGENTS.md` Layout, not heading-order match.
- **Run-card roster:** embed the owner heading (`![[Bloodhawk#Statblock]]`) at the bottom. Put default-mode compact numbers on the action cards (`run-guide`). Do not retype the owner's full Multiattack/HP table into the card body. Do not embed the whole monster essay.
- **Paths:** scratch → `inbox/`; **images/media** under `attachments/` as `{subject-slug}-{role}` (`wiki/attachments/README.md`). Prefer flat; nested campaign folders only on collision. Embed with `![[attachments/…]]`; wikilink with `[[attachments/…]]`. See [[attachments/00 Attachments]] + [references/EMBEDS.md](references/EMBEDS.md). No parallel `wiki/` · `concepts/` · `sources/` tree.
- **Surgical edits only:** Edit the elements in scope for the current pass. Preserve existing image embeds, wikilink paths, frontmatter fields, and structure unless that exact element is broken and verified broken. A copy pass edits copy; it does not rewrite embeds or paths.
- **Lint:** Run `./scripts/lint-wiki-write` (obsidian-markdown plus literal-newlines on session/beat bodies). The literal-newline check skips YAML frontmatter and fenced code/statblocks.

## Write workflow

1. Copy matching `wiki/templates/` note as a scaffold when creating. Omit empty sections.
2. Fill frontmatter (`type`, `lifecycle`, `reveal`, `campaign`, `visibility` + llm-wiki fields + `summary`). On file, `type` is `creature` not `monster`.
3. If `type: creature` → optional `## Statblock`, then the `statblock` fence.
4. Leading `[!narration]` when the template expects it.
5. Body: one topic/note; facts to run, say, or know; wikilink nearest index/MOC/`hot` as needed. Drop `## Do not` and other author-process bans.
6. On session/run beats, procedure is a heading; the only callout is `[!narration]`. Do not add a `DM truth` section — the whole card is DM-facing. Layout uses `col` / `col-md` codeblock fences, not `[!col]`. Do not put callouts inside table cells. Conditional spoken in a cell is `==_italic_==`. On owner pages, DM procedure / hidden truth → `[!mechanic]` or `[!secret]`. Use collapsed `[!secret]-` only on long-lived owner pages such as NPC/PC/faction pages.
7. In prose, lists, and callout bodies, type each line break as a real newline; do not serialize it as a backslash-`n` sequence.

## Syntax (day-to-day)

### Wikilinks

```markdown
[[Note Name]]
[[Note Name|Display]]
[[Note Name#Heading]]
[[Note Name#^block-id]]
[[#Heading in same note]]
```

A Markdown table treats `|` as a new column. In a table cell, escape the alias or image-size pipe so the wikilink stays inside one cell:

```markdown
| Place | Cover |
| --- | --- |
| [[Aruhe - Old Gardens\|Terrace woods]] | Messy landing cover. |
| ![[session-11-01-angry-birds-overview.jpg\|400]] | Width in a cell. |
```

Bare `[[Note]]` in a cell needs no escape. Prose outside tables keeps `[[Note|Display]]`.

Block id on a paragraph: `text ^block-id`. For lists/quotes, put `^id` on its own line after the block.

### Images & embeds

```markdown
![[attachments/shattered-sea/map.png]]              Embed image
![[attachments/shattered-sea/map.png|400]]          Embed + width
[[attachments/shattered-sea/map.png]]               Wikilink to asset
[[attachments/shattered-sea/map.png|Campaign map]]
![[Note Name]]
![[Note Name#Heading]]
![[Bloodhawk#Statblock]]                            Run-card combat (tight heading)
![[Item#Charges / limits]]                          Run-card item limits, only if this slice spends them
```

More: [references/EMBEDS.md](references/EMBEDS.md) · hub [[attachments/00 Attachments]].

### Callouts

```markdown
> [!narration] Initial Narration
> Session/run scene-setting (or leave empty on pass 1).

> [!narration] Narration
> Owner-page player-facing prose (or leave empty).
```

Session/run: only `[!narration]`. Owner pages may still use `[!mechanic]` and `[!secret]` — [references/CALLOUTS.md](references/CALLOUTS.md).

Other types (`note`, `tip`, `warning`, …): [references/CALLOUTS.md](references/CALLOUTS.md).

### At-table scan

One treatment, one meaning. **Bold** always means look here / mechanical noun — triggers, applied states, and named checks share that meaning.

| Content | Syntax | Example |
|---|---|---|
| DM instructions / information | Plain text | The bridge collapses when two creatures cross. |
| Important trigger / state | **Bold** | **Trigger:** A creature touches the idol. |
| Game term / creature / item emphasis | *Italics* | *poisoned*, *Giant Eagle* |
| Skill / check / save | **Bold** | **Wisdom (Perception)** |
| DC | `inline code` | `DC 15` |
| Damage / mechanical numbers | `inline code` | `2d6 + 3` fire damage |
| Result / consequence | → arrow | → Spots the concealed tunnel. |
| Unconditional spoken | Narration callout | `> [!narration]` |
| Conditional spoken in a table cell | Highlighted italic | `==_The grass closes over you._==` |

**Bold** = look here / mechanical noun. `` `code` `` = the number you need. Plain text = what happens. → = what a mechanic produces. `[!narration]` = words always spoken on this slot. `==_italic_==` in a table cell = words spoken only if that row is live.

Check, save, and DC choice still come from `dnd5e-mechanics`. This section is the mark.

Checks:

```markdown
**Wisdom (Perception) — `DC 14`**
- Success → Notices claw marks beneath the window.
- Failure → Nothing appears disturbed.
```

Saves:

```markdown
**Dexterity save — `DC 15`**
- Success → Half damage.
- Failure → `3d6` fire damage and falls **prone**.
```

Obvious consequence, one line:

```markdown
**Strength (Athletics) — `DC 13`** → Climb the wet wall.
```

Several approaches:

```markdown
- **Wisdom (Survival) — `DC 13`** → Follow the tracks.
- **Intelligence (Nature) — `DC 15`** → Identify the creature.
- **Wisdom (Perception) — `DC 17`** → Notice it watching from the canopy.
```

Quality ladder (one attempt, stacked rungs; `dnd5e-mechanics`):

```markdown
**Wisdom (Survival) — harvest the grove**
- `DC 10` → Fallen ordinary take; no contest.
- `DC 15` → Ripe useful specimen; some noise.
- `DC 20` → Prize grade.
- Failure → Local fauna close in, or the living source is claimed.
```

Narration stays visually isolated. Mechanics sit in the DM layer after it:

```markdown
> [!narration]
> The grass parts ahead of you. Something enormous moves through it without making a sound.

**Wisdom (Perception) — `DC 14`**
- Success → They see the feathers before the creature emerges.

**Trigger:** Someone enters the grass.

The creature attacks from concealment.
```

On a `run-guide` Be ready for table, the same treatments apply inside cells: approach is **Ability (Skill)**; DC column is `` `DC 14` ``; dice and damage are inline code; applied conditions are **bold**. The columns already split success / partial / failure, so those cells do not also need →. Zones, Threat clock, and How the Scene Resolves Narration cells are spoken variants: wrap the italic sentence in `==_…_==`. Ruling cells stay plain.

### Properties

```yaml
---
title: Example NPC
category: entities
type: npc
lifecycle: proposed
reveal: unrevealed
campaign: shattered-sea
visibility: dm
tags: [npc]
sources: []
summary: Harbor clerk who sells tide tables and owes the dock syndicate.
created: 2026-09-11
updated: 2026-09-11
---
```

Types and tags: [references/PROPERTIES.md](references/PROPERTIES.md).

### Columns (obsidian-columns plugin)

On session/run surfaces, use **codeblock** `col` / `col-md` fences so `[!narration]` stays a real callout. Do not wrap a session card in `[!col]` callouts.

Pair same-moment DM jobs. Leave spoken callouts and wide ruling tables full width.

`````markdown
````col
```col-md
## Scene ends when

End condition, time budget, cut lines.
```

```col-md
flexGrow=2
===
## At a Glance

- **Stakes:**
- **Goal / exit:**
```
````

> [!narration] Initial Narration
> Spoken scene-setting stays full width, outside the fence.
`````

Parent fences need more backticks than children. `flexGrow` sets relative width. Headings may sit inside `col-md` so the title stays with its body in Reading view. Monster roster rows are two `![[Name#Statblock]]` columns max; extra monsters wrap to the next row. Other cockpit pairs are unaffected.

Owner pages may still use callout `[!col]` when no `[!narration]` sits in the same row. Full pairing catalog: [references/COLUMNS.md](references/COLUMNS.md).
PC owner pages: `player-characters` and `wiki/templates/pc.md`. Pair featured portrait with Identity when art exists; Combat Stats stays full-width. Pair Ability Scores with Skills.


### Also supported (use when needed)

`%%comment%%` · `$math$` / `$$` · ` ```mermaid ` · footnotes `[^1]`

## Anti-patterns

| Fail | Do instead |
|---|---|
| `[text](Campaign Note.md)` for vault notes | `[[Campaign Note]]` |
| Wikilink alias or image-size pipe left raw in a table cell | `[[Note\|text]]` / `![[image.png\|400]]` |
| Frontmatter with only `title`/`date` | AGENTS `type` + campaign fields |
| Prose monster stats / fence not first | `## Statblock` then `statblock` fence, or fence first |
| Owner's full Multiattack/HP table retyped above the embed | `![[Monster#Statblock]]` at the bottom plus action-card compact numbers (`run-guide`) |
| Secrets inside `[!narration]` | Session/run: a heading. Owner pages: `[!secret]` / `[!secret]-` |
| `**DC 15**` or `**DC 15** *Perception*` | `**Wisdom (Perception) — \`DC 15\`**` |
| `==highlight==` for a private DM note | Session/run: a heading. Owner page: `[!secret]` / `[!mechanic]`. Session/run table cells use `==_spoken_==` only for conditional player-facing prose |
| Stacked variant `[!narration]` blocks for if/then outcomes | One unconditional `[!narration]`; likely options in a table with `==_text_==` (`run-guide`) |
| `## Do not` / author-process bans on campaign pages | Facts to run, say, or know; unresolved as unknowns or table limits |
| New `campaigns/` trees | `wiki/` categories + `wiki/AGENTS.md` `type` |
| WotC book paste | paraphrase / house / SRD link in `source` |
| `![](…)` / absolute disk paths for vault art | `![[attachments/…]]` / `[[attachments/…]]` |
| Broken image wikilink | fix path or add file under `attachments/` |
| `[!col]` / `[!col-md]` on a session/run card | `col` / `col-md` codeblock fences so `[!narration]` stays a callout |
| `[!col]` for PC featured-portrait+Identity or Ability Scores+Skills | nested `col`/`col-md` codeblock fences; Combat Stats full-width; parent longer than children; narration stays outside fences |

