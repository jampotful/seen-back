// Checks of the recognizer inside the page, in a headless browser (Chromium unless BROWSER says otherwise), against the stand-in under test/rec/models/standin
// (made by test/rec/make_standin.py; it is not a recognizer, only the same machinery with labels made from its own answers).
//   node test/rec/serve.js 8782 &
//   NODE_PATH=<where playwright lives> node test/rec/check_rec.js [flow|nameover|camera|fuse|notsure|trained|parity|progress|typeit|service|large|away|zone|offline|version|keptcopy|missing|damaged|dying|about|viewer ...]
// "large" (the full database a person may download) needs a second origin for the model's parts: the script starts test/rec/serve.js <BIG_PORT> cors
// by itself (8788 unless BIG_PORT says otherwise) if nothing answers there.
// Every check ends with ok: true or false, and the script exits 1 if any is false.
// A real model: make a slot with test/rec/make_slot.py --photos <dir>, then
//   SLOT=<slot dir, from the repository root> PHOTOS=<dir> node test/rec/check_rec.js parity
// compares the browser with Python on those photos and prints the kinds and the timings.
const playwright = require('playwright');
const { devices } = playwright;
// BROWSER=firefox or BROWSER=webkit runs the same checks there (not tried yet: this sandbox has Chromium only).
const ENGINE = process.env.BROWSER || 'chromium', isChromium = ENGINE === 'chromium';
const path = require('path'), fs = require('fs'), http = require('http');
const here = __dirname, PORT = process.env.PORT || 8782, ORIGIN = 'http://127.0.0.1:' + PORT;
const SLOT = process.env.SLOT || 'test/rec/models/standin';
// The species service is off (svc=off) unless a check names a service file, so that a service.json at the site's root changes nothing in the other checks.
// The full database is off too (big=off) unless a check names its slot, so that a models/naturalist/ at the site's root changes nothing in the other checks.
const url = (q) => ORIGIN + '/index.html?side=' + (process.env.SIDE || 420) + (/[?&]svc=/.test(q || '') ? '' : '&svc=off') + (/[?&]big=/.test(q || '') ? '' : '&big=off') + (q || '');
const BIG_PORT = +(process.env.BIG_PORT || 8788), BIG_ORIGIN = 'http://127.0.0.1:' + BIG_PORT, BIG = 'test/rec/models/standin-big';
const bctl = (q) => new Promise((res, rej) => http.get(BIG_ORIGIN + '/__ctl?' + q, (r) => { let b = ''; r.on('data', (d) => b += d); r.on('end', () => { try { res(JSON.parse(b)); } catch (e) { rej(e); } }); }).on('error', rej));
const SVC_PORT = +(process.env.SVC_PORT || 8784);
// SLOW=4 on a busy machine: every wait for something to appear lasts four times as long before it gives up. Nothing else changes.
const SLOW = +(process.env.SLOW || 1);
const patient = (page) => { if (SLOW === 1) return page;
  const scale = (o) => (o && o.timeout ? Object.assign({}, o, { timeout: o.timeout * SLOW }) : o), wf = page.waitForFunction.bind(page), ws = page.waitForSelector.bind(page);
  page.waitForFunction = (fn, arg, o) => wf(fn, arg, scale(o)); page.waitForSelector = (sel, o) => ws(sel, scale(o)); return page; };
const phone = Object.assign({}, devices['Pixel 7'], { timezoneId: 'America/New_York' });   // the county's time zone, where the page uses its species list (build 22); the section 'zone' tries others
if (ENGINE === 'firefox') { delete phone.isMobile; delete phone.userAgent; }      // Firefox has no mobile emulation in Playwright
if (ENGINE === 'webkit') delete phone.userAgent;
const PHOTOS = process.env.PHOTOS || path.join(here, 'photos');
const photo = (n) => path.join(PHOTOS, n);
const slotDir = path.join(here, '..', '..', SLOT);
const expect = JSON.parse(fs.readFileSync(path.join(slotDir, 'expect.json'), 'utf8'));   // what Python got (make_standin.py, or make_slot.py --photos for a real model)
const want = process.argv.slice(2).length ? process.argv.slice(2) : ['flow', 'nameover', 'camera', 'fuse', 'notsure', 'trained', 'parity', 'progress', 'typeit', 'service', 'large', 'away', 'zone', 'offline', 'version', 'keptcopy', 'missing', 'damaged', 'dying', 'about', 'viewer']
  .filter((w) => isChromium || w !== 'camera');                                     // the stand-in camera feed is a Chromium switch
const ctl = (q) => new Promise((res, rej) => http.get(ORIGIN + '/__ctl?' + q, (r) => { let b = ''; r.on('data', (d) => b += d); r.on('end', () => res(JSON.parse(b))); }).on('error', rej));
const text = (page, id) => page.evaluate((i) => document.getElementById(i).textContent, id);
const about = (page) => page.evaluate(() => window.__seenBack.rec.about());
const st = (page) => page.evaluate(() => { const b = window.__seenBack; return { screen: b.S.screen, eyes: b.S.eyes, named: b.S.named, claim: !document.getElementById('claim').hidden, notice: document.getElementById('notice').hidden ? '' : document.getElementById('noticeText').textContent }; });
// The camera refused. In macOS WebKit the init script's refusal did not take: Begin waited on a getUserMedia that never answered (no
// prompt can appear there), so every case stopped at #askAnimal (runs engines/12 and 15). So the refusal is also defined on the
// prototype, and begin() sets it again in the loaded page before it taps.
// ("Button failed to load, iconName = ...-placard" is macOS WebKit's own video controls, logged as an error; it is not the page's.)
const noCamera = () => { if (!navigator.mediaDevices) return; const no = () => Promise.reject(new DOMException('Permission denied', 'NotAllowedError'));
  try { navigator.mediaDevices.getUserMedia = no; } catch (e) {}
  for (const o of [navigator.mediaDevices, window.MediaDevices && MediaDevices.prototype]) { if (o) try { Object.defineProperty(o, 'getUserMedia', { value: no, configurable: true, writable: true }); } catch (e) {} } };

async function open(browser, q, opts, ctxIn) {
  const ctx = ctxIn || await browser.newContext(Object.assign({}, phone, opts || {}));
  const page = patient(await ctx.newPage()); const errors = [];
  page.on('pageerror', (e) => errors.push('pageerror: ' + e.message));
  page.on('console', (m) => { if (m.type() === 'error' && !/favicon|Failed to load resource|ERR_INTERNET_DISCONNECTED|ERR_FAILED|Button failed to load, iconName = [\w-]*placard/.test(m.text())) errors.push('console: ' + m.text()); });
  await page.addInitScript(noCamera);
  await page.goto(url(q)); await page.waitForTimeout(300);
  return { ctx, page, errors };
}
const ready = (page, ms) => page.waitForFunction(() => window.__seenBack.rec.about().state === 'ready', null, { timeout: ms || 60000 });
const sentence = (n) => n.toLowerCase().replace(/\bgulf\b/g, 'Gulf');   // a species' name as the page sets it: all small, except the place names the test list holds (build 24)
const aboutOpen = async (page) => { await page.locator('#recAbout').tap(); await page.waitForSelector('#aboutSheet', { state: 'visible', timeout: 5000 }); await page.waitForTimeout(250); };   // About is a sheet of its own, opened from the record's header
const shut = (page) => page.evaluate(() => { document.getElementById(document.getElementById('aboutSheet').hidden ? 'recordClose' : 'aboutClose').click(); });
const begin = async (page) => { await page.evaluate(noCamera).catch(() => {}); await page.locator('#btnBegin').tap(); await page.waitForSelector('#askAnimal', { state: 'visible', timeout: 8000 }); };
// choose a photo of who was met, and wait until it has a name or the sheet asks for one
async function meet(page, name) {
  if (!(await page.locator('#askAnimal').isVisible())) {
    const s = await st(page);
    if (s.claim) await page.locator('#claimBack').tap();
    if ((await st(page)).screen === 'askView') await page.locator('#backAskView').tap();
    if ((await st(page)).screen === 'naming') await page.evaluate(() => history.back());
    if ((await st(page)).screen === 'intro') await page.locator('#btnBegin').tap();
    await page.waitForSelector('#askAnimal', { state: 'visible', timeout: 8000 });
  }
  const n0 = await page.evaluate(() => window.__seenBack.diag().length ? window.__seenBack.diag()[window.__seenBack.diag().length - 1].at : 0);
  await page.locator('#inAnimalPick').setInputFiles(photo(name));
  await page.waitForFunction(() => { const b = window.__seenBack; return !!b.S.eyes || !document.getElementById('claim').hidden || !document.getElementById('notice').hidden; }, null, { timeout: 60000 });
  await page.waitForTimeout(150);
  const s = await st(page);
  s.shown = await text(page, 'rvName'); s.sci = await text(page, 'rvSci'); s.sub = s.claim ? await text(page, 'claimSub') : '';
  s.last = await page.evaluate(() => { const r = window.__seenBack.rec.about().last; return r ? { kind: r.kind, kindP: r.kindP, top: r.species[0] || null, offers: r.offers.map((o) => o.en || o.sci), ms: r.ms, model: r.model, backend: r.backend,
    kinds3: r.kinds.slice(0, 3).map((k) => [k.key, +k.p.toFixed(4)]), head3: r.kinds.slice().sort((a, b) => b.head - a.head).slice(0, 3).map((k) => [k.key, +k.head.toFixed(4)]), species3: r.species.slice(0, 3).map((x) => [x.en || x.sci, +x.p.toFixed(4)]) } : null; });
  return s;
}

