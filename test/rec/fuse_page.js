// The page's own answers for the cases of tools/fusion/parity.py. Needs test/rec/serve.js running.
//   NODE_PATH=<where playwright lives> node test/rec/fuse_page.js cases.json page.json
const playwright = require('playwright'), fs = require('fs');
(async () => {
  const cases = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await playwright[process.env.BROWSER || 'chromium'].launch();
  const page = await browser.newPage();
  await page.goto('http://127.0.0.1:' + (process.env.PORT || 8782) + '/index.html?side=420&nosw=1&rec=test/rec/models/standin');
  await page.waitForFunction(() => window.__seenBack && window.__seenBack.rec.about().state === 'ready', null, { timeout: 60000 });
  const out = await page.evaluate((cs) => cs.map((c) => window.__seenBack.rec.fuse(c.kd, c.sd, c.month)), cases);
  fs.writeFileSync(process.argv[3], JSON.stringify(out));
  console.log(out.length + ' answers from the page');
  await browser.close();
})().catch((e) => { console.error('FAILED', e); process.exit(1); });
