# Quickstart: Agent-Shaped Wiki CLI

Validate [spec.md](spec.md) against [contracts/wiki-cli.md](contracts/wiki-cli.md). From repo root. Vault from existing config.

## Prerequisites

- Feature branch `027-wiki-agent-cli`
- `.venv/bin/python` for pytest
- `qmd` on PATH for query (SC-004). If missing, record blocker; lint/health still run.
- Configured `OBSIDIAN_VAULT_PATH` (or repo `.env`)

## Setup

```bash
chmod +x scripts/wiki
```

No extra packages. Vale and tiktoken are already project dependencies.

## V-001 Bounded bulk lint and smallest next page (SC-001, SC-002)

```bash
.venv/bin/python scripts/wiki lint
```

Expect: compact JSON whose aggregate `counts`, `finding_total`, and `affected_pages` cover all configured checkers. `next.path` is the smallest dirty file by bytes then path, and `next.action` tells the agent to lint it with `--full`. Default output has no `files`, `unique`, or `backlog` dump.

```bash
.venv/bin/python scripts/wiki lint --full
```

Expect: the same overview plus complete per-file findings, including 1-based lines.

```bash
.venv/bin/python scripts/wiki lint entities/npc/<next-page>.md --full
```

Expect: detailed findings for only the recommended page.

## V-002 Scoped bulk lint (SC-002)

```bash
.venv/bin/python scripts/wiki lint entities/npc/page-a.md entities/npc/page-b.md
```

Expect: the same bounded overview shape, with `next` selected from the dirty files in scope. Add `--full` to get two detailed file groups.

## V-003 Unknown path fails closed (SC-007)

```bash
.venv/bin/python scripts/wiki lint entities/npcs
```

Expect: exit 2; `status=error` on stdout; finishes in under one second; does not enumerate the wiki.

## V-004 Cache (SC-003)

```bash
.venv/bin/python scripts/wiki lint
.venv/bin/python scripts/wiki lint
```

Second run: `cache.hits` > 0 for previously checked pages; Vale not re-executed on unchanged files (`vale_skipped` accounts for those pages). Change a page byte and rerun: that path is a miss.

## V-005 Query (SC-004)

```bash
CI=true .venv/bin/python scripts/wiki query "<a known in-wiki title>"
```

Expect: exit 0; at least one hit with `title`, `path`, `id`; `timing.command` is `query`. Backend down: exit 2, structured error, no fake hits.

## V-006 Health alias, trends, focus (SC-005, FR-019, SC-010, SC-011)

```bash
.venv/bin/python scripts/wiki health
.venv/bin/python scripts/wiki-maintain --report
```

Expect: identical snapshot; keys `pages`, `bytes`, `tokens`, lint hard total, `trends` (including `slowest_commands` and `token_heaviest` when records exist), `focus`, `next`, `timing`; no `files` dump; no `steps` essays; no raw sitting/trace rows; no skill-eval keys. `next` is `focus[0]` or null. `len(focus) <= 5`.

After two prior `wiki lint` or `wiki query` runs, `trends.slowest_commands` names the slower command.

## V-007 Pretty vs default (SC-006)

```bash
.venv/bin/python scripts/wiki lint entities/npc
.venv/bin/python scripts/wiki lint entities/npc --pretty
```

On an interactive terminal, the first is still compact JSON. The second is text (scoreboard plus `file:line  RULE  message` grouped by file). `--json` does not change the first.

## V-008 Cold agent (SC-008)

Independent subject, cold context: this spec’s command examples only. Task: lint one file, name at least one finding line, and name `next_page`. Pass if it does not parse nested per-rule maps.

## V-009 Health next for a small agent (SC-009)

Independent subject (smol / Luna-Haiku class), cold context: this spec’s health object only. Task: name `next.path` and its `reason`, then state the one action to take. Pass if it does not ask for a DM prompt or parse an essay.

## V-010 Empty trackers

Temp vault with no `sittings.jsonl`, `errors.md`, or traces. `wiki health` still emits `trends` with zero counts and `focus`/`next` from lint/remorph only.

## pytest

```bash
.venv/bin/python -m pytest tests/test_wiki_cli.py -q
```

Temp-vault tests cover V-001–V-004, V-006–V-007, and V-010 seams. V-005 needs the live wiki / qmd when available.

## Instruction check

`.agents/skills/wiki-lint/SKILL.md` documents `wiki lint` as the sole agent-facing lint command with a bounded default overview and `--full` detail. Health docs say run `scripts/wiki health` then do `next`.
