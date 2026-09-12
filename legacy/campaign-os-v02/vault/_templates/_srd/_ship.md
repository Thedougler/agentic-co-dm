---
type: ship
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
owner_skill: ".claude/skills/draft-content/references/ship.md"   # OPTIONAL — the guide or skill that owns this page's quality
tags: []
tier: 1                 # OPTIONAL — 1 | 2 | 3 | 4, the ship Tier Model; NOT the universal core/supporting/peripheral scale other types use
# governed keys — set real values or DELETE the line; an empty "" fails
# lint as present-but-invalid (omit-when-unstated)
ship_class: ""
home_port: ""            # OPTIONAL — wikilink to this vessel's home port location page
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
uid: eb315a44-abb6-412a-b133-d43abad12cd7
---

# <Name>

No Player-Known/DM Only split — `publish:`/`status:` on the page itself is the visibility gate, not a heading name; DM-only material (the Ship Toy table, hidden cargo, true ownership) flows in plain prose/table below the stat line, before `## Stats & Combat`, never partitioned into its own heading.

![[<slug>-narration-appearance]]

*[Ship class] · Tier [N] · [home port or "unmoored"].*

The stat line always closes with a period — a standalone emphasis line with no closing punctuation trips markdownlint's MD036.

## Stats & Combat

Ship stats as a body table or statblock (hull, AC, speed, weapons) — never promoted to frontmatter.

## Crew

- Captain: <plain text or wikilink once the page exists>
- Notable crew: append one line each.

## Connections

Optional (not lint-required): owner, home-port faction, rival vessels, writs/liens — durable non-crew relationships. Keeps `## Session Log` (born at first session appearance, per `_templates/CLAUDE.md` § Session Log sections) purely for session-appearance evidence.
