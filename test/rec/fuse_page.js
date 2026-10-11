// The page's own answers for the cases of tools/fusion/parity.py. Needs test/rec/serve.js running (PORT says where; 8782 by default).
//   NODE_PATH=<where playwright lives> node test/rec/fuse_page.js cases.json page.json
const playwright = require('playwright'), fs = require('fs');
(async () => {
  const made = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const origin = 'http://127.0.0.1:' + (process.env.PORT || 8782);
  const browser = await playwright[process.env.BROWSER || 'chromium'].launch();
  const ready = (page) => page.waitForFunction(() => window.__seenBack && window.__seenBack.rec.about().state === 'ready', null, { timeout: 60000 });
  const out = { cases: [], photos: {} };
  {
    const page = await browser.newPage();
    await page.goto(origin + '/index.html?side=420&nosw=1&rec=test/rec/models/standin'); await ready(page);
    out.build = await page.evaluate(() => window.__seenBack.about().split('\n')[0]);
    // scores into the slot as loaded, or into settings handed over through the readers a real slot goes through
    out.cases = await page.evaluate((made) => {
      const rec = window.__seenBack.rec, ids = made.worlds.map((w) => rec.test.world(w.manifest, w.table, w.sb));
      return made.cases.map((c) => ('world' in c) ? rec.test.fuseIn(ids[c.world], c.kd, c.sd, c.month) : rec.fuse(c.kd, c.sd, c.month));
    }, made);
    await page.close();
  }
  if (made.photos) {     // the trained-head slot, from a photo's pixels to the answer
    const page = await browser.newPage();
    await page.goto(origin + '/index.html?side=420&nosw=1&rec=' + made.photos.slot); await ready(page);
    for (const name of made.photos.names) {
      out.photos[name] = await page.evaluate(async (name) => {
        const rec = window.__seenBack.rec; rec.wantPre = true;
        const bmp = await createImageBitmap(await (await fetch('test/rec/photos/' + name)).blob());
        const c = document.createElement('canvas'); c.width = bmp.width; c.height = bmp.height; c.getContext('2d').drawImage(bmp, 0, 0);
        const r = await rec.recognize(c, null);
        return { month: r.month, emb: Array.from(rec.lastEmb), kd: Array.from(rec.lastDots.kinds), sd: Array.from(rec.lastDots.species),
          result: { kind: r.kind, kindP: r.kindP, sure: r.sure, kinds: r.kinds, kindOffers: r.kindOffers, species: r.species, named: r.named, offers: r.offers } };
      }, name);
    }
    out.trained = await page.evaluate(() => { const a = window.__seenBack.rec.about(); return { model: a.model, rule: a.rule, trained: a.trained }; });
    await page.close();
  }
  fs.writeFileSync(process.argv[3], JSON.stringify(out));
  console.log(out.build + ' ' + out.cases.length + ' answers from the page, ' + Object.keys(out.photos).length + ' photos through ' + JSON.stringify(out.trained || null));
  await browser.close();
})().catch((e) => { console.error('FAILED', e); process.exit(1); });
