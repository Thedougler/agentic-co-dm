---
name: llm-wiki-lint
description: Run a standalone bulk lint sweep of a Campaign OS wiki (vault/ present) against the `npm run lint -- --rules` rule table. Use for "lint the wiki", "check wiki health", "audit the vault", "find broken links/orphans/deadends", "fix the frontmatter", "tag hygiene", or a git ref for an incremental check.
---

# llm-wiki-lint

`npm run lint -- --rules` prints the rule registry that every
campaign skill already self-checks its own output against as a "done-check"
(`.claude/rules/skills.md`). This skill runs that same table
**standalone, across many pages at once** — whole-repo health or "what
changed since `<ref>`" — instead of one skill's one page. `npm run lint:sweep`
runs every producer that's mechanically checkable — markdownlint-obsidian
W-rules, the ajv/remark frontmatter-schema pipeline, Vale (`CampaignOS`
style), oxlint, jscpd (duplication), and link resolution — all already
wired into this repo's PostToolUse hook and pre-commit (`.claude/settings.json`,
`.pre-commit-config.yaml`). The "Built" column in `npm run lint -- --rules`'s output is the live
source of which rule runs through which producer; only genuine
cross-file/semantic judgment stays hand-checked below.

Never restate the rule table, its severities, or its FIX-line wording here
— run `npm run lint -- --rules` for all
of that. This skill owns *running* the table at scale and *working* what it
finds; `npm run lint -- --rules` owns *what the rules are*.

## Invoked bare — lead the backlog drain

No specific request attached → don't sweep serially: read
[references/backlog-drain.md](references/backlog-drain.md) and run DR1–DR7
— waves of parallel Haiku subagents (`content-fixer` for vault/**.md,
`general-purpose` for everything else), verified per wave with
`rerun-check.mjs lint`, ratchet-synced and promoted per wave close. The
loop below still governs what a linter may touch: handoff findings (step 4)
never go to a drain-wave subagent.

## Standard queries

**Run `npm run lint:sweep` first — it's the default check for everything
the producers cover** (autofix + every producer, one manifest). This skill's job
is the same check in bulk, on files that bypassed the per-edit gates (a
git pull, a script-generated batch, edits outside this harness):

```bash
# Whole corpus — autofix + dispatch manifest
npm run lint:sweep

# Inspect without autofixing
npm run lint:sweep -- --no-fix

# One file or directory
npm run lint -- <path>

# One rule in isolation
npm run lint -- <path> --only <id>
```

Translate every finding into a block: `OFM001`/W3, any `W<n>` a
markdownlint-obsidian custom rule emits, and any frontmatter-schema/Vale/
jscpd finding mapping to a `W<n>` (README's "Built" table says which) all
map to `WIKI-LINT W<n> (hard|soft)` — same block format as every rule
below, whichever tool caught it. A CLI finding with no W-table entry (bare
`OFM0xx` codes; an unmapped ajv/Vale/jscpd finding) still isn't optional:
emit `LINT <ruleCode> (<severity>) — <file>:<line>` / the tool's own
message / `FIX: <run the tool's own --fix, or its suggested edit>`.

Never hand-grep what the CLI runs above already covered — every rule in
`npm run lint -- --rules`'s "Built" table runs as a real
deterministic check now, through whichever producer owns it.

The per-rule greps for what's left — genuine cross-file relationships and
judgment calls no per-file lint rule can make (paste every hit; an empty
result is itself a finding — say so, don't go hunting for one):

```bash
# W9 — duplicate alias claimed by two pages' frontmatter
awk '
  /^aliases:[[:space:]]*\[/ {
    line=$0; sub(/^aliases:[[:space:]]*\[/,"",line); sub(/\][[:space:]]*$/,"",line);
    n=split(line, arr, ",");
    for (i=1;i<=n;i++){
      v=arr[i]; gsub(/^[[:space:]"]+/,"",v); gsub(/[[:space:]"]+$/,"",v);
      if(v!="") print v"\t"FILENAME
    }
    inblock=0; next
  }
  /^aliases:[[:space:]]*$/ { inblock=1; next }
  inblock && /^[[:space:]]+-[[:space:]]+/ {
    v=$0; sub(/^[[:space:]]+-[[:space:]]+/,"",v);
    gsub(/^"+/,"",v); gsub(/"+$/,"",v);
    print v"\t"FILENAME; next
  }
  { inblock=0 }
' $(grep -rl "^aliases:" vault/ --include="*.md") | sort | cut -f1 | uniq -d

# W16 — unresolved CONTRADICTION blocks
grep -rl "^> \[!warning\] CONTRADICTION" vault/ --include="*.md" 2>/dev/null

# W19 — content-type folder missing its template or owning skill/guide (whole-repo only)
# Both lookups scan a fixed set once, not once per folder.
templates="$(find vault/_templates -name '_*.md')"
prep_skills="$(find . -path '*/.claude/skills/*-prep/SKILL.md' -not -path './node_modules/*' -not -path '*/fixtures/*')"
for folder in $(printf '%s\n' vault/srd/*/ vault/campaigns/*/*/ | xargs -n1 basename | sort -u); do
  [ "$folder" = "_meta" ] && continue
  type="${folder%s}"                      # plain-plural default
  case "$folder" in                       # irregular folder->type exceptions
    rules) type=rule ;;
    classes) type=class ;;
    deities) type=deity ;;
    lore) type=lore ;;
    species) type=species ;;              # plural-invariant
    vehicles) type=ship ;;                # folder names the content, the type stays ship
    campaign|dashboards|pcs|statblocks) continue ;;  # no content type of their own, or owned outside the -prep convention
  esac
  guide_file=".claude/skills/draft-content/references/${type}.md"  # a type owns authoring here, or via a legacy <type>-prep skill in any subtree's skills root
  printf '%s\n' "$templates" | grep -q "/_${type}\.md$" || echo "W19: ${folder}/ (vault/srd or vault/campaigns/*/) has no vault/_templates/**/_${type}.md"
  [ -f "$guide_file" ] || printf '%s\n' "$prep_skills" | grep -q "/${type}-prep/SKILL\.md$" || echo "W19: ${folder}/ (vault/srd or vault/campaigns/*/) has no ${guide_file} and no */.claude/skills/${type}-prep/"
