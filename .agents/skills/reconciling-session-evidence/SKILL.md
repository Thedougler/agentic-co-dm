---
name: reconciling-session-evidence
description: >-
  Reconstruct what became true from a D&D session transcript, notes, ASR text, audio-derived
  summary, or session log, then route supported changes to their owners. Use after
  session-transcript-ingest when correcting evidence, updating a session log, reconciling PC/world
  state, or surfacing canon conflicts. Do not duplicate raw ingest or rewrite evidence.
---

# Reconcile Session Evidence
## Work gate

Wrapup. Follow `docs/agents/work.md`.

Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Reject leaves no page. Ground claims in wiki pages and/or D&D 5e rules; cite `[[pages]]`. Contradictions surface to the DM. Never present invention as wiki fact; unused prep is not canon. Outcomes remain proposed until accept, then make surgical owner-page updates.


Evidence fidelity beats prep fidelity. Raw evidence remains immutable; this skill builds a sparse,
auditable interpretation and reconciliation delta. Clear play can revise prepared material, but
unsupported summaries or ambiguous ASR readings cannot silently become canon.

## Boundary

`session-transcript-ingest` owns capture, raw files, manifest, transcript indexing, and initial
filing. Load this skill for interpretation after ingest. Agent/chat history is not campaign-play
evidence; route it to the history-ingest procedure. If several page kinds or runtime components
are affected, load `decomposing-campaign-content` after the claim ledger exists.

## Workflow

1. **Establish evidence.** Identify session boundaries, raw transcript/notes, generated summary,
   session prep/run guide, existing session log, `hot.md` at start, and directly implicated owners.
   Use exact paths/aliases first, then narrow search. Treat prep as context, never proof. A summary
   is an index of candidate claims; corroborate it or mark consequential claims `summary-only`.
2. **Normalize.** Build vocabulary from existing PC/NPC/place/faction/item/quest aliases. Normalize
   only obvious ASR errors (unique phonetic alias, punctuation, duplicate fragment, unambiguous
   speaker continuation, or clear dice notation). Keep probable/ambiguous readings as diagnostics.
   For each material correction record locator, raw, normalized, class, support, and confidence.
3. **Classify discourse.** Label state-changing segments as DM narration/adjudication, player
   declaration plus result, resolved mechanic, in-character speech, planning/speculation, rules
   talk, or OOC/joke. Assign one temporal label: `present`, `historical`, `intention`,
   `hypothetical`, or `parallel`. Only present play advances current state; a plan is not an action.
4. **Extract claims.** Verify summary claims against source spans and actor/action/object/outcome.
   Extract only durable events, elapsed time, discoveries, completed actions, NPC decisions,
   relationships, quest/front/clock changes, item transfers, durable PC changes, rulings, and
   improvised named entities. Record source span, correction, confidence, owner, and disposition.
   Clear play replaces provisional prep; locked-canon conflict is evidence plus a human gate.
5. **Reconcile state.** Load only relevant owner procedures. Keep table state at session end separate
   from lasting next-session PC/build state. Advance time only from present discourse, use weakest
   supported precision, preserve player choices, and gate protected runtime/canon promotions.
6. **Apply narrowly.** Give each claim exactly one disposition: patch owner, create justified
   template-based node, patch session log/table state, promote lasting PC fact, record ruling, propose
   gated change, or retain as evidence/diagnostic. Preserve authored prose and provenance; never
   copy transcript wording throughout the vault or hand-author derived compiler output. Route durable PC changes through `player-characters` into canonical owner sections. Preserve `lifecycle` / `reveal` / `visibility`. Do not dump satellites or invent conflict resolutions.


Run applicable link, frontmatter, and derived-state checks.

## Completion

Raw evidence is intact; corrections are traceable; uncertain readings remain uncertain; summary-only
claims are marked; OOC/speculation stays out of canon; clear improvisation is retained; every durable
claim has one owner and provenance; time, event, PC, and session-log bounds agree or show an explicit
gate/diagnostic. Report accepted patches, retained evidence, conflicts, and gates.

## Post-session synthesis gate

After reconciliation, support the short wiki spine: within 24 hours capture who
acted, decisions that became true, and open threads in roughly 15 minutes. Promote
improvised NPCs, places, loot, and other durable facts only to their typed atomic
owners, preserving provenance and uncertainty. Compare a player recap only after
the evidence-backed log exists; route faction clocks and off-screen movement to
`world-tick`. After players interact with or witness lore: update Current Truth when it changed and append a Canon Log row. Until then the DM may change lore freely. Quest log stays with `narrative-islands`. Never use raw transcript wording as the vault's durable prose.
