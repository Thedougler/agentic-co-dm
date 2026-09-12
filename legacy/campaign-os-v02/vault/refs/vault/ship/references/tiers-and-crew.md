---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Ship tiers 1-4 — the stats, minimum crew, upkeep costs, and below-minimum penalty each tier sets."
created: "2026-08-03"
updated: "2026-08-03"
tags: [maritime]
uid: 905c1dd6-34db-4f2e-8a06-89bada3621c5
---

# Ship tiers, stats, crew, and upkeep

Mechanical craft only — no campaign-specific proper nouns, so every tier and
crew rule here transfers to any setting. `.claude/skills/draft-content/references/ship.md`
references this file rather than restating it.

---

## 1. Tier Model

Determine tier before generating any other content (the Tier Comes First rule). Tier is the optional
`tier:` frontmatter key (`vault/_templates/_srd/_ship.md`, governed enum `1 | 2 | 3 | 4`).

| Tier | Vessel examples | Cargo | Guns | Cost (used/prize) |
|---|---|---|---|---|
| 1 | Sloop, cutter, lugger | 20 tons | 2–6 | 800–2,000gp |
| 2 | Brigantine, schooner | 60 tons | 8–16 | 4,000–10,000gp |
| 3 | Frigate, galleon | 150 tons | 20–40 | 15,000–35,000gp |
| 4 | Ship of the line, man-of-war | 300 tons | 60–100 | 60,000–120,000gp |

Used or prize vessels cost 40–60% of new. Tier 1 is attainable in early play. Tier 2
requires a significant job, prize, or faction backing. Tier 3 is late-campaign. Tier 4
is end-game fleet-command territory.

**Tier Progression Principle.** Each higher tier is superior in almost all respects — a
Tier 2 vessel out-sails, out-guns, and out-carries a Tier 1. **The speed exception:**
large vessels sacrifice speed for mass — Tier 3 is slower than Tier 2, Tier 4 slower
than Tier 3, by design, not an error. A speed-built lower-tier vessel may match or
outrun a standard higher-tier one under ideal conditions — the intended exception, not
grounds for treating tiers as equivalent.

**The tier floor holds for all variants** (§ 4 below). Customization moves stats within
a tier; it never compresses the gap between tiers. A Tier 2 cargo-optimized hull still
out-carries any Tier 1 vessel.

**RAW calibration.** The 5e SRD's own Airborne and Waterborne Vehicles table
(`vault/srd/rules/mounts-vehicles.md`) is the gut-check anchor for these
four tiers, since nothing else in this file is RAW-sourced: Tier 1 sits around the
[[keelboat|Keelboat]]/[[rowboat|Rowboat]] scale (AC 11–15, HP 50–100, crew 1); Tier 2 around the [[longship|Longship]]/
[[sailing-ship|Sailing Ship]] scale (AC 15, HP 300, crew 20–40); Tier 3 around the [[warship|Warship]]/Galley scale
(AC 15, HP 500, crew 60–80); Tier 4 exceeds anything the SRD table states outright —
end-game fleet-command territory, `[HB]` by necessity. Use this to sanity-check a
custom vessel's stats before finalizing, not to force an exact match — the SRD table
has no Maneuverability/Profile columns and no per-role crew breakdown, both of which
stay this skill's own elaboration (§ 3 below).

## 2. Ship stats

