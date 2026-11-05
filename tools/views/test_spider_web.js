// Run with node tools/views/test_spider_web.js. Uses the real resolver and event handler, no browser mocks of their logic.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '../..');
const specs = Object.fromEntries(fs.readdirSync(path.join(root, 'views')).filter(n => n.endsWith('.json') && n !== 'index.json').map(n => [n.slice(0, -5), JSON.parse(fs.readFileSync(path.join(root, 'views', n)))]));
const source = fs.readFileSync(path.join(root, 'src/cam.a.js'), 'utf8').replace('/*@SPECS@*/{}', JSON.stringify(specs));
function context(search = '') {
  const c = { window: {}, navigator: {}, document: {}, location: {search}, Math, Date };
  vm.createContext(c); vm.runInContext(source, c); return c;
}
const plain = context();
assert.equal(plain.EYES.spider, undefined); assert.equal(plain.EYES.jumper, undefined);
assert.equal(specs.spider.offered, false); assert.equal(specs.jumper.offered, false);
const trial = context('?try=spider&draw=web');
assert.ok(trial.EYES.spider); assert.equal(trial.EYES.jumper, undefined);
let checked = 0;
for (const s of Object.values(specs)) {
  const selections = new Set(['', 'unknown', ...Object.values(s.draw || {}).flatMap(a => a.map(o => o.name))]);
  for (const choice of selections) {
    trial.TUNE.draw = choice;
    const result = trial.drawOf(s.draw);
    for (const [category, options] of Object.entries(s.draw || {})) {
      const old = options.some(o => o.name === choice) ? choice : options[0]?.name;
      const expected = s.key === 'spider' && choice === 'web' && category === 'haptic' ? 'buzz' : old;
      assert.equal(result[category], expected, `${s.key}/${choice}/${category}`); checked++;
    }
  }
}
trial.TUNE.draw = 'web';
const p = trial.paramsOf(trial.EYES.spider);
assert.equal(p.ovlMode, 'web'); assert.equal(p.hapMode, 'buzz'); assert.equal(p.hap.on, 'knock');
assert.equal(p.senses.motion, 1); assert.equal(p.senses.jolt, 1);
trial.TUNE.draw = ''; const d = trial.paramsOf(trial.EYES.spider);
assert.equal(d.ovlMode, ''); assert.equal(d.hapMode, '');
trial.TUNE.draw = 'buzz'; const b = trial.paramsOf(trial.EYES.spider);
assert.equal(b.ovlMode, ''); assert.equal(b.hapMode, 'buzz');
const engine = fs.readFileSync(path.join(root, 'src/cam.b.js'), 'utf8');
const start = engine.indexOf('    function addOnsTo('), end = engine.indexOf('\n    // ---- the light module', start);
assert.ok(start > 0 && end > start);
let knock = 0, sound = {onsetAt: 0}, calls = 0;
const e = {senses: {sound: () => sound, knock: () => knock}, LIGHT: {shock: 0}, evts: [], seenOnset: 0, seenKnock: 0, seenShock: 0, hapAt: 0, pulse: 0,
  navigator: {vibrate: pat => {calls++; assert.deepEqual(Array.from(pat), [25]); return true;}}, Math, clamp: trial.clamp, canvas: {width: 200, height: 200}};
vm.createContext(e); vm.runInContext(engine.slice(start, end), e);
e.addOnsTo(p, 1000, 16); assert.equal(calls, 0);
knock = 1100; e.addOnsTo(p, 1100, 16); assert.equal(calls, 1); assert.equal(e.evts.length, 1);
e.addOnsTo(p, 1150, 16); assert.equal(calls, 1); // no repeat while the event timestamp is unchanged
sound = {onsetAt: 1200, onsetBand: 0, band: [.5, 0, 0]};
e.addOnsTo(p, 1400, 16); assert.equal(calls, 1); // sound is not a contact-triggered buzz
e.navigator.vibrate = () => false; knock = 1500; e.addOnsTo(p, 1500, 16); assert.ok(e.pulse > 0);
delete e.navigator.vibrate; knock = 1700; e.addOnsTo(p, 1700, 16); assert.ok(e.pulse > 0);
e.navigator.vibrate = () => {throw new Error('refused');}; knock = 1900; e.addOnsTo(p, 1900, 16); assert.ok(e.pulse > 0);
assert.equal(calls, 1);
console.log(`PASS: ${checked} option/category comparisons; experimental isolation, defaults, combined web/knock output, no repeat, sound separation, and three haptic fallbacks`);
