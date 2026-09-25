---
description: Load cli-for-agents on scripts/ writes
condition: ".*"
scope: "tool:edit(scripts/*), tool:write(scripts/*), tool:edit(scripts/**), tool:write(scripts/**), tool:edit(**/scripts/**), tool:write(**/scripts/**)"
interruptMode: always
---

Read `skill://cli-for-agents` before editing anything in `scripts/`. Follow it for this write.
