// A stand-in for the species service, speaking Gradio's two-step call as the page's client expects it (src/cam.rec.js, "naturalist"):
//   POST /gradio_api/call/identify   {"data": [photo as base64 JPEG, month 1-12, region or "", top]}  ->  {"event_id": "..."}
//   GET  /gradio_api/call/identify/<event_id>   a stream of events; "complete" carries [answer], the answer in the shape docs/CONTRACTS.md gives
//   GET  /health                     {"ok": true, "ready": true | false, "model": "...", "species": 5911}
// It names nothing: the answer is whichever canned one the check has chosen. It keeps a note of what each call carried, so that a check
// can say exactly what left the page. Used inside test/rec/check_rec.js (require and start), or by itself:
//   node test/rec/fake_service.js [port]     then GET /__ctl?reset=1 | answer=<name> | mode=<ok|error|refuse|garbled|busy> | delay=<ms> | sleep=<ms> | log=1
const http = require('http');

const ANSWERS = {
  monarch: { species: [['Danaus plexippus', 'Monarch', 'insect', 0.88, 5133088], ['Danaus gilippus', 'Queen', 'insect', 0.07, 5133091], ['Dione vanillae', 'Gulf Fritillary', 'insect', 0.02, 1], ['Limenitis archippus', 'Viceroy', 'insect', 0.01, 2], ['Junonia coenia', 'Common Buckeye', 'insect', 0.005, 3], ['Papilio glaucus', 'Eastern Tiger Swallowtail', 'insect', 0.001, 4]], kinds: [['insect', 0.99], ['bee', 0.004]] },
  egret: { species: [['Ardea alba', 'Great Egret', 'wader', 0.91, 9752617], ['Egretta thula', 'Snowy Egret', 'wader', 0.05, 5], ['Bubulcus ibis', 'Cattle Egret', 'wader', 0.02, 6], ['Eudocimus albus', 'White Ibis', 'wader', 0.005, 7], ['Mycteria americana', 'Wood Stork', 'wader', 0.002, 8]], kinds: [['wader', 0.97], ['bird', 0.02]] },
  unsure: { species: [['Ardea alba', 'Great Egret', 'wader', 0.55, 9752617], ['Dryophytes cinereus', 'Green Treefrog', 'frog', 0.2, 9], ['Egretta thula', 'Snowy Egret', 'wader', 0.05, 5]], kinds: [['wader', 0.62], ['frog', 0.3]] },
  faint: { species: [['Danaus plexippus', 'Monarch', 'insect', 0.2, 5133088], ['Danaus gilippus', 'Queen', 'insect', 0.18, 5133091], ['Dione vanillae', 'Gulf Fritillary', 'insect', 0.15, 1]], kinds: [['insect', 0.8]] },
};
function jpegSize(buf) {                                     // width and height from the JPEG's own frame header, or null if it is not a JPEG
  if (buf.length < 4 || buf[0] !== 0xff || buf[1] !== 0xd8) return null;
  let o = 2;
  while (o + 9 < buf.length) {
    if (buf[o] !== 0xff) return null;
    const m = buf[o + 1], len = buf.readUInt16BE(o + 2);
    if (m >= 0xc0 && m <= 0xcf && m !== 0xc4 && m !== 0xc8 && m !== 0xcc) return { h: buf.readUInt16BE(o + 5), w: buf.readUInt16BE(o + 7) };
    o += 2 + len;
  }
  return null;
}
function start(port) {
  const S = { answer: 'monarch', mode: 'ok', delay: 0, asleepUntil: 0, log: [], jobs: {}, n: 0, health: 0 };
  const allowed = (origin) => /^http:\/\/(127\.0\.0\.1|localhost)(:\d+)?$/.test(origin || '') || origin === 'https://jampotful.github.io';
  const server = http.createServer((req, res) => {
    const u = new URL(req.url, 'http://x'), origin = req.headers.origin, asleep = Date.now() < S.asleepUntil;
    const cors = allowed(origin) ? { 'Access-Control-Allow-Origin': origin, 'Vary': 'Origin' } : {};
    const json = (code, obj, extra) => { res.writeHead(code, Object.assign({ 'Content-Type': 'application/json', 'Cache-Control': 'no-store' }, cors, extra || {})); res.end(JSON.stringify(obj)); };
    if (u.pathname === '/__ctl') {
      const q = u.searchParams;
      if (q.has('reset')) { S.answer = 'monarch'; S.mode = 'ok'; S.delay = 0; S.asleepUntil = 0; S.log = []; S.health = 0; }
      if (q.has('answer')) S.answer = q.get('answer');
      if (q.has('mode')) S.mode = q.get('mode');
      if (q.has('delay')) S.delay = +q.get('delay');
      if (q.has('sleep')) S.asleepUntil = Date.now() + +q.get('sleep');
      res.writeHead(200, { 'Content-Type': 'application/json' }); res.end(JSON.stringify(q.has('log') ? { calls: S.log, health: S.health } : { ok: true })); return;
    }
    if (req.method === 'OPTIONS') {                             // the browser asks first whether a JSON POST from this page is welcome
      if (asleep) { res.writeHead(503, { 'Content-Type': 'text/html' }); res.end('<h1>This Space is sleeping</h1>'); return; }
      res.writeHead(204, Object.assign({ 'Access-Control-Allow-Methods': 'GET, POST, OPTIONS', 'Access-Control-Allow-Headers': 'content-type', 'Access-Control-Max-Age': '600' }, cors)); res.end(); return;
    }
    if (u.pathname === '/health') { S.health++; json(200, { ok: true, ready: !asleep, model: 'fake-naturalist', species: 5911 }); return; }
    if (asleep) { res.writeHead(503, { 'Content-Type': 'text/html' }); res.end('<h1>This Space is sleeping</h1>'); return; }   // as a sleeping host answers: no JSON, and nothing a browser may read
    if (req.method === 'POST' && u.pathname === '/gradio_api/call/identify') {
      const chunks = [];
      req.on('data', (d) => chunks.push(d));
      req.on('end', () => {
        const raw = Buffer.concat(chunks); let d = null, note = { at: Date.now(), bytes: raw.length, origin: origin || '', cookie: req.headers.cookie || '', referer: req.headers.referer || '', type: req.headers['content-type'] || '', auth: req.headers.authorization || '' };
        try { d = JSON.parse(raw.toString('utf8')).data; } catch (e) { d = null; }
        if (Array.isArray(d) && typeof d[0] === 'string') {
          const img = Buffer.from(d[0], 'base64'), size = jpegSize(img);
          Object.assign(note, { fields: d.length, jpeg: !!size, w: size ? size.w : 0, h: size ? size.h : 0, imageBytes: img.length, month: d[1], region: d[2], top: d[3], prefix: d[0].slice(0, 5) === 'data:' });
        }
        S.log.push(note);
        if (S.mode === 'refuse') { json(403, { detail: 'This page may not ask.' }); return; }
        if (S.mode === 'busy') { json(429, { detail: 'Too many questions just now.' }); return; }
        if (!note.jpeg || note.w > 512 || note.h > 512 || note.imageBytes >= 1e6 || !(note.month >= 1 && note.month <= 12)) { json(422, { detail: 'Not a small JPEG with a month.' }); return; }
        const id = 'e' + (++S.n) + Math.random().toString(36).slice(2, 8);
        S.jobs[id] = { mode: S.mode, answer: S.answer, delay: S.delay, region: d[2], top: d[3] };
        json(200, { event_id: id });
      });
      return;
    }
    const m = /^\/gradio_api\/call\/identify\/([A-Za-z0-9]+)$/.exec(u.pathname);
    if (req.method === 'GET' && m && S.jobs[m[1]]) {
      const job = S.jobs[m[1]]; delete S.jobs[m[1]];
      res.writeHead(200, Object.assign({ 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-store', 'Connection': 'keep-alive' }, cors));
      const beat = setInterval(() => res.write('event: heartbeat\ndata: null\n\n'), 400);
      res.write('event: heartbeat\ndata: null\n\n');
      setTimeout(() => {
        clearInterval(beat);
        if (job.mode === 'error') res.end('event: error\ndata: null\n\n');
        else if (job.mode === 'garbled') res.end('event: complete\ndata: this is not JSON\n\n');
        else if (job.mode === 'refusal') res.end('event: complete\ndata: ' + JSON.stringify([{ error: 'That is not a photo this service will look at.' }]) + '\n\n');
        else {
          const a = ANSWERS[job.answer] || ANSWERS.monarch;
          const out = { model: 'fake-naturalist', region: job.region || '', ms: job.delay, species: a.species.slice(0, job.top || 5).map((s) => ({ key: s[4], sci: s[0], en: s[1], eyes: s[2], p: s[3] })), kinds: a.kinds.map((k) => ({ key: k[0], p: k[1] })) };
          const text = 'event: complete\ndata: ' + JSON.stringify([out]) + '\n\n', half = text.length >> 1;
          res.write(text.slice(0, half)); setTimeout(() => res.end(text.slice(half)), 30);      // in two pieces, as a network may deliver it
        }
      }, job.delay);
      return;
    }
    json(404, { detail: 'Not found.' });
  });
  return new Promise((resolve) => server.listen(port, '127.0.0.1', () => resolve({
    port, server, state: S,
    reset() { S.answer = 'monarch'; S.mode = 'ok'; S.delay = 0; S.asleepUntil = 0; S.log = []; S.health = 0; },
    set(o) { Object.assign(S, o); }, sleep(ms) { S.asleepUntil = Date.now() + ms; }, calls() { return S.log.slice(); }, close() { server.close(); },
  })));
}
module.exports = { start, ANSWERS };
if (require.main === module) start(+(process.argv[2] || process.env.SVC_PORT || 8784)).then((f) => console.log('fake species service on http://127.0.0.1:' + f.port));
