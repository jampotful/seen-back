// What happens in one engine when the page is reloaded while the larger model is being downloaded (check_rec.js "large" stopped there
// in WebKit on Linux and macOS, runs engines/33: after the reload the download never reached "kept" in 60 s).
//   BROWSER=webkit PORT=8782 BIG_PORT=8788 NODE_PATH=<playwright> node test/engines/resume_probe.js > out.json
// Needs test/rec/serve.js on PORT and on BIG_PORT with "cors" (the stand-in's parts are named at 127.0.0.1:8788).
// Prints one JSON object: the state before the reload, then once a second for 45 s after it (the larger model's about(), its choice,
// the page's diag lines about it, and what the parts' server was asked), and the console.
const pw = require('playwright'), http = require('http'), path = require('path');
const NAME = process.env.BROWSER || 'webkit', PORT = +(process.env.PORT || 8782), BIG_PORT = +(process.env.BIG_PORT || 8788);
const ORIGIN = 'http://127.0.0.1:' + PORT, BIG = 'http://127.0.0.1:' + BIG_PORT;
const get = (u) => new Promise((res, rej) => http.get(u, (r) => { let b = ''; r.on('data', (d) => b += d); r.on('end', () => { try { res(JSON.parse(b)); } catch (e) { res(b); } }); }).on('error', rej));
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
(async () => {
  const out = { browser: NAME, console: [], before: null, after: [] };
  // REF (the run branch's name) chooses a variant: "persist" uses a persistent context (a profile on disk, as Safari has) instead of
  // Playwright's ephemeral one; "halt" stops the download and lets it settle before the reload, so that no fetch is in flight then.
  const REF = process.env.GITHUB_REF_NAME || process.env.VARIANT || '', PERSIST = /persist/.test(REF), HALT = /halt/.test(REF);
  out.variant = { ref: REF, persist: PERSIST, halt: HALT }; out.trace = [];
  let browser = null, ctx;
  if (PERSIST) { const dir = require('fs').mkdtempSync(require('os').tmpdir() + '/resume-'); ctx = await pw[NAME].launchPersistentContext(dir, { viewport: { width: 390, height: 844 }, hasTouch: true }); }
  else { browser = await pw[NAME].launch(); out.version = browser.version(); }
  try {
    await get(ORIGIN + '/__ctl?reset=1'); await get(BIG + '/__ctl?reset=1'); await get(BIG + '/__ctl?slow=part01&bps=50000');
    if (!PERSIST) ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, hasTouch: true });
    const page = PERSIST ? (ctx.pages()[0] || await ctx.newPage()) : await ctx.newPage();
    // Every call the page makes to Cache Storage, with its result and its caller, as console lines "KT {...}" (they survive the reload)
    const trace = () => {
      if (!window.Cache || window.__kt) return; window.__kt = 1;
      const pid = Math.random().toString(36).slice(2, 6), ids = new WeakMap(); let seq = 0, nc = 0;
      const cid = (c) => { if (!c || typeof c !== 'object') return 0; if (!ids.has(c)) ids.set(c, ++nc); return ids.get(c); };
      const short = (u) => String(u && u.url || u).replace(/^https?:\/\/[^\/]+\//, '').replace(/^test\/rec\/models\//, '').replace(/[0-9a-f]{64}/, (m) => m.slice(0, 8));
      const who = () => (new Error().stack || '').split('\n').slice(3, 8).map((l) => { l = l.trim().replace(/^at /, ''); const name = l.split(/[@ ]/)[0] || '?', pos = /:(\d+):(\d+)\)?$/.exec(l); return name + (pos ? ':' + pos[1] + ':' + pos[2] : ''); }).join(' < ');
      const log = (o) => { try { console.debug('KT ' + JSON.stringify(Object.assign({ p: pid, t: Math.round(performance.now()) }, o))); } catch (e) {} };
      const sum = (name, v) => name === 'keys' ? (v || []).map(short).filter((u) => /big|manifest/.test(u)) : name === 'open' ? 'cache#' + cid(v) : name === 'match' ? (v ? 'hit ' + (v.headers.get('content-length') || '?') : 'miss') : v;
      const wrap = (proto, name, kind) => {
        const f = proto && proto[name]; if (!f) return;
        proto[name] = function (...a) {
          const u = a.length ? short(a[0]) : '', quiet = (name === 'match' || name === 'put') && !/standin-big/.test(u), n = ++seq;
          if (!quiet) log({ n, op: kind + (kind === 'cache' ? '#' + cid(this) : '') + '.' + name, u, opt: a[1] && name !== 'put' ? a[1] : undefined, by: who() });
          let r; try { r = f.apply(this, a); } catch (e) { log({ n, ph: 'throw', e: e.name + ' ' + e.message }); throw e; }
          return Promise.resolve(r).then((v) => { if (!quiet) log({ n, ph: 'ok', v: sum(name, v) }); return v; }, (e) => { log({ n, ph: 'err', op: name, u, e: (e && e.name) + ' ' + (e && e.message) }); throw e; });
        };
      };
      ['put', 'match', 'delete', 'keys', 'add', 'addAll', 'matchAll'].forEach((m) => wrap(Cache.prototype, m, 'cache'));
      ['open', 'match', 'delete', 'keys', 'has'].forEach((m) => wrap(CacheStorage.prototype, m, 'caches'));
      log({ op: 'document', u: location.href.replace(/^.*\?/, '?').slice(0, 80) });
      addEventListener('pagehide', () => log({ op: 'pagehide' })); addEventListener('beforeunload', () => log({ op: 'beforeunload' }));
    };
    await page.addInitScript(trace);
    page.on('console', (m) => { const x = m.text(); if (/^KT /.test(x)) { if (out.trace.length < 1500) out.trace.push(x.slice(3, 600)); return; } out.console.push(m.type() + ': ' + x.slice(0, 200)); });
    page.on('pageerror', (e) => out.console.push('pageerror: ' + String(e.message).slice(0, 200)));
    const noCamera = () => { if (!navigator.mediaDevices) return; const no = () => Promise.reject(new DOMException('Permission denied', 'NotAllowedError'));
      for (const o of [navigator.mediaDevices, window.MediaDevices && MediaDevices.prototype]) { if (o) try { Object.defineProperty(o, 'getUserMedia', { value: no, configurable: true, writable: true }); } catch (e) {} } };
    await page.addInitScript(noCamera);
    await page.goto(ORIGIN + '/index.html?side=420&svc=off&nosw=1&rec=test/rec/models/standin&big=test/rec/models/standin-big', { waitUntil: 'load' });
    await page.waitForFunction(() => window.__seenBack && window.__seenBack.rec.about().state === 'ready', null, { timeout: 60000 });
    await page.evaluate(noCamera); await page.locator('#btnBegin').click(); await page.waitForSelector('#askAnimal', { state: 'visible', timeout: 8000 });
    await page.locator('#inAnimalPick').setInputFiles(path.join(__dirname, '..', 'rec', 'photos', 'stripes.png'));
    await page.waitForSelector('#svcView', { state: 'visible', timeout: 15000 }); await page.locator('#svcView').click();
    await page.waitForSelector('#big', { state: 'visible', timeout: 8000 }); await page.locator('#bigYes').click();
    await page.waitForFunction(() => window.__seenBack.big.about().keptBytes > 300000, null, { timeout: 30000 });
    const now = () => page.evaluate(() => { const B = window.__seenBack, a = B.big.about(); return { t: Math.round(performance.now()), ready: document.readyState, have: a.have, kept: a.keptBytes, state: a.state, why: a.why, fail: a.fail, getFail: a.getFail, choice: B.bigChoice(), online: navigator.onLine,
      diag: B.diag().filter((d) => /^large/.test(d.what)).slice(-4).map((d) => d.what + ' ' + String(d.code).slice(0, 120)), line: (document.getElementById('svcView').hidden ? '' : document.getElementById('svcView').textContent) || (document.getElementById('svcHud').hidden ? '' : document.getElementById('svcHud').textContent) }; });
    out.before = await now(); out.asked = await get(BIG + '/__ctl?log=1');
    if (HALT) {        // no fetch in flight at the reload: stopped, settled, and the choice set back to 'yes' so that the next visit carries on
      await page.evaluate(() => window.__seenBack.big.halt());
      for (let i = 0; i < 20; i++) { await sleep(250); if (await page.evaluate(() => window.__seenBack.big.about().have !== 'getting')) break; }
      await sleep(1000); out.halted = await now();
      await page.evaluate(() => localStorage.setItem('seenback.large.v1', 'yes'));
    }
    out.keysBefore = await page.evaluate(async () => (await (await caches.open('keep-v1')).keys()).map((q) => q.url.replace(/^.*standin-big\//, '').replace(/[0-9a-f]{64}/, 'SHA')).filter((u) => !/^http/.test(u)));
    const t0 = Date.now(); await page.reload(); out.reloadMs = Date.now() - t0;
    for (let i = 0; i < 45; i++) {
      await sleep(1000);
      try { const s = await now(); s.at = Math.round((Date.now() - t0) / 1000); out.after.push(s); if (s.have === 'kept' && s.state === 'ready') break; } catch (e) { out.after.push({ error: String(e.message).split('\n')[0] }); }
    }
    out.askedAfter = await get(BIG + '/__ctl?log=1');
    out.kept = await page.evaluate(async () => (await (await caches.open('keep-v1')).keys()).map((q) => q.url.replace(/^.*standin-big\//, '').replace(/[0-9a-f]{64}/, 'SHA')).filter((u) => !/^http/.test(u)));
    out.stores = await page.evaluate(async () => { const o = {}; for (const n of await caches.keys()) o[n] = (await (await caches.open(n)).keys()).map((q) => q.url.replace(/^https?:\/\/[^\/]+\//, '').replace(/[0-9a-f]{64}/, 'SHA')).filter((u) => /big/.test(u)); return o; });
  } catch (e) { out.error = String(e && e.stack || e).slice(0, 600); }
  await (browser || ctx).close().catch(() => {});
  console.log(JSON.stringify(out, null, 1));
  process.exit(0);
})();
