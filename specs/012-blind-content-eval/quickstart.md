# Quickstart: Blind Cold Evaluation of D&D Content

Prove the feature with cold judgments of samples. Do not treat a file-shape check as pass. Do not rewrite `legacy/`.

## Prerequisites

- Branch `012-blind-content-eval`
- Spec [spec.md](./spec.md), contract [contracts/blind-content-eval.md](./contracts/blind-content-eval.md)
- `.agents/skills/blind-content-eval/SKILL.md` exists
- `writing-for-agents` D&D content guidance lists two cold evals as done
- Rubrics still live on `copy-writer`, `theatre-of-the-mind`, `obsidian-markdown` / `wiki/AGENTS.md` Layout

## 1. Eval is required, scripts are not enough (P1, SC-001, SC-002)

Cover contract jobs 1–5, 15.

- Guidance change that produces D&D content: two cold evals of a sample. Fail if treated as done after a file-shape check only.
- Evaluator who saw the authoring session: void.
- Author self-review: not this test.
- Non-D&D-content guidance: eval not required.

## 2. Form and appropriate use (P2, SC-006)

- Sample claims a kind: layout/format/shape/mechanics match that kind and are used for those jobs.
- Fail if a mechanic or layout treatment is decoration.
- Fail if heading-order match is the only virtue and the page is unusable.
- Spoken-only handout: do not fail missing mechanics.

## 3. DM copy (P3, SC-004)

- DM-facing bands: complete-sentence table reference.
- Fail telegram, slash-stacks, agent-speak.
- No DM band: omit this axis.

## 4. Spoken look (P4, SC-005)

- Player-facing narration: drawable, speakable, no secret/DC/unearned name/process note.
- Fail telegram or padding.
- No spoken band: omit this axis.

## 5. Two judges agree (SC-003)

Two independent cold evals on the same sample. Disagreement → not done. Cover at least the mixed sample (job 7), spoken-only (8), DM-only (9), and a fail case (10–12).

## 6. Pointers, not copies (Constitution IX)

- Eval skill names axes and fail modes. It does not restate copy-writer or TotM.
- `writing-for-agents` only adds the done-gate. It does not become the judge.
- No 010 stack-table row. No pytest suite.

## 7. Legacy untouched (SC-007)

This change set does not rewrite `legacy/` or restyle historical wiki pages solely to prove eval.

Pass: steps 1–7 hold. Fail any step → the eval is not the default yet.
