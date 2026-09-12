---
type: faction
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
owner_skill: ".claude/skills/draft-content/references/faction.md"   # OPTIONAL — the guide or skill that owns this page's quality
created: "{date}"
updated: "{date}"
tags: []
tier: supporting        # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
faction_status: active   # active | dormant | dissolved
has_active_front: false  # OPTIONAL — true | false; true when ## Goals & Fronts has 1+ Front at Lifecycle: active — queryable across factions/npcs, kept in sync by .claude/skills/draft-content/references/faction.md and world-update
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
uid: 77e3f9f7-d28f-46cb-8009-f7648fd3cc4a
---

# <Name>

![[_assets/banners/<slug>-banner.webp]]                     <!-- OPTIONAL — only when the asset file exists; never invent one -->

*One-line description — what this faction wants and how it operates.*

## Members

Named leadership and notable members — who speaks for this faction? Hidden truths (a secret identity, a motive the faction itself doesn't advertise) go here inline, marked in prose — not in a separate section (runtime-surface.md § Prep-entity floor § 8).

## Goals & Fronts

OPTIONAL — only when real, sourced content fills it.

Active Fronts (clocks) — what is this faction working toward, and what happens if it succeeds? What hasn't reached the party yet still lives here — a Front's own `Per-PC awareness` field carries what differs across PCs (runtime-surface.md § Prep-entity floor § 8).
