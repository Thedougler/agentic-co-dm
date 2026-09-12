#!/usr/bin/env node
// context-cost-decisions — the optimize-wiki-context-size skill's
// duplicate-effort guard. OC1-OC6 (SKILL.md) used to re-derive its top-5
// from .claude/.context-cost.json fresh every invocation with nothing
// recording which files a prior run already investigated or fixed, so a
// file confirmed "necessary, no action" got the identical re-investigation
// every subsequent run, and two concurrent invocations could both start
// editing the same files. This script is the persistent ledger that closes
// both gaps.
//
//   node utils/scripts/context-cost-decisions.mjs filter
//   node utils/scripts/context-cost-decisions.mjs claim <path...> [--session <id>]
//   node utils/scripts/context-cost-decisions.mjs resolve <path> --verdict <1-5> --action <deleted|edited|kept-necessary|misleader-fixed> --tokens <N> [--note "..."]
//   node utils/scripts/context-cost-decisions.mjs list
//
// Ledger lives at .claude/.context-cost-decisions.json, keyed by
// repo-relative path — unlike the wholly-regenerated .context-cost.json
// cache (gitignored), this file is tracked in git: it is the durable
// cross-session/cross-clone record the whole mechanism depends on.
//
// `claim` is the concurrency lock: OC1 writes one for each of its chosen
// top-5 before OC2 investigation starts, so a concurrent invocation's
// `filter` call sees them and skips those paths. A claim older than
// CONTEXT_COST_CLAIM_TIMEOUT_MINUTES is abandoned, never permanently
// blocking — a run that died mid-pass cannot deadlock a file forever.
//
// `resolve` is OC6's write: it replaces the claim with the final verdict.
// A resolved decision keeps its path off `filter`'s candidate list for
// CONTEXT_COST_DECISION_COOLDOWN_DAYS, unless either breaks the cooldown
// early: tokens_total grew >= CONTEXT_COST_RESPIKE_PCT% past the decision
// (a real regression), or the file's mtime is newer than the decision (its
// content changed since, so the decision is stale).
import { readFileSync, writeFileSync, statSync, existsSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { REPO_ROOT } from './lib/prose-scope.mjs';

export const CACHE_PATH = path.join(REPO_ROOT, '.claude/.context-cost.json');
export const LEDGER_PATH = path.join(REPO_ROOT, '.claude/.context-cost-decisions.json');

const VALID_ACTIONS = ['claimed', 'deleted', 'edited', 'kept-necessary', 'misleader-fixed'];
const VALID_VERDICTS = ['1-necessity', '2-progressive-disclosure', '3-erroneous-read', '4-conflict', '5-unclear'];

function _readTomlThreshold(key, defaultValue) {
  try {
    const raw = readFileSync(path.join(REPO_ROOT, 'wiki.toml'), 'utf8');
    for (const line of raw.split('\n')) {
      const m = line.match(new RegExp(`^${key}\\s*=\\s*"(\\d+)"`));
      if (m) return Number(m[1]);
    }
  } catch { /* wiki.toml missing or unreadable */ }
  return defaultValue;
}

export function thresholds() {
  return {
    cooldownDays: _readTomlThreshold('CONTEXT_COST_DECISION_COOLDOWN_DAYS', 14),
    claimTimeoutMinutes: _readTomlThreshold('CONTEXT_COST_CLAIM_TIMEOUT_MINUTES', 120),
    respikePct: _readTomlThreshold('CONTEXT_COST_RESPIKE_PCT', 20),
  };
}

/** Repo-relative, forward-slash path — the ledger's key shape, portable across machines/clones. */
export function toRelPath(p) {
  const rel = path.isAbsolute(p) ? path.relative(REPO_ROOT, p) : p;
  return rel.split(path.sep).join('/');
}

/** {decisions: {}} on a missing or unparseable ledger file — never throws. */
export function loadLedger(ledgerPath = LEDGER_PATH) {
  try {
    const parsed = JSON.parse(readFileSync(ledgerPath, 'utf8'));
    return { decisions: parsed.decisions && typeof parsed.decisions === 'object' ? parsed.decisions : {} };
  } catch {
    return { decisions: {} };
  }
}

export function saveLedger(decisions, ledgerPath = LEDGER_PATH) {
  writeFileSync(ledgerPath, `${JSON.stringify({ decisions }, null, 2)}\n`);
}

/** mtime in ms, or null when the file doesn't exist (never throws). */
function mtimeMs(absPath) {
  try {
    return statSync(absPath).mtimeMs;
  } catch {
    return null;
  }
}

// Excluded from cooldown/candidacy entirely: the transcript engine's own
// synthetic rows (`<unattributed:text-only-turns>`, `<other:Bash>`, ...)
// carry no real file to investigate or claim.
function isRealFileRow(row) {
  return typeof row.path === 'string' && !row.path.startsWith('<');
}

/**
 * Live cooldown/claim status for one ledger entry against current state.
 * Returns 'active-claim' | 'cooldown' | 'expired' | 'respiked' | 'stale-mtime'.
 * 'expired'/'respiked'/'stale-mtime' all mean: not excluded, eligible again.
 */
export function entryStatus(entry, { currentTokens, absPath, now = Date.now(), limits = thresholds() } = {}) {
  const decidedAt = Date.parse(entry.decided_at);
  const ageMs = now - decidedAt;

  if (entry.action === 'claimed') {
    return ageMs < limits.claimTimeoutMinutes * 60_000 ? 'active-claim' : 'expired';
  }

  if (ageMs >= limits.cooldownDays * 86_400_000) return 'expired';

  const mt = absPath ? mtimeMs(absPath) : null;
  if (mt != null && mt > decidedAt) return 'stale-mtime';

  const priorTokens = entry.tokens_total_at_decision;
  if (typeof currentTokens === 'number' && typeof priorTokens === 'number' && priorTokens > 0) {
    const growthPct = ((currentTokens - priorTokens) / priorTokens) * 100;
    if (growthPct >= limits.respikePct) return 'respiked';
  }

  return 'cooldown';
}

function isExcluded(status) {
  return status === 'active-claim' || status === 'cooldown';
}

/**
 * OC1's ranking step: buckets the snapshot cache, computes the real
 * ratio (sum tokens_total per bucket — the cache has no
 * content_tokens/non_content_tokens fields to divide directly), excludes
 * ledger-cooled/claimed paths from candidacy, returns the top 5 plus what
 * got skipped and why.
 */
export function computeFilter({ cachePath = CACHE_PATH, ledgerPath = LEDGER_PATH, now = Date.now(), limits = thresholds() } = {}) {
  const cache = JSON.parse(readFileSync(cachePath, 'utf8'));
  const { decisions } = loadLedger(ledgerPath);

  const rows = (cache.rows ?? []).filter(isRealFileRow);
  let vaultTokens = 0;
  let totalTokens = 0;
  const inScope = [];

  for (const row of rows) {
    const rel = toRelPath(row.path);
    totalTokens += row.tokens_total ?? 0;
    if (rel.startsWith('vault/')) {
      vaultTokens += row.tokens_total ?? 0;
      continue;
    }
    inScope.push({ ...row, rel });
  }

  const candidates = [];
  const skipped = [];
  for (const row of inScope) {
    const entry = decisions[row.rel];
    if (!entry) {
      candidates.push(row);
      continue;
    }
    const status = entryStatus(entry, { currentTokens: row.tokens_total, absPath: row.path, now, limits });
    if (isExcluded(status)) {
      skipped.push({ path: row.rel, reason: status, tokens_total: row.tokens_total });
    } else {
      candidates.push(row);
    }
  }

  candidates.sort((a, b) => b.tokens_total - a.tokens_total);
  const top5 = candidates.slice(0, 5).map((r) => ({ path: r.rel, tokens_total: r.tokens_total }));

  return {
    ratio: totalTokens > 0 ? vaultTokens / totalTokens : null,
    top5,
    skipped_cooldown: skipped,
  };
}

export function claimPaths(paths, { session = 'unknown', ledgerPath = LEDGER_PATH, now = Date.now() } = {}) {
  const { decisions } = loadLedger(ledgerPath);
  const decidedAt = new Date(now).toISOString();
  for (const p of paths) {
    decisions[toRelPath(p)] = { action: 'claimed', verdict: null, tokens_total_at_decision: null, decided_at: decidedAt, session_id: session, note: null };
  }
  saveLedger(decisions, ledgerPath);
  return paths.map(toRelPath);
}

export function resolvePath(p, { verdict, action, tokens, note = '', session = 'unknown', ledgerPath = LEDGER_PATH, now = Date.now() }) {
  if (!VALID_ACTIONS.includes(action)) throw new Error(`resolve: --action must be one of ${VALID_ACTIONS.join(', ')}, got ${JSON.stringify(action)}`);
  if (!VALID_VERDICTS.includes(verdict)) throw new Error(`resolve: --verdict must be one of ${VALID_VERDICTS.join(', ')}, got ${JSON.stringify(verdict)}`);
  if (typeof tokens !== 'number' || Number.isNaN(tokens)) throw new Error(`resolve: --tokens must be a number, got ${JSON.stringify(tokens)}`);

  const { decisions } = loadLedger(ledgerPath);
  const rel = toRelPath(p);
  decisions[rel] = { action, verdict, tokens_total_at_decision: tokens, decided_at: new Date(now).toISOString(), session_id: session, note };
  saveLedger(decisions, ledgerPath);
  return rel;
}

export function listLedger({ ledgerPath = LEDGER_PATH, now = Date.now(), limits = thresholds() } = {}) {
  const { decisions } = loadLedger(ledgerPath);
  return Object.entries(decisions).map(([rel, entry]) => ({
    path: rel,
    ...entry,
    status: entryStatus(entry, { currentTokens: undefined, absPath: path.join(REPO_ROOT, rel), now, limits }),
  }));
}

function parseFlags(argv) {
  const positional = [];
  const flags = {};
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith('--')) {
      flags[a.slice(2)] = argv[i + 1];
      i++;
    } else {
      positional.push(a);
    }
  }
  return { positional, flags };
}

