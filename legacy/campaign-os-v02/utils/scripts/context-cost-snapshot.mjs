#!/usr/bin/env node
// context-cost-snapshot — caches real, billed per-file token cost for this
// repo's own instructional surfaces (.claude/, docs/guardrails/, _templates/,
// CLAUDE.md files), sourced from `session-transcripts`' transcripts.py
// context-cost subcommand. `optimize-wiki-context-size` reads the cache this
// writes on manual invocation (docs/adr/0039 — `npm run lint` no longer
// reads it).
//
//   npm run context-cost:snapshot
//
// Real session-transcript history is external to this repo and not
// guaranteed present (a fresh clone, CI, another machine) — missing data is
// not an error here: exit 0, write nothing, and the reader-side consumer
// degrades to silent. Not wired into the pre-commit hook; run manually or
// from a periodic job, same cadence class as `npm run lint:bench`.
//
// --with-friction adds corrections_after/errs_after/turns_resident/
// friction_sessions to every row (additive — `optimize-wiki-context-size`
// only reads path/reads/tokens_total/trend_pct and is unaffected). Deeper
// views (--timeline, --buckets N) aren't cached here — run transcripts.py
// context-cost directly for those; see session-transcripts/reference.md.
import { existsSync, mkdirSync, writeFileSync } from 'node:fs';
import { homedir } from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { REPO_ROOT } from './lib/prose-scope.mjs';

const CACHE_PATH = path.join(REPO_ROOT, '.claude/.context-cost.json');
const TRANSCRIPTS_PY = path.join(homedir(), '.claude/skills/session-transcripts/transcripts.py');
const SINCE = process.argv.find((a) => a.startsWith('--since='))?.split('=')[1] ?? '24h';

function main() {
  if (!existsSync(TRANSCRIPTS_PY)) {
    console.log(`context-cost-snapshot: no session-transcripts engine at ${TRANSCRIPTS_PY} — skipping, no cache written.`);
    process.exit(0);
  }

  const r = spawnSync(
    'python3',
    [TRANSCRIPTS_PY, 'context-cost', '--repo', REPO_ROOT, '--since', SINCE, '--with-friction', '--json'],
    { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 },
  );
  if (r.error || r.status == null) {
    console.log(`context-cost-snapshot: could not run transcripts.py (${r.error?.message ?? 'no exit status'}) — skipping, no cache written.`);
    process.exit(0);
  }

  const rows = [];
  for (const line of (r.stdout ?? '').split('\n')) {
    if (!line.trim()) continue;
    try {
      rows.push(JSON.parse(line));
    } catch {
      // one malformed row is not worth failing the whole snapshot over — skip it, keep the rest.
    }
  }
  if (rows.length === 0) {
    console.log('context-cost-snapshot: no rows in this window (empty session history, or nothing matched) — no cache written.');
    process.exit(0);
  }

  mkdirSync(path.dirname(CACHE_PATH), { recursive: true });
  writeFileSync(CACHE_PATH, JSON.stringify({ generatedAt: new Date().toISOString(), sinceDays: SINCE, rows }, null, 2));
  console.log(`context-cost-snapshot: wrote ${rows.length} row(s) to ${path.relative(REPO_ROOT, CACHE_PATH)}`);
}

main();
