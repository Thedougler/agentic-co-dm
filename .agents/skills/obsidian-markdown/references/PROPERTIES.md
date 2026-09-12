# Properties (frontmatter)

YAML between `---` at the top of the note.

## ai-co-dm required / usual

| Field | Notes |
|---|---|
| `type` | AGENTS enum: `hub` \| `campaign` \| `session-prep` \| `session` \| `npc` \| `pc` \| `location` \| `faction` \| `quest` \| `front` \| `encounter` \| `item` \| `monster` \| `lore` \| `template` \| `lexicon` |
| `campaign` | e.g. `shattered-sea` |
| `status` | as used by the note (live, stub, …) |
| `tags` | YAML list |
| `visibility` | `table` \| `dm` |
| `summary` | One sentence — what the note is and anything non-obvious. Use to assess a note without full read; create on new notes; update when the note changes |
| `aliases` | optional alternate link names |

Creature extras often include `role`, `cr`, `source` (see `wiki/templates/creature.md`).
Location extras: `kind` (site | settlement | region | dungeon | planar), `region`,
`source` (see `wiki/templates/place.md`).

## Obsidian defaults

`tags` · `aliases` · `cssclasses`

## Types

| Type | Example |
|---|---|
| Text | `campaign: shattered-sea` |
| Number | `cr: 17` |
| Checkbox | `completed: true` |
| Date | `date: 2026-09-05` |
| List | `tags: [npc, aruhe]` |
| Link | `related: "[[Other Note]]"` |

## Tags

Inline `#tag` / `#nested/tag`. Frontmatter:

```yaml
tags:
  - npc
  - aruhe
```

Letters, numbers (not first), `_`, `-`, `/` for nesting.
