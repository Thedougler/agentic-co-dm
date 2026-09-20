---
description: Load place-design on place entity writes
condition: ".*"
scope: "tool:edit(wiki/entities/place/**), tool:write(wiki/entities/place/**), tool:edit(**/wiki/entities/place/**), tool:write(**/wiki/entities/place/**)"
interruptMode: always
---

Read `wiki/templates/place.md` and `skill://place-design`. Follow both for this write.
