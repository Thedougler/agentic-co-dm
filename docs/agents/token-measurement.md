# ASE method: objective token measurement (#86)

**Status:** design lock for ATE.  
**Rule:** any field labeled **tokens** (or compared to `WIKI_TOKEN_WARN_THRESHOLD`) MUST use a real tokenizer — **not** `file_size_bytes / 4`, not “lines ≈ tokens.”  
**Standing:** do not thin narrative/mechanics/instruction craft to chase a token score (#71 / #84 / #87).

---

## 1. Encoding default

| Setting | Value |
|---|---|
| **Default encoding** | `cl100k_base` (tiktoken) |
| **Rationale** | Stable, widely used comparative substrate for GPT-4-class context budgets; reproducible across the fleet |
| **Override** | env `WIKI_TOKEN_ENCODING` (e.g. `o200k_base` for GPT-4o-family experiments) |
| **CLI flag** | `--encoding <name>` overrides env for one run |

Do **not** silently switch defaults per machine. Document the encoding in every JSON payload (`encoding` field).

Absolute counts approximate the named encoding’s model family; they are for **budget comparison and thresholds**, not model-billing invoices.

---

## 2. Surfaces that MUST report tiktoken

| Surface | Requirement |
|---|---|
| `scripts/token-count.py` (new thin CLI) | Primary: path(s) or stdin → JSON `{path, encoding, tokens}` (optional `bytes` alongside, never as tokens) |
| `wiki-status` footprint / token estimate | Replace `file_size_bytes / 4` with tiktoken totals; dual-report one sitting then drop approx |
| Any JSON field named `tokens` / `token_count` / `tokens_*` | Must be tiktoken under the locked encoding |
| `WIKI_TOKEN_WARN_THRESHOLD` comparison | Compare against tiktoken sum only |

## 3. Surfaces that keep bytes/lines (not “tokens”)

| Surface | Keep |
|---|---|
| `context-waste-scan.py` S3/S4 leads | `bytes` / `lines` as structural investigation leads — **do not** rename them to tokens |
| Optional scan add-on | If a `tokens` field is added later, it must call the shared counter; still not a delete mandate |

---

## 4. Thin CLI contract (`scripts/token-count.py`)

```text
python3 scripts/token-count.py path [path ...]
python3 scripts/token-count.py --stdin
python3 scripts/token-count.py --sum wiki/entities/npc   # optional rollup
```

**Stdout JSON (default):**
```json
{
  "encoding": "cl100k_base",
  "files": [{"path": "wiki/hot.md", "tokens": 412, "bytes": 2048}],
  "total_tokens": 412
}
```

**Acceptance:** no file bodies in stdout; pin `tiktoken` in project deps; works on box; exit 0 on success; missing path → non-zero + stderr.

Shared importable helper preferred (e.g. `tools/token_count.py` or package function) so wiki-status / scan do not reimplement.

---

## 5. `WIKI_TOKEN_WARN_THRESHOLD` migration

1. **Wire** wiki-status to tiktoken totals under `cl100k_base`.
2. **Dual-report** one transition: `tokens` (tiktoken) + `tokens_approx_bytes_div_4` (deprecated label).
3. **Remeasure** full active vault once with `token-count.py --sum`; if the old threshold (default `100000`) was calibrated on ÷4, adjust only if the ratio drift would false-alarm or hide real bloat — document the measured vault total in the PR that removes approx.
4. **Remove** ÷4 heuristic from wiki-status skill text and any helper.
5. Threshold meaning stays: warn when **tiktoken** full-wiki (or scoped) sum exceeds env; `0` disables.

Do not lower craft quality to get under the threshold.

---

## 6. Docs pointers

| Location | Add |
|---|---|
| This doc | Method of record |
| `AGENTS.md` Token cost / Helpers | Point at `token-count.py`; forbid ÷4 for anything labeled tokens |
| `wiki-status` skill | Footprint uses tiktoken CLI/helper |
| `docs/agents/context-waste-method.md` | Size leads ≠ token counts; token fields → #86 |

---

## ATE packet

```text
ATE: implement scripts/token-count.py + pin tiktoken; wire wiki-status; optional scan tokens field
Issue: #86
Default encoding: cl100k_base (env WIKI_TOKEN_ENCODING override)
Replace file_size/4; dual-report then drop approx
Keep context-waste-scan bytes/lines as leads (not labeled tokens)
No craft thinning for scores
```
