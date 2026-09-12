---
type: session
subtype: overview
status: draft
publish: false
aliases: []
created: "{date}"
updated: "{date}"
tags: []
summary: ""                   # one sentence, ≤200 chars — cheap page preview, never empty
tier: supporting        # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
edit_pass: 0            # OPTIONAL — last completed line pass (0–3); the draft-story skill is this key's sole writer
session_number:
session_date:
session_shape:          # crossing | site | town | intrigue | investigation | set-piece | hunt | downtime | climax
world_date:              # this session's in-fiction date, in the campaign calendar's own reckoning, e.g. "15 Eleint, 1495 DR" (see the calendar page's current_date)
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
owner_skill: ".claude/skills/draft-content/references/run-guide.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: c4e8a1f0-9b2d-4c7e-8a11-0f3d6b9e2a14
---

# Session <NN>: Overview (<Title>)

Write this file as `vault/episodes/<NNN>/e<NN>-overview.md`. Agents read this page before writing or opening a run-guide.

## Tonight

Where play starts, the shape, the opening pressure.

- Shape: <session_shape>
- Start: <place, time, immediate condition>
- Opening pressure: <live force already moving>
- Opening stretch: [[e<NN>-run-guide-<slug>|<Name>]]

## Run guides

Stretches that can start tonight, in start order. One line each. Tonight's overview lists nearby and tonight-reachable guides; far planned guides exist on their Situation and stay off this list.

- [[e<NN>-run-guide-<slug>|<Stretch>]] — <one line: when to open it>
- [[<situation-slug>-run-guide|<Situation>]] — <one line: when to open it>
