// Run the page's own self-test (?selftest=1) in Playwright browsers and keep what it reports.
// Serve the repository root first (ci/engines/serve.py), then:
//   PORT=8781 OUT=out BROWSERS=chromium,firefox,webkit VIEWPORTS=phone,desktop NODE_PATH=<playwright> node test/engines/run.js
// Writes OUT/<browser>-<viewport>.json and screenshots (PNG; the workflow shrinks them), and prints one line per run.
const pw = require('playwright');
const fs = require('fs');
const path = require('path');
const PORT = process.env.PORT || 8781;
const OUT = process.env.OUT || 'out';
const BASE = 'http://127.0.0.1:' + PORT + '/index.html';
const EXTRA = process.env.EXTRA || '';                     // e.g. &side=420
const BROWSERS = (process.env.BROWSERS || 'chromium').split(',').filter(Boolean);
const VIEWPORTS = (process.env.VIEWPORTS || 'phone,desktop').split(',').filter(Boolean);
const LABEL = process.env.LABEL || process.platform;
const LIMIT = +(process.env.LIMIT_MS || 180000);
const HEADED = process.env.HEADED === '1', TAGX = process.env.TAG || '';
fs.mkdirSync(OUT, { recursive: true });
const log = (...a) => { const s = new Date().toISOString().slice(11, 19) + ' ' + a.join(' '); console.log(s); fs.appendFileSync(path.join(OUT, 'run-log.txt'), s + '\n'); };
const VP = {
  phone: { viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true },
  desktop: { viewport: { width: 1280, height: 800 }, deviceScaleFactor: 1, isMobile: false, hasTouch: false },
};
const GL_ARGS = ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--autoplay-policy=no-user-gesture-required',
  '--use-fake-device-for-media-stream', '--use-fake-ui-for-media-stream'];
const FF_PREFS = { 'media.navigator.streams.fake': true, 'media.navigator.permission.disabled': true, 'webgl.force-enabled': true, 'media.autoplay.default': 0,
  'media.autoplay.blocking_policy': 0 };

function launchOpts(name) {
  if (name === 'chromium') return { headless: !HEADED, args: process.env.CHROMIUM_ARGS ? process.env.CHROMIUM_ARGS.split(' ') : GL_ARGS };
  if (name === 'firefox') return { headless: !HEADED, firefoxUserPrefs: FF_PREFS };
  return { headless: !HEADED };
}
// Firefox and WebKit do not take Playwright's isMobile
function ctxOpts(name, vp) { const o = Object.assign({}, VP[vp]); if (name === 'firefox') delete o.isMobile; return o; }

async function watchPage(page, rec) {
  page.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') rec.console.push(m.type() + ': ' + m.text().slice(0, 300)); });
  page.on('pageerror', e => rec.pageErrors.push(String(e && e.message || e).slice(0, 300)));
  page.on('requestfailed', r => rec.failedRequests.push(r.url().replace(BASE.replace('/index.html', ''), '') + ' ' + (r.failure() && r.failure().errorText)));
}
const shot = async (page, file, rec) => { try { await page.screenshot({ path: path.join(OUT, file), scale: 'css', timeout: 45000 }); rec.shots.push(file); } catch (e) { rec.notes.push('screenshot ' + file + ' failed: ' + String(e.message).slice(0, 160)); } };

