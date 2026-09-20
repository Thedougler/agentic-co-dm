---
description: Load npc-design on npc entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/npc/**), tool:write(wiki/entities/npc/**), tool:edit(**/wiki/entities/npc/**), tool:write(**/wiki/entities/npc/**)"
interruptMode: always
---

Read `wiki/templates/npc.md` and `skill://npc-design`. Follow both for this write.
