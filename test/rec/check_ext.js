// The larger model in its second form (docs/CONTRACTS.md, "vision.graph"): a small graph beside its weights as an external data file in parts.
//   python3 -I build.py; python3 -I test/rec/make_standin.py --ext; node test/rec/check_ext.js
// The page is served on PORT (8809 unless PORT says otherwise) and the parts from a second origin on 8807 (the port the stand-in's manifests
// name), with CORS; either server is started here if nothing answers. Nothing leaves this machine. SLOW=3 on a busy machine: every wait is
// three times as long before it gives up.
// What is held: the model is fetched in parts, verified, kept, started and answers, with the same answer as the same encoder in one file;
// a reload fetches nothing of it; a damaged weights part, or a damaged graph, is refused in words and the download carries on afterwards
// from what was kept; a manifest without vision.graph still loads; an older form of the same slot stays kept until the new one is kept,
// and goes then; a manifest that gives a graph without the name of its weights, or a graph to the pocket slot, is refused.
const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path'), { spawn } = require('child_process');
const here = __dirname, PORT = +(process.env.PORT || 8809), EXT_PORT = 8807, ORIGIN = 'http://127.0.0.1:' + PORT, SLOW = +(process.env.SLOW || 1);
const EXT = 'test/rec/models/standin-ext', OLD = 'test/rec/models/standin-big';
const say = { damaged: 'The full database\u2019s download is damaged.' };   // the page's words as of build 34
const get = (u) => new Promise((res, rej) => http.get(u, (r) => { let b = ''; r.on('data', (d) => b += d); r.on('end', () => res(b)); }).on('error', rej));
const ctl = (port, q) => get('http://127.0.0.1:' + port + '/__ctl?' + q).then((b) => JSON.parse(b));
const servers = [];
async function up(port, cors) {
  try { await ctl(port, 'reset=1'); return; } catch (e) {}
  servers.push(spawn(process.execPath, [path.join(here, 'serve.js'), String(port)].concat(cors ? ['cors'] : []), { stdio: 'ignore' }));
  for (let i = 0; i < 60; i++) { await new Promise((r) => setTimeout(r, 100)); try { await ctl(port, 'reset=1'); return; } catch (e) {} }
  throw new Error('no server on port ' + port);
}
const results = []; let failed = 0;
function hold(name, cond, detail) { results.push(name); if (!cond) { failed++; console.log('FAILED ' + name + (detail ? ': ' + JSON.stringify(detail).slice(0, 600) : '')); } else console.log('ok ' + name); }

