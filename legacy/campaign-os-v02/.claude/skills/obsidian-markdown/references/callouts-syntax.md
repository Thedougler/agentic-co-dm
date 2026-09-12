# Callouts

Callouts are blockquotes with a type keyword. They render as styled alert boxes.

```markdown
> [!note]
> Default informational callout.

> [!note] Custom Title
> Callout with a custom title.

> [!note]- Collapsible (closed by default)
> Click to expand.

> [!note]+ Collapsible (open by default)
> Click to collapse.

> [!note] Multi-paragraph
> First paragraph.
>
> A lone `>` line keeps the next paragraph inside the same callout.
```

A fully blank line (no `>`) ends the callout — the next `>` line starts a new block.

## Which type to use

This file owns callout *syntax* only. Which type is legal on which page, each type's prose
contract, and its CSS live in the `callouts` skill (`.claude/skills/callouts`) — consult it
before writing any `> [!` in this repo.
