# Aruhe Guardian Defense Stack Audit

## Current Defenses
- **AC:** 18
- **HP:** 200
- **Damage Resistances:** Bludgeoning, Piercing, Slashing
- **Regeneration:** 10 HP/round
- **Save Bonuses:** +9 to all saves
- **Mobility:** 30 ft. teleport

---

## Stack Analysis

### 1. AC 18 Effectiveness
**Status:** HIGH — Within range for a guardian creature
- AC 18 is appropriate for a magical or heavily armored guardian
- Requires +7 to-hit to reach 50% accuracy (typical for mid-tier monsters)
- Synergizes well with regeneration (forces repeated hits to overcome healing)

### 2. HP 200 with Regeneration 10
**Status:** DANGEROUS SYNERGY — Potential balance issue
- **Effective HP vs. non-magical damage:** ~300+ (10 HP regen per round before first damage applied)
- **Problem:** Without ability to stop regeneration (fire damage, necrotic, etc.), creatures dealing <10 DPS cannot harm it
- **Recommendation:** Ensure regeneration has conditions that disable it (e.g., stops if takes fire or necrotic damage in single turn, or if reduced to 0 HP by specific damage types)
- **Math check:** At 200 HP, combats extend 20+ rounds unless enemies deal >10 DPS

### 3. Resistance to B/P/S
**Status:** STRONG with regen, PROBLEMATIC stack element
- **Effective damage reduction:** 50% against most melee attacks
- **Interaction:** Combined with +9 saves and AC 18, guardian takes 25% effective damage from typical attacks
- **Issue:** This creates a "trinity of defense" that may be too difficult to overcome for martial-focused parties
- **Recommendation:** Consider limiting to two of: {high AC, B/P/S resistance, regen 10}

### 4. +9 to All Saves
**Status:** EXTREMELY HIGH
- **Problem:** This is typically reserved for legendary creatures or high-CR beings
- **Context:** A +9 bonus means DC 16-17 saves become 50/50, DC 13-14 becomes near-impossible to affect
- **Interaction:** Significantly reduces spell and ability effectiveness
- **Recommendation:** Differentiate saves (e.g., +9 STR/WIS, +5 DEX/INT/CHA) to allow tactical vulnerabilities

### 5. 30 ft. Teleport
**Status:** STRONG EVASION tool
- **Synergy issue:** Allows escape from grapple, difficult terrain, and opportunity attacks
- **Combines poorly with:** AC 18 + regen + high saves (becomes nearly unkillable AND mobile)
- **Recommendation:** Add conditions (e.g., "once per turn," requires line of sight, or only when damaged)

---

## Stack Issues Summary

| Issue | Severity | Impact |
|-------|----------|--------|
| Regen has no disable condition | **CRITICAL** | Infinite durability vs. common damage types |
| +9 all saves too high | **HIGH** | Trivializes spell-based encounters |
| B/P/S + AC 18 + regen triple-stack | **HIGH** | Only 25% effective damage from attacks |
| Unrestricted 30 ft. teleport | **MEDIUM** | Bypasses positioning strategies |
| No defined stat weaknesses | **MEDIUM** | No tactical entry point for players |

---

## Recommended Fixes

### Fix 1: Conditional Regeneration (Choose One)
**Option A:** Regeneration stops if guardian takes fire or necrotic damage in a single turn
```
Regeneration. The guardian regains 10 HP at the start of its turn if it has at least 1 HP. If the guardian takes fire or necrotic damage, its regeneration doesn't function until the end of its next turn.
```

**Option B:** Regeneration stops at 0 HP (magic-only reanimation)
```
Regeneration. The guardian regains 10 HP at the start of its turn if it has at least 1 HP, but not above half its maximum. Regeneration stops if the guardian is reduced to 0 HP and doesn't automatically restart.
```

### Fix 2: Differentiate Saves
Replace +9 all saves with:
- **Strength, Wisdom:** +9 (primary defensive saves)
- **Dexterity, Intelligence, Charisma:** +4 or +5 (tactical weaknesses)

This preserves the "guardian" feel while allowing control spells and mental effects.

### Fix 3: Restrict Teleport
Add one condition:
- "once per turn" (classic restriction)
- "only if it can see the destination" (removes blind teleporting)
- "only within 30 ft. of its starting position" (keeps it zoned)

### Fix 4: Reduce Resistance Stack
Choose one modification:
- **Option A:** Remove resistance to slashing (keep B/P for "guardian" flavor)
- **Option B:** Reduce resistance to immunity to one type, vulnerability to another (e.g., "immune to bludgeoning, vulnerable to fire")
- **Option C:** Change "resistance" to "has advantage on saves against spells" (keeps flavor, reduces damage stack)

---

## Revised Defensive Profile (Balanced)

**Conservative Build:**
- AC 18 (unchanged)
- HP 200 (unchanged)
- Resistance: Bludgeoning & Piercing only (removed slashing)
- Regeneration 10 (stops if takes fire/necrotic damage)
- Saves: STR +9, WIS +9, DEX +5, INT +4, CHA +4
- Teleport: 30 ft., once per turn, line of sight required

**Aggressive Build (if CR is justified high):**
- AC 18 (unchanged)
- HP 200 (unchanged)
- Resistance: B/P/S (unchanged)
- Regeneration 10 (stops if reduced to 0 HP)
- Saves: All +9 (unchanged)
- Teleport: 30 ft., once per turn, line of sight required

---

## Estimated CR Impact

| Configuration | Estimated CR | Viable Against |
|---|---|---|
| Current (unfixed) | 15+ | Parties level 12+ |
| Conservative fix | 11-12 | Parties level 9-10 |
| Aggressive fix | 13-14 | Parties level 11-12 |

---

## Summary

The guardian's defensive stack is **overloaded**. The combination of AC 18, regeneration 10, full B/P/S resistance, +9 saves, and unrestricted teleport creates a creature that is effectively unkillable by most parties. The **critical issue** is regeneration without a clear disable condition—it must have a trigger (fire/necrotic damage, or damage type immunity).

**Immediate action:** Add a disable condition to regeneration and differentiate saves to create tactical vulnerabilities.
