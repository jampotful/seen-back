// Checks of the recognizer inside the page, in a headless browser (Chromium unless BROWSER says otherwise), against the stand-in under test/rec/models/standin
// (made by test/rec/make_standin.py; it is not a recognizer, only the same machinery with labels made from its own answers).
//   node test/rec/serve.js 8782 &
//   NODE_PATH=<where playwright lives> node test/rec/check_rec.js [flow|camera|fuse|trained|parity|progress|typeit|service|away|offline|version|missing|damaged|dying|about|viewer ...]
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
const url = (q) => ORIGIN + '/index.html?side=' + (process.env.SIDE || 420) + (/[?&]svc=/.test(q || '') ? '' : '&svc=off') + (q || '');
const SVC_PORT = +(process.env.SVC_PORT || 8784);
// SLOW=4 on a busy machine: every wait for something to appear lasts four times as long before it gives up. Nothing else changes.
const SLOW = +(process.env.SLOW || 1);
const patient = (page) => { if (SLOW === 1) return page;
  const scale = (o) => (o && o.timeout ? Object.assign({}, o, { timeout: o.timeout * SLOW }) : o), wf = page.waitForFunction.bind(page), ws = page.waitForSelector.bind(page);
  page.waitForFunction = (fn, arg, o) => wf(fn, arg, scale(o)); page.waitForSelector = (sel, o) => ws(sel, scale(o)); return page; };
const phone = Object.assign({}, devices['Pixel 7']);
if (ENGINE === 'firefox') { delete phone.isMobile; delete phone.userAgent; }      // Firefox has no mobile emulation in Playwright
if (ENGINE === 'webkit') delete phone.userAgent;
const PHOTOS = process.env.PHOTOS || path.join(here, 'photos');
const photo = (n) => path.join(PHOTOS, n);
const slotDir = path.join(here, '..', '..', SLOT);
const expect = JSON.parse(fs.readFileSync(path.join(slotDir, 'expect.json'), 'utf8'));   // what Python got (make_standin.py, or make_slot.py --photos for a real model)
const want = process.argv.slice(2).length ? process.argv.slice(2) : ['flow', 'camera', 'fuse', 'trained', 'parity', 'progress', 'typeit', 'service', 'away', 'offline', 'version', 'missing', 'damaged', 'dying', 'about', 'viewer']
  .filter((w) => isChromium || w !== 'camera');                                     // the stand-in camera feed is a Chromium switch
