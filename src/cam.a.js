  'use strict';
  var $ = function (id) { return document.getElementById(id); };

  // ---------- where is this running?
  // Inside Claude's viewer the camera is normally refused, and only there can Claude name a photo.
  var inViewer = !!(window.claude && typeof window.claude.use === 'function');
  var hasCamera = !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);
  var coarse = !!(window.matchMedia && window.matchMedia('(pointer: coarse)').matches);
  var calm = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var BUILD = '38';
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
    if ((key === 'M' || key === 'dark') && typeof x === 'string') { var m = mats[x] || (spec.matrices || {})[x]; return m && m.rows && m.rows.length === 3 ? m.rows.every(function (r) { return r.length === 3; }) ? [].concat.apply([], m.rows) : m.rows.map(function (r) { return r.slice(0, 3); }).reduce(function (a, r) { return a.concat(r); }, []).concat(m.rows.map(function (r) { return r[3] || 0; })) : I3.slice(); }
    if (key === 'q' && typeof x === 'string') { var mq = mats[x] || (spec.matrices || {})[x]; return mq && mq.q ? [].concat.apply([], mq.q) : null; }
    if (isParam(x)) return x.hasOwnProperty('value') ? specValue(x.value, spec, mats, key) : specCurve(x);
    if (Array.isArray(x)) return x.map(function (v) { return specValue(v, spec, mats, key); });
    if (x && typeof x === 'object') { var o = {}, k; for (k in x) o[k] = specValue(x[k], spec, mats, k); return o; }
    return x;
  }
  // A value given against a measured input ({ curve: 'lux', points: [[x, v], ...] }) is interpolated in the logarithm of light, x being
  // log10 of the light module's relative level (LIGHT.lum, 0 to 1 of the camera's exposure; absolute light needs the exposure time, which
  // most browsers do not report). Before the first reading it takes the first point. The page recomputes such a view twice a second.
  // A curve against "dark" (0 by day, 1 by night) or "moon" (the lit fraction of tonight's moon) reads the clock below instead.
  function specCurve(p) {
    var P = p.points || []; if (!P.length) return 0;
    var C = p.curve === 'dark' || p.curve === 'moon' ? clockNow() : null;
    if (!C && !LIGHT.reads) return P[0][1];
    var x = C ? C[p.curve] : Math.log(Math.max(LIGHT.lum, 1e-3)) / Math.LN10, i;
    if (x <= P[0][0]) return P[0][1];
    for (i = 1; i < P.length; i++) if (x <= P[i][0]) return P[i - 1][1] + (P[i][1] - P[i - 1][1]) * (x - P[i - 1][0]) / (P[i][0] - P[i - 1][0]);
    return P[P.length - 1][1];
  }
  // ---------- the clock, the sun and the moon (module 3, light; docs/ENGINE-DESIGN.md). From the date and the time zone only.
  // The sun's height uses the usual declination and hour-angle formulas with the longitude taken from the time zone (15 degrees an
  // hour) and a latitude of 35 degrees north unless the page knows better (CLOCK_LAT): both INVENTED stand-ins, good to an hour or so.
  // "dark" ramps from 0 with the sun 6 degrees up to 1 with it 12 degrees down, about the two hours of dusk the scorpion sheet asks for
  // (the ramp's ends are the app's). The moon's lit fraction counts synodic months of 29.530589 days from the new moon of 6 January
  // 2000, 18:14 UTC (a standard reference epoch; good to about a day). &hour=<0-24> and &moon=<0-1> set them by hand for checking.
  var CLOCK_LAT = 35, CLOCK_SET = { hour: +((/[?&]hour=([0-9.]+)/.exec(location.search || '') || [0, NaN])[1]), moon: +((/[?&]moon=([0-9.]+)/.exec(location.search || '') || [0, NaN])[1]) };
  function clockNow(d) {
    d = d || new Date();
    var hour = isNaN(CLOCK_SET.hour) ? d.getHours() + d.getMinutes() / 60 : CLOCK_SET.hour % 24, off = -d.getTimezoneOffset() / 60;
    var day = Math.floor((Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) - Date.UTC(d.getFullYear(), 0, 0)) / 864e5);
    var decl = -23.44 * Math.cos(2 * Math.PI * (day + 10) / 365), lon = off * 15;
    var solar = hour - off + lon / 15, ha = (solar - 12) * 15 * Math.PI / 180, la = CLOCK_LAT * Math.PI / 180, de = decl * Math.PI / 180;
    var alt = Math.asin(Math.sin(la) * Math.sin(de) + Math.cos(la) * Math.cos(de) * Math.cos(ha)) * 180 / Math.PI;
    var age = ((d.getTime() - Date.UTC(2000, 0, 6, 18, 14)) / 864e5) % 29.530589; if (age < 0) age += 29.530589;
    var moon = isNaN(CLOCK_SET.moon) ? (1 - Math.cos(2 * Math.PI * age / 29.530589)) / 2 : clamp(CLOCK_SET.moon, 0, 1);
    var t = clamp((6 - alt) / 18, 0, 1);
    var az = (Math.atan2(Math.sin(ha), Math.cos(ha) * Math.sin(la) - Math.tan(de) * Math.cos(la)) * 180 / Math.PI + 180) % 360;   // the sun's azimuth from north, for the polarization overlay
    return { hour: hour, sun: alt, az: az, dark: t * t * (3 - 2 * t), moon: moon, moonAge: age };
  }
  function viewOf(spec) {
    var mats = spec.matrices || {}, v = { chip: spec.chip, who: spec.who, cue: spec.cue }, k, g;
    for (k in spec.params) v[k] = specValue(spec.params[k], spec, mats, k);
    if (spec.zones) v.zones = specValue(spec.zones, spec, mats, 'zones');
    if (spec.gaze) v.gaze = specValue(spec.gaze, spec, mats, 'gaze');
    ['spectrum', 'clock', 'pace', 'motion', 'slow', 'tilt', 'magnet', 'remap', 'overlay', 'sound', 'haptic'].forEach(function (b) { if (spec[b]) v[b] = specValue(spec[b], spec, mats, b); });
    if (spec.draw) v.draw = spec.draw;
    if (spec.inputs && spec.inputs.senses) v.senses = specValue(spec.inputs.senses, spec, mats, 'senses');
    if (spec.by && spec.by.genus) { v.byGenus = {}; for (g in spec.by.genus) v.byGenus[g] = specValue(spec.by.genus[g], spec, mats, g); }
    v.rows = (spec.rows || []).map(function (r) { return r.slice(0, 3); });
    return v;
  }
  // A spec's "trial" block holds changes being tried on an offered view: they apply only when the view is reached with ?try=<key>,
  // so the view the app offers stays as it is. Objects merge key by key; anything else in the block replaces what it names.
  function merged(a, b) { var o = {}, k; for (k in a) o[k] = a[k]; for (k in b) o[k] = a[k] && b[k] && typeof a[k] === 'object' && typeof b[k] === 'object' && !Array.isArray(b[k]) && !isParam(b[k]) ? merged(a[k], b[k]) : b[k]; return o; }
  var EYES = {}, TRY = {};
  Object.keys(SPECS).forEach(function (k) {
    var s = SPECS[k]; s.hasCurve = JSON.stringify(s).indexOf('"curve"') >= 0 || !!s.clock;
    (s.offered ? EYES : TRY)[k] = viewOf(s);
    if (s.offered && s.trial) { TRY[k] = viewOf(merged(s, s.trial)); TRY[k].trial = true; }
  });
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
  TRY_KEYS.forEach(function (k) { EYES[k] = TRY[k]; if (SPECS[k].offered && SPECS[k].trial) { SPECS[k] = merged(SPECS[k], SPECS[k].trial); delete SPECS[k].trial; SPECS[k].hasCurve = JSON.stringify(SPECS[k]).indexOf('"curve"') >= 0 || !!SPECS[k].clock; } });
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
      inv: z.cpd ? 1 / z.cpd : P.inv, M: z.M ? z.M.slice(0, 9) : P.M, U: z.M && z.M.length === 12 ? z.M.slice(9) : P.U, sat: z.sat === undefined ? P.sat : z.sat, gain: z.gain || P.gain, gate: z.gate === undefined ? P.gate : z.gate,
      rate: z.rate || P.rate, glow: z.glow === undefined ? P.glow : z.glow, living: z.living === undefined ? P.living : z.living,
      uv: z.uv === undefined ? P.uvBlue : z.uv, uvR: z.uvR === undefined ? P.uvR : z.uvR, sheen: z.sheen === undefined ? P.sheen : z.sheen, mag: z.mag || 1 };
  }
  var ZNUM = ['inv', 'sat', 'gain', 'gate', 'glow', 'living', 'uv', 'uvR', 'sheen', 'mag'];
  function neutralZone(z, P) {                     // the same place and shape, drawn as the other view would draw it there
    var o = {}, k; for (k in z) o[k] = z[k];
    o.inv = P.inv; o.M = P.M; o.U = P.U; o.sat = P.sat; o.gain = P.gain; o.gate = P.gate; o.rate = P.rate; o.glow = P.glow; o.living = P.living; o.uv = P.uvBlue; o.uvR = P.uvR; o.sheen = P.sheen; o.mag = 1;
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
      dof: m.dof || 0, ax: m.pupil === 'v' ? .3 : 1, ay: m.pupil === 'h' ? .3 : 1, M: m.M ? m.M.slice(0, 9) : I3, U: m.M && m.M.length === 12 ? m.M.slice(9) : [0, 0, 0], uvBlue: m.uvBlue || 0, sheen: m.sheen || 0,
      gain: m.gain || 1, sat: m.sat === undefined ? 1 : m.sat, noGreen: m.noGreen || 0, gate: m.gate || 0, field: m.field || 0,
      persist: m.persist || 0, hold: m.hold || 0, thrust: m.thrust || 0, rate: m.rate || 1,
      glow: m.glow || 0, living: m.living || 0, uvR: m.uvR || 0, sal: m.salience ? 1 : 0, ripple: m.ripple || 0, shimmer: m.shimmer || 0,
      pan: m.sweep ? m.sweep[0] : 0, panS: m.sweep ? m.sweep[1] : 1 };
    P.glowC = m.glowC || [1, 1, 1];
    P.zones = m.zones ? m.zones.slice(0, 4).map(function (z) { return zoneOf(z, P); }) : null;
    // drawing options (&draw=, docs/views/ATLAS.md): each category's first option is the default
    P.draw = drawOf(m.draw); P.palm = P.draw.colour === 'palm' ? 1 : 0; P.stamps = P.draw.gaze === 'stamps' ? 1 : 0;
    if (P.draw.surround === 'pond') { P.gate = 1; if (P.zones) P.zones.forEach(function (z) { z.gate = z.gaze ? 0 : 1; }); }   // still things fade out
    spectrumOf(P, m); P.clock = m.clock || null; P.pace = m.pace || null; P.motion = m.motion || null;
    if (P.clock && P.draw.clock === 'moon') { var C = clockNow(); P.gain *= lerp(1, .15 + .85 * C.moon, C.dark); }   // tonight's moon (atlas 25, invented)
    if (P.pace && P.draw.pace === 'replay') P.replay = P.pace.ratio || 3;
    if (P.motion && P.draw.steady === 'arm') { P.hold = 0; P.thrust = P.motion.thrustMs || 140; P.arm = 1; }
    if (P.motion && P.draw.steady === 'lock') P.lock = 1;
    // module 12, slow, and module 5's tilt and heading (docs/ENGINE.md): each drawn only through its category's option
    P.slow = m.slow || null; P.slowMode = P.slow && P.draw.slow && P.draw.slow !== 'off' ? P.draw.slow : '';
    P.tilt = m.tilt || null; P.snell = P.tilt && P.draw.tilt === 'snell' ? 1 : 0;
    P.magnet = m.magnet || null; P.magMode = P.magnet && (P.draw.magnet === 'grain' || P.draw.magnet === 'tide') ? P.draw.magnet : '';
    // modules 8 to 11 (docs/ENGINE.md): field, overlay, sound and haptic, each drawn only through its category's option
    P.remap = m.remap || null; P.fieldMode = P.remap && /^(wedge|fold|window|ribbon)$/.test(P.draw.field || '') ? P.draw.field : '';
    P.ovl = m.overlay || null; P.ovlMode = P.ovl && /^(polar|web|rings|shadow)$/.test(P.draw.overlay || '') ? P.draw.overlay : '';
    P.snd = m.sound || null; P.sndMode = P.snd && /^(hear|clap|air|rumble|rings)$/.test(P.draw.sound || '') ? P.draw.sound : '';
    P.hap = m.haptic || null; P.hapMode = P.hap && /^(buzz|edge)$/.test(P.draw.haptic || '') ? P.draw.haptic : '';
    if (P.fieldMode === 'window') { P.tilt = P.tilt || { fromDeg: 0, fullDeg: 1 }; P.snellFixed = 1; }
    P.senses = m.senses || null;
    var hearIt = P.sndMode || P.ovlMode === 'rings' || (P.hapMode && P.hap.on === 'onset');
    if (hearIt || P.fieldMode === 'wedge' || P.fieldMode === 'ribbon' || P.ovlMode === 'polar' || P.ovlMode === 'web' || (P.hapMode && P.hap.on === 'knock')) {
      var sn = {}, sk; for (sk in P.senses || {}) sn[sk] = P.senses[sk];
      if (hearIt) { sn.mic = sn.mic || [40, 12000]; sn.sound = 1; if (P.snd && P.snd.say) sn.say = P.snd.say; if (P.sndMode === 'clap' && P.snd && P.snd.clickHz) sn.click = P.snd.clickHz; }
      if (P.fieldMode === 'wedge' || P.fieldMode === 'ribbon' || P.ovlMode === 'polar') sn.motion = 1;
      if ((P.hapMode && P.hap.on === 'knock') || P.ovlMode === 'web') { sn.motion = 1; sn.jolt = 1; }
      P.senses = sn;
    }
    P.gz = m.gaze || null; P.water = m.water || null; P.waterC = m.waterC || null;
    return P;
  }
  // Module 2, spectrum: the ultraviolet column (P.U) comes with a 3 by 4 matrix; the animal's classes (P.Q, 4 by 4) serve the colour
  // wheel (&draw=wheel) and the neutral band (&draw=neutral); a dark-adapted matrix is blended in as the light falls (snail, dog).
  var WHEEL = { turn: 0 };   // the colour wheel's turn, 0 to 4, set by a finger dragged across the picture (src/cam.tune.js)
  function spectrumOf(P, m) {
    var sp = m.spectrum; P.spec = sp ? 1 : 0; P.Q = null; P.rot4 = -1; P.neutral = 0; P.adapt = null;
    if (!sp) return;
    P.Q = sp.q || null;
    if (sp.dark) P.adapt = { M: sp.dark.slice(0, 9), U: sp.dark.length === 12 ? sp.dark.slice(9) : [0, 0, 0], at: sp.adaptAt || [-1.6, -0.6] };
    if (P.draw.spectrum === 'wheel' && P.Q) P.rot4 = 0;
    if (P.draw.spectrum === 'neutral') P.neutral = sp.neutral === undefined ? 1 : sp.neutral;
  }
  function adaptOf(P) {                            // how far the eye has gone toward its dark-adapted matrix, from the light module's level
    if (!P.adapt || !LIGHT.reads) return 0;
    var x = Math.log(Math.max(LIGHT.lum, 1e-3)) / Math.LN10, a = P.adapt.at;
    return 1 - ease((x - a[0]) / Math.max(a[1] - a[0], .01));
  }
  var HUMAN = paramsOf(null);
  function mixZones(a, b, t) {
    var za = a.zones || [], zb = b.zones || [], n = Math.max(za.length, zb.length), out = [], i;
    for (i = 0; i < n; i++) {
      var A = za[i] || neutralZone(zb[i], a), B = zb[i] || neutralZone(za[i], b), z = {}, k;
      for (k in B) z[k] = B[k];
      ZNUM.forEach(function (f) { z[f] = lerp(A[f], B[f], t); });
      z.M = A.M.map(function (x, j) { return lerp(x, B.M[j], t); }); z.U = A.U.map(function (x, j) { return lerp(x, B.U[j], t); });
      z.rate = t > .5 ? B.rate : A.rate;
      out.push(z);
    }
    return out;
  }
  function mix(a, b, t) {
    var o = {}, k;
    for (k in a) if (typeof a[k] === 'number') o[k] = lerp(a[k], b[k], t);
    o.M = a.M.map(function (x, i) { return lerp(x, b.M[i], t); }); o.U = a.U.map(function (x, i) { return lerp(x, b.U[i], t); });
    var src = t > .5 ? b : a;                      // the pace of movement switches whole, half way
    o.persist = src.persist; o.hold = src.hold; o.thrust = src.thrust; o.rate = src.rate; o.gate = t > .5 ? b.gate * clamp(t * 2 - 1, 0, 1) : 0;
    var z = b.zones || b.sal ? b : a;               // what comes with zones keeps to the view that has them
    var w = b.spec || b.clock || b.pace || b.motion || b.slow || b.tilt || b.magnet || b.remap || b.ovl || b.snd || b.hap ? b : a;   // the new modules keep to the view that has them
    o.Q = w.Q; o.adapt = w.adapt; o.clock = w.clock; o.pace = w.pace; o.motion = w.motion; o.rot4 = w.rot4; o.lock = w.lock; o.arm = w.arm; o.replay = w.replay; o.slow = w.slow; o.slowMode = w.slowMode; o.tilt = w.tilt; o.snell = w.snell; o.magnet = w.magnet; o.magMode = w.magMode; o.remap = w.remap; o.fieldMode = w.fieldMode; o.snellFixed = w.snellFixed; o.ovl = w.ovl; o.ovlMode = w.ovlMode; o.snd = w.snd; o.sndMode = w.sndMode; o.hap = w.hap; o.hapMode = w.hapMode;
    o.glowC = z.glowC; o.gz = z.gz; o.draw = z.draw; o.senses = z.senses; o.waterC = (b.water ? b : a).waterC;
    o.water = a.water || b.water ? [0, 1, 2, 3].map(function (i) { return lerp(a.water ? a.water[i] : 0, b.water ? b.water[i] : 0, t); }) : null;
    o.zones = a.zones || b.zones ? mixZones(a, b, t) : null;
    return o;
  }