function main(argv) {
  const [cmd, ...rest] = argv;
  const { positional, flags } = parseFlags(rest);

  if (cmd === 'filter') {
    if (!existsSync(CACHE_PATH)) {
      console.log(JSON.stringify({ ratio: null, top5: [], skipped_cooldown: [], note: 'no .claude/.context-cost.json — run npm run context-cost:snapshot first' }, null, 2));
      return;
    }
    console.log(JSON.stringify(computeFilter(), null, 2));
    return;
  }

  if (cmd === 'claim') {
    if (positional.length === 0) throw new Error('claim: at least one path is required');
    const claimed = claimPaths(positional, { session: flags.session ?? 'unknown' });
    console.log(`claimed: ${claimed.join(', ')}`);
    return;
  }

  if (cmd === 'resolve') {
    const [p] = positional;
    if (!p) throw new Error('resolve: a path is required');
    const rel = resolvePath(p, {
      verdict: flags.verdict,
      action: flags.action,
      tokens: Number(flags.tokens),
      note: flags.note ?? '',
      session: flags.session ?? 'unknown',
    });
    console.log(`resolved: ${rel} -> ${flags.action} (${flags.verdict})`);
    return;
  }

  if (cmd === 'list') {
    console.log(JSON.stringify(listLedger(), null, 2));
    return;
  }

  throw new Error(`unknown subcommand ${JSON.stringify(cmd)} — expected filter | claim | resolve | list`);
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  main(process.argv.slice(2));
}
