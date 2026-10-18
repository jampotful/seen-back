// The recognizer's runtime alone in one browser (test/engines/ffbench.html), case after case, each in a fresh page of one browser.
//   BROWSER=firefox|chromium HEADED=1 PREFS='{"javascript.options.wasm_baselinejit":false}' SITE=http://127.0.0.1:8790/ OUT=out
//   CASES='pocket:all:5 big:all:2:wb'  (model:optimization level:runs[:wb (the page's way: the runtime's bytes handed over)][:t<threads>])
// Writes OUT/ffbench-<LABEL>.json and prints one line a case.
const fs = require('fs'), path = require('path');
const OUT = process.env.OUT || 'out', SITE = (process.env.SITE || 'http://127.0.0.1:8790/').replace(/\/?$/, '/'), NAME = process.env.BROWSER || 'firefox';
const LABEL = process.env.LABEL || NAME, PREFS = JSON.parse(process.env.PREFS || '{}'), CASES = (process.env.CASES || 'pocket:all:3').trim().split(/\s+/);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), LABEL, ...a);
fs.mkdirSync(OUT, { recursive: true });
const R = { label: LABEL, browser: NAME, prefs: PREFS, headed: process.env.HEADED === '1', cases: [] };
const save = () => fs.writeFileSync(path.join(OUT, 'ffbench-' + LABEL + '.json'), JSON.stringify(R, null, 1));
(async () => {
  const pw = require('playwright');
  const o = { headless: process.env.HEADED !== '1' };
  if (NAME === 'firefox') o.firefoxUserPrefs = PREFS;
  if (NAME === 'chromium') o.args = ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'];
  const br = await pw[NAME].launch(o); R.version = br.version(); const ctx = await br.newContext();
  for (const c of CASES) {
    const [model, opt, reps, ...flags] = c.split(':');
    const th = (flags.find((f) => /^t\d+$/.test(f)) || 't1').slice(1);
    const url = SITE + 'test/engines/ffbench.html?model=' + model + '&opt=' + opt + '&reps=' + reps + '&threads=' + th + (flags.includes('wb') ? '&wb=1' : '');
    const t0 = Date.now(), one = { case: c, url };
    const page = await ctx.newPage(); page.on('pageerror', (e) => (one.notes = (one.notes || []).concat(String(e.message).slice(0, 200))));
    page.on('console', (m) => { if (m.type() === 'error') one.notes = (one.notes || []).concat('console: ' + m.text().slice(0, 200)); });
    try {
      await page.goto(url, { waitUntil: 'load', timeout: 60000 });
      const lim = model === 'big' ? 1500000 : 600000; let last = null;
      while (Date.now() - t0 < lim) { await sleep(2000); last = await page.evaluate(() => window.__ff); if (last && last.done) break; }
      Object.assign(one, last || {}, { wallMs: Date.now() - t0, timedOut: !(last && last.done) });
    } catch (e) { one.error = String(e.message || e).split('\n')[0].slice(0, 300); }
    await page.close().catch(() => {});
    R.cases.push(one); save();
    const t = (one.result && one.result.t) || {};
    log(c, '| fetch', t.fetch, 'ms | session', t.session, 'ms | runs', JSON.stringify(t.runs), 'ms | head', JSON.stringify(one.result && one.result.head), 'sum', one.result && one.result.sum, '| error', one.error || '', one.timedOut ? 'TIMED OUT' : '');
  }
  const F = (R.cases[0] && R.cases[0].features) || {};
  log('version', R.version, '| features', JSON.stringify(F));
  await br.close().catch(() => {}); save(); process.exit(0);
})().catch((e) => { R.error = String(e && e.stack || e).slice(0, 800); save(); console.log(R.error); process.exit(1); });
