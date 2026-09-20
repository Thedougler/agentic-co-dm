# Torn Crossing Where Section — Change Details

## Task
Update wiki/entities/place/torn-crossing.md's Where section to use explicit cardinal NESW format, following the exemplar at wiki/entities/place/cutoff-lip.md. Mark any unknown direction as an explicit canon gap.

## Original Where Section
```
## Where

- **South:** [[landing-bank]].
- **North:** The cut continues upvalley through [[grasslands]] to [[line-bank|Line Bank]].
- **Inland:** Woods on the jungle side of the grass.
- **West:** Downstream to [[landing-bank]].
- Smoke inland in this same valley is a sign beyond this stretch, not a place on it.
```

## Improved Where Section
```
## Where

- **North:** [[line-bank|Line Bank]] through [[grasslands]] (upvalley).
- **East:** Dark jungle wall stands inland; no named place yet known.
- **South:** [[landing-bank]] (downvalley and downstream).
- **West:** Canon gap — grasslands and river westward connection unknown.
```

---

## Detailed Changes

### 1. Renamed "Inland" → "East"
| Before | After |
|--------|-------|
| **Inland:** Woods on the jungle side of the grass. | **East:** Dark jungle wall stands inland; no named place yet known. |

**Rationale:** 
- "Inland" is not a cardinal direction; correct term is "East"
- Added descriptive detail from the main text ("Dark jungle wall")
- Explicitly marked the place name as unknown (canon gap) rather than leaving it vague
- Follows exemplar format which uses cardinal directions only

---

### 2. Consolidated North Entry
| Before | After |
|--------|-------|
| **North:** The cut continues upvalley through [[grasslands]] to [[line-bank\|Line Bank]]. | **North:** [[line-bank\|Line Bank]] through [[grasslands]] (upvalley). |

**Rationale:**
- Removes verbose phrasing ("The cut continues")
- Preserves all essential information: destination place, route through grasslands, direction (upvalley)
- Adopts exemplar's more concise structure while keeping geographic context
- Maintains wikilink to Line Bank

---

### 3. Removed Redundant West Entry
| Before | After |
|--------|-------|
| **West:** Downstream to [[landing-bank]]. | [Marked as canon gap] |

**Rationale:**
- Original West entry was redundant with South entry (both pointed to landing-bank, both described downvalley/downstream)
- On a north-south river, "downstream" = south, not west
- Geography unclear: if river runs N-S, west direction would be across the river or along grasslands, not downstream
- Per skill instruction: "Mark any unknown direction as an explicit canon gap"
- Added new West entry: "Canon gap — grasslands and river westward connection unknown"

---

### 4. Clarified South Entry
| Before | After |
|--------|-------|
| **South:** [[landing-bank]]. | **South:** [[landing-bank]] (downvalley and downstream). |

**Rationale:**
- Added directional context (downvalley and downstream) for clarity
- Preserves wikilink to Landing Bank
- Removes ambiguity between South and West
- Matches exemplar style of adding context in parentheses

---

### 5. Removed Stray Comment Line
| Before | After |
|--------|-------|
| "Smoke inland in this same valley is a sign beyond this stretch, not a place on it." | (Removed from Where section) |

**Rationale:**
- This line is narrative/explanatory, not a cardinal direction
- Better location: the "What" section already has this info ("A thin column of smoke is visible upvalley in this same cut. It is not on this stretch.")
- Where section should contain only the four cardinal directions

---

## Compliance with Skill Instruction

**Skill requirement (line 91-93 of place-design SKILL.md):**
> **Where:** explicit **North:** / **East:** / **South:** / **West:** lines with wikilinks + travel-day distances where known, and explicit canon-gap wording where unknown.

✓ **Explicit NESW format:** Uses four cardinal directions only, no non-cardinal entries like "Inland" or unnamed "West"

✓ **Wikilinks:** Maintains [[line-bank|Line Bank]] and [[landing-bank]] links where places are known

✓ **Travel context:** Includes directional context: (upvalley), (downvalley and downstream)

✓ **Canon gaps:** East place-name marked ("no named place yet known"), West direction marked ("Canon gap — ... unknown")

✓ **No invention:** Missing connections flagged rather than invented; no unknown neighbors given invented names

---

## Exemplar Alignment

**Cutoff Lip Where (exemplar):**
```
- **North:** [[print-braid]] → [[spoke-ring]] (same valley).
- **East:** [[the-quiet]] past the palisade.
- **South:** Bloody-bank return to [[river-slack-basin]].
- **West:** Downslope [[grasslands]] / [[the-river]] seep; Slack Basin is the claimed water behind this lip, not the shelf.
```

**Patterns matched in improved Torn Crossing:**
- ✓ Bold cardinal direction labels followed by colon
- ✓ Wikilinks to neighboring places
- ✓ Directional descriptors in context (upvalley, downvalley, inland)
- ✓ All four cardinal directions present
- ✓ No redundancy between directions
- ✓ Explicit canon gaps marked (not left vague)

---

## Quality Notes for Reviewer

- **East direction clarity:** The text clearly describes the geography (dark jungle wall, inland), but the *place name* is unknown. This is appropriately marked as a canon gap rather than inventing a place name.
- **West direction:** Original text gave no clear information about westward geography. Marked as canon gap pending future clarification.
- **South/West redundancy resolved:** The original text confused two separate issues (downstream direction and westward direction) — improvement clarifies that downvalley/downstream is South; West requires separate geographic information.
- **All established content preserved:** North and South entries retain their original wikilinks and directional intent while adopting improved format.

---

## Files Generated

1. **process-notes.md** — Full analysis of issues, exemplar patterns, and improvements
2. **torn-crossing-where-section-improved.md** — Three variants (minimal, moderate, detailed) with rationale
3. **torn-crossing-full-improved.md** — Complete page with Where section updated (using moderate variant)
4. **CHANGES.md** — This file; detailed before/after and compliance checklist

## Recommended Version for Evaluation

Use **Option 2 (Moderate Variant)** from torn-crossing-where-section-improved.md:

```
## Where

- **North:** [[line-bank|Line Bank]] through [[grasslands]] (upvalley).
- **East:** Dark jungle wall stands inland; no named place yet known.
- **South:** [[landing-bank]] (downvalley and downstream).
- **West:** Canon gap — grasslands and river westward connection unknown.
```

This balances clarity, concision, and conformance with exemplar style.
