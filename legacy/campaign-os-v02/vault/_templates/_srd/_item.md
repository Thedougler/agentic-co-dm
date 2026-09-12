---
type: item
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
tags: []
tier: supporting        # core | supporting | peripheral
source: ""               # required for a transcribed or vendored item — the sourcebook or document this item comes from; OPTIONAL for an original homebrew item
source_url: ""            # OPTIONAL — a live external source link, when one exists
rarity: common          # mundane | common | uncommon | rare | very rare | legendary | artifact | varies (varies = a disambiguation hub linking each rarity's own variant page — this page never uses attunement:/form: meaningfully, since those differ per variant)
attunement: false
unique: false
form: ""                # weapon | armor | wondrous item | potion | scroll | consumable | tool | material | document — OPTIONAL only on a `rarity: varies` disambiguation hub, where no single form applies
found_at: []             # array of wikilinks to the shops/places where players can find/obtain this item in play (a common item may be sold at several); the item's current holder once already acquired
value: ""                # gp worth of this item, e.g. "50 gp" — its value whether or not it's actively for sale
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
reference_image: ""     # OPTIONAL — vault-relative path to a reference image asset in _assets/reference/, used by image-gen skills as generation context
owner_skill: ".claude/skills/draft-content/references/item.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: 3cf3c9c9-2f4e-476a-b071-928260717afd
---

# <Name>

![[<slug>-narration-appearance]]

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

*[Category] ([subtype, if any]), [Rarity] [(Requires Attunement[ by X], if applicable)].* The SRD stat-line convention immediately follows the narration embed — e.g. "Wondrous Item, Rare (Requires Attunement)." or "Weapon (Longsword), Uncommon." — with the Item Toy table and any other DM-only framing flowing here too, as plain prose/table, no heading of its own.

## Mechanics

OPTIONAL — omit only when the stat-line paragraph above already states the item's full rules text and nothing more remains to add.

Full mechanical text. Every power: labeled [RAW] (book-accurate, name the book) or [HB] (homebrew); bounded with explicit range, duration, and recovery (long rest / short rest / X charges / at-will — "no bounds stated" is the most common balance mistake); edge cases named where they'd plausibly come up at the table. Close with a **Limitations** line — what the item explicitly cannot do.

## Provenance

OPTIONAL — omit only when the item has no in-fiction ownership history to record.

Where this item came from, and who has held it since.
