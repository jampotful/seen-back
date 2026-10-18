// The decision whether this device can hold the full database (bigFits in src/cam.rec.js), run in Node with made-up devices.
// node test/rec/fits_test.js   (no browser, no server)
const fs = require('fs');
const path = require('path');
const src = fs.readFileSync(path.join(__dirname, '..', '..', 'src', 'cam.rec.js'), 'utf8');
const m = /\/\* bigFits:start \*\/([\s\S]*?)\/\* bigFits:end \*\//.exec(src);
if (!m) { console.error('FAIL bigFits markers not found in src/cam.rec.js'); process.exit(1); }
const bigFits = new Function(m[1] + '\nreturn bigFits;')();

let bad = 0, asked = [];
function heap(answer) { return (mib) => { asked.push(mib); if (answer instanceof Error) throw answer; return answer; }; }
function check(name, dev, want) {
  asked = [];
  const got = bigFits(dev);
  const ok = got.ok === want.ok && got.by === want.by && (want.asked === undefined || JSON.stringify(asked) === JSON.stringify(want.asked));
  if (!ok) bad++;
  console.log((ok ? 'ok   ' : 'FAIL ') + name + ' -> ' + JSON.stringify(got) + (asked.length ? ' heap asked ' + asked.join(',') : ''));
}

// Chromium says how much memory there is: 0.25, 0.5, 1, 2, 4 or 8 GiB. Twice the worst peak (2,600 MiB) needs 8.
for (const g of [0.25, 0.5, 1, 2, 4]) check('deviceMemory ' + g + ' GiB', { memory: g, tryHeap: heap(true) }, { ok: false, by: 'memory', asked: [] });
check('deviceMemory 8 GiB', { memory: 8, tryHeap: heap(false) }, { ok: true, by: 'memory', asked: [] });
check('deviceMemory 16 GiB (a future browser)', { memory: 16 }, { ok: true, by: 'memory' });
check('deviceMemory 6 GiB (not a power of two)', { memory: 6 }, { ok: true, by: 'memory' });
check('deviceMemory 5 GiB', { memory: 5 }, { ok: false, by: 'memory' });
// No usable figure: the heap test decides, and it is asked for 1 GiB.
check('no deviceMemory, heap granted', { tryHeap: heap(true) }, { ok: true, by: 'heap', asked: [1024] });
check('no deviceMemory, heap refused', { tryHeap: heap(false) }, { ok: false, by: 'heap', asked: [1024] });
check('no deviceMemory, heap test throws', { tryHeap: heap(new RangeError('out of memory')) }, { ok: false, by: 'heap', asked: [1024] });
check('deviceMemory 0, heap granted', { memory: 0, tryHeap: heap(true) }, { ok: true, by: 'heap' });
check('deviceMemory NaN, heap refused', { memory: NaN, tryHeap: heap(false) }, { ok: false, by: 'heap' });
check('deviceMemory a string, heap granted', { memory: '8', tryHeap: heap(true) }, { ok: true, by: 'heap' });
check('deviceMemory Infinity, heap refused', { memory: Infinity, tryHeap: heap(false) }, { ok: false, by: 'heap' });
check('no test at all', {}, { ok: false, by: 'heap' });
check('no device object', undefined, { ok: false, by: 'heap' });

console.log(bad ? 'FAIL ' + bad + ' case(s)' : 'PASS all cases');
process.exit(bad ? 1 : 0);
