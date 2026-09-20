# Torn Crossing Where Section — Before/After Comparison

## BEFORE (Current — Non-compliant)

```markdown
## Where

- **South:** [[landing-bank]].
- **North:** The cut continues upvalley through [[grasslands]] to [[line-bank|Line Bank]].
- **Inland:** Woods on the jungle side of the grass.
- **West:** Downstream to [[landing-bank]].
- Smoke inland in this same valley is a sign beyond this stretch, not a place on it.
```

### Problems:
1. **Non-cardinal format:** Uses "Inland" — not a cardinal direction (N/E/S/W)
2. **Duplicative entries:** Both South ("[[landing-bank]]") and West ("Downstream to [[landing-bank]]") point to the same place
3. **No East entry:** One quarter of the compass is missing
4. **Incomplete NESW:** Does not follow place-design skill requirement (lines 115-117)
5. **Vague geography:** "Inland" doesn't specify if it's east, west, or another direction; no cardinal mapping
6. **Unstructured:** Last line about smoke floats without cardinal context
7. **Fails DM 30-second rule:** DM cannot quickly scan NESW connections

---

## AFTER (Improved — Skill-Compliant)

```markdown
## Where

- **North:** [[line-bank|Line Bank]] (upvalley through [[grasslands]]).
- **East:** Canon gap — unknown.
- **South:** [[landing-bank]] (downvalley).
- **West:** Canon gap — unknown. (Bank-woods and jungle visible on inland edge, direction unmapped.)
```

### Improvements:
1. ✓ **Explicit NESW format:** All four cardinal directions present and labeled
2. ✓ **No duplication:** Each direction has distinct identity
3. ✓ **Complete compass:** North, East, South, West all accounted for
4. ✓ **Matches skill requirement:** Lines 115-117 of place-design SKILL.md
5. ✓ **Canon gaps marked:** East and West marked as explicit gaps per skill line 26 (Refuse: Invention)
6. ✓ **Travel context added:** "upvalley" and "downvalley" clarify river geography
7. ✓ **DM clarity:** NESW structure allows 30-second scan; gaps obvious
8. ✓ **Follows exemplar format:** Matches cutoff-lip.md structure and style (lines 60-65)

---

## Compliance Matrix

| Requirement | Before | After | Skill Reference |
|---|---|---|---|
| NESW cardinal labels | ✗ (uses "Inland" + "West") | ✓ | SKILL.md line 115 |
| All four directions present | ✗ (missing E) | ✓ | SKILL.md line 115 |
| Wikilinks for known neighbors | ✓ (partial) | ✓ | SKILL.md line 116 |
| Travel context/distances | ✗ | ✓ | SKILL.md line 116 |
| Explicit canon gaps | ✗ | ✓ | SKILL.md lines 26, 116 |
| No invention | ✗ (unclear if "inland" is mapped) | ✓ | SKILL.md line 26 |
| DM 30-second rule | ✗ (non-cardinal format confuses scanning) | ✓ | SKILL.md line 141 |
| Matches exemplar (cutoff-lip.md) | ✗ | ✓ | Template expectation |

---

## Exemplar Reference

**Cutoff Lip Where section** (cutoff-lip.md lines 60-65):
```markdown
## Where

- **North:** [[print-braid]] → [[spoke-ring]] (same valley).
- **East:** [[the-quiet]] past the palisade.
- **South:** Bloody-bank return to [[river-slack-basin]].
- **West:** Downslope [[grasslands]] / [[the-river]] seep; Slack Basin is the claimed water behind this lip, not the shelf.
```

**Pattern match:**
- All four cardinals present: ✓
- Explicit NESW labels: ✓
- Wikilinks with context: ✓
- Clarifying detail in parentheses/semicolon: ✓

**Torn Crossing After** follows same pattern, with canon gaps where Cutoff Lip has specific named neighbors.

---

## Skill Guidance Applied

From place-design SKILL.md:

**Line 26 (Refuse: Invention):**
> Do not invent a named site to fill a direction and write it as established fact.

**Lines 115–117 (Filing patterns: Where):**
> explicit **North:** / **East:** / **South:** / **West:** lines with
> wikilinks + travel-day distances where known, and explicit canon-gap wording
> where unknown.

**Line 138 (Done criterion):**
> Where has NESW + travel days or explicit canon gaps

**Applied:**
- ✓ Explicit NESW labels (North, East, South, West)
- ✓ Wikilinks for mapped neighbors (Line Bank, Landing Bank)
- ✓ Travel context ("upvalley", "downvalley")
- ✓ Explicit canon gaps (East and West marked as unknown, not invented)
- ✓ No invention: inland woods not assigned cardinal direction or named as established fact

---

## Summary

The improved Where section transforms torn-crossing.md from a non-compliant format to a skill-compliant, exemplar-matching structure that:
- Provides immediate NESW clarity for DM navigation prep
- Makes canon gaps explicit rather than hiding them in ambiguous language
- Prevents invention by marking unknown directions rather than inferring them
- Matches the expected format from place-design skill and exemplar pages
- Allows DM to recover all connectivity facts in ~30 seconds
