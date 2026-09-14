# Quickstart: PC Page Redesign

## Prerequisites

Run from the repository root after implementation has conformed the template and five live owners. The canonical page contract is [`contracts/pc-page.md`](contracts/pc-page.md). The five owners are under `wiki/entities/pc/`.

## 1. Run the feature fixture

```bash
.venv/bin/python specs/020-pc-page-redesign/fixtures/check.py
```

Expected result: exit `0`; the report confirms the template and five pages have the required frontmatter/spine, no `Voice` section, fenced column pairs, omission behavior, preserved source/link metadata, and no live satellite duplicate.

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

## 4. Review the rendered surface

Open each of the five pages in Obsidian Reading view. Confirm:

- The narration callout is full width and player-safe.
- `At a Glance`/`Connections` and `Sheet`/`Combat Profile` render as paired scan surfaces.
- Headings and tables remain understandable when columns are unavailable.
- No page has `## Voice`, an empty optional heading, a second H1, or a competing live satellite dump.
- A DM can locate player, class/level, AC, current/max HP, initiative, signature options, a named connection, and a decision-relevant pressure in under 60 seconds per page.

## 5. Preserve facts

Compare each conformed page with its pre-change copy and all named archive satellites. Confirm every prior fact is inline in its canonical section, represented by an owner link, or marked `[verify]` with its source. Confirm source entries, aliases, art, lifecycle, reveal, visibility, and player handles are unchanged. Do not use `tools/check_wiki_pages.py` as PC proof; its type allowlist omits `pc`.

## Representative authoring checks

Using only the template, this contract, governing wiki instructions, and representative source evidence, create temporary in-memory or scratch outputs for:

- a caster with multiple casting pools;
- a non-caster with no `Spells` section;
- a multiclass PC with distinct class/resource pools.

Each output must use the same frontmatter and heading contract, omit empty sections, preserve unknowns without invented values, keep narration safe, and pass the scoped lint checks before scratch files are removed.
