# Shared DM-usability grammar

Authority: `wiki/AGENTS.md`, `.agents/skills/obsidian-markdown/SKILL.md` (+ `references/CALLOUTS.md`).
Scope: Obsidian Flavored Markdown templates under `wiki/templates/`. DM at-table scan first. One Markdown treatment = one meaning. Prefer fewer shared patterns over kind-specific quirks. Placeholders only — no invented lore.

## Common frontmatter core

Every campaign page carries at least:

| Field | Role |
|---|---|
| `title` | Display name |
| `category` | llm-wiki folder (`entities/`, `journal/`, …) |
| `tags` | Search / filter tags |
| `sources` | Evidence list |
| `created` | ISO date |
| `updated` | ISO date |
| `type` | Campaign kind (AGENTS enum — do not invent values) |
| `lifecycle` | `draft` \| `proposed` \| `accepted` \| `rejected` \| `canon` |
| `reveal` | `unrevealed` \| `revealed` |
| `campaign` | Campaign slug (e.g. `shattered-sea`) |
| `visibility` | Defaults `dm`; distinct from `reveal` |
| `summary` | One sentence a DM can read in a list |

Optional identity keys (`kind`, `region`, `owner`, rarity, etc.) only when the kind needs them. Omit unused keys.

```yaml
---
title: "{{title}}"
category: entities
tags: []
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: item
lifecycle: proposed
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: ""
---
```

## Shared section patterns

**Casing (accepted):** Title Case for shared headings — `At a Glance`, `At the Table`, `Connections`, `Secrets`, `Provenance`, `Art`.
Do not use sentence case (`At a glance`) or synonym titles (`Relationships`, `Related`, `Links`, `Ties`) when the job is Connections.

Use these **heading names** when the job is the same across kinds. Do not invent synonyms (`Related`, `Links`, `Ties`, `Relationships` as a section title when the job is Connections).

| Section | When to use | Notes |
|---|---|---|
| Leading `> [!narration]` | Owner pages with a spoken look / cold portrait | Title `Narration` (or the entity name). Player-safe TotM. Empty stub ok on pass 1. |
| `## At a Glance` | Compact orientation a DM can skim before the long body | One short block or table. What it is / why it matters / current pressure. |
| `## At the Table` | How to run it tonight — choices, notice, enables, warns | Owner pages. Not a second narration dump. |
| `## Connections` | Named wikilinked ties that change a ruling or route | Bullets or a small table. Omit when empty. |
| `## Secrets` | Unearned / hidden truth on owner pages | Prefer body heading + `[!secret]` where progressive disclosure helps. **Omit if empty.** |
| `## Provenance` | Where the facts came from / contested chains | Owner pages when history or ingest ambiguity matters. **Omit if empty.** |
| `## Art` | Extra embeds beyond a leading identity image | Filenames: `attachments/{slug}-{role}.ext` — see Attachment filenames. **Omit if empty.** |

Kind-specific job blocks (Sheet, Hazard bullets, Effect, Wiki facts, …) stay after narration / At a Glance and before Connections / Secrets / Provenance when those apply.

**Omit empty sections.** Pass is kind jobs in AGENTS Layout, not rigid heading-order match — but when a shared job appears, use the shared heading name.

## Callout grammar

| Surface | Allowed callouts |
|---|---|
| Session / run / beat / recap spoken | **Only** `[!narration]` |
| Owner pages (item, vehicle, place, npc, …) | `[!narration]` for spoken look; `[!mechanic]` / `[!secret]` for procedure and hidden truth |

- Live session surfaces: never collapsed `[!…]-`. Collapsed `[!secret]-` only on long-lived owner pages when progressive disclosure helps.
- Do **not** put callouts inside table cells.
- Do **not** proliferate new house callout types (`[!check]`, custom tip stacks, etc.) for jobs already covered by headings + at-table scan marks. Prefer plain headings + the scan table below.
- Session/run: procedure is a **heading**. The whole card is DM-facing — no `DM truth` section.

## At-table scan (one treatment = one meaning)

Cite: `.agents/skills/obsidian-markdown/SKILL.md` → **At-table scan**.

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

Check form: `**Wisdom (Perception) — \`DC 14\`**`. Never `**DC 15**` or `**DC 15** *Perception*`.


## Page filenames (wiki `.md`)

Owner and journal **page** files use a **space-free kebab slug** derived from `title` (FM `title` may keep human spaces). Strip legacy `Aruhe - ` on mint/rename. Recaps: `Session-<NN>-Recap.md`. Full rule: `wiki/AGENTS.md` § Page filenames (issue #80).

Attachment images remain kebab `{subject-slug}-{role}.ext` below — same family of space-free names, different role enum.

## Attachment filenames (images)

Flat by default: `wiki/attachments/{subject-slug}-{role}.{ext}`

| Role | Use |
|---|---|
| `banner` | Wiki/page hero; mood open; not Foundry |
| `portrait` | Face/bust; TotM + player-visible; not a token |
| `token` | Foundry piece only (circular crop); not TotM spoken art |
| `battlemap` | Tactical grid Foundry/combat; not TotM |
| `overview` | Establishing/wide; TotM “where you are” |
| `reference` | Props/details/still for TotM grounding |
| `handout` | Player-facing table asset (letter, sketch, clue); not battlemap/portrait |
| `teaser` | Cinematic scene still; player-shareable mood/hype; not battlemap, portrait, or diegetic handout |

- **TotM/spoken / player-shareable:** portrait, overview, reference, handout, teaser (± banner mood).
- Distinguish: `overview` = establishing/layout; `teaser` = cinematic scene still for share/hype; `handout` = diegetic table prop.
- **Foundry-only:** token, battlemap.
- kebab-case subject slug; one role suffix; no spaces.
- Embed: `![[attachments/{subject-slug}-{role}.ext]]` (optional `\|width` in tables).
- Deprecate nested `attachments/shattered-sea/{type}/` unless multi-campaign collision forces a campaign prefix.
- One file per subject+role; dedup parallel copies; update embeds on rename.
- `## Art` cites these roles; omit section when unused.


## DM-visible labels (no snake_case)

User-facing production wiki text must not use snake_case labels (e.g. table Field column `one_thing`, `primary_goal`). Prefer Title Case / spaced words: `One thing`, `Primary goal`.

- Applies to: body prose, markdown table labels, callout titles, section stubs meant for the DM at the table.
- Does **not** apply to: YAML frontmatter / machine keys (`quest_giver`, `hp_max`, `class_levels`, …), code fences, wikilink paths, attachment filenames.
- Scaffolds must never present snake_case as a copy-start Field label.

## Explicit non-goals

- Do **not** proliferate new callout types for the same job.
- Do **not** invent synonym headings for the same job across kinds.
- Do **not** invent lore in templates — placeholders (`{{title}}`) and instructional comments only.
- Session-11 cockpits vs beat scaffolds (T050 composition) is out of scope for this package.
