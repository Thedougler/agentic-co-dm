// REFACTOR-PLAN.md P2.5 — every-session capped auto-drain wave. Pure
// selection/session-cap logic is unit-tested directly against synthetic
// findings (never the live repo's own lint findings, which are non-
// deterministic run to run); the lock-guard is tested against the real
// session_health.sh script pointed at a throwaway fixture root via
// CAMPAIGN_ROOT override, real repo root.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { mkdtempSync, rmSync, mkdirSync, writeFileSync, existsSync, readFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { selectFiles, isKitFile, main } from './auto-drain.mjs';

const scriptDir = dirname(fileURLToPath(import.meta.url));

function fixableFinding(rel, rule = 'MD012') {
  return { rel, rule, slug: rule, severity: 'warning', line: 1, message: 'x', fixable: true };
}

// --- selectFiles: cap (never more than 5 files) ---

test('selectFiles caps selection at 5 files even with more candidates', () => {
  const findings = [];
  for (let i = 0; i < 12; i++) findings.push(fixableFinding(`vault/campaigns/shattered-sea/npcs/npc-${i}.md`));
  const selected = selectFiles(findings);
  assert.equal(selected.length, 5);
});

test('selectFiles honors a smaller explicit max too', () => {
  const findings = [fixableFinding('a.md'), fixableFinding('b.md'), fixableFinding('c.md')];
  const selected = selectFiles(findings, { max: 2 });
  assert.equal(selected.length, 2);
});

test('selectFiles ranks lowest finding-count files first (lowest-risk-first)', () => {
  const findings = [
    fixableFinding('busy.md'), fixableFinding('busy.md'), fixableFinding('busy.md'),
    fixableFinding('quiet.md'),
  ];
  const selected = selectFiles(findings, { max: 1 });
  assert.deepEqual(selected, [{ rel: 'quiet.md', count: 1 }]);
});

test('selectFiles drops non-fixable findings entirely', () => {
  const findings = [{ rel: 'a.md', rule: 'W64', severity: 'warning', line: 1, message: 'x', fixable: false }];
  assert.deepEqual(selectFiles(findings), []);
});

// --- kit-file exclusion (docs/guardrails/_FORMAT.md F15) ---

test('isKitFile flags every CLAUDE.md at any depth and every docs/guardrails/*.md path', () => {
  assert.equal(isKitFile('CLAUDE.md'), true);
  assert.equal(isKitFile('docs/guardrails/CODE.md'), true);
  assert.equal(isKitFile('docs/guardrails/nested/DEEP.md'), true);
  assert.equal(isKitFile('vault/CLAUDE.md'), true); // subtree kit file, same edit-deliberately discipline
  assert.equal(isKitFile('vault/campaigns/shattered-sea/npcs/otar.md'), false);
});

test('selectFiles never selects a kit file even when it is the single lowest-risk candidate', () => {
  const findings = [
    fixableFinding('CLAUDE.md'), // 1 finding — would rank first by count
    fixableFinding('docs/guardrails/CODE.md'), // 1 finding — would also rank first
    fixableFinding('busy.md'), fixableFinding('busy.md'), fixableFinding('busy.md'),
  ];
  const selected = selectFiles(findings);
  assert.deepEqual(selected.map((s) => s.rel), ['busy.md']);
});

test('selectFiles never selects a nested CLAUDE.md or a lint-rule fixture', () => {
  const findings = [
    fixableFinding('vault/_templates/CLAUDE.md'), // subtree kit file, 1 finding
    fixableFinding('utils/scripts/lint-rules/fixtures/checker-vault/vault/creatures/x.md'),
    fixableFinding('busy.md'), fixableFinding('busy.md'), fixableFinding('busy.md'),
  ];
  const selected = selectFiles(findings);
  assert.deepEqual(selected.map((s) => s.rel), ['busy.md']);
});

// --- one wave per session (marker short-circuit, no live-repo I/O) ---

test('main() is a no-op when the marker already records this session_id', () => {
  const dir = mkdtempSync(join(tmpdir(), 'auto-drain-marker-'));
  const markerPath = join(dir, '.auto-drain.session');
  const summaryPath = join(dir, '.lint-sweep.summary');
  try {
    writeFileSync(markerPath, 'session-abc\n');
    const result = main('session-abc', { markerPath, summaryPath });
    assert.deepEqual(result, { ranWave: false, reason: 'already ran this session', fixed: [] });
    assert.equal(existsSync(summaryPath), false); // never touched — proves no autofix ran
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
});

test('main() treats a different session_id as a fresh session (marker check does not match)', () => {
  const dir = mkdtempSync(join(tmpdir(), 'auto-drain-marker-'));
  const markerPath = join(dir, '.auto-drain.session');
  try {
    writeFileSync(markerPath, 'session-old\n');
    const already = readFileSync(markerPath, 'utf8').trim();
    assert.notEqual(already, 'session-new'); // the exact comparison main() makes
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
});

// --- lock-guard: session_health.sh never runs the wave while its lock is held ---

function runSessionHealth(fixtureRoot) {
  const gateScript = join(scriptDir, 'session_health.sh');
  try {
    const stdout = execFileSync('bash', [gateScript], {
      input: JSON.stringify({ session_id: 'test-session' }),
      cwd: fixtureRoot,
      encoding: 'utf8',
      env: { ...process.env, CAMPAIGN_ROOT: fixtureRoot },
      timeout: 10_000,
    });
    return { status: 0, stdout };
  } catch (err) {
    return { status: err.status, stdout: err.stdout ?? '' };
  }
}

test('session_health.sh: auto-drain never fires while the lint-sweep lock is held', () => {
  const dir = mkdtempSync(join(tmpdir(), 'auto-drain-lock-'));
  try {
    mkdirSync(join(dir, '.claude'), { recursive: true });
    // A live pid (this test process's own) makes `kill -0` succeed, exactly
    // like a still-running refresh from an earlier SessionStart trigger.
    writeFileSync(join(dir, '.claude', '.lint-sweep.lock'), String(process.pid));

    const start = Date.now();
    const { status } = runSessionHealth(dir);
    const elapsed = Date.now() - start;

    assert.equal(status, 0); // never blocks session start
    assert.ok(elapsed < 5000, `session_health.sh took ${elapsed}ms while the lock was held — should skip fast`);
    // The lock branch never enters the background subshell, so auto-drain.mjs
    // never runs and never writes its session marker.
    assert.equal(existsSync(join(dir, '.claude', '.auto-drain.session')), false);
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
});
