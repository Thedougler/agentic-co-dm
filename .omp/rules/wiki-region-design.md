---
description: Load region-design on region entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/region/**), tool:write(wiki/entities/region/**), tool:edit(**/wiki/entities/region/**), tool:write(**/wiki/entities/region/**)"
interruptMode: always
---

Read `skill://region-design`. Follow it for this write.
