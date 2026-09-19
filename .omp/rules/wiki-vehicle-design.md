---
description: Load vehicle-design on vehicle entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/vehicle/**), tool:write(wiki/entities/vehicle/**), tool:edit(**/wiki/entities/vehicle/**), tool:write(**/wiki/entities/vehicle/**)"
interruptMode: always
---

Read `skill://vehicle-design`. Follow it for this write.
