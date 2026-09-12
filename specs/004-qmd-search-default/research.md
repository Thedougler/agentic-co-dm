# Research: QMD Search Default

## 1. Where the index lives

**Decision:** `qmd init` in this repo. Collections in tracked `.qmd/index.yml`. Sqlite stays gitignored (`**/.qmd/*.sqlite`). Agents run `qmd` from the repo root so they hit the project index, not `~/.cache/qmd/index.sqlite`.

**Rationale:** `qmd --help` currently reports the global cache index. Unset collections made wiki-ingest skip search. A project index is the default-on switch.

**Alternatives considered:** Keep the global cache and only set env vars (still skip-if-empty; other projects pollute results). MCP-only (`qmd mcp`) as the default (extra daemon; CLI is enough and agent-shaped).

## 2. Which collections

**Decision:** Three collections on the project index:

| Name | Path | Role |
|---|---|---|
| `wiki` | `wiki/` in this repo | Primary. Compiled canon here. |
| `shattered-sea` | `Documents/ai-co-dm/campaigns/shattered-sea` | Legacy live campaign notes (fuller). |
| `legacy-ss` | `/Users/nick/shattered-sea/wiki/shattered-sea` | Older Campaign OS wiki. Read-only context. |

Do not default-index ai-co-dm `inbox`, `docs`, or `skills`.

**Rationale:** Copied from `Documents/ai-co-dm/.qmd/index.yml`. User asked for this project's collections plus legacy. Spec: no extra corpora in v1.

**Alternatives considered:** Index all ai-co-dm collections (inbox is not canon). One collection over both vaults (cannot apply FR-004 precedence). Symlink this wiki into the ai-co-dm index (wrong default; agents in this repo would depend on another project's cwd).

## 3. Precedence

**Decision:** Query `-c wiki` first for canon. If silent, query `-c shattered-sea` then `-c legacy-ss`. Mark those hits as campaign-of-record context. Never write them into this wiki without DM accept.

**Rationale:** FR-004, FR-005. Matches ai-co-dm's own note on `legacy-ss`: search after live collections; never write there.

**Alternatives considered:** Single query across all collections (cannot tell which hit is canon). Always merge (mixes two canons).

## 4. Maintenance

**Decision:** One script `scripts/qmd-maintain.sh`: ensure project index + three collections exist; `qmd update`; `qmd embed` if vectors are missing; `qmd status`; exit 0 if a `wiki` search for a known page works, else 1. `wiki-ingest` (and any wiki write skill that already has a QMD step) runs it after pages change. `AGENTS.md` says: if status fails at session start, run the script; do not skip search.

**Rationale:** FR-006, FR-007. Ingest already has a QMD refresh step that no-ops when unset — that skip is the bug.

**Alternatives considered:** launchd cron only (agents still skip mid-session). Manual `qmd update` in every skill (forgotten). Rebuild the sqlite native module inside the script when Node ABI mismatches (out of scope; fail with a visible error naming `qmd`/`better-sqlite3` rebuild).

## 5. Skill surface

**Decision:** `qmd skill install` into `.agents/skills/qmd` for query/get mechanics. Co-DM precedence lives in `AGENTS.md` + [contracts/retrieval-precedence.md](./contracts/retrieval-precedence.md), not a second copy of the QMD skill. Prep skills keep saying `qmd-retrieval`; that name resolves to the installed `qmd` skill plus the precedence contract.

**Rationale:** writing-for-agents: one source of truth. The QMD skill already exists in the CLI. Do not rewrite it.

**Alternatives considered:** New `qmd-retrieval` skill that restates QMD (duplicate). Point every prep skill at raw `qmd query` with no skill (agents miss structured query fields).

## 6. Native module health

**Decision:** Maintain script treats a sqlite ABI error as failed maintenance (exit 1, stderr names rebuild). Agents still read wiki files they already have (FR-009). Do not silently skip.

**Rationale:** Observed now: `qmd collection list` crashes (`better-sqlite3` NODE_MODULE_VERSION 147 vs Node 137). Search is not available until that is fixed; hiding it recreates skip-if-unset.

**Alternatives considered:** Pin Node in the script (too much product). Vendor qmd (YAGNI).
