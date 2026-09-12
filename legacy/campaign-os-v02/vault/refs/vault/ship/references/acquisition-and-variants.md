---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The five acquisition methods, the variant list, and how to bound a magical shipboard enhancement."
created: "2026-08-03"
updated: "2026-08-03"
tags: [maritime]
uid: 95baaaca-499a-4da8-b0e1-180315cf95a5
---

# Acquiring a ship, variants, and magical enhancements

Mined from the archived `prep-ship` skill's ship-rules and ship-generation
references. Campaign-specific proper nouns (a named shipwright NPC, a specific
home port's dockfront broker, a specific customs authority) are dropped in favor of
generic language — grep this campaign's own `vault/` for a real NPC/faction/location to
fill that role instead of inventing or reusing the archived source's. Reference from
`.claude/skills/draft-content/references/ship.md`, don't restate.

---

## 1. Acquisition methods

Every ship a PC controls names how it was (or will be) acquired — the Acquisition Is Resolved rule. Five
methods, none of them a rubber-stamp:

**Buy.** Available at any port with a shipyard. Asking price runs 10–15% above the
Tier Model's baseline (`vault/refs/vault/ship/references/tiers-and-crew.md` § 1).

> [!check] [Charisma](vault/srd/rules/charisma.md) (Persuasion) — Negotiating Ship Price
> DC 12; negotiating a lower price with a reasonable counter-offer.
> **Success:** The markup gap closes; you negotiate the ship at baseline price.
> **Failure:** You pay the full asking price (10–15% markup included).

Second-hand
ships may hide a real defect — roll secretly (1 on a d6): a meaningful problem the
seller knew about and didn't disclose.

**Steal.** Resolved through the fiction, never summarized. The party needs a plan: who
owns the ship, where she's moored, the watch schedule, how to get her out of harbor.
A well-administered main harbor is hard to steal from (garrison watches the piers,
logs traffic); a loosely administered secondary harbor is easier. A ship sitting in the
outer anchorage waiting for a berth is reachable by rowboat and can simply sail once
crewed.

**Mutiny.** Built on crew relationships, not a single roll — not every sailor flips
because the party asks. Approach potential allies privately before the move; the
outcome reflects the trust actually built beforehand, not a persuasion check rolled in
the moment.

**Prize.** Taking a ship in combat — `encounter-prep`'s territory for the fight
itself (the Player Character Boundary); this file covers only the aftermath. A sinking vessel can be
saved if the winning crew boards and controls the flooding fast enough. A captured
prize needs crew to sail her to port. Stripping her for parts instead of taking her
whole: 2,000–4,000gp in parts for a Tier 2 hull, at the right buyer.

**Build.** Requires a shipyard. Costs the same as buying new, but allows custom
specifications. Build times: Tier 1 — 2–4 months. Tier 2 — 6–12 months. Tier 3 —
18–36 months. Tier 4 — 36–60 months.

## 2. Ship variants and customization

Ships within a tier specialize at construction or via later refit. A variant shifts
which quality the ship optimizes for — the tier floor (`vault/refs/vault/ship/references/tiers-and-crew.md` § 1)
always holds regardless of variant. **Apply one primary variant**; combining variants
is possible but each compounds the tradeoff — only do it for a strong narrative reason.
Refit cost to convert an existing ship: roughly 10–20% of base cost, 2–8 weeks at a
shipyard.

| Variant | Key gain | Key loss | Cost modifier |
|---|---|---|---|
| Speed-Built | +15–20 mi/day good wind, +5–10 mi/day poor wind | −⅓ cargo, −¼ guns | +10–15% |
| Armed | +25–30% gun mounts | −10 mi/day, −⅕ cargo | +10% |
| Defended | Hull Points +20%, AC +1 | −5 mi/day, −⅒ cargo | +15% |
| Cargo | +40–50% cargo | −½ guns (min 2 for self-defense), −10 mi/day | same or below |
| Crew-Optimized | +1 bastion facility space unit, hireling loyalty checks at advantage | none | +5–10% |

A speed-built lower-tier vessel may match a standard higher-tier one under ideal
conditions — the deliberate tier-floor exception named in `vault/refs/vault/ship/references/tiers-and-crew.md` § 1,
not grounds for treating tiers as interchangeable.

## 3. Magical enhancements

Purchasable items and installations, not story-breaking wonders — professional tools a
ship can carry. Tag every one `[RAW]` (a 2024 item used directly or reskinned) or
`[HB]` (homebrew) — same bounded/labeled discipline the Bound And Label Every Effect rule uses for
any homebrew mechanic. State range/duration/recovery and edge cases the same way.

**Price anchors by rarity** (match to this campaign's real availability, not the
archived setting's):

| Rarity | Price range |
|---|---|
| Common | 150–400gp |
| Uncommon | 600–1,500gp |
| Rare | 3,000–12,000gp |
| Legendary | 20,000gp+ |

These sit deliberately below the SRD's own Magic Item Rarities and Values table
(`vault/srd/rules/magic-items.md`: Common 100gp, Uncommon 400gp, Rare 4,000gp, Very
Rare 40,000gp, Legendary 200,000gp) — a shipboard enhancement is professional/utility
gear (a weatherglass, a hull coating, a signal lantern), not a combat-power item like a
+1 weapon or a [Ring of Invisibility](vault/srd/items/legendary/ring-of-invisibility.md), so it shouldn't cost like one. The two scales are
intentionally separate, not a discrepancy: if a specific enhancement's effect is
strong enough to belong in the full magic-item economy instead (e.g. it grants a
combat-relevant benefit comparable to a real magic item), price and label it against
that table instead of this one.

**Worked examples from the archive** (rewrite names/flavor for this campaign — these
are mechanic templates, not fixed catalog entries):

- **Weather forecaster** [HB], Common — accurate 24-hour weather forecast within
  100 miles.
- **Paired signal lanterns** [HB], Common — send a short message to the paired lantern
  at range.
- **Hull mending resin** [HB], Common — repairs hull HP over time with no check
  required, capped at one application per hull section per day.
- **True-north instrument** [HB], Common — immune to magical/environmental compass
  drift.
- **Prow-mounted revealing lantern** [RAW — *[Lantern of Revealing](vault/srd/items/uncommon/lantern-of-revealing.md)* reskin], Common.
- **Favorable-wind charm** [HB], Uncommon — once per day, a fixed bonus to speed for a
  few hours, doesn't function in a storm.
- **Stealth hull coating** [HB], Uncommon — advantage on Stealth checks at sea,
  periodic reapplication.
- **Fog generator** [HB — based on *[Fog Cloud](vault/srd/spells/conjuration/fog-cloud.md)*], Uncommon — deck-mounted, area fog,
  daily recharge.
- **Sending-stone helm** [RAW — [Sending](vault/srd/spells/divination/sending.md) Stones installed at the helm], Uncommon.
- **Automated route-charting table** [HB], Rare — maps the ship's route in real time;
  the charts it produces are themselves saleable.
- **Warded figurehead** [HB], Rare — advantage on saves against magic targeting the
  ship; hostile divination against it requires a save.
- **Crewed by the willing dead** [HB — requires a specific ritual/patron, name the real
  one from this campaign's wiki], Rare — spectral sailors who count as ordinary crew,
  no wages or provisions, but have their own temperament and won't act against what
  binds them.
- **Force-bolt battery** [HB], Rare — per-gun-mount installation, limited charges per
  short rest, unaffected by wet or fire.
- **Submersible hull** [HB — late-campaign salvage only], Legendary — the ship can
  submerge and operate for a limited time per day; crew don't need air while submerged.

Match rarity to actual in-fiction availability: common items are found in any real
market town; legendary items are end-game only, gated behind a named NPC/faction this
campaign's wiki actually establishes (grep `vault/` first — never invent a new access
point when an established one already fits).
