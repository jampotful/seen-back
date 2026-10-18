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

// Build 38: an iPhone, iPad or iPod is refused before either test until a real iPhone has run the model, unless the owner lifted the gate (?bigios=1).
const UA = {
  iphone: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Mobile/15E148 Safari/604.1',
  iphoneChrome: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/141.0.7390.96 Mobile/15E148 Safari/604.1',
  ipadOld: 'Mozilla/5.0 (iPad; CPU OS 12_5_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1',
  ipod: 'Mozilla/5.0 (iPod touch; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.6 Mobile/15E148 Safari/604.1',
  mac: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Safari/605.1.15',
  android: 'Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36',
  windows: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'
};
check('iPhone, heap granted', { ua: UA.iphone, touch: 5, tryHeap: heap(true) }, { ok: false, by: 'ios-untested', asked: [] });
check('iPhone, Chrome, heap granted', { ua: UA.iphoneChrome, touch: 5, tryHeap: heap(true) }, { ok: false, by: 'ios-untested', asked: [] });
check('iPad before iPadOS 13, heap granted', { ua: UA.ipadOld, touch: 5, tryHeap: heap(true) }, { ok: false, by: 'ios-untested', asked: [] });
check('iPod touch, heap granted', { ua: UA.ipod, touch: 5, tryHeap: heap(true) }, { ok: false, by: 'ios-untested', asked: [] });
check('iPadOS with a Mac user agent and 5 touch points', { ua: UA.mac, touch: 5, tryHeap: heap(true) }, { ok: false, by: 'ios-untested', asked: [] });
check('iPhone that says 8 GiB (a future browser)', { ua: UA.iphone, touch: 5, memory: 8, tryHeap: heap(true) }, { ok: false, by: 'ios-untested', asked: [] });
check('iPhone, the switch not exactly true', { ua: UA.iphone, touch: 5, iosTest: 1, tryHeap: heap(true) }, { ok: false, by: 'ios-untested', asked: [] });
check('iPhone, gate lifted, heap granted', { ua: UA.iphone, touch: 5, iosTest: true, tryHeap: heap(true) }, { ok: true, by: 'heap', asked: [1024] });
check('iPhone, gate lifted, heap refused', { ua: UA.iphone, touch: 5, iosTest: true, tryHeap: heap(false) }, { ok: false, by: 'heap', asked: [1024] });
check('iPadOS, gate lifted, heap granted', { ua: UA.mac, touch: 5, iosTest: true, tryHeap: heap(true) }, { ok: true, by: 'heap', asked: [1024] });
check('Mac, no touch points, heap granted', { ua: UA.mac, touch: 0, tryHeap: heap(true) }, { ok: true, by: 'heap', asked: [1024] });
check('Mac, one touch point (an emulated touch screen), heap granted', { ua: UA.mac, touch: 1, tryHeap: heap(true) }, { ok: true, by: 'heap', asked: [1024] });
check('Mac, touch points unknown, heap refused', { ua: UA.mac, tryHeap: heap(false) }, { ok: false, by: 'heap', asked: [1024] });
check('Android phone, 5 touch points, 8 GiB', { ua: UA.android, touch: 5, memory: 8 }, { ok: true, by: 'memory' });
check('Windows laptop, 10 touch points, 4 GiB', { ua: UA.windows, touch: 10, memory: 4 }, { ok: false, by: 'memory' });
check('user agent not a string, heap granted', { ua: 42, touch: 5, tryHeap: heap(true) }, { ok: true, by: 'heap', asked: [1024] });

console.log(bad ? 'FAIL ' + bad + ' case(s)' : 'PASS all cases');
process.exit(bad ? 1 : 0);
