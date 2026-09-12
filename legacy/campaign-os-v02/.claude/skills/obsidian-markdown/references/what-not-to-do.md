# What NOT to Do

- Do not use markdown link syntax (square brackets plus a parenthesized target) for internal links — use `[[Note Name]]` instead
- Do not write inline HTML anywhere on a page (`<div>`, `<br>`, an `<!-- -->` comment) — standard Obsidian markdown and transclusion only: wikilinks, embeds, callouts, frontmatter properties, extended markdown
- Do not use HTML inside callouts — stick to Markdown
- Do not use `##` inside a callout body — headings don't render inside callouts
- Do not write `tags: [a, b, c]` inline in frontmatter — Obsidian prefers the list format
- Do not write ISO datetimes in frontmatter (`2026-04-08T00:00:00Z`) — use `2026-04-08`
- Do not write `[[Page|Alias]]` unescaped inside a table cell — the pipe splits the column; use `[[Page\|Alias]]`