const ctl = (q) => new Promise((res, rej) => http.get(ORIGIN + '/__ctl?' + q, (r) => { let b = ''; r.on('data', (d) => b += d); r.on('end', () => res(JSON.parse(b))); }).on('error', rej));
const text = (page, id) => page.evaluate((i) => document.getElementById(i).textContent, id);
const about = (page) => page.evaluate(() => window.__seenBack.rec.about());
const st = (page) => page.evaluate(() => { const b = window.__seenBack; return { screen: b.S.screen, eyes: b.S.eyes, named: b.S.named, claim: !document.getElementById('claim').hidden }; });
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
  await page.waitForFunction(() => { const b = window.__seenBack; return !!b.S.eyes || !document.getElementById('claim').hidden; }, null, { timeout: 60000 });
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
  const section = async (name, fn) => { try { await fn(); } catch (e) { done(name + ' (did not finish)', { error: String(e && e.message || e).split('\n')[0] }, false); await ctl('reset=1'); } };

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
    await page.locator('#claimOffers button', { hasText: 'Monarch' }).tap(); await page.waitForTimeout(300);
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
    r.person = await meet(page, 'portrait.jpg');
    await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
    r.wall = await meet(page, 'wall.png');                       // nothing alive
    await page.locator('#claimBack').tap(); await page.waitForTimeout(200);
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
    const anole = month === 0 ? 'Green Anole' : 'Brown Anole';
    done('flow', r, r.heron.eyes === 'wader' && r.heron.shown === 'Great Blue Heron' && r.heron.sci === 'Ardea herodias' && r.heron.named.by === 'page' && /Great Blue Heron\|Ardea herodias\|page\|wader/.test(r.heronRecord[0]) && !r.heronOffersShown
      && r.stripes.eyes === 'insect' && r.stripes.shown === 'Insect' && r.stripes.sci === '' && r.offerLine === 'It may be one of these.' && r.offerButtons.join() === 'Gulf Fritillary,Monarch,Queen' && r.offersAboveField
      && r.afterOffer.eyes === 'insect' && r.afterOffer.named.common === 'Monarch' && r.afterOffer.named.by === 'you' && /^Monarch\|Danaus plexippus\|you\|insect/.test(r.afterOfferRecord[0])
      && r.dots.eyes === 'frog' && r.dots.shown === 'Frog or toad' && !r.dotsOffersShown
      && r.rings.eyes === 'reptile' && r.rings.shown === anole
      && r.garden.eyes === 'plant' && r.garden.shown === 'Beggarticks' && r.person.eyes === 'person' && r.person.shown === 'A person'
      && r.wall.claim && !r.wall.eyes && /^Nothing alive was found in that photo\. So you tell it\./.test(r.wall.sub)
      && /^Ardea herodias\. Recognized on this (phone|computer) by a small model, which can be wrong\. Chosen among species recorded around Gainesville, Florida\.$/.test(r.infoSub) && r.notRightIsThere
      && r.rows.some((x) => /Great Blue Heron \| Ardea herodias .* recognized by a small model/.test(x)) && r.rows.some((x) => /^Monarch \| .* on your word/.test(x))
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
    await page.waitForFunction(() => { const b = window.__seenBack; return !!b.S.eyes || !document.getElementById('claim').hidden; }, null, { timeout: 30000 });
    r.state = await st(page); r.sub = r.state.claim ? await text(page, 'claimSub') : ''; r.last = await page.evaluate(() => { const x = window.__seenBack.rec.about().last; return x && { kind: x.kind, from: x.from, ms: x.ms }; });
    if (r.state.claim) await page.locator('#claimBack').tap(); else await page.waitForTimeout(3500);
    await page.waitForTimeout(600);
    r.after = await st(page); r.framesSince = (await page.evaluate(() => window.__seenBack.state().writes)) - w0; r.glError = await page.evaluate(() => window.__seenBack.state().err); r.errors = errors;
    done('camera', r, !!r.last && /^\d+x\d+$/.test(r.last.from) && (r.state.claim ? /^Nothing alive was found/.test(r.sub) : !!r.state.eyes) && r.glError === 0 && !errors.length);
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
      && c.sum === '1 17 5' && r.kindsOnly.eyes === 'wader' && r.kindsOnly.shown === 'Wading bird' && r.kindsOnlyModel === 'standin-kinds-only');
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
      const tail = ' So you tell it. Type the kind of animal or plant, such as cat, heron or oak.';
      const a = await open(browser, '&nosw=1&rec=' + SLOT + '/manifest.unknown-rule.json'); await begin(a.page); r.unknownRule = (await meet(a.page, 'heron.png')).sub; r.unknownRuleWhy = (await about(a.page)).fail; await a.ctx.close();
      await ctl('reset=1'); await ctl('cut=' + encodeURIComponent('species\\.bias'));
      const b = await open(browser, '&nosw=1&rec=' + SLOT + '/manifest.trained.json'); await begin(b.page); r.biasCutShort = (await meet(b.page, 'heron.png')).sub; r.biasCutShortWhy = (await about(b.page)).fail; await b.ctx.close(); await ctl('reset=1');
      same = same && r.unknownRule === 'The recognizer’s files do not fit this build of the page.' + tail && r.biasCutShort === 'The recognizer’s file arrived damaged.' + tail;
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
    await page.waitForFunction(() => { const b = window.__seenBack; return !!b.S.eyes || !document.getElementById('claim').hidden; }, null, { timeout: 60000 });
    const lines = await page.evaluate(() => window.__lines);
    r.lines = lines.length > 12 ? lines.slice(0, 4).concat(['... ' + (lines.length - 8) + ' more ...'], lines.slice(-4)) : lines; r.end = await st(page); r.shown = await text(page, 'rvName'); r.waited = await page.evaluate(() => window.__seenBack.rec.about().last.ms); r.errors = errors;
    const nums = lines.map((l) => /^Getting the recognizer: (\d+) of (\d+) MB\.$/.exec(l)).filter(Boolean);
    done('progress', r, r.stateAtPhoto !== 'ready' && nums.length >= 3 && nums.every((n, i) => +n[1] <= +n[2] && (!i || +n[1] >= +nums[i - 1][1])) && +nums[nums.length - 1][2] === 15 && r.end.eyes === 'wader' && r.shown === 'Great Blue Heron' && !errors.length);
    await ctl('reset=1'); await ctx.close();
  });

  if (want.includes('typeit')) await section('typeit', async () => {   // a way out of a long first download: type the name, and the download carries on by itself
    await ctl('reset=1'); await ctl('slow=' + encodeURIComponent('ort-wasm.*\\.wasm') + '&bps=1500000');
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
    done('typeit', r, !r.buttonBefore && /^Getting the recognizer: \d+ of 15 MB\.$/.test(r.line) && r.button === 'Type it instead' && r.buttonUnderLine
      && r.sub === 'The recognizer keeps downloading meanwhile. Type the kind of animal or plant, such as cat, heron or oak.' && r.stateAtTap === 'loading' && !r.buttonWhileAsking
      && r.typed.eyes === 'wader' && r.typed.named.by === 'you' && r.typed.named.common === 'Heron' && r.after.eyes === 'wader' && r.after.named.by === 'you' && r.after.screen === 'askView' && r.record.length === 1 && r.record[0] === 'Heron|you|wader'
      && r.next.eyes === 'insect' && !r.buttonNext && r.trace === 1 && !errors.length);
    await ctl('reset=1'); await ctx.close();
  });

  // ---------- the species service: a fake server that speaks Gradio's two-step call (test/rec/fake_service.js)
  const until = async (fn, ms) => { const t0 = Date.now(); while (!fn()) { if (Date.now() - t0 > (ms || 15000)) throw new Error('waited too long'); await new Promise((res) => setTimeout(res, 50)); } };
  const svcLine = (page) => page.evaluate(() => { const vis = (e) => !e.hidden && e.offsetParent !== null, a = document.getElementById('svcView'), b = document.getElementById('svcHud'); return vis(a) ? a.textContent : vis(b) ? b.textContent : ''; });
  const svcWatch = (page) => page.evaluate(() => { window.__svc = []; const el = document.getElementById('svcView'); new MutationObserver(() => { const t = el.hidden ? '' : el.textContent; if (window.__svc[window.__svc.length - 1] !== t) window.__svc.push(t); }).observe(el, { childList: true, characterData: true, subtree: true, attributes: true }); });
  const svcSettled = (page) => page.waitForFunction(() => { const v = window.__seenBack.S.svc; return !v || (v.state !== 'asking' && v.state !== 'waking'); }, null, { timeout: 20000 });
  const byService = (page) => page.waitForFunction(() => { const n = window.__seenBack.S.named; return !!n && n.by === 'service'; }, null, { timeout: 20000 });
  const recordRows = (page) => page.evaluate(() => window.__seenBack.record().map((m) => m.common + '|' + m.sci + '|' + m.by + '|' + m.key));
  const typeName = async (page, name) => { await page.waitForSelector('#claim', { state: 'visible', timeout: 8000 }); await page.locator('#claimName').fill(name); await page.locator('#claimForm button[type=submit]').tap(); };
  let fake = null;
  const quiet = (errors) => errors.filter((e) => !/blocked by CORS policy|net::ERR_/.test(e));     // a sleeping server's refusals are written to the console by the browser itself
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
      await page.locator('#backAskView').tap(); await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' }); await page.locator('#about summary').tap(); await page.waitForTimeout(300);
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
      all('offer', r.offer.eyesAtOnce === 'insect' && r.offer.shown === 'Insect' && r.offer.line === 'A larger model on a server can try to name the species. Ask it?' && r.offer.sentBeforeYes === 0);
      all('sheet', r.sheet.title === 'Ask a larger model?' && r.sheet.sub === 'This one photo, made smaller, would be sent to a server run for this project, at 127.0.0.1:' + SVC_PORT + '. The month and the name of this region go with it. The photo is not kept there.'
        && r.sheet.tick === 'Do not ask again' && r.sheet.yes === 'Ask it' && r.sheet.no === 'Not now' && /About this build/.test(r.sheet.note) && !r.sheet.ticked);
      all('notNow', r.notNow.line === '' && r.notNow.sent === 0 && r.notNow.choice === '' && r.notNow.named === 'page');
      // the next photo asks again. This time: yes, and do not ask again
      fake.set({ delay: 700 });
      await meet(page, 'stripes.png'); await page.waitForSelector('#svcView', { state: 'visible', timeout: 8000 });
      await page.locator('#svcView').tap(); await page.waitForSelector('#ask', { state: 'visible' }); await page.locator('#askKeep').check(); await page.locator('#askYes').tap();
      await byService(page); await page.waitForTimeout(200);
      const month = new Date().getMonth() + 1;
      r.asked = { named: (await st(page)).named, lines: await page.evaluate(() => window.__svc.filter(Boolean).filter((x, i, a) => a.indexOf(x) === i)), sent: fake.calls(), choice: await page.evaluate(() => window.__seenBack.svc.choice()), record: await recordRows(page), line: await svcLine(page) };
      const c = r.asked.sent[0] || {};
      all('asked', r.asked.named.common === 'Monarch' && r.asked.named.scientific === 'Danaus plexippus' && r.asked.named.by === 'service' && r.asked.lines.indexOf('Asking the larger model.') >= 0 && r.asked.line === 'The larger model says Monarch.' && r.asked.choice === 'yes'
        && r.asked.record[0] === 'Monarch|Danaus plexippus|service|insect' && r.asked.record.length === 2);
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
      await page.locator('#about summary').tap(); await page.waitForTimeout(300);
      r.about = await page.evaluate(() => ({ shown: !document.getElementById('svcBox').hidden, value: document.getElementById('svcChoice').value, options: [...document.querySelectorAll('#svcChoice option')].map((o) => o.textContent), label: document.querySelector('#svcBox label').textContent }));
      await page.evaluate(() => { document.getElementById('record').scrollTop = 99999; }); await page.waitForTimeout(150); await page.screenshot({ path: path.join(here, 'shots', 'service-about.png'), scale: 'css' }).catch(() => {});
      await page.locator('#recordClose').tap();
      all('shownAfter', r.pill === 'Monarch' && r.infoSub === 'Danaus plexippus. Named by a larger model on a server, which can be wrong. Chosen among species recorded around Gainesville, Florida.'
        && r.offers.join() === 'Monarch,Queen,Gulf Fritillary,Viceroy,Common Buckeye' && /^Monarch \| Danaus plexippus .* named by a larger model on a server$/.test(r.rows[0]) && r.about.shown && r.about.value === 'yes' && r.about.options.join() === 'Ask me each time,Always ask it,Never ask it');
      // from now on it is asked without a prompt. It sees another kind of creature and is sure: the change is offered in one line, and not made
      fake.set({ answer: 'egret', delay: 300 }); let n = fake.calls().length;
      await meet(page, 'dots.png'); await page.waitForFunction(() => /Change eyes\?$/.test(document.getElementById('svcView').textContent), null, { timeout: 15000 });
      await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
      const before = await st(page);
      r.change = { line: await text(page, 'svcView'), eyesBefore: before.eyes, namedBefore: before.named.common + '|' + before.named.by, posts: fake.calls().length - n, meetings: (await recordRows(page)).length };
      await page.screenshot({ path: path.join(here, 'shots', 'service-change.png'), scale: 'css' }).catch(() => {});
      await page.locator('#svcView').tap(); await page.waitForFunction(() => window.__seenBack.S.eyes === 'wader', null, { timeout: 6000 }); await page.waitForTimeout(300);
      const after = await st(page); r.change.after = after.eyes + '|' + after.named.common + '|' + after.named.by; r.change.record = await recordRows(page); r.change.lineAfter = await svcLine(page);
      all('change', r.change.line === 'It looks like a Great Egret, a wading bird. Change eyes?' && r.change.eyesBefore === 'frog' && r.change.namedBefore === 'Frog or toad|page' && r.change.posts === 1
        && r.change.after === 'wader|Great Egret|service' && r.change.record[0] === 'Great Egret|Ardea alba|service|wader' && r.change.record.length === r.change.meetings && r.change.lineAfter === '');
      // another kind, but it is not sure enough: nothing changes, and its likeliest stay as offers
      fake.set({ answer: 'unsure' }); n = fake.calls().length;
      await meet(page, 'dots.png'); await until(() => fake.calls().length > n); await svcSettled(page); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); await page.waitForTimeout(200);
      const u = await st(page); r.unsure = { state: u.eyes + '|' + u.named.common + '|' + u.named.by, line: await svcLine(page) };
      await page.locator('#changeAskView').tap(); await page.waitForSelector('#claim', { state: 'visible' }); await page.waitForTimeout(150);
      r.unsure.offers = await page.evaluate(() => [...document.querySelectorAll('#claimOffers button')].map((b) => b.textContent)); await page.locator('#claimBack').tap();
      all('unsure', r.unsure.state === 'frog|Frog or toad|page' && r.unsure.line === '' && r.unsure.offers.join() === 'Great Egret,Green Treefrog,Snowy Egret');
      // the same kind, but its best guess is under the service's own mark for naming: the name stays, the guesses are offered
      fake.set({ answer: 'faint' }); n = fake.calls().length;
      await meet(page, 'stripes.png'); await until(() => fake.calls().length > n); await svcSettled(page); await page.waitForTimeout(200);
      const f = await st(page); r.faint = f.eyes + '|' + f.named.common + '|' + f.named.by; all('faint', r.faint === 'insect|Insect|page');
      // the device named the species itself: nobody is asked
      n = fake.calls().length; await meet(page, 'heron.png'); await page.waitForTimeout(900);
      r.namedByDevice = { posts: fake.calls().length - n, by: (await st(page)).named.by, line: await svcLine(page) }; all('namedByDevice', r.namedByDevice.posts === 0 && r.namedByDevice.by === 'page' && r.namedByDevice.line === '');
      // a name typed while the question is out is not overwritten when the answer comes
      fake.set({ answer: 'monarch', delay: 1500 }); n = fake.calls().length;
      await meet(page, 'stripes.png'); await until(() => fake.calls().length > n); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
      await page.locator('#changeAskView').tap(); await typeName(page, 'beetle'); await page.waitForTimeout(2300);
      const t = await st(page); r.typedWins = t.named.common + '|' + t.named.by; all('typedWins', r.typedWins === 'Beetle|you');
      // "Never ask it", chosen in the About block: no line, nothing sent; and back to asking each time
      await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); await page.locator('#backAskView').tap(); await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' });
      await page.locator('#about summary').tap().catch(() => {}); await page.waitForTimeout(200);
      if (!(await page.locator('#svcChoice').isVisible())) { await page.locator('#about summary').tap(); await page.waitForTimeout(300); }
      await page.selectOption('#svcChoice', 'no'); await page.locator('#recordClose').tap();
      fake.set({ delay: 0 }); n = fake.calls().length; await meet(page, 'stripes.png'); await page.waitForTimeout(900);
      r.never = { posts: fake.calls().length - n, line: await svcLine(page), choice: await page.evaluate(() => window.__seenBack.svc.choice()) };
      await page.evaluate(() => window.__seenBack.svc.setChoice('')); await meet(page, 'stripes.png'); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 }); await page.waitForTimeout(400);
      r.eachTimeAgain = await svcLine(page);
      all('never', r.never.posts === 0 && r.never.line === '' && r.never.choice === 'no' && r.eachTimeAgain === 'A larger model on a server can try to name the species. Ask it?');
      r.errors = errors; all('noErrors', !errors.length);
      await ctx.close();
    }
    for (const [name, file] of [['asleep', 'service.json'], ['asleepWithHealth', 'service.health.json']]) {   // a sleeping server: one honest line, then the answer
      fake.reset(); const { ctx, page, errors } = await open(browser, Q + file); await ready(page);
      await page.evaluate(() => { window.__seenBack.svc.setChoice('yes'); window.__seenBack.svc.test.times({ poll: 400 }); }); await begin(page); await svcWatch(page);
      fake.sleep(600000); const t0 = Date.now(); await meet(page, 'stripes.png');
      await page.waitForFunction(() => window.__svc.indexOf('The larger model is waking up, which can take a minute.') >= 0, null, { timeout: 15000 });
      const eyesWhileWaiting = (await st(page)).eyes; await page.waitForTimeout(1300); fake.sleep(0);     // it wakes
      await byService(page);
      r[name] = { lines: await page.evaluate(() => window.__svc.filter(Boolean).filter((x, i, a) => a.indexOf(x) === i)), eyesWhileWaiting, named: (await st(page)).named.common, posts: fake.calls().length, healthAsked: fake.state.health, wokeAfterMs: Date.now() - t0, errors: quiet(errors) };
      all(name, r[name].lines.join(' / ') === 'Asking the larger model. / The larger model is waking up, which can take a minute. / The larger model says Monarch.' && eyesWhileWaiting === 'insect' && r[name].named === 'Monarch' && r[name].posts === 1 && (file === 'service.json' ? r[name].healthAsked === 0 : r[name].healthAsked >= 2) && !r[name].errors.length);
      await ctx.close();
    }
    { // it does not wake within the wait (shortened here from 90 seconds to 2): it lets go quietly, and what the device said stands. Then failures and refusals of every sort
      fake.reset(); const { ctx, page, errors } = await open(browser, Q + 'service.json'); await ready(page);
      r.waitByDefault = await page.evaluate(() => { window.__seenBack.svc.setChoice('yes'); const t = window.__seenBack.svc.test.times({}); return { wake: t.wake, answer: t.answer }; });
      await page.evaluate(() => { window.__seenBack.svc.test.times({ wake: 2000, poll: 400 }); }); await begin(page); await svcWatch(page);
      fake.sleep(600000); await meet(page, 'stripes.png');
      await page.waitForFunction(() => window.__svc.length >= 2 && window.__svc[window.__svc.length - 1] === '', null, { timeout: 15000 });
      const s = await st(page);
      r.neverWakes = { lines: await page.evaluate(() => window.__svc.filter((x, i, a) => (i || x) && (!i || a[i - 1] !== x))), state: s.eyes + '|' + s.named.common + '|' + s.named.by, claim: s.claim, msg: await text(page, 'msg'), why: await page.evaluate(() => window.__seenBack.diag().filter((d) => d.what === 'service-none').map((d) => d.code).join()) };
      all('neverWakes', r.waitByDefault.wake === 90000 && r.neverWakes.lines.join(' / ') === 'Asking the larger model. / The larger model is waking up, which can take a minute. / ' && r.neverWakes.state === 'insect|Insect|page' && !r.neverWakes.claim && r.neverWakes.msg === '' && r.neverWakes.why === 'asleep');
      await page.evaluate(() => { window.__seenBack.svc.test.times({ wake: 90000, answer: 1500 }); });
      r.failures = {};
      for (const mode of ['error', 'garbled', 'refusal', 'refuse', 'busy', 'slow']) {
        fake.reset(); fake.set(mode === 'slow' ? { delay: 4000 } : { mode });
        await meet(page, 'stripes.png'); await until(() => fake.calls().length > 0); await svcSettled(page); await page.waitForTimeout(150);
        const x = await st(page);
        r.failures[mode] = { state: x.eyes + '|' + x.named.common + '|' + x.named.by, line: await svcLine(page), posts: fake.calls().length, claim: x.claim, msg: await text(page, 'msg') };
        all('failure ' + mode, r.failures[mode].state === 'insect|Insect|page' && r.failures[mode].line === '' && r.failures[mode].posts === 1 && !x.claim && r.failures[mode].msg === '');
      }
      r.failureCodes = await page.evaluate(() => window.__seenBack.diag().filter((d) => d.what === 'service-none').map((d) => d.code).join());
      r.failureErrors = quiet(errors); all('failuresQuiet', !r.failureErrors.length);
      await ctx.close();
    }
    fake.reset();
    done('service', r, ok);
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
    const about = async () => { await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' }); if (!(await page.locator('#awayBox').isVisible())) { await page.locator('#about summary').tap(); await page.waitForTimeout(300); } };
    r.near = { heron: (await meet(page, 'heron.png')).shown }; r.near.info = await info();
    await about(); r.switch = { label: (await page.locator('#awayRow .tick').textContent()).trim(), note: await text(page, 'awayNote'), tickedAtFirst: await page.locator('#awayBox').isChecked() };
    await page.evaluate(() => { document.getElementById('record').scrollTop = 99999; }); await page.waitForTimeout(150); await page.screenshot({ path: path.join(here, 'shots', 'away.png'), scale: 'css' }).catch(() => {});
    await page.locator('#awayBox').check(); await page.locator('#recordClose').tap();
    // elsewhere: the device names the kind and no species, and the larger model is asked without a region
    fake.reset(); fake.set({ answer: 'egret' });
    const h = await meet(page, 'heron.png'); r.away = { atOnce: h.eyes + '|' + h.shown, top: h.last && h.last.top }; await byService(page);
    r.away.sent = fake.calls().map((c) => JSON.stringify(c.region) + ' month ' + c.month); r.away.named = (await st(page)).named.common + '|' + (await st(page)).named.by; r.away.info = await info();
    await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' }); r.away.rows = await page.evaluate(() => [...document.querySelectorAll('#metList li')].slice(0, 1).map((li) => li.querySelector('.nm').textContent + ' | ' + li.querySelector('.sm').textContent)); await page.locator('#recordClose').tap();
    // the choice is kept across a reload, and can be undone
    await page.reload(); await page.waitForTimeout(400); await ready(page);
    r.afterReload = await page.evaluate(() => window.__seenBack.rec.local); await begin(page);
    await about(); r.tickedAfterReload = await page.locator('#awayBox').isChecked(); await page.locator('#awayBox').uncheck(); await page.locator('#recordClose').tap();
    fake.reset(); r.nearAgain = (await meet(page, 'heron.png')).shown; r.nearAgainPosts = fake.calls().length;
    r.locationAsked = await page.evaluate(() => window.__geo); r.errors = errors;
    done('away', r, r.near.heron === 'Great Blue Heron' && /which can be wrong\. Chosen among species recorded around Gainesville, Florida\.$/.test(r.near.info)
      && r.switch.label === 'I am not near Gainesville' && /^Species are named from a list of those recorded around Gainesville, Florida\./.test(r.switch.note) && !r.switch.tickedAtFirst
      && r.away.atOnce === 'wader|Wading bird' && r.away.top === null && r.away.sent.join() === '"" month ' + (new Date().getMonth() + 1) && r.away.named === 'Great Egret|service'
      && r.away.info === 'Ardea alba. Named by a larger model on a server, which can be wrong.' && /named by a larger model on a server$/.test(r.away.rows[0])
      && r.afterReload === false && r.tickedAfterReload && r.nearAgain === 'Great Blue Heron' && r.nearAgainPosts === 0 && r.locationAsked === 0 && !errors.length);
    await ctx.close();
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
    await page.locator('#backAskView').tap(); await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' }); await page.locator('#about summary').tap(); await page.waitForTimeout(250);
    r.offline.aboutLine = (await text(page, 'buildMark')).split('\n')[1];
    r.first.errors = []; let ok = r.first.heron === 'Great Blue Heron' && r.offline.online === false && r.offline.heron === 'Great Blue Heron' && r.offline.stripes === 'insect' && /^Recognizer: standin-random-conv, wasm/.test(r.offline.aboutLine)
      && r.fetchedFirst.filter((x) => /vision\.int8\.onnx/.test(x)).length === 1 && r.fetchedFirst.filter((x) => /\.wasm\?/.test(x)).length === 1 && !errors.length;
    await page.close(); await ctx.setOffline(false); await ctl('reset=1');
    if (want.includes('version')) {
      // online again with nothing changed: the manifest is asked for, the model is not
      await ctl('reset=1');
      ({ page, errors } = await open(browser, '&rec=' + SLOT, null, ctx)); await ready(page);
      r.again = { asked: (await ctl('log=1')).filter((x) => !/^index\.html/.test(x) && /standin|vendor/.test(x)), errors: errors.slice() }; ok = ok && !errors.length;
      await page.close();
      // the laboratory publishes a new model under the same address: another manifest, so another version
      await ctl('reset=1'); await ctl('swap=' + SLOT + '/manifest.json&with=' + SLOT + '/manifest.kinds-only.json');
      ({ page, errors } = await open(browser, '&rec=' + SLOT, null, ctx)); await ready(page); await page.waitForTimeout(600);
      r.newVersion = { model: (await about(page)).model, asked: (await ctl('log=1')).filter((x) => !/^index\.html/.test(x) && /standin/.test(x)),
        kept: await page.evaluate(async () => (await (await caches.open('keep-v1')).keys()).map((q) => q.url.replace(location.origin + '/', '')).filter((u) => /standin/.test(u)).sort()), errors: errors.slice() };
      const vs = new Set(r.newVersion.kept.map((u) => (/v=([0-9a-f]+)/.exec(u) || [])[1]).filter(Boolean));
      ok = ok && r.again.asked.length === 1 && /manifest\.json$/.test(r.again.asked[0]) && r.newVersion.model === 'standin-kinds-only' && r.newVersion.asked.some((x) => /vision\.int8\.onnx\?v=/.test(x)) && vs.size === 1 && r.newVersion.kept.some((u) => /vision\.int8\.onnx\?v=/.test(u)) && !errors.length;
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
    const tail = ' So you tell it. Type the kind of animal or plant, such as cat, heron or oak.';
    done('missing', r, r.noSlot.claim && r.noSlot.sub === 'This page has no recognizer yet.' + tail && r.noModel.claim && r.noModel.sub === 'The recognizer’s files are missing.' + tail && r.recovered === 'Great Blue Heron'
      && r.offlineFirst.claim && r.offlineFirst.sub === 'The recognizer could not be downloaded.' + tail && r.off.claim && r.off.sub === 'This page’s recognizer is switched off.' + tail);
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
    const tail = ' So you tell it. Type the kind of animal or plant, such as cat, heron or oak.', sub = 'The recognizer’s file arrived damaged.' + tail;
    done('damaged', r, r.changed.claim && r.changed.sub === sub && /sha256/.test(r.changedWhy) && r.keptAfter === 0 && r.cut.claim && r.cut.sub === sub && /^damaged: session/.test(r.keptBadWhy) && r.keptBadThenFetchedAgain === 'Great Blue Heron');
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
    const tail = ' So you tell it. Type the kind of animal or plant, such as cat, heron or oak.';
    done('dying', r, r.before === 'Great Blue Heron' && r.thrown.claim && r.thrown.sub === 'The recognizer stopped working.' + tail && r.afterThrow === 'Great Blue Heron'
      && r.hung.claim && r.hung.sub === 'The recognizer took too long.' + tail && r.afterHang === 'insect' && r.pictureStillDrawn);
    await ctx.close();
  });

  if (want.includes('about')) await section('about', async () => {    // the block to copy from a real phone
    const { ctx, page, errors } = await open(browser, '&nosw=1&rec=' + SLOT, isChromium ? { permissions: ['clipboard-read', 'clipboard-write'] } : {}); const r = {}; await ready(page);
    await begin(page); await meet(page, 'heron.png'); await page.waitForSelector('#askView', { state: 'visible', timeout: 6000 });
    await page.locator('#backAskView').tap(); await page.locator('#recAskAnimal').tap(); await page.waitForSelector('#record', { state: 'visible' });
    await page.locator('#about summary').tap(); await page.waitForTimeout(200);
    r.block = (await text(page, 'buildMark')).split('\n');
    await page.locator('#aboutCopy').tap(); await page.waitForTimeout(300);
    r.note = await text(page, 'aboutNote'); r.clip = isChromium ? (await page.evaluate(() => navigator.clipboard.readText())).split('\n').length : r.block.length;   // reading the clipboard back is allowed to a check only in Chromium
    await page.evaluate(() => { document.getElementById('record').scrollTop = 99999; }); await page.waitForTimeout(150);
    fs.mkdirSync(path.join(here, 'shots'), { recursive: true }); await page.screenshot({ path: path.join(here, 'shots', 'about.png'), scale: 'css' });
    r.overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth); r.errors = errors;
    done('about', r, /^Seen Back, build \d+\.$/.test(r.block[0]) && /^Recognizer: standin-random-conv, wasm, 1 thread, ready in [\d.]+ s\.$/.test(r.block[1]) && /^Last photo: wader 1\.00, Ardea herodias 1\.00; .*prepared in \d+ ms from 900x1200, recognized in \d+ ms\.$/.test(r.block[2])
      && /^Picture: \d+ by \d+.* limit 420, [\d.]+ ms a frame over the last \d+\.$/.test(r.block[3]) && /^Screen: /.test(r.block[4]) && (r.note === 'Copied.' || !isChromium) && r.clip === r.block.length && r.overflow <= 0 && !errors.length);
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

  await browser.close(); if (fake) fake.close();
  console.log(JSON.stringify(out, null, 1));
  console.log(Object.keys(out).map((k) => k + ': ' + (out[k].ok ? 'ok' : 'FAILED')).join(' | '));
  process.exit(bad ? 1 : 0);
})().catch((e) => { console.error('FAILED', e); process.exit(1); });
