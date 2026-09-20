---
description: Load vehicle-design on vehicle entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/vehicle/**), tool:write(wiki/entities/vehicle/**), tool:edit(**/wiki/entities/vehicle/**), tool:write(**/wiki/entities/vehicle/**)"
interruptMode: always
---

Read `wiki/templates/vehicle.md` and `skill://vehicle-design`. Follow both for this write.
