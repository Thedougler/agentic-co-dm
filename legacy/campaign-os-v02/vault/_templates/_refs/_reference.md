---
type: reference
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
tags: []
owner_skill: "~/.claude/skills/writing-for-agents/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality; user-level skill, outside this repo, per this template's own consolidation directive
uid: fccdd603-53f8-468c-8d84-4019a1a004ac
---

# <Title>

Instantiated directly by whichever skill or CLAUDE.md routing entry needs
it — no single owning skill. Body is freeform prose that directs Claude, same
layout discipline as a `.claude/skills/*/SKILL.md` body: no fixed
headings, no agent-instruction HTML comments (`CampaignOS.TemplateAgentComments`,
error), state facts or steps directly rather than restating what another
file already owns (`.claude/rules/docs.md` § DRY).

A lookup catalog of campaign or rules facts for an operator running the
campaign: a safety-boundary table, a feature/system catalog. States the
facts directly.

Structures freely with whatever H2/H3 breakdown the content actually
needs — no fixed sub-headings required.
