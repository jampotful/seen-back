// What the opening screen's Begin does in this engine, under check_rec.js's own phone emulation and without it:
//   BROWSER=webkit PORT=8782 NODE_PATH=<playwright> OUT=<dir> node test/engines/begin_probe.js
// For macOS WebKit, where every check_rec.js case stopped waiting 8 s for #askAnimal after Begin.
const pw = require('playwright'); const path = require('path'); const fs = require('fs');
const ENGINE = process.env.BROWSER || 'webkit', PORT = process.env.PORT || 8782, OUT = process.env.OUT || '.';
const URL = 'http://127.0.0.1:' + PORT + '/index.html?side=420&nosw=1&rec=test/rec/models/standin';
const noCamera = () => { if (navigator.mediaDevices) navigator.mediaDevices.getUserMedia = () => Promise.reject(new DOMException('Permission denied', 'NotAllowedError')); };
const look = (page) => page.evaluate(() => { const b = window.__seenBack, $ = (i) => document.getElementById(i);
  return { screen: b && b.S.screen, engine: b && b.state(), beginDisabled: $('btnBegin') && $('btnBegin').disabled, introFine: $('introFine') && $('introFine').textContent,
    askAnimalHidden: $('askAnimal') && $('askAnimal').hidden, msg: $('msg') && $('msg').textContent, mediaDevices: !!navigator.mediaDevices, touch: 'ontouchstart' in window, ua: navigator.userAgent.slice(0, 120) }; }).catch((e) => ({ error: e.message }));
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const out = { engine: ENGINE }, browser = await pw[ENGINE].launch(); out.version = browser.version();
  const phone = Object.assign({}, pw.devices['Pixel 7']); delete phone.userAgent; if (ENGINE === 'firefox') delete phone.isMobile;
  for (const [name, opts, how] of [['phone-tap', phone, 'tap'], ['phone-click', phone, 'click'], ['plain-click', { viewport: { width: 412, height: 839 } }, 'click']]) {
    const r = out[name] = { errors: [] };
    const ctx = await browser.newContext(opts), page = await ctx.newPage();
    page.on('pageerror', (e) => r.errors.push('pageerror: ' + e.message)); page.on('console', (m) => { if (m.type() === 'error' || m.type() === 'warning') r.errors.push(m.type() + ': ' + m.text().slice(0, 200)); });
    await page.addInitScript(noCamera);
    try {
      await page.goto(URL); await page.waitForTimeout(1500);
      r.before = await look(page);
      try { await page.locator('#btnBegin')[how]({ timeout: 5000 }); r.pressed = how; } catch (e) { r.pressed = how + ' failed: ' + e.message.split('\n')[0]; }
      await page.waitForTimeout(3000);
      r.after = await look(page);
      await page.screenshot({ path: path.join(OUT, 'begin-' + ENGINE + '-' + name + '.png'), scale: 'css' }).catch(() => {});
    } catch (e) { r.error = e.message.split('\n')[0]; }
    await ctx.close();
  }
  await browser.close();
  console.log(JSON.stringify(out, null, 1));
})();
