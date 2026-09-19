---
description: Load theatre-of-the-mind when a wiki write carries a narration callout
condition: '(?i)\[!narration'
scope: "tool:edit(wiki/**), tool:write(wiki/**), tool:edit(**/wiki/**), tool:write(**/wiki/**)"
interruptMode: always
---

Read `skill://theatre-of-the-mind`. Follow it for this write.
