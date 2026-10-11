// The self-test in real Safari, through safaridriver (WebDriver). Start `safaridriver -p 4444` first.
//   PORT=8781 OUT=out node test/engines/safari.js
// Writes OUT/safari-desktop.json and screenshots. Needs Node 18 or later (global fetch).
const fs = require('fs');
const path = require('path');
const PORT = process.env.PORT || 8781, OUT = process.env.OUT || 'out', WD = process.env.WD || 'http://127.0.0.1:4444';
const BASE = 'http://127.0.0.1:' + PORT + '/index.html';
fs.mkdirSync(OUT, { recursive: true });
const rec = { browser: 'safari', viewport: 'desktop', platform: 'macos', shots: [], notes: [], steps: [] };
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
async function wd(method, p, body) {
  const r = await fetch(WD + p, { method, headers: { 'Content-Type': 'application/json' }, body: body ? JSON.stringify(body) : undefined });
  const j = await r.json().catch(() => ({}));
  if (!r.ok || (j.value && j.value.error)) throw new Error((j.value && (j.value.error + ': ' + j.value.message)) || ('HTTP ' + r.status));
  return j.value;
}
const sleep = ms => new Promise(r => setTimeout(r, ms));
// what is really on the screen, beside what WebDriver's screenshot returns (it may leave out a WebGL canvas)
const { execFileSync } = require('child_process');
function screen(name) { try { execFileSync('screencapture', ['-x', path.join(OUT, name)], { timeout: 15000 }); rec.shots.push(name); } catch (e) { rec.notes.push('screencapture ' + name + ': ' + String(e.message).split('\n')[0].slice(0, 160)); } }
(async () => {
  let sid = null;
  try {
    const s = await wd('POST', '/session', { capabilities: { alwaysMatch: { browserName: 'safari' } } });
    sid = s.sessionId; rec.version = s.capabilities && s.capabilities.browserVersion; rec.steps.push('session ' + rec.version);
    log('session', sid, rec.version);
    const shot = async (name) => { try { const b = await wd('GET', `/session/${sid}/screenshot`); fs.writeFileSync(path.join(OUT, name), Buffer.from(b, 'base64')); rec.shots.push(name); } catch (e) { rec.notes.push('screenshot ' + name + ': ' + e.message); } };
    const js = (script) => wd('POST', `/session/${sid}/execute/sync`, { script, args: [] });
    try { await wd('POST', `/session/${sid}/window/rect`, { width: 1280, height: 860, x: 0, y: 0 }); } catch (e) { rec.notes.push('window size: ' + e.message); }
    await wd('POST', `/session/${sid}/url`, { url: BASE }); await sleep(3500); await shot('safari-desktop-1-open.png'); screen('safari-desktop-1-open-screen.png');
    rec.openState = await js('return {screen: window.__seenBack && window.__seenBack.S.screen, engine: window.__seenBack && window.__seenBack.state(), serif: document.fonts ? document.fonts.check(\'400 20px "Instrument Serif"\') : null, sw: !!navigator.serviceWorker}').catch(e => ({ error: e.message }));
    rec.steps.push('opening screen');
    await wd('POST', `/session/${sid}/url`, { url: BASE + '?selftest=1&nosw=1&report=/report/safari-desktop' });
    const t0 = Date.now(), seen = {};
    let T = null;
    while (Date.now() - t0 < 240000) {
      T = await js('return window.__selftest ? {phase: window.__selftest.phase, posing: window.__selftest.posing, done: window.__selftest.done} : null').catch(() => null);
      if (T && T.phase === 'still' && !seen.still) { seen.still = 1; await shot('safari-desktop-2-still.png'); }
      if (T && T.phase === 'motion' && !seen.motion) { seen.motion = 1; await sleep(1200); await shot('safari-desktop-3-motion.png'); screen('safari-desktop-3-motion-screen.png'); }
      if (T && T.posing === 'cat@0.45' && !seen.cat) { seen.cat = 1; await shot('safari-desktop-4-pose-cat.png'); screen('safari-desktop-4-pose-cat-screen.png'); }
      if (T && T.posing === 'bee@0.45' && !seen.bee) { seen.bee = 1; await shot('safari-desktop-5-pose-bee.png'); }
      if (T && T.done) break;
      await sleep(300);
    }
    rec.selftestMs = Date.now() - t0;
    rec.selftest = await js('return window.__selftest').catch(e => ({ error: e.message }));
    await sleep(500); await shot('safari-desktop-6-sheet.png');
    rec.steps.push('self-test ' + (rec.selftest && rec.selftest.done ? 'finished' : 'did not finish'));
  } catch (e) { rec.error = String(e.message || e).slice(0, 600); log('error', rec.error); }
  if (sid) await wd('DELETE', `/session/${sid}`).catch(() => {});
  const T = rec.selftest || {};
  log('safari', rec.version, 'done=' + T.done, 'ok=' + T.ok, 'fails=' + (T.fails ? T.fails.length : '-'), (T.env && (T.env.unmaskedRenderer || T.env.renderer)) || '');
  fs.writeFileSync(path.join(OUT, 'safari-desktop.json'), JSON.stringify(rec, null, 1));
})();