done
```

W8 (stale pending pages) and W17 (entity dedup) need a judgment read no
grep can stand in for — walk the file list from the scope step above. W19 is
whole-repo only (directory-level, not per-file) — skip it under `--since`.

## The loop

1. **Scope.** Whole-repo, or `--since <ref>` — paste the file list either
   way. `LT1: <file list pasted, whole-repo or --since ref>` (a lint run
   with no file list pasted didn't run).
2. **Run every rule in the table** against that scope — the CLI run first
   (Standard queries above) for what it covers, then the remaining greps/reads
   for what only the agent can check. Emit one WIKI-LINT block per finding
   (format below), hard findings before soft, grouped by rule ID within each
   tier. `LT2: <finding count by severity, or 0 — clean>`.
3. **Work the report**, same compliance rule CLAUDE.md already states for
   every WIKI-LINT block anywhere in this repo: obey the FIX line, or paste
   `NOTED (not done): <reason>`. Two failed fixes of the same finding — stop,
   escalate to the human (L5). This is not a separate auto-fix mode; it's
   the normal edit you'd make to any file, scoped by **Mechanical vs
   judgment** below. `LT3: <fixed count, NOTED count>`.
4. **Never resolve W9/W16/W17/W18 yourself.** Each names a call only a
   human or canon-review makes (`npm run lint -- --rules`'s own FIX lines say so
   per rule) — append the CONTRADICTION block (format: `transcript-ingest`
   SKILL.md § Contradictions) / REVIEW ledger line, then hand off. `LT4: <queue items handed off, or
   N/A — none this pass>. -> chain-load canon-review; next tool call is Read
   on canon-review's SKILL.md, no acting tool call beside it` (canon-review
   drains the queue, this skill only builds it). A W19 finding surfaces the
   same way — report it, don't launch `content-type-scaffold`'s multi-step
   research procedure mid-sweep; the human or the next content-authoring
   pass triggers it. **Never resolve a W25 finding yourself either** — any
   findings this pass -> chain-load `cross-linker`; next tool call is Read
   on `cross-linker`'s SKILL.md, no acting tool call beside it (this skill
   only surfaces W25, cross-linker applies or reports the fix). **Never
   resolve a W13 unknown-tag or W27 empty-tag finding yourself either** —
   an alias→canonical remap you fix inline (Mechanical vs judgment table
   below), but a tag in neither the canonical list nor its aliases, or a
   page with no tags at all, is a taxonomy decision -> chain-load
   `tag-taxonomy`; next tool call is Read on `tag-taxonomy`'s SKILL.md, no
   acting tool call beside it (this skill surfaces W13/W27, tag-taxonomy
   proposes the vocabulary change or the remap/drop).
5. **Manual lore pass** on whatever the automated sweep flagged or you
   touched — see [references/manual-lore-review.md](references/manual-lore-review.md)
   for the temporal-consistency technique the table can't run itself.
   `LT5: <contradictions found, or none>`.
6. **Stop** when only findings a human/canon-review must rule on remain;
   report them, don't guess. `LT6: <items surfaced, or N/A — clean>`.
7. **A recurring shape no rule in the table flags** → `npm run lint -- --rules`
   § When to add a rule (add the rule first), then work the findings.

## WIKI-LINT block format

`npm run lint -- --rules` § Finding format owns the literal
template every WIKI-LINT block in this repo follows — read it there, not
restated here. One block per finding, never batched into prose paragraphs
— a block a reader can't grep for the fix line is a block that gets
skimmed, not obeyed.

## Mechanical vs judgment — what this skill may edit directly

Shape-only corrections (fix directly) vs. calls that need real judgment (report,
never fix silently) — the full table plus the design principle it holds the line
on: `references/mechanical-vs-judgment.md`.

## Reference files

| File | Read when |
|---|---|
| `references/backlog-drain.md` | Invoked bare — leading the drain waves (DR1–DR7) |
| `references/manual-lore-review.md` | Running the manual lore pass (step 5) — the temporal-consistency technique the automated table can't run itself |
| `references/mechanical-vs-judgment.md` | Deciding whether a finding is safe to fix directly or must be reported for a human/canon-review call |

## Relationship to other skills

- **canon-review** — drains what this skill only surfaces (W9, W16, W17,
  W18, manual-pass contradictions); this skill never picks a winner.
- **cross-linker** (W25) and **tag-taxonomy** (W13/W27) — drain the
  findings loop step 4 hands them; the mechanical alias→canonical remap
  stays here.
- **Every other campaign skill's own "lint before done" step** — this
  skill's bulk counterpart, not a replacement (contract item 3).
