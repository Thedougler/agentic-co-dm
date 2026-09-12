---
type: pc
status: draft
publish: false
aliases: []
created: "{date}"
updated: "{date}"
tags: []
owner_skill: ".claude/skills/dnd5e-character-interview/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
tier: supporting        # OPTIONAL - core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
player:
voice_actor: ""         # OPTIONAL - first name of the real person voicing this character (voice-profile enrollment); for a pc, the player's first name
class_levels:
level:                  # total character level — sum of every class in class_levels, e.g. Bard 3 / Warlock 2 -> 5
hp_max:
ac:
init_mod:               # initiative modifier, e.g. +3: Dexterity modifier plus any bonus (Alert feat, class feature)
pp:                     # passive Perception, e.g. 14: 10 + Wisdom (Perception) modifier, including proficiency
speed:                  # walking speed in feet, bare number, e.g. 30 (never "30 ft." or a combined string)
fly_speed:              # OPTIONAL - flying speed in feet, bare number; omit when the PC has no fly speed
swim_speed:             # OPTIONAL - swimming speed in feet, bare number; omit when the PC has no swim speed
climb_speed:            # OPTIONAL - climbing speed in feet, bare number; omit when the PC has no climb speed
burrow_speed:           # OPTIONAL - burrowing speed in feet, bare number; omit when the PC has no burrow speed
role: []                # OPTIONAL — villain | ally | rival | recurring | contact; rarely used for a pc, omit when unstated
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
reference_image: ""     # OPTIONAL — vault-relative path to a reference image asset in _assets/reference/, used by image-gen skills as generation context
uid: cbc801c4-d314-43d0-82b9-4c375b31e70a
---

# <Name>

*One-line description of who they are at a glance.*

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

```meta-bind-button
label: ⏺ Record Voice Profile
style: primary
action:
  type: command
  command: obsidian-shellcommands:shell-command-voiceprstart
```

```meta-bind-button
label: ⏹ Stop
style: destructive
action:
  type: command
  command: obsidian-shellcommands:shell-command-voiceprstop0
```

```meta-bind-button
label: ✔ Save Voice Profile
style: default
action:
  type: command
  command: obsidian-shellcommands:shell-command-voiceprsave0
```

Read while recording: [[<slug>-voice-script|voice-profile script]]

## Overview

![[<pc-slug>-gallery#Portraits]]

## Mechanics

![[<pc-slug>-stats#Combat Stats]]

**Attributes:** [[<pc-slug>-stats]] · **Abilities:** [[<pc-slug>-abilities]] ·
**Spells:** [[<pc-slug>-spells]] · **Inventory:** [[<pc-slug>-inventory]] ·
**Gallery:** [[<pc-slug>-gallery]]

This section transcludes and links. It never states a mechanical fact on
its own. Every per-ability score, skill, action, spell, and item lives on
the satellite page above instead. `class_levels`, `level`, `hp_max`, `ac`,
`init_mod`, `pp`, and `speed` are the scalar keys the roster `.base` views
query, and they stay in this page's frontmatter as the canonical copy. A
non-caster has no spells page, so drop that link instead of pointing at a
file that doesn't exist.

## Backstory

This character's history before the campaign began.

## Relationships

Who this character is bound to and how — party members, family, rivals,
mentors — one line each, wikilinked. Matches the npc template's own
Relationships shape (ADR-0040, FR Wiki character-article genre): a PC is
still a character article, not a bare mechanical sheet.

## Arc Notes (DM Only)

Where this character's personal arc is heading: prepped reveals, hooks tied to their backstory.
