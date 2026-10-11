// Browser checks. Serve the repository root on port 8765 first (python3 -m http.server 8765 --bind 127.0.0.1),
// then: NODE_PATH=<where playwright lives> node test/check4.js <record|lent|viewer|edge|sweep|film|lex>
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
    const cases = { 'cat': 'cat', 'my kitten': 'cat', 'bobcat': 'cat', 'catbird': 'bird', 'catfish': 'other', 'fox squirrel': 'squirrel', 'red fox': 'dog', 'foxglove': '', 'dogwood': 'plant',
      'rat snake': 'reptile', 'squirrel treefrog': 'frog', 'crane fly': 'insect', 'sandhill crane': 'wader', 'turkey vulture': 'bird', 'black vulture': 'bird', 'red-shouldered hawk': 'hawk', 'wild turkey': 'wader', 'wood stork': 'wader', 'wood duck': 'bird',
      'great blue heron': 'wader', 'honeybee': 'bee', 'bumblebees': 'bee', 'gulf fritillary': 'insect', 'dragonfly': 'insect', 'tufted titmouse': 'bird', 'mockingbird': 'bird', 'swallow-tailed kite': 'hawk',
      'tiger swallowtail': 'insect', 'american alligator': 'alligator', 'green anole': 'reptile', 'southern toad': 'frog', 'white-tailed deer': 'deer', 'marsh rabbit': 'rabbit', 'spanish moss': 'plant',
      'beautyberry': 'plant', 'live oak': 'plant', 'wolf spider': 'other', 'armadillo': 'other', 'plant': 'plant', 'ant': 'insect', 'a person': 'person', 'limpkin': 'wader', 'barred owl': 'bird', 'walkingstick': 'insect', 'elephant': '', 'biscuit': '', 'biscuit, a cat': 'cat', 'my dog rex': 'dog' };
    const got = await page.evaluate(c => Object.keys(c).filter(k => window.__seenBack.kindOfName(k) !== c[k]).map(k => k + ' -> ' + window.__seenBack.kindOfName(k) + ' (wanted ' + c[k] + ')'), cases);
    // the sheet "Now your view." says how the view returns, in plain English for every kind (for 'other' it once read "as this one may take it in")
    const view = await page.evaluate(() => Object.keys(window.__seenBack.EYES).filter((k) => k !== 'person').map((k) => { window.__seenBack.setViewPrompt(k); return [k, document.getElementById('askViewH').textContent + '|' + document.getElementById('askViewText').textContent]; }));
    view.forEach(([k, t]) => { if (!/^Now see as [^.|]+\.\|$/.test(t) || / as this one\./.test(t) || (k === 'other' && t !== 'Now see as this living thing.|')) got.push('view prompt for ' + k + ': ' + t); });
    out.lex = { tried: Object.keys(cases).length + view.length, wrong: got }; await ctx.close();
  }

  if (mode === 'lent') {   // eyes are lent for a week from a meeting: an older meeting stays in the record, and its eyes cannot be looked through
    const ctx = await browser.newContext(Object.assign({}, phone)); const page = await ctx.newPage(); const errors = [];
    page.on('pageerror', (e) => errors.push(e.message));
    const day = 864e5;
    await page.addInitScript((day) => { if (localStorage.getItem('seenback.record.v1')) return; const now = Date.now();
      localStorage.setItem('seenback.record.v1', JSON.stringify([
        { id: 'mm01', key: 'wader', common: 'Great blue heron', sci: 'Ardea herodias', by: 'you', at: now - 6.5 * day, thumb: '', up: 0, loc: 0 },
        { id: 'mm02', key: 'cat', common: 'Cat', sci: '', by: 'you', at: now - 8 * day, thumb: '', up: 0, loc: 0 },
        { id: 'mm03', key: 'wader', common: 'Great egret', sci: 'Ardea alba', by: 'you', at: now - 30 * day, thumb: '', up: 0, loc: 0 }])); }, day);
    await page.goto(HTTP); await page.waitForTimeout(700);
    await page.locator('#introRec').tap(); await page.waitForSelector('#record', { state: 'visible' }); await page.waitForTimeout(250);
    const r = { sub: await text(page, 'recordSub') };
    r.eyes = await page.evaluate(() => [...document.querySelectorAll('#eyeStrip .eye')].map(b => (b.disabled ? 0 : 1) + (b.querySelector('.pupil') ? 'p' : '-') + ':' + b.getAttribute('aria-label')).filter(x => !/not yet met/.test(x)));
    r.rows = await page.evaluate(() => [...document.querySelectorAll('#metList li')].map(li => li.querySelector('.nm').textContent + ' | ' + li.querySelector('.sm').textContent + ' | look ' + !!li.querySelector('.ico')));
    r.rings = await page.evaluate(() => document.querySelectorAll('#eyeStrip .eye .loan').length); r.days = await page.evaluate(() => [...document.querySelectorAll('#metList .days')].map((d) => d.textContent));
    await shot(page, 'L1-lent');
    await page.evaluate(() => window.__seenBack.lookAgain && window.__seenBack.lookAgain(window.__seenBack.record()[1])); await page.waitForTimeout(600);
    r.goneStays = await page.evaluate(() => !document.getElementById('record').hidden && window.__seenBack.S.screen);
    await page.locator('#metList li .ico').first().tap(); await page.waitForTimeout(1200); r.lentOpens = (await st(page)).eyes;
    r.errors = errors; out.lent = r;
    const ok = r.sub === 'Eyes stay with you for a week.' && r.rings === 1 && r.days.join() === '1d'
      && r.eyes.length === 2 && r.eyes.some((e) => /^1p:Look as/.test(e)) && r.eyes.some((e) => /^0p:A kind of eye that has gone back$/.test(e))
      && /its eyes go back within a day \| look true$/.test(r.rows[0]) && /its eyes have gone back \| look false$/.test(r.rows[1]) && /its eyes have gone back \| look false$/.test(r.rows[2])
      && r.goneStays && r.lentOpens === 'wader' && !errors.length;
    await ctx.close();
    if (!ok) { console.log(JSON.stringify(out, null, 1)); throw new Error('lent: the week of lending is not as it should be'); }
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
    r.petName = { note: await text(page, 'claimNote'), other: await text(page, 'claimOther'), still: (await st(page)).screen }; await shot(page, 'R2b-pet-name');
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
    await page.locator('#g60 summary').tap(); await page.waitForTimeout(200);
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
    await page.waitForSelector('#claim', { state: 'visible', timeout: 8000 }); r.nothingAlive = await text(page, 'claimSub');
    await page.locator('#claimBack').tap(); await page.waitForTimeout(200); r.afterDismiss = (await st(page)).screen;
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
      await page.locator('#claimName').fill('capybara'); await page.locator('#claimForm button[type=submit]').tap(); await page.locator('#claimOther').tap();
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

  await browser.close();
  console.log(JSON.stringify(out, null, 1));
})().catch(e => { console.error('FAILED', e); process.exit(1); });
