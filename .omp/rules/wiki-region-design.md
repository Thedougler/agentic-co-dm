---
description: Load region-design on region entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/region/**), tool:write(wiki/entities/region/**), tool:edit(**/wiki/entities/region/**), tool:write(**/wiki/entities/region/**)"
interruptMode: always
---

Read `wiki/templates/region.md` and `skill://region-design`. Follow both for this write.
