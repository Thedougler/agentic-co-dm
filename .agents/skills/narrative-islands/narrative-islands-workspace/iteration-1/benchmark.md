# Skill Benchmark: narrative-islands + sandbox-narrative

**Model**: claude-haiku-4-5-20251001
**Date**: 2026-09-20T12:19:24Z
**Evals**: agency-audit, frozen-island, situation-not-story, eruptibility

## Summary

| Metric | With Skill | Without Skill | Delta |
|--------|-----------|--------------|-------|
| Pass Rate | 75% | 43% | +0.32 |
| Time | 102.5s | 78.9s | +23.6s |
| Tokens | 60260 | 48524 | +11736 |

## Per-Eval Breakdown

| Eval | With Skill | Without Skill | Winner |
|------|-----------|--------------|--------|
| agency-audit | 67% (6/9) | 78% (7/9) | without_skill |
| frozen-island | 33% (2/6) | 33% (2/6) | tie |
| situation-not-story | 100% (7/7) | 43% (3/7) | with_skill |
| eruptibility | 100% (6/6) | 17% (1/6) | with_skill |

## Analyst Notes

- agency-audit: with-skill FAILED to reject single-approach constraint — baseline actually offered negotiation option. Skill needs stronger guardrail against prescribed single approaches.
- frozen-island: BOTH versions implemented the frozen-island anti-pattern. Neither resisted the prompt's instruction to freeze escalation to party arrival. Skill needs explicit anti-pattern rejection guidance.
- situation-not-story: Strong with-skill win (7/7 vs 3/7). Skill successfully converted prescribed PC sequence into situation-first forces.
- eruptibility: Massive with-skill win (6/6 vs 1/6). Baseline built exact anti-pattern (trigger questions, static town). Skill produced active forces with visible tells.
- Non-discriminating assertion: Causality consistently passes for both configs — the principle is too easy for haiku to satisfy without skill guidance.