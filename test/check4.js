// Browser checks. Serve the repository root on port 8765 first (python3 -m http.server 8765 --bind 127.0.0.1),
// then: NODE_PATH=<where playwright lives> node test/check4.js <record|lent|typed|viewer|edge|sweep|film|lex>
const { chromium, devices } = require('playwright');
const path = require('path');
const fs = require('fs');
const here = __dirname, shots = path.join(here, 'shots4');
fs.mkdirSync(shots, { recursive: true });
const PORT = process.env.PORT || 8765;
// These checks are about the picture, the typed name and the record, so the page's own recognizer is switched off (rec=off) and so is the
// service worker (nosw=1). The recognizer has its own checks in test/rec/check_rec.js.
// The species service is switched off too (svc=off), so that a service.json at the site's root changes nothing here, and so is the larger
// model a person may download (big=off), so that a models/naturalist/ at the site's root changes nothing either.
const HTTP = 'http://127.0.0.1:' + PORT + '/index.html?side=' + (process.env.SIDE || 420) + '&nosw=1&svc=off&big=off&rec=' + (process.env.REC || 'off');
const phone = devices['Pixel 7'];
const mode = process.argv[2] || 'record';
// SLOW=4 on a busy machine: every wait for something to appear lasts four times as long before it gives up. Nothing else changes.
const SLOW = +(process.env.SLOW || 1);
const patient = (page) => { if (SLOW === 1) return page;
  const scale = (o) => (o && o.timeout ? Object.assign({}, o, { timeout: o.timeout * SLOW }) : o), wf = page.waitForFunction.bind(page), ws = page.waitForSelector.bind(page);
  page.waitForFunction = (fn, arg, o) => wf(fn, arg, scale(o)); page.waitForSelector = (sel, o) => ws(sel, scale(o)); return page; };
const fontCss = () => ['normal', 'italic'].map(st => `@font-face{font-family:"Instrument Serif";font-style:${st};font-weight:400;src:url(http://127.0.0.1:${PORT}/fonts/instrument-serif-latin-400-${st}.woff2) format("woff2");}`).join('\n');

const claudeStub = () => {
  const sample = Object.assign(async () => ({ text: '' }), {
    limits: async () => ({ maxPromptBytes: 262144, images: { maxCount: 4, maxInputBytes: 2e7, mediaTypes: ['image/jpeg', 'image/png'] } }),
    json: async (input, opts) => {
      window.__calls = (window.__calls || []).concat([{ tier: opts.modelTier, images: opts.images && opts.images.length }]);
      await new Promise(r => setTimeout(r, 600));
      return window.__answer || { found: true, common: 'Domestic cat', scientific: 'Felis catus', eyes: 'cat' };
    },
  });
  const downloads = { save: async (r) => { window.__saved = (window.__saved || []).concat([{ filename: r.filename, size: r.data && r.data.size }]); return { status: 'saved' }; } };
  // a small stand-in for the artifact's document store, kept across reloads of the test page
  const load = () => { try { return JSON.parse(localStorage.getItem('__dbstub') || '{}'); } catch (e) { return {}; } };
  const save = (o) => localStorage.setItem('__dbstub', JSON.stringify(o));
  const segs = (p) => p.split('/').length;
  const docRef = (p) => {
    if (segs(p) % 2) throw new TypeError('document path needs an even number of segments: ' + p);
    return { id: p.split('/').pop(), path: p,
      get: async () => { const v = load()[p]; return { id: p.split('/').pop(), exists: !!v, data: () => v }; },
      set: async (d) => { window.__sets = (window.__sets || 0) + 1; const o = load(); o[p] = JSON.parse(JSON.stringify(d)); save(o); },
      delete: async () => { const o = load(); delete o[p]; save(o); },
      collection: (c) => colRef(p + '/' + c) };
  };
  const colRef = (p) => {
    if (!(segs(p) % 2)) throw new TypeError('collection path needs an odd number of segments: ' + p);
    const q = { path: p, _o: null, _n: 1000,
      doc: (id) => docRef(p + '/' + (id || 'x' + Math.random().toString(36).slice(2))),
      orderBy(f, d) { this._o = [f, d]; return this; }, limit(n) { this._n = n; return this; },
      async get() {
        const o = load(); let docs = Object.keys(o).filter(k => k.startsWith(p + '/') && segs(k) === segs(p) + 1).map(k => ({ id: k.split('/').pop(), exists: true, data: () => o[k] }));
        if (this._o) docs.sort((a, b) => (a.data()[this._o[0]] - b.data()[this._o[0]]) * (this._o[1] === 'desc' ? -1 : 1));
        docs = docs.slice(0, this._n); return { docs, size: docs.length, empty: !docs.length };
      } };
    return q;
  };
  const db = { doc: docRef, collection: colRef };
  const user = { id: async () => 'u_test1', isOwner: async () => true };
  const table = { sample, downloads, db, user };
  window.claude = { use: (name) => Promise.resolve(table[name] || null) };
  if (navigator.mediaDevices) navigator.mediaDevices.getUserMedia = () => Promise.reject(new DOMException('Permission denied', 'NotAllowedError'));
};
const st = page => page.evaluate(() => { const b = window.__seenBack; return Object.assign({ screen: b.S.screen, src: b.S.src, eyes: b.S.eyes, k: +b.S.k.toFixed(2), hasView: b.S.hasView, nov: b.S.nov, rec: b.record().length }, { err: b.state() && b.state().err, moving: b.state() && b.state().moving }); });
const hidden = (page, id) => page.evaluate(i => { const e = document.getElementById(i); return e.hidden || getComputedStyle(e).display === 'none'; }, id);
const text = (page, id) => page.evaluate(i => document.getElementById(i).textContent, id);
const shot = (page, name) => page.screenshot({ path: path.join(shots, name + '.png'), scale: 'css' });
const overflow = page => page.evaluate(() => [document.documentElement.scrollWidth - window.innerWidth, document.documentElement.scrollHeight - window.innerHeight]);
const say = async (page, name) => { await page.waitForSelector('#claim', { state: 'visible', timeout: 8000 }); await page.locator('#claimName').fill(name); await page.locator('#claimForm button[type=submit]').tap(); };

async function launch() {
  const args = ['--use-fake-device-for-media-stream', '--use-fake-ui-for-media-stream', '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--autoplay-policy=no-user-gesture-required'];
  if (fs.existsSync(path.join(here, 'cam.mjpeg'))) args.push('--use-file-for-fake-video-capture=' + path.join(here, 'cam.mjpeg'));
  return chromium.launch({ args });
}
async function open(browser, opts, init, ctxIn) {
  const ctx = ctxIn || await browser.newContext(Object.assign({}, phone, opts || {}));
  const page = patient(await ctx.newPage()); const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' && !/TUNNEL|ERR_|favicon/.test(m.text())) errors.push('console: ' + m.text()); });
  await page.route('https://fonts.googleapis.com/**', r => r.fulfill({ contentType: 'text/css', body: fontCss() }));
  if (init) await page.addInitScript(init);
  await page.goto(HTTP); await page.waitForTimeout(500);
  return { ctx, page, errors };
}
const toFinder = async (page) => { await page.locator('#btnBegin').tap(); await page.waitForSelector('#barFinder', { state: 'visible', timeout: 10000 }); await page.waitForTimeout(700); };

