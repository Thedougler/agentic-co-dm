// Colocated CLI-level tests for scripts/inbox/sweep-to-markdown.mjs. Runs the
// real script as a subprocess against an isolated temp sandbox
// (INBOX_REPO_ROOT), never the real repo's inbox/.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, writeFileSync, readFileSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const CLI = fileURLToPath(new URL('./sweep-to-markdown.mjs', import.meta.url));

function sandbox() {
  const root = mkdtempSync(path.join(tmpdir(), 'inbox-sweep-test-'));
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

test('does nothing on an empty inbox', () => {
  const out = run(sandbox());
  assert.equal(out, '');
});

test('leaves markdown/text files alone', () => {
  const root = sandbox();
  writeFileSync(path.join(root, 'inbox', 'note.md'), '# note\n');
  writeFileSync(path.join(root, 'inbox', 'note.txt'), 'hello\n');
  const out = run(root);
  assert.equal(out, '');
  assert.ok(!existsSync(path.join(root, 'inbox', 'note.md.md')));
});

test('never generates a companion for a PDF', () => {
  const root = sandbox();
  writeFileSync(path.join(root, 'inbox', 'sheet.pdf'), '%PDF-1.4 fake');
  const out = run(root);
  assert.equal(out, '');
  assert.ok(!existsSync(path.join(root, 'inbox', 'sheet.md')));
});

test('skips a file that already has a markdown companion', () => {
  const root = sandbox();
  writeFileSync(path.join(root, 'inbox', 'page.html'), '<p>hi</p>');
  writeFileSync(path.join(root, 'inbox', 'page.md'), 'hand-written already\n');
  const out = run(root);
  assert.equal(out, '');
  assert.equal(readFileSync(path.join(root, 'inbox', 'page.md'), 'utf8'), 'hand-written already\n');
});

test('converts every companion-less non-markdown file, nested included, and reports them', () => {
  const root = sandbox();
  writeFileSync(path.join(root, 'inbox', 'a.html'), '<h1>A</h1>');
  mkdirSync(path.join(root, 'inbox', 'sub'), { recursive: true });
  writeFileSync(path.join(root, 'inbox', 'sub', 'b.html'), '<h1>B</h1>');

  const out = run(root);
  assert.match(out, /Converted to markdown/);
  assert.match(out, /a\.md/);
  assert.match(out, /sub\/b\.md/);

  assert.ok(existsSync(path.join(root, 'inbox', 'a.md')));
  assert.ok(existsSync(path.join(root, 'inbox', 'sub', 'b.md')));
});
