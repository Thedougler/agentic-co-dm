# View fields

```
VIEW[content][viewFieldType(args):writeTarget]
```

The type defaults to `math` if omitted — `VIEW[{a} * {b}]` ≡ `VIEW[{a} * {b}][math]`. Frontmatter/memory placeholders inside `content` use `{...}` and follow the full bind-target syntax in `bind-targets.md`.

## The 4 types

| Type | `content` means | Notes |
|---|---|---|
| `math` (default) | A mathjs expression | Custom functions need a JS Engine startup script — not installed in this vault |
| `text` | Plain or markdown text | `renderMarkdown` arg renders it as markdown |
| `link` | A property value | Rendered as an Obsidian wiki-link or markdown link |
| `image` | An image path property | Rendered as an embedded image |

## Arguments

`class` (CSS class), `hidden` (compute and optionally write, render nothing), `renderMarkdown` (text type only).

```
VIEW[**{someText}**][text(renderMarkdown)]
VIEW[{property}][link]
VIEW[{property}][image]
VIEW[{a} * {b}][math:c]              ← computes a*b, writes result to c
VIEW[{a} * {b}][math(hidden):c]      ← computes and saves, renders nothing
```

## Circular writes are blocked

If `VIEW[{a}][math:b]` and `VIEW[{b}+1][math:a]` both exist, Meta Bind detects the circular write-to dependency and blocks it (prevents an Obsidian lockup). Treat this as a hard rule, not something to route around.

**A VIEW only recomputes while the note containing the declaration is open.** A cross-note `VIEW[{NoteA#prop}]` written in NoteB stops updating the instant NoteA closes — the computation happens in the note holding the `VIEW[...]` declaration, not the note being read from. This is the single fact most likely to break a "live dashboard" design; don't bury it under a caveat elsewhere, check it before proposing any cross-note VIEW.

## This vault's real usage

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

Used identically across `_templates/{pc,npc,creature,location,location-dungeon,location-settlement,item}.md` — displays a creature/NPC/PC/location's reference image, renders nothing when the property is empty. Owning convention and CSS hook (`.reference-image-view`) documented in `.claude/skills/reference-images/SKILL.md` — read that skill for anything specific to the reference-image convention itself; this file covers `VIEW[...]` in general.