Ships in this repo state stats as a body table under `## Stats & Combat` (never
frontmatter — `vault/_templates/_srd/_ship.md`'s ship keys are `ship_class`/`tier`/`home_port` only).
`vault/campaigns/shattered-sea/vehicles/vethka.md` is the live local precedent for the table's shape: Tier, Hull
Points, Hull AC, Maneuverability, Profile, Crew (min/full), Cargo — adapt columns to
what the vessel actually needs (a Tier 1 raiding proa doesn't need a Guns row; an
armed Tier 3 galleon does). Use the 2024 DMG vehicle stat block as the mechanical
grounding for Hull Points/AC/Speed when a real number is needed at the table; Condition
(Pristine / Worn / Damaged / Wrecked) is tracked narratively, mechanical effects applied
when relevant.

**Damage Threshold** — a standard column for any Tier 2+ vessel, or a Tier 1 vessel
with the Defended variant (`vault/refs/vault/ship/references/acquisition-and-variants.md` § 2). Per the SRD's
Damage Threshold rule (`vault/srd/rules/damage-threshold.md`): the vessel has
[[immunity|Immunity]] to all damage from a single attack or effect unless that instance meets or
exceeds the threshold, in which case it takes the entire amount. The SRD table's own
thresholds (Keelboat 10, Longship/Sailing Ship 15, Galley/Warship 20) are the anchor —
scale a custom vessel's threshold to its tier accordingly. A Tier 1 vessel with no
Defended variant carries no threshold (any hit that beats its Hull AC deals full
damage, same as a normal object).

**Repair.** Per the SRD (`vault/srd/rules/mounts-vehicles.md`): repairing 1
Hull Point costs 1 day and 20gp for materials and labor while the vessel is berthed;
halved (time and cost both) at a location with abundant supplies and skilled labor,
such as a city shipyard.

**Ship combat and chases are not this skill's craft.** Vehicle combat/chase resolution
is `encounter-prep`'s territory (the Player Character Boundary) — this guide stops at
"what the ship's numbers are," never "how a chase or a boarding action resolves."

## 3. Crew roles

The SRD states only a single bare crew-minimum number per vessel type
(`vault/srd/rules/mounts-vehicles.md`'s Crew column) with no role breakdown. The role
table below — Captain through Ordinary sailor — is this skill's own `[HB]`
elaboration on top of that RAW floor, same labeling discipline this skill applies to
variants and enhancements (the Bound And Label Every Effect rule): the minimum-crew *number* per tier is RAW-
anchored (§ 1 above), the *roles* that number is divided into are not.

Every ship needs its required roles filled for normal operation. Each role is filled by
a **PC** (adds their relevant ability modifier to checks for that function), a
**hireling** (competent at baseline, no bonus beyond their own stat block), or is
**unfilled** (the function can't be performed, or is attempted at disadvantage).

| Role | Function | Key ability | Required? |
|---|---|---|---|
| Captain | [[command\|Command]] decisions, crew direction, morale | [[charisma\|Charisma]] | Always |
| Navigator | Plotting course, hazard avoidance | [[intelligence\|Intelligence]] ([[navigators-tools\|Navigator's Tools]]) | Open-water voyages |
| Bosun | Rigging, sails, on-deck crew management | [[strength\|Strength]] or [[dexterity\|Dexterity]] | Always |
| Gunner | [[weapon\|Weapon]] maintenance and direction | [[dexterity\|Dexterity]] | If guns are carried |
| Carpenter | Hull repair, damage control | [[intelligence\|Intelligence]] ([[carpenters-tools\|Carpenter's Tools]]) | Repairs at sea |
| Cook | Provisions, crew sustenance | [[wisdom\|Wisdom]] | Voyages over 3 days |
| Surgeon | Treating wounds, casualties | Wisdom (Medicine) | Required only for the Surgeon's-berth facility |
| Ordinary sailor | All other duties | — | Enough headcount to crew the ship |

**Minimum crew by tier** — below minimum, all ship-related checks are at disadvantage
and speed is reduced by 20%:

| Tier | Minimum crew | Full crew |
|---|---|---|
| 1 | 2–4 | 8–12 |
| 2 | 8–10 | 20–30 |
| 3 | 20–25 | 55–80 |
| 4 | 60–80 | 150–250 |

Minimum crew fills the required roles and enough ordinary sailors to operate the ship.
Full crew mans every gun mount and performs at full capability.

## 4. Upkeep

Weekly cost regardless of whether the ship is sailing.

| Cost component | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Crew wages | 8–20gp | 40–80gp | 150–250gp | 400–700gp |
| Provisions | 5–10gp | 20–40gp | 70–120gp | 200–350gp |
| Maintenance | 5gp | 15gp | 40gp | 100gp |
| Berthing fees | 2–5gp | 5–10gp | 10–20gp | 30–60gp |
| **Total (approx)** | **20–40gp/wk** | **80–145gp/wk** | **270–430gp/wk** | **730–1,210gp/wk** |

**Crew wages and facility hirelings.** When a hireling fills both a crew role and a
bastion-facility role (e.g. the Surgeon also crewing the Surgeon's Berth,
`vault/refs/vault/ship/references/bastion.md`), pay the higher of the two rates, not both — the upkeep totals above
assume this. A facility hireling with no matching crew role is an additional cost on
top of upkeep. Missing upkeep is handled narratively: crew will not work indefinitely
unpaid, and the DM decides when patience runs out.

## 5. Living space and reputation

**Quarters by tier** (informs what the read-aloud description and `## Crew` section can
plausibly describe): Tier 1 — captain's bunk aft, hammocks forward, close quarters
throughout. Tier 2 — private captain's cabin, two shared officer berths, forward crew
hammocks. Tier 3 — officer cabins, wardroom, captain's suite, full party privacy. Tier
4 — flag officer suites, captain's great cabin, dedicated surgeon's/carpenter's
quarters, personal stewards.

**Captain's locker** — standard on Tier 2+: a lockable strongbox in the captain's
cabin. Useful as a detail for hidden cargo or ledgers, stated in prose ahead of `## Stats & Combat` rather than partitioned into its own heading
(`.claude/skills/composing-beats/references/runtime-surface.md` §8).

> [!mechanic] Captain's Locker — Lockpicking
> A captain's locker is a locked strongbox with AC 18 against force, or DC 18 **Dexterity ([[thieves-tools|Thieves' Tools]])** to pick. Success opens the locker; failure leaves it intact and alerts the crew.

**Ship reputation** — track separately per major faction and per port the ship
regularly calls at; state it in `## Connections` or the prose ahead of `## Stats &
Combat`, not frontmatter (no governed key for it — same "prose, not a duplicate YAML
field" reasoning as the item guide's `asking_price`).

| Level | Effect |
|---|---|
| Respected | Reduced berth fees, willing hires, faction contacts available |
| Known | Treated on actual deeds, neutral default |
| Wanted | Port access restricted or denied, bounties posted |
| Notorious | Capable crew seek the ship out; some targets surrender rather than fight |

Flying no flag reads as suspicious; flying a false flag is common and carries legal
risk if the deception is caught — name the relevant authority/faction per campaign,
don't invent one from the archived setting's flavor.