async function one(name, vp) {
  const tag = name + TAGX + '-' + vp, rec = { headed: HEADED, browser: name + TAGX, viewport: vp, platform: LABEL, console: [], pageErrors: [], failedRequests: [], shots: [], notes: [] };
  const t0 = Date.now();
  let browser;
  try { browser = await pw[name].launch(launchOpts(name)); } catch (e) { rec.launchError = String(e.message).slice(0, 600); log(tag, 'launch failed', rec.launchError.split('\n')[0]); return rec; }
  rec.version = browser.version();
  try {
    const ctx = await browser.newContext(ctxOpts(name, vp));
    // 1. the opening screen, as a person first sees it
    {
      const page = await ctx.newPage(); await watchPage(page, rec);
      await page.goto(BASE, { waitUntil: 'load', timeout: 30000 });
      await page.waitForTimeout(3500);
      await shot(page, tag + '-1-open.png', rec);
      rec.openState = await page.evaluate(() => ({ screen: window.__seenBack && window.__seenBack.S.screen, engine: window.__seenBack && window.__seenBack.state(),
        fine: (document.getElementById('introFine') || {}).textContent, begin: !(document.getElementById('btnBegin') || {}).disabled,
        serif: document.fonts ? document.fonts.check('400 20px "Instrument Serif"') : null })).catch(e => ({ error: String(e.message).slice(0, 200) }));
      if (name === 'chromium') {
        try {
          const cdp = await ctx.newCDPSession(page);
          rec.installability = (await cdp.send('Page.getInstallabilityErrors')).installabilityErrors;
          const man = await cdp.send('Page.getAppManifest').catch(e => ({ error: e.message }));
          rec.manifest = { url: man.url, errors: man.errors, bytes: man.data ? man.data.length : 0 };
        } catch (e) { rec.installability = 'CDP failed: ' + String(e.message).slice(0, 200); }
      }
      rec.serviceWorker = await page.evaluate(async () => {
        if (!('serviceWorker' in navigator)) return { supported: false };
        const t = Date.now();
        const reg = await Promise.race([navigator.serviceWorker.ready, new Promise(r => setTimeout(() => r(null), 8000))]);
        return { supported: true, ready: !!reg, active: !!(reg && reg.active), state: reg && reg.active ? reg.active.state : null, scope: reg ? reg.scope : null, ms: Date.now() - t };
      }).catch(e => ({ error: String(e.message).slice(0, 200) }));
      await page.close();
    }
    // 2. the self-test
    {
      const page = await ctx.newPage(); await watchPage(page, rec);
      const url = BASE + '?selftest=1&nosw=1&report=/report/' + tag + EXTRA;
      rec.url = url;
      await page.goto(url, { waitUntil: 'load', timeout: 30000 });
      const seen = {}; let T = null; const tS = Date.now();
      while (Date.now() - tS < LIMIT) {
        T = await page.evaluate(() => window.__selftest ? { phase: window.__selftest.phase, posing: window.__selftest.posing, done: window.__selftest.done } : null).catch(() => null);
        if (T && T.phase === 'still' && !seen.still && Date.now() - tS > 1500) { seen.still = 1; await page.waitForTimeout(600); await shot(page, tag + '-2-still.png', rec); }
        if (T && T.phase === 'motion' && !seen.motion) { seen.motion = 1; await page.waitForTimeout(1500); await shot(page, tag + '-3-motion.png', rec); }
        if (T && T.posing === 'cat@0.45' && !seen.cat) { seen.cat = 1; await page.waitForTimeout(250); await shot(page, tag + '-4-pose-cat.png', rec); }
        if (T && T.posing === 'bee@0.45' && !seen.bee) { seen.bee = 1; await page.waitForTimeout(250); await shot(page, tag + '-5-pose-bee.png', rec); }
        if (T && T.done) break;
        await page.waitForTimeout(250);
      }
      rec.selftestMs = Date.now() - tS;
      rec.selftest = await page.evaluate(() => window.__selftest).catch(e => ({ error: String(e.message).slice(0, 200) }));
      if (!rec.selftest || !rec.selftest.done) rec.notes.push('self-test did not finish within ' + LIMIT + ' ms (phase ' + (T && T.phase) + ')');
      await page.waitForTimeout(400);
      await shot(page, tag + '-6-sheet.png', rec);
      await page.close();
    }
    // 3. Firefox: the live flow with its fake camera, from the opening screen to the finder
    if (name === 'firefox' && vp === 'phone') {
      const page = await ctx.newPage(); await watchPage(page, rec);
      const flow = rec.liveFlow = { steps: [] };
      try {
        await page.goto(BASE + '?nosw=1', { waitUntil: 'load', timeout: 30000 }); await page.waitForTimeout(1200);
        await page.locator('#btnBegin').click({ timeout: 8000 }); flow.steps.push('tapped Begin');
        await page.waitForFunction(() => window.__seenBack.S.src === 'cam', null, { timeout: 15000 }); flow.steps.push('camera running');
        await page.waitForSelector('#barFinder', { state: 'visible', timeout: 15000 }); flow.steps.push('finder screen shown');
        const w1 = await page.evaluate(() => window.__seenBack.state().writes); await page.waitForTimeout(2000);
        const st = await page.evaluate(() => ({ s: window.__seenBack.S.screen, src: window.__seenBack.S.src, e: window.__seenBack.state() }));
        flow.writesIn2s = st.e.writes - w1; flow.state = st;
        if (flow.writesIn2s > 0) flow.steps.push('camera frames reach the engine');
        await shot(page, tag + '-7-finder.png', rec);
        await page.locator('#btnShutter').click({ timeout: 8000 }); await page.waitForSelector('#claim', { state: 'visible', timeout: 8000 }); flow.steps.push('shutter: asked who it was');
        await page.locator('#claimName').fill('cat'); await page.locator('#claimForm button[type=submit]').click();
        await page.waitForFunction(() => window.__seenBack.S.screen === 'animal' && window.__seenBack.S.eyes === 'cat', null, { timeout: 8000 }); flow.steps.push('cat eyes on the live camera');
        await page.waitForTimeout(4000); flow.end = await page.evaluate(() => ({ k: window.__seenBack.S.k, e: window.__seenBack.state() }));
        await shot(page, tag + '-8-live-cat.png', rec);
      } catch (e) { flow.stoppedAt = String(e.message).split('\n')[0].slice(0, 200); }
      await page.close();
    }
    await ctx.close();
  } catch (e) { rec.error = String(e && e.stack || e).slice(0, 800); }
  await browser.close().catch(() => {});
  rec.wallMs = Date.now() - t0;
  const T = rec.selftest || {};
  log(tag, rec.version || '', 'done=' + T.done, 'ok=' + T.ok, 'fails=' + (T.fails ? T.fails.length : '-'), 'checks=' + T.checks, 'webgl2=' + (T.env && T.env.webgl2), 'float=' + (T.env && T.env.floatOK), (T.env && (T.env.unmaskedRenderer || T.env.renderer)) || '', rec.wallMs + 'ms');
  fs.writeFileSync(path.join(OUT, tag + '.json'), JSON.stringify(rec, null, 1));
  return rec;
}

