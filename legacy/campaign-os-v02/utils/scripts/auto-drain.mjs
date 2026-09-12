#!/usr/bin/env node
// auto-drain.mjs — REFACTOR-PLAN.md P2.5: every-session, capped auto-drain
// wave, dispatched from session_health.sh's existing lock-guarded background
// pass (utils/scripts/session_health.sh's LOCK block).
//
// Design constraint this resolves: a shell SessionStart hook cannot dispatch
// a Claude Code subagent, so a real /drain wave (worklist -> agent dispatch,
// .claude/commands/drain.md) is not reachable from here. The only mechanism
// that actually does work without an agent is the deterministic autofix path
// per-edit deterministic fixers use (oxlint --fix / markdownlint-
// obsidian --fix on findings `wiki lint --json` marks `fixable: true`) —
// that's what this script runs, scoped to a capped file selection. The other
// option considered — writing a worklist file for "the session's agent to
// pick up" — was rejected: nothing forces an agent to read it, so it would
// silently no-op as often as not; a hook that only ever *prepares* work
// without a guaranteed consumer is not a drain wave, it's a file nobody
// reads. Full /drain (worklist -> subagent dispatch -> wave-verifier) stays
// the manual big lever for everything this deterministic pass can't reach.
//
// Caps enforced here, not by convention:
//   - MAX_FILES: never more than 5 files touched in one wave (selectFiles).
//   - one wave per session: session_health.sh passes the SessionStart
//     payload's session_id as argv[2]; MARKER_PATH records the last session
//     a wave ran for, and a repeat call for the same session_id (SessionStart
//     also fires on resume/clear/compact, same as the lint pass above it)
//     is a no-op (main()'s `already === id` check).
//   - lock-guarded: this script does no locking of its own — it is only ever
//     invoked from inside session_health.sh's existing LOCK-guarded
//     background subshell, so holding that lock already makes a concurrent
//     invocation a no-op (mirrors the standing lint pass exactly, no new
//     mechanism invented).
//   - kit files (root CLAUDE.md, docs/guardrails/*.md) are never selected,
//     even though routeType() below classifies both as 'wiki' scope —
//     docs/guardrails/_FORMAT.md F15 forbids a script rewriting them
//     unattended. See isKitFile().
import path from 'node:path';
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { REPO_ROOT } from './lib/prose-scope.mjs';
import { isKitFile } from './lib/kitFiles.mjs';

const WIKI_CLI_DIR = path.join(REPO_ROOT, 'utils/wiki-cli');
const MAX_FILES = 5;
export const MARKER_PATH = path.join(REPO_ROOT, '.claude/.auto-drain.session');
export const SUMMARY_PATH = path.join(REPO_ROOT, '.claude/.lint-sweep.summary');

export { isKitFile } from './lib/kitFiles.mjs';

// Lint-rule fixtures are planted violations — a file whose findings are the
// point of its existence. Autofixing one rewrites the evidence a test asserts
// against, turning a green suite red for a reason nobody watched happen.
export function isFixture(rel) {
  return rel.startsWith('utils/scripts/lint-rules/fixtures/');
}

// Mirrors wiki-cli's own routing (utils/wiki-cli's producer scoping) and
// the retired per-edit hook's 3 case-arms — kept inline since
// this is a pure path-pattern classification, not a lint call.
function routeType(rel) {
  if (/^utils\/scripts\/.*\.(mjs|js)$/.test(rel)) return 'scripts';
  if (
    /(^|\/)\.claude\/skills\/.*\.md$/.test(rel)
    || /^\.claude\/agents\/.*\.md$/.test(rel)
    || /^_templates\/.*\.md$/.test(rel)
  ) return 'skills';
  if (
    /^vault\/.*\.md$/.test(rel)
    || /(^|\/)CLAUDE\.md$/.test(rel)
    || /^docs\/guardrails\/.*\.md$/.test(rel)
    || /^\.claude\/rules\/.*\.md$/.test(rel)
    || /^\.claude\/commands\/.*\.md$/.test(rel)
  ) return 'wiki';
  return null;
}

// Shells out to the Python lint engine of record (ADR-0042/0045) and parses
// its newline-delimited JSON into the {rel, fixable, ...} shape the rest of
// this file expects. `paths` empty runs `wiki sweep` — the corpus command
// (ADR-0064); `wiki lint` takes paths and rejects an empty list. Either
// exits 1 whenever any
// gating finding exists (Law 8) — that is the expected, findings-bearing
// case here, not a failure, so a non-zero exit with stdout present is read
// the same way runOxlint/runMarkdownlint always treated a findings-bearing
// run.
function collectFindings(paths) {
  const args = paths.length > 0
    ? ['run', '--directory', WIKI_CLI_DIR, 'wiki', 'lint', '--json', ...paths]
    : ['run', '--directory', WIKI_CLI_DIR, 'wiki', 'sweep', '--json'];
  let stdout;
  try {
    stdout = execFileSync('uv', args, { cwd: REPO_ROOT, encoding: 'utf8' });
  } catch (e) {
    if (typeof e.status === 'number' && typeof e.stdout === 'string') {
      stdout = e.stdout;
    } else {
      throw e;
    }
  }
  const findings = stdout
    .split('\n')
    .filter((line) => line.trim().length > 0)
    .map((line) => {
      const f = JSON.parse(line);
      return { rel: f.path, rule: f.rule, severity: f.severity, line: f.line, message: f.message, fixable: f.fixable === true };
    });
  return { findings };
}

