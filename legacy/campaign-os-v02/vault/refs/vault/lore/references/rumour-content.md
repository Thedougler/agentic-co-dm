# Rumour Content Reference

Spark and fuel for a rumour when the DM doesn't have one yet — sibling
reference to `vault/refs/vault/lore/references/content.md`. A page's field
shape and formatting are `vault/refs/vault/lore/references/rumour.md`'s (the
rumour guide), not this file's.

## Sparking a Rumour

A rumour earns its page when it has all three of these; missing one means
it's not ready yet:

- **A draw** — something a PC would actually stop to listen to, not
  background noise.
- **A live question** — the Truth Value isn't settled at the table yet.
- **A path to press further** — a named skill check, NPC, or location
  that can confirm or deny it.

Distortion is the interesting part of a "Partially true" rumour: what a
witness actually saw versus what the retelling turned it into, and why
the distortion happened (fear, self-interest, a game of telephone across
several tellers).

Field shape and mapping onto `vault/_templates/_campaigns/_lore/_lore_rumour.md`
are `vault/refs/vault/lore/references/rumour.md`'s Hard rules — this file
never restates them.

## Worked Example (fixture — placeholder names, not real campaign content)

User: "The party's in port and I want a rumour about the wreck they're
about to go investigate."

Standard queries come back empty for `"The Drowned Ledger"` (the chosen
name) — clean to create.

```markdown
---
type: lore
subtype: rumour
status: pending
publish: false
aliases: ["The Drowned Ledger"]
created: 2026-07-31
updated: 2026-07-31
tags: []
---

# The Drowned Ledger

*Dockside talk that the wreck the party's chasing was carrying more than
cargo.*

## The Rumour

"That ship didn't just sink — the harbormaster's own ledger got dropped
with it, and somebody wants it to stay down there."

## Truth Value

**Partially true.** The ship did carry a ledger, but it was a smuggler's
private accounts, not the harbormaster's — the rumour conflates the two
because the smuggler bribed a harbor clerk, and the clerk is the one who
started this version to cover his own tracks.

## Spread

Started by the bribed clerk, now repeated by two dockside taverns' worth
of regulars. Each retelling adds a little — the latest version claims the
ledger names "half the port," which nobody who's heard it can verify.

## Investigating It

> [!check] Investigation — Cross-check the clerk's story
> DC 13. **Success:** the clerk's account has a gap the night of the
> wreck. **Failure:** the clerk grows suspicious and warns the smuggler.
```
