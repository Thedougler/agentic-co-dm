---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The Front template — clock, trigger, and consequence — plus lifecycle states, the quest-link rule, and the faction_status frontmatter key."
created: "2026-08-03"
updated: "2026-08-03"
tags: [politics]
uid: 037aad92-fb0e-40da-b2cc-ea8dd66ff409
---

# The Front (clock, trigger, consequence)

Full mechanics for authoring a front inside a faction's `## Goals & Fronts`
section. See `.claude/skills/draft-content/references/faction.md` for the Clock Decision
Rule and when to apply this.

## Front template

```markdown
### Front: <Name>
**Lifecycle:** active | dormant | resolved
**Primary goal:** <vector — see `vault/refs/vault/faction/references/toy.md`>
**Consistent method:** <behavior — see `vault/refs/vault/faction/references/toy.md`>
**Off-screen move if unopposed:** <observable — see `vault/refs/vault/faction/references/toy.md`>
**Trigger conditions:**
- <what advances this clock — player inaction, a named NPC/faction action, elapsed time. Dormant fronts: this is what starts the clock running.>
**Clock:** N segments (4 = fast-moving, 6 = slow burn) — filled: 0
**Consequence at fill:** <specific, observable, irreversible>
**Escalation timeline** *(optional — for fronts whose approach matters, not just their fill)*:
| Interval | Move | Observable signal |
|---|---|---|
| ... | ... | ... |
**Possible outcomes (2-3):** <none requiring one specific player choice — anti-railroading check, `.claude/skills/composing-beats/references/audits.md` intro>
**PC connection:** <named PC + the specific mechanism, per `.claude/skills/composing-beats/references/runtime-surface.md` §2>
**Per-PC awareness** *(only when it differs across PCs)*: <who knows what>
**Quest link:** <[[quest-slug]] if this front's stakes are actionable content for the party right now, else "none yet">
**Three-Clue Audit** *(only if hidden conclusion)*:
Conclusion: ...
Clue 1: [location/NPC] — [discovery mechanic]
Clue 2: [different location/NPC] — [different mechanic]
Clue 3: [third node] — [third mechanic]
```

The Three-Clue Audit applies whenever the front has a hidden conclusion (a
concealed cause, secret backer, or hidden threat the party must *reach*,
not just witness): three independent clues, different nodes, at least two
reachable without combat. Skip it when the pressure is already fully
visible — an openly advancing faction needs no clues.

## Lifecycle states

- `active` — the clock is running right now.
- `dormant` — the clock starts once its named trigger fires; the trigger
  conditions field is what to watch.
- `resolved` — the front concluded (fired, defused, or overtaken by
  events). Leave it in the page as history; don't delete it.

## If-Ignored discipline

Every front answers what happens if the party never touches it: the
consequence-at-fill field, plus — for fronts whose *approach* should be
visible — the escalation timeline. The tick test (a consequence that isn't
a single visible, in-world change isn't concrete enough) is
`.claude/skills/composing-beats/references/audits.md` §4; this file supplies the
fields that satisfy it.

## Quest links

When a front's stakes become something the party can actively pursue or
oppose — not just observe — link out to a `type: quest` page rather than
letting the front try to *be* the quest. One fact, one page
(`vault/refs/runbook-wiki.md` § Single-source rules): quest beats live on
the quest page; the front links to it. If the quest page doesn't exist
yet, name it as needed and hand off to `.claude/skills/draft-content/references/quest.md` to author it — never
create a full quest page mid-front-write; this file only ever links out.

## The `faction_status` field

The domain field `faction_status: active | dormant | dissolved` records
the faction's own operational state, distinct from the wiki's universal
`status` key (the canon tier: `draft | pending | canon | retired`) — a
page can't carry two meanings on one key. `vault/_templates/_srd/_faction.md` declares
`faction_status` as a `faction`-specific frontmatter key, the same way
`quest_status` is governed for `quest`. Set the whole faction's operational
state there, in frontmatter — never in prose, never as a second
`status`-named key. Each *front*'s own `Lifecycle` field stays a body field
on the Front template (per-front, not per-page — a faction can run several
fronts in different states at once, and frontmatter holds only one value
per key).

The template also pre-fills an optional `campaigns:` key (open value, e.g.
`campaigns: [Shattered Sea]`) — no interview question needed, it's just
carried through from the template.
