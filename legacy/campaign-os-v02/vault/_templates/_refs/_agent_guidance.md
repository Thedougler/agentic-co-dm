---
type: agent-guidance
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
tags: []
tier: supporting               # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
owner_skill: "~/.claude/skills/writing-for-agents/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality; user-level skill, outside this repo, per this template's own consolidation directive
uid: bd7f4ca5-a092-45ee-8642-537551b0c94a
---

# <Title>

Instantiated directly by whichever skill or CLAUDE.md routing entry needs
it — no single owning skill. Body is freeform prose that directs Claude, same
layout discipline as a `.claude/skills/*/SKILL.md` body: no fixed
headings, no agent-instruction HTML comments (`CampaignOS.TemplateAgentComments`,
error), state facts or steps directly rather than restating what another
file already owns (`.claude/rules/docs.md` § DRY).

Standing operational/architectural knowledge about this system itself,
addressed to the agent (e.g. `vault/refs/w<N>-*.md`, docs/adr/0029). Never a
numbered procedure (that's `type: runbook`) and never a lookup catalog of
campaign/rules facts (that's `type: reference`).

Structures freely with whatever H2/H3 breakdown the content actually
needs — no fixed sub-headings required.
