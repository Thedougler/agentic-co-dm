---
type: world
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: ["<Planet or Setting Name>", "<Short Name>"]
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
owner_skill: ".claude/skills/draft-content/references/world.md"   # OPTIONAL — the guide or skill that owns this page's quality
tags: []
tier: core              # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill). A world a campaign actually runs in is core by definition
subtype: original       # original | published | hybrid — invented whole, a published setting, or a published setting carrying homebrew additions
within: ""              # OPTIONAL — quoted, full vault-relative wikilink to the containing world or planet, when this page is one continent/region of a larger body; absent ⇒ this page is the outermost world
current_date: ""        # the world's in-fiction "now", written so it sorts (e.g. "1495 DR")
campaigns: []            # OPTIONAL — the campaigns running in this world
reference_image: ""
uid: c128c381-0313-4f02-b9a8-f5f416c6eabe
---

# <World Name>

A world is the outermost container: campaigns,
seasons, sessions and one-shots all sit inside one. Its child pages — the
campaigns run here, the regions and planes it holds — carry `world:` or
`within:` pointing back to it.

<One evocative line — what kind of world this is and the promise it makes to a party, the way a back-of-book blurb would.>

## Map

OPTIONAL — keep this heading when a chart of this world has been drawn and
stored under `_assets/maps/`; delete it outright when none has. Never write
the heading over prose describing the world's shape: that prose belongs in
`## Geography` below.

<An `![[_assets/maps/<slug>-map.webp]]` embed of the world map.>

## Overview

<Three paragraphs at most. What this world is, what makes it distinct from any other fantasy world, and what a player walking in needs to hold. Not a history and not a gazetteer — both have their own sections below.>

### Tenets

<The world's non-negotiable premises — the facts that hold true in every region and every campaign run here. One sentence each, wikilinked to the entity, place or power it names.>

1. <Tenet one.>

## Geography

<The world's major divisions — continents, seas, and the regions a campaign is likely to touch. One row each; a region with real detail gets its own `_templates/_campaigns/_location/_location_region.md` page and is wikilinked here, never restated.>

| Region | Kind | Notes |
|---|---|---|
| <Name> | <continent \| sea \| region> | <One line — where it sits and what it is known for.> |

## Peoples & Powers

<Who lives here and who rules. Species and cultures by where they are found, then the organizations whose reach crosses regions. A faction with a goal and a timeline gets its own `_templates/faction.md` page and is wikilinked here.>

## Faith & Pantheon

<The deities worshipped here and how faith is actually practised — temple, tribute, oath, or habit. A deity with real presence at the table gets its own `_templates/lore.md` page and is wikilinked from this table.>

| Deity | God of | Domains | Symbol |
|---|---|---|---|
| <Name> | <portfolio> | <domains> | <symbol> |

## Cosmology & Planes

<The planes this world touches and how travel between them works, if it does. Name only what a campaign here can reach or be reached by — a complete planar catalogue belongs in the rules reference, not on a world page.>

## History & Calendar

<The calendar this world dates by, its current year, and the handful of world-shaking events behind the present situation. Ordered oldest to newest, one line each. A campaign's own chronology lives on its timeline page, not here.>

- **<Year>** — <What happened, and why the present still feels it.>

## Campaigns in This World

<The campaigns, one-shots and modules set here, each wikilinked to its own `_templates/campaign.md` page. One line each on where in the world it runs. None yet — say so plainly.>

| Campaign | Where | Status |
|---|---|---|
| [[<slug>\|<Name>]] | <Region.> | <ongoing \| one-shot \| planned> |

## GM Notes

<What is invented and what is inherited. A `subtype: published` or `hybrid` world states plainly which material comes from the published setting and which is this table's own, so a later session never has to guess which it is safe to overwrite. Any licensing constraint on the source material goes here too. Then the world-level secrets: powers not yet public, truths the table has not earned. If genuinely none, say so explicitly rather than leaving the section silently empty.>
