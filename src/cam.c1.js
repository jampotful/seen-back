
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

  // ---------- the phone's own senses, for views that ask for them (build 23)
  // The motion sensors tell the movement map how fast the phone is turning and whether it lies still; the microphone turns low
  // sounds into ripples for creatures that sense vibration and moving air. Each input stays off behind SENSE_ON until the app's
  // thread turns it on (a visit with ?try= may turn them on with &sense=motion,mic), and nothing asks for a permission until the
  // person taps the line that says, in plain words, what the input is for. docs/ENGINE.md describes both.
  var SENSE_ON = { motion: false, mic: false };
  if (TRY_KEYS.length) ((/[?&]sense=([a-z,]+)/.exec(location.search || '') || [0, ''])[1]).split(',').forEach(function (k) { if (SENSE_ON.hasOwnProperty(k)) SENSE_ON[k] = true; });
  var senses = (function () {
    var want = null, motionOn = false, rotS = 0, accMean = 0, accDev = 0, gotMotion = 0, lastJolt = 0, mic = null, micAsked = false, rips = [], line = null;
    var SAY = { motion: 'This view can feel the phone move and lie still. Tap to let it use the motion sensors.',
      mic: 'This view can show low sounds as ripples. Tap to let it listen through the microphone. Nothing is recorded or kept.' };
    // module 5, motion: the turn of the phone since the last snap, in degrees (the locked world, &draw=lock), and its thrusts forward
    // (the arm as the neck, &draw=arm). Which way each rotation axis moves the picture is the app's reading of the specification and
    // waits for a phone to confirm it.
    var stabX = 0, stabY = 0, snapAt = 0, lastM = 0, thrustAt = 0;
    // tilt and heading (module 5): the phone's roll in the screen's plane and the camera's elevation, from gravity, and the compass
    // heading. iOS reports gravity with the opposite sign to Android, so its readings are turned round. &roll=, &elev= and &heading=
    // set them by hand for checking. Which way each one turns the picture waits for a phone to confirm it.
    var POSE_SET = {}; ['roll', 'elev', 'heading'].forEach(function (k) { var m = new RegExp('[?&]' + k + '=(-?[0-9.]+)').exec(location.search || ''); if (m) POSE_SET[k] = +m[1]; });
    var IOS = !!(window.DeviceMotionEvent && typeof window.DeviceMotionEvent.requestPermission === 'function'), roll = 0, elev = 0, heading = null;
    function onOrient(e) {
      if (typeof e.webkitCompassHeading === 'number') heading = e.webkitCompassHeading;
      else if (e.absolute && typeof e.alpha === 'number') heading = (360 - e.alpha) % 360;
    }
    function onMotion(e) {
      var r = e.rotationRate || {}, a = e.acceleration, g = e.accelerationIncludingGravity, now = performance.now(), am;
      var dts = lastM ? Math.min((now - lastM) / 1000, .1) : 0; lastM = now;
      stabX += (r.gamma || 0) * dts; stabY += (r.beta || 0) * dts;   // held upright: gamma turns the phone left and right, beta tips it up and down
      if (a && a.z !== null && a.z !== undefined && want && want.motion && eyeP && eyeP.arm && Math.abs(a.z) > ((eyeP.motion && eyeP.motion.thrust) || 3) && now - thrustAt > 250) {
        thrustAt = now; if (engine && engine.kick) engine.kick(); if (navigator.vibrate) try { navigator.vibrate(12); } catch (x) { /* refused */ }
      }
      gotMotion = now;
      if (g && g.x !== null && g.x !== undefined) {
        var sg = IOS ? -1 : 1, gx = g.x * sg, gy = g.y * sg, gz = g.z * sg, gm = Math.sqrt(gx * gx + gy * gy + gz * gz) || 1;
        if (gx * gx + gy * gy > .5) roll = Math.atan2(gx, gy) * 180 / Math.PI;
        elev = -Math.asin(clamp(gz / gm, -1, 1)) * 180 / Math.PI;
      }
      rotS = lerp(rotS, Math.sqrt((r.alpha || 0) * (r.alpha || 0) + (r.beta || 0) * (r.beta || 0) + (r.gamma || 0) * (r.gamma || 0)), .2);   // degrees a second
      if (a && a.x !== null && a.x !== undefined) am = Math.sqrt(a.x * a.x + a.y * a.y + a.z * a.z);
      else if (g && g.x !== null && g.x !== undefined) { am = Math.sqrt(g.x * g.x + g.y * g.y + g.z * g.z); accMean = lerp(accMean || am, am, .02); am = Math.abs(am - accMean); }
      else return;
      accDev = lerp(accDev, am, .1);
      if (want && want.jolt && am > 2.2 && now - lastJolt > 140) {   // a knock on the phone, or on the table it lies on, starts a ripple from that side
        lastJolt = now; var dx = a ? -(a.x || 0) : 0, dy = a ? (a.y || 0) : 0, d = Math.sqrt(dx * dx + dy * dy) || 1;
        rips.push({ x: .32 * dx / d, y: .32 * dy / d, t: now, a: clamp(am / 6, .3, 1) });
      }
    }
    function startMotion() {
      if (motionOn) return;
      motionOn = true; window.addEventListener('devicemotion', onMotion);
      window.addEventListener('ondeviceorientationabsolute' in window ? 'deviceorientationabsolute' : 'deviceorientation', onOrient);
    }
    function startMic() {
      if (mic || !navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) return;
      micAsked = true; paint();
      navigator.mediaDevices.getUserMedia({ audio: { echoCancellation: false, noiseSuppression: false, autoGainControl: false }, video: false }).then(function (st) {
        var AC = window.AudioContext || window.webkitAudioContext, ctx = new AC(), lo = (want && want.mic && want.mic[0]) || 60, hi = (want && want.mic && want.mic[1]) || 400;
        var src = ctx.createMediaStreamSource(st), bp = ctx.createBiquadFilter(), an = ctx.createAnalyser(), c = Math.sqrt(lo * hi);
        bp.type = 'bandpass'; bp.frequency.value = c; bp.Q.value = c / (hi - lo); an.fftSize = 1024;
        src.connect(bp); bp.connect(an); if (ctx.resume) ctx.resume();
        mic = { st: st, ctx: ctx, an: an, buf: new Float32Array(an.fftSize), mean: 0, last: 0 };
        if (!want || !want.mic) stopMic();
        paint();
      }, function () { paint(); });
    }
    function stopMic() {
      if (!mic) return;
      try { mic.st.getTracks().forEach(function (t) { t.stop(); }); mic.ctx.close(); } catch (e) {}
      mic = null;
    }
    function paint() {                              // the one line on the picture that offers an input, while the view wants one that is off
      var need = want && S.screen === 'animal' ? (want.motion && SENSE_ON.motion && !motionOn ? 'motion' : want.mic && SENSE_ON.mic && !mic && !micAsked ? 'mic' : '') : '';
      if (!need) { if (line) line.hidden = true; return; }
      if (!line) {
        line = document.createElement('button'); line.type = 'button'; line.className = 'line'; line.id = 'senseLine';
        var at = $('svcHud'); at.parentNode.insertBefore(line, at.nextSibling);
        line.addEventListener('click', function () {
          var k = line.dataset.k;
          if (k === 'motion') {
            var D = window.DeviceMotionEvent;
            if (D && typeof D.requestPermission === 'function') D.requestPermission().then(function (s) { if (s === 'granted') startMotion(); paint(); }, function () { paint(); });
            else { startMotion(); paint(); }
          } else if (k === 'mic') startMic();
        });
      }
      line.dataset.k = need; line.textContent = SAY[need]; line.hidden = false;
    }
    window.addEventListener('pagehide', stopMic);
    return {
      want: function (s) { want = s || null; if (!want || !want.mic) { stopMic(); micAsked = false; } paint(); },
      paint: paint,
      still: function () { return !motionOn || performance.now() - gotMotion > 1500 || (rotS < 4 && accDev < .08); },   // without the sensors, the picture alone decides
      turning: function () { return motionOn ? rotS : 0; },
      pose: function () { return { roll: 'roll' in POSE_SET ? POSE_SET.roll : roll, elev: 'elev' in POSE_SET ? POSE_SET.elev : elev, heading: 'heading' in POSE_SET ? POSE_SET.heading : heading }; },
      stab: function (cfg, now) {                     // degrees to shift the picture by, so the world holds still until the next snap
        var hold = (cfg && cfg.holdMs) || 700, most = (cfg && cfg.maxDeg) || 8;
        if (!motionOn || now - snapAt > hold || Math.abs(stabX) > most || Math.abs(stabY) > most) { stabX = 0; stabY = 0; snapAt = now; }
        return [stabX, -stabY];
      },
      // ripples for the view pass: up to four, as [x, y, age in seconds, strength], in the picture's own units from its centre
      fx: function (fx, now) {
        if (mic && want && want.mic) {
          mic.an.getFloatTimeDomainData(mic.buf);
          var s = 0, b = mic.buf; for (var i = 0; i < b.length; i++) s += b[i] * b[i];
          var lv = clamp((20 * Math.log10(Math.sqrt(s / b.length) + 1e-6) + 62) / 40, 0, 1);   // -62 dB of full scale is nothing, -22 is the loudest
          mic.mean = lerp(mic.mean, lv, .02);
          if (lv > mic.mean + .16 && now - mic.last > 170) { mic.last = now; rips.push({ x: (Math.random() - .5) * .3, y: (Math.random() - .5) * .3, t: now, a: clamp(lv, .3, 1) }); }
        }
        while (rips.length && (now - rips[0].t > 2600 || rips.length > 4)) rips.shift();
        if (!rips.length) return;
        fx.rip = rips.map(function (r) { return [r.x, r.y, (now - r.t) / 1000, r.a]; }); fx.ripK = calm ? .3 : 1;
      }
    };
  })();

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
  // A species' English name in lower case, except words that are names of places or people ("North American river otter",
  // "Cooper's hawk", "Schaus' swallowtail"). The first word is no exception: "domestic cat" starts small, as the names of groups do.
  var PROPER = ' african alaskan american andean antarctic antillean appalachian arabian arctic argentine asian asiatic atlantic australian bahama bahaman baltic bermuda bolivian brazilian british burmese california californian canada canadian caribbean carolina carolinian chilean chinese colombian colorado cuban dutch egyptian english eurasian european florida floridian french georgia german greek guatemalan gulf haitian hawaiian himalayan hispaniolan indian indies indonesian irish italian jamaican japanese javan korean louisiana madagascar malayan mediterranean mexican mississippi new nile norway norwegian pacific panama panamanian persian peruvian philippine polynesian portuguese puerto rican russian scotia scottish siberian spanish sumatran swedish swiss tasmanian texas texan thai turkish virginia virginian world york zealand amazon bolivia china peru lanka keys st. augustine charles sebastian william susan maria lizzie jones hentz caesar hercules jesus venus quaker confederate january february march april june july august september october november december acadian alachua alamo allegheny apache apalachicola arkansas baltimore bengal benghal blackburnian bradford brahminy caspian ceylon chickasaw columbian connecticut cretan darlington dixie everglades eustis fakahatchee formosa formosan georgian hebrew hudsonian illinois jerusalem kentucky maryland mascarene nashville nearctic neotropical ocala ohio okefenokee oklahoma ouachita oriental palamedes pandorus paraguayan pennsylvania philadelphia phoenician piedmont pharaoh polydamas polyphemus putnam rio grande santa saratoga savannah seminole shumard siam surinam tahitian taiwan taiwanese tampa tennessee tule yucatan zabulon zarucco julia isabella hermes phaon cassius dorantes eufala nessus dion io atala tokay muscovy bahia christmas halloween agrippina alyce anna delilah esther francesca ivana jair mabel sappho cyrano ';
  function nameCase(name) {
    name = String(name || ''); if (!name) return name;
    return name.replace(/[^\s-]+/g, function (w, at) {
      if (PROPER.indexOf(' ' + w.toLowerCase() + ' ') >= 0) return w.charAt(0).toUpperCase() + w.slice(1);
      var keep = /['’]s?$/.test(w) || (w.length <= 3 && w === w.toUpperCase() && /[A-Z]/.test(w) && (at > 0 || w.length === 1));
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
    senses.paint();
  }
  function go(screen) { S.screen = screen; paintUI(); }
  function setEyes(key, named) {
    S.eyes = key; S.named = named || null; eyeP = key ? paramsOf(EYES[key], named) : HUMAN; S.k = 0; S.kGoal = 0; S.tr = null; S.focus = S.focusGoal = .5;
    if (engine && engine.newView) engine.newView();            // a new pair of eyes starts with no memory of where the last one looked
    senses.want(eyeP.senses);
  }

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
    if (key && eyeP.senses) senses.fx(fx, now);
    return fx;
  }

  // ---------- a view being tried (?try=<key>): Start opens it on the camera at once, with no photograph first, and keeps no
  // encounter. Where the camera is closed, it asks for a clip or a photo of the person's view, as looking again does.
  // &genus=<Genus> chooses a genus's own settings (byGenus), as a name from the recognizer would.
  function tryStart() {
    var key = TRY_KEYS[0]; if (!key) return false;
    var g = (/[?&]genus=([A-Z][a-z]+)/.exec(location.search || '') || [0, ''])[1], named = { common: EYES[key].chip, scientific: g, by: 'you' };
    S.animalPhoto = null; S.meetingId = null; S.nov = ''; S.seq++; S.token++;
    function live() { thaw(); setEyes(key, named); go('animal'); showName(); later(startChange, calm ? 150 : 750); }
    function still() { showStill(blankStill(), false); setEyes(key, named); setViewPrompt(key); go('askView'); }
    openCamera(TUNE.draw === 'face' ? 'user' : 'environment').then(live, still);
    return true;
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
      if (fresh) { S.newFrame = false; S.lastVideoTime = vid.currentTime; engine.setFrame(vid, vid.videoWidth, vid.videoHeight, now, S.src === 'clip' ? vid.currentTime * 1000 : undefined); }
    }
    var fx = fxNow(now, dt), P = S.eyes ? mix(HUMAN, eyeP, S.k) : HUMAN;
    if (s === 'askView') fx.expo = .5;                       // the animal's photo sits dimmed behind the prompt
    engine.draw(P, fx, now, dt);
    if (rec && recX) { recX.drawImage(canvas, 0, 0, recCv.width, recCv.height); if (recOver) recX.drawImage(recOver, 0, 0); }
    perfSum += dt;
    if (++perfN >= 45) {   // a phone that falls behind gives up detail in the movement map first, and only then in the picture
      if (!sideAsked && !rec && perfSum / perfN > 42 && !engine.lighten() && engine.side() > 540) engine.setSide(Math.max(540, engine.side() * .75));
      perfN = 0; perfSum = 0;
    }
  }
