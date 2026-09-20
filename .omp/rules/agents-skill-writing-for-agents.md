---
description: Load writing-for-agents on skill, instruction, or wiki template writes
condition: ".*"
scope: "tool:edit(AGENTS.md), tool:write(AGENTS.md), tool:edit(SKILL.md), tool:write(SKILL.md), tool:edit(wiki/templates/**), tool:write(wiki/templates/**), tool:edit(**/wiki/templates/**), tool:write(**/wiki/templates/**)"
interruptMode: always
---

Read `skill://writing-for-agents`. Follow it for this write. Keep skills/instructions and their `wiki/templates/` counterparts synchronized: updating either requires updating the other.
