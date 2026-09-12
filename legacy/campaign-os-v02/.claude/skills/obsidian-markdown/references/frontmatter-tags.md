# Properties (Frontmatter) and Tags

## Properties (Frontmatter)

Obsidian renders YAML frontmatter as a Properties panel. Rules:

```yaml
---
type: entity
title: "Note Title"
campaign: "shattered-sea"
created: 2026-04-08
updated: 2026-04-08
tags:
  - npc
  - shattered-sea
status: active
related:
  - "[[Other Note]]"
sources:
  - "[[source-page]]"
---
```

Rules:
- Flat YAML only. Never nest objects.
- Dates as `YYYY-MM-DD`, not `2026-04-08T00:00:00`.
- Lists as `- item`, not inline `[a, b, c]`.
- Wikilinks in YAML must be quoted: `"[[Page]]"`.
- `tags` field: Obsidian reads this as the tag list, searchable in vault.

---

## Tags

Two valid forms:

```markdown
#tag-name             — inline tag anywhere in the body
#parent/child-tag     — nested tag (shows hierarchy in tag pane)
```

In frontmatter:
```yaml
tags:
  - research
  - npc
```

Do not use `#` inside frontmatter tag lists. Just the tag name.
