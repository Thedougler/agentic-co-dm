# The Front — what a clock looks like

`.claude/skills/draft-content/references/faction.md` defines this template (its `vault/refs/vault/faction/references/front.md` is the
authoritative spec — read it if a Front looks malformed or a field is unfamiliar).
This skill only ever reads and mechanically edits three of its lines:

```markdown
### Front: <Name>
**Lifecycle:** active | dormant | resolved
**Primary goal:** ...
**Consistent method:** ...
**Off-screen move if unopposed:** ...
**Trigger conditions:**
- <what advances this clock>
**Clock:** N segments (4 = fast-moving, 6 = slow burn) — filled: <n>
**Consequence at fill:** <specific, observable, irreversible>
**Escalation timeline** *(optional)*: | Interval | Move | Observable signal |
**Possible outcomes (2-3):** ...
**PC connection:** ...
**Quest link:** ...
```

Only `active` Fronts get triaged and advanced. `dormant` Fronts are only touched if
this turn's evidence shows their named trigger firing (a `FACT` line flipping
`**Lifecycle:** dormant` → `active`, still citing the evidence). `resolved` Fronts are
history — skip them; `.claude/skills/draft-content/references/faction.md` keeps them on the page as a record, this skill
never revisits them.

A Front missing `**Trigger conditions:**` or `**Consequence at fill:**` isn't ready to
advance — that's a `.claude/skills/draft-content/references/faction.md` gap, not something to guess at here. Flag it and
suggest the DM route back to `.claude/skills/draft-content/references/faction.md` to complete the Front (Hard Rule 5).