(async () => {
  if (!fs.existsSync(path.join(here, '..', '..', 'index.html'))) throw new Error('no index.html: run python3 -I build.py first');
  if (!fs.existsSync(path.join(here, 'models', 'standin-ext', 'manifest.json'))) throw new Error('no ' + EXT + ': run python3 -I test/rec/make_standin.py --ext first');
  // the older form names the parts on the port the stand-ins were made for; a copy of its manifest names this one
  fs.writeFileSync(path.join(here, 'models', 'standin-big', 'manifest.port' + EXT_PORT + '.json'), fs.readFileSync(path.join(here, 'models', 'standin-big', 'manifest.json'), 'utf8').replace(/127\.0\.0\.1:8788/g, '127.0.0.1:' + EXT_PORT));
  await up(PORT, false); await up(EXT_PORT, true);
  const browser = await chromium.launch(); const errors = [];
  async function open(ctx, slot) {
    const page = await ctx.newPage(); page.setDefaultTimeout(30000 * SLOW);
    page.on('pageerror', (e) => errors.push(e.message));
    await page.goto(ORIGIN + '/index.html?side=420&nosw=1&svc=off&rec=off&bigmem=8&big=' + slot);   // bigmem=8: a device that can hold it (build 33), whatever this machine is
    await page.waitForFunction(() => !!(window.__seenBack && window.__seenBack.big), null, { timeout: 30000 * SLOW });
    return page;
  }
  const fetchIt = (page) => page.evaluate(() => window.__seenBack.big.get().then(() => ({ ok: true }), (e) => ({ ok: false, code: e.code, sentence: e.sentence, detail: e.detail })));
  const survey = (page) => page.evaluate(() => window.__seenBack.big.survey(true));
  const about = (page) => page.evaluate(() => { const a = window.__seenBack.big.about(); return { state: a.state, why: a.why, fail: a.fail, have: a.have, getFail: a.getFail }; });
  const keys = (page) => page.evaluate(() => caches.open('keep-v1').then((c) => c.keys()).then((ks) => ks.map((r) => r.url.replace(location.origin + '/', ''))));
  const theirs = (k, dir) => k.filter((u) => u.indexOf(dir + '/part/') === 0 || u.indexOf(dir + '/whole/') === 0).sort();
  const ask = (page, photo) => page.evaluate(async (u) => {
    const blob = await (await fetch(u)).blob(), file = new File([blob], 'photo', { type: blob.type }), c = document.createElement('canvas'); c.width = c.height = 1;
    try { const r = await window.__seenBack.big.recognize(c, file); return { kind: r.kind, sure: r.sure, named: r.named ? r.named.en : '', top: r.species.map((s) => [s.sci, s.p]) }; }
    catch (e) { return { error: e.code, sentence: e.sentence, detail: e.detail }; }
  }, ORIGIN + '/test/rec/photos/' + photo);
  const asked = async (port) => (await ctl(port, 'log=1')).filter((u) => /standin-(ext|big)\//.test(u));
  const M = JSON.parse(fs.readFileSync(path.join(here, 'models', 'standin-ext', 'manifest.json'), 'utf8')), mine = [M.vision.graph].concat(M.vision.parts).map((p) => EXT + '/part/' + p.sha256 + '?bytes=' + p.bytes);
  const MO = JSON.parse(fs.readFileSync(path.join(here, 'models', 'standin-ext', 'manifest.old.json'), 'utf8')), older = MO.vision.parts.map((p) => EXT + '/part/' + p.sha256 + '?bytes=' + p.bytes);
  const files = M.vision.parts.map((p) => p.url.replace(/^http:\/\/[^\/]+\//, '')), graphFile = M.vision.graph.url.replace(/^http:\/\/[^\/]+\//, '');

  // 1. fetched in parts, verified, kept, started; it answers, and as the same encoder in one file answers
  let ctx = await browser.newContext(), page = await open(ctx, EXT); let newAnswer = null;
  {
    await ctl(EXT_PORT, 'reset=1');
    const before = await survey(page), r = await fetchIt(page), a = await about(page), k = theirs(await keys(page), EXT), log = await asked(EXT_PORT);
    hold('fresh: nothing kept before', before === 'absent', before);
    hold('fresh: fetched, verified, kept and started', r.ok && a.state === 'ready' && a.have === 'kept', { r, a });
    hold('fresh: the graph and each part asked for once', JSON.stringify(log) === JSON.stringify([graphFile].concat(files)), log);
    hold('fresh: the graph and the parts kept by their checksums, the whole marked verified', JSON.stringify(k) === JSON.stringify(mine.concat([EXT + '/whole/' + M.vision.sha256]).sort()), k);
    newAnswer = await ask(page, 'stripes.png');
    hold('fresh: it answers', !newAnswer.error && newAnswer.top.length === 5 && newAnswer.named === 'Monarch', newAnswer);
  }
  // 2. a reload fetches nothing of it
  {
    await ctl(EXT_PORT, 'reset=1'); await ctl(PORT, 'reset=1');
    await page.close(); page = await open(ctx, EXT);
    const s = await survey(page), r = await ask(page, 'stripes.png'), a = await about(page), far = await asked(EXT_PORT), near = (await asked(PORT)).filter((u) => !/manifest\.json/.test(u));
    hold('reload: kept', s === 'kept', s);
    hold('reload: it answers as before', !r.error && JSON.stringify(r) === JSON.stringify(newAnswer) && a.state === 'ready', { r, a });
    hold('reload: nothing of the model fetched', far.length === 0 && near.length === 0, { far, near });
  }
  await ctx.close();
  // 3. a manifest without vision.graph still loads, and the same encoder gives the same answer to the last digit
  ctx = await browser.newContext(); page = await open(ctx, OLD + '/manifest.port' + EXT_PORT + '.json');
  {
    const r = await fetchIt(page), a = await about(page), old = await ask(page, 'stripes.png');
    hold('one file: fetched, kept and started', r.ok && a.state === 'ready' && a.have === 'kept', { r, a });
    hold('one file: the same answer as the external form', !old.error && JSON.stringify(old) === JSON.stringify(newAnswer), { old, newAnswer });
  }
  await ctx.close();
  // 4. a damaged weights part is refused in words; afterwards the download carries on from what was kept
  ctx = await browser.newContext(); page = await open(ctx, EXT);
  {
    await ctl(EXT_PORT, 'reset=1&damage=' + encodeURIComponent('vision\\.weights\\.bin\\.part01'));
    const r = await fetchIt(page), a = await about(page), k = theirs(await keys(page), EXT);
    hold('damaged part: refused in words', !r.ok && r.code === 'damaged' && r.sentence === say.damaged && a.have === 'partial', { r, a });
    hold('damaged part: the graph and the first part kept, the damaged one not', JSON.stringify(k) === JSON.stringify(mine.slice(0, 2).sort()), k);
    await ctl(EXT_PORT, 'reset=1');
    const r2 = await fetchIt(page), a2 = await about(page), log = await asked(EXT_PORT), ans = await ask(page, 'stripes.png');
    hold('damaged part: the next try fetches only what is missing, and it answers', r2.ok && a2.state === 'ready' && JSON.stringify(log) === JSON.stringify(files.slice(1)) && JSON.stringify(ans) === JSON.stringify(newAnswer), { r2, a2, log, ans });
  }
  await ctx.close();
  // 5. a damaged graph is refused in words, and nothing of it is kept
  ctx = await browser.newContext(); page = await open(ctx, EXT);
  {
    await ctl(EXT_PORT, 'reset=1&damage=' + encodeURIComponent('vision\\.graph\\.onnx'));
    const r = await fetchIt(page), k = theirs(await keys(page), EXT);
    hold('damaged graph: refused in words, nothing kept', !r.ok && r.code === 'damaged' && r.sentence === say.damaged && k.length === 0, { r, k });
    await ctl(EXT_PORT, 'reset=1');
  }
  await ctx.close();
  // 6. the same slot's older form stays kept until the new one is kept, and goes then
  ctx = await browser.newContext(); page = await open(ctx, EXT);
  {
    await ctl(PORT, 'reset=1&swap=' + encodeURIComponent(EXT + '/manifest.json') + '&with=' + encodeURIComponent(EXT + '/manifest.old.json'));
    const r = await fetchIt(page), k = theirs(await keys(page), EXT);
    hold('older form: kept and started in this slot', r.ok && JSON.stringify(k) === JSON.stringify(older.concat([EXT + '/whole/' + MO.vision.sha256]).sort()), { r, k });
    await ctl(PORT, 'reset=1');
    await page.close(); page = await open(ctx, EXT);
    const s = await survey(page); await page.waitForTimeout(1500 * SLOW); const k2 = theirs(await keys(page), EXT);
    hold('older form: still kept once the slot names the new one, before the new one is kept', s === 'absent' && older.every((u) => k2.indexOf(u) >= 0), { s, k2 });
    const r2 = await fetchIt(page); let k3 = [];
    for (let i = 0; i < 20 * SLOW; i++) { k3 = theirs(await keys(page), EXT); if (!older.some((u) => k3.indexOf(u) >= 0)) break; await page.waitForTimeout(250); }
    hold('older form: let go once the new one is kept', r2.ok && JSON.stringify(k3) === JSON.stringify(mine.concat([EXT + '/whole/' + M.vision.sha256]).sort()), { r2, k3 });
    const ans = await ask(page, 'stripes.png');
    hold('older form: the new one answers', JSON.stringify(ans) === JSON.stringify(newAnswer), ans);
  }
  await ctx.close();
  // 7. what is refused: a graph without the name of its weights; a graph in the pocket slot
  ctx = await browser.newContext(); page = await open(ctx, EXT);
  {
    const r = await page.evaluate((m) => {
      const B = window.__seenBack, rows = [['Danaus plexippus', 'Monarch', 'insect', null]], a = JSON.parse(JSON.stringify(m)); delete a.vision.weights_name; a.species.count = 1;
      const p = JSON.parse(JSON.stringify(m)); p.vision.url = 'vision.int8.onnx'; delete p.vision.parts; p.species.count = 1;
      const one = (rec, x) => { try { rec.test.world(x, rows); return 'taken'; } catch (e) { return e.code + ': ' + e.detail; } };
      return { noName: one(B.big, a), pocket: one(B.rec, p), whole: one(B.big, Object.assign(JSON.parse(JSON.stringify(m)), { species: Object.assign({}, m.species, { count: 1 }) })) };
    }, M);
    hold('refused: a graph without the name of its weights; a graph in the pocket slot', /^unfit/.test(r.noName) && /^unfit/.test(r.pocket) && r.whole === 'taken', r);
  }
  await ctx.close();
  await browser.close();
  hold('no errors on the page', errors.length === 0, errors.slice(0, 5));
  servers.forEach((s) => { try { s.kill(); } catch (e) {} });
  console.log(failed ? 'check_ext: FAILED ' + failed + ' of ' + results.length : 'check_ext: all ' + results.length + ' passed');
  process.exit(failed ? 1 : 0);
})().catch((e) => { console.log('check_ext: FAILED with ' + (e && e.stack || e)); servers.forEach((s) => { try { s.kill(); } catch (x) {} }); process.exit(1); });
