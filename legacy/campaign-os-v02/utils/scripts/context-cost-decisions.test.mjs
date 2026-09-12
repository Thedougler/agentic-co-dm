// context-cost-decisions.mjs — the optimize-wiki-context-size ledger.
// Every test points cachePath/ledgerPath/absPath at a throwaway tmp dir
// (never the real repo's own .claude/.context-cost.json or ledger, which
// are non-deterministic run to run) — same isolation pattern as
// auto-drain.test.mjs.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, writeFileSync, statSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { REPO_ROOT } from './lib/prose-scope.mjs';
import {
  computeFilter,
  entryStatus,
  claimPaths,
  resolvePath,
  listLedger,
  loadLedger,
  toRelPath,
} from './context-cost-decisions.mjs';

function scratchDir() {
  return mkdtempSync(join(tmpdir(), 'context-cost-decisions-'));
}

function writeCache(dir, rows) {
  const cachePath = join(dir, 'cache.json');
  writeFileSync(cachePath, JSON.stringify({ generatedAt: new Date().toISOString(), sinceDays: '24h', rows }));
  return cachePath;
}

const LIMITS = { cooldownDays: 14, claimTimeoutMinutes: 120, respikePct: 20 };

// --- computeFilter: ratio + bucketing + top5 ---

test('computeFilter computes ratio from real tokens_total fields, no content_tokens needed', () => {
  const dir = scratchDir();
  const cachePath = writeCache(dir, [
    { path: join(REPO_ROOT, 'vault/campaigns/foo.md'), tokens_total: 300 },
    { path: join(REPO_ROOT, 'CLAUDE.md'), tokens_total: 100 },
  ]);
  const ledgerPath = join(dir, 'ledger.json');
  const result = computeFilter({ cachePath, ledgerPath, limits: LIMITS });
  assert.equal(result.ratio, 300 / 400);
});

test('computeFilter excludes synthetic <...> rows from both buckets and candidacy', () => {
  const dir = scratchDir();
  const cachePath = writeCache(dir, [
    { path: '<unattributed:text-only-turns>', tokens_total: 999_999 },
    { path: join(REPO_ROOT, 'CLAUDE.md'), tokens_total: 100 },
  ]);
  const ledgerPath = join(dir, 'ledger.json');
  const result = computeFilter({ cachePath, ledgerPath, limits: LIMITS });
  assert.equal(result.ratio, 0);
  assert.deepEqual(result.top5.map((r) => r.path), ['CLAUDE.md']);
});

test('computeFilter ranks in-scope (non-vault) rows by tokens_total descending, caps at 5', () => {
  const dir = scratchDir();
  const rows = [];
  for (let i = 0; i < 8; i++) rows.push({ path: join(REPO_ROOT, `.claude/skills/s${i}/SKILL.md`), tokens_total: i * 10 });
  const cachePath = writeCache(dir, rows);
  const ledgerPath = join(dir, 'ledger.json');
  const result = computeFilter({ cachePath, ledgerPath, limits: LIMITS });
  assert.equal(result.top5.length, 5);
  assert.deepEqual(result.top5.map((r) => r.tokens_total), [70, 60, 50, 40, 30]);
});

// --- entryStatus: claim / cooldown / expiry / respike / stale-mtime ---

test('entryStatus: a fresh claim is active-claim, excluded', () => {
  const now = Date.now();
  const entry = { action: 'claimed', decided_at: new Date(now - 5000).toISOString() };
  assert.equal(entryStatus(entry, { now, limits: LIMITS }), 'active-claim');
});

test('entryStatus: a claim older than the timeout is expired, re-eligible', () => {
  const now = Date.now();
  const entry = { action: 'claimed', decided_at: new Date(now - 121 * 60_000).toISOString() };
  assert.equal(entryStatus(entry, { now, limits: LIMITS }), 'expired');
});

test('entryStatus: a fresh resolved decision is on cooldown', () => {
  const now = Date.now();
  const entry = { action: 'kept-necessary', decided_at: new Date(now - 1000).toISOString(), tokens_total_at_decision: 1000 };
  assert.equal(entryStatus(entry, { currentTokens: 1000, now, limits: LIMITS }), 'cooldown');
});

test('entryStatus: a decision past the cooldown window is expired', () => {
  const now = Date.now();
  const entry = { action: 'kept-necessary', decided_at: new Date(now - 15 * 86_400_000).toISOString(), tokens_total_at_decision: 1000 };
  assert.equal(entryStatus(entry, { currentTokens: 1000, now, limits: LIMITS }), 'expired');
});

test('entryStatus: tokens growing >= respikePct breaks cooldown early even inside the window', () => {
  const now = Date.now();
  const entry = { action: 'kept-necessary', decided_at: new Date(now - 1000).toISOString(), tokens_total_at_decision: 1000 };
  assert.equal(entryStatus(entry, { currentTokens: 1199, now, limits: LIMITS }), 'cooldown'); // +19.9%, under threshold
  assert.equal(entryStatus(entry, { currentTokens: 1200, now, limits: LIMITS }), 'respiked'); // +20%, at threshold
});

