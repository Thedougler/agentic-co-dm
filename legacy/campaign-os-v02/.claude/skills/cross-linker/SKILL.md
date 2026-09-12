---
name: cross-linker
description: >
  Resolve a W25 or W122 finding — prose that names an established page or alias but never
  wikilinks it — in a Campaign OS repo (vault/ present). Use when the user says "link my pages",
  "find missing links", or "add wikilinks", or after llm-wiki-lint reports a W25/W122 finding.
  Mechanical, zero judgment call: every detected finding gets linked.
---

# cross-linker

Resolves W25 and W122 findings. The CLI detector
(`wiki_cli/rules/unlinked_mention.py` for `vault/` and
`vault/campaigns/shattered-sea/pcs/`,
`narrative_unlinked_mention.py` for `vault/stories/`+`vault/ideas/` — same
detection engine, both warning-severity and gating) already decided what
counts as a real mention — the regex, capitalization, and
stoplist/allowlist gates in `scan_unlinked_mentions` are the one place
that judgment call gets made. By the time a finding reaches this skill,
it is a fact: prose names
a resolvable page and never links it. This skill's own job is purely
mechanical — apply the fix, identically for both rules. Never restate
either rule's wording here — read `unlinked_mention.py`'s and
`narrative_unlinked_mention.py`'s own module docstrings for both.

**No narrative or literary judgment.** "Does this really refer to the
target page, or is it just flavor text / an ordinary word / incidental
description?" is never asked here — the detector already decided that. A
deer described walking through a clearing IS the entity the deer statblock
page represents; a spell name naming a moment of quiet IS a mention of
that page, mechanically true regardless of whether the scene depicts the
spell being cast. The **sole** skip/report case is genuine RESOLUTION
ambiguity — the matched name resolves to 2+ different candidate target
pages in the vault index, a checkable fact, not a taste call.

## Standard queries

```
# Whole-repo candidate list (W25 + W122)
node_modules/.bin/markdownlint-obsidian --output-formatter json \
  | jq '.[] | select(.errors[]?.ruleCode == "unlinked-entity-mention" or .errors[]?.ruleCode == "narrative-unlinked-mention")'

# One page only
node_modules/.bin/markdownlint-obsidian <path> --output-formatter json
```

Each finding names the source page, line, the matched name, and its
target page.

## Owned write scope

Narrow and explicit — this skill never does anything else to a page:

- Wrap an already-detected mention in `[[target|display]]`, at its first
  natural occurrence only (never every occurrence on the page — W25/W122
  fire once per target page per source page, by design). `display` is the
  prose exactly as written — copy the matched span verbatim, never
  retitle, recase, or expand it to the target page's own title/alias.
- A table cell holding a full sentence (a Toy Method field, a relationship
  row) still counts as natural prose — wrap inline, matching how existing
  links already on that page are written (escaped `\|` inside a table
  cell). Only a bare label or list item with no sentence structure at all
  routes to `## Related` instead (create the section if absent; append to
  it if present, never duplicate an existing entry).
- Never any other prose change, never a `status`/`publish` frontmatter
  flip, never a fact invented or altered.

## Workflow

1. **Get the candidate list** (Standard queries above). `CL1: <finding
   count, or 0 — clean>`.
2. **Read the actual sentence around each finding** to locate the exact
   span to wrap and pick a Standard-queries-correct target slug — never to
   judge whether the mention is "real." Check the vault index for the
   matched name: 2+ distinct candidate pages → genuine resolution ambiguity,
   report it (Workflow step 4/7). One candidate (the normal case, already
   confirmed by the detector) → it links, full stop. `CL2: <resolution
   ambiguities found, or none>`.
3. **Check the source page's `status`.** Any status — `pending`, `canon`,
   `retired` — applies the fix the same way; canon status never excuses a
   page from the lint table. `CL3: <applied vs reported, by status>`.
4. **Apply** — inline wikilink or `## Related`, per Owned write scope, to
   every finding except a genuine resolution ambiguity (name resolves to
   2+ candidate pages) → report that one, don't guess (W25/W122's own FIX
   line). `CL4: <links applied, or N/A — report-only run>`.
5. **Lint before done** — re-run the Standard query on every page touched;
   confirm zero new findings (a wikilink insertion shouldn't create a
   W3/W9 problem, but check). `CL5: <clean, or NOTED>`.
6. **Report.** Links added (page → target), pages reported instead of
   applied (canon-gated or resolution-ambiguous) and why. `CL6: <report
   given>`.

## Canon pages — no gate, but the same discipline

No hook blocks an edit to a `status: canon`/`retired` page. That makes this
skill's own discipline the only thing keeping a W25/W122 fix mechanical
(W122 gates the same way W25 does — both are warning-severity):

**Out of bounds, always:**
- Any prose change beyond wrapping an already-detected mention or adding
  to `## Related` (Owned write scope is exhaustive)
- Flipping `status`, `publish`, or any other frontmatter key — INGEST's,
  canon-review's, and PUBLISH's exclusive verbs, not this skill's
- Skipping a finding on narrative/literary grounds ("just flavor text",
  "an ordinary word here") — not a real skip case; see the top-level No
  narrative or literary judgment note
- Guessing which target to link when a match is genuinely ambiguous — still
  routes to Workflow step 4/7

**Red flags — stop and report instead of applying the fix:**
- The fix would touch anything outside Owned write scope
- The match is genuinely resolution-ambiguous (2+ candidate targets in the
  vault index)
- Citing a document or rule name to justify a wider edit without having
  actually opened and confirmed it exists and says what you think it says

## Degrade by asking

- A finding resolves to 2+ candidate target pages in the vault index (true
  resolution ambiguity, not a content/intent judgment) → report it, don't
  guess (Workflow step 4).
- A W25 fix on a canon page that can't stay inside Owned write scope (the
  mention needs a rename, a merge, or a ruling to link correctly) → that
  routes through this repo's normal canon-editing convention (a ledger
  line, or `canon-review`), never a standing exception carved out for
  this skill.

## Relationship to other skills

- **`utils/wiki-cli/src/wiki_cli/rules/unlinked_mention.py`** and
  **`narrative_unlinked_mention.py`** — W25's and W122's rule and FIX
  wording; never restated here.
- **`llm-wiki-lint`** — runs the W-table at scale and surfaces W25/W122
  findings; hands them here to resolve, the same way it hands W9/W16/W17/
  W18 to `canon-review`. `llm-wiki-lint` itself never inserts a link.
- **`canon-review`** — owns any actual entity-merge or contradiction
  judgment call; a W25/W122 finding is never one of those (it's "these two
  already-distinct pages should reference each other," not "are these the
  same page").
- **`llm-wiki-ingest`**, **`transcript-ingest`** — each already adds its
  own reciprocal wikilink for the one citation it just wrote; this skill
  is the broader sweep for what those single-claim links miss, run
  afterward, not a replacement for either.
