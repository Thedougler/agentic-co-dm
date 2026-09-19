# EVAL_AUTHOR_FLAGS — place-design iteration 1 (Batch A post-#138)

Flags for **non-discriminating craft assertions** (pass under both `with_skill` and `without_skill`), plus related author notes.

## Non-discriminating (craft / structure)

### eval-14-file-a-wilderness-location

1. **Includes all four cardinal directions in the filed Where section**  
   - Both configs emitted North/East/South/West. Baseline still invents the southern neighbor as fact, so the *cardinal presence* check does not measure skill value.  
   - **Suggestion:** Require cardinals *and* gap-or-wikilink discipline in the same assertion, or keep cardinals as structure-only and rely on the existing southern-gap guardrail (which *does* discriminate).

2. **Names known neighbors as wikilinks and gives approximate travel-day distances rather than precise mileage math**  
   - Baseline can satisfy weak wikilink+days patterns while still inventing south.  
   - **Suggestion:** Assert that *only* the three known neighbors are wikilinked and that south has neither a wikilink nor a proper name.

3. **Output follows wiki/templates/place.md Where conventions**  
   - Presence of a `## Where` heading + "North" passes too easily.  
   - **Suggestion:** Pin conventions to explicit `**North:**` / `**East:**` / `**South:**` / `**West:**` lines with `~N days of travel` language and gap wording.

### eval-10-write-four-location-moves (grader note → author note)

4. **Moves alter routes, relationships, resources, information, or rules of access**  
   - On this run the naive grader false-positived when the baseline *mentioned* routes/relationships in a negation ("No lasting change to routes…"). Corrected to fail for without_skill.  
   - Still at risk of non-discrimination if a weak baseline lists "routes change" without actor/trigger/consequence fields.  
   - **Suggestion:** Require the five-part move shape (actor, trigger, visible result, new opportunity, lasting consequence) per move, not keyword hits.

## Discriminating craft assertions (no flag)

Craft evals **5–9** and **11–13** assertions all discriminated on this iteration (with_skill pass, without_skill fail) against lore-only / single-solution / ability-negating / reset-state baselines. Keep as-is unless future baselines improve enough to collapse the gap.

## Process / wiki evals (context)

Evals **1–4** process and guardrail assertions discriminate as intended (kernel, work gate, invention labels, resist-invent). Content/structure on improve/flesh still partially pass without the skill when the live page + template are strong — expected; not craft-author flags.
