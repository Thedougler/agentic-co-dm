---
description: Load lore-design on lore entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/lore/**), tool:write(wiki/entities/lore/**), tool:edit(**/wiki/entities/lore/**), tool:write(**/wiki/entities/lore/**)"
interruptMode: always
---

Read `skill://lore-design`. Follow it for this write.
