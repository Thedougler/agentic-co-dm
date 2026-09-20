---
description: Load spell-design on spell entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/spell/**), tool:write(wiki/entities/spell/**), tool:edit(**/wiki/entities/spell/**), tool:write(**/wiki/entities/spell/**)"
interruptMode: always
---

Read `wiki/templates/spell.md` and `skill://spell-design`. Follow both for this write.
