// REFACTOR-PLAN.md P1.2 — real CLI subprocess against the actual script,
// CAMPAIGN_ROOT override pattern.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const repoRoot = dirname(fileURLToPath(import.meta.url));
const script = join(repoRoot, 'rerun-check.mjs');

function runCheck(args) {
  try {
    const stdout = execFileSync('node', [script, ...args], { cwd: repoRoot, encoding: 'utf8' });
    return { status: 0, stdout };
  } catch (err) {
    return { status: err.status, stdout: err.stdout ?? '' };
  }
}

test('rerun-check --cmd: prints VERDICT: PASS and exits 0 on a succeeding command', () => {
  const { status, stdout } = runCheck(['--cmd', 'true']);
  assert.equal(status, 0);
  assert.match(stdout, /VERDICT: PASS/);
});

test('rerun-check --cmd: prints VERDICT: FAIL and exits 1 on a failing command', () => {
  const { status, stdout } = runCheck(['--cmd', 'false']);
  assert.equal(status, 1);
  assert.match(stdout, /VERDICT: FAIL/);
});

test('rerun-check: an unknown check name is a usage error, not a silent no-op', () => {
  const { status } = runCheck(['not-a-real-check']);
  assert.equal(status, 1);
});

test('rerun-check: no arguments is a usage error', () => {
  const { status } = runCheck([]);
  assert.equal(status, 1);
});

test('rerun-check test: runs node --test against exactly the given file and passes', () => {
  const { status, stdout } = runCheck(['test', 'utils/scripts/rerun-check.test.mjs']);
  assert.equal(status, 0);
  assert.match(stdout, /VERDICT: PASS/);
});
