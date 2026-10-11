// Two of check_rec.js's cases, taken apart for engines where that script cannot finish them (WebKit), with a timeline of the
// recognizer's state. Uses test/rec/serve.js (port 8782) and the stand-in slot.
//   BROWSER=webkit PORT=8782 NODE_PATH=<playwright> node test/engines/rec_probe.js
//  1. offline: a first visit with the service worker; then the server drops every request (no Playwright offline switch, which
//     WebKit cannot take with a service worker) and a new tab opens the page: does it load, and does the recognizer start from kept
//     copies? This is the question of whether a worker's requests (importScripts, ORT's import of its .mjs) pass the service worker.
//  2. a kept model that is not a model: the bytes in Cache Storage replaced; the page reloaded; how the state moves.
const pw = require('playwright'); const http = require('http'); const path = require('path'); const fs = require('fs');
const ENGINE = process.env.BROWSER || 'webkit', PORT = process.env.PORT || 8782, ORIGIN = 'http://127.0.0.1:' + PORT, SLOT = 'test/rec/models/standin';
const ctl = (q) => new Promise((res, rej) => http.get(ORIGIN + '/__ctl?' + q, (r) => { let b = ''; r.on('data', (d) => b += d); r.on('end', () => res(JSON.parse(b))); }).on('error', rej));
const about = (page) => page.evaluate(() => { const a = window.__seenBack.rec.about(); return { state: a.state, why: a.why, fail: a.fail, loadMs: a.loadMs, got: a.got }; }).catch((e) => ({ error: String(e.message).slice(0, 120) }));
async function timeline(page, ms, until) { const t0 = Date.now(), out = []; let last = ''; while (Date.now() - t0 < ms) { const a = await about(page), k = JSON.stringify(a); if (k !== last) { out.push([Date.now() - t0, a]); last = k; } if (until && until(a)) break; await page.waitForTimeout(250); } return out; }
(async () => {
  const out = { engine: ENGINE };
  const browser = await pw[ENGINE].launch(); out.version = browser.version();
  try {
    await ctl('reset=1');
    const ctx = await browser.newContext({ viewport: { width: 390, height: 844 } });
    let page = await ctx.newPage(); const errs = []; page.on('pageerror', (e) => errs.push(e.message)); page.on('console', (m) => { if (m.type() === 'error') errs.push(m.text().slice(0, 200)); });
    await page.goto(ORIGIN + '/index.html?side=420&rec=' + SLOT);
    out.firstReady = await timeline(page, 60000, (a) => a.state === 'ready' || a.state === 'failed');
    out.controlled = await page.evaluate(() => navigator.serviceWorker.ready.then(() => new Promise((r) => setTimeout(() => r(!!navigator.serviceWorker.controller), 1500))));
    out.kept = await page.evaluate(async () => (await (await caches.open('keep-v1')).keys()).map((q) => q.url.replace(location.origin + '/', '')));
    out.swKept = await page.evaluate(async () => { const n = await caches.keys(); const o = {}; for (const k of n) o[k] = (await (await caches.open(k)).keys()).length; return o; });
    await page.close();
    // 1. offline, by the server dropping every request
    await ctl('reset=1'); await ctl('down=1');
    page = await ctx.newPage(); page.on('pageerror', (e) => errs.push(e.message)); page.on('console', (m) => { if (m.type() === 'error') errs.push(m.text().slice(0, 200)); });
    try {
      await page.goto(ORIGIN + '/index.html?side=420&rec=' + SLOT, { timeout: 20000 });
      out.offline = { loaded: true, controlled: await page.evaluate(() => !!navigator.serviceWorker.controller) };
      await page.evaluate(() => window.__seenBack.rec.ready().catch(() => {}));
      out.offline.timeline = await timeline(page, 45000, (a) => a.state === 'ready' || a.state === 'failed');
      out.offline.asked = (await ctl('log=1')).map((x) => x.split('?')[0]).filter((x, i, a) => a.indexOf(x) === i);
    } catch (e) { out.offline = { loaded: false, error: String(e.message).split('\n')[0] }; }
    await ctl('reset=1'); await page.close();
    // 2. a kept model that is not a model
    page = await ctx.newPage();
    await page.goto(ORIGIN + '/index.html?side=420&nosw=1&rec=' + SLOT);
    await timeline(page, 60000, (a) => a.state === 'ready' || a.state === 'failed');
    await page.evaluate(async () => { const c = await caches.open('keep-v1'), k = (await c.keys()).filter((q) => /onnx/.test(q.url))[0], n = (await (await c.match(k)).arrayBuffer()).byteLength; await c.put(k, new Response(new Uint8Array(n).fill(7))); });
    await page.reload();
    out.keptBad = await timeline(page, 45000, (a) => a.state === 'failed');
    out.errors = errs;
    await ctx.close();
  } catch (e) { out.error = String(e && e.stack || e).slice(0, 600); }
  await browser.close();
  console.log(JSON.stringify(out, null, 1));
})();