test('entryStatus: a file edited after its decision (mtime > decided_at) is stale-mtime, re-eligible', () => {
  const dir = scratchDir();
  const absPath = join(dir, 'file.md');
  writeFileSync(absPath, 'content');
  const fileMtime = statSync(absPath).mtimeMs;

  const decidedBeforeEdit = { action: 'kept-necessary', decided_at: new Date(fileMtime - 5000).toISOString(), tokens_total_at_decision: 1000 };
  assert.equal(entryStatus(decidedBeforeEdit, { currentTokens: 1000, absPath, now: fileMtime + 1000, limits: LIMITS }), 'stale-mtime');

  const decidedAfterEdit = { action: 'kept-necessary', decided_at: new Date(fileMtime + 5000).toISOString(), tokens_total_at_decision: 1000 };
  assert.equal(entryStatus(decidedAfterEdit, { currentTokens: 1000, absPath, now: fileMtime + 6000, limits: LIMITS }), 'cooldown');
});

// --- claimPaths / resolvePath / loadLedger round-trip ---

test('claimPaths writes a claimed entry per path, loadLedger reads it back', () => {
  const dir = scratchDir();
  const ledgerPath = join(dir, 'ledger.json');
  claimPaths(['CLAUDE.md', 'docs/guardrails/CODE.md'], { session: 's1', ledgerPath, now: Date.now() });
  const { decisions } = loadLedger(ledgerPath);
  assert.equal(decisions['CLAUDE.md'].action, 'claimed');
  assert.equal(decisions['docs/guardrails/CODE.md'].session_id, 's1');
});

test('resolvePath overwrites a claim with the final decision', () => {
  const dir = scratchDir();
  const ledgerPath = join(dir, 'ledger.json');
  claimPaths(['CLAUDE.md'], { ledgerPath, now: Date.now() });
  resolvePath('CLAUDE.md', { verdict: '1-necessity', action: 'kept-necessary', tokens: 500, note: 'still needed', ledgerPath, now: Date.now() });
  const { decisions } = loadLedger(ledgerPath);
  assert.equal(decisions['CLAUDE.md'].action, 'kept-necessary');
  assert.equal(decisions['CLAUDE.md'].tokens_total_at_decision, 500);
});

test('resolvePath rejects an invalid action or verdict', () => {
  const dir = scratchDir();
  const ledgerPath = join(dir, 'ledger.json');
  assert.throws(() => resolvePath('x.md', { verdict: '1-necessity', action: 'bogus', tokens: 1, ledgerPath }), /action/);
  assert.throws(() => resolvePath('x.md', { verdict: 'bogus', action: 'edited', tokens: 1, ledgerPath }), /verdict/);
});

test('loadLedger on a missing file returns empty decisions, never throws', () => {
  const dir = scratchDir();
  assert.deepEqual(loadLedger(join(dir, 'nope.json')), { decisions: {} });
});

test('loadLedger on a corrupt file returns empty decisions, never throws', () => {
  const dir = scratchDir();
  const ledgerPath = join(dir, 'ledger.json');
  writeFileSync(ledgerPath, '{not json');
  assert.deepEqual(loadLedger(ledgerPath), { decisions: {} });
});

test('toRelPath normalizes an absolute repo path and leaves a relative one alone', () => {
  assert.equal(toRelPath('docs/guardrails/CODE.md'), 'docs/guardrails/CODE.md');
});

// --- the actual duplicate-effort proof: a resolved file drops out of top5 ---

test('computeFilter excludes a resolved kept-necessary file from top5 (the RED->GREEN case)', () => {
  const dir = scratchDir();
  const cachePath = writeCache(dir, [
    { path: join(REPO_ROOT, 'docs/guardrails/WIKI.md'), tokens_total: 147_717 },
    { path: join(REPO_ROOT, '.claude/skills/faction-prep/SKILL.md'), tokens_total: 140_481 },
  ]);
  const ledgerPath = join(dir, 'ledger.json');

  const before = computeFilter({ cachePath, ledgerPath, limits: LIMITS });
  assert.equal(before.top5[0].path, 'docs/guardrails/WIKI.md');

  resolvePath('docs/guardrails/WIKI.md', {
    verdict: '1-necessity',
    action: 'kept-necessary',
    tokens: 147_717,
    note: 'confirmed necessary',
    ledgerPath,
    now: Date.now(),
  });

  const after = computeFilter({ cachePath, ledgerPath, limits: LIMITS });
  assert.deepEqual(after.top5.map((r) => r.path), ['.claude/skills/faction-prep/SKILL.md']);
  assert.equal(after.skipped_cooldown.length, 1);
  assert.equal(after.skipped_cooldown[0].path, 'docs/guardrails/WIKI.md');
});

// --- listLedger ---

test('listLedger surfaces the computed status alongside each entry', () => {
  const dir = scratchDir();
  const ledgerPath = join(dir, 'ledger.json');
  claimPaths(['CLAUDE.md'], { ledgerPath, now: Date.now() });
  const list = listLedger({ ledgerPath, now: Date.now(), limits: LIMITS });
  assert.equal(list.length, 1);
  assert.equal(list[0].status, 'active-claim');
});
