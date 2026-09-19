---
description: Load faction-design on faction entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/faction/**), tool:write(wiki/entities/faction/**), tool:edit(**/wiki/entities/faction/**), tool:write(**/wiki/entities/faction/**)"
interruptMode: always
---

Read `skill://faction-design`. Follow it for this write.
