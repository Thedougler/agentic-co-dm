---
type: rule
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
tags: []
tier: supporting        # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
subtype: subsystem      # class | subclass | background | condition | subsystem | spell | feat | species — always set the real value, never leave this default
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
owner_skill: ".claude/skills/rule-prep/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: 9d2fd531-546d-4391-a0b5-ac9cc1c8c7bd
---

# <Name>

*One-line description — what this rule/option does, in one sentence.*

## Which shape

`subtype: class` or `subclass` → mirror `_srd/_class.md`'s real shape
(Core Traits, Becoming a Class, per-level features) — don't use the
generic shape below. `subtype: background` → mirror `_srd/_background.md`.
`subtype: species` → mirror `_srd/_species.md`. `subtype: spell` → mirror
`_srd/_spell.md`'s Level/School/Casting Time/Range/Components/Duration
shape. Each of these already has a dedicated template with a real
external standard behind it (the 2024 SRD's own format) — copy that
file, not this one's generic headings.

`subtype: feat`, `condition`, or `subsystem` have no dedicated template
— these three use the generic shape below, thickened against the 2024
DMG's own homebrew-content guidance (the same balance-and-precedent
fields the DMG names for a new spell — level/tier equivalence, an
explicit numeric ceiling, a named RAW precedent it sits beside — adapted
to whichever of the three this page is):

## Mechanics

Full mechanical text, structured DMG-style: state the explicit numeric
ceiling (DC, damage dice, duration, uses-per-rest, level/tier
equivalence) and the RAW precedent it was balanced against, not just
"what it does." Label each mechanic [RAW] (book-accurate, name the book)
or [HB] (homebrew), same convention item pages use.

## Provenance

Source book/page, or the ruling/date that created it, plus the RAW
precedent named above.
