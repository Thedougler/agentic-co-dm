---
description: Load lore-design on lore entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/lore/**), tool:write(wiki/entities/lore/**), tool:edit(**/wiki/entities/lore/**), tool:write(**/wiki/entities/lore/**)"
interruptMode: always
---

Read `wiki/templates/lore.md` and `skill://lore-design`. Follow both for this write.
