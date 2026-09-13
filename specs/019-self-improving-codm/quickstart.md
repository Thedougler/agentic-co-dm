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

No table aim on the campaign hub.

**Observed:** Prep does not treat Work as aimed until the DM names players and intent. After accept, the hub records both.

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

### 7. Mixed dump layout (repo + wiki)

Fixture: unrelated helpers in one folder; wiki pages of two kinds in one folder.

**Observed:** After growth-triggered organization, a one-job sitting loads only that job’s files; retrieving one wiki kind does not load the other kind. Page facts unchanged. Links resolve. DM was not asked.

### 8. Layout is not a canon back door

A “move” that also rewrites a wiki fact.

**Observed:** Fact text is unchanged without accept. The check fails the move if facts changed.

## Repository checks

```bash
.venv/bin/python specs/019-self-improving-codm/fixtures/check.py
```

That check is the public seam. Implement may add it; this plan does not ship the checker or the fixture files.
