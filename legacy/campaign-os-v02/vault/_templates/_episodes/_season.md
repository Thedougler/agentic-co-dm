---
type: season
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: ["<Season N Nickname>", "<Short Title>"]
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
owner_skill: ".claude/skills/draft-content/references/season.md"   # OPTIONAL — the guide or skill that owns this page's quality
tags: []
tier: core              # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill). A season is core by definition — it structures the campaign's timeline.
number:                 # this season's number, e.g. 1 — seasons are sequential, season 1 starts at session 1
season_status: planning # planning | active | complete — advances only on session evidence (draft-season.md); "complete" only once the finale below has actually happened at the table
dnd_tier:               # 1 | 2 | 3 | 4 — the 5e tier of play this season covers (SRD: 1 = lvl 1-4, 2 = lvl 5-10, 3 = lvl 11-16, 4 = lvl 17-20). A tier commonly spans more than one season, especially at higher tiers.
level_range: ""         # OPTIONAL — starting-ending party level this season spans, e.g. "1-4"; fill in as sessions land, don't guess ahead
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
uid: f4b47064-0834-43ed-801a-ec97db615bef
---

# Season <N> — <Title>

A season groups a run of sessions under one throughline; its end is
a GM-planned event, never an emergent stopping point.

<One evocative line — this season's throughline or the question it's built to answer.>

## Overview

<What this season is actually about — the throughline connecting its sessions. Not a session-by-session recap — that lives in each session's own recap page.>

## Fronts on Stage

| Front | Where it stands | If nothing stops it |
|---|---|---|
| [[<owning-page>]] | <standing at this season's current edge> | <its next move> |

## PC Arcs

| PC | This season's pull | Last moved |
|---|---|---|
| [[<pc-page>]] | <the specific hook this season presses on> | [[<session-slug>]] |

## Sessions

<Every session in this season, in order. A session belongs to exactly one season — update this table as sessions land, don't pre-fill sessions that haven't happened yet.>

| # | Session | One-line outcome |
|---|---|---|
| 1 | [[<session-slug>]] | <what changed> |

## Finale / End Condition

**Planned:** <the specific event/boss/moment that marks this season's end.>

**Routes:** <at least two distinct player paths that could reach it.>

**If ignored:** <one line — the concrete consequence if the party never pursues it; when the owning page has its own If-ignored section, wikilink it rather than restating its chain.>

**Reached:** <yes, with the session it happened in — or no, still pending.>

## GM Notes

<Themes this season is exploring, threads deliberately left loose for the next season — each named concretely, not implied — and any secrets not yet surfaced to the players.>
