---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-07-25"
updated: "2026-08-10"
tags: [craft]
summary: "Exemplar quality rubric: structure, retrieval, numbers, and mechanics checks (R1–R10)."
within: "[[exemplar-quality-rubric]]"
uid: a733669e-c80d-4db5-b29f-b7b2c708abf9
---

# Exemplar Quality Rubric: Structure, Retrieval & Numbers

Checks R1–R10 from the `vault/refs/exemplar-quality-rubric.md` quality rubric.

## A. Structure and retrieval

- **R1 — Declared conventions.** The document (or its type's template) states its
  own reading rules: what the unit grammar is, where stat blocks and reference
  live, what's player-safe vs DM-only. Check: a reader can answer "how do I parse
  this?" from the document itself. *(Wild Sheep Chase "Using This Adventure";
  Night Hunter GM page; Silverpine "About the Module".)*
- **R2 — One unit grammar, spent where warranted.** Every unit of the same kind
  follows one fixed section skeleton; trivial units may collapse to a paragraph,
  but no unit invents a new shape. Check: diff the section order of any two
  same-kind units — identical or strictly truncated. *(Potent Brew rooms;
  Silverpine encounters; Night Hunter events; Darker Dungeons chapters.)*
- **R3 — Scannable retrieval keys.** Facts sit in bullets whose first bolded
  words are the load-bearing nouns, or under headers naming the interactable —
  never mid-paragraph. Check: for any fact a runner needs mid-scene, the eye
  path is header/bold → fact. This is the structural requirement; the bolding
  mechanic itself (which words, on which lines) is R27/R28's job — this check
  only asks whether the document's retrieval keys exist at all. *(Night Hunter's
  bolded-keyword bullets; Silverpine's element headers.)*
- **R4 — Explicit transitions.** Every scene/unit ends with a pointer: exit
  conditions, the next unit by name, elapsed in-fiction time where relevant;
  spatial docs name each exit as direction → destination key. Check: no unit
  ends without a "go to / leads to" line. *(Night Hunter Transitions; Silverpine
  Move On; Serpent Kings' loud cross-references.)*
- **R5 — Two layers: prep view and play view.** Beyond the full prose, a
  compressed at-table layer exists — a scan table, summary block, quick-ref
  section, or tracker — holding dimensions/senses/contents/numbers per unit.
  Check: the runner can operate mid-session without rereading prose paragraphs.
  *(Serpent Kings' annotated map layer; Darker Dungeons' trackers and sheets.)*
- **R6 — Reference quarantined but linked.** Stat blocks and lookup material sit
  at point of first use or in a linked appendix — never interrupting scene flow,
  never more than one hop away. Check: scene text names behavior; numbers are
  one link/glance away. *(Night Hunter appendices + links; Pleasantries' end
  quarantine; Wild Sheep Chase at-point-of-use.)*

## B. Numbers and mechanics

- **R7 — Checks complete at point of use.** Every check states ability + skill +
  DC + failure consequence (and invocation flags: passive / no action /
  proficiency-gated / advantage-with-reason) in one line where it fires. Check:
  grep any DC — its line carries the full anatomy; no bare DCs. *(Silverpine's
  typed check format; Potent Brew inline checks.)*
- **R8 — Both outcomes pre-written.** Roll-triggering text resolves in labeled
  success and failure lines; degrees where they matter (bonus fact on a high
  roll). Check: no check whose failure outcome the runner must invent.
  *(Darker Dungeons Success:/Failure: pairs; Pleasantries' high-roll bonus.)*
- **R9 — Concrete numbers close every loop.** Prices in gp, repair times, XP,
  distances, durations, capacities — stated wherever a loop resolves. Check: no
  "valuable", "a while", "several" where a number would be acted on.
  *(Potent Brew's 25gp/50gp/100xp; the Jinx's costed misfortunes; Serpent Kings'
  inline valuations.)*
- **R10 — Deltas over duplication.** Variants state themselves as changes to a
  named chassis ("as X, but..."; role-labeled models sharing declared common
  traits; reskins by stat-swap sentence). Full duplication only where an
  artifact must run standalone. Check: no near-identical block pair without a
  declared chassis. *(Wild Sheep Chase's pony-sheep; Serpent Kings' "stats as a
  lich"; `docs/exemplars/pointyhat-the-necromaton.md`'s model family.)*
