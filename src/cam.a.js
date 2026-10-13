  'use strict';
  var $ = function (id) { return document.getElementById(id); };

  // ---------- where is this running?
  // Inside Claude's viewer the camera is normally refused, and only there can Claude name a photo.
  var inViewer = !!(window.claude && typeof window.claude.use === 'function');
  var hasCamera = !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);
  var coarse = !!(window.matchMedia && window.matchMedia('(pointer: coarse)').matches);
  var calm = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var BUILD = '27';
  // Sharpness is drawn against the viewer's own eye: the long side of the screen is taken to fill
  // this many degrees of their view (a phone at arm's length, a laptop on a desk). An assumption.
  var VIEW_DEG = coarse ? 24 : 34;
  var HUMAN_CPD = 60;

  // ---------- the eyes, as data (module 0, docs/ENGINE-DESIGN.md section 3)
  // Every view is a spec in views/<key>.json, inlined here by build.py, so the page makes no request for them. A spec's numbers are
  // parameter objects ({ value, grade, invented, src }); viewOf turns a spec into the flat view the engine reads, as EYES held before.
  // rows: [grade, title, text, sources]. m = measured in this animal, g = measured in a relative or a wider group, i = a guess,
  // x = left out. Specs with "offered": true are the views the app offers; the rest are reached only with ?try=<key>.
  var I3 = [1, 0, 0, 0, 1, 0, 0, 0, 1];
  var SPECS = /*@SPECS@*/{};
  var LIGHT = { lum: 0, raw: 0, col: [0, 0, 0], dir: [.5, .5], shock: 0, at: 0, reads: 0, cells: null };   // written by the light module (src/cam.b.js)
  var FLOOR = /*@FLOOR@*/{};   // docs/views/floor.json: the smallest visible change of each parameter, by view
  function isParam(x) { return !!x && typeof x === 'object' && !Array.isArray(x) && x.hasOwnProperty('grade') && (x.hasOwnProperty('value') || x.hasOwnProperty('curve')); }
  function specValue(x, spec, mats, key) {
    if (typeof x === 'string' && x.charAt(0) === '@') return specValue(spec.params[x.slice(1)], spec, mats, x.slice(1));
    if (key === 'M' && typeof x === 'string') { var m = mats[x] || (spec.matrices || {})[x]; return m && m.rows && m.rows.length === 3 ? [].concat.apply([], m.rows).slice(0, 9).length === 9 && m.rows.every(function (r) { return r.length === 3; }) ? [].concat.apply([], m.rows) : m.rows.map(function (r) { return r.slice(0, 3); }).reduce(function (a, r) { return a.concat(r); }, []) : I3.slice(); }
    if (isParam(x)) return x.hasOwnProperty('value') ? specValue(x.value, spec, mats, key) : specCurve(x);
    if (Array.isArray(x)) return x.map(function (v) { return specValue(v, spec, mats, key); });
    if (x && typeof x === 'object') { var o = {}, k; for (k in x) o[k] = specValue(x[k], spec, mats, k); return o; }
    return x;
  }
  // A value given against a measured input ({ curve: 'lux', points: [[x, v], ...] }) is interpolated in the logarithm of light, x being
  // log10 of the light module's relative level (LIGHT.lum, 0 to 1 of the camera's exposure; absolute light needs the exposure time, which
  // most browsers do not report). Before the first reading it takes the first point. The page recomputes such a view twice a second.
  function specCurve(p) {
    var P = p.points || []; if (!P.length) return 0;
    if (!LIGHT.reads) return P[0][1];
    var x = Math.log(Math.max(LIGHT.lum, 1e-3)) / Math.LN10, i;
    if (x <= P[0][0]) return P[0][1];
    for (i = 1; i < P.length; i++) if (x <= P[i][0]) return P[i - 1][1] + (P[i][1] - P[i - 1][1]) * (x - P[i - 1][0]) / (P[i][0] - P[i - 1][0]);
    return P[P.length - 1][1];
  }
  function viewOf(spec) {
    var mats = spec.matrices || {}, v = { chip: spec.chip, who: spec.who, cue: spec.cue }, k, g;
    for (k in spec.params) v[k] = specValue(spec.params[k], spec, mats, k);
    if (spec.zones) v.zones = specValue(spec.zones, spec, mats, 'zones');
    if (spec.gaze) v.gaze = specValue(spec.gaze, spec, mats, 'gaze');
    if (spec.draw) v.draw = spec.draw;
    if (spec.inputs && spec.inputs.senses) v.senses = specValue(spec.inputs.senses, spec, mats, 'senses');
    if (spec.by && spec.by.genus) { v.byGenus = {}; for (g in spec.by.genus) v.byGenus[g] = specValue(spec.by.genus[g], spec, mats, g); }
    v.rows = (spec.rows || []).map(function (r) { return r.slice(0, 3); });
    return v;
  }
  var EYES = {}, TRY = {};
  Object.keys(SPECS).forEach(function (k) { SPECS[k].hasCurve = JSON.stringify(SPECS[k]).indexOf('"curve"') >= 0; (SPECS[k].offered ? EYES : TRY)[k] = viewOf(SPECS[k]); });
  var ORDER = ['cat', 'dog', 'squirrel', 'deer', 'rabbit', 'wader', 'bird', 'hawk', 'alligator', 'reptile', 'frog', 'bee', 'insect', 'plant'];
  // Groups the app can name and cannot yet view the world as (docs/COVERAGE.md, decided by the owner on 12 October 2026).
  // A photo or a typed name in one of them gets the notice that Regards can't view the world as that creature yet, and no
  // encounter is kept. A group moves into EYES when its view is drawn from its sheet (docs/views/sheets/).
  var GROUPS = { fungus: 'a fungus', slime: 'a slime mould', spider: 'a spider', jumper: 'a jumping spider', fish: 'a fish', shark: 'a shark or ray',
    snail: 'a snail or slug', sealife: 'a sea creature', crab: 'a crustacean', salamander: 'a salamander or newt', worm: 'a worm, millipede or centipede',
    scorpion: 'a scorpion or harvestman', tick: 'a tick', mammal: 'a mammal', primate: 'a monkey or ape', whale: 'a whale, dolphin or seal',
    bat: 'a bat', flyingfox: 'a flying fox', cephalopod: 'an octopus or squid' };
  function noView(key) { return key === 'other' || (!!GROUPS[key] && !EYES[key]); }
  function noViewOrPerson(key) { return key === 'person' || noView(key); }   // neither becomes a view, and neither is kept as an encounter

  // ---------- views being tried: reached only with ?try=<key> (several with ?try=a,b), offered nowhere else yet. They are the specs
  // without "offered" (above). A view tried joins EYES for that visit only, so a photo or a typed name in its group then opens it too.
  var TRY_KEYS = ((/[?&]try=([a-z,]+)/.exec(location.search || '') || [0, ''])[1]).split(',').filter(function (k) { return TRY.hasOwnProperty(k); });
  if (/[?&]selftest=1(?:&|$)/.test(location.search || '') && !TRY_KEYS.length) TRY_KEYS = Object.keys(TRY);   // the self-test draws them all
  TRY_KEYS.forEach(function (k) { EYES[k] = TRY[k]; });
  // The tuning panel and the compare slider (src/cam.tune.js) appear only with ?try=<view>&tune=1. &draw=<option> picks one of the
  // drawing options a view offers (docs/views/ATLAS.md), the first being the default. cmp is the compare divider's place, 0 when hidden.
  var TUNE = { on: TRY_KEYS.length > 0 && /[?&]tune=1(?:&|$)/.test(location.search || ''), cmp: 0,
    draw: ((/[?&]draw=([a-z]+)/.exec(location.search || '') || [0, ''])[1]) };

  function clamp(x, a, b) { return x < a ? a : x > b ? b : x; }
  function lerp(a, b, t) { return a + (b - a) * t; }
  function ease(t) { t = clamp(t, 0, 1); return t * t * (3 - 2 * t); }
  var SHAPES = { whole: 0, strip: 1, ellipse: 2, annulus: 3, band: 4, cross: 5 };
  // A zone's size is a fraction of the camera picture's long side (size: [half width, half height]), or degrees of the world (deg: [width,
  // height]), taking the long side of a phone camera's picture to span CAM_DEG degrees. An assumption: main cameras span about 60 to 70.
  var CAM_DEG = 64;
  // A zone states only what differs from its view; everything it leaves out is the view's own value (docs/ENGINE.md).
  function zoneOf(z, P) {
    var at = z.at || [.5, .5], size = z.deg ? [z.deg[0] / 2 / CAM_DEG, z.deg[1] / 2 / CAM_DEG] : z.size || [.5, .5];
    var tilt = z.tilt || [0, 0];
    return { id: z.id || '', shape: SHAPES[z.shape] || 0, cx: at[0], cy: at[1], hw: size[0], hh: size[1], inner: z.inner || 0, soft: z.soft === undefined ? .04 : z.soft,
      rot: (z.rot || 0) * Math.PI / 180, gaze: z.gaze ? +z.gaze || 1 : 0, frac: z.frac || null, tiltU: tilt[0] * Math.PI / 180, tiltD: tilt[1] * Math.PI / 180, gap: (z.gap || 0) / CAM_DEG, tip: z.tip === undefined ? 1 : z.tip,
      inv: z.cpd ? 1 / z.cpd : P.inv, M: z.M || P.M, sat: z.sat === undefined ? P.sat : z.sat, gain: z.gain || P.gain, gate: z.gate === undefined ? P.gate : z.gate,
      rate: z.rate || P.rate, glow: z.glow === undefined ? P.glow : z.glow, living: z.living === undefined ? P.living : z.living,
      uv: z.uv === undefined ? P.uvBlue : z.uv, uvR: z.uvR === undefined ? P.uvR : z.uvR, sheen: z.sheen === undefined ? P.sheen : z.sheen, mag: z.mag || 1 };
  }
  var ZNUM = ['inv', 'sat', 'gain', 'gate', 'glow', 'living', 'uv', 'uvR', 'sheen', 'mag'];
  function neutralZone(z, P) {                     // the same place and shape, drawn as the other view would draw it there
    var o = {}, k; for (k in z) o[k] = z[k];
    o.inv = P.inv; o.M = P.M; o.sat = P.sat; o.gain = P.gain; o.gate = P.gate; o.rate = P.rate; o.glow = P.glow; o.living = P.living; o.uv = P.uvBlue; o.uvR = P.uvR; o.sheen = P.sheen; o.mag = 1;
    return o;
  }
  function withGenus(m, named) {                  // a view's settings for one genus, where the view lists any (byGenus)
    var g = named && typeof named.scientific === 'string' ? named.scientific.trim().split(/\s+/)[0] : '';
    var v = m && m.byGenus && g && m.byGenus.hasOwnProperty(g) ? m.byGenus[g] : null, o, k;
    if (!v) return m;
    o = {}; for (k in m) o[k] = m[k];
    for (k in v) if (k !== 'zones') o[k] = v[k];
    if (v.zones && m.zones) o.zones = m.zones.map(function (z) { var w = v.zones[z.id], r = {}, j; if (!w) return z; for (j in z) r[j] = z[j]; for (j in w) r[j] = w[j]; return r; });
    return o;
  }
  function drawOf(d) {
    var o = {}, c; if (!d) return o;
    for (c in d) { var names = d[c].map(function (x) { return x.name; }); o[c] = names.indexOf(TUNE.draw) >= 0 ? TUNE.draw : names[0]; }
    return o;
  }
  function paramsOf(m, named) {
    m = withGenus(m || {}, named);
    var s = clamp(180 / (m.fov || 180), .45, 1);
    var P = { zoom: s, barrel: (1 - s) * .9, fovea: m.fovea || 1, inv: 1 / (m.cpd || HUMAN_CPD), fall: m.fall || 0, wA: m.topoA || 0, wS: m.topoS || 0,
      dof: m.dof || 0, ax: m.pupil === 'v' ? .3 : 1, ay: m.pupil === 'h' ? .3 : 1, M: m.M || I3, uvBlue: m.uvBlue || 0, sheen: m.sheen || 0,
      gain: m.gain || 1, sat: m.sat === undefined ? 1 : m.sat, noGreen: m.noGreen || 0, gate: m.gate || 0, field: m.field || 0,
      persist: m.persist || 0, hold: m.hold || 0, thrust: m.thrust || 0, rate: m.rate || 1,
      glow: m.glow || 0, living: m.living || 0, uvR: m.uvR || 0, sal: m.salience ? 1 : 0, ripple: m.ripple || 0, shimmer: m.shimmer || 0,
      pan: m.sweep ? m.sweep[0] : 0, panS: m.sweep ? m.sweep[1] : 1 };
    P.glowC = m.glowC || [1, 1, 1];
    P.zones = m.zones ? m.zones.slice(0, 4).map(function (z) { return zoneOf(z, P); }) : null;
    // drawing options (&draw=, docs/views/ATLAS.md): each category's first option is the default
    P.draw = drawOf(m.draw); P.palm = P.draw.colour === 'palm' ? 1 : 0; P.stamps = P.draw.gaze === 'stamps' ? 1 : 0;
    if (P.draw.surround === 'pond') { P.gate = 1; if (P.zones) P.zones.forEach(function (z) { z.gate = z.gaze ? 0 : 1; }); }   // still things fade out
    P.gz = m.gaze || null; P.senses = m.senses || null; P.water = m.water || null; P.waterC = m.waterC || null;
    return P;
  }
  var HUMAN = paramsOf(null);
  function mixZones(a, b, t) {
    var za = a.zones || [], zb = b.zones || [], n = Math.max(za.length, zb.length), out = [], i;
    for (i = 0; i < n; i++) {
      var A = za[i] || neutralZone(zb[i], a), B = zb[i] || neutralZone(za[i], b), z = {}, k;
      for (k in B) z[k] = B[k];
      ZNUM.forEach(function (f) { z[f] = lerp(A[f], B[f], t); });
      z.M = A.M.map(function (x, j) { return lerp(x, B.M[j], t); });
      z.rate = t > .5 ? B.rate : A.rate;
      out.push(z);
    }
    return out;
  }
  function mix(a, b, t) {
    var o = {}, k;
    for (k in a) if (typeof a[k] === 'number') o[k] = lerp(a[k], b[k], t);
    o.M = a.M.map(function (x, i) { return lerp(x, b.M[i], t); });
    var src = t > .5 ? b : a;                      // the pace of movement switches whole, half way
    o.persist = src.persist; o.hold = src.hold; o.thrust = src.thrust; o.rate = src.rate; o.gate = t > .5 ? b.gate * clamp(t * 2 - 1, 0, 1) : 0;
    var z = b.zones || b.sal ? b : a;               // what comes with zones keeps to the view that has them
    o.glowC = z.glowC; o.gz = z.gz; o.draw = z.draw; o.senses = z.senses; o.waterC = (b.water ? b : a).waterC;
    o.water = a.water || b.water ? [0, 1, 2, 3].map(function (i) { return lerp(a.water ? a.water[i] : 0, b.water ? b.water[i] : 0, t); }) : null;
    o.zones = a.zones || b.zones ? mixZones(a, b, t) : null;
    return o;
  }
