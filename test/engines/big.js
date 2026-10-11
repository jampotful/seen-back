// The larger model, for real, from the live address, in one browser; the in-page work is test/engines/big_page.js.
//   BROWSER=chromium|firefox|webkit (Playwright, NODE_PATH=<playwright>) or BROWSER=safari|sim (safaridriver on WD=http://127.0.0.1:4444)
//   OUT=out PHOTOS=photos.json SITE=https://jampotful.github.io/seen-back/ node test/engines/big.js
// PHOTOS lists {name, path, type, truth}; the first is the photo that should raise the offer, the rest go through the model.
// Chromium also answers the home-screen questions (HOME=1): installability through CDP, the second visit under the service worker,
// a visit with the network cut at a proxy here, and the larger model answering with the network off.
// Writes OUT/big-<browser>.json and screenshots. Epoch times (epoch*) let ci/engines/bigsum.py find the memory peaks in mem.jsonl.
const fs = require('fs'), path = require('path'), net = require('net');
const OUT = process.env.OUT || 'out', SITE0 = process.env.SITE || 'https://jampotful.github.io/seen-back/', SITE = SITE0.includes('?') ? SITE0 : SITE0.replace(/\/?$/, '/'), NAME = process.env.BROWSER || 'chromium';
const WD = process.env.WD || 'http://127.0.0.1:4444', LIMIT = +(process.env.LIMIT_MS || 900000);
const PAGE_JS = fs.readFileSync(path.join(__dirname, 'big_page.js'), 'utf8');
const list = JSON.parse(fs.readFileSync(process.env.PHOTOS || 'photos.json', 'utf8'));
const asB64 = (p) => ({ name: p.name, type: p.type, truth: p.truth || '', b64: fs.readFileSync(p.path).toString('base64') });
const opts = { offerPhotos: [asB64(list[0])], photos: list.slice(1).map(asB64), limitMs: LIMIT };
fs.mkdirSync(OUT, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), NAME, ...a);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const r = { browser: NAME, site: SITE, notes: [], shots: [], net: [], marks: {} };
const mark = (k) => { r.marks[k] = Date.now(); };
const save = () => fs.writeFileSync(path.join(OUT, 'big-' + NAME + '.json'), JSON.stringify(r, null, 1));
// a proxy, so that the network can be cut for Chromium's offline visits (as test/engines/live.js does)
const PROXY_PORT = +(process.env.PROXY_PORT || 8811); const proxy = { down: false, socks: new Set(), refused: 0, tunnels: 0 };
const proxyServer = require('http').createServer((q, s) => {      // plain http (a page on localhost) is passed on too
  if (proxy.down) { proxy.refused++; s.writeHead(502); s.end(); return; }
  try { const u = new URL(q.url), up = require('http').request({ host: u.hostname, port: u.port || 80, path: u.pathname + u.search, method: q.method, headers: q.headers }, (ur) => { s.writeHead(ur.statusCode, ur.headers); ur.pipe(s); });
    up.on('error', () => { s.writeHead(502); s.end(); }); q.pipe(up); } catch (e) { s.writeHead(405); s.end(); }
});
proxyServer.on('connect', (req, sock, head) => {
  if (proxy.down) { proxy.refused++; sock.end('HTTP/1.1 502 Bad Gateway\r\n\r\n'); return; }
  const [h, p] = req.url.split(':'); proxy.tunnels++;
  const up = net.connect(+p || 443, h, () => { sock.write('HTTP/1.1 200 Connection Established\r\n\r\n'); if (head && head.length) up.write(head); up.pipe(sock); sock.pipe(up); });
  proxy.socks.add(sock); proxy.socks.add(up);
  const done = () => { proxy.socks.delete(sock); proxy.socks.delete(up); sock.destroy(); up.destroy(); };
  up.on('error', done); sock.on('error', done); up.on('close', done); sock.on('close', done);
});
const setDown = (d) => { proxy.down = d; if (d) for (const x of proxy.socks) x.destroy(); };

