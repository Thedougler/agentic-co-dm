---
type: deity
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
owner_skill: ".claude/skills/draft-content/references/deity.md"   # OPTIONAL — the guide or skill that owns this page's quality
created: "{date}"
updated: "{date}"
tags: []
tier: supporting         # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
domains: []               # e.g. storm, the deep, oaths — this setting's own domain vocabulary, never a D&D domain list; a deity always has at least one
worship_status: active    # active | dormant | forgotten | usurped — this deity's current worship state in this campaign, independent of status:
alignment: ""              # OPTIONAL — this setting's own moral/ethical schema, if it has one; delete this key entirely for a setting with no alignment axis
within: ""                 # OPTIONAL — quoted vault-relative wikilink to this deity's pantheon or divine-index page, e.g. "[[campaigns/shattered-sea/lore/shattered-sea-pantheon]]"
has_active_front: false   # OPTIONAL — true | false; true when ## Goals & Fronts has 1+ Front at Lifecycle: active — queryable across factions/npcs/deities, kept in sync by .claude/skills/draft-content/references/faction.md and world-update
campaigns: []              # OPTIONAL — this page's campaign(s), if this repo runs more than one
uid: d075a65b-1a36-4b73-9046-79ef3a62b0c8
---

# <Name>

*One-line description: what this deity holds dominion over, and how mortals actually experience it.*

## Portfolio & Presence

What this deity actually governs, stated plainly: expand each domain listed in frontmatter into what it means at the table. How directly this deity acts in the world spans a real range, from never seen at all to walking among mortals in person; pick the real point on that range for this campaign and commit to it instead of hedging across the whole spread. Any hidden truth about the deity's own nature or limits (a power that has quietly failed, a boundary its own clergy won't examine) goes here inline, marked in prose, not in a separate section (runtime-surface.md § Prep-entity floor § 8).

## Worship

How this deity is actually worshipped, where mortals encounter it: tribute, rite, holy day, taboo, stated as lived practice, not doctrine trivia. A church, cult, or clergy organized enough to have leadership and goals of its own is a `faction` page, linked here by `[[wikilink]]`, never restated.

## Relationships

OPTIONAL. A page carries it only when real, sourced content fills it.

Other deities this one allies with, opposes, ranks against, or quietly counters, and why a mortal would ever notice it.

## Goals & Fronts

OPTIONAL. A page carries it only when real, sourced content fills it.

Active Fronts (clocks): what is this deity working toward on its own timeline, and what happens if nobody stops it? Front Template and Clock Decision Rule: `vault/refs/vault/faction/references/front.md`.