(async () => {
  const out = {};
  const browser = await launch();

  if (mode === 'lex') {
    const { ctx, page } = await open(browser, {});
    const cases = { 'cat': 'cat', 'my kitten': 'cat', 'bobcat': 'cat', 'catbird': 'bird', 'catfish': 'fish', 'fox squirrel': 'squirrel', 'red fox': 'dog', 'foxglove': '', 'dogwood': 'plant',
      'rat snake': 'reptile', 'squirrel treefrog': 'frog', 'crane fly': 'insect', 'sandhill crane': 'wader', 'turkey vulture': 'bird', 'black vulture': 'bird', 'red-shouldered hawk': 'hawk', 'wild turkey': 'wader', 'wood stork': 'wader', 'wood duck': 'bird',
      'great blue heron': 'wader', 'honeybee': 'bee', 'bumblebees': 'bee', 'gulf fritillary': 'insect', 'dragonfly': 'insect', 'tufted titmouse': 'bird', 'mockingbird': 'bird', 'swallow-tailed kite': 'hawk',
      'tiger swallowtail': 'insect', 'american alligator': 'alligator', 'green anole': 'reptile', 'southern toad': 'frog', 'white-tailed deer': 'deer', 'marsh rabbit': 'rabbit', 'spanish moss': 'plant',
      'beautyberry': 'plant', 'live oak': 'plant', 'wolf spider': 'spider', 'armadillo': 'mammal', 'plant': 'plant', 'ant': 'insect', 'a person': 'person', 'limpkin': 'wader', 'barred owl': 'bird', 'walkingstick': 'insect', 'elephant': 'mammal', 'biscuit': '', 'biscuit, a cat': 'cat', 'my dog rex': 'dog',
      // the groups with no view yet (build 21), and names whose last word decides
      'flying fox': 'flyingfox', 'fruit bat': 'flyingfox', 'big brown bat': 'bat', 'sea lion': 'whale', 'manatee': 'whale', 'jellyfish': 'sealife', 'starfish': 'sealife', 'crayfish': 'crab', 'pill bug': 'crab',
      'water bear': 'other', 'mites': 'other', 'slime mold': 'slime', 'jumping spider': 'jumper', 'camel spider': 'scorpion', 'seahorse': 'fish', 'octopus': 'cephalopod', 'cuttlefish': 'cephalopod', 'stingray': 'shark',
      'earthworm': 'worm', 'millipede': 'worm', 'garden snail': 'snail', 'red eft': 'salamander', 'deer tick': 'tick', 'mushroom': 'fungus', 'turkey tail': 'fungus', 'chicken of the woods': 'fungus', 'raccoon': 'mammal', 'spider monkey': 'primate',
      'giraffe': 'deer', 'penguin': 'bird', 'fish crow': 'bird', 'american herring gull': 'bird', 'snail kite': 'hawk', 'potter wasp': 'bee', 'velvet ant': 'bee', 'oakworm moth': 'insect', 'inchworm': 'insect', 'eastern pondhawk': 'insect',
      'zebra longwing': 'insect', 'cricket frog': 'frog', 'butterfly weed': 'plant', 'cat’s-ear': 'plant', 'baby deer': 'deer', 'baby': 'person' };
    const got = await page.evaluate(c => Object.keys(c).filter(k => window.__seenBack.kindOfName(k) !== c[k]).map(k => k + ' -> ' + window.__seenBack.kindOfName(k) + ' (wanted ' + c[k] + ')'), cases);
    // the sheet "Now your view." says how the view returns, in plain English for every kind with a view ('other' has had none since build 19, so its sheet is never shown)
    const view = await page.evaluate(() => Object.keys(window.__seenBack.EYES).filter((k) => k !== 'person' && k !== 'other').map((k) => { window.__seenBack.setViewPrompt(k); return [k, document.getElementById('askViewH').textContent + '|' + document.getElementById('askViewText').textContent]; }));
    view.forEach(([k, t]) => { if (!/^View the world as [^.|]+\.\|$/.test(t) || / as this one\./.test(t)) got.push('view prompt for ' + k + ': ' + t); });
    out.lex = { tried: Object.keys(cases).length + view.length, wrong: got }; await ctx.close();
  }

  if (mode === 'lent') {   // eyes are lent for a week from a meeting: an older meeting stays in the record, and its eyes cannot be looked through
    const ctx = await browser.newContext(Object.assign({}, phone)); const page = await ctx.newPage(); const errors = [];
    page.on('pageerror', (e) => errors.push(e.message));
    const day = 864e5;
    await page.addInitScript((day) => { if (localStorage.getItem('seenback.record.v1')) return; const now = Date.now();
      localStorage.setItem('seenback.record.v1', JSON.stringify([
        { id: 'mm01', key: 'wader', common: 'Great blue heron', sci: 'Ardea herodias', by: 'you', at: now - 6.5 * day, thumb: '', up: 0, loc: 0 },
        { id: 'mm02', key: 'cat', common: 'cat', sci: '', by: 'you', at: now - 8 * day, thumb: '', up: 0, loc: 0 },
        { id: 'mm03', key: 'wader', common: 'Great egret', sci: 'Ardea alba', by: 'you', at: now - 30 * day, thumb: '', up: 0, loc: 0 }])); }, day);
    await page.goto(HTTP); await page.waitForTimeout(700);
    await page.locator('#introRec').tap(); await page.waitForSelector('#record', { state: 'visible' }); await page.waitForTimeout(250);
    const r = { sub: await text(page, 'recordSub') };
    r.eyes = await page.evaluate(() => [...document.querySelectorAll('#eyeStrip .eye')].map(b => (b.disabled ? 0 : 1) + (b.querySelector('.pupil') ? 'p' : '-') + ':' + b.getAttribute('aria-label')).filter(x => !/haven’t met yet/.test(x)));
    r.rows = await page.evaluate(() => [...document.querySelectorAll('#metList li')].map(li => li.querySelector('.nm').textContent + ' | ' + li.querySelector('.sm').textContent + ' | look ' + !!li.querySelector('.ico')));
    r.rings = await page.evaluate(() => document.querySelectorAll('#eyeStrip .eye .loan').length); r.days = await page.evaluate(() => [...document.querySelectorAll('#metList .days')].map((d) => d.textContent));
    await shot(page, 'L1-lent');
    await page.evaluate(() => window.__seenBack.lookAgain && window.__seenBack.lookAgain(window.__seenBack.record()[1])); await page.waitForTimeout(600);
    r.goneStays = await page.evaluate(() => !document.getElementById('record').hidden && window.__seenBack.S.screen);
    await page.locator('#metList li .ico').first().tap();
    // wait for the look to open (the eyes change), up to 15 s, in place of a fixed pause that was short on a loaded machine
    await page.waitForFunction(() => window.__seenBack.S.eyes === 'wader', null, { timeout: 15000 * SLOW }).catch(() => {}); r.lentOpens = (await st(page)).eyes;
    r.errors = errors; out.lent = r;
    const ok = r.sub === '' && r.rings === 1 && r.days.join() === '1d'
      && r.eyes.length === 2 && r.eyes.some((e) => /^1p:Look as/.test(e)) && r.eyes.some((e) => /^0p:A creature you’ve already viewed the world as$/.test(e))
      && /This is the last day with this creature’s view \| look true$/.test(r.rows[0]) && /This creature’s view has disappeared \| look false$/.test(r.rows[1]) && /This creature’s view has disappeared \| look false$/.test(r.rows[2])
      && r.goneStays && r.lentOpens === 'wader' && !errors.length;
    await ctx.close();
    if (!ok) { console.log(JSON.stringify(out, null, 1)); throw new Error('lent: the week of lending is not as it should be'); }
  }
  if (mode === 'typed') {   // a typed name: a species of the list by its own name, one with no eyes of its own, a slip of the keys, and a word that names nothing
    const ctx = await browser.newContext(Object.assign({}, phone)); const page = await ctx.newPage(); const errors = [];
    page.on('pageerror', (e) => errors.push(e.message));
    await page.addInitScript(() => { if (navigator.mediaDevices) navigator.mediaDevices.getUserMedia = () => Promise.reject(new DOMException('no', 'NotAllowedError')); });
    await page.goto(HTTP.replace('rec=off', 'rec=models/pocket')); await page.waitForFunction(() => window.__seenBack.rec.about().state === 'ready', null, { timeout: 120000 });
    await page.locator('#btnBegin').tap(); await page.waitForSelector('#askAnimal', { state: 'visible' });
    const r = {}; const type = async (w) => { await page.evaluate(() => window.__seenBack.openClaim('')); await page.waitForSelector('#claim', { state: 'visible' }); await page.locator('#claimName').fill(w); await page.locator('#claimForm button[type=submit]').tap(); await page.waitForTimeout(350);
      return page.evaluate(() => ({ note: document.getElementById('claimNote').textContent, sug: [...document.querySelectorAll('#claimSuggest button')].map((b) => b.textContent), show: !!document.getElementById('claimOtherRow') && !document.getElementById('claimOtherRow').hidden, about: !!document.querySelector('#claimNote a[href*="issues/new"]'), eyes: window.__seenBack.S.eyes, named: window.__seenBack.S.named && (window.__seenBack.S.named.common + '|' + window.__seenBack.S.named.scientific) })); };
    r.unknown = await type('xqzzvk'); r.slip = await type('herron'); r.slipSpecies = await type('monarhc'); r.several = await type('blue heron x'); r.noEyes = await type('wolf spider');
    r.exact = await type('green treefrog');
    r.human = await type('human');   // a human is no view (build 22): the sheet says so and the eyes stay as they are
    r.errors = errors; out.typed = r; await ctx.close();
    const ok = /^Xqzzvk isn’t a creature we know\./.test(r.unknown.note) && r.unknown.about && !r.unknown.sug.length && !r.unknown.eyes
      && r.slip.note === 'Did you mean:' && r.slip.sug.includes('heron') && r.slipSpecies.sug.includes('monarch')
      && /^Regards doesn’t have the ability to view the world as a wolf spider right now\./.test(r.noEyes.note) && !r.noEyes.show && !r.noEyes.about
      && r.exact.eyes === 'frog' && /\|Dryophytes cinereus$/.test(r.exact.named || '')
      && r.human.note === 'That’s a human. You already see the world as one. Try photographing another creature.' && r.human.eyes === r.exact.eyes && !errors.length;
    if (!ok) { console.log(JSON.stringify(out, null, 1)); throw new Error('typed: a typed name is not handled as it should be'); }
  }
  if (mode === 'record') {
    const { ctx, page, errors } = await open(browser, { permissions: ['camera'], acceptDownloads: true });
    const r = {};
    r.introLink = await text(page, 'introRec');
    await page.locator('#introRec').tap(); await page.waitForSelector('#record', { state: 'visible' }); await page.waitForTimeout(250);
    r.emptySub = await text(page, 'recordSub'); await shot(page, 'R1-record-empty');
    await page.locator('#recordClose').tap();
    await toFinder(page);
    await page.locator('#btnShutter').tap(); await page.waitForSelector('#claim', { state: 'visible' }); await page.waitForTimeout(300);
    r.claimSub = await text(page, 'claimSub'); await shot(page, 'R2-claim');
    await page.locator('#claimForm button[type=submit]').tap(); r.emptyNote = await text(page, 'claimNote');
    await page.locator('#claimBack').tap(); await page.waitForTimeout(200); r.afterDismiss = await st(page);   // do-over
    await page.locator('#btnShutter').tap(); await page.waitForSelector('#claim', { state: 'visible' });
    await page.locator('#claimName').fill('Biscuit'); await page.locator('#claimForm button[type=submit]').tap(); await page.waitForTimeout(200);
    r.petName = { note: await text(page, 'claimNote'), about: await page.locator('#claimNote a').isVisible(), other: await page.locator('#claimOtherRow').isVisible(), still: (await st(page)).screen };
    if (!/^Biscuit isn’t a creature we know\. /.test(r.petName.note) || !r.petName.about || r.petName.other) throw new Error('an unknown word: ' + JSON.stringify(r.petName)); await shot(page, 'R2b-pet-name');
    await page.locator('#claimBack').tap(); await page.waitForTimeout(200); await page.locator('#btnShutter').tap(); await page.waitForSelector('#claim', { state: 'visible' }); await page.waitForTimeout(150);
    r.cleanAgain = await page.evaluate(() => document.getElementById('claimName').value + '|' + document.getElementById('claimNote').textContent + '|' + !document.getElementById('claimAboutRow').hidden);
    if (r.cleanAgain !== '||false') throw new Error('the naming sheet kept an earlier word: ' + r.cleanAgain);   // build 12 left the field, the note and the link in place
    await say(page, 'Biscuit, a cat'); await page.waitForTimeout(700);
    r.count1 = await text(page, 'rvCount'); r.shown1 = await text(page, 'rvName'); await shot(page, 'R3-new-kind'); await page.waitForTimeout(3600);
    r.cat = await st(page);
    await page.locator('#btnBack').tap(); await page.waitForTimeout(200);
    await page.locator('#btnShutter').tap(); await say(page, 'fox squirrel'); await page.waitForTimeout(500); r.count2 = await text(page, 'rvCount'); await page.waitForTimeout(3600);
    r.squirrel = await st(page);
    // the name was wrong: say it again, and the same meeting is corrected
    await page.locator('#btnWho').tap(); await page.locator('#infoChange').tap(); await say(page, 'Great blue heron'); await page.waitForTimeout(600);
    r.count3 = await text(page, 'rvCount'); await page.waitForTimeout(3600); r.heron = await st(page);
    await page.locator('#btnBack').tap(); await page.waitForTimeout(200);
    await page.locator('#btnShutter').tap(); await say(page, 'cat'); await page.waitForTimeout(500); r.count4 = await text(page, 'rvCount'); await page.waitForTimeout(3400);
    await page.locator('#btnBack').tap(); await page.waitForTimeout(200);
    await page.locator('#btnRecF').tap(); await page.waitForSelector('#record', { state: 'visible' }); await page.waitForTimeout(300);
    r.sub = await text(page, 'recordSub'); r.g60 = await text(page, 'g60Sum');
    r.eyesOn = await page.evaluate(() => [...document.querySelectorAll('#eyeStrip .eye')].map(b => b.disabled ? 0 : 1).join(''));
    r.rows = await page.evaluate(() => [...document.querySelectorAll('#metList li')].map(li => li.querySelector('.nm').textContent + ' | ' + li.querySelector('.sm').textContent));
    await shot(page, 'R4-record');
    await page.evaluate(() => { document.getElementById('g60').open = true; }); await page.waitForTimeout(200);
    r.g60rows = await page.evaluate(() => [...document.querySelectorAll('#g60List li')].slice(0, 3).map(li => li.className + ':' + li.textContent));
    await page.evaluate(() => { document.getElementById('record').scrollTop = 9999; }); await page.waitForTimeout(150); await shot(page, 'R5-record-g60');
    await page.evaluate(() => { document.getElementById('record').scrollTop = 0; });
    // forget one, with a second thought first
    await page.locator('#metList li .x').first().tap(); await page.waitForTimeout(150); await shot(page, 'R6-forget-ask');
    await page.locator('#metList li.ask .mini', { hasText: 'Keep' }).tap(); r.keptCount = (await st(page)).rec;
    await page.locator('#metList li .x').first().tap(); await page.locator('#metList li.ask .mini', { hasText: 'Forget' }).tap(); await page.waitForTimeout(150); r.afterForget = (await st(page)).rec;
    // look again through eyes already met, from the row
    await page.locator('#metList li .ico').first().tap(); await page.waitForTimeout(900);
    r.againCount = await text(page, 'rvCount'); await page.waitForTimeout(3300); r.again = await st(page);
    // reload: the record is still here, and an eye on the strip opens the camera in that view
    await page.reload(); await page.waitForTimeout(700);
    r.afterReload = { link: await text(page, 'introRec'), rec: (await st(page)).rec };
    await page.locator('#introRec').tap(); await page.waitForSelector('#record', { state: 'visible' });
    await page.locator('#eyeStrip .eye:not([disabled])').first().tap();
    await page.waitForFunction(() => window.__seenBack.S.screen === 'animal', null, { timeout: 10000 }); await page.waitForTimeout(4200);
    r.fromStrip = await st(page); await shot(page, 'R7-again-live');
    await page.goBack(); await page.waitForTimeout(300); r.sysBack = (await st(page)).screen;
    r.overflow = await overflow(page); r.errors = errors; out.record = r; await ctx.close();
  }

  if (mode === 'viewer') {
    const ctx = await browser.newContext(Object.assign({}, phone));
    let { page, errors } = await open(browser, {}, claudeStub, ctx);
    const r = {};
    await page.locator('#btnBegin').tap(); await page.waitForSelector('#askAnimal', { state: 'visible', timeout: 8000 });
    await page.locator('#inAnimalPick').setInputFiles(path.join(here, 'assets', 'garden.jpg'));
    await page.waitForFunction(() => window.__seenBack.S.eyes === 'cat', null, { timeout: 8000 }); await page.waitForTimeout(500);
    r.count = await text(page, 'rvCount'); r.named = await st(page); await shot(page, 'V1-named');
    await page.waitForSelector('#askView', { state: 'visible', timeout: 5000 });
    await page.locator('#inViewPick').setInputFiles(path.join(here, 'assets', 'clip.webm'));
    await page.waitForFunction(() => window.__seenBack.S.screen === 'animal', null, { timeout: 12000 }); await page.waitForTimeout(4600);
    r.animal = await st(page);
    r.store1 = await page.evaluate(() => { const o = JSON.parse(localStorage.getItem('__dbstub') || '{}'); return Object.keys(o).map(k => k.replace(/m[a-z0-9]+$/, 'ID') + ' ' + o[k].common + ' ' + o[k].by + ' thumb:' + (o[k].thumb || '').length); });
    // the name was wrong: say who it was; the one kept meeting is corrected in both places
    await page.locator('#btnWho').tap(); await page.locator('#infoChange').tap(); await say(page, 'great blue heron'); await page.waitForTimeout(4600);
    r.corrected = await st(page);
    r.store2 = await page.evaluate(() => { const o = JSON.parse(localStorage.getItem('__dbstub') || '{}'); return Object.keys(o).map(k => o[k].key + ' ' + o[k].common + ' ' + o[k].by); });
    // another device: the browser's own copy is gone, the store still has it
    await page.evaluate(() => localStorage.removeItem('seenback.record.v1')); await page.reload(); await page.waitForTimeout(900);
    r.restored = { link: await text(page, 'introRec'), rec: (await st(page)).rec };
    await page.locator('#introRec').tap(); await page.waitForSelector('#record', { state: 'visible' }); await page.waitForTimeout(200);
    r.g60 = await text(page, 'g60Sum'); await shot(page, 'V2-record');
    // look again inside the viewer: no camera, so it asks for the view
    await page.locator('#metList li .ico').first().tap(); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
    r.againAsk = await text(page, 'askViewText'); r.againState = await st(page); await page.waitForTimeout(300); await shot(page, 'V3-again-askview');
    await page.locator('#inViewPick').setInputFiles(path.join(here, 'assets', 'portrait.jpg'));
    await page.waitForFunction(() => window.__seenBack.S.screen === 'animal', null, { timeout: 8000 }); await page.waitForTimeout(600);
    r.againCount = await text(page, 'rvCount'); await page.waitForTimeout(3600); r.againView = await st(page);
    // forgotten on another device: it leaves this one too at the next load
    await page.evaluate(() => localStorage.setItem('__dbstub', '{}')); await page.reload(); await page.waitForTimeout(900);
    r.forgottenElsewhere = (await st(page)).rec;
    r.sets = await page.evaluate(() => window.__sets || 0);
    // Claude finds nothing alive
    await page.evaluate(() => { window.__answer = { found: false }; });
    await page.locator('#btnBegin').tap(); await page.waitForSelector('#askAnimal', { state: 'visible' });
    await page.locator('#inAnimalPick').setInputFiles(path.join(here, 'assets', 'portrait.jpg'));
    await page.waitForSelector('#notice', { state: 'visible', timeout: 8000 }); r.nothingAlive = await text(page, 'noticeText');
    if (!/^We can’t find a creature in your photo\. Try again\.$/.test(r.nothingAlive)) throw new Error('nothing alive: ' + r.nothingAlive);
    await page.locator('#noticeOk').tap(); await page.waitForTimeout(200); r.afterDismiss = (await st(page)).screen;
    r.overflow = await overflow(page); r.errors = errors; out.viewer = r; await ctx.close();
  }

  if (mode === 'edge') {
    { // desktop inside the viewer
      const { ctx, page, errors } = await open(browser, { viewport: { width: 1200, height: 800 }, deviceScaleFactor: 1, isMobile: false, hasTouch: false, userAgent: undefined }, claudeStub);
      await page.locator('#btnBegin').click(); await page.waitForSelector('#askAnimal', { state: 'visible', timeout: 8000 });
      await page.locator('#inAnimalPick').setInputFiles(path.join(here, 'assets', 'garden.jpg'));
      await page.waitForSelector('#askView', { state: 'visible', timeout: 9000 });
      await page.locator('#changeAskView').click(); await page.waitForSelector('#claim', { state: 'visible' }); await page.waitForTimeout(300); await shot(page, 'E1-desktop-claim');
      await page.locator('#claimName').fill('bumblebee'); await page.keyboard.press('Enter'); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
      await page.locator('#backAskView').click(); await page.locator('#recAskAnimal').click(); await page.waitForSelector('#record', { state: 'visible' }); await page.waitForTimeout(250); await shot(page, 'E2-desktop-record');
      out.desktop = { state: await st(page), overflow: await overflow(page), errors }; await ctx.close();
    }
    { // reduced motion, hosted
      const { ctx, page, errors } = await open(browser, { permissions: ['camera'], reducedMotion: 'reduce' });
      await toFinder(page); await page.locator('#btnShutter').tap(); await say(page, 'deer'); await page.waitForTimeout(1600);
      out.calm = { state: await st(page), msg: await text(page, 'msg'), errors }; await ctx.close();
    }
    { // no WebGL 2
      const { ctx, page, errors } = await open(browser, {}, () => { const g = HTMLCanvasElement.prototype.getContext; HTMLCanvasElement.prototype.getContext = function (t) { return t === 'webgl2' ? null : g.apply(this, arguments); }; });
      await page.locator('#introRec').tap(); await page.waitForSelector('#record', { state: 'visible' });
      out.noGL = { fine: await text(page, 'introFine'), disabled: await page.evaluate(() => document.getElementById('btnBegin').disabled), errors }; await ctx.close();
    }
    { // hosted, camera refused, storage refused too
      const { ctx, page, errors } = await open(browser, {}, () => {
        if (navigator.mediaDevices) navigator.mediaDevices.getUserMedia = () => Promise.reject(new DOMException('Permission denied', 'NotAllowedError'));
        Object.defineProperty(window, 'localStorage', { get() { throw new DOMException('denied', 'SecurityError'); } });
      });
      const r = {};
      await page.locator('#btnBegin').tap(); await page.waitForSelector('#askAnimal', { state: 'visible', timeout: 8000 }); r.fine = await text(page, 'askFine');
      await page.locator('#inAnimalPick').setInputFiles(path.join(here, 'assets', 'garden.jpg')); await page.waitForSelector('#claim', { state: 'visible', timeout: 8000 }); r.sub = await text(page, 'claimSub');
      await page.locator('#claimName').fill('heron'); await page.locator('#claimForm button[type=submit]').tap();
      await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); r.kept = await st(page);
      await page.locator('#changeAskView').tap(); await say(page, 'honeybee');
      await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
      await page.locator('#inViewPick').setInputFiles(path.join(here, 'assets', 'clip.webm'));
      await page.waitForFunction(() => window.__seenBack.S.screen === 'animal', null, { timeout: 12000 }); await page.waitForTimeout(4400);
      r.state = await st(page);
      await page.goBack(); await page.waitForTimeout(300); r.b1 = (await st(page)).screen;
      await page.goBack(); await page.waitForTimeout(300); r.b2 = (await st(page)).screen;
      await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' });
      await page.locator('#metList li .ico').first().tap(); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); r.again = await st(page);
      r.errors = errors; out.refused = r; await ctx.close();
    }
  }

  if (mode === 'sweep' || mode === 'film') {
    const { ctx, page, errors } = await open(browser, { permissions: ['camera'] });
    const names = { cat: 'cat', dog: 'dog', squirrel: 'squirrel', deer: 'deer', rabbit: 'rabbit', wader: 'heron', bird: 'cardinal', hawk: 'hawk', alligator: 'alligator', reptile: 'anole', frog: 'treefrog', bee: 'bee', insect: 'butterfly', plant: 'oak', other: 'mushroom' };
    const want = (process.argv[3] || Object.keys(names).join(',')).split(',');
    const r = {}; let first = true;
    await toFinder(page); await page.locator('#btnShutter').tap();
    for (const key of want) {
      if (!first) { await page.evaluate(() => window.__seenBack.pose(null)); await page.locator('#btnWho').tap(); await page.locator('#infoChange').tap(); }
      first = false;
      await say(page, names[key]);
      if (mode === 'sweep') { await page.waitForTimeout(4600); r[key] = (await st(page)).eyes; await shot(page, 'S-' + key); }
      else { await page.waitForTimeout(300); let i = 0; for (const t of [0.3, 0.46, 0.62, 0.9]) { await page.evaluate(v => window.__seenBack.pose(v), t); await page.waitForTimeout(700); await shot(page, 'F-' + key + '-' + (i++)); } }
    }
    r.errors = errors; out[mode] = r; await ctx.close();
  }

  if (mode === 'try') {
    // The views being tried (?try=, TRY lists them; jumper, reef, shark and spider by default), each on the scene clip: no errors, the rows
    // are there, the movement map is read where the view has one, and the gaze jumps where the view has one, with what each fixation landed
    // on (test/assets/scene.json says where everything is). Small screenshots go to test/shots/engine/.
    const dir = path.join(here, 'shots', 'engine'); fs.mkdirSync(dir, { recursive: true });
    const keys = (process.env.TRY || 'jumper,reef,shark,spider').split(',');
    out.try = {}; const bad = [];
    for (const key of keys) {
      const ctx = await browser.newContext(Object.assign({}, phone)); const page = patient(await ctx.newPage()); const errors = [];
      page.on('pageerror', (e) => errors.push(e.message)); page.on('console', m => { if (m.type() === 'error' && !/favicon/.test(m.text())) errors.push('console: ' + m.text()); });
      await page.route('https://fonts.googleapis.com/**', r => r.fulfill({ contentType: 'text/css', body: fontCss() }));
      await page.addInitScript(() => { if (navigator.mediaDevices) navigator.mediaDevices.getUserMedia = () => Promise.reject(new DOMException('no', 'NotAllowedError')); });
      await page.goto(HTTP + '&try=' + key + (process.env.GENUS ? '&genus=' + process.env.GENUS : '') + (process.env.EXTRA || '')); await page.waitForTimeout(500);
      const r = out.try[key] = {};
      await page.locator('#btnBegin').tap(); await page.waitForSelector('#askView', { state: 'visible', timeout: 8000 });
      r.prompt = await text(page, 'askViewH');
      await page.locator('#inViewPick').setInputFiles(path.join(here, 'assets', process.env.CLIP || 'scene.webm'));
      await page.waitForFunction(() => window.__seenBack.S.screen === 'animal', null, { timeout: 15000 });
      // Software graphics draw a few frames a second, so the clip is slowed (PLAYBACK, 0.15) until each drawn frame is about one of the
      // clip's frames after the last, as a phone's camera delivers them. The movement map keeps to the clip's own clock.
      await page.evaluate((x) => { document.getElementById('vid').playbackRate = x; }, +(process.env.PLAYBACK || .15));
      await page.waitForTimeout(1200); await page.evaluate(() => window.__seenBack.pose(null));
      const P = await page.evaluate((k) => { const p = window.__seenBack.params(k); return { sal: p.sal, gaze: !!p.gz, zoned: !!(p.zones && p.zones.length), slow: p.slowMode || '' }; }, key);   // a view with no zones (zones: []) need not compile the zone programs
      const trace = [], t0 = Date.now(), SECS = +(process.env.TRY_SECS || 30);
      let n = 0;
      while (Date.now() - t0 < SECS * 1000) {
        await page.waitForTimeout(500);
        const g = await page.evaluate(() => window.__seenBack.engine.gazeState());
        trace.push({ t: Date.now() - t0, x: +g.x.toFixed(3), y: +g.y.toFixed(3), mode: g.mode, jumps: g.jumps, gazes: g.gazes, maxE: +g.map.maxE.toFixed(3), maxL: +g.map.maxL.toFixed(3), shift: g.map.shift.map((v) => +v.toFixed(2)), reads: g.map.reads, salFrames: g.salFrames });
        if (n < 2 && Date.now() - t0 > (SECS * 1000) * (n + 1) / 3) { await page.screenshot({ path: path.join(dir, key + '-' + n + '.png'), scale: 'css' }); n++; }
      }
      if (/tune=1/.test(process.env.EXTRA || '')) {   // the tuning panel: it lists the spec's parameters, a slider changes the view, and the compare divider draws
        r.tune = await page.evaluate(() => { const t = window.__seenBack.tune; if (!t) return null; const l = t.list(); return { n: l.length, first: l[0] }; });
        if (r.tune) {
          r.tune.set = await page.evaluate(() => window.__seenBack.tune.set('params.cpd', .6));
          await page.locator('#tunePanel button', { hasText: 'Compare' }).click(); await page.waitForTimeout(1500);
          r.tune.divider = await page.evaluate(() => getComputedStyle(document.getElementById('tuneDivider')).display !== 'none');
          r.tune.patch = await page.evaluate(() => window.__seenBack.tune.patch());
          await page.screenshot({ path: path.join(dir, key + '-tune' + (process.env.DRAW ? '-' + process.env.DRAW : '') + '.png'), scale: 'css' });
        }
        if (!r.tune || !r.tune.n || !r.tune.set || !r.tune.divider) errors.push('the tuning panel did not work: ' + JSON.stringify(r.tune));
      }
      const last = trace[trace.length - 1], gs = await page.evaluate(() => window.__seenBack.engine.gazeState());
      r.eyes = (await st(page)).eyes; r.reads = last.reads; r.maxE = Math.max.apply(null, trace.map((x) => x.maxE)); r.maxL = Math.max.apply(null, trace.map((x) => x.maxL));
      r.jumps = (gs.gazes || []).map((g) => g[3]); r.probe = await page.evaluate(() => window.__seenBack.engine.probe());
      r.slow = await page.evaluate(() => window.__seenBack.engine.slowState && window.__seenBack.engine.slowState());   // module 12: frames kept in the store
      const scene = (process.env.CLIP || 'scene.webm') === 'scene.webm' ? JSON.parse(fs.readFileSync(path.join(here, 'assets', 'scene.json'), 'utf8')) : null;
      r.landed = {};
      if (scene) gs.log.forEach(([x, y, at, media]) => {   // the first gaze's fixations, against where test/make_scene.py drew everything at that clip time
        const nn = scene.where.beetle.length, f = ((Math.round(media / 1000 * scene.fps) % nn) + nn) % nn, A = scene.size[0] / scene.size[1];
        let best = 'nothing', bd = .1;
        Object.keys(scene.where).forEach((k) => { const p = scene.where[k][f], d = Math.hypot((x - p[0]) * A, (1 - y) - p[1]); if (d < bd) { bd = d; best = k; } });
        r.landed[best] = (r.landed[best] || 0) + 1;
      });
      await page.locator('#btnWho').tap(); await page.waitForSelector('#info', { state: 'visible' }); await page.waitForTimeout(300);
      r.rows = await page.evaluate(() => [...document.querySelectorAll('#rows li')].length);
      await page.screenshot({ path: path.join(dir, key + '-rows.png'), scale: 'css' });
      r.errors = errors;
      if (process.env.TRACE) fs.writeFileSync(process.env.TRACE.replace(/(\.json)?$/, '-' + key + '.json'), JSON.stringify(trace, null, 1));
      await ctx.close();
      if (r.probe.glErr) errors.push('GL error ' + r.probe.glErr);
      if (/draw=palm|draw=pond|draw=strip|draw=face/.test(process.env.EXTRA || '') === false && key === 'jumper' && process.env.STAMPS && !(r.probe.stamps > 0)) errors.push('no stamp of attention was left');
      if (key === 'jumper' && !(r.probe.light > 0)) errors.push('the light module read nothing');
      const ok = r.eyes === key && r.rows >= 6 && !errors.length && (!P.zoned || r.probe.zones) && !r.probe.zErr && (!P.sal || (r.reads > 3 && r.maxE > 0)) && (!P.gaze || r.jumps.some((j) => j >= (+process.env.MIN_JUMPS || 1)))
        && (!/^(hour|exposure)$/.test(P.slow) || (r.slow && r.slow.mode === P.slow && r.slow.n > 1)) && (!P.slow || r.probe.zones);
      if (!ok) bad.push(key);
    }
    if (bad.length) { console.log(JSON.stringify(out, null, 1)); throw new Error('try: these views being tried did not behave as they should: ' + bad.join(', ')); }
  }

  if (mode === 'still') {
    // Every offered view on one still photo (test/assets/garden.jpg) with the camera refused, a screenshot of each after its change of eyes
    // has finished. The picture holds still, so two builds' screenshots can be compared pixel for pixel (STILL_DIR names where they go).
    const dir = process.env.STILL_DIR || path.join(shots, 'still'); fs.mkdirSync(dir, { recursive: true });
    const ctx = await browser.newContext(Object.assign({}, phone)); const page = patient(await ctx.newPage()); const errors = [];
    page.on('pageerror', (e) => errors.push(e.message));
    await page.route('https://fonts.googleapis.com/**', r => r.fulfill({ contentType: 'text/css', body: fontCss() }));
    await page.addInitScript(() => { if (navigator.mediaDevices) navigator.mediaDevices.getUserMedia = () => Promise.reject(new DOMException('no', 'NotAllowedError')); });
    await page.goto(HTTP); await page.waitForTimeout(500);
    await page.locator('#btnBegin').tap(); await page.waitForSelector('#askAnimal', { state: 'visible', timeout: 8000 });
    await page.locator('#inAnimalPick').setInputFiles(path.join(here, 'assets', 'garden.jpg'));
    await page.waitForSelector('#askView:visible, #claim:visible', { timeout: 20000 });
    if (await page.locator('#claim').isVisible()) { await page.locator('#claimName').fill('cat'); await page.keyboard.press('Enter'); await page.waitForSelector('#askView', { state: 'visible', timeout: 8000 }); }
    await page.locator('#inViewPick').setInputFiles(path.join(here, 'assets', 'garden.jpg'));
    await page.waitForFunction(() => window.__seenBack.S.screen === 'animal', null, { timeout: 15000 });
    const keys = await page.evaluate(() => Object.keys(window.__seenBack.EYES).filter((k) => k !== 'other' && k !== 'person' && !window.__seenBack.EYES[k].zones));
    const names = { cat: 'cat', dog: 'dog', squirrel: 'squirrel', deer: 'deer', rabbit: 'rabbit', wader: 'heron', bird: 'cardinal', hawk: 'hawk', alligator: 'alligator', reptile: 'anole', frog: 'treefrog', bee: 'bee', insect: 'beetle', plant: 'oak' };
    for (const k of keys) {
      if (k !== 'cat') {
        await page.locator('#btnWho').tap(); await page.locator('#infoChange').tap(); await say(page, names[k] || k);
        await page.waitForTimeout(600);
        if (await page.locator('#askView').isVisible()) { await page.locator('#inViewPick').setInputFiles(path.join(here, 'assets', 'garden.jpg')); await page.waitForFunction(() => window.__seenBack.S.screen === 'animal', null, { timeout: 15000 }); }
      }
      await page.waitForTimeout(4500);
      await page.locator('canvas').first().screenshot({ path: path.join(dir, k + '.png') });
    }
    out.still = { keys: keys, errors: errors }; await ctx.close();
    if (errors.length) throw new Error('still: ' + errors.join('; '));
  }

  if (mode === 'floor') {
    // The visibility floor (docs/ENGINE-DESIGN.md, section 5), on a still picture: the view (FLOOR_VIEW, jumper) at 390 by 844 CSS pixels
    // and a device pixel ratio of 2, the clip paused at FLOOR_T seconds and the gaze pinned, rendered at a parameter's value v and at v + d;
    // d is doubled until the 95th percentile of delta E*ab between the renders passes FLOOR_DE (2.3, see docs/views/floor.json), then
    // bisected four times. FLOOR_PARAMS lists tuning-panel labels (all of the view's scalars by default); FLOOR_VALUES the number of values
    // across each range (1: the spec's value only). Results go to FLOOR_OUT (docs/views/floor.json's form). Temporal parameters need the
    // moving clip and are not measured here.
    const view = process.env.FLOOR_VIEW || 'jumper', DE = +(process.env.FLOOR_DE || 2.3), tmp = fs.mkdtempSync(path.join(require('os').tmpdir(), 'floor-'));
    const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, userAgent: phone.userAgent });
    const page = patient(await ctx.newPage()); const errors = [];
    page.on('pageerror', (e) => errors.push(e.message));
    await page.route('https://fonts.googleapis.com/**', r => r.fulfill({ contentType: 'text/css', body: fontCss() }));
    await page.addInitScript(() => { if (navigator.mediaDevices) navigator.mediaDevices.getUserMedia = () => Promise.reject(new DOMException('no', 'NotAllowedError')); });
    await page.goto(HTTP + '&try=' + view + '&tune=1&draw=strip'); await page.waitForTimeout(500);
    await page.locator('#btnBegin').tap(); await page.waitForSelector('#askView', { state: 'visible', timeout: 8000 });
    await page.locator('#inViewPick').setInputFiles(path.join(here, 'assets', 'scene.webm'));
    await page.waitForFunction(() => window.__seenBack.S.screen === 'animal', null, { timeout: 15000 });
    await page.evaluate((t) => { const v = document.getElementById('vid'); v.pause(); v.currentTime = t; window.__seenBack.tune.hide(true); window.__seenBack.engine.pinGaze(.5, .5); }, +(process.env.FLOOR_T || 2));
    await page.waitForTimeout(3000); await page.evaluate(() => window.__seenBack.pose(null));
    const specs = await page.evaluate(() => { const t = window.__seenBack.tune; return t.list(); });
    let want = (process.env.FLOOR_PARAMS ? process.env.FLOOR_PARAMS.split(',') : specs);
    if (process.env.FLOOR_SKIP && fs.existsSync(process.env.FLOOR_SKIP)) {   // parameters already measured (docs/views/floor.json) are left out
      const done = (JSON.parse(fs.readFileSync(process.env.FLOOR_SKIP, 'utf8')).floor || {})[view] || {}; want = want.filter((l) => !done[l]);
    }
    const info = await page.evaluate((v) => window.__seenBack.tuneInfo ? window.__seenBack.tuneInfo() : null, view);
    let n = 0;
    async function render(lab, x) {
      await page.evaluate(([l, v]) => window.__seenBack.tune.set(l, v), [lab, x]); await page.waitForTimeout(+(process.env.FLOOR_WAIT || 1800));
      const f = path.join(tmp, (n++) + '.png'); await page.locator('canvas').first().screenshot({ path: f }); return f;
    }
    const de = (a, b) => JSON.parse(require('child_process').execFileSync(process.env.FLOOR_PY || 'python3', ['-I', path.join(here, '..', 'tools', 'views', 'delta_e.py'), a, b]).toString());
    const res = {}, NV = +(process.env.FLOOR_VALUES || 1);
    for (const lab of want) {
      const meta = info && info[lab]; if (!meta) { res[lab] = 'no such parameter'; continue; }
      const [lo, hi, v0] = meta, vals = NV <= 1 ? [v0] : Array.from({ length: NV }, (_, i) => lo + (hi - lo) * (i + .5) / NV);
      res[lab] = [];
      for (const v of vals) {
        const a = await render(lab, v); let d = (hi - lo) / 64, up = v + d <= hi ? 1 : -1, seen = null, lastNo = 0, e = null;
        while (Math.abs(d) <= (hi - lo)) {
          const b = await render(lab, v + up * d); e = de(a, b);
          if (e.p95 > DE) { seen = d; break; } lastNo = d; d *= 2;
          if (v + up * d > hi || v + up * d < lo) break;
        }
        if (seen === null) { res[lab].push([v, 'invisible', e && e.p95]); continue; }
        let A = lastNo, B = seen;
        for (let i = 0; i < 4; i++) { const m = (A + B) / 2, b = await render(lab, v + up * m); if (de(a, b).p95 > DE) B = m; else A = m; }
        res[lab].push([+v.toPrecision(4), +B.toPrecision(3)]);
        await render(lab, v0);
      }
      console.log(lab, JSON.stringify(res[lab]));
      if (process.env.FLOOR_OUT) fs.writeFileSync(process.env.FLOOR_OUT, JSON.stringify({ view: view, threshold: DE, partial: true, floor: res }, null, 1));
    }
    out.floor = { view: view, threshold: DE, errors: errors, floor: res };
    if (process.env.FLOOR_OUT) fs.writeFileSync(process.env.FLOOR_OUT, JSON.stringify(out.floor, null, 1));
    await ctx.close();
  }

  if (mode === 'perf') {
    // Every view for a fixed number of frames on a fixed clip (test/assets/scene.webm, made by test/make_scene.py), with a table at the end.
    // A frame's cost is measured from outside the page, so the same harness measures any build: the time of the page's own animation
    // callbacks in that frame plus a one-pixel read of the picture after the one that drew, which waits for the graphics work to end
    // (gl.finish() returns at once in Chromium, so it measures nothing). Headless software graphics are slow and share the machine's
    // processors, so the numbers only compare views and builds with each other, on one machine.
    // PERF_FRAMES (60) sets the frames a view, TRY (jumper) the views reached with ?try=, PERF_OUT a file for the JSON.
    const FRAMES = +(process.env.PERF_FRAMES || 60), TRY = process.env.TRY === undefined ? 'jumper,reef,shark,spider' : process.env.TRY;
    const measure = () => {
      const W = window, pf = W.__pf = { gl: null, rec: false, frames: [] };
      const gc = HTMLCanvasElement.prototype.getContext;
      HTMLCanvasElement.prototype.getContext = function (t, o) { const c = gc.call(this, t, o); if (t === 'webgl2' && this.id === 'gl' && c && !pf.gl) pf.gl = c; return c; };
      const da = WebGL2RenderingContext.prototype.drawArrays; let drew = false;
      WebGL2RenderingContext.prototype.drawArrays = function () { if (this === pf.gl) drew = true; return da.apply(this, arguments); };
      const raf = W.requestAnimationFrame.bind(W); let cur = null; const px = new Uint8Array(4);
      W.requestAnimationFrame = function (cb) {
        return raf(function (ts) {
          if (!cur || cur.ts !== ts) { if (cur && pf.rec && cur.drew) pf.frames.push(cur); cur = { ts, cb: 0, fin: 0, drew: false }; }
          const s = performance.now(); drew = false;
          try { cb(ts); } finally {
            cur.cb += performance.now() - s;
            if (drew && pf.gl) { const f = performance.now(), g = pf.gl; g.bindFramebuffer(g.FRAMEBUFFER, null); g.readPixels(0, 0, 1, 1, g.RGBA, g.UNSIGNED_BYTE, px); cur.fin += performance.now() - f; cur.drew = true; }
          }
        });
      };
      if (navigator.mediaDevices) navigator.mediaDevices.getUserMedia = () => Promise.reject(new DOMException('no', 'NotAllowedError'));
    };
    const ctx = await browser.newContext(Object.assign({}, phone)); const page = patient(await ctx.newPage()); const errors = [];
    page.on('pageerror', (e) => errors.push(e.message));
    await page.route('https://fonts.googleapis.com/**', r => r.fulfill({ contentType: 'text/css', body: fontCss() }));
    await page.addInitScript(measure);
    await page.goto(HTTP + (TRY ? '&try=' + TRY : '')); await page.waitForTimeout(500);
    await page.locator('#btnBegin').tap(); await page.waitForSelector('#askAnimal:not([hidden]), #askView:not([hidden])', { timeout: 8000 });
    if (await page.locator('#askAnimal').isVisible()) {   // a build that knows ?try= goes straight to the view being tried
      await page.locator('#inAnimalPick').setInputFiles(path.join(here, 'assets', 'garden.jpg'));
      await say(page, 'cat'); await page.waitForSelector('#askView', { state: 'visible', timeout: 8000 });
    }
    await page.locator('#inViewPick').setInputFiles(path.join(here, 'assets', 'scene.webm'));
    await page.waitForFunction(() => window.__seenBack.S.screen === 'animal', null, { timeout: 15000 }); await page.waitForTimeout(3500);
    const names = { cat: 'cat', dog: 'dog', squirrel: 'squirrel', deer: 'deer', rabbit: 'rabbit', wader: 'heron', bird: 'cardinal', hawk: 'hawk', alligator: 'alligator', reptile: 'anole', frog: 'treefrog', bee: 'bee', insect: 'butterfly', plant: 'oak',
      jumper: 'jumping spider', spider: 'wolf spider', fish: 'bass', snail: 'garden snail', crab: 'blue crab', bat: 'big brown bat', tick: 'deer tick', salamander: 'red eft', fungus: 'mushroom', mammal: 'raccoon', sealife: 'jellyfish' };
    const have = await page.evaluate(() => Object.keys(window.__seenBack.EYES).filter((k) => k !== 'person' && k !== 'other'));
    const hook = await page.evaluate(() => !!window.__seenBack.look), views = ['human'].concat(have.filter((k) => hook || names[k]));
    const rows = [];
    const stat = (a) => { if (!a.length) return null; const s = a.slice().sort((x, y) => x - y), m = a.reduce((x, y) => x + y, 0) / a.length; return { mean: +m.toFixed(2), median: +s[s.length >> 1].toFixed(2), p90: +s[Math.min(s.length - 1, Math.floor(s.length * .9))].toFixed(2) }; };
    for (const key of views) {
      if (key === 'human') { await page.evaluate(() => { window.__seenBack.S.holding = true; }); await page.waitForTimeout(600); }
      else {
        await page.evaluate(() => { window.__seenBack.S.holding = false; window.__seenBack.pose(null); });
        if (await page.evaluate((k) => window.__seenBack.look ? window.__seenBack.look(k) : false, key)) await page.waitForTimeout(600);   // a build with the hook goes straight in
        else if (await page.evaluate((k) => window.__seenBack.S.eyes !== k, key)) {
          await page.locator('#btnWho').tap(); await page.locator('#infoChange').tap(); await say(page, names[key]);
          await page.waitForFunction((k) => window.__seenBack.S.eyes === k && window.__seenBack.S.screen === 'animal', key, { timeout: 12000 });
          await page.waitForTimeout(900);
        }
        await page.evaluate(() => window.__seenBack.pose(null)); await page.waitForTimeout(700);
      }
      await page.evaluate(() => { window.__pf.frames = []; window.__pf.rec = true; });
      await page.waitForFunction((n) => window.__pf.frames.length >= n, FRAMES, { timeout: 600000, polling: 250 });
      const got = await page.evaluate(() => { const f = window.__pf.frames.slice(); window.__pf.rec = false; const b = window.__seenBack; return { f, probe: b.probe ? b.probe() : null, eyes: b.S.eyes, k: b.S.k, err: b.state() && b.state().err, side: b.state() && b.state().sw + 'x' + b.state().sh }; });
      const f = got.f.slice(0, FRAMES), cost = f.map((x) => x.cb + x.fin), gaps = f.slice(1).map((x, i) => x.ts - f[i].ts);
      rows.push({ view: key, frames: f.length, cost: stat(cost), interval: stat(gaps), script: stat(f.map((x) => x.cb)), gpu: got.probe && got.probe.gpu !== null ? +got.probe.gpu.toFixed(2) : null, err: got.err, k: +got.k.toFixed(2), ring: got.side });
    }
    await page.evaluate(() => { window.__seenBack.S.holding = false; });
    const table = ['| view | cost, mean ms | median | p90 | frame interval, median ms | script, mean ms | GPU timer, ms |', '|---|---|---|---|---|---|---|']
      .concat(rows.map((r) => '| ' + [r.view, r.cost.mean, r.cost.median, r.cost.p90, r.interval ? r.interval.median : '', r.script.mean, r.gpu === null ? 'none' : r.gpu].join(' | ') + ' |'));
    console.log(table.join('\n'));
    out.perf = { url: HTTP, frames: FRAMES, rows, errors };
    if (process.env.PERF_OUT) fs.writeFileSync(process.env.PERF_OUT, JSON.stringify(out.perf, null, 1));
    await ctx.close();
    if (errors.length || rows.some((r) => r.err)) { console.log(JSON.stringify(out, null, 1)); throw new Error('perf: an error while drawing'); }
  }

  await browser.close();
  console.log(JSON.stringify(out, null, 1));
})().catch(e => { console.error('FAILED', e); process.exit(1); });
