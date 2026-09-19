---
description: Load spell-design on spell entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/spell/**), tool:write(wiki/entities/spell/**), tool:edit(**/wiki/entities/spell/**), tool:write(**/wiki/entities/spell/**)"
interruptMode: always
---

Read `skill://spell-design`. Follow it for this write.