// Mechanically-fixable, lowest-risk-first, capped selection: only findings
// `wiki lint --json` marks `fixable: true`, kit files excluded, ranked by
// ascending fixable-finding count per file (fewer changes = lower risk),
// ties broken alphabetically for determinism, capped at `max` files.
export function selectFiles(findings, { max = MAX_FILES } = {}) {
  const byFile = new Map();
  for (const f of findings) {
    if (f.fixable !== true) continue;
    if (isKitFile(f.rel)) continue;
    if (isFixture(f.rel)) continue;
    if (!byFile.has(f.rel)) byFile.set(f.rel, []);
    byFile.get(f.rel).push(f);
  }
  return [...byFile.entries()]
    .sort((a, b) => a[1].length - b[1].length || a[0].localeCompare(b[0]))
    .slice(0, max)
    .map(([rel, fs]) => ({ rel, count: fs.length }));
}

// Runs the deterministic --fix pass per-edit, scoped
// to one file. Returns true only for a route this script actually knows how
// to autofix (scripts: oxlint; wiki: markdownlint-obsidian) — 'skills' has no
// --fix path and 'none' isn't lint-governed at all, so both
// are left alone rather than guessed at.
export function runFix(rel) {
  const type = routeType(rel);
  if (type === 'scripts') {
    const bin = path.join(REPO_ROOT, 'node_modules/.bin/oxlint');
    if (!existsSync(bin)) return false; // fail open on a broken/missing install
    execFileSync(bin, [rel, '--fix'], { cwd: REPO_ROOT, stdio: 'ignore' });
    return true;
  }
  if (type === 'wiki') {
    const bin = path.join(REPO_ROOT, 'node_modules/.bin/markdownlint-obsidian');
    if (!existsSync(bin)) return false; // fail open on a broken/missing install
    execFileSync(bin, ['--fix', rel], { cwd: REPO_ROOT, stdio: 'ignore' });
    return true;
  }
  return false;
}

// Appends/overwrites a 4th line on session_health.sh's cached summary file —
// lines 1-3 stay session_health.sh's own wiki-baseline summary format,
// untouched.
export function appendSummaryLine(line, summaryPath = SUMMARY_PATH) {
  try {
    mkdirSync(path.dirname(summaryPath), { recursive: true });
    const prev = existsSync(summaryPath) ? readFileSync(summaryPath, 'utf8').replace(/\n$/, '') : '';
    const lines = prev.length > 0 ? prev.split('\n') : [];
    while (lines.length < 3) lines.push('');
    lines[3] = line;
    writeFileSync(summaryPath, `${lines.join('\n')}\n`);
  } catch {
    // best-effort — a summary write failure never blocks or fails the wave
  }
}

export function main(sessionId, { markerPath = MARKER_PATH, summaryPath = SUMMARY_PATH } = {}) {
  const id = sessionId && sessionId.length > 0 ? sessionId : 'unknown';
  const already = existsSync(markerPath) ? readFileSync(markerPath, 'utf8').trim() : '';
  if (already === id) {
    return { ranWave: false, reason: 'already ran this session', fixed: [] };
  }

  let findings;
  try {
    ({ findings } = collectFindings([]));
  } catch (e) {
    return { ranWave: false, reason: `collectFindings failed: ${e.message}`, fixed: [] };
  }

  const selected = selectFiles(findings);
  const fixed = [];
  for (const { rel } of selected) {
    try {
      if (runFix(rel)) fixed.push(rel);
    } catch {
      // best-effort — one file's fixer failing never aborts the rest of the wave
    }
  }

  try {
    mkdirSync(path.dirname(markerPath), { recursive: true });
    writeFileSync(markerPath, `${id}\n`);
  } catch {
    // best-effort — a marker write failure means a future call may re-run
    // the wave, never that this call fails
  }

  if (fixed.length > 0) {
    appendSummaryLine(`AUTO-DRAIN: autofixed ${fixed.length} file(s) this session — ${fixed.join(', ')}.`, summaryPath);
  }

  return { ranWave: true, fixed };
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  main(process.argv[2]);
}
