---
description: Load narrative-islands on quest entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/quest/**), tool:write(wiki/entities/quest/**), tool:edit(**/wiki/entities/quest/**), tool:write(**/wiki/entities/quest/**)"
interruptMode: always
---

Read `skill://narrative-islands`. Follow it for this write.
