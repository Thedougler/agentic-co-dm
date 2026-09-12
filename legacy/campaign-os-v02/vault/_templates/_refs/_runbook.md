---
type: runbook
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
tags: []
phase: any                     # 1 | 3 | 4 | 5 | 6 | any — the session-pipeline phase this runbook drives ("any" for standing procedures)
owner_skill: "~/.claude/skills/writing-for-agents/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality; user-level skill, outside this repo, per this template's own consolidation directive
uid: fbd4e020-7b2f-4ef9-8c35-071c94bbad1b
---

# <Title>

Instantiated directly by whichever skill or CLAUDE.md routing entry needs
it — no single owning skill. Body is freeform prose that directs Claude, same
layout discipline as a `.claude/skills/*/SKILL.md` body: no fixed
headings, no agent-instruction HTML comments (`CampaignOS.TemplateAgentComments`,
error), state facts or steps directly rather than restating what another
file already owns (`.claude/rules/docs.md` § DRY).

The one type here with real steps: a numbered multi-step operation
orchestrating templates/skills/linters. Follows `vault/refs/README.md`'s
shared format — a GATE, numbered steps, and a Done line, stated as plain
prose rather than forced into fixed sub-headings:

GATE: <shell command proving the prior phase / precondition — paste its
output>. No/failed → STOP; <the remedy>.

1. <Imperative step. Name the skill that does the work (`<skill>` skill)
   and the exact path it writes. Paste a `<MARKER>:` line from real tool
   output.>
2. <…>

Done = <MARKER>: <what to paste>, <checks green>, commit `<verb>(sNN): ...`
