// The live address (GitHub Pages), from a build machine, in Chromium, Firefox and WebKit:
//   OUT=out BROWSERS=chromium,firefox,webkit SITE=https://jampotful.github.io/seen-back/ NODE_PATH=<playwright> node test/engines/live.js
// For each browser: the page loads; the service worker registers and takes control; crossOriginIsolated; the recognizer's
// state (a slot at models/pocket/ or "no slot yet"), and when there is one, a few photos through it; then visits with the network
// cut at the proxy below (WebKit three times), each waiting for the recognizer to start from kept copies and naming a photo. Writes OUT/live-<browser>.json and screenshots. Response headers are read with curl by ci/engines/live.sh.
const pw = require('playwright');
const fs = require('fs'), path = require('path');
const OUT = process.env.OUT || 'out', SITE = (process.env.SITE || 'https://jampotful.github.io/seen-back/').replace(/\/?$/, '/');
const BROWSERS = (process.env.BROWSERS || 'chromium,webkit').split(',').filter(Boolean);
const PHOTOS = ['test/rec/photos/heron.png', 'test/rec/photos/portrait.jpg', 'test/rec/photos/wall.png', 'test/rec/photos/garden.jpg'];
fs.mkdirSync(OUT, { recursive: true });
// Every browser goes through this little proxy, so that "no network" can be made the same way for all three engines (Playwright's
// offline switch fails in WebKit once a service worker is involved): when it is down, open tunnels are cut and new ones refused.
const net = require('net'); const PROXY_PORT = +(process.env.PROXY_PORT || 8799); const proxy = { down: false, socks: new Set(), refused: 0, tunnels: 0 };
const proxyServer = require('http').createServer((q, s) => { s.writeHead(405); s.end(); });
proxyServer.on('connect', (req, sock, head) => {
  if (proxy.down) { proxy.refused++; sock.end('HTTP/1.1 502 Bad Gateway\r\n\r\n'); return; }
  const [h, p] = req.url.split(':'); proxy.tunnels++;
  const up = net.connect(+p || 443, h, () => { sock.write('HTTP/1.1 200 Connection Established\r\n\r\n'); if (head && head.length) up.write(head); up.pipe(sock); sock.pipe(up); });
  proxy.socks.add(sock); proxy.socks.add(up);
  const done = () => { proxy.socks.delete(sock); proxy.socks.delete(up); sock.destroy(); up.destroy(); };
  up.on('error', done); sock.on('error', done); up.on('close', done); sock.on('close', done);
});
const setDown = (d) => { proxy.down = d; if (d) for (const x of proxy.socks) x.destroy(); };
const HERON = fs.readFileSync('test/rec/photos/heron.png').toString('base64');
const offlineRecognize = (page) => page.evaluate(async (b64) => {
  const rec = window.__seenBack && window.__seenBack.rec; if (!rec) return { error: 'no recognizer' };
  const t0 = performance.now(); const st = await Promise.race([rec.ready().then(() => 'ready', (e) => 'failed: ' + (e && e.code) + ' ' + (e && (e.sentence || e.detail))), new Promise((r) => setTimeout(() => r('still waiting after 90 s'), 90000))]);
  const o = { ready: st, readyMs: Math.round(performance.now() - t0), about: rec.about() };
  if (st === 'ready') {
    const bin = atob(b64), u = new Uint8Array(bin.length); for (let i = 0; i < bin.length; i++) u[i] = bin.charCodeAt(i);
    const file = new File([u], 'heron.png', { type: 'image/png' }), bmp = await createImageBitmap(file), c = document.createElement('canvas'); c.width = bmp.width; c.height = bmp.height; c.getContext('2d').drawImage(bmp, 0, 0);
    const t = performance.now(), x = await rec.recognize(c, file); o.photo = { kind: x.kind, p: +x.kinds[0].p.toFixed(3), species1: x.species[0] ? [x.species[0].sci, +x.species[0].p.toFixed(3)] : null, ms: x.ms, wall: Math.round(performance.now() - t) };
  }
  return o;
}, HERON).catch((e) => ({ error: String(e.message).split('\n')[0] }));
const kept = (page) => page.evaluate(async () => { const o = {}; for (const k of await caches.keys()) { const c = await caches.open(k), ks = await c.keys(); o[k] = ks.map((q) => q.url.replace(location.origin, '')); } return o; }).catch((e) => ({ error: String(e.message).slice(0, 200) }));
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const shot = (page, f, r) => page.screenshot({ path: path.join(OUT, f), scale: 'css', timeout: 10000 }).then(() => r.shots.push(f), (e) => r.notes.push(f + ': ' + String(e.message).split('\n')[0]));