async function pollPage(evalFn, label, limitMs) {      // read window.__big until done; a dead page or tab is said as such
  const t0 = Date.now(); let last = null, fails = 0, polls = 0;
  while (Date.now() - t0 < limitMs) {
    await sleep(2000);
    try { last = await evalFn('var b = window.__seenBack, a = b && b.big ? b.big.about() : {}; return window.__big ? {done: window.__big.done, steps: window.__big.steps.slice(-1), phase: window.__big.phase, err: window.__big.error || null, now: b ? [b.S.screen, b.S.eyes, b.S.svc && b.S.svc.state, b.S.named && b.S.named.by, a.have, a.keptBytes, a.state, a.getFail].join(" | ") : "no page"} : null'); fails = 0; }
    catch (e) { fails++; r.notes.push(label + ' poll ' + String(e.message || e).split('\n')[0].slice(0, 200)); if (fails >= 5) return { died: String(e.message || e).split('\n')[0].slice(0, 300) }; continue; }
    if (++polls % 10 === 1) log(label, Math.round((Date.now() - t0) / 1000) + ' s', JSON.stringify(last).slice(0, 300));
    if (last && last.done) return { done: true };
  }
  return { timeout: true, last };
}

async function playwrightRun() {
  const pw = require('playwright');
  const isC = NAME === 'chromium', udd = fs.mkdtempSync('/tmp/big-' + NAME + '-');
  const o = Object.assign({ headless: process.env.HEADED !== '1', viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, hasTouch: true },
    isC ? { isMobile: true, proxy: { server: 'http://127.0.0.1:' + PROXY_PORT }, args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] } : {});
  let ctx, br = null;
  // WebKit refused a persistent profile on macOS (run engines/35: "Browser started with no default context"), so it gets an ordinary context
  if (NAME === 'webkit') { br = await pw.webkit.launch({ headless: o.headless }); delete o.headless; ctx = await br.newContext(o); r.context = 'new context'; }
  else { ctx = await pw[NAME].launchPersistentContext(udd, o); r.context = 'persistent profile'; }
  r.version = br ? br.version() : ctx.browser() ? ctx.browser().version() : '';
  const onResp = async (resp) => {
    const u = resp.url(); if (!/githubusercontent\.com/.test(u)) return;
    const q = resp.request(), h = resp.headers(), o = { url: u.replace(/^https:\/\/[^/]+\//, '').replace(/[0-9a-f]{40}/, 'COMMIT'), status: resp.status(), fromSW: resp.fromServiceWorker(), t: Date.now(),
      redirectedFrom: q.redirectedFrom() ? q.redirectedFrom().url() : null, h: {} };
    for (const k of ['access-control-allow-origin', 'content-encoding', 'content-length', 'content-type', 'cache-control', 'etag', 'x-cache', 'via', 'age', 'location', 'timing-allow-origin']) if (h[k] != null) o.h[k] = h[k];
    r.net.push(o);
    resp.finished().then(async () => { o.done = Date.now(); try { o.sizes = await q.sizes(); } catch (e) {} try { const t = q.timing(); o.timing = { start: t.startTime, responseStart: Math.round(t.responseStart), responseEnd: Math.round(t.responseEnd) }; } catch (e) {} }).catch((e) => { o.failed = String(e).slice(0, 200); });
  };
  ctx.on('response', onResp);
  ctx.on('requestfailed', (q) => { if (/githubusercontent\.com/.test(q.url())) r.net.push({ url: q.url().replace(/^https:\/\/[^/]+\//, ''), failed: q.failure() && q.failure().errorText, t: Date.now() }); });
  let page = ctx.pages()[0] || await ctx.newPage();
  const watch = (p, tag) => { p.on('crash', () => { r.notes.push(tag + ': the page crashed'); r.crashed = (r.crashed || []).concat(tag); }); p.on('pageerror', (e) => r.notes.push(tag + ' pageerror: ' + String(e.message).slice(0, 200)));
    p.on('console', (m) => { if (m.type() === 'error') r.notes.push(tag + ' console: ' + m.text().slice(0, 200)); }); };
  watch(page, 'first');
  const ev = (p) => (src) => p.evaluate(new Function(src));
  const shot = (p, f) => p.screenshot({ path: path.join(OUT, f), scale: 'css', timeout: 20000 }).then(() => r.shots.push(f), (e) => r.notes.push(f + ': ' + String(e.message).split('\n')[0]));
  mark('open'); await page.goto(SITE, { waitUntil: 'load', timeout: 60000 }); await sleep(1500);
  await page.evaluate(PAGE_JS); await page.evaluate((o) => window.__bigRun('get', o), opts); mark('getStarted');
  const g = await pollPage(ev(page), 'get', LIMIT + 400000); r.getPoll = g;
  r.get = await page.evaluate(() => window.__big).catch((e) => ({ error: 'could not read: ' + String(e.message).split('\n')[0] })); mark('getDone');
  await shot(page, 'big-' + NAME + '-1-after.png'); save();
  // reload: nothing may be fetched again
  const nBefore = r.net.length; mark('reload');
  try { await page.reload({ waitUntil: 'load', timeout: 60000 }); } catch (e) { r.notes.push('reload: ' + String(e.message).split('\n')[0]); }
  await sleep(1500);
  await page.evaluate(PAGE_JS); await page.evaluate((o) => window.__bigRun('again', o), opts);
  r.againPoll = await pollPage(ev(page), 'again', 420000); r.again = await page.evaluate(() => window.__big).catch((e) => ({ error: String(e.message).split('\n')[0] }));
  r.againNet = r.net.slice(nBefore); mark('againDone'); await shot(page, 'big-' + NAME + '-2-again.png'); save();
  if (isC && process.env.HOME_CHECKS !== '0') {
    const h = r.home = {};
    try {
      const cdp = await ctx.newCDPSession(page);
      h.installability = await cdp.send('Page.getInstallabilityErrors').catch((e) => ({ error: String(e.message).slice(0, 300) }));
      const m = await cdp.send('Page.getAppManifest').catch((e) => ({ error: String(e.message).slice(0, 300) }));
      h.manifest = { url: m.url, errors: m.errors, bytes: m.data ? m.data.length : 0, parsed: m.data ? (() => { try { const j = JSON.parse(m.data); return { name: j.name, short_name: j.short_name, start_url: j.start_url, scope: j.scope, display: j.display, icons: (j.icons || []).map((i) => i.sizes + ' ' + (i.purpose || '') + ' ' + i.type) }; } catch (e) { return 'not JSON'; } })() : null, error: m.error };
      try { h.appId = await cdp.send('Page.getAppId'); } catch (e) { h.appId = { error: String(e.message).slice(0, 200) }; }
    } catch (e) { h.cdpError = String(e.message).slice(0, 300); }
    // a second visit in a new tab: is it under the service worker?
    try { const p2 = await ctx.newPage(); watch(p2, 'second'); const resp = await p2.goto(SITE, { waitUntil: 'domcontentloaded', timeout: 30000 }); await sleep(2500);
      h.second = Object.assign({ status: resp && resp.status(), fromSW: resp ? resp.fromServiceWorker() : null }, await p2.evaluate(() => ({ controlled: !!(navigator.serviceWorker && navigator.serviceWorker.controller), screen: window.__seenBack && window.__seenBack.S.screen }))); await p2.close(); }
    catch (e) { h.second = { failed: String(e.message).split('\n')[0] }; }
    // the network off: the page starts, the pocket model is ready, and the larger model answers a photo
    setDown(true); mark('offline');
    try { const p3 = await ctx.newPage(); watch(p3, 'offline'); const resp = await p3.goto(SITE, { waitUntil: 'domcontentloaded', timeout: 30000 }); await sleep(2500);
      h.offline = { status: resp && resp.status(), fromSW: resp ? resp.fromServiceWorker() : null, online: await p3.evaluate(() => navigator.onLine) };
      await p3.evaluate(PAGE_JS); await p3.evaluate((o) => window.__bigRun('again', o), opts);
      h.offlinePoll = await pollPage(ev(p3), 'offline', 420000); h.offlineRun = await p3.evaluate(() => window.__big).catch((e) => ({ error: String(e.message).split('\n')[0] }));
      await shot(p3, 'big-' + NAME + '-3-offline.png'); await p3.close().catch(() => {}); }
    catch (e) { h.offline = Object.assign(h.offline || {}, { failed: String(e.message).split('\n')[0] }); }
    h.proxy = { refused: proxy.refused, tunnels: proxy.tunnels }; setDown(false); mark('offlineDone');
  }
  await ctx.close().catch(() => {}); if (br) await br.close().catch(() => {});
}

async function wd(method, p, body) {
  const res = await fetch(WD + p, { method, headers: { 'Content-Type': 'application/json' }, body: body ? JSON.stringify(body) : undefined });
  const j = await res.json().catch(() => ({}));
  if (!res.ok || (j.value && j.value.error)) throw new Error((j.value && (j.value.error + ': ' + j.value.message)) || ('HTTP ' + res.status));
  return j.value;
}
async function webdriverRun() {
  const caps = NAME === 'sim' ? { browserName: 'safari', platformName: 'iOS', 'safari:useSimulator': true } : { browserName: 'safari' };
  if (NAME === 'sim' && process.env.UDID) caps['safari:deviceUDID'] = process.env.UDID;
  let sid = null;
  try {
    const s = await wd('POST', '/session', { capabilities: { alwaysMatch: caps } }); sid = s.sessionId; r.version = s.capabilities && s.capabilities.browserVersion; r.caps = s.capabilities;
    const js = (script, args) => wd('POST', `/session/${sid}/execute/sync`, { script, args: args || [] });
    const shot = async (f) => { try { const b = await wd('GET', `/session/${sid}/screenshot`); fs.writeFileSync(path.join(OUT, f), Buffer.from(b, 'base64')); r.shots.push(f); } catch (e) { r.notes.push('screenshot ' + f + ': ' + e.message); } };
    mark('open'); await wd('POST', `/session/${sid}/url`, { url: SITE }); await sleep(3000);
    await js(PAGE_JS); await js('return window.__bigRun("get", arguments[0])', [opts]); mark('getStarted');
    r.getPoll = await pollPage(js, 'get', LIMIT + 400000);
    r.get = await js('return window.__big').catch((e) => ({ error: 'could not read: ' + e.message })); mark('getDone'); await shot('big-' + NAME + '-1-after.png'); save();
    mark('reload'); await wd('POST', `/session/${sid}/url`, { url: SITE }); await sleep(3000);
    await js(PAGE_JS); await js('return window.__bigRun("again", arguments[0])', [opts]);
    r.againPoll = await pollPage(js, 'again', 420000); r.again = await js('return window.__big').catch((e) => ({ error: e.message })); mark('againDone'); await shot('big-' + NAME + '-2-again.png');
  } catch (e) { r.error = String(e.message || e).slice(0, 600); }
  if (sid) await wd('DELETE', `/session/${sid}`).catch(() => {});
}

(async () => {
  await new Promise((res) => proxyServer.listen(PROXY_PORT, '127.0.0.1', res));
  try { if (NAME === 'safari' || NAME === 'sim') await webdriverRun(); else await playwrightRun(); } catch (e) { r.error = String(e && e.stack || e).slice(0, 800); }
  save(); proxyServer.close();
  const G = r.get || {}, A = r.again || {};
  log('version', r.version, '| path', G.path, '| ready', G.download && G.download.readyMs, 'ms | getFail', G.getFail || '', '| photos', JSON.stringify((G.photos || []).map((p) => [p.name, p.large && p.large.named, p.wallMs])).slice(0, 400),
    '| again', A.survey, A.photo && A.photo.large && A.photo.large.named, A.photo && A.photo.wallMs, '| refetched', (r.againNet || []).length, '| error', r.error || '');
  process.exit(0);
})();