(async () => {
  const all = [];
  for (const b of BROWSERS) for (const v of VIEWPORTS) all.push(await one(b, v));
  const brief = all.map(r => {
    const T = r.selftest || {}, E = T.env || {}, M = (T.motion && T.motion.runs) || {};
    const pick = (size) => { const xs = Object.keys(M).filter(k => k.startsWith(size + ' ')).map(k => M[k]); if (!xs.length) return null;
      return { ms: Math.round(xs.reduce((a, x) => a + (x.ms || 0), 0) / xs.length * 10) / 10, worst: Math.max.apply(null, xs.map(x => x.worst || 0)) }; };
    return { browser: r.browser, viewport: r.viewport, platform: r.platform, version: r.version, launchError: r.launchError, done: T.done, ok: T.ok, checks: T.checks, fails: T.fails,
      webgl2: E.webgl2, floatOK: E.floatOK, renderer: E.unmaskedRenderer || E.renderer, engineError: E.engineError, side0: T.motion && T.motion.side0,
      frame_default: pick('default'), frame_540: pick('540'), video: T.motion && T.motion.video, serif: E.serif, pageErrors: r.pageErrors, consoleCount: r.console.length,
      installability: r.installability, serviceWorker: r.serviceWorker, liveFlow: r.liveFlow, notes: r.notes, selftestMs: r.selftestMs, totalMs: T.ms && T.ms.total };
  });
  fs.writeFileSync(path.join(OUT, 'selftest-summary.json'), JSON.stringify(brief, null, 1));
})().catch(e => { log('FAILED', e && e.stack || e); process.exit(1); });
