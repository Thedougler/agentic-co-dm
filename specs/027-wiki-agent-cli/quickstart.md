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

## V-001 Worklist, not a findings blob (SC-001, SC-002)

```bash
.venv/bin/python scripts/wiki lint entities/npc
```

Expect: compact JSON; keys in the worklist contract; no `findings` / `findings_by_file`; `unique` already deduped; stdout size under 8 KB on a ~100-page prefix. Exit 0 or 1, never 2.

```bash
.venv/bin/python scripts/wiki lint entities/npc --full
```

Expect: worklist keys plus finding dump; may exceed 8 KB.

## V-002 Single file includes lines (FR-010)

```bash
.venv/bin/python scripts/wiki lint entities/npc/<existing-page>.md
```

Expect: `findings[]` with `rule`, `file`, `line` (int ≥ 1), `severity`, `message`.

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

Expect: exit 0; at least one hit with `title`, `path`, `id`. Backend down: exit 2, structured error, no fake hits.

## V-006 Health alias, trends, focus (SC-005, FR-019)

```bash
.venv/bin/python scripts/wiki health
.venv/bin/python scripts/wiki-maintain --report
```

Expect: identical snapshot; keys `pages`, `bytes`, `tokens`, lint hard total, `trends`, `focus`, `next`; no findings dump; no `steps` essays; no raw sitting/trace rows. `next` is `focus[0]` or null. `len(focus) <= 5`.

## V-007 Pretty vs default (SC-006)

```bash
.venv/bin/python scripts/wiki lint entities/npc
.venv/bin/python scripts/wiki lint entities/npc --pretty
```

On an interactive terminal, the first is still compact JSON. The second is text (scoreboard). `--json` does not change the first.

## V-008 Cold agent (SC-008)

Independent subject, cold context: this spec’s command examples only. Task: lint one file and name `next_page` from the worklist. Pass if it does not parse nested finding maps.

## V-009 Health next for a small agent (SC-009)

Independent subject (smol / Luna-Haiku class), cold context: this spec’s health object only. Task: name `next.path` and its `reason`, then state the one action to take. Pass if it does not ask for a DM prompt or parse an essay.

## V-010 Empty trackers

Temp vault with no `sittings.jsonl`, `errors.md`, or traces. `wiki health` still emits `trends` with zero counts and `focus`/`next` from lint/remorph only.

## pytest

```bash
.venv/bin/python -m pytest tests/test_wiki_cli.py -q
```

Temp-vault tests cover V-001–V-007 and V-010 seams. V-002/V-004/V-006 may use fixtures; V-001 size and V-005 need the live wiki / qmd when available.

## Instruction check

`.agents/skills/wiki-lint/SKILL.md` documents `scripts/wiki lint`, not `./scripts/wiki-lint --json wiki/` as the default structural pass. Health docs say run `scripts/wiki health` then do `next`.
