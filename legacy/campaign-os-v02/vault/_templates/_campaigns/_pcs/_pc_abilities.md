---
type: pc-abilities
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
last_synced: ""         # date this page was last reconciled against the character sheet
uid: adc7d8dc-63fa-4965-a8f4-286114ebac6b
---

# <Name> — Abilities

Built from the player's character sheet. One
section per action-economy slot so a table runner can transclude exactly
the one they need mid-round (`![[<pc-slug>-abilities#Reactions]]`) — an
ability that costs an Action goes under Actions and is named, not
repeated, anywhere else.

Everything [[<pc-slug>]] can do, sorted by what it costs to do it.
Spells are listed on [[<pc-slug>-spells]]; only the class feature that
grants the casting appears here.

## Traits

Species and background traits — always-on, no activation cost.

| Trait | Source | Effect |
|---|---|---|

## Features

Class and subclass features that are not themselves an Action, Bonus
Action, or Reaction — passives, resource grants, and rest recoveries.

| Feature | Source | Effect | Uses | Recovery |
|---|---|---|---|---|

## Actions

Attacks belong here, one row per distinct option, with the full stat line.

| Action | To-Hit / DC | Damage / Effect | Uses | Notes |
|---|---|---|---|---|

## Bonus Actions

| Bonus Action | Trigger / Cost | Effect | Uses | Recovery |
|---|---|---|---|---|

## Reactions

| Reaction | Trigger | Effect | Uses | Recovery |
|---|---|---|---|---|

## Feats

A feat whose whole effect is an Action, Bonus Action, or Reaction is named
here and its mechanics live in that section — one row, one pointer, never
the mechanics twice. No feats taken states so in one line; the section is
never left empty.

| Feat | Source | Effect |
|---|---|---|
