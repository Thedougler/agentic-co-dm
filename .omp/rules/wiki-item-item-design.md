---
description: Load item-design on item entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/item/**), tool:write(wiki/entities/item/**), tool:edit(**/wiki/entities/item/**), tool:write(**/wiki/entities/item/**)"
interruptMode: always
---

Read `wiki/templates/item.md` and `skill://item-design`. Follow both for this write.
