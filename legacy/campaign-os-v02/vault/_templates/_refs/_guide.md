---
type: guide
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
tags: []
tier: supporting               # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
source: ""                     # REQUIRED — the raw/ path this guide was built from, e.g. raw/2026-07/city-creation-guide.md
source_url: ""                 # OPTIONAL — the external URL this guide was originally sourced from
campaigns: []                  # OPTIONAL — this page's campaign(s), if this repo runs more than one
owner_skill: ".claude/skills/find-guidelines/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: 4374c020-0b26-4660-93dc-879d9b1bf25a
---

# <Title>

Instantiated directly by the `find-guidelines` skill. Body is freeform
prose that directs Claude, same layout discipline as a
`.claude/skills/*/SKILL.md` body: no fixed headings, no
agent-instruction HTML comments (`CampaignOS.TemplateAgentComments`, error),
state facts or steps directly rather than restating what another file
already owns (`.claude/rules/docs.md` § DRY).

Reference distilled from a named external source, filed at the source's
topically-appropriate `vault/refs/` location; `source:` is required and
names the `raw/` path it was built from.

Structures freely with whatever H2/H3 breakdown the content actually
needs — no fixed sub-headings required.
