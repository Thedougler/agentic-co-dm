# Worked example (fixture — placeholder names, not real campaign content)

User: "I need a fight — smugglers ambush the party on the docks, tied to a
PC's debt thread."

Standard queries: `"harborwatch ambush"` returns nothing across
`vault/campaigns/shattered-sea/pcs/`; clean to create. Party read: that PC's
sheet under `vault/campaigns/shattered-sea/pcs/` shows
`class_levels: "Rogue 5"`, `hp_max: 38`; `## Session Log` shows two prior
CR-4 fights, one "nearly dropped them to 0 from a single crit" note from
session 3.

Interview fills in: combat encounter, connects to `<PC name>`'s debt to
`<the faction that holds the debt>` (§ Hard Rule 1) — both are slots to fill
from the PC sheets and the real creditor, never from this page; location
`[[example-harborwatch]]` (existing page), 4 generic smugglers plus one named
enforcer who might recur.

The named enforcer triggers a hand-off: `.claude/skills/draft-content/references/npc.md` builds its own page for
Vess Corrow (a Standard-role villain, per that skill's own villain stat
approach). This skill does not write that stats block.

`vault/campaigns/shattered-sea/encounters/<harborwatch-ambush>.md`:

```markdown
---
type: encounter
status: pending
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: []
---

# Harborwatch Ambush

**Brief:** Four smugglers and their enforcer hit the party the moment they
leave [[example-harborwatch]] with <PC name>'s debt ledger in hand.

| Field | Value |
|---|---|
| primary_goal | Prove the debt isn't paper — someone is willing to use force over it. |
| consistent_method | Surround, demand the ledger, escalate only if refused. |
| active_problem | The creditor's enforcer is already three days overdue reporting back. |
| performance_hooks | Dockside-crew vibe; the enforcer never raises her voice. |
| link_of_relevance | Directly targets <PC name>'s debt thread. |
| terrain_shift | Round 2: a passing harbor patrol forces the smugglers to commit or flee. |
| objective | Recover the debt ledger — the fight ends the moment either side has it and breaks contact, not necessarily when one side is defeated. |

## Enemy Roster

- 4× Smuggler — reskinned Bandit (*MM p.343*), no changes.
- [[vess-corrow|Vess Corrow]] (enforcer) — see her page for stats.

## Challenge Calibration

Party: <PC name> (Rogue 5, HP 38), [+3 more PCs, stats pasted]. Session Log
evidence: session 3 near-drop to a single crit at CR 4 → this party's
Deadly ceiling for a *solo* burst threat is lower than the standard band
suggests. 5-enemy group at CR 1/2 each (smugglers) + CR 3 enforcer sits at
Hard, not Deadly, per the standard XP budget — but the enforcer's opening
action should avoid a single burst-crit scenario against one PC, per the
session-3 evidence. `[medium confidence — 1 comparable data point]`.

## Terrain

- Stacked cargo crates: partial cover, climbable (DC 12 Athletics).
- Wet dock boards near the edge: DEX save or prone on a hit within 5 ft of
  the edge.

## Tactical Notes

Smugglers surround and demand the ledger round 1. If refused, Vess opens
combat targeting whoever's holding it. Smugglers flee at 2 remaining or if
Vess is dropped below half HP.

## Run Sheet

**Foe roster**

| Foe | Init | AC | HP | Flees/breaks at | Action script |
|---|---|---|---|---|---|
| 4× Smuggler | +1 | 12 | 11/11 each | 2 remaining | Surrounds, demands ledger; attacks whoever refuses |
| Vess Corrow | +3 | 15 | 52/52 | ≤26 HP (half) | Opens on the ledger-holder; disengages if dropped below half |

**Round script**

- **R1:** Smugglers surround the party and demand the ledger; no attacks yet.
- **R2+:** On refusal, Vess attacks the ledger-holder; smugglers pile onto whoever fights back.
- **Trigger — round 2:** a harbor patrol passes (terrain_shift); both sides must commit or break off.

Statblocks: 4× Smuggler — [[bandit|reskinned Bandit, *MM p.343*]]; Vess Corrow — see [[vess-corrow]].

## Raising the Stakes

- **Trigger:** party clears 2+ smugglers before round 2 with resources to spare → **Delta:** the harbor patrol's terrain_shift arrives a round early, forcing a choice under pressure instead of a clean mop-up.

## Lowering the Stakes

- **Trigger:** a PC drops below half HP → **Delta:** remaining smugglers (2 or fewer) flee immediately instead of holding for the "2 remaining" threshold.

## Endings

**Win:** the party recovers the ledger and breaks contact — <PC name>'s debt terms hold at their current rate.

**Defeat:** a downed party doesn't die here — smugglers take the ledger and anything of obvious value, then withdraw; the creditor's price for silence goes up next negotiation (same as the flee outcome below).

**Disengage/flee:** the smugglers keep the ledger and Vess reports it recovered, changing next session's debt-negotiation terms.

## Stakes

Ledger lost → <PC name>'s debt terms get worse next negotiation. Ledger kept →
the creditor's price for silence goes up instead.

## If Ignored

Not skippable — this is an ambush, not a hook. If the party breaks off the
fight early (flees), the smugglers keep the ledger and Vess reports it
recovered, changing next session's debt-negotiation terms.

## Transition

- Ledger recovered or lost, contact broken → [[example-harborwatch]], same evening.
```

**Failure case, same encounter.** A tempting shortcut: skip the `.claude/skills/draft-content/references/npc.md`
hand-off and just write Vess's stats directly into the Enemy Roster
because "she's simple, just a [[bandit-captain|Bandit Captain]] reskin." This fails Hard Rule
4 — the interview already flagged her as possibly recurring, and a stat
block written here has no page, no Toy Chest, no Three Villain Questions,
and no escape mechanic if the party corners her. If she survives this
fight and shows up again, there's nothing to expand — the encounter page
isn't the right home for a character who outlives the encounter. Fix: hand
off to `.claude/skills/draft-content/references/npc.md` even for "simple" villains once recurrence is possible;
the page costs one extra step now and saves a retrofit later.
