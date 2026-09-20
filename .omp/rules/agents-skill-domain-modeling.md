---
description: Load domain-modeling on agent-facing doc writes
condition: ".*"
scope: "tool:edit(docs/*), tool:write(docs/*), tool:edit(docs/**), tool:write(docs/**), tool:edit(**/docs/**), tool:write(**/docs/**), tool:edit(styles/*), tool:write(styles/*), tool:edit(styles/**), tool:write(styles/**), tool:edit(**/styles/**), tool:write(**/styles/**), tool:edit(.vale.ini), tool:write(.vale.ini), tool:edit(AGENTS.md), tool:write(AGENTS.md), tool:edit(SKILL.md), tool:write(SKILL.md), tool:edit(constitution.md), tool:write(constitution.md), tool:edit(CONTEXT.md), tool:write(CONTEXT.md), tool:edit(CODEX.md), tool:write(CODEX.md), tool:edit(GROK.md), tool:write(GROK.md), tool:edit(RULES.md), tool:write(RULES.md), tool:edit(specs/**), tool:write(specs/**), tool:edit(**/specs/**), tool:write(**/specs/**), tool:edit(.omp/agents/**), tool:write(.omp/agents/**), tool:edit(.agents/skills/**), tool:write(.agents/skills/**), tool:edit(.omp/skills/**), tool:write(.omp/skills/**)"
interruptMode: always
---

Read `skill://domain-modeling`. Follow it for this write.
