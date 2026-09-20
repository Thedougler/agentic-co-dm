---
description: Load narrative-islands on quest entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/quest/**), tool:write(wiki/entities/quest/**), tool:edit(**/wiki/entities/quest/**), tool:write(**/wiki/entities/quest/**)"
interruptMode: always
---

Read `wiki/templates/quest.md` and `skill://narrative-islands`. Follow both for this write.
