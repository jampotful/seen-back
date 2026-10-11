// The threads experiment's driver. Needs test/engines/coi_serve.js running (ci/engines/threads.sh starts it) with ports
// 8791 = no isolation, 8792 = the service worker adds COEP require-corp, 8793 = COEP credentialless, 8794 = the other origin.
//   BROWSERS=chromium,firefox,webkit REPORTS=out/threads NODE_PATH=<playwright> node test/engines/threads.js
//   BROWSERS=safari (safaridriver on :4444) works the same way through WebDriver.
// For each browser, each mode and each thread count it opens the real page with the probe (test/engines/coi_probe.js) in a fresh
// context and waits for the probe's final report in REPORTS/<browser>-<mode>-t<threads>.json. Writes REPORTS/threads-<browser>.json.
const fs = require('fs'), path = require('path');
const REPORTS = process.env.REPORTS || 'out/threads', BROWSERS = (process.env.BROWSERS || 'chromium').split(',').filter(Boolean);
const MODES = (process.env.MODES || 'none:8791,require-corp:8792,credentialless:8793').split(',').map((s) => s.split(':'));
const THREADS = (process.env.THREADS || '1,2,4').split(',').map(Number), ROUNDS = process.env.ROUNDS || '3', WAIT = +(process.env.WAIT_MS || 300000);
const PHOTOS = 'test/rec/photos/heron.png,test/rec/photos/portrait.jpg,test/rec/photos/wall.png,test/rec/photos/garden.jpg';
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
fs.mkdirSync(REPORTS, { recursive: true });
const url = (port, name, threads, mode) => `http://127.0.0.1:${port}/index.html?probe=1&name=${name}&threads=${threads}&want=${mode === 'none' ? '' : 'coi'}&photos=${PHOTOS}&rounds=${ROUNDS}&x=${process.env.XORIGIN || 'http://127.0.0.1:8794'}&cam=${process.env.CAM || '1'}`;
async function report(name, ms) {
  const f = path.join(REPORTS, name + '.json'), t0 = Date.now(); let last = null;
  while (Date.now() - t0 < ms) { try { last = JSON.parse(fs.readFileSync(f, 'utf8')); if (last.done) return last; } catch (e) {} await sleep(1000); }
  return Object.assign(last || {}, { timedOut: true });
}
function brief(r) {
  const runs = (r.photos || []).filter((x) => x.round > 0).map((x) => x.ms && x.ms.run).filter((x) => x > 0).sort((a, b) => a - b);
  return { coi: r.coi, controlled: r.controlled, reloads: r.reloads, ready: r.ready, readyMs: r.readyMs, threads: r.about && r.about.threads, loadMs: r.about && r.about.loadMs, start: r.about && r.about.start,
    medianRunMs: runs.length ? runs[runs.length >> 1] : null, minRunMs: runs[0] || null, n: runs.length, kinds: (r.photos || []).filter((x) => x.round === 0).map((x) => x.name + ':' + x.kind), breaks: r.breaks, error: r.error, timedOut: r.timedOut };
}
async function playwright(engine) {
  const pw = require('playwright'), out = { browser: engine, runs: {} };
  const launch = engine === 'chromium' ? { args: ['--use-fake-device-for-media-stream', '--use-fake-ui-for-media-stream'] } : engine === 'firefox' ? { firefoxUserPrefs: { 'media.navigator.streams.fake': true, 'media.navigator.permission.disabled': true } } : {};
  const browser = await pw[engine].launch(launch); out.version = browser.version();
  for (const [mode, port] of MODES) for (const th of (mode === 'none' ? [1, 4] : THREADS)) {
    const name = `${engine}-${mode}-t${th}`, errs = [];
    try { fs.unlinkSync(path.join(REPORTS, name + '.json')); } catch (e) {}
    const ctx = await browser.newContext({ viewport: { width: 390, height: 844 } });
    const page = await ctx.newPage(); page.on('console', (m) => { if (m.type() === 'error' || m.type() === 'warning') errs.push(m.type() + ': ' + m.text().slice(0, 300)); }); page.on('pageerror', (e) => errs.push('pageerror: ' + String(e.message).slice(0, 300)));
    const t0 = Date.now();
    await page.goto(url(port, name, th, mode), { waitUntil: 'domcontentloaded', timeout: 60000 }).catch((e) => errs.push('goto: ' + String(e.message).split('\n')[0]));
    const r = await report(name, WAIT);
    out.runs[name] = Object.assign(brief(r), { wallMs: Date.now() - t0, console: errs.slice(0, 12) });
    log(name, JSON.stringify(out.runs[name]).slice(0, 400));
    await ctx.close().catch(() => {});
  }
  await browser.close().catch(() => {});
  return out;
}
async function safari() {
  const WD = process.env.WD || 'http://127.0.0.1:4444', out = { browser: 'safari', runs: {} };
  const wd = async (method, p, body) => { const r = await fetch(WD + p, { method, headers: { 'Content-Type': 'application/json' }, body: body ? JSON.stringify(body) : undefined }); const j = await r.json().catch(() => ({})); if (!r.ok || (j.value && j.value.error)) throw new Error((j.value && (j.value.error + ': ' + j.value.message)) || ('HTTP ' + r.status)); return j.value; };
  for (const [mode, port] of MODES) {
    let sid = null;
    try {
      const s = await wd('POST', '/session', { capabilities: { alwaysMatch: { browserName: 'safari' } } }); sid = s.sessionId; out.version = s.capabilities && s.capabilities.browserVersion;
      for (const th of (mode === 'none' ? [1, 4] : THREADS)) {
        const name = `safari-${mode}-t${th}`, t0 = Date.now();
        try { fs.unlinkSync(path.join(REPORTS, name + '.json')); } catch (e) {}
        await wd('POST', `/session/${sid}/url`, { url: url(port, name, th, mode).replace('cam=1', 'cam=0') }).catch((e) => log('url', e.message));
        const r = await report(name, WAIT);
        out.runs[name] = Object.assign(brief(r), { wallMs: Date.now() - t0 });
        log(name, JSON.stringify(out.runs[name]).slice(0, 400));
      }
    } catch (e) { out['error-' + mode] = String(e.message || e).slice(0, 300); log('safari', mode, e.message); }
    if (sid) await wd('DELETE', `/session/${sid}`).catch(() => {});
  }
  return out;
}
(async () => {
  for (const b of BROWSERS) {
    let o; try { o = b === 'safari' ? await safari() : await playwright(b); } catch (e) { o = { browser: b, error: String(e && e.stack || e).slice(0, 600) }; }
    fs.writeFileSync(path.join(REPORTS, 'threads-' + b + '.json'), JSON.stringify(o, null, 1));
  }
})();
