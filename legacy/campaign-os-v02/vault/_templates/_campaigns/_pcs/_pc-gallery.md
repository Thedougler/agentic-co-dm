---
type: pc-gallery
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
tags: []
pc: "{pc-slug}"
owner_skill: ".claude/skills/visual-aids/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: e7c9cfb7-3c53-413f-b272-3a2ae90a3117
---

# <Name> Gallery

One Obsidian image embed per line, `![[_assets/<subfolder>/<file>.webp|alt text]]`,
the subfolder matching `wiki.toml`'s `[thresholds]`'s
`ASSET_SUBFOLDERS`. Every embedded asset must already exist on disk — a
broken embed reads as a missing image, not a placeholder.

Visual reference for [[<pc-slug>]].

## Portraits

The character alone — face, full body, costume changes across levels.

## Scenes

OPTIONAL — only when real, sourced images fill it.

Moments from play. Caption each with the session it came from so the image
stays findable from the session file.

## Reference

OPTIONAL — only when real, sourced images fill it.

Mood, costume, and likeness references handed to image-gen skills. The one
image `reference_image:` points at on [[<pc-slug>]] belongs here too.
