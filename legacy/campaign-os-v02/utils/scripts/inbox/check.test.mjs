// Colocated CLI-level tests for scripts/inbox/check.mjs. Runs the real
// script as a subprocess against an isolated temp sandbox (INBOX_REPO_ROOT),
// never the real repo's inbox/.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const CLI = fileURLToPath(new URL('./check.mjs', import.meta.url));

function sandbox() {
  const root = mkdtempSync(path.join(tmpdir(), 'inbox-check-test-'));
  mkdirSync(path.join(root, 'inbox'), { recursive: true });
  return root;
}

/** @param {string} root */
function run(root) {
  return execFileSync('node', [CLI], {
    encoding: 'utf8',
    env: { ...process.env, INBOX_REPO_ROOT: root },
  });
}

test('reports an empty inbox/', () => {
  const out = run(sandbox());
  assert.match(out, /inbox is empty — nothing to check\./);
});

test('lists a new file under NEW', () => {
  const root = sandbox();
  writeFileSync(path.join(root, 'inbox', 'note.md'), '# A note\n');
  const out = run(root);
  assert.match(out, /NEW \(needs ingesting\):/);
  assert.match(out, /- note\.md/);
});

test('lists a nested file with its relative path', () => {
  const root = sandbox();
  mkdirSync(path.join(root, 'inbox', 'sub'), { recursive: true });
  writeFileSync(path.join(root, 'inbox', 'sub', 'note.md'), '# A note\n');
  const out = run(root);
  assert.match(out, /- sub[\\/]note\.md/);
});
