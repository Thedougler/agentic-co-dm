---
title: "A Sliver of the Unstable Form"
aliases:
  - A Sliver of the Unstable Form
category: entities
tags: [shattered-sea, item]
sources:
  - "campaign-os:a-sliver-of-the-unstable-form.md"
created: 2026-09-13
updated: 2026-09-13
type: item
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: revealed
campaign: shattered-sea
visibility: dm
summary: "A fist-sized fragment of warm red hide from Otar the Foul granting 2d8 HP regeneration per turn (1 minute, once per long rest, suppressed by fire/acid). Held by Catarina Da'Virelli in Calveno."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# A Sliver of the Unstable Form

> [!narration] Narration A fragment of red hide the size of a fist, still faintly warm long after everything around it has gone cold. It shouldn't have kept its shape this long. Flesh like this doesn't survive separation from what it belonged to, yet it does anyway. Every so often, so slowly you're uncertain whether the edge of the wound is closing a little further, or if it simply pauses here.

*Wondrous Item, Very Rare (Requires Attunement).*

| Field | Value |
|---|---|
| One thing | Once per long rest, invoke the sliver to regenerate a burst of hit points at the start of each of your turns for 1 minute, unless you've taken fire or acid damage since your last turn. |
| Rarity justification | Comparable to *Ring of Regeneration*, from the opposite direction. |
| Attunement reason | A repeatable, high-value healing effect with no other resource cost. The decision tree's "useful in most encounters without consuming a resource" branch requires attunement. |
| Current holder | [[catarina-davirelli]], kept in her Calveno workshop. |
| Narrative hook | Part of tonight's raid-site loot, offered as a Reward in `vault/episodes/006/s06-run-guide.md` § Rewards. |

Nobody cut this free on purpose. It tore loose at the last moment, as the creature fell. Whether it means anything remains unclear.

*Ring of Regeneration* is permanent and passive, and reattaches severed limbs. This sliver trades permanence for a much stronger in-combat burst, gated to once per long rest and suppressed by the exact damage types that stopped the creature it came from. Both land at roughly the same power tier.

## Mechanics

**[HB] Borrowed regeneration.** As a bonus action, invoke the sliver. For the next minute, at the start of each turn you regain 2d8 hit points. If you took fire or acid damage since your last turn, that turn's regeneration fails. It returns on your next turn unless fresh damage blocks it. Once per long rest.

**Edge cases:** the sliver still triggers at 0 HP if stable and works like any healing to end unconsciousness. It checks damage taken for suppression, not damage type available, so your own fire/acid spells won't suppress it. Invoking it again before the first use ends has no added effect.

**Limitations:** only you gain the benefit. It grants no bonus to attack, damage, save DC, or AC. The effect stops early if you dismiss it (no action) or if you drop to 0 HP and fail a death save while suppressed.

## Provenance

Torn from the creature that rose out of [[solange-barret]]'s summoning circle in the Primary Chamber and fell there after the fight. See [[otar-the-foul]]. Nobody has identified who or what originally intended this fragment to survive on its own. It simply persists.
