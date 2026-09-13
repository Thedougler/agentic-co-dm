# Quickstart: Self-Improving Co-DM

## Prerequisites

From the repository root, after implement lands standing rules, the ledger helper, and the wrapup reflection step:

```bash
python --version
.venv/bin/python specs/019-self-improving-codm/fixtures/check.py
```

Use [contracts/self-improving-codm.md](contracts/self-improving-codm.md) and [data-model.md](data-model.md). Fixture vault pages belong under `fixtures/wiki/`; a mixed agent dump belongs under `fixtures/ops/`.

The check asserts observable files and Work outcomes. Do not replace it with a string snapshot of `AGENTS.md` or `session-wrapup`.

## Validation scenarios

### 1. Missing aim is asked

No table aim on the campaign hub (Campaign State group).

**Observed:** Prep does not treat Work as aimed until the DM names players and intent. After accept, the hub records both. The aim is not on a DM Intelligence page.

### 2. Gap does not stall

Prep request the wiki does not cover.

**Observed:** A proposal marked invention lands in that sitting. The gap is named. No campaign-facing practice file changed.

### 3. Wrapup reflection is Work

Finished wrapup with one thing that served these players and one that did not.

**Observed:** Chat reflection exists. Reject leaves wiki facts unchanged. Accept of a fact change is a proposal, not a silent page write.

### 4. Sitting is recorded without the DM

One prep sitting completes.

**Observed:** A sitting record exists (kind, jobs, paths/skills loaded). No DM accept step for that record.

### 5. Ledger fill and drain

Runtime failure, then an accepted wiki fact write that removes that cause.

**Observed:** `errors.md` gained an entry before sitting close. After the accepted write, that entry is gone. Unrelated open entries remain. Drain without `cause_fixed` fails the helper.

### 6. Helper on a repeating job

Same job twice; no existing command.

**Observed:** After the first sitting a helper exists. Second sitting uses it. DM did not request it. Wrapping `qmd` does not count.

### 7. Mixed dump layout (wiki kinds + agent files)

Fixture: System files mixed with Source Material (`wiki/_raw/`); wiki pages for Encounters and Rules mixed in one folder (existing `type` values unchanged).

**Observed:** After growth-triggered organization, retrieving Encounters does not load Rules; retrieving System does not load Source Material. Page facts unchanged. `type` unchanged. DM was not asked.

### 8. Layout is not a canon back door

A “move” that also rewrites a wiki fact, or that files Source Material as canon, or that copies table aim onto DM Intelligence.

**Observed:** Fact text is unchanged without accept. Source Material is not canon. Aim remains on the hub. The check fails the move if any of those happened.

## Repository checks

```bash
.venv/bin/python specs/019-self-improving-codm/fixtures/check.py
```

That check is the public seam. It covers scenarios 1–8 against `fixtures/wiki/` and `fixtures/ops/`, and invokes `scripts/error-ledger.py` for sitting records and ledger fill/drain.
