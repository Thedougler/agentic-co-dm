// Colocated CLI-level tests for scripts/inbox/similar.mjs, covering the
// argument-validation and file-resolution paths (fast, no external state).
// qmd's search output itself is an integration concern rather than a unit
// test — it depends on the real "wiki" collection's index and embeddings.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, mkdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const CLI = fileURLToPath(new URL('./similar.mjs', import.meta.url));

function sandbox() {
  const root = mkdtempSync(path.join(tmpdir(), 'inbox-similar-test-'));
  mkdirSync(path.join(root, 'inbox'), { recursive: true });
  return root;
}

/**
 * @param {string[]} args
 * @param {string} root
 */
function run(args, root) {
  return execFileSync('node', [CLI, ...args], {
    encoding: 'utf8',
    env: { ...process.env, INBOX_REPO_ROOT: root },
  });
}

/** @param {any} err */
const exitedWithStatusOne = (err) => err.status === 1;

test('errors when -f is missing', () => {
  assert.throws(() => run([], sandbox()), exitedWithStatusOne);
});

test('errors clearly when the file does not exist under inbox/ or raw/', () => {
  assert.throws(() => run(['-f', 'nope.md'], sandbox()), exitedWithStatusOne);
});
