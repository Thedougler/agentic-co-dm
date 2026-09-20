# Torn Crossing Where Section Evaluation — Process Notes

## Task
Improve `wiki/entities/place/torn-crossing.md` Where section to use explicit cardinal format (NESW) with wikilinks and travel context, following place-design skill guidance and exemplar from `wiki/entities/place/cutoff-lip.md`.

## Skill Guidance (place-design SKILL.md lines 115-117)
> **Where:** explicit **North:** / **East:** / **South:** / **West:** lines with
> wikilinks + travel-day distances where known, and explicit canon-gap wording
> where unknown.

Also at line 26 (Refuse gates):
> **Canon gaps.** Missing cardinal neighbors stay explicit gaps. Do not invent a
> named site to fill a direction and write it as established fact.

And at line 138 (Done criteria):
> Where has NESW + travel days or explicit canon gaps

## Current State Analysis

### Current Where section (torn-crossing.md lines 61-67):
```
## Where

- **South:** [[landing-bank]].
- **North:** The cut continues upvalley through [[grasslands]] to [[line-bank|Line Bank]].
- **Inland:** Woods on the jungle side of the grass.
- **West:** Downstream to [[landing-bank]].
- Smoke inland in this same valley is a sign beyond this stretch, not a place on it.
```

### Issues Identified:
1. **Non-cardinal format:** Uses "Inland" instead of cardinal direction; West is imprecise
2. **Duplicative entries:** Both South and West point to Landing Bank (redundant)
3. **Missing East:** No East entry at all; blank direction
4. **Vague cardinal mapping:** "Inland" doesn't specify if it's E, W, NE, NW, etc.
5. **Incomplete NESW:** Template requires all four cardinal directions

### Exemplar Format (cutoff-lip.md lines 60-65):
```
## Where

- **North:** [[print-braid]] → [[spoke-ring]] (same valley).
- **East:** [[the-quiet]] past the palisade.
- **South:** Bloody-bank return to [[river-slack-basin]].
- **West:** Downslope [[grasslands]] / [[the-river]] seep; Slack Basin is the claimed water behind this lip, not the shelf.
```

**Exemplar strengths:**
- All four cardinal directions present
- Explicit NESW: formatting
- Wikilinks provided
- Travel context ("same valley", "return to", "downslope")
- Clarifying context when needed (e.g., "Slack Basin is the claimed water behind this lip, not the shelf")

## Geographic Analysis

### What torn-crossing specifies:
- **Upriver (North):** Leads to Line Bank through grasslands (explicit at line 64)
- **Downriver (South):** Leads to Landing Bank (explicit at line 63)
- **Inland direction:** "dark jungle wall," "bank-woods and jungle wall close the inland edge" — BUT cardinal direction unspecified
- **Perpendicular directions:** No explicit mapping to E/W; unclear which side is which

### What torn-crossing does NOT specify:
- Which cardinal direction is "inland" (east? west? northeast?)
- What lies on the opposite bank/perpendicular direction
- Explicit East entry
- Explicit West entry

## Decision: Mark Cardinal Gaps per Skill Guidance

Per skill line 26 (Refuse: Invention) and line 138 (Done: canon gaps):
- **Do not invent** cardinal neighbors to fill gaps
- **Mark explicitly** where direction is unknown
- The page mentions "inland woods/jungle" but does NOT specify if it's east, west, or another direction
- Best practice: Mark East and West as explicit canon gaps rather than infer/invent

## Improved Where Section

```markdown
## Where

- **North:** [[line-bank|Line Bank]] (upvalley through [[grasslands]]).
- **East:** Canon gap — unknown.
- **South:** [[landing-bank]] (downvalley).
- **West:** Canon gap — unknown. (Bank-woods and jungle visible on inland edge, direction unmapped.)
```

### Rationale:
1. **North/South:** Explicit and verified from page text
2. **East/West:** Marked as canon gaps since the page does not specify cardinal directions for inland woods or opposite bank
3. **Format:** Matches exemplar SKILL expectation (NESW + context + wikilinks where known)
4. **Invention prevention:** Does not invent named sites or directions not in source material
5. **DM clarity:** DM sees immediately which connections are mapped vs. gap

## Compliance Check Against place-design Skill

| Criterion | Status | Notes |
|---|---|---|
| Explicit NESW format | ✓ | All four cardinal directions present |
| Wikilinks for known neighbors | ✓ | North and South link to Line Bank and Landing Bank |
| Travel context | ✓ | "upvalley" and "downvalley" specify river flow direction |
| Canon gaps marked explicitly | ✓ | East and West labeled "Canon gap — unknown" |
| No invention | ✓ | Inland woods not assigned a direction; not presented as established fact |
| DM can recover facts in ~30s | ✓ | Clear NESW structure; gaps obvious |

## Files
- Input: `/Users/nick/agentic-co-dm/wiki/entities/place/torn-crossing.md` (current version, lines 61-67)
- Exemplar: `/Users/nick/agentic-co-dm/wiki/entities/place/cutoff-lip.md` (lines 60-65)
- Skill: `/Users/nick/agentic-co-dm/.agents/skills/place-design/SKILL.md`
- Output (this notes): `/Users/nick/agentic-co-dm/.agents/skills/place-design-workspace/iteration-2/eval-torn-crossing-where/with_skill/outputs/process-notes.md`
