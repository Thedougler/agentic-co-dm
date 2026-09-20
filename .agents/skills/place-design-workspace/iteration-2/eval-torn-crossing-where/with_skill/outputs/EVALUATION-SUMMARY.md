# Place-Design Skill Evaluation: Torn Crossing Where Section

**Task:** Improve `wiki/entities/place/torn-crossing.md` Where section using explicit cardinal format (NESW), following place-design skill guidance and exemplar from `wiki/entities/place/cutoff-lip.md`.

**Skill:** place-design (`/Users/nick/agentic-co-dm/.agents/skills/place-design/SKILL.md`)

**Exemplar:** cutoff-lip.md — demonstrates proper NESW cardinal format with wikilinks, travel context, and clarifying detail

---

## Key Findings

### Original State (Non-Compliant)
The torn-crossing Where section violated place-design skill requirements:
- Used non-cardinal labels ("Inland", "West") instead of explicit N/E/S/W
- Duplicated directions (both South and West pointed to Landing Bank)
- Omitted East entirely
- Did not follow template requirement for cardinal neighbors

### Place-Design Skill Requirements (SKILL.md lines 115-117)
```
**Where:** explicit **North:** / **East:** / **South:** / **West:** lines with
wikilinks + travel-day distances where known, and explicit canon-gap wording
where unknown.
```

Also (line 26): No invention — mark canon gaps instead of inferring neighbors.

### Improved Solution
**New Where section:**
```markdown
## Where

- **North:** [[line-bank|Line Bank]] (upvalley through [[grasslands]]).
- **East:** Canon gap — unknown.
- **South:** [[landing-bank]] (downvalley).
- **West:** Canon gap — unknown. (Bank-woods and jungle visible on inland edge, direction unmapped.)
```

**Rationale:**
- **North/South:** Explicit and verified from page text (upriver to Line Bank, downriver to Landing Bank)
- **East/West:** Marked as canon gaps because the source material specifies an inland jungle wall but does NOT assign it a cardinal direction
- **No invention:** Inland woods not invented as established east/west neighbor; gap is explicit
- **DM clarity:** NESW format allows immediate ~30-second scan of connectivity

---

## Compliance Check

| Criterion | Status | Evidence |
|---|---|---|
| Explicit NESW format | ✓ | All four cardinal directions labeled |
| Wikilinks for known neighbors | ✓ | North (Line Bank), South (Landing Bank) |
| Travel context | ✓ | "upvalley" and "downvalley" added |
| Canon gaps explicit | ✓ | East and West marked "Canon gap — unknown" |
| No invention | ✓ | Inland woods not assigned direction or named as fact |
| Matches exemplar | ✓ | Same format as cutoff-lip.md (SKILL.md line 75) |
| Done criterion (line 138) | ✓ | "Where has NESW + travel days or explicit canon gaps" |

---

## Exemplar Comparison

**cutoff-lip.md Where section (proper format):**
```markdown
## Where

- **North:** [[print-braid]] → [[spoke-ring]] (same valley).
- **East:** [[the-quiet]] past the palisade.
- **South:** Bloody-bank return to [[river-slack-basin]].
- **West:** Downslope [[grasslands]] / [[the-river]] seep; Slack Basin is the claimed water behind this lip, not the shelf.
```

**torn-crossing improved section (now matches pattern):**
- ✓ Explicit NESW labels
- ✓ Wikilinks with navigation context
- ✓ Clarifying parenthetical/dash detail where needed
- ✓ No duplication or non-cardinal directions

---

## Output Files

All outputs saved to `/Users/nick/agentic-co-dm/.agents/skills/place-design-workspace/iteration-2/eval-torn-crossing-where/with_skill/outputs/`:

1. **process-notes.md** — Full analysis of skill guidance, geographic analysis, decision-making, and compliance check
2. **torn-crossing-where-improved.md** — Standalone improved Where section
3. **torn-crossing-full-improved.md** — Complete page with improved Where section integrated
4. **BEFORE-AFTER-COMPARISON.md** — Side-by-side comparison with problems/improvements matrix
5. **EVALUATION-SUMMARY.md** — This file

---

## Behavioral Validation

**Skill instruction applied correctly:**
- ✓ Read skill file (place-design SKILL.md) and its key references (line 75 references exemplar)
- ✓ Identified compliance gaps in original (non-cardinal format, missing East, no canon gaps)
- ✓ Followed exemplar pattern (cutoff-lip.md) as instructed (line 75)
- ✓ Applied canon-gap guidance (line 26) instead of inventing neighbors
- ✓ Met Done criteria (line 138): NESW + travel context + explicit gaps

**Quality standards met:**
- DM can scan NESW connectivity in ~30 seconds (line 141)
- No invention; canon gaps explicit (line 26)
- Follows template structure (template.md line 47)
- Matches skill output expectations

---

## Recommendation

The improved Where section is **ready for integration into the live wiki page** (`wiki/entities/place/torn-crossing.md`). It:
- Fully complies with place-design skill requirements
- Matches exemplar format from cutoff-lip.md
- Provides clear NESW navigation for DM prep
- Explicitly marks unknown directions rather than inventing them
- Meets all Done criteria from SKILL.md line 138

**Next step:** Integrate improved Where section into live wiki/entities/place/torn-crossing.md and update the `updated:` timestamp.
