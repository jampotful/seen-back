// The service worker and a 5xx: a first visit keeps everything, then the server answers 502 to every request (as a proxy, a captive
// portal or a CDN having a bad moment does; WebKit also hands a proxy's refused CONNECT to the page as a 502, live run 30), and a
// second visit opens the page. Unpatched, the worker passes the 502 on and the app does not open; with
// ci/engines/patches/sw-5xx-kept.patch it serves the kept copy. Needs coi_serve.js with OLD and NEW ports (ci/engines/sw5xx.sh).
//   BROWSERS=chromium,firefox,webkit OLD=8795 NEW=8796 OUT=out/sw5xx NODE_PATH=<playwright> node test/engines/sw5xx.js
const pw = require('playwright'), fs = require('fs'), path = require('path'), http = require('http');
const OUT = process.env.OUT || 'out/sw5xx', BROWSERS = (process.env.BROWSERS || 'chromium').split(','), PORTS = { unpatched: process.env.OLD || 8795, patched: process.env.NEW || 8796 };
const HERON = fs.readFileSync('test/rec/photos/heron.png').toString('base64');
fs.mkdirSync(OUT, { recursive: true });
const get = (u) => new Promise((res) => http.get(u, (r) => { let b = ''; r.on('data', (d) => b += d); r.on('end', () => res(b)); }).on('error', (e) => res('error ' + e.message)));
const race = (p, ms, v) => Promise.race([p, new Promise((r) => setTimeout(() => r(v), ms))]);
(async () => {
  for (const name of BROWSERS) {
    const out = { browser: name, runs: {} }; const browser = await pw[name].launch(); out.version = browser.version();
    for (const [tree, port] of Object.entries(PORTS)) {
      const R = { console: [] }, O = 'http://127.0.0.1:' + port; let ctx;
      try {
        await get(O + '/__bad?on=0');
        ctx = await browser.newContext({ viewport: { width: 390, height: 844 } });
        let page = await ctx.newPage();
        await page.goto(O + '/index.html?side=420', { waitUntil: 'load', timeout: 60000 });
        R.first = await page.evaluate(() => Promise.race([window.__seenBack.rec.ready().then(() => 'ready', (e) => 'failed ' + (e && e.code)), new Promise((r) => setTimeout(() => r('waiting after 90 s'), 90000))]));
        R.controlled = await page.evaluate(() => navigator.serviceWorker.ready.then(() => new Promise((r) => setTimeout(() => r(!!navigator.serviceWorker.controller), 1500))));
        await page.close();
        R.bad = await get(O + '/__bad?on=1');
        page = await ctx.newPage(); page.on('console', (m) => { if (m.type() === 'error') R.console.push(m.text().slice(0, 200)); });
        const resp = await page.goto(O + '/index.html?side=420', { waitUntil: 'domcontentloaded', timeout: 30000 }).catch((e) => { R.gotoError = String(e.message).split('\n')[0]; return null; });
        R.status = resp && resp.status(); R.fromServiceWorker = resp ? resp.fromServiceWorker() : null;
        await page.waitForTimeout(1500);
        R.app = await page.evaluate(() => !!window.__seenBack).catch(() => false);
        if (R.app) R.second = await page.evaluate(async (b64) => {
          const rec = window.__seenBack.rec, st = await Promise.race([rec.ready().then(() => 'ready', (e) => 'failed ' + (e && e.code) + ' ' + (e && e.detail)), new Promise((r) => setTimeout(() => r('waiting after 60 s'), 60000))]);
          const o = { ready: st };
          if (st === 'ready') { const bin = atob(b64), u = new Uint8Array(bin.length); for (let i = 0; i < bin.length; i++) u[i] = bin.charCodeAt(i); const f = new File([u], 'heron.png', { type: 'image/png' }), bmp = await createImageBitmap(f), c = document.createElement('canvas'); c.width = bmp.width; c.height = bmp.height; c.getContext('2d').drawImage(bmp, 0, 0); const x = await rec.recognize(c, f); o.kind = x.kind; o.runMs = x.ms && x.ms.run; }
          return o;
        }, HERON).catch((e) => ({ error: String(e.message).split('\n')[0] }));
      } catch (e) { R.error = String(e && e.message || e).split('\n')[0]; }
      await get(O + '/__bad?on=0'); if (ctx) await ctx.close().catch(() => {});
      out.runs[tree] = R; console.log(name, tree, JSON.stringify(R).slice(0, 400));
    }
    await browser.close(); fs.writeFileSync(path.join(OUT, 'sw5xx-' + name + '.json'), JSON.stringify(out, null, 1));
  }
})();
