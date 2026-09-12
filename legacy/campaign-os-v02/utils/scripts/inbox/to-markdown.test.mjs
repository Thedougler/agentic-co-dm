// Colocated CLI-level tests for scripts/inbox/to-markdown.mjs. Runs the real
// script as a subprocess against an isolated temp sandbox (INBOX_REPO_ROOT),
// never the real repo's inbox/.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, writeFileSync, readFileSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const CLI = fileURLToPath(new URL('./to-markdown.mjs', import.meta.url));

function sandbox() {
  const root = mkdtempSync(path.join(tmpdir(), 'inbox-to-markdown-test-'));
  mkdirSync(path.join(root, 'inbox'), { recursive: true });
  return root;
}

/** @param {string[]} args @param {string} root */
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

test('errors clearly when the file does not exist under inbox/', () => {
  assert.throws(() => run(['-f', 'nope.pdf'], sandbox()), exitedWithStatusOne);
});

test('skips a file that is already markdown', () => {
  const root = sandbox();
  writeFileSync(path.join(root, 'inbox', 'note.md'), '# note\n');
  const out = run(['-f', 'note.md'], root);
  assert.match(out, /already markdown\/text/);
});

test('skips a plain text file', () => {
  const root = sandbox();
  writeFileSync(path.join(root, 'inbox', 'note.txt'), 'hello\n');
  const out = run(['-f', 'note.txt'], root);
  assert.match(out, /already markdown\/text/);
});

test('never generates a companion for a PDF, and points to anthropic-skills:pdf', () => {
  const root = sandbox();
  writeFileSync(path.join(root, 'inbox', 'sheet.pdf'), '%PDF-1.4 fake');
  const out = run(['-f', 'sheet.pdf'], root);
  assert.match(out, /anthropic-skills:pdf/);
  assert.ok(!existsSync(path.join(root, 'inbox', 'sheet.md')));
});

test('refuses to overwrite an existing sibling .md file', () => {
  const root = sandbox();
  writeFileSync(path.join(root, 'inbox', 'page.html'), '<html><body><p>hi</p></body></html>');
  writeFileSync(path.join(root, 'inbox', 'page.md'), 'already here\n');
  assert.throws(() => run(['-f', 'page.html'], root), exitedWithStatusOne);
});

test('converts an HTML file to a sibling .md file and leaves the original untouched', () => {
  const root = sandbox();
  const html = '<html><body><h1>Title</h1><p>Some text.</p></body></html>';
  writeFileSync(path.join(root, 'inbox', 'page.html'), html);
  const out = run(['-f', 'page.html'], root);
  assert.match(out, /Wrote page\.md/);

  const mdPath = path.join(root, 'inbox', 'page.md');
  assert.ok(existsSync(mdPath));
  const md = readFileSync(mdPath, 'utf8');
  assert.match(md, /Title/);
  assert.match(md, /Some text/);

  const original = readFileSync(path.join(root, 'inbox', 'page.html'), 'utf8');
  assert.equal(original, html);
});
