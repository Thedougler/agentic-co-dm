---
type: pc-spells
status: canon
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
owner_skill: ".claude/skills/combat-profiles/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality
tags: []
pc: "{pc-slug}"
pc_level:               # total character level — must match [[<pc-slug>]]'s own `level:`
casting_classes: []     # every spellcasting class on this PC, e.g. [Bard, Warlock]
last_synced: ""         # date this page was last reconciled against the character sheet
uid: acebcaab-b40d-44cd-b528-9c63515914e1
---

# <Name> — Spells

[[<pc-slug>]]'s spell list. A multiclass caster keeps each class's pool
separate — Pact Magic is not a Bard slot and the two never merge. Every
spell name wikilinks to its SRD page under `vault/srd/spells/`
where one exists — the spell's own text lives there, never copied here;
this page carries only what is true of this character's copy of it.

## Spellcasting

| Class | Ability | Save DC | Attack Bonus | Prepared / Known |
|---|---|---|---|---|

## Cantrips

| Cantrip | Class | Effect at this level |
|---|---|---|

## Known & Prepared

| Level | Spell | Class | Key effect |
|---|---|---|---|

"Key effect" is one clause naming what this spell does for this character
at the table, never the full spell text, which lives on the linked SRD
page.

## Slots & Pools

| Pool | Slots by level | Recovery |
|---|---|---|

One row per independent pool (Bard slots, Pact Magic, a feature that
regains a slot). A pool that recovers on a short rest is stated as such —
the combat sim reads recovery from here when a loadout is authored.
