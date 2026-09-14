# Quickstart: PC Page Redesign

## Prerequisites

Run from the repository root after implementation has landed the `player-characters` skill, the redesigned template, and the five live owners. The canonical page contract is [`contracts/pc-page.md`](contracts/pc-page.md). The five owners are under `wiki/entities/pc/`.

## 1. Run the feature fixture

```bash
.venv/bin/python specs/020-pc-page-redesign/fixtures/check.py
```

Expected result: exit `0`; the report confirms the template and five pages have the required frontmatter, D&D Beyond spine (`Identity`, `Combat Stats`, `Ability Scores`, `Skills`, `Actions`, …), no `Voice` / `At a Glance` / `Sheet` / `Combat Profile` / `Abilities`, fenced column pairs for Identity+Combat Stats and Ability Scores+Skills, omission behavior, preserved source/link metadata, and no live satellite duplicate.

## 2. Run scoped Markdown checks

```bash
./scripts/lint-wiki-write --path wiki/entities/pc
./scripts/lint-obsidian-markdown --strict --path wiki/entities/pc
```

Expected result: both commands exit `0`. This proves current link syntax, narration safety, escaped table-cell pipes, image targets, required type fields, and real body newlines. The lint does not prove visual column rendering.

## 3. Run owner-schema wiki lint

```bash
./scripts/wiki-lint --json
```

Expected result: no HARD findings for broken links, missing/invalid frontmatter, PC identity/path mismatch, or filename violations.

## 4. Confirm skill routing

Open `.agents/skills/player-characters/SKILL.md` and the wiki-kind routing in `wiki/AGENTS.md`. Confirm:

- `player-characters` is the sole skill owner for `type: pc`.
- `npc-design` has no PC-page path and tells agents to use `player-characters` instead.
- The skill records from supplied source only (PDF, prose, Foundry MCP, other DM files) and refuses inventing a PC, generating stats, or writing the player's actions.

## 5. Review the rendered surface

Open each of the five pages in Obsidian Reading view. Confirm:

- The narration callout is full width and player-safe.
- `Identity`/`Combat Stats` and `Ability Scores`/`Skills` render as paired scan surfaces.
- Headings and tables remain understandable when columns are unavailable.
- No page has `## Voice`, `## At a Glance`, `## Sheet`, `## Combat Profile`, `## Abilities`, an empty optional heading, a second H1, a required DM thesis, or a competing live satellite dump.
- A DM can locate player, class/level, AC, current/max HP, initiative, signature options, a named connection, and a decision-relevant pressure in under 60 seconds per page.

## 6. Preserve facts (structure-only)

Compare each conformed page with its pre-change copy and all named archive satellites. Confirm every prior fact is inline in its canonical section, represented by an owner link, or marked `[verify]` with its source — unless a later ingest from a newer supplied source overwrote a number under FR-020. Confirm source entries, aliases, art, lifecycle, reveal, visibility, and player handles are unchanged by structure-only work. Do not use `tools/check_wiki_pages.py` as PC proof; its type allowlist omits `pc`.

## Representative recording checks

Using only `player-characters`, the template, this contract, governing wiki instructions, and representative **supplied** source evidence, produce temporary scratch outputs for:

- a caster with multiple casting pools;
- a non-caster with no `Spells` section;
- a multiclass PC with distinct class/resource pools.

Each output must use the same frontmatter and heading contract, omit empty sections, preserve unknowns without invented values, keep narration safe, and pass the scoped lint checks before scratch files are removed.

Also confirm a negative: with no supplied source, or with a request to invent a PC / generate stats / write the character's actions, the skill refuses and does not mint a page.
