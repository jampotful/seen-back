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
  const browser = await pw[NAME].launch(); out.version = browser.version();
  try {
    await get(ORIGIN + '/__ctl?reset=1'); await get(BIG + '/__ctl?reset=1'); await get(BIG + '/__ctl?slow=part01&bps=50000');
    const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, hasTouch: true });
    const page = await ctx.newPage();
    page.on('console', (m) => out.console.push(m.type() + ': ' + m.text().slice(0, 200)));
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
    const t0 = Date.now(); await page.reload(); out.reloadMs = Date.now() - t0;
    for (let i = 0; i < 45; i++) {
      await sleep(1000);
      try { const s = await now(); s.at = Math.round((Date.now() - t0) / 1000); out.after.push(s); if (s.have === 'kept' && s.state === 'ready') break; } catch (e) { out.after.push({ error: String(e.message).split('\n')[0] }); }
    }
    out.askedAfter = await get(BIG + '/__ctl?log=1');
    out.kept = await page.evaluate(async () => (await (await caches.open('keep-v1')).keys()).map((q) => q.url.replace(/^.*standin-big\//, '').replace(/[0-9a-f]{64}/, 'SHA')).filter((u) => !/^http/.test(u)));
  } catch (e) { out.error = String(e && e.stack || e).slice(0, 600); }
  await browser.close().catch(() => {});
  console.log(JSON.stringify(out, null, 1));
  process.exit(0);
})();
