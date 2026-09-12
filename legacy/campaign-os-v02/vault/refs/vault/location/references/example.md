---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "A worked single-page location fixture running interview to finished page in the current _location.md template shape, with the PC and faction draws left as placeholder slots, plus the NPC stub the prep spawns."
created: "2026-08-03"
updated: "2026-08-10"
tags: [war]
uid: 41884350-cbf1-4a9b-a1b1-92091081e882
---

# Draft — Location, Worked Example

(fixture — placeholder names, not real campaign content)

User: "prep a location — a warehouse a PC's debt runs through, near
Harborwatch."

Standard queries come back empty for `"the Salt Ledger warehouse"` (the
chosen name) across `vault/ vault/campaigns/shattered-sea/pcs/` and
`vault/episodes/*/transcript.md` — clean to
create. `[[example-harborwatch]]` itself already exists (per the npc
guide's fixture), so this new page links `within:` it rather than
recreating it. Interview fills in: subtype `building`, human cultural
root (Harborwatch dockworkers), current role: front for part of
`<PC name>`'s debt to `<the faction that holds the debt>` — both are slots
to fill from the PC sheets and the real creditor, never from this page;
compass neighbours resolved against Harborwatch's own Geography.

```markdown
---
type: location
status: pending
publish: false
title: ""
aliases: ["the Salt Ledger warehouse"]
summary: "A licensed salt-curing warehouse that fronts part of <PC name>'s debt."
created: "2026-07-30"
updated: "2026-07-30"
tags: []
tier: supporting
subtype: building
within: "[[example-harborwatch]]"
north_of: "[[harborwatch-warehouses]]"
east_of: "[[harborwatch-market]]"
south_of: "[[harborwatch-docks]]"
west_of: "[[harborwatch-customs]]"
geography: [urban, waterfront]
campaigns: []
reference_image: ""
---

# The Salt Ledger Warehouse

> [!read-aloud]
> Salt cures the air before the door is even open, and the tally boards
> inside are chalked three names deep for every crate. A clerk squints up
> from a ledger that hasn't left his hands since you walked in. Somewhere
> behind the stacked crates, a second set of footsteps stops the moment
> yours do.

## Structure

Roughly 120 ft. by 60 ft., a long rectangle with the short end on the
street and the loading door at the far, blind end. Flat packed earth
throughout, dropping about 4 ft. to a brine cellar under the rear third,
reached by a plank ramp. Footing turns slick within a stride of the
curing vats, where spilled brine never dries. Crates stacked twice
head-height run the length of the floor in two aisles, so nobody standing
at the street door can see the loading door, or anyone between. Two ways
in: the street door and the loading door, plus the cellar hatch if the
ramp is clear.

Licensed as a salt-curing warehouse, the Ledger's real business is
laundering tallies for anyone who can't put a transaction on the official
Harborwatch books. [[renn-oxby|Renn Oxby]] runs the front desk; the
second set of footsteps belongs to whoever <the creditor faction> sent to
confirm this week's numbers.

**Toy Chest**

| Field | Value |
|---|---|
| verb | Conceal |
| unstable_condition | This week's auditor is a day early and hasn't announced himself yet. |
| consequence | If undetected past close of business, he reports a discrepancy that doubles <PC name>'s next payment. |
| link_of_relevance | Fronts part of <PC name>'s debt to <the creditor faction> at undisclosed terms. |

## Notable NPCs

- [[renn-oxby|Renn Oxby]] — runs the front desk. (existing page)
- [[example-warehouse-auditor|the creditor's auditor]] — stub spawned by
  location prep; needs a full `.claude/skills/draft-content/references/npc.md` pass
  before the table sees him.

```

The spawned stub (illustrative only — this file doesn't exist in the
repo):

```markdown
---
type: npc
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: []
---

# <the creditor's auditor — name pending>

Stub spawned by location prep from the-salt-ledger-warehouse.md — needs a
full npc-guide pass (Toy Chest, Voice & Delivery, Relationships) before
the table sees them.

## Stats & Combat

## Relationships

## Session Log
```

For the settlement-tree case, see
`vault/refs/vault/location/references/settlement.md`'s own worked example (a
smugglers' port with two districts) rather than duplicating a multi-page
example here.
