# Contract: Self-Improving Co-DM

Agent-facing. Players never operate this loop. Does not replace [001 Co-DM](../../001-agentic-co-dm/spec.md), [work.md](../../../docs/agents/work.md), 012 eval, or 016 dispatch.

## Aim

1. If table aim is missing, ask for players and current intent before treating Work as aimed.
2. After the DM records it on the campaign hub (accept), later Work uses that aim. The hub is grouped under Campaign State. DM Intelligence is not the aim.
3. Work that could be used on a different table without edits does not count as aimed.

## Gaps

4. A missing wiki fact or missing Co-DM practice does not stall playable Work in that sitting.
5. Name the gap.
6. Campaign-facing practice fixes are proposals. Wasted-context cuts are not.

## Reflection

7. After wrapup, offer a reflection with at least one observation about these players.
8. After prep, offer a reflection only if the DM asks.
9. Reflection is chat Work. Reject: no wiki fact write, no campaign-facing practice change.
10. Accepted fact change → canon proposal, still wait for accept.
11. Accepted campaign-facing practice change → improvement proposal, still wait for accept.
12. No reflection or improvement during a session.

## Token cost (agents)

13. Record every prep/wrapup sitting: kind, jobs, paths read, skills loaded, helpers used, waste named, errors filled.
14. Compare only same-kind sittings.
15. The DM does not record, review, or gate token cost.
16. A change that raises cost for the same jobs without a named failure is not an improvement.
17. A change that lowers cost by lowering quality is not an improvement.

## Helpers (agents)

18. If a job will repeat and a helper would lower later token cost, create it without being asked.
19. Use it on the next same-kind sitting. Keep it current or remove it.
20. Agent-shaped: no GUI, arguments in, text or JSON out, exit distinguishes done vs failed.
21. Do not wrap a command that already does the job.

## Error ledger (agents)

22. File is `errors.md` at the repo root. Operated by `scripts/error-ledger.py` (`error append|drain|list`, `sitting record|list`). Sitting log is `sittings.jsonl` beside it.
23. On runtime failure, append an entry before the sitting is complete.
24. Drain an entry only when its cause is actually fixed.
25. After an accepted wiki fact write (or other landed fix) that removes a cause, drain matching entries in that sitting.
26. Do not drain the whole ledger because some entries were fixed.
27. The DM does not edit the ledger. Fact writes that *are* the fix still wait on accept; drain after they land.

## Layout (agents)

28. As agent-facing files **and** the wiki (llm-wiki) grow mixed, regroup so one job or layout kind does not load unrelated trees.
29. Trigger is growth that makes lookup costly, not tidiness.
30. The DM does not approve layout.
31. Wiki layout moves do not change page facts or campaign `type`. Links and names still resolve in the same change.
32. Wiki fact changes still use the accept-gate. Layout is not a path around canon.
33. A layout change that increases hops or unrelated load is not an improvement.
34. Wiki layout kinds: Encounters, Rules, Campaign State, DM Intelligence. Agent-facing layout kinds: System, Source Material.
35. Do not add a layout kind that duplicates an existing `type`. Do not add `type: encounter` or `type: rules`.
36. System and Source Material stay non-canon. Source Material is `wiki/_raw/` staging.
37. Table aim stays on the campaign hub. Layout MUST NOT copy it onto DM Intelligence.
38. Wiki copy-start templates exist for Encounters, Rules, Campaign State, and DM Intelligence. New pages use `session-prep`, `lore`, `lore`, and `work` respectively.
39. System and Source Material do not get wiki templates.
40. Existing pages in those four groups are rewritten onto the matching templates when facts stay the same. Fact-changing rewrites still wait on accept.
41. Templates MUST NOT add a campaign `type`.

## Out of contract

Live Co-DM during a session. Player-operated feedback. Tokenizer infrastructure. New wiki kind or `type` for table aim, Encounters, or Rules. New self-improve skill. Wrapping `qmd` or git. Blind-eval of reflection chat. Rewriting session-log bands (that remains wrapup/012 if those bands change). A mandated folder taxonomy. Work coverage for every layout kind.
