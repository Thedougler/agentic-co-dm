---
description: Load npc-design on npc entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/npc/**), tool:write(wiki/entities/npc/**), tool:edit(**/wiki/entities/npc/**), tool:write(**/wiki/entities/npc/**)"
interruptMode: always
---

Read `skill://npc-design`. Follow it for this write.
