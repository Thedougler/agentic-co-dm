---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "A worked item page running interview through rarity check, DM review gate, and finished homebrew mechanics, with the PC draw left as a placeholder slot."
created: "2026-08-03"
updated: "2026-08-10"
tags: [survival]
uid: 3ffa5720-78c2-4bfe-a674-0e93b3e6a6c0
---

# Worked example (fixture — placeholder name, not real campaign content)

User: "Homebrew an item for one of the PCs — something that helps with their
smuggling debt plot, maybe disguises cargo."

Standard queries: `grep -ril "cargo.*disguise\|smuggler.*charm"
vault/` → no hits. Clean to create; nothing to reskin.

Interview fills in: PC connection — `<PC name>`, pulls on their debt
subplot with `<the faction that holds the debt>` (fill both from the PC
sheets and the real creditor, never from this page); one-thing
— "disguises the true nature of cargo to a cursory inspection"; rarity
target — Uncommon; narrative reason — Renn Oxby (an existing NPC fixer)
could plausibly sell it.

Rarity check (the Rarity Comes First rule): Uncommon, comparable to *Cloak
of Many Fashions* (cosmetic-only, too weak — this has a real function) and
[[bag-of-tricks|Bag of Tricks]] (situational,
no attunement) — this item's
one-time-per-inspection function without a resource cost pushes it to
require attunement per the decision tree: the "useful in most encounters
without consuming a resource" branch triggers, so a charge-based limit is
added instead to stay at Uncommon without attunement.

DM Review Gate: one-thing, rarity + benchmarks, and the charge-based
balance fix presented; DM approves. `status:` flips to `pending`.

Resulting page (`false-manifest-seal`):

```markdown
---
type: item
status: pending
publish: false
aliases: ["False Manifest Seal"]
created: 2026-07-30
updated: 2026-07-30
tags: []
rarity: uncommon
attunement: false
---

# False Manifest Seal

> [!read-aloud] A wax seal stamped with a harbor customs sigil that isn't
> quite right if you look twice, the harbor's eel motif facing the wrong
> way. It's warm to the touch even in the cold.

_Wondrous Item, Uncommon._

| Field | Value |
|---|---|
| one_thing | Disguises the true nature of cargo to a cursory inspection. |
| rarity_justification | Comparable to Bag of Tricks (situational, no attunement); charge limit added to stay at this tier without attunement per the decision tree. |
| attunement_reason | Charge-based limit substitutes for the attunement the "no resource cost" branch would otherwise require. |
| pc_connection | Directly serves <PC name>'s active smuggling arrangement under that debt. |
| current_holder | [[renn-oxby]], sells it quietly from his east-pier stall. |
| narrative_hook | Renn could offer it once the debt plot escalates past simple toll evasion. |

## Mechanics

**[HB] Manifest disguise.** Press the seal to a cargo manifest.

> [!mechanic] Manifest inspection
> Until the seal is used again, an inspector reading the manifest makes a
> DC 15 Intelligence (Investigation) check. On a success they spot that the
> paperwork doesn't match the cargo and hold the shipment; on a failure they
> stamp it through and wave the cargo on. No check succeeds automatically,
> and a customs officer with cause to search physically still finds the
> truth regardless of the roll. 3 charges, regains 1 charge at dawn.

**Limitations:** Does not disguise the cargo itself, only its paperwork —
physical inspection defeats it every time. Does not work on a manifest
already flagged as suspicious before the seal is used.

## Provenance

Made by a customs clerk turned forger who worked the harbor for a decade
before disappearing. [[renn-oxby]] acquired three of them from her estate
and sells them one at a time, at a price he never quotes twice.
```
