---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "A worked quest fixture running interview through a filled template, showing the Slow Burn pattern and a Strongest Objection in practice with PC draws left as placeholder slots."
created: "2026-08-03"
updated: "2026-08-15"
tags: [mystery]
uid: fd2e4ece-7a94-4c74-9674-d492c5719ea8
---

# Quest Worked Example Reference

Fixture — placeholder names, not real campaign content. Read this to see
the guide's § Secrets & Clues and workflow applied end to end.

User: "I need a quest — someone's been forging Harbormaster tolls, and I
want it to build over a few sessions."

Standard queries come back empty for `"The Toll Ledger"` (the chosen name)
across `vault/` and `vault/episodes/*/transcript.md` — clean to
create. Interview: the party does have a real objective (find and stop the
forger) — not a Front. Two PCs connect: `<PC name>` (their own debt runs
through the tolls) and one other — fill both from the PC sheets, never from
this page. Structural pattern: Slow Burn — the forger's
identity should surface through pattern-recognition across several
sessions, not a single reveal.

```markdown
---
type: quest
status: pending
publish: false
aliases: ["The Toll Ledger"]
created: 2026-07-30
updated: 2026-07-30
tags: []
quest_status: rumored
---

# The Toll Ledger

*Three separate toll receipts, three separate ledgers, and the numbers
don't match any of them.*

## Secrets & Clues

**Hook:** three separate toll receipts, three separate ledgers, and the
numbers don't match any of them.

**Stated objective:** find out who's forging Harborwatch toll receipts
before the Guild audits the books.

**Structural pattern:** Slow Burn. Seeds: a mismatched signature stamp
(session 1), a dockworker who mentions "the same clerk, twice, at two
different windows" (session 2), a torn ledger page with the forger's
real handwriting (session 3+). Payoff: the forger is [[renn-oxby]]'s own
apprentice, covering a debt of his own — players connect it themselves if
they compare the stamp to anything Renn's signed.

**True stakes / opposition:** the apprentice isn't malicious — he's paying
down a debt to the same network <PC name> owes. Exposing him exposes that
network's reach into the Guild itself.

**Strongest Objection:** this could be reading a coincidence (two unrelated
debts to the same creditor) as a conspiracy. `test: grep -ril "<the creditor
faction>" vault/` — if the apprentice's debt and the PC's debt trace to
different cells, the "same network" claim doesn't hold and this becomes two
separate threads, not one.

**link_of_relevance:** Directly threatens to unravel part of <PC name>'s
own debt if the network's exposure reaches them too.

## Beats

- Seed 1: a mismatched stamp on a routine toll receipt, easy to miss.

*(further beats — `draft-story`'s DS4 step fills these once this quest is
picked up at the table.)*

## Outcome

(empty — `transcript-ingest` fills this in once quest_status advances past active)
```
