# EVAL_AUTHOR_FLAGS — city-design Batch A re-run (post-#138)

Flags from grading + analyst pass. Soft lint / vault completeness correctly out of scope.

## Discriminating (keep)

- **Resist-invent plague/siege as canon** (eval-2): strongest discriminator (1.0 vs 0.0). Keep hostile prompt wording.
- **Closed S1 thread must stay closed** (eval-1 content + If-nobody-intervenes): catches baseline rewriting bombs into live plague.
- **invention: true on from-scratch** (eval-3): baseline often omits; keep.
- **kind: settlement → kind: city upgrade** (eval-4): baseline failed; keep explicit.
- **Identity sentence / work gate** (process): discriminate well when process-notes.md is required evidence. Document that graders must read process-notes, not only the page file.

## Non-discriminating / soft

- **Template structure headings present** (evals 1,3,4): both configs often pass if the template file is visible in-repo. Still useful as a floor assertion, but alone does not prove skill adherence. Consider requiring specific subsection content (e.g. Orientation districts table with ≥2 rows) for sharper discrimination.
- **Frontmatter type:place kind:city** on improve/from-scratch (eval-1, eval-3): weak discriminator when the prompt names `wiki/templates/city.md` — baseline can copy frontmatter without the skill. Pair with process/guardrail assertions (already done).

## Flaky / evidence-dependent

- **Identity sentence appears before the page draft**: fails if executor forgets `process-notes.md` even when skill was followed. Not flaky given notes requirement, but **assertion text should cite process-notes (or transcript) as the evidence locus** so future graders do not hunt the page file.
- **Shows a chat proposal / work gate before writing under wiki/**: same — needs process artifact. Also ambiguous if workspace-only writes count as "writing under wiki/" (they must not). Clarifying assertion: "chat proposal before any live `wiki/` path write; workspace outputs allowed."

## Bad / strengthen

- Eval-1 assertion *DM thesis is one sentence about the city's function in play* can pass weak theses that are still one sentence. Consider requiring pressure-forward / no-live-crisis framing for Mercatura specifically, or a negative check ("not a Season-1 history summary").
- Eval-3 *Arrival without secrets* is good; baseline failure mode (secret vault + knows party names) is clear. No change needed.
- Eval-4 content preservation assertion is long/compound (Dravosi + Houses + Paludi + Warren + Simone/Lavinia). Prefer splitting into 2–3 assertions so a partial miss does not all-or-nothing the grade — or keep compound but document that **any** major omission fails.

## Retarget note (post-#138)

- Improve target is **Mercatura** (kind:city); flesh target is **calven-and-calveno** (settlement→city). Do not grade live Mercatura stub completeness; grade output template conformance only.
- No invented lore filed as live wiki pages in this run (workspace `*/outputs/` only).
