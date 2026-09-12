import test from 'node:test';
import assert from 'node:assert';
import { analyze } from './prose-shape.mjs';

const monotone = `# T\n\n## A\nHe walked out. The sea kept what it took.\n\n## B\nShe paid him. Grief is a patient creditor.\n\n## C\nThey sailed. The doctrine holds.\n`;

test('flags repeated epigram endings', () => {
  const r = analyze(monotone);
  assert.equal(r.sections.length, 3);
  assert.ok(r.ending_counts.epigram >= 3);
  assert.ok(r.flags.some(f => f.includes('ending shape')));
});

test('clean when endings vary', () => {
  const varied = `# T\n\n## A\nHe walked out through the fish-gut smell of the lower docks.\n\n## B\n"Bring the rope," she said, and did not look back at him.\n\n## C\nThey counted out forty-one coins onto the wet planking of the pier.\n`;
  assert.equal(analyze(varied).flags.length, 0);
});
