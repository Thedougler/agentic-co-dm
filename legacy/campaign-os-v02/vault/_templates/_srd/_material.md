---
type: material
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
tags: []
tier: supporting        # core | supporting | peripheral
source: ""               # required for a transcribed or vendored material — the sourcebook or document this material comes from; OPTIONAL for an original homebrew material
source_url: ""            # OPTIONAL — a live external source link, when one exists
form: commodity          # ore | metal | reagent | flora | food | drink | poison | commodity | other
rarity: common           # mundane | common | uncommon | rare | very rare | legendary
unit: ""                  # the unit this material is counted, bought, and sold in — e.g. "lb", "oz", "vial", "bushel", "dose"
worth: ""                 # worth in this setting's currency unit, per the unit above — e.g. "50 gp", "200 credits"
found_at: []              # array of wikilinks to the places/sources this material can be obtained — mined, grown, brewed, bought — the closest thing to its current holder
campaigns: []             # OPTIONAL — this page's campaign(s), if this repo runs more than one
reference_image: ""      # OPTIONAL — vault-relative path to a reference image asset in _assets/reference/, used by image-gen skills as generation context
owner_skill: ".claude/skills/draft-content/references/material.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: bf72ad2d-db50-469c-b9c1-81f88f574d7f
---

# <Name>

![[<slug>-narration-appearance]]

*[Form], [Rarity].* The stat-line convention immediately follows the narration embed, e.g. "Ore (Metal), Rare." or "Flora (Herb), Common." or "Poison, Uncommon." Name what this substance concretely is in one line before any prose.

## Properties

What this substance physically is: appearance, texture, smell, how it forms or comes out of the ground, a plant, or a creature (mined, grown, brewed, rendered), and any hazard its raw form carries (toxic to handle, volatile, spoils fast). Absorbs substances, ores, reagents, flora, food and drink, and drugs and poisons at the raw-material level, not the finished, crafted thing a smith or brewer makes out of it.

## Uses

What this material is for. It might feed a crafting input or season a dish. It might brew into a medicinal or ritual reagent, or poison a blade or a drink instead. State only what the substance itself does as a traded good so future prep can lift it straight onto a stat line. Name the dose, then the method of application. A poison's mechanical effect on whoever it hits is a `condition` page, never restated here.

## Trade

OPTIONAL. Omit only when this material has no established market yet (a wild-only harvestable nobody buys or sells). Name who deals in it, whether it moves openly or someone guards it or bans it, and, via `found_at`, where a party could actually go get some.
