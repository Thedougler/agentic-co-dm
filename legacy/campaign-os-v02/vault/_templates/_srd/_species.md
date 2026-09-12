---
type: species
status: srd              # draft | pending | canon | srd | retired — sourced species (SRD) start at srd; homebrew starts at draft or canon
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: "5e species text for <Species Name>."
owner_skill: ".claude/skills/draft-content/references/species.md"   # OPTIONAL — the guide or skill that owns this page's quality
created: "{date}"
updated: "{date}"
tags: []
tier: supporting        # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
source: ""       # OPTIONAL — only for a page migrated from an raw/ source (srd) or its earlier draft (homebrew)
source_url: ""           # OPTIONAL — canonical/licensed source reference (SRD document, sourcebook + page citation)
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
uid: 7c542f27-d007-4935-819d-2412ec092408
---

# <Species Name>

**Creature Type:** <Humanoid | ...>

**Size:** <Size> (<height range, e.g. "about 5-6 feet tall">)

**Speed:** <feet> feet

As a(n) <Species Name>, you have these special traits.

**<Trait Name>.** <Trait text, transcribed verbatim from the SRD source. Any named spell, class, or other page the trait grants gets an inline `[[slug|Display Name]]` wikilink at first mention.>

Table: <Table Name>

OPTIONAL — only when the SRD source presents a lineage/ancestry/heritage choice as a table (e.g. Elven Lineages, Draconic Ancestors); omit both the `Table:` line and the table entirely otherwise.

| <Column> | <Column> |
|---|---|
| <Value> | <Value> |