async function one(name) {
  const r = { browser: name, site: SITE, shots: [], notes: [], console: [], pageErrors: [] };
  const browser = await pw[name].launch(Object.assign({ proxy: { server: 'http://127.0.0.1:' + PROXY_PORT } }, name === 'chromium' ? { args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] } : {}));
  r.version = browser.version();
  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, hasTouch: true, isMobile: name === 'chromium' });
  try {
    let page = await ctx.newPage();
    page.on('console', (m) => { if (m.type() === 'error' || m.type() === 'warning') r.console.push(m.type() + ': ' + m.text().slice(0, 240)); });
    page.on('pageerror', (e) => r.pageErrors.push(String(e.message).slice(0, 240)));
    const tNav = Date.now();
    const resp = await page.goto(SITE, { waitUntil: 'load', timeout: 45000 });
    r.loadEventMs = Date.now() - tNav;
    r.readyFromNav = await page.evaluate(() => window.__seenBack && window.__seenBack.rec ? Promise.race([window.__seenBack.rec.ready().then(() => 'ready', (e) => 'failed: ' + (e && e.code)), new Promise((res) => setTimeout(() => res('still waiting after 120 s'), 120000))]) : 'no recognizer').catch((e) => 'error: ' + e.message);
    r.readyFromNavMs = Date.now() - tNav;
    r.first = { status: resp && resp.status(), headers: resp && resp.headers() };
    await page.waitForTimeout(5000);
    await shot(page, 'live-' + name + '-1-first.png', r);
    r.first.page = await page.evaluate(async () => {
      const b = window.__seenBack, reg = navigator.serviceWorker ? await navigator.serviceWorker.getRegistration() : null;
      return { build: b && b.about ? b.about().split('\n')[0] : '', screen: b && b.S.screen, engine: b && b.state(), coi: !!window.crossOriginIsolated, secure: window.isSecureContext,
        swSupported: 'serviceWorker' in navigator, swRegistered: !!reg, swActive: !!(reg && reg.active), swState: reg && reg.active ? reg.active.state : null, controlled: !!(navigator.serviceWorker && navigator.serviceWorker.controller),
        rec: b && b.rec ? b.rec.about() : null, serif: document.fonts ? document.fonts.check('400 20px "Instrument Serif"') : null };
    });
    // the recognizer: a slot under models/pocket/, or none yet
    const man = await page.evaluate(async () => { try { const x = await fetch('models/pocket/manifest.json', { cache: 'no-store' }); return { status: x.status, text: x.ok ? (await x.text()).slice(0, 4000) : '' }; } catch (e) { return { error: String(e) }; } });
    r.slot = man.status === 200 ? 'present' : man.status === 404 ? 'no slot yet' : 'unknown: ' + JSON.stringify(man).slice(0, 200);
    if (man.status === 200) {
      try { r.manifest = JSON.parse(man.text); } catch (e) { r.manifest = 'not JSON'; }
      const t0 = Date.now();
      r.ready = await page.evaluate(() => Promise.race([window.__seenBack.rec.ready().then(() => 'ready', (e) => 'failed: ' + (e && e.code) + ' ' + (e && e.sentence) + ' ' + (e && e.detail)), new Promise((res) => setTimeout(() => res('still waiting after 60 s'), 60000))])).catch((e) => 'error: ' + e.message);
      r.readyMs = Date.now() - t0; r.about = await page.evaluate(() => window.__seenBack.rec.about());
      if (r.ready === 'ready') r.photos = await page.evaluate(async (list) => {
        const out = [];
        for (const u of list) {
          try {
            const blob = await (await fetch(u)).blob(), name = u.split('/').pop(), file = new File([blob], name, { type: blob.type });
            const bmp = await createImageBitmap(file), c = document.createElement('canvas'); c.width = bmp.width; c.height = bmp.height; c.getContext('2d').drawImage(bmp, 0, 0);
            const t = performance.now(), x = await window.__seenBack.rec.recognize(c, file);
            out.push({ name, kind: x.kind, kinds3: x.kinds.slice(0, 3).map((k) => [k.key, +k.p.toFixed(3)]), species1: x.species[0] ? [x.species[0].sci, +x.species[0].p.toFixed(3)] : null, ms: x.ms, wall: Math.round(performance.now() - t) });
          } catch (e) { out.push({ name: u, error: (e && e.sentence) || String(e) }); }
        }
        return out;
      }, PHOTOS);
    }
    r.kept = await kept(page);
    // a second visit, in a new tab (a reload under a service worker sometimes never reports "load" to Playwright)
    await page.close();
    page = await ctx.newPage();
    try {
      const resp1 = await page.goto(SITE, { waitUntil: 'domcontentloaded', timeout: 30000 }); await page.waitForTimeout(2500);
      r.second = await page.evaluate(() => ({ controlled: !!(navigator.serviceWorker && navigator.serviceWorker.controller), screen: window.__seenBack && window.__seenBack.S.screen }));
      r.second.fromServiceWorker = resp1 ? resp1.fromServiceWorker() : null;
    } catch (e) { r.second = { failed: String(e.message).split('\n')[0] }; }
    // then visits with the network off (the proxy cut), each in a new tab of the same browser; WebKit three times, for the lead that
    // a later offline visit there once failed to find kept copies
    await page.close();
    setDown(true); r.offlineVisits = [];
    for (let k = 0; k < (name === 'webkit' ? 3 : 1); k++) {
      const p2 = await ctx.newPage(), o = { console: [] };
      p2.on('console', (m) => { if (m.type() === 'error' || m.type() === 'warning') o.console.push(m.type() + ': ' + m.text().slice(0, 240)); }); p2.on('pageerror', (e) => o.console.push('pageerror: ' + String(e.message).slice(0, 240)));
      try {
        const resp2 = await p2.goto(SITE, { waitUntil: 'domcontentloaded', timeout: 30000 });
        Object.assign(o, { status: resp2 && resp2.status(), fromServiceWorker: resp2 ? resp2.fromServiceWorker() : null });
        await p2.waitForTimeout(2000);
        Object.assign(o, await p2.evaluate(() => ({ online: navigator.onLine, controlled: !!(navigator.serviceWorker && navigator.serviceWorker.controller), screen: window.__seenBack && window.__seenBack.S.screen,
          build: window.__seenBack && window.__seenBack.about ? window.__seenBack.about().split('\n')[0] : '', rec: window.__seenBack && window.__seenBack.rec ? window.__seenBack.rec.about().state : null })));
        o.recognized = await offlineRecognize(p2);
        o.kept = await kept(p2);
      } catch (e) { o.failed = String(e.message).split('\n')[0]; }
      if (k === 0) await shot(p2, 'live-' + name + '-2-offline.png', r);
      r.offlineVisits.push(o); await p2.close().catch(() => {});
    }
    r.offline = r.offlineVisits[0]; r.proxy = { refused: proxy.refused, tunnels: proxy.tunnels };
    setDown(false);
  } catch (e) { r.error = String(e && e.stack || e).slice(0, 600); }
  await browser.close().catch(() => {});
  log(name, r.version, 'status', r.first && r.first.status, 'sw', r.first && r.first.page && r.first.page.swActive, 'second controlled', r.second && r.second.controlled, 'offline', JSON.stringify((r.offlineVisits || []).map((o) => [o.status, o.controlled, o.failed, o.recognized && o.recognized.ready, o.recognized && o.recognized.photo && o.recognized.photo.kind])).slice(0, 300), 'slot', r.slot, r.ready || '');
  fs.writeFileSync(path.join(OUT, 'live-' + name + '.json'), JSON.stringify(r, null, 1));
}
(async () => { await new Promise((res) => proxyServer.listen(PROXY_PORT, '127.0.0.1', res)); for (const b of BROWSERS) await one(b); proxyServer.close(); process.exit(0); })().catch((e) => { log('FAILED', e && e.stack || e); process.exit(1); });
