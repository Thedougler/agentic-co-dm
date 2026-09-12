---
type: npc
status: draft
publish: false
aliases: []
created: "{date}"
updated: "{date}"
tags: []
summary: ""                     # one sentence, ≤200 chars — cheap page preview, never empty
owner_skill: ".claude/skills/draft-content/references/npc.md" # OPTIONAL — the guide or skill that owns this page's quality
subtype: minor           # major | minor | recurring
location: ""             # OPTIONAL — wikilink to this NPC's current location page
role: []                # OPTIONAL — villain | ally | rival | recurring | contact; omit when unstated
has_active_front: false # OPTIONAL — true | false; true when ## Goals & Fronts has 1+ Front at Lifecycle: active — queryable across factions/npcs, kept in sync by .claude/skills/draft-content/references/faction.md and world-update
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
reference_image: ""     # OPTIONAL — vault-relative path to a reference image asset in _assets/reference/, used by image-gen skills as generation context
voice_id: ""            # OPTIONAL — ElevenLabs voice id for dialogue audio (npc-voice skill)
voice: ""               # OPTIONAL — short spoken-voice description; npc-voice designs from this when voice_id is empty
voice_actor: ""         # OPTIONAL — first name of the real person voicing this character (voice-profile enrollment); for an npc, usually nick
uid: 0361b6c0-ff6f-4069-86b5-127881b00f8e
---

# <Name>

**Wants:** <One bold-led line compressing this NPC's `primary_goal` + `active_problem` from the Toy Chest table below: what they're after, and what's in the way right now.>

![[<slug>-narration-appearance]]

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

Read while recording: [[dm-voice-script|voice-profile script]]

Keep the button trio and link above only when a real person voices this
NPC at the table (`voice_actor:` set, Nick for this repo). Omit all four
otherwise.

## Stats & Combat

OPTIONAL. A page carries it only when this NPC fights.

A combat-capable NPC with no build yet defaults to `![[commoner#Stats & Combat]]` — the SRD Commoner as a generic placeholder — rather than an empty section. Once a real build exists, instantiate `vault/srd/monsters/<slug>-statblock.md` or `vault/campaigns/<campaign>/monsters/<slug>-statblock.md` (`vault/refs/vault/monster/references/statblock-format.md`), the same unified format every PC and creature uses, `sim: { side: enemy }` implied by omission, and swap the embed to `![[<slug>-statblock]]`. Never a freeform stat line. A CR-first build (statted as a monster instead of a class-leveled humanoid) follows `vault/refs/vault/npc/references/villains.md` § Stat block approach.

## Relationships

OPTIONAL. A page carries it only when real, sourced content fills it.

Who does <Name> trust, fear, answer to, or work against?

## Goals & Fronts

OPTIONAL. A page carries it only when `subtype: major` or `subtype: recurring` and real, sourced content fills it — a `minor` NPC's agenda doesn't warrant independent tracking.

Active Fronts (clocks) — what is <Name> working toward on their own timeline, and what happens if nobody stops them? Front template and Clock decision rule: `vault/refs/vault/faction/references/front.md`.
