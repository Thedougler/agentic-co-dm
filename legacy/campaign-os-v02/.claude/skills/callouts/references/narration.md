# `[!narration]` — a spoken picture on its own page

**Role:** the container on a `type: narration` sibling. The file is the
picture; this callout titles it and paints it as performed text.

## Use when

- Wrapping the body of a `type: narration` sibling (`-narration-open`,
  `-narration-condition`, `-narration-appearance`, recap).

## Never for → use instead

- A leftover box on a mechanical parent → extract to a sibling, then wrap
  that sibling. Do not leave `[!narration]` on a moment, Situation, or
  entity page.
- Spoken lines only → `[!dialogue]` on a `type: dialogue` sibling.
- A leftover beat that still ships boxed text inline → `[!read-aloud]`.

## Prose contract

- **No custom title.** Bare `[!narration]` so Obsidian shows the standard
  type name. The parent embed has no wrapping heading.
- Body stays the sibling's italic picture. No H1. No second callout.
- Picture craft is `.claude/skills/writing-player-prose`, not this file.

## Example

```markdown
> [!narration]
> *Face-down in six inches of water. Sand in the teeth.*
```

## CSS

```css
.callout[data-callout="narration"] {
  --callout-color: 201, 162, 74;
  --callout-icon: lucide-book-open;
  background-color: rgba(201, 162, 74, 0.08);
  border-left: 4px solid rgb(var(--callout-color));
}
.callout[data-callout="narration"] .callout-title {
  font-size: 0.95em;
  letter-spacing: 0.02em;
}
.callout[data-callout="narration"] .callout-content {
  font-style: italic;
  font-size: 1.08em;
  line-height: 1.55;
  padding: 0.85em 1.1em 1em;
}
```
