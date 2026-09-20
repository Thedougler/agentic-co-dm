---
description: Load dnd-5e-magic-item-design on item entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/item/**), tool:write(wiki/entities/item/**), tool:edit(**/wiki/entities/item/**), tool:write(**/wiki/entities/item/**)"
interruptMode: always
---

Read `wiki/templates/item.md` and `skill://dnd-5e-magic-item-design`. Follow both for this write.
