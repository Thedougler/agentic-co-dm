---
name: obsidian-markdown
description: >
  Obsidian Flavored Markdown syntax for a Campaign OS repo (vault/ present).
  Use when writing or editing any wiki page's wikilinks, embeds, frontmatter properties, tags,
  highlights, math, Mermaid diagrams, or footnotes. Not for which callout type to pick (callouts
  owns that) and not for Bases/Metabind/Canvas/Leaflet plugin syntax (their own skills own those).
---

# Obsidian Flavored Markdown

Reference this skill when writing any wiki page. Obsidian extends standard Markdown
with wikilinks, embeds, callouts, and properties. Getting syntax wrong causes broken
links, invisible callouts, or malformed frontmatter.

## What you're writing

| You need to... | Use | Detail |
|---|---|---|
| Link to another page | Wikilink `[[Note Name]]` | `references/wikilinks-embeds.md` |
| Show another page/section/image/canvas/PDF inline | Embed `![[...]]` | `references/wikilinks-embeds.md` |
| Flag an alert box (note/warning/DM secret/etc.) | Callout `> [!type]` | `references/callouts-syntax.md`, then the `callouts` skill for which type |
| Set YAML frontmatter or tag a page | Properties / tags | `references/frontmatter-tags.md` |
| Bold/italic/highlight/inline code, math, a Mermaid diagram, or a footnote | Standard extended Markdown | `references/formatting-math-mermaid-footnotes.md` |
| Avoid a known syntax mistake | — | `references/what-not-to-do.md` |
| Keep an overview/aggregation page DRY | Base embed / section embed / wikilink / static text | `references/dry-content-patterns.md` |

Decision order: prefer a wikilink or embed over restating content; use a callout only
for the types the `callouts` skill authorizes; never hand-write a roster or status
table that a `.base` embed could generate live.

## Reference files

| File | Covers |
|---|---|
| `references/wikilinks-embeds.md` | Wikilink and embed syntax, disambiguation rules |
| `references/callouts-syntax.md` | Callout block syntax and collapsible variants |
| `references/frontmatter-tags.md` | YAML frontmatter rules, tag syntax |
| `references/formatting-math-mermaid-footnotes.md` | Bold/italic/highlight, math, Mermaid, footnotes |
| `references/what-not-to-do.md` | Common syntax mistakes to avoid |
| `references/dry-content-patterns.md` | Base embed vs section embed vs wikilink vs static text, anti-patterns |
