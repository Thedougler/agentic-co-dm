---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "A worked NPC page running interview through every finished section — Toy Chest, Voice & Delivery, Relationships — with PC and faction draws left as placeholder slots."
created: "2026-08-03"
updated: "2026-08-10"
tags: [survival]
uid: 048596ab-1731-4898-8107-4ea900bda508
---

# Worked example (fixture — placeholder name, not real campaign content)

User: "prep an NPC — a smuggler at the docks who's connected to a PC's debt
plot."

Standard queries come back empty for `"Renn Oxby"` (the chosen name) across
`vault/ vault/campaigns/shattered-sea/pcs/` and `vault/episodes/*/transcript.md` — clean to create.
Interview fills in: human, dockside fixer, location `[[example-harborwatch]]`,
connects to `<PC name>`'s debt to `<the faction that holds the debt>`. Both
placeholders are slots, not answers — fill them from the PC sheets and the
real creditor the table has already met, never from this page.

```markdown
---
type: npc
status: pending
publish: false
aliases: ["Renn Oxby"]
created: 2026-07-30
updated: 2026-07-30
tags: []
location: "[[example-harborwatch]]"
---

# Renn Oxby

*A dockside fixer who fronts part of <PC name>'s debt to <the creditor faction>.*

**Quote:** "I don't do favors. I do arithmetic."

> [!read-aloud] Thirties, with a boxer's flattened nose and hair cropped
> back to stubble. His left ear is a knot of scar tissue where something
> took a piece out of it. Canvas vest over bare arms, forearms roped with
> the muscle that comes from work rather than training, and a belt carrying
> three empty knife-sheaths. He's stacking crates two at a time, one hand
> drifting back toward that belt between lifts. He doesn't look up.
> "Cargo, or conversation?"

**Roleplay Concept:** dockworkers'-union shop steward + freelance debt broker.

**Opening move:** stacking crates on the east pier · Renn speaks first · "Cargo, or conversation?"

**Lore Sheet:** Runs unlogged cargo through Harborwatch's east pier for
anyone who can pay the toll. Keeps no ledger — the numbers live in his
head, which is exactly why nothing traces back to him. Currently fronting
part of <PC name>'s debt to <the creditor faction>, at a rate the PC hasn't
seen written down.

**Toy Chest**

| Field | Value |
|---|---|
| primary_goal | Clear the east pier's toll debt before the harbormaster audits it. |
| consistent_method | Names a price only once, flat, no negotiation — then goes quiet until it's paid. |
| active_problem | A rival fixer is underselling his toll rate and pulling his regulars. |
| performance_hooks | Dockworkers'-union steward vibe. Never says a number twice. |
| link_of_relevance | Holds part of <PC name>'s debt to <the creditor faction> at undisclosed terms. |

**Voice & Delivery:** Flat, transactional. "Cargo, or conversation?" /
"That's the number." Doesn't posture, doesn't threaten — the silence after
a price does the work.

## Stats & Combat

(none — not a combat NPC)

## Relationships

- <PC name> — holds part of that PC's debt (link_of_relevance)
- [[example-harborwatch]] — works the east pier

## Session Log

(empty — `transcript-ingest` fills this in once Renn appears at the table)
```
