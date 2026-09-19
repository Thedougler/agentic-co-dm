---
description: Load dnd-5e-magic-item-design on item entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/item/**), tool:write(wiki/entities/item/**), tool:edit(**/wiki/entities/item/**), tool:write(**/wiki/entities/item/**)"
interruptMode: always
---

Read `skill://dnd-5e-magic-item-design`. Follow it for this write.