(async () => {
  const out = {}; let bad = 0;
  const done = (name, r, ok) => { r.ok = !!ok; if (!ok) bad++; out[name] = r; };
  const args = ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--use-fake-device-for-media-stream', '--use-fake-ui-for-media-stream'];
  if (fs.existsSync(path.join(here, '..', 'cam.mjpeg'))) args.push('--use-file-for-fake-video-capture=' + path.join(here, '..', 'cam.mjpeg'));   // sh tools/make_test_media.sh makes it
  const browser = await playwright[ENGINE].launch(isChromium ? { args } : {});
  await ctl('reset=1');
  const month = new Date().getMonth();
  // one check failing to finish must not hide the others
  let sofar = null;     // what a long check had gathered when it stopped, so that the place can be found
  const section = async (name, fn) => { sofar = null; try { await fn(); } catch (e) { done(name + ' (did not finish)', { error: String(e && e.stack || e).split('\n').slice(0, 4).join(' | '), sofar }, false); await ctl('reset=1'); } };

  // ---------- helpers for the line on the picture, the record and the sheet that asks for a name
  const until = async (fn, ms) => { const t0 = Date.now(); while (!fn()) { if (Date.now() - t0 > (ms || 15000)) throw new Error('waited too long'); await new Promise((res) => setTimeout(res, 50)); } };
  const svcLine = (page) => page.evaluate(() => { const vis = (e) => !e.hidden && e.offsetParent !== null, a = document.getElementById('svcView'), b = document.getElementById('svcHud'); return vis(a) ? a.textContent : vis(b) ? b.textContent : ''; });
  const svcWatch = (page) => page.evaluate(() => { window.__svc = []; const el = document.getElementById('svcView'); new MutationObserver(() => { const t = el.hidden ? '' : el.textContent; if (window.__svc[window.__svc.length - 1] !== t) window.__svc.push(t); }).observe(el, { childList: true, characterData: true, subtree: true, attributes: true }); });
  const svcSettled = (page) => page.waitForFunction(() => { const v = window.__seenBack.S.svc; return !v || (v.state !== 'asking' && v.state !== 'waking'); }, null, { timeout: 20000 });
  const byService = (page) => page.waitForFunction(() => { const n = window.__seenBack.S.named; return !!n && n.by === 'service'; }, null, { timeout: 20000 });
  const recordRows = (page) => page.evaluate(() => window.__seenBack.record().map((m) => m.common + '|' + m.sci + '|' + m.by + '|' + m.key));
  const typeName = async (page, name) => { await page.waitForSelector('#claim', { state: 'visible', timeout: 8000 }); await page.locator('#claimName').fill(name); await page.locator('#claimForm button[type=submit]').tap(); };
  // the big name over a screen that has text of its own: the largest opacity #reveal had, sampled every frame, while #askView or #askAnimal was in view
  const watchOver = (page) => page.evaluate(() => { window.__over = 0; const q = (id) => document.getElementById(id), f = () => { if (!q('askView').hidden || !q('askAnimal').hidden) window.__over = Math.max(window.__over, +getComputedStyle(q('reveal')).opacity); requestAnimationFrame(f); }; requestAnimationFrame(f); });
  const overNow = (page) => page.evaluate(() => window.__over);

  if (want.includes('nameover')) await section('nameover', async () => {     // the big name fades on the picture, and is never drawn across "Now your view." or "Who did you meet?"
    const { ctx, page, errors } = await open(browser, '&nosw=1&rec=' + SLOT), r = {}; await ready(page); await begin(page); await watchOver(page);
    r.heron = (await meet(page, 'heron.png')).eyes; await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); await page.waitForTimeout(900);
    r.overAskView = await overNow(page);
    await page.locator('#backAskView').tap(); await page.waitForTimeout(150); await page.evaluate(() => { window.__over = 0; });
    r.stripes = (await meet(page, 'stripes.png')).eyes; await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); await page.waitForTimeout(900);
    r.overAgain = await overNow(page); r.errors = errors;
    fs.mkdirSync(path.join(here, 'shots'), { recursive: true }); await page.screenshot({ path: path.join(here, 'shots', 'nameover.png'), scale: 'css' }).catch(() => {});
    done('nameover', r, r.heron === 'wader' && r.stripes === 'insect' && r.overAskView < 0.05 && r.overAgain < 0.05 && !errors.length); await ctx.close();
  });

  if (want.includes('flow')) await section('flow', async () => {     // a photo chosen through the file input, through to the name; each tier of naming; the correction sheet
    const { ctx, page, errors } = await open(browser, '&nosw=1&rec=' + SLOT);
    const r = {}; await ready(page); r.about0 = await about(page);
    await begin(page);
    r.heron = await meet(page, 'heron.png');                     // one species is sure: it is named
    await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
    r.heronRecord = await page.evaluate(() => window.__seenBack.record().map((m) => m.common + '|' + m.sci + '|' + m.by + '|' + m.key));
    await page.locator('#changeAskView').tap(); await page.waitForSelector('#claim', { state: 'visible' });
    r.heronOffersShown = await page.locator('#claimOfferBox').isVisible(); await page.locator('#claimBack').tap();
    r.stripes = await meet(page, 'stripes.png');                 // three close candidates: the kind alone, and three offers
    await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
    await page.locator('#changeAskView').tap(); await page.waitForSelector('#claim', { state: 'visible' }); await page.waitForTimeout(200);
    r.offerLine = await page.evaluate(() => document.querySelector('#claimOfferBox .note').textContent);
    r.offerButtons = await page.evaluate(() => [...document.querySelectorAll('#claimOffers button')].map((b) => b.textContent));
    r.offersAboveField = await page.evaluate(() => document.getElementById('claimOfferBox').getBoundingClientRect().bottom <= document.getElementById('claimName').getBoundingClientRect().top);
    await page.screenshot({ path: path.join(here, 'shots', 'offers.png'), scale: 'css' }).catch(() => {});
    await page.locator('#claimOffers button', { hasText: 'monarch' }).tap(); await page.waitForTimeout(300);
    r.afterOffer = await st(page); r.afterOfferRecord = await page.evaluate(() => window.__seenBack.record().map((m) => m.common + '|' + m.sci + '|' + m.by + '|' + m.key));
    await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
    r.dots = await meet(page, 'dots.png');                       // no species near: the kind alone, no offers
    await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
    await page.locator('#changeAskView').tap(); await page.waitForSelector('#claim', { state: 'visible' });
    r.dotsOffersShown = await page.locator('#claimOfferBox').isVisible(); await page.locator('#claimBack').tap();
    r.rings = await meet(page, 'rings.png');                     // two candidates as alike as each other: the month decides
    await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
    r.garden = await meet(page, 'garden.jpg');                   // a larger JPEG, brought to 1280 by the browser first
    await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
    r.person = await meet(page, 'portrait.jpg');                 // a human: a notice, no view, and no encounter kept (build 22)
    await page.locator('#noticeOk').tap(); await page.waitForTimeout(200);
    r.wall = await meet(page, 'wall.png');                       // nothing alive
    await page.locator('#noticeOk').tap(); await page.waitForTimeout(200);
    // the sheet behind the name says who recognized it; the list of meetings too
    r.heron2 = await meet(page, 'heron.png'); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
    await page.locator('#inViewPick').setInputFiles(path.join(here, '..', 'assets', 'portrait.jpg'));
    await page.waitForFunction(() => window.__seenBack.S.screen === 'animal', null, { timeout: 12000 });
    await page.locator('#btnWho').tap(); await page.waitForSelector('#info', { state: 'visible' }); r.infoSub = await text(page, 'infoSub');
    r.notRightIsThere = await page.locator('#infoChange').isVisible(); await page.locator('#infoClose').tap();
    await page.evaluate(() => history.back()); await page.waitForTimeout(200); await page.evaluate(() => history.back()); await page.waitForTimeout(200);
    await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' });
    r.rows = await page.evaluate(() => [...document.querySelectorAll('#metList li')].map((li) => li.querySelector('.nm').textContent + ' | ' + li.querySelector('.sm').textContent));
    r.trace = await page.evaluate(() => window.__seenBack.diag().filter((d) => /^pocket/.test(d.what)).slice(-2).map((d) => d.what + ' ' + d.code));
    r.errors = errors;
    const anole = month === 0 ? 'green anole' : 'brown anole';
    done('flow', r, r.heron.eyes === 'wader' && r.heron.shown === 'great blue heron' && r.heron.sci === 'Ardea herodias' && r.heron.named.by === 'page' && /great blue heron\|Ardea herodias\|page\|wader/.test(r.heronRecord[0]) && !r.heronOffersShown
      && r.stripes.eyes === 'insect' && r.stripes.shown === 'insect' && r.stripes.sci === '' && r.offerLine === 'Is it one of these?' && r.offerButtons.join() === 'Gulf fritillary,monarch,queen' && r.offersAboveField
      && r.afterOffer.eyes === 'insect' && r.afterOffer.named.common === 'monarch' && r.afterOffer.named.by === 'you' && /^monarch\|Danaus plexippus\|you\|insect/.test(r.afterOfferRecord[0])
      && r.dots.eyes === 'frog' && r.dots.shown === 'frog or toad' && !r.dotsOffersShown
      && r.rings.eyes === 'reptile' && r.rings.shown === anole
      && r.garden.eyes === 'plant' && r.garden.shown === 'beggarticks' && !r.person.eyes && r.person.notice === 'That’s a human. You already see the world as one. Try photographing another creature.'
      && !r.wall.claim && !r.wall.eyes && r.wall.notice === 'We can’t find a creature in your photo. Try again.'
      && r.infoSub === 'Ardea herodias' && r.notRightIsThere
      && r.rows.some((x) => /great blue heron \| Ardea herodias .* named by this app/.test(x)) && r.rows.some((x) => /^monarch \| /.test(x) && !/named by/.test(x))
      && r.trace.length === 2 && !errors.length);
    await ctx.close();
  });

  if (want.includes('camera')) await section('camera', async () => {   // the live camera and the shutter: the frame as it is goes to the recognizer, and the picture keeps being drawn
    const ctx = await browser.newContext(Object.assign({}, phone, { permissions: ['camera'] })); const page = patient(await ctx.newPage()); const errors = [];
    page.on('pageerror', (e) => errors.push('pageerror: ' + e.message));
    await page.goto(url('&nosw=1&rec=' + SLOT)); await ready(page);
    const r = {};
    await page.locator('#btnBegin').tap(); await page.waitForSelector('#barFinder', { state: 'visible', timeout: 10000 }); await page.waitForTimeout(700);
    const w0 = await page.evaluate(() => window.__seenBack.state().writes);
    await page.locator('#btnShutter').tap();
    await page.waitForFunction(() => { const b = window.__seenBack; return !!b.S.eyes || !document.getElementById('claim').hidden || !document.getElementById('notice').hidden; }, null, { timeout: 30000 });
    r.state = await st(page); r.sub = r.state.claim ? await text(page, 'claimSub') : ''; r.last = await page.evaluate(() => { const x = window.__seenBack.rec.about().last; return x && { kind: x.kind, from: x.from, ms: x.ms }; });
    if (r.state.claim) await page.locator('#claimBack').tap(); else await page.waitForTimeout(3500);
    await page.waitForTimeout(600);
    r.after = await st(page); r.framesSince = (await page.evaluate(() => window.__seenBack.state().writes)) - w0; r.glError = await page.evaluate(() => window.__seenBack.state().err); r.errors = errors;
    done('camera', r, !!r.last && /^\d+x\d+$/.test(r.last.from) && (r.state.notice ? /^We can’t find a creature/.test(r.state.notice) : !!r.state.eyes) && r.glError === 0 && !errors.length);
    await ctx.close();
  });

  if (want.includes('fuse')) await section('fuse', async () => {     // the arithmetic from scores to a name, with numbers set by hand
    const r = {};
    {
      const { ctx, page } = await open(browser, '&nosw=1&rec=' + SLOT); await ready(page);
      r.cases = await page.evaluate(async () => {
        const rec = window.__seenBack.rec, m = await (await fetch('test/rec/models/standin/manifest.json')).json(), t = (await (await fetch('test/rec/models/standin/species.json')).json()).species;
        const L = m.kinds.labels, kd = (o) => L.map((k) => o[k] || 0), sd = (o) => t.map((row) => o[row[1]] || 0), o = {};
        const pick = (x) => ({ kind: x.kind, kindP: +x.kindP.toFixed(4), top: x.species[0] && x.species[0].en, topP: x.species[0] && +x.species[0].p.toFixed(4), named: x.named && x.named.en, offers: x.offers.map((s) => s.en) });
        o.januaryAnole = pick(rec.fuse(kd({ reptile: 1 }), sd({ 'Brown Anole': .9, 'Green Anole': .9 }), 0));
        o.julyAnole = pick(rec.fuse(kd({ reptile: 1 }), sd({ 'Brown Anole': .9, 'Green Anole': .9 }), 6));
        o.personNotOutvoted = pick(rec.fuse(kd({ person: 1, bird: .95 }), sd({ 'Northern Cardinal': .9 }), 6));   // the species list has no people: it must not vote a person down
        o.noneNotOutvoted = pick(rec.fuse(kd({ none: 1, plant: .96 }), sd({ 'Beggarticks': .9 }), 6));
        o.speciesTipsTheKind = pick(rec.fuse(kd({ bird: 1, wader: .995 }), sd({ 'Great Blue Heron': .9 }), 6));        // kinds nearly tied; the species list settles it
        o.kindDisagrees = pick(rec.fuse(kd({ plant: 1, wader: .9 }), sd({ 'Great Blue Heron': .9, 'Beggarticks': .9 - Math.log(.65 / .35) / m.fusion.t_species }), 6));   // a likely species of a kind the kinds rule out is not named, and not offered either: the offers are of the kind that won
        // the same disagreement under each rule, both heads sure (temperature 100): the product is settled by the guard alone, the mix by the weight
        const world = (rule, w, guard) => rec.test.world({ id: 'x', vision: { url: 'x', size: 224, mean: [0, 0, 0], std: [1, 1, 1] }, width: 4, kinds: { url: 'k', labels: L }, species: { url: 's', table: 't', count: t.length },
          fusion: Object.assign({}, m.fusion, { rule: rule, w_kind: w }, guard ? { guard: guard } : {}) }, t, null);
        const clash = (id) => { const x = rec.test.fuseIn(id, kd({ plant: 1 }), sd({ 'Great Blue Heron': 1 }), 6), by = {}; x.kinds.forEach((k) => { by[k.key] = +k.p.toFixed(4); }); return { kind: x.kind, plant: by.plant, wader: by.wader }; };
        o.mixKindsLead = clash(world('mix', .7)); o.mixListLeads = clash(world('mix', .3)); o.productGuard9 = clash(world('product', .7)); o.productGuard3 = clash(world('product', .7, 1e-3));
        o.sum = (() => { const x = rec.fuse(kd({ cat: 1 }), sd({}), 6); return +x.kinds.reduce((a, k) => a + k.p, 0).toFixed(6) + ' ' + x.kinds.length + ' ' + x.species.length; })();
        return o;
      });
      await ctx.close();
    }
    {
      const { ctx, page } = await open(browser, '&nosw=1&rec=' + SLOT + '/manifest.kinds-only.json'); await ready(page);
      await begin(page); r.kindsOnly = await meet(page, 'heron.png'); r.kindsOnlyModel = (await about(page)).model;
      await ctx.close();
    }
    const c = r.cases;
    done('fuse', r, c.januaryAnole.top === 'Green Anole' && c.januaryAnole.named === 'Green Anole' && c.julyAnole.named === 'Brown Anole' && c.personNotOutvoted.kind === 'person' && c.noneNotOutvoted.kind === 'none'
      && c.speciesTipsTheKind.kind === 'wader' && c.speciesTipsTheKind.named === 'Great Blue Heron' && c.kindDisagrees.kind === 'plant' && c.kindDisagrees.top === 'Great Blue Heron' && c.kindDisagrees.named === null && c.kindDisagrees.offers[0] === 'Beggarticks' && c.kindDisagrees.offers.indexOf('Great Blue Heron') < 0
      && c.mixKindsLead.kind === 'plant' && Math.abs(c.mixKindsLead.plant - .7) < 1e-3 && Math.abs(c.mixKindsLead.wader - .3) < 1e-3 && c.mixListLeads.kind === 'wader' && Math.abs(c.mixListLeads.wader - .7) < 1e-3 && c.productGuard9.plant > .999 && c.productGuard3.plant < .9 && c.productGuard3.kind === 'plant'
      && c.sum === '1 17 5' && r.kindsOnly.eyes === 'wader' && r.kindsOnly.shown === 'wading bird' && r.kindsOnlyModel === 'standin-kinds-only');
  });

  if (want.includes('notsure')) await section('notsure', async () => {   // under fusion.kind_at the page asserts no kind: it says so, changes no eyes, and offers its three likeliest kinds above the typed field
    const { ctx, page, errors } = await open(browser, '&nosw=1&rec=' + SLOT + '/manifest.kind-at.json'); const r = {}; await ready(page); await begin(page);
    const w = expect.kind_at['odd.png'][month], hand = (keys) => page.evaluate((keys) => keys.map((k) => k === 'person' ? 'a person' : k === 'other' ? 'something alive' : window.__seenBack.EYES[k].who.replace(/^an? /, '')), keys);
    r.sure = await meet(page, 'heron.png'); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });     // a sure answer is as it was
    const before = (await page.evaluate(() => window.__seenBack.record().length));
    r.odd = await meet(page, 'odd.png'); await page.waitForTimeout(200);
    r.reference = w; r.buttonsWanted = await hand(w.kindOffers);
    r.sheet = await page.evaluate(() => { const q = (id) => document.getElementById(id), box = (id) => q(id).getBoundingClientRect(), l = window.__seenBack.rec.about().last;
      return { kinds: [...document.querySelectorAll('#claimKinds button')].map((b) => b.textContent), kindNote: document.querySelector('#claimKindBox .note').textContent, kindsShown: !q('claimKindBox').hidden,
        offers: [...document.querySelectorAll('#claimOffers button')].map((b) => b.textContent), offerNote: q('claimOfferNote').textContent, offersShown: !q('claimOfferBox').hidden,
        kindsAboveOffers: box('claimKindBox').bottom <= box('claimOfferBox').top + 1, aboveField: box('claimOfferBox').bottom <= box('claimName').top + 1,
        last: { kind: l.kind, sure: l.sure, p: +l.kindP.toFixed(4), kindOffers: l.kindOffers, named: l.named, offerSci: l.offers.map((o) => o.sci) }, screen: window.__seenBack.S.screen, meetings: window.__seenBack.record().length }; });
    await page.screenshot({ path: path.join(here, 'shots', 'notsure.png'), scale: 'css' }).catch(() => {});
    await page.locator('#claimKinds button').nth(1).tap(); await page.waitForTimeout(300);
    r.chosen = await st(page); r.record = await recordRows(page);
    await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); await page.locator('#changeAskView').tap(); await page.waitForSelector('#claim', { state: 'visible' }); await page.waitForTimeout(150);
    r.again = await page.evaluate(() => ({ kinds: [...document.querySelectorAll('#claimKinds button')].map((b) => b.textContent), sub: document.getElementById('claimSub').textContent })); await page.locator('#claimBack').tap();
    // the sheet closed without an answer: no eyes, no meeting
    r.odd2 = await meet(page, 'odd.png'); await page.locator('#claimBack').tap(); await page.waitForTimeout(250); r.dismissed = await st(page); r.meetingsAfterDismiss = (await recordRows(page)).length;
    // the rule with numbers set by hand: at the threshold it is sure; "nothing alive" is never among the kinds offered; a slot with no threshold is always sure
    r.byHand = await page.evaluate(async () => {
      const rec = window.__seenBack.rec, L = ['wader', 'plant', 'bird', 'person', 'none'], t = [['Ardea herodias', 'Great Blue Heron', 'wader', null], ['Bidens alba', 'Beggarticks', 'plant', null]];
      const world = (f, table) => rec.test.world({ id: 'x', vision: { url: 'x', size: 224, mean: [0, 0, 0], std: [1, 1, 1] }, width: 4, kinds: { url: 'k', labels: L }, species: table ? { url: 's', table: 't', count: table.length } : undefined, fusion: f }, table || null, null);
      const f = (kind_at) => Object.assign({ t_kind: 1, t_species: 100, alpha_prior: 0, w_kind: 1, name_at: 0.5, offer_at: 0.3 }, kind_at === undefined ? {} : { kind_at });
      const pick = (x) => ({ kind: x.kind, p: +x.kindP.toFixed(4), sure: x.sure, offered: x.kindOffers, named: x.named && x.named.en, offers: x.offers.map((o) => o.en) });
      const kd = [Math.log(6), Math.log(2), 0, 0, 0], o = {};     // wader 6 parts in 11, plant 2, the rest 1 each
      o.under = pick(rec.test.fuseIn(world(f(0.61), t), kd, [1, 0], 6)); o.at = pick(rec.test.fuseIn(world(f(6 / 11 - 1e-9), t), kd, [1, 0], 6)); o.noThreshold = pick(rec.test.fuseIn(world(f(undefined), t), kd, [1, 0], 6));
      o.noneLeads = pick(rec.test.fuseIn(world(f(0.9), t), [0, Math.log(2), 0, 0, Math.log(6)], [0, 1], 6));
      let refused = ''; try { world(Object.assign(f(0.5), { kind_at: 'high' }), t); } catch (e) { refused = e.code + ': ' + e.detail; } o.refused = refused;
      return o; });
    r.sameName = await page.evaluate(() => window.__seenBack.offerList([{ sci: 'Salvia azurea', en: 'giant blue sage' }, { sci: 'Salvia azurea', en: 'giant blue sage' }, { sci: 'Limenitis astyanax', en: 'red-spotted admiral' },
      { sci: 'Limenitis arthemis', en: 'red-spotted admiral' }, { sci: 'Larra bicolor', en: 'wasp' }]).map((o) => o.label));     // from the real list: Salvia azurea is filed under two GBIF keys; two admirals share a name
    r.errors = errors;
    const tail = '', b = r.byHand;
    done('notsure', r, r.sure.eyes === 'wader' && r.sure.shown === 'great blue heron' && before === 1
      && r.odd.claim && !r.odd.eyes && r.odd.sub === 'We’re not sure what kind of creature that is.' + tail && w.sure === false && r.sheet.last.sure === false && r.sheet.last.kind === w.kind && r.sheet.last.named === null && r.sheet.last.kindOffers.join() === w.kindOffers.join()
      && r.sheet.kinds.join() === r.buttonsWanted.join() && r.sheet.kinds.length === 3 && r.sheet.kindNote === 'Is it one of these?' && r.sheet.kindsShown
      && r.sheet.offers.length === w.offers.length && r.sheet.offers.every((b, i) => b === (w.offers.filter((x) => x === w.offers[i]).length > 1 ? sentence(w.offers[i]) + ' (' + r.sheet.last.offerSci[i] + ')' : sentence(w.offers[i]))) && new Set(r.sheet.offers).size === r.sheet.offers.length
      && r.sameName.join() === 'giant blue sage,red-spotted admiral (Limenitis astyanax),red-spotted admiral (Limenitis arthemis),wasp' && (w.offers.length ? r.sheet.offersShown && r.sheet.offerNote === 'Or one of these species:' && r.sheet.kindsAboveOffers && r.sheet.aboveField : !r.sheet.offersShown) && r.sheet.meetings === 1
      && r.chosen.eyes === w.kindOffers[1] && r.chosen.named.by === 'you' && r.chosen.named.common === r.buttonsWanted[1] && r.record.length === 2 && new RegExp('^' + r.buttonsWanted[1] + '\\|\\|you\\|' + w.kindOffers[1] + '$').test(r.record[0])
      && r.again.kinds.join() === r.buttonsWanted.join() && r.again.sub === ''
      && r.odd2.claim && !r.dismissed.eyes && !r.dismissed.claim && r.meetingsAfterDismiss === 2
      && b.under.sure === false && b.under.kind === 'wader' && b.under.offered.join() === 'wader,plant,bird' && b.under.named === null && b.under.offers[0] === 'Great Blue Heron'
      && b.at.sure === true && b.at.named === 'Great Blue Heron' && b.at.offered.length === 0 && b.noThreshold.sure === true && b.noThreshold.offered.length === 0
      && b.noneLeads.kind === 'none' && b.noneLeads.sure === false && b.noneLeads.offered.join() === 'plant,wader,bird' && b.noneLeads.offers.length === 0 && /^unfit: fusion\.kind_at/.test(b.refused) && !errors.length);
    await ctx.close();
  });

  if (want.includes('trained')) await section('trained', async () => {   // a trained head's files drop in: rows that are not unit vectors, a bias for every row, the mixing rule
    const r = { photos: {} }; let same = true;
    {
      const { ctx, page, errors } = await open(browser, '&nosw=1&rec=' + SLOT + '/manifest.trained.json'); await ready(page);
      r.about = await page.evaluate(() => { const a = window.__seenBack.rec.about(); return { model: a.model, rule: a.rule, trained: a.trained }; });
      await begin(page);
      for (const name of Object.keys(expect.trained)) {            // what tools/fusion/fuse.py gave for each photo, from Python's own embedding (make_standin.py)
        const s = await meet(page, name), w = expect.trained[name];
        const got = await page.evaluate(() => { const l = window.__seenBack.rec.about().last; return { kind: l.kind, named: l.named ? l.named.en : '', offers: l.offers.map((o) => o.en) }; });
        r.photos[name] = { page: got.kind + ' | ' + (got.named || '-') + ' | ' + (got.offers.join(', ') || '-'), reference: w.kind + ' | ' + (w.named || '-') + ' | ' + (w.offers.join(', ') || '-'), sentenceMade: w.plain_kind + ' | ' + (w.plain_named || '-'), shown: s.claim ? '(asks)' : s.shown };
        if (got.kind !== w.kind || got.named !== w.named || got.offers.join() !== w.offers.join()) same = false;
      }
      r.errors = errors; same = same && !errors.length;
      await ctx.close();
    }
    { // a rule this build does not know is refused in words, and so is a bias file cut short
      const tail = ' Tell us what’s there.';
      const a = await open(browser, '&nosw=1&rec=' + SLOT + '/manifest.unknown-rule.json'); await begin(a.page); r.unknownRule = (await meet(a.page, 'heron.png')).sub; r.unknownRuleWhy = (await about(a.page)).fail; await a.ctx.close();
      await ctl('reset=1'); await ctl('cut=' + encodeURIComponent('species\\.bias'));
      const b = await open(browser, '&nosw=1&rec=' + SLOT + '/manifest.trained.json'); await begin(b.page); r.biasCutShort = (await meet(b.page, 'heron.png')).sub; r.biasCutShortWhy = (await about(b.page)).fail; await b.ctx.close(); await ctl('reset=1');
      same = same && r.unknownRule === 'This app’s files are out of date. Close the app and open it again to update.' + tail && r.biasCutShort === 'This app’s download is damaged. Close the app and open it again.' + tail;
    }
    const t = expect.trained;
    done('trained', r, same && r.about.model === 'standin-trained' && r.about.rule === 'mix' && r.about.trained === true
      && t['small.png'].kind === 'hawk' && t['small.png'].named === 'Red-shouldered Hawk' && t['small.png'].plain_kind === 'bird'     // the flips the trained files were built to cause
      && t['dots.png'].kind !== 'frog' && t['dots.png'].plain_kind === 'frog' && Object.keys(t).length >= 7);
  });

  if (want.includes('parity')) await section('parity', async () => {   // the page's own preparing of a photo against Pillow's, and its embedding against onnxruntime's in Python
    const { ctx, page, errors } = await open(browser, '&nosw=1&rec=' + SLOT); await ready(page);
    await page.evaluate(() => { window.__seenBack.rec.wantPre = true; });
    await begin(page);
    const r = { photos: {}, python: 'onnxruntime ' + expect.onnxruntime + ', Pillow ' + expect.pillow };
    let worstExact = 0, worstCos = 1; const dump = {};
    for (const name of Object.keys(expect.photos)) {
      const s = await meet(page, name);
      const got = await page.evaluate(() => ({ pre: Array.from(window.__seenBack.rec.lastPre), emb: Array.from(window.__seenBack.rec.lastEmb) }));
      const ref = fs.readFileSync(path.join(slotDir, 'pre', name + '.u8')), e = expect.photos[name].embedding;
      dump[name] = got.emb;
      let max = 0, differ = 0, dot = 0, na = 0, nb = 0;
      for (let i = 0; i < ref.length; i++) { const d = Math.abs(ref[i] - got.pre[i]); if (d) differ++; if (d > max) max = d; }
      for (let i = 0; i < e.length; i++) { dot += e[i] * got.emb[i]; na += e[i] * e[i]; nb += got.emb[i] * got.emb[i]; }
      const cos = dot / Math.sqrt(na * nb), exact = /\.png$/.test(name);
      r.photos[name] = { size: expect.photos[name].w + 'x' + expect.photos[name].h, maxPixelDiff: max, valuesDiffering: differ + ' of ' + ref.length, cosine: +cos.toFixed(6), kind: s.last ? s.last.kind : '', kinds: s.last && s.last.kinds3, kindsAlone: s.last && s.last.head3, pythonKindsAlone: expect.kinds && expect.kinds[name], species: s.last && s.last.species3, ms: s.last && s.last.ms,
        from: await page.evaluate(() => window.__seenBack.rec.about().last.from), note: exact ? 'the same pixels reach both resizes' : 'a JPEG: the browser decodes it, and applies a colour profile if it has one' };
      if (exact) { worstExact = Math.max(worstExact, max); worstCos = Math.min(worstCos, cos); }
    }
    if (process.env.DUMP) fs.writeFileSync(process.env.DUMP, JSON.stringify(dump));     // the browser's embeddings, to study elsewhere
    r.worstPixelDiffOnSamePixels = worstExact; r.worstCosineOnSamePixels = +worstCos.toFixed(6); r.errors = errors;
    r.about = await page.evaluate(() => window.__seenBack.about().split('\n').slice(1, 3));
    // An int8 model's numbers differ between onnxruntime-web (the same in every browser) and native onnxruntime, and native onnxruntime's
    // differ from one processor to the next: for the same photos the worst cosine was 0.9984 on one build machine and 0.9821 on another
    // (tinyclip-8m-16, runs engines/8 and 11), and one photo's two likeliest kinds swapped places in Python while the browsers stayed put.
    // So an int8 model is held to a cosine of 0.98 and its kinds are compared only where Python's two likeliest are 0.05 or more apart.
    // (The stand-in is int8 too, but its expectations are made on the machine that runs the check, and it stays held to 0.999.)
    const int8 = !expect.kind_of && /int8/.test(JSON.parse(fs.readFileSync(path.join(slotDir, 'manifest.json'), 'utf8')).vision.url);
    r.cosineFloor = int8 ? 0.98 : 0.999;
    const clear = (n) => !int8 || (expect.kinds[n][0][1] - ((expect.kinds[n][1] || [0, 0])[1])) >= 0.05;
    r.closeCalls = int8 ? Object.keys(expect.kinds || {}).filter((n) => !clear(n)) : [];
    const labelsHold = expect.kind_of ? Object.keys(expect.kind_of).every((n) => r.photos[n].kind === expect.kind_of[n])       // the stand-in: this photo gives that label
      : Object.keys(expect.kinds || {}).filter(clear).every((n) => r.photos[n].kindsAlone[0][0] === expect.kinds[n][0][0]);     // a real model: the kinds alone agree with Python's
    done('parity', r, worstExact <= 2 && worstCos >= r.cosineFloor && labelsHold && !errors.length);
    await ctx.close();
  });

  if (want.includes('progress')) await section('progress', async () => { // the photo comes before the recognizer: honest numbers, then it goes on by itself
    await ctl('reset=1'); await ctl('slow=' + encodeURIComponent('ort-wasm.*\\.wasm') + '&bps=2500000');
    const { ctx, page, errors } = await open(browser, '&nosw=1&rec=' + SLOT);
    const r = {}; await begin(page);
    r.stateAtPhoto = (await about(page)).state;
    await page.evaluate(() => {     // every sentence the page shows, in order, noted inside the page so that none is missed
      const el = document.getElementById('msg'); window.__lines = [];
      new MutationObserver(() => { const t = el.textContent; if (t && window.__lines[window.__lines.length - 1] !== t) window.__lines.push(t); }).observe(el, { childList: true, characterData: true, subtree: true });
    });
    await page.locator('#inAnimalPick').setInputFiles(photo('heron.png'));
    await page.waitForFunction(() => { const b = window.__seenBack; return !!b.S.eyes || !document.getElementById('claim').hidden || !document.getElementById('notice').hidden; }, null, { timeout: 60000 });
    const lines = await page.evaluate(() => window.__lines);
    r.lines = lines.length > 12 ? lines.slice(0, 4).concat(['... ' + (lines.length - 8) + ' more ...'], lines.slice(-4)) : lines; r.end = await st(page); r.shown = await text(page, 'rvName'); r.waited = await page.evaluate(() => window.__seenBack.rec.about().last.ms); r.errors = errors;
    const nums = lines.map((l) => /^Downloading… (\d+) of (\d+) MB$/.exec(l)).filter(Boolean);
    done('progress', r, r.stateAtPhoto !== 'ready' && nums.length >= 3 && nums.every((n, i) => +n[1] <= +n[2] && (!i || +n[1] >= +nums[i - 1][1])) && +nums[nums.length - 1][2] === 15 && r.end.eyes === 'wader' && r.shown === 'great blue heron' && !errors.length);
    await ctl('reset=1'); await ctx.close();
  });

  if (want.includes('typeit')) await section('typeit', async () => {   // a way out of a long first download: type the name, and the download carries on by itself
    await ctl('reset=1'); await ctl('slow=' + encodeURIComponent('ort-wasm.*\\.wasm') + '&bps=500000');     // about half a minute of download, so that a busy machine still finds the button there
    const { ctx, page, errors } = await open(browser, '&nosw=1&rec=' + SLOT); const r = {}; await begin(page);
    r.buttonBefore = await page.locator('#barType').isVisible();
    await page.locator('#inAnimalPick').setInputFiles(photo('heron.png'));
    await page.waitForSelector('#btnType', { state: 'visible', timeout: 20000 });
    r.line = await text(page, 'msg'); r.button = (await text(page, 'btnType')).trim();
    r.buttonUnderLine = await page.evaluate(() => document.getElementById('btnType').getBoundingClientRect().top >= document.getElementById('msg').getBoundingClientRect().bottom - 1 && document.getElementById('btnType').getBoundingClientRect().bottom <= window.innerHeight);
    fs.mkdirSync(path.join(here, 'shots'), { recursive: true }); await page.screenshot({ path: path.join(here, 'shots', 'typeit.png'), scale: 'css' }).catch(() => {});
    await page.locator('#btnType').tap(); await page.waitForSelector('#claim', { state: 'visible' });
    r.sub = await text(page, 'claimSub'); r.stateAtTap = (await about(page)).state; r.buttonWhileAsking = await page.locator('#barType').isVisible();
    await page.locator('#claimName').fill('heron'); await page.locator('#claimForm button[type=submit]').tap();
    await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
    r.typed = await st(page); r.stateWhenTyped = (await about(page)).state;
    await ready(page, 60000);                                      // nobody is waiting, and the download finishes all the same
    await page.waitForTimeout(1500);                               // the late answer for the photo already named by hand changes nothing
    r.after = await st(page); r.record = await page.evaluate(() => window.__seenBack.record().map((m) => m.common + '|' + m.by + '|' + m.key));
    r.next = await meet(page, 'stripes.png'); r.buttonNext = await page.locator('#barType').isVisible();   // the next photo is recognized, with no button
    r.trace = await page.evaluate(() => window.__seenBack.diag().filter((d) => d.what === 'type-instead').length); r.errors = errors;
    done('typeit', r, !r.buttonBefore && /^Downloading… \d+ of 15 MB$/.test(r.line) && r.button === 'Type it instead' && r.buttonUnderLine
      && r.sub === 'Your download is finishing in the background.' && r.stateAtTap === 'loading' && !r.buttonWhileAsking
      && r.typed.eyes === 'wader' && r.typed.named.by === 'you' && r.typed.named.common === 'heron' && r.after.eyes === 'wader' && r.after.named.by === 'you' && r.after.screen === 'askView' && r.record.length === 1 && r.record[0] === 'heron|you|wader'
      && r.next.eyes === 'insect' && !r.buttonNext && r.trace === 1 && !errors.length);
    await ctl('reset=1'); await ctx.close();
  });

  // ---------- the species service: a fake server that speaks Gradio's two-step call (test/rec/fake_service.js)
  let fake = null;
  // a sleeping server's refusals are written to the console by the browser itself, each engine in its own words: Chromium "blocked by CORS policy",
  // "net::ERR_"; Firefox "Cross-Origin Request Blocked"; WebKit "Preflight response is not successful", "due to access control checks" (runs engines/33)
  const quiet = (errors) => errors.filter((e) => !/blocked by CORS policy|net::ERR_|Cross-Origin Request Blocked|Preflight response is not successful|due to access control checks|is not allowed by Access-Control-Allow-Origin/.test(e));
  const svcFiles = async () => {
    if (!fake) fake = await require('./fake_service.js').start(SVC_PORT);
    fake.reset();
    const dir = path.join(here, 'shots'), base = { api: 'gradio', call: 'http://127.0.0.1:' + SVC_PORT + '/gradio_api/call/identify', region: 'us-fl-alachua', model: 'fake-naturalist', kind_at: 0.9, name_at: 0.5 };
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(path.join(dir, 'service.json'), JSON.stringify(base));
    fs.writeFileSync(path.join(dir, 'service.health.json'), JSON.stringify(Object.assign({ health: 'http://127.0.0.1:' + SVC_PORT + '/health' }, base)));
    fs.writeFileSync(path.join(dir, 'service.elsewhere.json'), JSON.stringify(Object.assign({}, base, { api: 'rest' })));     // an arrangement this build does not know
    return '&nosw=1&rec=' + SLOT + '&svc=test/rec/shots/';
  };

  if (want.includes('service')) await section('service', async () => {   // consent first; what is sent; the answer on screen and in the record; another kind offered, never taken; sleep, failure, refusal
    const Q = await svcFiles(), r = {}; let ok = true; const all = (name, cond) => { if (!cond) { ok = false; (r.failed = r.failed || []).push(name); } };
    { // no service.json: the feature does not exist, nothing mentions it, and the file is asked for only once a photo is left without a species name
      await ctl('reset=1');
      const { ctx, page, errors } = await open(browser, '&nosw=1&rec=' + SLOT + '&svc=test/rec/nowhere.json'); await ready(page); await begin(page);
      const askedBefore = (await ctl('log=1')).filter((x) => /^test\/rec\/nowhere\.json/.test(x)).length;
      const s = await meet(page, 'stripes.png'); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); await page.waitForTimeout(500);
      r.absent = { askedBefore, askedAfter: (await ctl('log=1')).filter((x) => /^test\/rec\/nowhere\.json/.test(x)).length, eyes: s.eyes, line: await svcLine(page), posts: fake.calls().length };
      await page.locator('#backAskView').tap(); await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' }); await aboutOpen(page);
      r.absent.aboutMentionsIt = await page.locator('#svcBox').isVisible(); r.absent.errors = errors;
      all('absent', askedBefore === 0 && r.absent.askedAfter === 1 && s.eyes === 'insect' && r.absent.line === '' && r.absent.posts === 0 && !r.absent.aboutMentionsIt && !errors.length);
      await ctx.close();
      const b = await open(browser, Q + 'service.elsewhere.json'); await ready(b.page); await begin(b.page); await meet(b.page, 'stripes.png'); await b.page.waitForTimeout(600);
      r.unknownArrangement = { line: await svcLine(b.page), posts: fake.calls().length }; all('unknownArrangement', r.unknownArrangement.line === '' && r.unknownArrangement.posts === 0); await b.ctx.close();
    }
    { // consent first
      const { ctx, page, errors } = await open(browser, Q + 'service.json'); await ready(page);
      // how service.json is read: where the server is said to be, and what is not accepted as a service at all
      r.read = await page.evaluate(() => { const read = window.__seenBack.svc.test.read, c = 'https://someone-seen-back.hf.space/gradio_api/call/identify';
        const a = read({ api: 'gradio', call: c, region: 'us-fl-alachua', model: 'bioclip2-l14' }), b = read({ api: 'gradio', call: 'https://example.org/gradio_api/call/identify' });
        return { hf: a && a.where, kindAt: a && a.kindAt, nameAt: a && a.nameAt, top: a && a.top, other: b && b.where, plainHttp: read({ api: 'gradio', call: 'http://example.org/call/identify' }), noCall: read({ api: 'gradio' }), restApi: read({ api: 'rest', call: c }), notAnObject: read('x') }; });
      all('read', r.read.hf === 'hosted by Hugging Face' && r.read.kindAt === null && r.read.nameAt === 0 && r.read.top === 5 && r.read.other === 'at example.org' && r.read.plainHttp === null && r.read.noCall === null && r.read.restApi === null && r.read.notAnObject === null);
      await begin(page); await svcWatch(page);
      const s1 = await meet(page, 'stripes.png');
      await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); await page.waitForSelector('#svcView', { state: 'visible', timeout: 6000 });
      r.offer = { eyesAtOnce: s1.eyes, shown: s1.shown, line: await text(page, 'svcView'), sentBeforeYes: fake.calls().length };
      await page.screenshot({ path: path.join(here, 'shots', 'service-offer.png'), scale: 'css' }).catch(() => {});
      await page.locator('#svcView').tap(); await page.waitForSelector('#ask', { state: 'visible' }); await page.waitForTimeout(150);
      r.sheet = { title: await page.locator('#ask h3').textContent(), sub: await text(page, 'askSub'), tick: (await page.locator('#ask .tick').textContent()).trim(), yes: await text(page, 'askYes'), no: await text(page, 'askNo'), note: await page.locator('#ask .note').textContent(), ticked: await page.locator('#askKeep').isChecked() };
      await page.screenshot({ path: path.join(here, 'shots', 'service-ask.png'), scale: 'css' }).catch(() => {});
      await page.locator('#askNo').tap(); await page.waitForTimeout(300);
      r.notNow = { line: await svcLine(page), sent: fake.calls().length, choice: await page.evaluate(() => window.__seenBack.svc.choice()), named: (await st(page)).named.by };
      all('offer', r.offer.eyesAtOnce === 'insect' && r.offer.shown === 'insect' && r.offer.line === 'The full database on a server can try to name the species. Ask it?' && r.offer.sentBeforeYes === 0);
      all('sheet', r.sheet.title === 'Ask the full database?' && r.sheet.sub === 'This photo will be temporarily sent to this project’s server, at 127.0.0.1:' + SVC_PORT + '.'
        && r.sheet.tick === 'Do not ask again' && r.sheet.yes === 'Ask it' && r.sheet.no === 'Later' && /under About/.test(r.sheet.note) && !r.sheet.ticked);
      all('notNow', r.notNow.line === '' && r.notNow.sent === 0 && r.notNow.choice === '' && r.notNow.named === 'page');
      // the next photo asks again. This time: yes, and do not ask again
      fake.set({ delay: 700 });
      await meet(page, 'stripes.png'); await page.waitForSelector('#svcView', { state: 'visible', timeout: 8000 });
      await page.locator('#svcView').tap(); await page.waitForSelector('#ask', { state: 'visible' }); await page.locator('#askKeep').check(); await page.locator('#askYes').tap();
      await byService(page); await page.waitForTimeout(200);
      const month = new Date().getMonth() + 1;
      r.asked = { named: (await st(page)).named, lines: await page.evaluate(() => window.__svc.filter(Boolean).filter((x, i, a) => a.indexOf(x) === i)), sent: fake.calls(), choice: await page.evaluate(() => window.__seenBack.svc.choice()), record: await recordRows(page), line: await svcLine(page) };
      const c = r.asked.sent[0] || {};
      all('asked', r.asked.named.common === 'monarch' && r.asked.named.scientific === 'Danaus plexippus' && r.asked.named.by === 'service' && r.asked.lines.indexOf('Asking the full database…') >= 0 && r.asked.line === 'The full database says monarch.' && r.asked.choice === 'yes'
        && r.asked.record[0] === 'monarch|Danaus plexippus|service|insect' && r.asked.record.length === 2);
      all('whatWasSent', r.asked.sent.length === 1 && c.jpeg && Math.max(c.w, c.h) === 512 && c.imageBytes < 1e6 && c.fields === 4 && c.month === month && c.region === 'us-fl-alachua' && c.top === 5 && !c.prefix && c.cookie === '' && c.referer === '' && c.auth === '' && /^application\/json/.test(c.type));
      // the sheet behind the name, the list of meetings, and its five likeliest as offers
      await page.locator('#inViewPick').setInputFiles(path.join(here, '..', 'assets', 'portrait.jpg'));
      await page.waitForFunction(() => window.__seenBack.S.screen === 'animal', null, { timeout: 12000 });
      r.pill = await text(page, 'whoName'); await page.locator('#btnWho').tap(); await page.waitForSelector('#info', { state: 'visible' }); r.infoSub = await text(page, 'infoSub');
      await page.locator('#infoChange').tap(); await page.waitForSelector('#claim', { state: 'visible' }); await page.waitForTimeout(150);
      r.offers = await page.evaluate(() => [...document.querySelectorAll('#claimOffers button')].map((b) => b.textContent)); await page.locator('#claimBack').tap();
      await page.evaluate(() => history.back()); await page.waitForTimeout(200); await page.evaluate(() => history.back()); await page.waitForTimeout(200);
      await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' });
      r.rows = await page.evaluate(() => [...document.querySelectorAll('#metList li')].map((li) => li.querySelector('.nm').textContent + ' | ' + li.querySelector('.sm').textContent));
      await aboutOpen(page);
      r.about = await page.evaluate(() => ({ shown: !document.getElementById('svcBox').hidden, value: document.getElementById('svcChoice').value, options: [...document.querySelectorAll('#svcChoice option')].map((o) => o.textContent), label: document.querySelector('#svcBox label').textContent }));
      await page.evaluate(() => { document.getElementById('record').scrollTop = 99999; }); await page.waitForTimeout(150); await page.screenshot({ path: path.join(here, 'shots', 'service-about.png'), scale: 'css' }).catch(() => {});
      await shut(page);
      all('shownAfter', r.pill === 'monarch' && r.infoSub === 'Danaus plexippus'
        && r.offers.join() === 'monarch,queen,Gulf fritillary,viceroy,common buckeye' && /^monarch \| Danaus plexippus .* named by the full database on a server · This creature’s view is yours for a week$/.test(r.rows[0]) && r.about.shown && r.about.value === 'yes' && r.about.options.join() === 'Ask me each time,Always ask it,Never ask it');
      // from now on it is asked without a prompt. It sees another kind of creature and is sure: the change is offered in one line, and not made
      fake.set({ answer: 'egret', delay: 300 }); let n = fake.calls().length;
      await meet(page, 'dots.png'); await page.waitForFunction(() => /Change to this creature\?$/.test(document.getElementById('svcView').textContent), null, { timeout: 15000 });
      await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
      const before = await st(page);
      r.change = { line: await text(page, 'svcView'), eyesBefore: before.eyes, namedBefore: before.named.common + '|' + before.named.by, posts: fake.calls().length - n, meetings: (await recordRows(page)).length };
      await page.screenshot({ path: path.join(here, 'shots', 'service-change.png'), scale: 'css' }).catch(() => {});
      await page.locator('#svcView').tap(); await page.waitForFunction(() => window.__seenBack.S.eyes === 'wader', null, { timeout: 6000 }); await page.waitForTimeout(300);
      const after = await st(page); r.change.after = after.eyes + '|' + after.named.common + '|' + after.named.by; r.change.record = await recordRows(page); r.change.lineAfter = await svcLine(page);
      all('change', r.change.line === 'It looks like a great egret, a wading bird. Change to this creature?' && r.change.eyesBefore === 'frog' && r.change.namedBefore === 'frog or toad|page' && r.change.posts === 1
        && r.change.after === 'wader|great egret|service' && r.change.record[0] === 'great egret|Ardea alba|service|wader' && r.change.record.length === r.change.meetings && r.change.lineAfter === '');
      // another kind, but it is not sure enough: nothing changes, and its likeliest stay as offers
      fake.set({ answer: 'unsure' }); n = fake.calls().length;
      await meet(page, 'dots.png'); await until(() => fake.calls().length > n); await svcSettled(page); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); await page.waitForTimeout(200);
      const u = await st(page); r.unsure = { state: u.eyes + '|' + u.named.common + '|' + u.named.by, line: await svcLine(page) };
      await page.locator('#changeAskView').tap(); await page.waitForSelector('#claim', { state: 'visible' }); await page.waitForTimeout(150);
      r.unsure.offers = await page.evaluate(() => [...document.querySelectorAll('#claimOffers button')].map((b) => b.textContent)); await page.locator('#claimBack').tap();
      all('unsure', r.unsure.state === 'frog|frog or toad|page' && r.unsure.line === '' && r.unsure.offers.join() === 'great egret,green treefrog,snowy egret');
      // the same kind, but its best guess is under the service's own mark for naming: the name stays, the guesses are offered
      fake.set({ answer: 'faint' }); n = fake.calls().length;
      await meet(page, 'stripes.png'); await until(() => fake.calls().length > n); await svcSettled(page); await page.waitForTimeout(200);
      const f = await st(page); r.faint = f.eyes + '|' + f.named.common + '|' + f.named.by; all('faint', r.faint === 'insect|insect|page');
      // the device named the species itself: nobody is asked
      n = fake.calls().length; await meet(page, 'heron.png'); await page.waitForTimeout(900);
      r.namedByDevice = { posts: fake.calls().length - n, by: (await st(page)).named.by, line: await svcLine(page) }; all('namedByDevice', r.namedByDevice.posts === 0 && r.namedByDevice.by === 'page' && r.namedByDevice.line === '');
      // a name typed while the question is out is not overwritten when the answer comes
      fake.set({ answer: 'monarch', delay: 1500 }); n = fake.calls().length;
      await meet(page, 'stripes.png'); await until(() => fake.calls().length > n); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
      await page.locator('#changeAskView').tap(); await typeName(page, 'beetle'); await page.waitForTimeout(2300);
      const t = await st(page); r.typedWins = t.named.common + '|' + t.named.by; all('typedWins', r.typedWins === 'beetle|you');
      // "Never ask it", chosen in the About block: no line, nothing sent; and back to asking each time
      await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); await page.locator('#backAskView').tap(); await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' });
      await aboutOpen(page);
      await page.selectOption('#svcChoice', 'no'); await shut(page);
      fake.set({ delay: 0 }); n = fake.calls().length; await meet(page, 'stripes.png'); await page.waitForTimeout(900);
      r.never = { posts: fake.calls().length - n, line: await svcLine(page), choice: await page.evaluate(() => window.__seenBack.svc.choice()) };
      await page.evaluate(() => window.__seenBack.svc.setChoice('')); await meet(page, 'stripes.png'); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); await page.waitForTimeout(400);
      r.eachTimeAgain = await svcLine(page);
      all('never', r.never.posts === 0 && r.never.line === '' && r.never.choice === 'no' && r.eachTimeAgain === 'The full database on a server can try to name the species. Ask it?');
      r.errors = errors; all('noErrors', !errors.length);
      await ctx.close();
    }
    for (const [name, file] of [['asleep', 'service.json'], ['asleepWithHealth', 'service.health.json']]) {   // a sleeping server: one honest line, then the answer
      fake.reset(); const { ctx, page, errors } = await open(browser, Q + file); await ready(page);
      await page.evaluate(() => { window.__seenBack.svc.setChoice('yes'); window.__seenBack.svc.test.times({ poll: 400 }); }); await begin(page); await svcWatch(page);
      fake.sleep(600000); const t0 = Date.now(); await meet(page, 'stripes.png');
      await page.waitForFunction(() => window.__svc.indexOf('The full database is waking up. This can take a minute…') >= 0, null, { timeout: 15000 });
      const eyesWhileWaiting = (await st(page)).eyes; await page.waitForTimeout(1300); fake.sleep(0);     // it wakes
      await byService(page);
      r[name] = { lines: await page.evaluate(() => window.__svc.filter(Boolean).filter((x, i, a) => a.indexOf(x) === i)), eyesWhileWaiting, named: (await st(page)).named.common, posts: fake.calls().length, healthAsked: fake.state.health, wokeAfterMs: Date.now() - t0, errors: quiet(errors) };
      all(name, r[name].lines.join(' / ') === 'Asking the full database… / The full database is waking up. This can take a minute… / The full database says monarch.' && eyesWhileWaiting === 'insect' && r[name].named === 'monarch' && r[name].posts === 1 && (file === 'service.json' ? r[name].healthAsked === 0 : r[name].healthAsked >= 2) && !r[name].errors.length);
      await ctx.close();
    }
    { // it does not wake within the wait (shortened here from 90 seconds to 8): it lets go quietly, and what the device said stands. Then failures and refusals of every sort
      fake.reset(); const { ctx, page, errors } = await open(browser, Q + 'service.json'); await ready(page);
      r.waitByDefault = await page.evaluate(() => { window.__seenBack.svc.setChoice('yes'); const t = window.__seenBack.svc.test.times({}); return { wake: t.wake, answer: t.answer }; });
      await page.evaluate(() => { window.__seenBack.svc.test.times({ wake: 8000, poll: 400 }); }); await begin(page); await svcWatch(page);
      fake.sleep(600000); await meet(page, 'stripes.png');
      await page.waitForFunction(() => window.__svc.length >= 2 && window.__svc[window.__svc.length - 1] === '', null, { timeout: 40000 });
      const s = await st(page);
      r.neverWakes = { lines: await page.evaluate(() => window.__svc.filter((x, i, a) => (i || x) && (!i || a[i - 1] !== x))), state: s.eyes + '|' + s.named.common + '|' + s.named.by, claim: s.claim, msg: await text(page, 'msg'), why: await page.evaluate(() => window.__seenBack.diag().filter((d) => d.what === 'service-none').map((d) => d.code).join()) };
      all('neverWakes', r.waitByDefault.wake === 90000 && r.neverWakes.lines.join(' / ') === 'Asking the full database… / The full database is waking up. This can take a minute… / ' && r.neverWakes.state === 'insect|insect|page' && !r.neverWakes.claim && r.neverWakes.msg === '' && r.neverWakes.why === 'asleep');
      await page.evaluate(() => { window.__seenBack.svc.test.times({ wake: 90000, answer: 1500 }); });
      r.failures = {};
      for (const mode of ['error', 'garbled', 'refusal', 'refuse', 'busy', 'slow']) {
        fake.reset(); fake.set(mode === 'slow' ? { delay: 4000 } : { mode });
        await meet(page, 'stripes.png'); await until(() => fake.calls().length > 0); await svcSettled(page); await page.waitForTimeout(150);
        const x = await st(page);
        r.failures[mode] = { state: x.eyes + '|' + x.named.common + '|' + x.named.by, line: await svcLine(page), posts: fake.calls().length, claim: x.claim, msg: await text(page, 'msg') };
        all('failure ' + mode, r.failures[mode].state === 'insect|insect|page' && r.failures[mode].line === '' && r.failures[mode].posts === 1 && !x.claim && r.failures[mode].msg === '');
      }
      r.failureCodes = await page.evaluate(() => window.__seenBack.diag().filter((d) => d.what === 'service-none').map((d) => d.code).join());
      r.failureErrors = quiet(errors); all('failuresQuiet', !r.failureErrors.length);
      await ctx.close();
    }
    { // from the sheet that asks for a name there is a way to the full database: consent first, then its answer is taken as the name
      fake.reset(); fake.set({ answer: 'egret', delay: 300 }); const { ctx, page, errors } = await open(browser, Q + 'service.json'); await ready(page); await begin(page);
      const s = await meet(page, 'wall.png'); await page.evaluate(() => { document.getElementById('noticeOk').click(); window.__seenBack.openClaim(''); }); await page.waitForSelector('#claim', { state: 'visible', timeout: 4000 }); await page.waitForSelector('#claimAskRow', { state: 'visible', timeout: 6000 });
      r.fromSheet = { sub: await text(page, 'claimSub'), link: await text(page, 'claimAsk'), sentBefore: fake.calls().length };
      await page.locator('#claimAsk').tap(); await page.waitForSelector('#ask', { state: 'visible' }); r.fromSheet.askSub = await text(page, 'askSub'); r.fromSheet.sentAtSheet = fake.calls().length;
      await page.locator('#askNo').tap(); await page.waitForSelector('#claim', { state: 'visible', timeout: 4000 }); r.fromSheet.afterNo = (await st(page)).claim; r.fromSheet.sentAfterNo = fake.calls().length;
      await page.waitForSelector('#claimAskRow', { state: 'visible', timeout: 6000 }); await page.locator('#claimAsk').tap(); await page.waitForSelector('#ask', { state: 'visible' }); await page.locator('#askYes').tap();
      await byService(page); await page.waitForTimeout(200);
      const x = await st(page); r.fromSheet.after = x.eyes + '|' + x.named.common + '|' + x.named.by; r.fromSheet.record = await recordRows(page); r.fromSheet.sent = fake.calls().length;
      // it cannot name it: back to the sheet, with its guesses as offers, and no second link
      fake.set({ answer: 'faint' }); const s2 = await meet(page, 'wall.png'); await page.evaluate(() => { document.getElementById('noticeOk').click(); window.__seenBack.openClaim(''); }); await page.waitForSelector('#claim', { state: 'visible', timeout: 4000 }); await page.waitForSelector('#claimAskRow', { state: 'visible', timeout: 6000 }); await page.locator('#claimAsk').tap(); await page.waitForSelector('#ask', { state: 'visible' }); await page.locator('#askYes').tap();
      await page.waitForFunction(() => /can’t ID this photo/.test(document.getElementById('claimSub').textContent) && !document.getElementById('claim').hidden, null, { timeout: 15000 }); await page.waitForTimeout(400);
      r.fromSheet.faint = { sub: await text(page, 'claimSub'), offers: await page.evaluate(() => [...document.querySelectorAll('#claimOffers button')].map((b) => b.textContent)), linkAgain: await page.locator('#claimAskRow').isVisible(), eyes: (await st(page)).eyes };
      r.fromSheet.errors = errors;
      all('fromSheet', r.fromSheet.sub === '' && r.fromSheet.link === 'Ask the full database on a server' && r.fromSheet.sentBefore === 0 && /temporarily sent to this project’s server/.test(r.fromSheet.askSub) && r.fromSheet.sentAtSheet === 0 && r.fromSheet.afterNo && r.fromSheet.sentAfterNo === 0
        && r.fromSheet.after === 'wader|great egret|service' && r.fromSheet.record[0] === 'great egret|Ardea alba|service|wader' && r.fromSheet.sent === 1
        && r.fromSheet.faint.sub === 'The full database can’t ID this photo.' && r.fromSheet.faint.offers.join() === 'monarch,queen,Gulf fritillary' && !r.fromSheet.faint.linkAgain && !r.fromSheet.faint.eyes && !errors.length);
      await ctx.close();
    }
    fake.reset();
    done('service', r, ok);
  });

  // ---------- the full database on this device: a stand-in cut into three parts, served from a second origin (another port) with CORS
  let bigServer = null;
  const bigUp = async () => {
    try { await bctl('reset=1'); } catch (e) {
      bigServer = require('child_process').spawn(process.execPath, [path.join(here, 'serve.js'), String(BIG_PORT), 'cors'], { stdio: 'ignore' });
      let up = false; for (let i = 0; i < 50 && !up; i++) { try { await bctl('reset=1'); up = true; } catch (e2) { await new Promise((res) => setTimeout(res, 100)); } }
      if (!up) throw new Error('no second server on port ' + BIG_PORT);
    }
    if (BIG_PORT === 8788) return BIG;                 // the stand-in's manifest names that port; for another, a copy of it is written beside it
    for (const f of ['manifest.json', 'manifest.bad-whole.json']) fs.writeFileSync(path.join(here, 'models', 'standin-big', f.replace('manifest', 'manifest.port')), fs.readFileSync(path.join(here, 'models', 'standin-big', f), 'utf8').replace(/127\.0\.0\.1:8788/g, '127.0.0.1:' + BIG_PORT));
    return BIG + '/manifest.port.json';
  };
  const bigNow = (page) => page.evaluate(() => { const B = window.__seenBack, a = B.big.about(), l = a.last; return { have: a.have, kept: a.keptBytes, bytes: a.bytes, state: a.state, why: a.why, fail: a.fail, getFail: a.getFail, choice: B.bigChoice(), running: B.big.test.running(),
    last: l && { kind: l.kind, sure: l.sure, named: l.named ? (l.named.en || l.named.sci) : '', kindOffers: l.kindOffers, five: l.species.map((x) => x.en || x.sci), at: l.at, ms: l.ms } }; });
  const bigHave = (page, what, ms) => page.waitForFunction((w) => window.__seenBack.big.about().have === w, what, { timeout: ms || 30000 });
  const lineIs = (page, re, ms) => page.waitForFunction((src) => { const vis = (e) => !e.hidden && e.offsetParent !== null, a = document.getElementById('svcView'), b = document.getElementById('svcHud'); return new RegExp(src).test(vis(a) ? a.textContent : vis(b) ? b.textContent : ''); }, re.source, { timeout: ms || 20000 });
  const partsAsked = async () => (await bctl('log=1')).map((x) => (/part\d\d/.exec(x) || [''])[0]).filter(Boolean);
  const keptBig = (page) => page.evaluate(async () => (await (await caches.open('keep-v1')).keys()).map((q) => q.url).filter((u) => /standin-big\//.test(u)).map((u) => u.replace(/^.*standin-big\//, '').replace(/[0-9a-f]{64}/, 'SHA').replace(/v=[0-9a-f]+/, 'v=V')).sort());
  const byLarge = (page) => page.waitForFunction(() => { const n = window.__seenBack.S.named; return !!n && n.by === 'device-large'; }, null, { timeout: 30000 });
  const largeAfter = (page, at) => page.waitForFunction((t) => { const l = window.__seenBack.big.about().last; return !!l && l.at > t && !window.__seenBack.S.svc; }, at, { timeout: 30000 });
  const offered = async (page) => { await page.waitForSelector('#askView', { state: 'visible', timeout: 8000 }); await page.waitForSelector('#svcView', { state: 'visible', timeout: 8000 }); return text(page, 'svcView'); };
  const getIt = async (page) => { await page.locator('#svcView').tap(); await page.waitForSelector('#big', { state: 'visible' }); await page.locator('#bigYes').tap(); };
  const toAbout = async (page) => { if ((await st(page)).eyes) await page.waitForSelector('#askView', { state: 'visible', timeout: 8000 }); if ((await st(page)).screen === 'askView') await page.locator('#backAskView').tap(); await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' });
    await page.waitForTimeout(350); await page.evaluate(() => { document.getElementById('record').scrollTop = 99999; }); };

  // the full database for the whole world, in the large section and on its own as "world": a stand-in's rows at one byte a number, names and place files
  const worldBlock = async (r, all) => {
    { // the full database for the whole world (docs/tracks/worlddb.md): its rows at one byte a number, its names and its place files in parts from the
      // second origin, and its consent sheet's size of them all; the first guess from the time zone, and the encounter rule (test/rec/make_world_standin.py)
      const WD = path.join(here, 'models', 'standin-world'), WE = JSON.parse(fs.readFileSync(path.join(WD, 'expect.json'), 'utf8'));
      let wslot = 'test/rec/models/standin-world';
      if (BIG_PORT !== 8788) { fs.writeFileSync(path.join(WD, 'manifest.port.json'), fs.readFileSync(path.join(WD, 'manifest.json'), 'utf8').replace(/127\.0\.0\.1:8788/g, '127.0.0.1:' + BIG_PORT)); wslot += '/manifest.port.json'; }
      const named = async (page) => { const n = (await st(page)).named; return n ? n.common + '|' + n.by : ''; };
      const worldIn = async (tz) => {
        await ctl('reset=1'); await bctl('reset=1');
        const ctx = await browser.newContext(Object.assign({}, phone, { timezoneId: tz }));
        const o = await open(browser, '&nosw=1&rec=' + SLOT + '&big=' + wslot, null, ctx); await ready(o.page); await begin(o.page);
        const s0 = await meet(o.page, 'stripes.png'); const line = await offered(o.page);
        const size = await o.page.evaluate(() => window.__seenBack.big.size());
        await o.page.locator('#svcView').tap(); await o.page.waitForSelector('#big', { state: 'visible' }); await o.page.locator('#bigYes').tap();
        await bigHave(o.page, 'kept', 60000); await o.page.waitForFunction(() => { const l = window.__seenBack.big.about().last; return !!l && !window.__seenBack.S.svc; }, null, { timeout: 60000 }); await o.page.waitForTimeout(200);
        return { ctx, page: o.page, errors: o.errors, small: s0.eyes, line, size, parts: (await partsAsked()).sort() };
      };
      r.world = {};
      { const w = await worldIn('UTC'), pg = w.page;
        const a1 = await bigNow(pg);
        r.world.utc = { small: w.small, line: w.line, bytes: w.size.bytes, parts: w.parts, first: await named(pg), last: a1.last && a1.last.five.slice(0, 2).join(' / '), place0: await pg.evaluate(() => window.__seenBack.big.about().place) };
        await meet(pg, 'heron.png'); await byLarge(pg); await pg.waitForTimeout(150);
        r.world.utc.heron = await named(pg); r.world.utc.kept = await pg.evaluate(() => JSON.parse(localStorage.getItem('seenback.place.v1') || 'null'));
        r.world.utc.place1 = await pg.evaluate(() => window.__seenBack.big.about().place);
        const at = (await bigNow(pg)).last.at; await meet(pg, 'stripes.png'); await largeAfter(pg, at); await pg.waitForTimeout(150);
        r.world.utc.then = await named(pg);
        r.world.utc.parity = await pg.evaluate((x) => { const t = window.__seenBack.big.test.place(), c = x.cells, d = (P) => [P[c[0]], P[c[1]]];
          const P = t.update(t.firstGuess('UTC'), x.rows['Great Blue Heron']), L = t.logShare(P);
          return { first: { UTC: d(t.firstGuess('UTC')), 'America/New_York': d(t.firstGuess('America/New_York')), 'America/Argentina/Buenos_Aires': d(t.firstGuess('America/Argentina/Buenos_Aires')) }, after: d(P), share: Array.from(L) }; }, WE);
        r.world.utc.alias = await pg.evaluate(() => { const t = window.__seenBack.big.test.place(), a = t.firstGuess('US/Eastern'), b = t.firstGuess('America/New_York'), c = t.firstGuess('America/Buenos_Aires'), d = t.firstGuess('America/Argentina/Buenos_Aires');
          return a.every((x, i) => x === b[i]) && c.every((x, i) => x === d[i]) && a.some((x, i) => x !== c[i]); });
        r.world.utc.about = await pg.evaluate(() => window.__seenBack.about()); r.world.utc.errors = w.errors; await w.ctx.close(); }
      for (const tz of ['America/Argentina/Buenos_Aires', 'US/Eastern']) {
        const w = await worldIn(tz); await byLarge(w.page).catch(() => {}); r.world[tz] = { first: await named(w.page), place: await w.page.evaluate(() => window.__seenBack.big.about().place), errors: w.errors }; await w.ctx.close();
      }
      const u = r.world.utc, near = (a, b) => a.length === b.length && a.every((x, i) => Math.abs(x - b[i]) < 1e-6 * Math.max(1, Math.abs(b[i])));
      const sameP = Object.keys(WE.first_guess).every((z) => near(u.parity.first[z], WE.first_guess[z])) && near(u.parity.after, WE.after_heron) && near(u.parity.share, WE.log_share_utc_heron);
      const wantParts = ['part00', 'part00', 'part01', 'part01', 'part02'];       // the encoder's three parts and the rows' two, each once
      all('world', u.small === 'insect' && u.line === 'Download the full database of species?' && u.bytes === WE.bytes && u.parts.join() === wantParts.join()
        && u.first === 'insect|page' && /Monarch/.test(u.last || '') && u.place0 && u.place0.zone === 'UTC' && u.place0.known === false && u.place0.met === 0
        && u.heron === 'great blue heron|device-large' && u.kept && u.kept.met.length === 1 && u.kept.met[0].sci === 'Ardea herodias' && u.kept.met[0].zone === 'UTC' && u.place1.met === 1
        && u.then === 'monarch|device-large' && sameP && u.alias && /place from no known time zone and 2 creatures met\.$/m.test(u.about || '')
        && r.world['America/Argentina/Buenos_Aires'].first === 'southern monarch|device-large' && r.world['America/Argentina/Buenos_Aires'].place.known
        && r.world['US/Eastern'].first === 'monarch|device-large' && r.world['US/Eastern'].place.known
        && !quiet(u.errors).length && !quiet(r.world['America/Argentina/Buenos_Aires'].errors).length && !quiet(r.world['US/Eastern'].errors).length);
      r.world.sameAsPython = sameP;
    }
  };
  if (want.includes('large')) await section('large', async () => {    // consent, progress, a reload mid-way, stopping, deleting; the answer in the background; another kind offered, never taken; failures in words
    const slot = await bigUp(), Q = '&nosw=1&rec=' + SLOT + '&big=' + slot, r = {}; let ok = true; sofar = r; const all = (name, cond) => { if (!cond) { ok = false; (r.failed = r.failed || []).push(name); } };
    const MB = Math.max(1, Math.round(JSON.parse(fs.readFileSync(path.join(here, 'models', 'standin-big', 'manifest.json'), 'utf8')).vision.bytes / 1e6));
    const E = (name) => expect.big[name][month];
    { // no such model: the feature does not exist, and nothing mentions it
      await ctl('reset=1'); const { ctx, page, errors } = await open(browser, '&nosw=1&rec=' + SLOT + '&big=test/rec/nowhere'); await ready(page); await begin(page);
      const s = await meet(page, 'stripes.png'); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); await page.waitForTimeout(500);
      r.absent = { eyes: s.eyes, line: await svcLine(page), asked: (await ctl('log=1')).filter((x) => !/^index\.html/.test(x) && /nowhere/.test(x)).length }; await toAbout(page);
      r.absent.aboutMentionsIt = await page.locator('#bigBox').isVisible(); r.absent.errors = errors;
      all('absent', s.eyes === 'insect' && r.absent.line === '' && r.absent.asked === 1 && !r.absent.aboutMentionsIt && !errors.length); await ctx.close();
    }
    { // consent first, in plain words; what the connection says of itself; do not ask again; the About block
      await ctl('reset=1'); await bctl('reset=1');
      const { ctx, page, errors } = await open(browser, Q); await ready(page); await begin(page);
      const d = await page.evaluate(() => (matchMedia('(pointer: coarse)').matches ? 'phone' : 'computer')); r.device = d;
      const before = (await ctl('log=1')).filter((x) => !/^index\.html/.test(x) && /standin-big/.test(x)).length;
      const s = await meet(page, 'stripes.png');
      r.offer = { manifestAskedBeforeAPhoto: before, eyesAtOnce: s.eyes, shown: s.shown, line: await offered(page), partsAsked: (await partsAsked()).length };
      await page.locator('#svcView').tap(); await page.waitForSelector('#big', { state: 'visible' }); await page.waitForTimeout(150);
      r.sheet = { title: await text(page, 'bigTitle'), sub: await text(page, 'bigSub'), net: await text(page, 'bigNet'), yes: await text(page, 'bigYes'), no: await text(page, 'bigNo'), never: await text(page, 'bigNever'),
        note: await page.locator('#big .note:not(#bigNet)').textContent(), stopShown: await page.locator('#bigStop').isVisible(), overflow: await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth) };
      fs.mkdirSync(path.join(here, 'shots'), { recursive: true }); await page.screenshot({ path: path.join(here, 'shots', 'large-ask.png'), scale: 'css' }).catch(() => {});
      await page.locator('#bigNo').tap(); await page.waitForTimeout(300);
      r.notNow = { line: await svcLine(page), choice: (await bigNow(page)).choice, parts: (await partsAsked()).length, by: (await st(page)).named.by };
      r.net = {};
      for (const [name, c] of [['save', { saveData: true }], ['metered', { type: 'cellular' }], ['slow', { effectiveType: '2g' }]]) {
        await page.evaluate((c) => Object.defineProperty(navigator, 'connection', { value: c, configurable: true }), c);
        await meet(page, 'stripes.png'); await offered(page); await page.locator('#svcView').tap(); await page.waitForSelector('#big', { state: 'visible' });
        r.net[name] = await text(page, 'bigNet'); await page.locator('#bigNo').tap(); await page.waitForTimeout(200);
      }
      await page.evaluate(() => Object.defineProperty(navigator, 'connection', { value: undefined, configurable: true }));
      await meet(page, 'stripes.png'); await offered(page); await page.locator('#svcView').tap(); await page.waitForSelector('#big', { state: 'visible' }); await page.evaluate(() => document.getElementById('bigNever').click()); await page.waitForTimeout(200);
      r.never = { choice: (await bigNow(page)).choice }; await meet(page, 'stripes.png'); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); await page.waitForTimeout(600); r.never.line = await svcLine(page);
      await toAbout(page); await page.waitForSelector('#bigBox', { state: 'visible', timeout: 5000 });
      r.aboutAbsent = { state: await text(page, 'bigState'), get: await page.locator('#bigGet').isVisible(), del: await page.locator('#bigDel').isVisible(), halt: await page.locator('#bigHalt').isVisible(), ticked: await page.locator('#bigAsk').isChecked(), tick: (await page.locator('#bigAskRow').textContent()).trim() };
      await page.screenshot({ path: path.join(here, 'shots', 'large-about.png'), scale: 'css' }).catch(() => {});
      await page.evaluate(() => { const b = document.getElementById('bigAsk'); b.checked = false; b.dispatchEvent(new Event('change', { bubbles: true })); }); r.aboutAbsent.choiceAfter = (await bigNow(page)).choice; r.aboutAbsent.parts = (await partsAsked()).length; r.consentErrors = errors;
      all('offer', before === 0 && s.eyes === 'insect' && s.shown === 'insect' && r.offer.line === 'Download the full database of species?' && r.offer.partsAsked === 0);
      all('sheet', r.sheet.title === 'Get the full database?' && r.sheet.sub === 'The full database of species is free to download and provides more accuracy in IDing.'
        && r.sheet.net === '' && r.sheet.yes === 'Download' && r.sheet.no === 'Later' && r.sheet.never === 'Do not ask again' && /^You can always delete your download under your Encounters\.$/.test(r.sheet.note) && !r.sheet.stopShown && r.sheet.overflow <= 0);
      all('notNow', r.notNow.line === '' && r.notNow.choice === '' && r.notNow.parts === 0 && r.notNow.by === 'page');
      all('net', r.net.save === 'Your device is in data saver mode, and this download is about ' + MB + ' MB.' && r.net.metered === 'Your device’s connection is metered, and this download is about ' + MB + ' MB.' && r.net.slow === 'Your device’s connection is slow, and this download is about ' + MB + ' MB.');
      all('never', r.never.choice === 'no' && r.never.line === '');
      all('aboutAbsent', r.aboutAbsent.state === 'The full database of species is free to download and provides more accuracy in IDing.' && r.aboutAbsent.get && !r.aboutAbsent.del && !r.aboutAbsent.halt && r.aboutAbsent.ticked && r.aboutAbsent.tick === 'Do not offer the full database' && r.aboutAbsent.choiceAfter === '' && r.aboutAbsent.parts === 0 && !errors.length);
      await ctx.close();
    }
    { // the download: progress, each part kept as it arrives; a reload mid-way, after which it carries on by itself and fetches no kept part again
      await ctl('reset=1'); await bctl('reset=1'); await bctl('slow=' + encodeURIComponent('part01') + '&bps=50000');     // the second part takes about six seconds
      const ctx = await browser.newContext(Object.assign({}, phone)); let { page, errors } = await open(browser, Q, null, ctx); await ready(page); await begin(page); const d = r.device;
      await meet(page, 'stripes.png'); await offered(page); await svcWatch(page); await getIt(page);
      await page.waitForFunction(() => window.__seenBack.big.about().keptBytes > 300000, null, { timeout: 20000 });     // the first part is kept, the second is arriving
      const mid = await bigNow(page);
      r.progress = { have: mid.have, choice: mid.choice, lines: await page.evaluate(() => window.__svc.filter(Boolean).filter((x, i, a) => a.indexOf(x) === i)), kept: (await keptBig(page)).filter((k) => /^part/.test(k)).length, eyes: (await st(page)).eyes };
      await page.reload(); await page.waitForTimeout(300);
      r.afterReload = { choice: await page.evaluate(() => window.__seenBack.bigChoice()), have0: (await bigNow(page)).have };
      await bigHave(page, 'kept', 60000); await page.waitForFunction(() => window.__seenBack.bigChoice() === 'kept', null, { timeout: 30000 });
      const fin = await bigNow(page);
      r.resumed = { parts: await partsAsked(), kept: await keptBig(page), state: fin.state, choice: fin.choice, kept_bytes: fin.kept === fin.bytes, errors: errors.slice() };
      all('progress', mid.have === 'getting' && mid.choice === 'yes' && r.progress.lines.length >= 1 && r.progress.lines.every((l) => new RegExp('^Downloading the full database… \\d+ of ' + MB + ' MB$').test(l)) && r.progress.kept === 1 && r.progress.eyes === 'insect');
      all('resumed', r.afterReload.choice === 'yes' && r.resumed.parts.filter((x) => x === 'part00').length === 1 && r.resumed.parts.filter((x) => x === 'part01').length === 2 && r.resumed.parts.filter((x) => x === 'part02').length === 1
        && r.resumed.kept.filter((k) => /^part\/SHA/.test(k)).length === 3 && r.resumed.kept.indexOf('whole/SHA') >= 0 && fin.state === 'ready' && fin.choice === 'kept' && r.resumed.kept_bytes && !errors.length);
      // ---- on the device now: every photo is looked at in the background, and nothing is asked of any server
      await ctl('reset=1'); await bctl('reset=1'); await begin(page); await svcWatch(page); await watchOver(page);
      const s1 = await meet(page, 'stripes.png'); await byLarge(page); await page.waitForTimeout(150);
      r.named = { atOnce: s1.eyes + '|' + s1.last.kind + '|' + (s1.last.top && s1.last.top[0]) + '|' + s1.last.offers.length, small: await page.evaluate(() => { const l = window.__seenBack.rec.about().last; return l.kind + '|' + (l.named ? l.named.en : 'no name') + '|' + l.offers.length; }), after: (await st(page)).named, lines: await page.evaluate(() => window.__svc.filter(Boolean).filter((x, i, a) => a.indexOf(x) === i)), line: await svcLine(page), record: await recordRows(page),
        overlay: await page.evaluate(() => (document.getElementById('reveal').classList.contains('show') ? document.getElementById('rvName').textContent : '(gone)')), last: (await bigNow(page)).last, reference: E('stripes.png') };
      await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); await page.waitForTimeout(700); await page.screenshot({ path: path.join(here, 'shots', 'large-said.png'), scale: 'css' }).catch(() => {}); r.named.overSheet = await overNow(page);
      await page.locator('#inViewPick').setInputFiles(path.join(here, '..', 'assets', 'portrait.jpg')); await page.waitForFunction(() => window.__seenBack.S.screen === 'animal', null, { timeout: 12000 });
      r.named.pill = await text(page, 'whoName'); await page.locator('#btnWho').tap(); await page.waitForSelector('#info', { state: 'visible' }); r.named.infoSub = await text(page, 'infoSub');
      await page.locator('#infoChange').tap(); await page.waitForSelector('#claim', { state: 'visible' }); await page.waitForTimeout(150);
      r.named.offers = await page.evaluate(() => [...document.querySelectorAll('#claimOffers button')].map((b) => b.textContent)); await page.locator('#claimBack').tap();
      await page.evaluate(() => history.back()); await page.waitForTimeout(200); await page.evaluate(() => history.back()); await page.waitForTimeout(200);
      await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' });
      r.named.rows = await page.evaluate(() => [...document.querySelectorAll('#metList li')].slice(0, 1).map((li) => li.querySelector('.nm').textContent + ' | ' + li.querySelector('.sm').textContent));
      await page.waitForSelector('#bigBox', { state: 'visible', timeout: 5000 });
      r.aboutKept = { state: await text(page, 'bigState'), get: await page.locator('#bigGet').isVisible(), del: await page.locator('#bigDel').isVisible(), tickShown: await page.locator('#bigAskRow').isVisible(), block: (await text(page, 'buildMark')).split('\n').filter((l) => /^Larger model/.test(l))[0] };
      await shut(page);
      all('named', s1.eyes === 'insect' && r.named.overSheet < 0.05 && r.named.small === 'insect|no name|3' && r.named.after.common === 'monarch' && r.named.after.scientific === 'Danaus plexippus' && r.named.after.by === 'device-large' && r.named.lines.slice(-2).join(' / ') === 'Looking more closely… / The full database says monarch.'
        && r.named.line === 'The full database says monarch.' && r.named.record[0] === 'monarch|Danaus plexippus|device-large|insect' && (r.named.overlay === 'monarch' || r.named.overlay === '(gone)') && r.named.last.named === E('stripes.png').named && r.named.last.kind === E('stripes.png').kind
        && r.named.pill === 'monarch' && r.named.infoSub === 'Danaus plexippus'
        && r.named.offers.join() === E('stripes.png').five.map(sentence).join() && /^monarch \| Danaus plexippus .* named on this device by the full database · This creature’s view is yours for a week$/.test(r.named.rows[0]));
      all('aboutKept', r.aboutKept.state === 'You currently have the full database of species downloaded.' && !r.aboutKept.get && r.aboutKept.del && !r.aboutKept.tickShown && /^Larger model: standin-big, on this device, \d+ of \d+ MB; last photo insect 1\.00, Danaus plexippus [\d.]+, in [\d.]+ s/.test(r.aboutKept.block || ''));
      // another kind of creature, and it is sure: the change is offered in one line, and not made
      const s2 = await meet(page, 'dots.png'); await lineIs(page, /Change to this creature\?$/); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
      const b2 = await st(page);
      r.change = { atOnce: s2.eyes + '|' + s2.shown, line: await text(page, 'svcView'), before: b2.eyes + '|' + b2.named.common + '|' + b2.named.by, meetings: (await recordRows(page)).length };
      await page.screenshot({ path: path.join(here, 'shots', 'large-change.png'), scale: 'css' }).catch(() => {});
      await page.locator('#svcView').tap(); await page.waitForFunction(() => window.__seenBack.S.eyes === 'wader', null, { timeout: 6000 }); await page.waitForTimeout(300);
      const a2 = await st(page); r.change.after = a2.eyes + '|' + a2.named.common + '|' + a2.named.by; r.change.record = await recordRows(page); r.change.lineAfter = await svcLine(page);
      all('change', r.change.atOnce === 'frog|frog or toad' && r.change.line === 'It looks like a great egret, a wading bird. Change to this creature?' && r.change.before === 'frog|frog or toad|page'
        && r.change.after === 'wader|great egret|device-large' && r.change.record[0] === 'great egret|Ardea alba|device-large|wader' && r.change.record.length === r.change.meetings && r.change.lineAfter === '');
      // it is not sure: nothing changes; a person: it is not asked; a species the small model named: it has its say all the same
      let at = (await bigNow(page)).last.at;
      const s3 = await meet(page, 'small.png'); await largeAfter(page, at); await page.waitForTimeout(150); const a3 = await st(page);
      r.unsure = { state: a3.eyes + '|' + a3.named.common + '|' + a3.named.by, line: await svcLine(page), last: (await bigNow(page)).last, reference: E('small.png') };
      at = r.unsure.last.at; await meet(page, 'portrait.jpg'); await page.waitForTimeout(900); const a4 = await st(page); r.person = { eyes: a4.eyes, notice: a4.notice, asked: (await bigNow(page)).last.at !== at };
      if (a4.notice) { await page.locator('#noticeOk').tap(); await page.waitForTimeout(200); }
      const s5 = await meet(page, 'heron.png'); await byLarge(page); r.heron = { small: await page.evaluate(() => { const l = window.__seenBack.rec.about().last; return l.named && l.named.en; }), after: (await st(page)).named.common + '|' + (await st(page)).named.by };
      r.askedOfServers = { parts: (await partsAsked()).length, photos: (await ctl('log=1')).filter((x) => !/^test\/rec\/photos|^test\/assets/.test(x) && !/^index\.html/.test(x)) };
      all('unsure', r.unsure.state === s3.eyes + '|' + s3.shown + '|page' && r.unsure.line === '' && r.unsure.last.sure === false && r.unsure.last.kindOffers.join() === E('small.png').kindOffers.join());
      all('person', !r.person.eyes && r.person.notice === 'That’s a human. You already see the world as one. Try photographing another creature.' && !r.person.asked);   // a human: no view (build 22), and the larger model is not asked
      all('heron', r.heron.small === 'Great Blue Heron' && r.heron.after === 'great blue heron|device-large');
      // sure of the kind and unsure of the species (build 34): the species name the small model gave does not stand, and the kind's does.
      // The larger model's answer is set by hand here, since the stand-in is sure of the heron's species.
      await page.evaluate(() => { const b = window.__seenBack.big; b.__recognize = b.recognize; b.recognize = function () { return Promise.resolve({ kind: 'wader', kindP: 0.9, sure: true, kinds: [{ key: 'wader', p: 0.9 }], kindOffers: [], species: [{ sci: 'Ardea herodias', en: 'Great Blue Heron', p: 0.4, kind: 'wader' }, { sci: 'Ardea alba', en: 'Great Egret', p: 0.3, kind: 'wader' }], named: null, offers: [], local: true, kindAt: 0.5, ms: { load: 0, pre: 0, run: 0, post: 0 }, model: 'by hand', at: Date.now() }); }; });
      await meet(page, 'heron.png');
      const kindOnly = await page.waitForFunction(() => { const n = window.__seenBack.S.named; return !!n && n.by === 'device-large' && n.scientific === ''; }, null, { timeout: 20000 }).then(() => true, () => false);
      r.kindOnly = await page.evaluate(() => { const b = window.__seenBack, S = b.S, l = b.rec.about().last; b.big.recognize = b.big.__recognize; delete b.big.__recognize; return { eyes: S.eyes, common: S.named && S.named.common, sci: S.named && S.named.scientific, by: S.named && S.named.by, want: b.EYES.wader.who.replace(/^an? /, ''), small: l.named && l.named.en }; });
      all('kindOnly', kindOnly && r.kindOnly.small === 'Great Blue Heron' && r.kindOnly.eyes === 'wader' && r.kindOnly.common === r.kindOnly.want && r.kindOnly.sci === '' && r.kindOnly.by === 'device-large');
      all('nothingAsked', r.askedOfServers.parts === 0 && r.askedOfServers.photos.length === 0);
      // a minute with nothing to do (shortened here): its worker is let go, and the next photo starts it again
      await page.evaluate(() => window.__seenBack.big.test.idle(300)); await page.waitForFunction(() => !window.__seenBack.big.test.running(), null, { timeout: 8000 });
      r.rest = { state: (await bigNow(page)).state }; await meet(page, 'stripes.png'); await byLarge(page); r.rest.after = (await st(page)).named.common; r.rest.started = (await bigNow(page)).last.ms.load > 0;
      await page.evaluate(() => window.__seenBack.big.test.idle(60000));
      all('rest', r.rest.state === 'idle' && r.rest.after === 'monarch' && r.rest.started);
      // from the sheet that asks for a name: the small model found nothing alive; the larger one is asked, is not sure, and offers its three likeliest kinds
      const s6 = await meet(page, 'wall.png');
      r.fromSheet = { first: s6.notice };
      await page.waitForFunction(() => /not sure what kind of creature/.test(document.getElementById('claimSub').textContent) && !document.getElementById('claim').hidden, null, { timeout: 20000 }); await page.waitForTimeout(300);
      r.fromSheet.after = await page.evaluate(() => ({ sub: document.getElementById('claimSub').textContent, kinds: [...document.querySelectorAll('#claimKinds button')].map((b) => b.textContent), link: !document.getElementById('claimAskRow').hidden, eyes: window.__seenBack.S.eyes }));
      r.fromSheet.reference = E('wall.png'); await page.locator('#claimKinds button').first().tap(); await page.waitForTimeout(300); const a6 = await st(page); r.fromSheet.chosen = a6.eyes + '|' + a6.named.by;
      all('fromSheet', !r.fromSheet.first
        && r.fromSheet.after.sub === 'We’re not sure what kind of creature that is.' && r.fromSheet.after.kinds.length === 3 && !r.fromSheet.after.link && !r.fromSheet.after.eyes
        && r.fromSheet.chosen === E('wall.png').kindOffers[0] + '|you');
      await page.close();
      // the small model is not sure, and the larger one is on the device: it is asked before the person is, and its answer is taken
      ({ page, errors } = await open(browser, '&nosw=1&rec=' + SLOT + '/manifest.kind-at.json&big=' + slot, null, ctx)); await ready(page); await begin(page);
      await page.evaluate(() => { const el = document.getElementById('msg'); window.__lines = []; new MutationObserver(() => { const t = el.textContent; if (t && window.__lines[window.__lines.length - 1] !== t) window.__lines.push(t); }).observe(el, { childList: true, characterData: true, subtree: true }); });
      const s7 = await meet(page, 'odd.png'); r.first = { state: s7.eyes + '|' + s7.shown + '|' + (s7.named && s7.named.by), claim: s7.claim, lines: await page.evaluate(() => window.__lines.filter((x, i, a) => a.indexOf(x) === i)), small: await page.evaluate(() => window.__seenBack.rec.about().last.sure), record: (await recordRows(page))[0], errors };
      all('first', r.first.state === 'bee|western honey bee|device-large' && !r.first.claim && r.first.lines.indexOf('Looking more closely…') >= 0 && r.first.small === false && r.first.record === 'western honey bee|Apis mellifera|device-large|bee' && !errors.length);
      // deleted from the device, with a second thought first; after that it is not offered
      await toAbout(page); await page.waitForSelector('#bigDel', { state: 'visible', timeout: 5000 }); await page.locator('#bigDel').tap(); await page.waitForTimeout(250);
      r.del = { asks: await text(page, 'bigState'), keep: await page.locator('#bigDelNo').isVisible(), keptWhileAsking: (await keptBig(page)).length };
      await page.screenshot({ path: path.join(here, 'shots', 'large-delete.png'), scale: 'css' }).catch(() => {});
      await page.locator('#bigDelNo').tap(); await page.waitForTimeout(200); r.del.keptAfterKeep = (await bigNow(page)).have; await page.locator('#bigDel').tap(); await page.waitForTimeout(150); await page.locator('#bigDel').tap();
      await bigHave(page, 'absent', 15000); await page.waitForTimeout(300);
      r.del.after = { kept: await keptBig(page), state: await text(page, 'bigState'), choice: (await bigNow(page)).choice, running: (await bigNow(page)).running, ticked: await page.locator('#bigAsk').isChecked() };
      await shut(page); const s8 = await meet(page, 'heron.png'); await page.waitForTimeout(700); r.del.next = { by: (await st(page)).named.by, line: await svcLine(page), parts: (await partsAsked()).length };
      all('delete', r.del.asks === 'Delete the full database? It is ' + MB + ' MB, and would have to be downloaded again.' && r.del.keep && r.del.keptWhileAsking >= 4 && r.del.keptAfterKeep === 'kept'
        && r.del.after.kept.length === 0 && /^The full database of species is free to download/.test(r.del.after.state) && r.del.after.choice === 'no' && !r.del.after.running && r.del.after.ticked && r.del.next.by === 'page' && r.del.next.line === '' && r.del.next.parts === 0);
      await ctx.close();
    }
    { // stopped mid-way: what arrived is kept, the line says where it stands, and "Get the rest" carries on without fetching a kept part again
      await ctl('reset=1'); await bctl('reset=1'); await bctl('slow=' + encodeURIComponent('part01') + '&bps=30000');
      const { ctx, page, errors } = await open(browser, Q); await ready(page); await begin(page); const d = r.device;
      await meet(page, 'stripes.png'); await offered(page); await getIt(page);
      await page.waitForFunction(() => window.__seenBack.big.about().keptBytes > 300000, null, { timeout: 20000 });
      await lineIs(page, /^Downloading the full database/); await page.locator('#svcView').tap(); await page.waitForSelector('#big', { state: 'visible' }); await page.waitForTimeout(150);
      r.stop = { title: await text(page, 'bigTitle'), stop: await page.locator('#bigStop').isVisible() && (await text(page, 'bigStop')), yesShown: await page.locator('#bigYes').isVisible(), net: await text(page, 'bigNet') };
      await page.locator('#bigStop').tap(); await bigHave(page, 'partial', 10000); await page.waitForTimeout(200);
      const x = await bigNow(page); r.stop.after = { have: x.have, choice: x.choice, line: await svcLine(page), kept: (await keptBig(page)).filter((k) => /^part/.test(k)).length };
      await meet(page, 'stripes.png'); r.stop.offer = await offered(page); await page.locator('#svcView').tap(); await page.waitForSelector('#big', { state: 'visible' }); await page.waitForTimeout(150);
      r.stop.sheet = { title: await text(page, 'bigTitle'), yes: await text(page, 'bigYes'), net: (await text(page, 'bigNet')).trim() };
      await bctl('reset=1'); await page.locator('#bigYes').tap(); await bigHave(page, 'kept', 30000); await byLarge(page);
      r.stop.rest = { parts: await partsAsked(), named: (await st(page)).named.common, errors };
      all('stop', r.stop.title === 'Getting the full database' && r.stop.stop === 'Stop the download' && !r.stop.yesShown && /^Downloading the full database… \d+ of \d+ MB$/.test(r.stop.net)
        && x.have === 'partial' && x.choice === '' && /^The download has been stopped\./.test(r.stop.after.line) && r.stop.after.kept === 1
        && /^The full database is partly downloaded: \d+ of \d+ MB\. Get the rest\?$/.test(r.stop.offer) && r.stop.sheet.title === 'Get the rest of the full database?' && r.stop.sheet.yes === 'Get the rest' && /^\d+ of \d+ MB have been downloaded\.$/.test(r.stop.sheet.net)
        && r.stop.rest.parts.join() === 'part01,part02' && r.stop.rest.named === 'monarch' && !errors.length);
      // a larger slot may carry a kinds head too (the same parts, kept already): it names as before, and it can say that nothing alive is there
      if (BIG_PORT === 8788) {
        await page.close(); const k = await open(browser, '&nosw=1&rec=' + SLOT + '&big=' + BIG + '/manifest.kinds.json', null, ctx); await ready(k.page); await begin(k.page); await bctl('reset=1');
        const h = await meet(k.page, 'heron.png'); await byLarge(k.page); const kb = await bigNow(k.page);
        r.kindsHead = { model: await k.page.evaluate(() => window.__seenBack.big.about().model), heron: (await st(k.page)).named.common + '|' + (await st(k.page)).named.by, parts: (await partsAsked()).length, reference: expect.big_kinds['heron.png'][month].named };
        await meet(k.page, 'wall.png');
        await k.page.waitForFunction((t) => { const l = window.__seenBack.big.about().last; return !!l && l.at > t && !document.getElementById('notice').hidden; }, kb.last.at, { timeout: 20000 }); await k.page.waitForTimeout(300);
        r.kindsHead.wall = await k.page.evaluate(() => ({ sub: document.getElementById('noticeText').textContent, kinds: document.querySelectorAll('#claimKinds button').length, link: !document.getElementById('claimAskRow').hidden, last: window.__seenBack.big.about().last.kind, eyes: window.__seenBack.S.eyes }));
        r.kindsHead.errors = k.errors;
        all('kindsHead', r.kindsHead.model === 'standin-big-kinds' && r.kindsHead.heron === 'great blue heron|device-large' && r.kindsHead.parts === 0 && r.kindsHead.wall.last === 'none' && !r.kindsHead.wall.eyes
          && r.kindsHead.wall.sub === 'We can’t find a creature in your photo. Try again.' && r.kindsHead.wall.kinds === 0 && !r.kindsHead.wall.link && !k.errors.length);
      }
      await ctx.close();
    }
    // failures, each in words on the line, with a way on where there is one; what the small model said stands throughout
    r.failures = {};
    for (const [name, rule, wanted, keptWanted] of [['missingPart', 'lose=' + encodeURIComponent('part01'), 'The full database’s files are missing. Try again?', 1], ['damagedPart', 'damage=' + encodeURIComponent('part02'), 'The full database’s download is damaged. Try again?', 2], ['noNetwork', 'drop=' + encodeURIComponent('part'), 'The full database’s download was interrupted. Try again?', 0]]) {
      await ctl('reset=1'); await bctl('reset=1'); await bctl(rule);
      const { ctx, page, errors } = await open(browser, Q); await ready(page); await begin(page);
      await meet(page, 'stripes.png'); await offered(page); await getIt(page); await lineIs(page, /Try again\?$/, 30000);
      const b = await bigNow(page), x = { line: await svcLine(page), have: b.have, why: b.getFail, kept: (await keptBig(page)).filter((k) => /^part/.test(k)).length, state: (await st(page)).eyes + '|' + (await st(page)).named.by, claim: (await st(page)).claim };
      await bctl('reset=1'); await page.locator('#svcView').tap(); await bigHave(page, 'kept', 30000); await byLarge(page);      // put right: a tap on the line carries on from what is kept
      x.partsAfter = (await partsAsked()).join(); x.named = (await st(page)).named.common; r.failures[name] = x;
      all(name, x.line === wanted && x.have === (keptWanted ? 'partial' : 'absent') && x.kept === keptWanted && x.state === 'insect|page' && !x.claim && x.partsAfter === ['part00', 'part01', 'part02'].slice(keptWanted).join() && x.named === 'monarch' && !quiet(errors).length);
      await ctx.close();
    }
    { // every part passes its own checksum and the whole does not: nothing of it is kept
      await ctl('reset=1'); await bctl('reset=1'); const { ctx, page } = await open(browser, '&nosw=1&rec=' + SLOT + '&big=' + slot.replace(/\/manifest\.port\.json$/, '') + (BIG_PORT === 8788 ? '/manifest.bad-whole.json' : '/manifest.port.bad-whole.json')); await ready(page); await begin(page);
      await meet(page, 'stripes.png'); await offered(page); await getIt(page); await lineIs(page, /download is damaged/, 30000); const b = await bigNow(page);
      r.failures.badWhole = { line: await svcLine(page), have: b.have, why: b.getFail, kept: (await keptBig(page)).filter((k) => /^part|^whole/.test(k)).length, by: (await st(page)).named.by };
      all('badWhole', r.failures.badWhole.line === 'The full database’s download is damaged. Try again?' && b.have === 'absent' && /sha256/.test(b.getFail) && r.failures.badWhole.kept === 0 && r.failures.badWhole.by === 'page'); await ctx.close();
    }
    { // the browser says there is no room: nothing is fetched, and there is nothing to try again
      await ctl('reset=1'); await bctl('reset=1'); const { ctx, page } = await open(browser, Q); await ready(page); await begin(page);
      await page.evaluate(() => { navigator.storage.estimate = () => Promise.resolve({ quota: 1000, usage: 900 }); });
      await meet(page, 'stripes.png'); await offered(page); await getIt(page); await lineIs(page, /not enough storage/, 15000); const b = await bigNow(page);
      r.failures.noRoom = { line: await svcLine(page), tappable: await page.evaluate(() => !document.getElementById('svcView').disabled), have: b.have, choice: b.choice, parts: (await partsAsked()).length };
      all('noRoom', r.failures.noRoom.line === 'There is not enough storage on this device for the full database.' && !r.failures.noRoom.tappable && b.have === 'absent' && b.choice === '' && r.failures.noRoom.parts === 0); await ctx.close();
    }
    { // where there is a server too, the device comes first; "Do not ask again" for the device leaves the server to be offered
      await ctl('reset=1'); await bctl('reset=1'); const Qs = (await svcFiles()) + 'service.json&big=' + slot; const { ctx, page } = await open(browser, Qs); await ready(page); await begin(page);
      await meet(page, 'stripes.png'); r.both = { first: await offered(page), sent: fake.calls().length };
      await page.locator('#svcView').tap(); await page.waitForSelector('#big', { state: 'visible' }); await page.evaluate(() => document.getElementById('bigNever').click()); await page.waitForTimeout(200);
      await meet(page, 'stripes.png'); r.both.then = await offered(page); r.both.sentAfter = fake.calls().length;
      all('both', r.both.first === 'Download the full database of species?' && r.both.then === 'The full database on a server can try to name the species. Ask it?' && r.both.sent === 0 && r.both.sentAfter === 0); await ctx.close();
    }
    await worldBlock(r, all);
    await bctl('reset=1'); await ctl('reset=1');
    done('large', r, ok);
  });

  if (want.includes('world')) await section('world', async () => {    // the world block of the large section, alone
    await bigUp(); const r = {}; let ok = true; sofar = r; const all = (name, cond) => { if (!cond) { ok = false; (r.failed = r.failed || []).push(name); } };
    await worldBlock(r, all); await bctl('reset=1'); await ctl('reset=1'); done('world', r, ok);
  });

  if (want.includes('keptcopy')) await section('keptcopy', async () => {   // the manifest's kept copy is found where a plain lookup would miss it, and used where the network neither answers nor fails
    await ctl('reset=1'); const r = {};
    { const { ctx, page, errors } = await open(browser, '&nosw=1&rec=' + SLOT); await ready(page);
      // the kept manifest is put back as a host that varies by a header leaves it: a plain lookup by its address no longer finds it
      r.plainLookupFinds = await page.evaluate(async () => { const c = await caches.open('keep-v1'), k = (await c.keys()).filter((q) => /standin\/manifest\.json$/.test(q.url))[0], t = await (await c.match(k)).text();
        await c.delete(k); await c.put(new Request(k.url, { headers: { 'X-Seen': 'one' } }), new Response(t, { headers: { 'Content-Type': 'application/json', 'Vary': 'X-Seen' } })); return !!(await c.match(k.url)); });
      await page.evaluate(() => window.__seenBack.rec.test.forget()); await ctl('drop=' + encodeURIComponent('standin'));     // no network for the slot's files (the worker's own script is the service worker's to keep, and there is none here)
      r.withVary = await page.evaluate(() => window.__seenBack.rec.ready().then(() => 'ready', (e) => e.code + ': ' + e.detail));
      await begin(page); r.heron = (await meet(page, 'heron.png')).shown;
      // a network that neither answers nor fails: after the wait (six seconds, shortened here) the kept copy is used
      await ctl('reset=1'); await ctl('hang=' + encodeURIComponent('standin/manifest'));
      r.hanging = await page.evaluate(() => { const rec = window.__seenBack.rec, t0 = performance.now(); rec.test.forget(); rec.test.netWait(700); return rec.ready().then(() => 'ready in ' + (performance.now() - t0 < 6000 ? 'under six seconds' : 'six seconds or more'), (e) => e.code + ': ' + e.detail); });
      r.errors = quiet(errors); await ctx.close(); }
    { await ctl('reset=1'); await ctl('drop=' + encodeURIComponent('standin|vendor'));     // and where there is no kept copy at all, the reason says so
      const { ctx, page } = await open(browser, '&nosw=1&rec=' + SLOT); await begin(page); r.none = (await meet(page, 'heron.png')).sub; r.noneWhy = (await about(page)).fail; await ctl('reset=1'); await ctx.close(); }
    done('keptcopy', r, r.plainLookupFinds === false && r.withVary === 'ready' && r.heron === 'great blue heron' && r.hanging === 'ready in under six seconds' && !r.errors.length
      && /^This app’s download is incomplete\./.test(r.none) && /^network: .*manifest\.json; no kept copy found$/.test(r.noneWhy));
    await ctl('reset=1');
  });

  if (want.includes('away')) await section('away', async () => {     // the species list is one town's: the sheet says so, and a switch turns local naming off. No location is asked of the device
    const Q = await svcFiles(), r = {};
    const ctx = await browser.newContext(Object.assign({}, phone));
    await ctx.addInitScript(() => { window.__geo = 0; try { const g = navigator.geolocation; if (g) { g.getCurrentPosition = () => { window.__geo++; }; g.watchPosition = () => { window.__geo++; return 0; }; } } catch (e) {} });
    let { page, errors } = await open(browser, Q + 'service.json', null, ctx); await ready(page);
    await page.evaluate(() => window.__seenBack.svc.setChoice('yes')); await begin(page);
    const info = async () => { await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); await page.locator('#inViewPick').setInputFiles(path.join(here, '..', 'assets', 'portrait.jpg'));
      await page.waitForFunction(() => window.__seenBack.S.screen === 'animal', null, { timeout: 12000 }); await page.locator('#btnWho').tap(); await page.waitForSelector('#info', { state: 'visible' }); const t = await text(page, 'infoSub');
      await page.locator('#infoClose').tap(); await page.evaluate(() => history.back()); await page.waitForTimeout(200); await page.evaluate(() => history.back()); await page.waitForTimeout(200); return t; };
    const about = async () => { await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' }); await aboutOpen(page); };
    r.near = { heron: (await meet(page, 'heron.png')).shown }; r.near.info = await info();
    await about(); r.switch = { label: (await page.locator('#awayRow .tick').textContent()).trim(), note: await text(page, 'awayNote'), tickedAtFirst: await page.locator('#awayBox').isChecked() };
    await page.evaluate(() => { document.getElementById('record').scrollTop = 99999; }); await page.waitForTimeout(150); await page.screenshot({ path: path.join(here, 'shots', 'away.png'), scale: 'css' }).catch(() => {});
    await page.evaluate(() => { const b = document.getElementById('awayBox'); b.checked = true; b.dispatchEvent(new Event('change', { bubbles: true })); }); await shut(page);
    // elsewhere: the device names the kind and no species, and the full database is asked without a region
    fake.reset(); fake.set({ answer: 'egret', delay: 900 });     // long enough for the kind alone to be read off the screen first: a finer name now replaces it there as soon as it comes
    const h = await meet(page, 'heron.png'); r.away = { atOnce: h.eyes + '|' + h.shown, top: h.last && h.last.top }; await byService(page);
    r.away.sent = fake.calls().map((c) => JSON.stringify(c.region) + ' month ' + c.month); r.away.named = (await st(page)).named.common + '|' + (await st(page)).named.by; r.away.info = await info();
    await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' }); r.away.rows = await page.evaluate(() => [...document.querySelectorAll('#metList li')].slice(0, 1).map((li) => li.querySelector('.nm').textContent + ' | ' + li.querySelector('.sm').textContent)); await shut(page);
    // the choice is kept across a reload, and can be undone
    await page.reload(); await page.waitForTimeout(400); await ready(page);
    r.afterReload = await page.evaluate(() => window.__seenBack.rec.local); await begin(page);
    await about(); r.tickedAfterReload = await page.locator('#awayBox').isChecked(); await page.evaluate(() => { const b = document.getElementById('awayBox'); b.checked = false; b.dispatchEvent(new Event('change', { bubbles: true })); }); await shut(page);
    fake.reset(); r.nearAgain = (await meet(page, 'heron.png')).shown; r.nearAgainPosts = fake.calls().length;
    r.locationAsked = await page.evaluate(() => window.__geo); r.errors = errors;
    done('away', r, r.near.heron === 'great blue heron' && r.near.info === 'Ardea herodias'
      && r.switch.label === 'I am not near Gainesville' && /^Species are named from a list of those recorded around Gainesville, Florida\./.test(r.switch.note) && !r.switch.tickedAtFirst
      && r.away.atOnce === 'wader|wading bird' && r.away.top === null && r.away.sent.join() === '"" month ' + (new Date().getMonth() + 1) && r.away.named === 'great egret|service'
      && r.away.info === 'Ardea alba' && /named by the full database on a server · This creature’s view is yours for a week$/.test(r.away.rows[0])
      && r.afterReload === false && r.tickedAfterReload && r.nearAgain === 'great blue heron' && r.nearAgainPosts === 0 && r.locationAsked === 0 && !errors.length);
    await ctx.close();
  });

  if (want.includes('zone')) await section('zone', async () => {     // the phone's time zone says whether the county's list applies (build 22); a choice the person made stands
    const r = {}, Q = '&rec=' + SLOT;
    const tryZone = async (zone, said) => {
      const ctx = await browser.newContext(Object.assign({}, phone, { timezoneId: zone }));
      if (said) await ctx.addInitScript((v) => { try { localStorage.setItem('seenback.away.v1', v); } catch (e) {} }, said);
      const { page, errors } = await open(browser, Q, null, ctx); await ready(page);
      const local = await page.evaluate(() => window.__seenBack.rec.local); await begin(page);
      const h = await meet(page, 'heron.png'); const out = { local, shown: h.shown, eyes: h.eyes, errors: errors.length };
      await ctx.close(); return out;
    };
    r.paris = await tryZone('Europe/Paris'); r.chicago = await tryZone('America/Chicago'); r.newYork = await tryZone('America/New_York');
    r.parisSaidNear = await tryZone('Europe/Paris', '0'); r.newYorkSaidAway = await tryZone('America/New_York', '1');
    done('zone', r, r.paris.local === false && r.paris.eyes === 'wader' && r.paris.shown === 'wading bird' && r.chicago.local === false
      && r.newYork.local === true && r.newYork.shown === 'great blue heron' && r.parisSaidNear.local === true && r.parisSaidNear.shown === 'great blue heron'
      && r.newYorkSaidAway.local === false && r.newYorkSaidAway.shown === 'wading bird'
      && [r.paris, r.chicago, r.newYork, r.parisSaidNear, r.newYorkSaidAway].every((x) => x.errors === 0));
  });

  if (want.includes('offline') || want.includes('version')) await section('offline', async () => {   // a second visit with the network off; then a new version is noticed, fetched, and the old one let go
    await ctl('reset=1');
    const ctx = await browser.newContext(Object.assign({}, phone));
    let { page, errors } = await open(browser, '&rec=' + SLOT, null, ctx);
    const r = {}; await ready(page);
    await page.waitForFunction(() => navigator.serviceWorker && navigator.serviceWorker.controller, null, { timeout: 15000 });
    r.first = { loadMs: (await about(page)).loadMs };
    await begin(page); r.first.heron = (await meet(page, 'heron.png')).shown;
    await page.waitForTimeout(800);
    r.kept = await page.evaluate(async () => (await (await caches.open('keep-v1')).keys()).map((q) => q.url.replace(location.origin + '/', '')).sort());
    const log1 = await ctl('log=1'); r.fetchedFirst = log1.filter((x) => /onnx|\.wasm|f16|species\.json|rec-worker|ort\./.test(x));
    await ctl('reset=1'); await ctl('down=1');     // the server drops every request too: the offline switch below does not reach the service worker's own requests
    await page.close();
    await ctx.setOffline(true);
    ({ page, errors } = await open(browser, '&rec=' + SLOT, null, ctx));
    await ready(page); r.offline = { loadMs: (await about(page)).loadMs, online: await page.evaluate(() => navigator.onLine) };
    await begin(page); const h = await meet(page, 'heron.png'); r.offline.heron = h.shown; r.offline.ms = h.last && h.last.ms;
    r.offline.stripes = (await meet(page, 'stripes.png')).eyes;
    r.offline.requestsDropped = (await ctl('log=1')).map((x) => x.split('?')[0]).filter((x, i, a) => a.indexOf(x) === i); r.offline.errors = errors;
    await page.locator('#backAskView').tap(); await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' }); await page.waitForTimeout(250);
    r.offline.aboutLine = (await text(page, 'buildMark')).split('\n')[1];
    r.first.errors = []; let ok = r.first.heron === 'great blue heron' && r.offline.online === false && r.offline.heron === 'great blue heron' && r.offline.stripes === 'insect' && /^Recognizer: standin-random-conv, wasm/.test(r.offline.aboutLine)
      && r.fetchedFirst.filter((x) => /vision\.int8\.onnx/.test(x)).length === 1 && r.fetchedFirst.filter((x) => /\.wasm\?/.test(x)).length === 1 && !errors.length;
    await page.close(); await ctx.setOffline(false); await ctl('reset=1');
    if (want.includes('version')) {
      // online again with nothing changed: the manifest is asked for, the model is not
      await ctl('reset=1');
      ({ page, errors } = await open(browser, '&rec=' + SLOT, null, ctx)); await ready(page);
      r.again = { asked: (await ctl('log=1')).filter((x) => !/^index\.html/.test(x) && /standin|vendor/.test(x)), errors: errors.slice() }; ok = ok && !errors.length;
      // a phone that kept build 8's files holds the encoder under the manifest's fingerprint as well: a copy under such an address must be let go
      r.again.encoderKey = await page.evaluate(async () => { const c = await caches.open('keep-v1'), k = (await c.keys()).map((q) => q.url).filter((u) => /vision\.int8\.onnx\?v=/.test(u));
        if (k.length === 1) await c.put(k[0].replace(/v=[^&]+/, 'v=0123abcd'), await c.match(k[0])); return k.map((u) => u.replace(location.origin + '/', '')); });
      await page.close();
      // the laboratory publishes a new model under the same address: another manifest, so another version
      await ctl('reset=1'); await ctl('swap=' + SLOT + '/manifest.json&with=' + SLOT + '/manifest.kinds-only.json');
      ({ page, errors } = await open(browser, '&rec=' + SLOT, null, ctx)); await ready(page); await page.waitForTimeout(600);
      r.newVersion = { model: (await about(page)).model, asked: (await ctl('log=1')).filter((x) => !/^index\.html/.test(x) && /standin/.test(x)),
        kept: await page.evaluate(async () => (await (await caches.open('keep-v1')).keys()).map((q) => q.url.replace(location.origin + '/', '')).filter((u) => /standin/.test(u)).sort()), errors: errors.slice() };
      const vs = new Set(r.newVersion.kept.map((u) => (/v=([0-9a-f]+)/.exec(u) || [])[1]).filter(Boolean));
      // the new manifest names the same encoder (the same sha256): it is not fetched again, and stays kept under its checksum; the old copy is gone
      const sha = JSON.parse(fs.readFileSync(path.join(slotDir, 'manifest.kinds-only.json'), 'utf8')).vision.sha256;
      ok = ok && r.again.asked.length === 1 && /manifest\.json$/.test(r.again.asked[0]) && r.again.encoderKey.length === 1 && r.again.encoderKey[0].endsWith('vision.int8.onnx?v=sha256-' + sha) && r.newVersion.model === 'standin-kinds-only'
        && !r.newVersion.asked.some((x) => /vision\.int8\.onnx/.test(x)) && vs.size === 1 && r.newVersion.kept.filter((u) => /vision\.int8\.onnx/.test(u)).join() === r.again.encoderKey[0] && !errors.length;
      await page.close(); await ctl('reset=1');
    }
    done(want.includes('version') ? 'offline+version' : 'offline', r, ok);
    await ctx.close();
  });

  if (want.includes('missing')) await section('missing', async () => {  // no recognizer at all; a model file that is not there; no network on a first visit
    const r = {};
    { const { ctx, page } = await open(browser, '&nosw=1&rec=test/rec/nowhere'); await begin(page); r.noSlot = (await meet(page, 'heron.png')); await ctx.close(); }
    { await ctl('reset=1'); await ctl('lose=' + encodeURIComponent('vision\\.int8\\.onnx'));
      const { ctx, page } = await open(browser, '&nosw=1&rec=' + SLOT); await begin(page); r.noModel = (await meet(page, 'heron.png'));
      // and when the file is back, the next photo is recognized without reloading the page
      await ctl('reset=1'); await page.locator('#claimBack').tap(); r.recovered = (await meet(page, 'heron.png')).shown; await ctx.close(); }
    { await ctl('reset=1'); await ctl('drop=' + encodeURIComponent('standin|vendor'));     // the page arrives, and then the network is gone for everything the recognizer needs
      const { ctx, page } = await open(browser, '&nosw=1&rec=' + SLOT); await begin(page); r.offlineFirst = await meet(page, 'heron.png'); await ctl('reset=1'); await ctx.close(); }
    { const { ctx, page } = await open(browser, '&nosw=1&rec=off'); await begin(page); r.off = (await meet(page, 'heron.png')); await ctx.close(); }
    const tail = ' Tell us what’s there.';
    done('missing', r, r.noSlot.claim && r.noSlot.sub === 'This app can’t ID photos yet.' + tail && r.noModel.claim && r.noModel.sub === 'Some of this app’s files are missing. Close the app and open it again.' + tail && r.recovered === 'great blue heron'
      && r.offlineFirst.claim && r.offlineFirst.sub === 'This app’s download is incomplete. Check your connection, then close the app and open it again.' + tail && r.off.claim && r.off.sub === 'IDing is turned off.' + tail);
  });

  if (want.includes('damaged')) await section('damaged', async () => {  // the model's bytes changed on the way; the model cut short; a kept copy that is not a model
    const r = {};
    { await ctl('reset=1'); await ctl('damage=' + encodeURIComponent('vision\\.int8\\.onnx'));
      const { ctx, page } = await open(browser, '&nosw=1&rec=' + SLOT); await begin(page); r.changed = (await meet(page, 'heron.png')); r.changedWhy = (await about(page)).fail;
      r.keptAfter = await page.evaluate(async () => (await (await caches.open('keep-v1')).keys()).filter((q) => /onnx/.test(q.url)).length); await ctx.close(); }
    { await ctl('reset=1'); await ctl('cut=' + encodeURIComponent('vision\\.int8\\.onnx'));
      const { ctx, page } = await open(browser, '&nosw=1&rec=' + SLOT); await begin(page); r.cut = (await meet(page, 'heron.png')); r.cutWhy = (await about(page)).fail; await ctx.close(); }
    { await ctl('reset=1');       // a manifest with no checksum, and a file of the right length that is not a model: the encoder refuses it
      const { ctx, page } = await open(browser, '&nosw=1&rec=' + SLOT); await ready(page);
      await page.evaluate(async () => {
        const c = await caches.open('keep-v1'), keys = await c.keys(), k = keys.filter((q) => /onnx/.test(q.url))[0], n = (await (await c.match(k)).arrayBuffer()).byteLength;
        await c.put(k, new Response(new Uint8Array(n).fill(7)));
      });
      await page.reload();     // the page tries the kept copy by itself once it is idle, finds it is no model, and throws it away; the next photo fetches a good one
      await page.waitForFunction(() => window.__seenBack.rec.about().state === 'failed', null, { timeout: 20000 }); r.keptBadWhy = (await about(page)).fail;
      await begin(page); r.keptBadThenFetchedAgain = (await meet(page, 'heron.png')).shown; await ctx.close(); }
    const tail = ' Tell us what’s there.', sub = 'This app’s download is damaged. Close the app and open it again.' + tail;
    done('damaged', r, r.changed.claim && r.changed.sub === sub && /sha256/.test(r.changedWhy) && r.keptAfter === 0 && r.cut.claim && r.cut.sub === sub && /^damaged: session/.test(r.keptBadWhy) && r.keptBadThenFetchedAgain === 'great blue heron');
    await ctl('reset=1');
  });

  if (want.includes('dying')) await section('dying', async () => {    // the worker throws while a photo is with it; the worker never answers; the next photo starts it again
    const { ctx, page, errors } = await open(browser, '&nosw=1&rec=' + SLOT); const r = {}; await ready(page); await begin(page);
    r.before = (await meet(page, 'heron.png')).shown; await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
    await page.evaluate(() => window.__seenBack.rec.test.kill('throw'));
    r.thrown = await meet(page, 'heron.png'); r.thrownWhy = (await about(page)).fail;
    await page.locator('#claimBack').tap();
    r.afterThrow = (await meet(page, 'heron.png')).shown; await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
    await page.evaluate(() => { window.__seenBack.rec.test.watch(1500); window.__seenBack.rec.test.kill('hang'); });
    r.hung = await meet(page, 'heron.png');
    await page.locator('#claimBack').tap(); await page.evaluate(() => window.__seenBack.rec.test.watch(45000));
    r.afterHang = (await meet(page, 'stripes.png')).eyes;
    r.pictureStillDrawn = await page.evaluate(() => window.__seenBack.state().err === 0);
    const tail = ' Tell us what’s there.';
    done('dying', r, r.before === 'great blue heron' && r.thrown.claim && r.thrown.sub === 'This app’s IDing has crashed. Check that your device has enough memory.' + tail && r.afterThrow === 'great blue heron'
      && r.hung.claim && r.hung.sub === 'The IDing timed out. Try again.' + tail && r.afterHang === 'insect' && r.pictureStillDrawn);
    await ctx.close();
  });

  if (want.includes('about')) await section('about', async () => {    // the block to copy from a real phone
    const { ctx, page, errors } = await open(browser, '&nosw=1&rec=' + SLOT, isChromium ? { permissions: ['clipboard-read', 'clipboard-write'] } : {}); const r = {}; await ready(page);
    await begin(page); await meet(page, 'heron.png'); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
    await page.locator('#backAskView').tap(); await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' });
    await aboutOpen(page); await page.locator('#fittedOn').tap(); await page.waitForSelector('#buildBox', { state: 'visible' });
    r.block = (await text(page, 'buildMark')).split('\n');
    await page.locator('#aboutCopy').tap(); await page.waitForTimeout(300);
    r.note = await text(page, 'aboutNote'); r.clip = isChromium ? (await page.evaluate(() => navigator.clipboard.readText())).split('\n').length : r.block.length;   // reading the clipboard back is allowed to a check only in Chromium
    await page.evaluate(() => { document.getElementById('record').scrollTop = 99999; }); await page.waitForTimeout(150);
    fs.mkdirSync(path.join(here, 'shots'), { recursive: true }); await page.screenshot({ path: path.join(here, 'shots', 'about.png'), scale: 'css' });
    r.overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth); r.errors = errors;
    r.fitted = { none: await text(page, 'fittedOn') };      // the stand-in's manifest has no fitted_on block: no sentence
    for (const [name, m] of [['full', 'manifest.fitted.json'], ['bare', 'manifest.fitted-bare.json']]) {    // a block with its sentence and count; a block with neither (a count that is not a number)
      const o = await open(browser, '&nosw=1&rec=' + SLOT + '/' + m); await ready(o.page); await o.page.locator('#btnBegin').tap(); await o.page.waitForSelector('#askAnimal', { state: 'visible', timeout: 8000 });
      await o.page.locator('#recAskAnimal').tap(); await o.page.waitForSelector('#record', { state: 'visible' }); await aboutOpen(o.page);
      r.fitted[name] = (await o.page.locator('#fittedOn').isVisible()) ? await text(o.page, 'fittedOn') : '(hidden)'; r.fitted[name + 'Errors'] = o.errors;
      if (name === 'full') { await o.page.evaluate(() => { document.getElementById('record').scrollTop = 99999; }); await o.page.waitForTimeout(150); await o.page.screenshot({ path: path.join(here, 'shots', 'about-fitted.png'), scale: 'css' }).catch(() => {}); }
      await o.ctx.close();
    }
    const base = 'Regards identifies species by comparing with iNaturalist and Flickr photos made available under Creative Commons licenses or in the public domain.';
    done('about', r, /^v1\.\d+$/.test(r.fitted.none) && r.fitted.full === r.fitted.none + base
      && r.fitted.bare === r.fitted.none + base && !r.fitted.fullErrors.length && !r.fitted.bareErrors.length && /^Regards, build \d+\.$/.test(r.block[0]) && /^Recognizer: standin-random-conv, wasm, 1 thread, ready in [\d.]+ s\.$/.test(r.block[1]) && /^Last photo: wader 1\.00, Ardea herodias 1\.00; .*prepared in \d+ ms from 900x1200, recognized in \d+ ms\.$/.test(r.block[2])
      && /^Picture: \d+ by \d+.* limit 420, [\d.]+ ms a frame over the last \d+\.$/.test(r.block[3]) && (!/^Engine: /.test(r.block[4]) || /^Engine: [\d.]+ ms of script a frame, /.test(r.block[4])) && /^Screen: /.test(r.block[/^Engine: /.test(r.block[4]) ? 5 : 4]) && (r.note === 'Copied.' || !isChromium) && r.clip === r.block.length && r.overflow <= 0 && !errors.length);
    await ctx.close();
  });

  if (want.includes('viewer')) await section('viewer', async () => {   // inside Claude's viewer nothing of this starts: no worker, no request for the recognizer
    await ctl('reset=1');
    const ctx = await browser.newContext(Object.assign({}, phone)); const page = patient(await ctx.newPage());
    await page.addInitScript(() => { window.claude = { use: () => Promise.resolve(null) }; });
    await page.goto(url('&nosw=1&rec=' + SLOT)); await page.waitForTimeout(2500);
    const r = { usable: await page.evaluate(() => window.__seenBack.rec.usable()), asked: (await ctl('log=1')).filter((x) => !/^index\.html/.test(x) && /standin|vendor|service/.test(x)), block: (await page.evaluate(() => window.__seenBack.about())).split('\n')[1] };
    done('viewer', r, r.usable === false && r.asked.length === 0 && /Claude/.test(r.block));
    await ctx.close();
  });

  await browser.close(); if (fake) fake.close(); if (bigServer) bigServer.kill();
  console.log(JSON.stringify(out, null, 1));
  console.log(Object.keys(out).map((k) => k + ': ' + (out[k].ok ? 'ok' : 'FAILED')).join(' | '));
  process.exit(bad ? 1 : 0);
})().catch((e) => { console.error('FAILED', e); process.exit(1); });
