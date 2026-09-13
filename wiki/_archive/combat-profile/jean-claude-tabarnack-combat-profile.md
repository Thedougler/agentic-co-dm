---
type: pc
subtype: combat-profile
pc: "jean-claude-tabarnack"
pc_level: 5
last_session_data: "06"
last_simulated: "2026-07-25"
sim_seed: 1
sim_version: "6.3.0"
confidence_level: "theoretical"
updated: "2026-07-25"
summary: "Ranger 5 combat analysis, sustained DPR 14.97, AC 15, fragile under concentration pressure despite Extra Attack and Dreadful Strike."
tags: [nature, horror]
uid: a2e63976-ca07-46c7-82fc-296f243249b2
---

**FIDELITY WARNING:** this profile relies on a theoretical Ranger 5 sheet — no character-sheet PDF exists yet. Every `[simulated]` number is real script output over `[theoretical]` inputs; the inputs, not the math, are the weak link.

> [!dm]
> Built on `jean-claude-tabarnack-sheet.md`, Ranger 5, full RAW kit (Extra Attack, Dreadful Strike, [[initiative|Initiative]] Bonus, [[hunters-mark|Hunter's Mark]]/[[cure-wounds|Cure Wounds]]/[[magic-weapon|Magic Weapon]]).

## Fast Read

Ranged ambush striker, darkness scout (Gloom Stalker) · sustained DPR 14.97 vs AC 15 `[simulated]` · nova (p95) 26.0 vs AC 15 `[simulated]` · effective HP 44 `[assumed]`, survives ~6–7 attacks at +7 to-hit/10 dmg, poison-immune · Achilles heel: concentration — his single point of failure. Worst-3 matchups ([[aboleth|Aboleth]], Adult Black Dragon, Adult Blue Dragon) break it 0.994/0.526/0.572 times per run `[simulated]`; damage drops to bare bow once broken.

## Combat Stats

| Stat | Value | Lane |
|---|---|---|
| AC / HP | 15 / 44 | `[assumed]` |
| Init / Speed | climb + Standing Leap; Umbral Sight (darkvision-invisible in darkness, unmodeled) | `[sheet]` |
| Hit% vs AC ladder | Shortbow +9 (incl. crit): 75.0% vs AC 15, 65.0% vs AC 17. Incoming: +2 40.0% / +5 55.0% / +7 65.0% / +9 75.0% / +12 90.0% | `[simulated]` |
| Save bonuses (weak → strong) | CHA -1, INT +0, WIS +2, CON +2, STR +3, DEX +6 | `[sheet]` |
| Resource pools (per rest) | 1st-level slots ×4, 2nd-level slots ×2, Dreadful Strike ×2 (= WIS mod, min 1) | `[srd]` |

`node utils/scripts/combat-sim/cli.mjs profile vault/campaigns/shattered-sea/pcs/character-sheets/jean-claude-tabarnack-sheet.md --seed 1`

Damage/round (shortbow +9, optimal auto-policy): mean 14.97/13.26 at AC 15/17, p50 17.0/16.0, p95 26.0/26.0 `[simulated]`. Extra Attack, Dreadful Strike, and Hunter's Mark follow RAW `[srd]`. Expected attacks survived at +7: 13.0 (5 dmg) / 6.5 (10 dmg) / 4.3 (15 dmg) / 3.3 (20 dmg) `[simulated]`. Immune: poison damage, poisoned condition `[pcs-page, grung]` — every [[grung-npc|Grung]] poison rider and Otar's Foul Miasma are zero against him.

Not modeled: Ambusher's Leap's +10 ft [[speed|Speed]] round-1 boost (no round-gated movement primitive), Umbral Sight (no light-state/darkvision primitive), Weapon Mastery (no weapon-mastery primitive), Toxic Secretion and Mortis (passive, no combat math), Favored [[enemy|Enemy]]'s free Hunter's Mark casts (sim costs every cast from the slot pool), [[ensnaring-strike|Ensnaring Strike]]/[[longstrider|Longstrider]]/[[pass-without-trace|Pass without Trace]]/[[spike-growth|Spike Growth]] (unfenced picks), Magic Weapon's +1/+2/+3 upcast damage bonus (no combined to-hit-plus-damage or upcast-scaling primitive; typically cast on an ally's weapon but modifiers compile onto the caster only). Arc Note's "Tongue Lash" has no confirmed SRD match. The level-5 2nd-level spell prepared (if any) is unknown.

## Counters & Synergy

Hard counters: bright light and open ground strip his ambush advantage; [[aboleth|Aboleth]], [[adult-black-dragon|Adult Black Dragon]], [[adult-blue-dragon|Adult Blue Dragon]] — near-0% win, dies fast `[simulated]`. Soft counters: sustained damage and tremorsense break his concentration; [[doppelganger|doppelgänger]] 50.4%, [[ogre-zombie|Ogre Zombie]] 51.6%, [[pirate-captain|Pirate Captain]] 52.1%, [[weretiger|weretiger]] 53.6%, [[black-pudding|Black Pudding]] 55.0% `[simulated]`. No answer for: flying enemies out of reach, dragons, social combat.

Amplifies: any darkness (advantage engine works alone). Depends on: dim light/darkness for peak output, allies on the front line (mid-tier AC/HP). Observed: ceiling scout then ambush attack, the party's surprise opener.

## Session Combat Log

| Session | Encounter | Rounds | Dmg dealt | Dmg taken | Hits/attacks | Key moments |
|---|---|---|---|---|---|---|
| 04 | Sewer patrol Grung (ambush from ceiling) | 1 | ~24 | 0 | `[unknown]` | Dread Strike instant kill on patrol Grung |
| 04 | Powder-ship demolition | 1 | n/a (mission goal) | 0 | 1/1 | Fire arrow into 8 barrels, ship destroyed |
| 06 | Primary Chamber fight ([[ozzeth-the-twiceborn\|Ozzeth]]) | `[unknown]` | 13 (bow, finishing shot) | 0 noted | 1/1 (17 to hit) | Re-cast Hunter's Mark on Ozzeth, finished him with a 17-to-hit bow shot for 13 piercing/force after Delmar shot his arm off. His Bardic-Inspiration-boosted save (nat 19+inspiration=20) resisted Ozzeth's [[dominate-person\|Dominate Person]] on Delmar. Leveled up to Ranger 5 |

## Calibration

Simulated-vs-observed delta: sim's steady ~7.5-vs-current-14.97 DPR vs observed 24-damage round-1 ambush spike (S04) and confirmed 13-damage finishing shot (S06) — Dread Ambusher plus surprise is his real shape; sustained lane undercounts the opener, overcounts staying power. Design implication: performs at max only in darkness with an unbroken Mark; strip that away to pressure him. Confidence: `theoretical` across the board until a real sheet lands; session-04/06 narrative evidence `[low]`. Unsimulable: whatever "Tongue Lash" his Arc Note names (unconfirmed), actual spells prepared, real ability scores.
