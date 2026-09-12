---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-03"
updated: "2026-08-10"
tags: [craft]
summary: "W120 section-count-outlier findings: what the neighbour comparison means and how to fix a firing page."
uid: 22153897-d8df-4654-9d89-9c0c55c65f77
---

# W120 — Section-count outlier

Protects: `vault/refs/qc-wiki-page.md`'s ONE-FACT-ONE-PAGE
contract, mechanically. A page whose H2 section count runs far past its
`type:` siblings' is probably several distinct entities or topics wedged
onto one page instead of split into linked atomic pages. Advisory
(docs/adr/0024): the comparison is a heuristic against real siblings, not a
correctness rule, so it is reported but never blocks an edit or a commit.
`fixable: false` — the split itself is a judgment call, not a mechanical
transform.

## Fix

Read the firing page and decide, per section, whether it names a distinct
entity/topic that deserves its own page. For each one: instantiate the
matching template from `vault/_templates/`, move that section's content there,
and replace it on the original page with a `[[wikilink]]` (or
`![[page#Heading]]` transclusion if the operative content still needs to
render inline). Sections that are genuinely one topic explored in depth —
not several topics — are a false positive: leave the page as-is, the
finding is advisory and does not need silencing.

## Edge cases

- Below `ATOMICITY_MIN_SIBLINGS` same-`type` pages in the corpus, the rule
  stays silent — a cohort that thin has no meaningful median/p90 to compare
  against (`wiki.toml` `[thresholds]`).
- Below `ATOMICITY_SECTION_FLOOR` H2 sections, the rule stays silent
  regardless of siblings — a small page is never "several entities wedged
  together."
- Exempt outright: `vault/dashboards/**`,
  `vault/refs/tables/**` (one section per rollable table by design), any
  path matching `transcript` (one section per speaker turn/part by
  design), and the derived-data `pc-*`/`party-combat-profile` types
  (generated data, no authored sections to split).
- A heading inside a fenced code block (a statblock, a shell example) is
  never counted as a section.
