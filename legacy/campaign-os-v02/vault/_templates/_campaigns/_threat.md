---
type: threat
status: draft
publish: false
title: ""                      # OPTIONAL (display title if it differs from the H1 heading; absent, the H1 is the title, llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
owner_skill: ".claude/skills/draft-content/references/threat.md"   # OPTIONAL — the guide or skill that owns this page's quality
created: "{date}"
updated: "{date}"
tags: []
tier: core              # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
threat_status: active   # active | dormant | resolved
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
uid: ee491933-d8e4-440f-bb87-e3238558a54f
---

# <Threat Name>

*One-line description: what danger this is and why it's dangerous.*

## Nature

What this threat concretely is (a plague, a rising war, a countdown to a
ritual, a collapsing trade route). In-world facts only; the timeline itself
belongs to `## Clock` below.

## Clock

Same field shape as a faction's Front (`vault/refs/vault/faction/references/front.md`
defines every field below), this page doesn't redefine them, only carries
its own instance:

```markdown
**Lifecycle:** active | dormant | resolved
**Trigger conditions:**
- <what advances this clock — player inaction, a named NPC/faction action, elapsed time. Dormant: this is what starts the clock running.>
**Clock:** N segments (4 = fast-moving, 6 = slow burn) — filled: 0
**Consequence at fill:** <specific, observable, irreversible>
**Escalation timeline** *(optional — for threats whose approach matters, not just their fill)*:
| Interval | Move | Observable signal |
|---|---|---|
| ... | ... | ... |
**Possible outcomes (2-3):** <none requiring one specific player choice>
**PC connection:** <named PC + the specific mechanism>
**Per-PC awareness** *(only when it differs across PCs)*: <who knows what>
**Quest link:** <[[quest-slug]] if this threat's stakes are actionable content for the party right now, else "none yet">
**Three-Clue Audit** *(only if hidden conclusion)*:
Conclusion: ...
Clue 1: [location/NPC] — [discovery mechanic]
Clue 2: [different location/NPC] — [different mechanic]
Clue 3: [third node] — [third mechanic]
```

## Entangled Parties

OPTIONAL, kept only when a real faction, NPC, or location is actually
caught up in this threat without owning it. Delete outright if nothing
fills it yet. A single clear owner belongs on that faction's or NPC's own
`## Goals & Fronts` instead; this heading is for the plural or partial
case, never a substitute owner field.
