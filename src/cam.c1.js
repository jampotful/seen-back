
  // ---------- state
  var canvas = $('gl'), vid = $('vid'), engine = null;
  try { engine = Engine(canvas); } catch (e) { engine = null; if (window.console) console.error(e); }
  var S = {
    screen: 'intro',          // intro | finder | askAnimal | naming | askView | animal
    src: 'none',              // what the picture is made from: none | cam | clip | still
    hasView: false,           // true once the picture is the person's own view (and not the animal's photo)
    freeze: false, eyes: null, named: null, animalPhoto: null,
    meetingId: null,          // the kept meeting that belongs to the photo in hand
    nov: '', camOK: false,
    k: 0, kGoal: 0, tr: null, holding: false,
    stream: null, facing: 'environment', mirror: false, cameras: 0, zoomCaps: null, camZoom: 1, camRefused: false,
    newFrame: false, vfc: 0, lastVideoTime: -1, lastNow: 0, token: 0, seq: 0, focus: .5, focusGoal: .5, clipUrl: null
  };
  var eyeP = HUMAN;
  var sample = null, canImages = false, downloads = null, nameCtl = null;
  var capsSettled = !inViewer, capsDone = function () {}, capsReady = inViewer ? new Promise(function (res) { capsDone = function () { capsSettled = true; res(); }; }) : Promise.resolve();
  var rec = null, recChunks = [], recT0 = 0, recTimer = null, recCv = null, recX = null, recOver = null, recDrop = false, kept = null;
  var msgTimer = 0, nameTimer = 0;
  // picture size: full where the phone keeps up, stepped down where it does not (or fixed with ?side=NNN)
  var sideAsked = /[?&]side=(\d+)/.exec(location.search || ''), perfN = 0, perfSum = 0;
  if (engine && sideAsked) engine.setSide(+sideAsked[1]);

  // ---------- small helpers
  function show(id, on) { $(id).hidden = !on; }
  // A line that is waiting carries a bar under it: one that slides while the wait has no known end (the line holds an ellipsis),
  // and one that fills where the line says how far it has come ("12 of 310 MB").
  function waitMark(el, text) {
    var t = text === undefined ? el.textContent : text, m = /(\d+) of (\d+) MB/.exec(t || ''), on = !!m || /\u2026|\.\.\./.test(t || '');
    el.classList.toggle('wait', on); el.classList.toggle('det', !!m);
    if (m) el.style.setProperty('--p', String(Math.max(0, Math.min(1, +m[1] / Math.max(1, +m[2]))))); else el.style.removeProperty('--p');
  }
  function msg(t, ms) { clearTimeout(msgTimer); $('msg').textContent = t || ''; waitMark($('msg')); if (t && ms) msgTimer = setTimeout(function () { $('msg').textContent = ''; waitMark($('msg')); }, ms); }
  function cap(s) { s = String(s || ''); return s.charAt(0).toUpperCase() + s.slice(1); }
  function clip(s, n) { s = (typeof s === 'string' ? s : '').replace(/\s+/g, ' ').trim(); return s.length > n ? s.slice(0, n) : s; }
  function makeCanvas(w, h) { var c = document.createElement('canvas'); c.width = Math.max(1, Math.round(w)); c.height = Math.max(1, Math.round(h)); return c; }
  function fit(src, sw, sh, max) {
    var k = Math.min(1, max / Math.max(sw, sh)), c = makeCanvas(sw * k, sh * k), x = c.getContext('2d');
    x.imageSmoothingQuality = 'high'; x.drawImage(src, 0, 0, c.width, c.height); return c;
  }
  function decode(file) {
    function viaImg() {
      return new Promise(function (res, rej) {
        var url = URL.createObjectURL(file), im = new Image();
        im.onload = function () { var c = fit(im, im.naturalWidth, im.naturalHeight, 1280); URL.revokeObjectURL(url); res(c); };
        im.onerror = function () { URL.revokeObjectURL(url); rej(new Error('decode')); };
        im.src = url;
      });
    }
    if (typeof createImageBitmap !== 'function') return viaImg();
    // the bitmap is let go only once the canvas has really drawn it (a one-pixel read makes it): an accelerated canvas may record a draw
    // and carry it out later, and in macOS WebKit a photo then sometimes reached the recognizer unlike itself (runs engines/12 and 15)
    return createImageBitmap(file).then(function (bmp) {
      var c = fit(bmp, bmp.width, bmp.height, 1280);
      try { c.getContext('2d').getImageData(0, 0, 1, 1); } catch (e) {}
      if (bmp.close) bmp.close(); return c;
    }, viaImg);
  }
  function labelDate(d) { var M = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']; return d.getDate() + ' ' + M[d.getMonth()] + ' ' + d.getFullYear(); }   // the month once stood as a Roman numeral, which read as a fault
  // A species' English name in sentence case: the first letter a capital, the rest small, except words that are names of
  // places or people ("North American river otter", "Cooper's hawk"). A scientific name passes through unchanged in effect.
  var PROPER = ' african alaskan american andean antarctic antillean appalachian arabian arctic argentine asian asiatic atlantic australian bahama bahaman baltic bermuda bolivian brazilian british burmese california californian canada canadian caribbean carolina carolinian chilean chinese colombian colorado cuban dutch egyptian english eurasian european florida floridian french georgia german greek guatemalan gulf haitian hawaiian himalayan hispaniolan indian indies indonesian irish italian jamaican japanese javan korean louisiana madagascar malayan mediterranean mexican mississippi new nile norway norwegian pacific panama panamanian persian peruvian philippine polynesian portuguese puerto rican russian scotia scottish siberian spanish sumatran swedish swiss tasmanian texas texan thai turkish virginia virginian world york zealand amazon bolivia china peru lanka keys st. augustine charles sebastian william susan maria lizzie jones hentz caesar hercules jesus venus quaker confederate january february march april june july august september october november december ';
  function nameCase(name) {
    name = String(name || ''); if (!name) return name;
    var first = true;
    return name.replace(/[^\s-]+/g, function (w, at) {
      var keep = /['’]s?$/.test(w) || PROPER.indexOf(' ' + w.toLowerCase() + ' ') >= 0 || (w.length <= 3 && w === w.toUpperCase() && /[A-Z]/.test(w) && at > 0);
      if (first) { first = false; return w.charAt(0).toUpperCase() + w.slice(1); }
      return keep ? w : w.toLowerCase();
    });
  }
  function handName(key) { return key === 'other' ? 'this creature' : (EYES[key] ? EYES[key].who : GROUPS[key] || 'this creature').replace(/^an? /, ''); }   // the names of groups carry no capital; a species keeps its own. A creature of no known group has no general name (build 22)
  function shownName() { return (S.named && S.named.common) || handName(S.eyes); }
  function guessed(key) { return EYES[key].rows.some(function (r) { return r[0] === 'i' || r[0] === 'g'; }); }
  function later(fn, ms) { var seq = S.seq; setTimeout(function () { if (seq === S.seq) fn(); }, ms); }
  function isMoving() { return S.src === 'cam' || S.src === 'clip'; }
  function canRecord() { return !!(window.MediaRecorder && HTMLCanvasElement.prototype.captureStream); }

  // ---------- screens
  function paintUI() {
    var s = S.screen, onPicture = s === 'finder' || s === 'animal' || s === 'naming';
    show('intro', s === 'intro'); show('askAnimal', s === 'askAnimal'); show('askView', s === 'askView');
    show('hud', onPicture);
    show('barFinder', s === 'finder'); show('barAnimal', s === 'animal');
    show('btnWho', s === 'animal' && !!S.eyes);
    show('btnFlip', S.src === 'cam' && (s === 'finder' || s === 'animal') && S.cameras > 1 && !S.freeze);
    $('btnRec').style.visibility = isMoving() && canRecord() ? 'visible' : 'hidden';
    if (S.eyes) { $('whoName').textContent = shownName(); $('whoMark').className = 'mk ' + (guessed(S.eyes) ? 'g' : 'm'); }
  }
  function go(screen) { S.screen = screen; paintUI(); }
  function setEyes(key, named) { S.eyes = key; S.named = named || null; eyeP = key ? paramsOf(EYES[key]) : HUMAN; S.k = 0; S.kGoal = 0; S.tr = null; S.focus = S.focusGoal = .5; }

  // ---------- the opening picture: soft lights, passed through one pair of eyes after another
  var introCv = makeCanvas(160, 300), introX = introCv.getContext('2d');
  var BLOBS = [[.22, .30, .20, '232,72,58', .31, 1.3], [.74, .22, .17, '242,199,68', .23, 2.1], [.60, .58, .24, '210,74,158', .19, .4],
    [.25, .72, .26, '47,128,62', .27, 3.3], [.82, .80, .18, '120,92,255', .21, 5.1], [.48, .40, .10, '255,255,255', .37, 4.2]];
  var INTRO = ['cat', 'wader', 'deer', 'bee'], introP = {};
  INTRO.forEach(function (k) { introP[k] = paramsOf(EYES[k]); });
  function paintIntro(now) {
    var t = now / 1000, x = introX, W = introCv.width, H = introCv.height, g = x.createLinearGradient(0, 0, 0, H);
    g.addColorStop(0, '#7fa6cf'); g.addColorStop(.5, '#b9c79a'); g.addColorStop(1, '#2f4a22');
    x.fillStyle = g; x.fillRect(0, 0, W, H);
    BLOBS.forEach(function (b) {
      var cx = (b[0] + .08 * Math.sin(t * b[4] + b[5])) * W, cy = (b[1] + .06 * Math.cos(t * b[4] * .8 + b[5])) * H, r = b[2] * H;
      var rg = x.createRadialGradient(cx, cy, 0, cx, cy, r);
      rg.addColorStop(0, 'rgba(' + b[3] + ',.95)'); rg.addColorStop(1, 'rgba(' + b[3] + ',0)');
      x.fillStyle = rg; x.fillRect(cx - r, cy - r, 2 * r, 2 * r);
    });
  }
  function drawIntro(now, dt, dim) {
    paintIntro(calm ? 0 : now); engine.setImage(introCv);
    var fx = { ap: 1, shape: 0, mosaic: 0, apY: .17, expo: dim ? .4 : 1, focus: .5 }, P = HUMAN;
    if (!calm) {
      var CYC = 5200, n = Math.floor(now / CYC), t = (now % CYC) / CYC, k;
      var next = INTRO[n % INTRO.length], from = n === 0 ? HUMAN : introP[INTRO[(n - 1) % INTRO.length]];
      if (EYES[next].pupil === 'none') { k = ease(clamp((t - .12) / .5, 0, 1)); fx.mosaic = Math.sin(Math.PI * clamp(t / .74, 0, 1)); }
      else {
        fx.shape = shapeOf(next);
        fx.ap = t < .26 ? 1 - ease(t / .26) : t < .36 ? 0 : ease((t - .36) / .38);
        k = ease(clamp((t - .26) / .1, 0, 1));
      }
      P = mix(from, introP[next], k);
    }
    engine.draw(P, fx, now, dt);
  }

  // ---------- where the picture comes from
  function watchFrames() {
    if (!vid.requestVideoFrameCallback) return;
    var id = ++S.vfc;
    (function again() { vid.requestVideoFrameCallback(function () { if (id !== S.vfc) return; S.newFrame = true; again(); }); })();
  }
  function stopSource() {
    if (S.stream) S.stream.getTracks().forEach(function (t) { t.stop(); });
    S.stream = null; S.vfc++;
    try { vid.pause(); } catch (e) {}
    vid.srcObject = null;
    if (S.clipUrl) { vid.removeAttribute('src'); try { vid.load(); } catch (e) {} URL.revokeObjectURL(S.clipUrl); S.clipUrl = null; }
    S.src = 'none'; S.hasView = false; S.freeze = false; S.newFrame = false; S.lastVideoTime = -1; S.zoomCaps = null; S.camZoom = 1;
  }
  function startCamera(facing) {
    stopSource(); S.facing = facing;
    return navigator.mediaDevices.getUserMedia({ video: { facingMode: { ideal: facing }, width: { ideal: 1280 }, height: { ideal: 720 } }, audio: false }).then(function (stream) {
      S.stream = stream; vid.loop = false; vid.srcObject = stream;
      var tr = stream.getVideoTracks()[0], set = tr && tr.getSettings ? tr.getSettings() : {};
      S.mirror = set.facingMode ? set.facingMode === 'user' : true;      // a webcam with no stated facing is treated as a mirror
      var caps = tr && tr.getCapabilities ? tr.getCapabilities() : {};
      S.zoomCaps = caps && caps.zoom && typeof caps.zoom.min === 'number' ? { min: caps.zoom.min, max: caps.zoom.max, track: tr } : null;
      return vid.play();
    }).then(function () {
      S.src = 'cam'; S.hasView = true; watchFrames();
      if (navigator.mediaDevices.enumerateDevices) {
        navigator.mediaDevices.enumerateDevices().then(function (ds) { S.cameras = ds.filter(function (d) { return d.kind === 'videoinput'; }).length; paintUI(); }).catch(function () {});
      }
    });
  }
  function startClip(file) {
    stopSource();
    function load(url) {
      vid.loop = true; vid.muted = true; vid.src = url;
      return new Promise(function (res, rej) {
        var done = false, to = setTimeout(function () { if (!done) { done = true; rej(new Error('slow')); } }, 9000);
        vid.onloadeddata = function () { if (done) return; done = true; clearTimeout(to); res(); };
        vid.onerror = function () { if (done) return; done = true; clearTimeout(to); rej(new Error('video')); };
      });
    }
    S.clipUrl = URL.createObjectURL(file);
    return load(S.clipUrl).catch(function (e) {
      // some viewers refuse a clip handed over as a blob address; a smaller one can go in whole instead
      if (file.size > 48e6 || typeof FileReader !== 'function') throw e;
      return new Promise(function (res, rej) {
        var fr = new FileReader(); fr.onload = function () { res(fr.result); }; fr.onerror = function () { rej(e); }; fr.readAsDataURL(file);
      }).then(load);
    }).then(function () {
      S.src = 'clip'; S.hasView = true; S.mirror = false; watchFrames();
      return vid.play().catch(function () {});
    });
  }
  function showStill(c, isView) { stopSource(); S.src = 'still'; S.hasView = !!isView; if (engine) engine.setImage(c); }
  function thaw() { if (!S.freeze) return; S.freeze = false; if (engine) engine.resetTime(); }
  function setCamZoom(z) {
    var c = S.zoomCaps; if (!c || S.src !== 'cam') return;
    z = clamp(z, c.min, Math.max(c.min, 1));               // only ever wider than the usual view, where the phone offers it
    if (Math.abs(z - S.camZoom) < .02) return;
    c.track.applyConstraints({ advanced: [{ zoom: z }] }).then(function () { S.camZoom = z; }).catch(function () {});
  }

  // ---------- the change of eyes
  function shapeOf(key) { var p = EYES[key].pupil; return p === 'v' ? 1 : p === 'h' ? 2 : 0; }
  function showName() {
    $('rvName').textContent = shownName(); $('rvSci').textContent = (S.named && S.named.scientific) || '';
    $('rvCount').textContent = S.named && S.named.again ? 'Encountered ' + labelDate(new Date(S.named.again)) : S.nov === 'kind' && S.eyes !== 'person' ? 'See the world as ' + (/^[aeiou]/i.test(shownName()) ? 'an' : 'a') : S.nov === 'name' ? 'First encounter' : S.nov === 'again' ? 'Encountered before' : '';
    var mNow = S.meetingId ? record.filter(function (r) { return r.id === S.meetingId; })[0] : null;
    $('rvWarn').textContent = S.eyes !== 'person' && mNow ? lentLine(mNow) : '';      // the week, said once at the meeting; what is a guess is marked on the name and in its sheet
    $('reveal').classList.add('show');
    clearTimeout(nameTimer); nameTimer = setTimeout(function () { $('reveal').classList.remove('show'); }, calm ? 1500 : 2500);
  }
  function hideName() { clearTimeout(nameTimer); $('reveal').classList.remove('show'); }
  function startChange() {
    if (!S.eyes) return;
    S.tr = { t0: performance.now(), dur: calm ? 500 : (EYES[S.eyes].pupil === 'none' ? 3000 : 2800) };
    S.kGoal = 1;
  }
  function fxNow(now, dt) {
    var key = S.eyes, fx = { ap: 1, shape: 0, mosaic: 0, soft: 0, expo: 1 };
    if (S.tr && key) {
      var t = S.tr.fixed !== undefined ? S.tr.fixed : clamp((now - S.tr.t0) / S.tr.dur, 0, 1), none = EYES[key].pupil === 'none';
      if (calm) S.k = ease(t);
      else if (none) { S.k = ease(clamp((t - .15) / .7, 0, 1)); fx.mosaic = (key === 'bee' || key === 'insect') ? Math.sin(Math.PI * t) : 0; }
      else {
        // the aperture closes to the shape of that pupil, the eyes change while it is smallest, and it opens again
        fx.shape = shapeOf(key);
        fx.ap = t < .38 ? 1 - ease(t / .38) : t < .5 ? 0 : ease((t - .5) / .5);
        S.k = ease(clamp((t - .38) / .12, 0, 1));
        var settle = t < .3 ? 0 : t < .38 ? ease((t - .3) / .08) : t < .5 ? 1 : 1 - ease((t - .5) / .42);
        fx.soft = 16 * settle; fx.expo = 1 + .6 * settle;     // the new eye opens bright and unfocused, then settles
        if (t >= .4 && !S.tr.zoomed) { S.tr.zoomed = true; setCamZoom(clamp(180 / (EYES[key].fov || 180), .45, 1)); }
      }
      if (t >= 1) { S.tr = null; S.k = 1; afterChange(); }
    } else if (key) {
      var goal = S.holding ? 0 : S.kGoal;
      S.k += clamp(goal - S.k, -(dt || 16) / 220, (dt || 16) / 220);
    } else S.k = 0;
    S.focus += (S.focusGoal - S.focus) * (1 - Math.exp(-(dt || 16) / 90));
    fx.focus = S.focus; fx.mirror = S.src === 'cam' && S.mirror; fx.camZoom = S.camZoom;
    return fx;
  }
  function afterChange() {
    if (S.screen !== 'animal') return;
    var E = EYES[S.eyes], line = S.eyes === 'person' ? 'That’s a human. You already see the world as one.'
      : (isMoving() || !/slow|still|Walk/.test(E.cue)) && E.cue ? E.cue : '';
    msg(line, 6500);
  }

  // ---------- drawing loop
  function loop(now) {
    requestAnimationFrame(loop);
    if (!engine || S.selftest) return;                       // the self-test (?selftest=1) draws for itself
    var dt = S.lastNow ? Math.min(100, now - S.lastNow) : 16; S.lastNow = now;
    engine.resize();
    var s = S.screen;
    if (s === 'intro' || s === 'askAnimal') { drawIntro(now, dt, s === 'askAnimal'); return; }
    if (isMoving() && !S.freeze && vid.readyState >= 2 && vid.videoWidth) {
      var fresh = vid.requestVideoFrameCallback ? S.newFrame : vid.currentTime !== S.lastVideoTime;
      if (fresh) { S.newFrame = false; S.lastVideoTime = vid.currentTime; engine.setFrame(vid, vid.videoWidth, vid.videoHeight, now); }
    }
    var fx = fxNow(now, dt), P = S.eyes ? mix(HUMAN, eyeP, S.k) : HUMAN;
    if (s === 'askView') fx.expo = .5;                       // the animal's photo sits dimmed behind the prompt
    engine.draw(P, fx, now, dt);
    if (rec && recX) { recX.drawImage(canvas, 0, 0, recCv.width, recCv.height); if (recOver) recX.drawImage(recOver, 0, 0); }
    perfSum += dt;
    if (++perfN >= 45) {
      if (!sideAsked && !rec && perfSum / perfN > 42 && engine.side() > 540) engine.setSide(Math.max(540, engine.side() * .75));
      perfN = 0; perfSum = 0;
    }
  }
