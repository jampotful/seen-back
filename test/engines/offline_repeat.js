// The WebKit lead, made to happen on purpose: a later offline visit that once failed with "network: .../manifest.json" although
// every file was kept (engines runs 23 and 24, rec_probe.js PHONE=1). Repeats rec_probe.js's offline case TRIALS times per variant,
// each in a fresh context, and when the recognizer fails it asks the page, there and then, what Cache Storage still holds and
// whether a match for the manifest finds it, so that "the kept copy is gone" can be told from "the kept copy is there and was missed".
// Uses test/rec/serve.js (its down switch drops every request by destroying the socket) and the stand-in slot.
//   BROWSER=webkit PORT=8782 TRIALS=6 VARIANTS=desk,phone NODE_PATH=<playwright> node test/engines/offline_repeat.js
const pw = require('playwright'); const http = require('http');
const ENGINE = process.env.BROWSER || 'webkit', PORT = process.env.PORT || 8782, ORIGIN = 'http://127.0.0.1:' + PORT, SLOT = 'test/rec/models/standin';
const TRIALS = +(process.env.TRIALS || 6), VARIANTS = (process.env.VARIANTS || 'desk,phone').split(',');
const ctl = (q) => new Promise((res, rej) => http.get(ORIGIN + '/__ctl?' + q, (r) => { let b = ''; r.on('data', (d) => b += d); r.on('end', () => { try { res(JSON.parse(b)); } catch (e) { res(b); } }); }).on('error', rej));
const about = (page) => page.evaluate(() => { const a = window.__seenBack.rec.about(); return { state: a.state, why: a.why, fail: a.fail, loadMs: a.loadMs }; }).catch((e) => ({ error: String(e.message).slice(0, 120) }));
async function until(page, ms, ok) { const t0 = Date.now(); let a; while (Date.now() - t0 < ms) { a = await about(page); if (ok(a)) return Object.assign(a, { atMs: Date.now() - t0 }); await page.waitForTimeout(200); } return Object.assign(a || {}, { atMs: Date.now() - t0, timeout: true }); }
const look = (page, slot) => page.evaluate(async (slot) => {
  const man = new URL(slot + '/manifest.json', location.href).href, o = {};
  try { o.cacheNames = await caches.keys(); } catch (e) { o.cacheNames = 'threw ' + e; }
  try { const c = await caches.open('keep-v1'), ks = await c.keys(); o.keep = ks.length; o.keepHasManifest = ks.some((q) => q.url === man); o.matchKeep = !!(await c.match(man)); } catch (e) { o.keep = 'threw ' + e; }
  try { o.matchAny = !!(await caches.match(man)); } catch (e) { o.matchAny = 'threw ' + e; }
  try { const r = await fetch(slot + '/manifest.json', { cache: 'no-cache' }); o.refetch = r.status + ' ' + r.type; } catch (e) { o.refetch = 'failed: ' + e; }
  o.controlled = !!(navigator.serviceWorker && navigator.serviceWorker.controller);
  return o;
}, slot).catch((e) => ({ error: String(e.message).slice(0, 160) }));
(async () => {
  const out = { engine: ENGINE, trials: [] };
  const browser = await pw[ENGINE].launch(); out.version = browser.version();
  for (const variant of VARIANTS) for (let t = 0; t < TRIALS; t++) {
    const T = { variant, trial: t, errors: [] };
    let ctx;
    try {
      await ctl('reset=1');
      ctx = await browser.newContext(variant === 'phone' ? pw.devices['Pixel 7'] : { viewport: { width: 390, height: 844 } });
      let page = await ctx.newPage(); page.on('pageerror', (e) => T.errors.push('first: ' + e.message.slice(0, 160)));
      await page.goto(ORIGIN + '/index.html?side=420&rec=' + SLOT);
      T.first = await until(page, 60000, (a) => a.state === 'ready' || a.state === 'failed');
      T.controlled = await page.evaluate(() => navigator.serviceWorker.ready.then(() => new Promise((r) => setTimeout(() => r(!!navigator.serviceWorker.controller), 1500))));
      T.before = await look(page, SLOT);
      await page.close();
      await ctl('reset=1'); await ctl('down=1');
      page = await ctx.newPage();
      page.on('pageerror', (e) => T.errors.push(e.message.slice(0, 160))); page.on('console', (m) => { if (m.type() === 'error') T.errors.push(m.text().slice(0, 160)); });
      try {
        await page.goto(ORIGIN + '/index.html?side=420&rec=' + SLOT, { timeout: 20000 });
        await page.evaluate(() => window.__seenBack.rec.ready().catch(() => {}));
        T.offline = await until(page, 30000, (a) => a.state === 'ready' || a.state === 'failed');
        T.asked = (await ctl('log=1')).map((x) => x.split('?')[0]);
        T.after = await look(page, SLOT);                   // the network is still down here
      } catch (e) { T.offline = { loaded: false, error: String(e.message).split('\n')[0] }; }
    } catch (e) { T.error = String(e && e.stack || e).slice(0, 400); }
    await ctl('reset=1').catch(() => {}); if (ctx) await ctx.close().catch(() => {});
    out.trials.push(T);
    console.error(variant, t, JSON.stringify({ offline: T.offline, after: T.after, asked: T.asked, errors: T.errors }).slice(0, 600));
  }
  await browser.close();
  out.failed = out.trials.filter((x) => !x.offline || x.offline.state !== 'ready').length;
  console.log(JSON.stringify(out, null, 1));
})();
