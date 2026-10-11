
  // ---------- naming
  var PROMPT = [
    'The attached photograph was taken by someone who wants to know what living thing is in it.',
    'Name the main living subject. Reply with only one JSON object, no other text, in this shape:',
    '{"found": true, "common": "Domestic cat", "scientific": "Felis catus", "eyes": "cat"}',
    'Rules:',
    '- "common" is the everyday English name, as fine as the photo supports. "scientific" is the Latin name at that level, or "" if you have none.',
    '- "eyes" is exactly one of: "cat" (any cat), "dog" (dogs, foxes, coyotes), "squirrel" (squirrels, chipmunks, rats, mice), "deer" (deer, horses, cattle, goats, sheep), "rabbit" (rabbits, hares), "hawk" (hawks, eagles, falcons, kites, ospreys), "wader" (herons, egrets, ibis, storks, cranes, limpkins, coots, moorhens, pigeons, doves, chickens, turkeys), "bird" (any other bird, with owls, ducks and vultures included), "alligator" (alligators, crocodiles), "reptile" (lizards, snakes, turtles), "frog" (frogs, toads), "bee" (bees, wasps), "insect" (any other insect), "plant" (plants, trees, flowers, mosses, ferns), "person" (a human being), "other" (anything else alive: fungi, spiders, fish, snails, other mammals).',
    '- If the main subject is a person, set "eyes" to "person", "common" to "A person", "scientific" to "", and say nothing else about them.',
    '- If nothing alive is the subject, reply {"found": false}.'
  ].join('\n');

  function openSheet(id) { show('scrim', true); show(id, true); }
  function anySheet() { return !$('claim').hidden || !$('record').hidden || !$('info').hidden || !$('keep').hidden; }
  function closeSheets() {
    var wasClaim = !$('claim').hidden;
    show('claim', false); show('record', false); show('info', false); show('keep', false); show('scrim', false);
    try { $('claimName').blur(); $('keepVideo').pause(); } catch (e) {}
    return wasClaim;
  }
  function dismissSheets() {                       // closed by the person, without saying who it was
    if (!closeSheets()) return;
    if (S.screen === 'finder') { thaw(); paintUI(); }
    else if (S.screen === 'naming' && !S.eyes) go('askAnimal');
  }
  function openClaim(sub) {
    $('claimSub').textContent = (sub ? sub + ' ' : '') + 'Type the kind of animal or plant, such as cat, heron or oak.'; $('claimName').value = ''; $('claimNote').textContent = ''; show('claimOtherRow', false);
    var offers = pocket.offers || [], box = $('claimOffers'); box.textContent = '';      // what the small model could not choose between
    offers.forEach(function (o) {
      var b = el('button', 'pill ghost', o.en || o.sci); b.type = 'button';
      b.addEventListener('click', function () { diag('offer', o.kind); reveal(o.kind, { common: clip(o.en || o.sci, 60), scientific: clip(o.sci, 80), by: 'you' }); });
      box.appendChild(b);
    });
    show('claimOfferBox', offers.length > 0);
    show('info', false); show('record', false); show('keep', false); openSheet('claim');
    setTimeout(function () { try { if (!$('claim').hidden) $('claimName').focus(); } catch (e) {} }, 80);
  }
  function setViewPrompt(key) {
    $('askViewText').textContent = (coarse ? 'Record a few seconds of what is in front of you, or photograph it.' : 'Choose a clip or a photo of what is in front of you.') +
      (key === 'person' ? '' : ' It returns as ' + EYES[key].who + ' may take it in.');
    $('askViewFine').textContent = '';
  }

  function reveal(key, named) {
    S.seq++; closeSheets(); setEyes(key, named); msg(''); noteMeeting(key, named);
    if (S.hasView) { thaw(); go('animal'); showName(); later(startChange, calm ? 150 : 750); return; }
    if (S.animalPhoto) showStill(S.animalPhoto, false);
    setViewPrompt(key);
    go('naming'); showName();
    later(function () { hideName(); go('askView'); }, calm ? 1400 : 2100);
  }
  function failName(why) {
    msg('');
    if (S.src === 'cam') go('finder'); else go('naming');
    openClaim(why + ' So you tell it.');
  }
  function identify() {
    if (!S.animalPhoto) return;
    var t = ++S.token; S.seq++;
    if (!capsSettled) { go('naming'); msg('Looking at what it is.'); }     // Claude's part of the page may still be arriving
    capsReady.then(function () { if (t === S.token) recognize(t); });
  }
  function recognizeHere(t) {                      // outside Claude: the page's own small model, on this device
    go('naming'); msg(pocket.line());
    pocket.progress(function () { if (t === S.token && S.screen === 'naming' && !S.eyes && !anySheet()) msg(pocket.line()); });
    pocket.recognize(S.animalPhoto, pocket.file).then(function (r) {
      if (t !== S.token) return;
      diag('pocket', JSON.stringify({ kind: r.kind, p: +r.kindP.toFixed(3), sp: r.species.slice(0, 3).map(function (x) { return [x.sci, +x.p.toFixed(3)]; }), ms: r.ms, model: r.model, backend: r.backend }).slice(0, 400));
      if (r.kind === 'none') { failName('Nothing alive was found in that photo.'); return; }
      pocket.offers = r.offers;
      var common = r.kind === 'person' ? 'A person' : r.named ? (r.named.en || r.named.sci) : handName(r.kind);
      reveal(r.kind, { common: clip(common, 60) || handName(r.kind), scientific: r.named ? clip(r.named.sci, 80) : '', by: 'page' });
    }, function (e) {
      if (t !== S.token) return;
      diag('pocket-error', String((e && e.code) || 'unknown'));
      failName((e && e.sentence) || 'It could not be recognized this time.');
    });
  }
  function recognize(t) {
    if (!inViewer && pocket.usable()) { recognizeHere(t); return; }
    if (!(sample && canImages)) {
      msg(''); if (S.src !== 'cam') go('naming'); else go('finder');
      diag('no-recognizer', inViewer ? (sample ? 'no-images' : 'no-sample') : 'outside');
      openClaim(inViewer ? 'Claude could not be reached from this view, so you tell it.' : (pocket.whyNot() || 'This page cannot recognize a photo here.') + ' So you tell it.');
      return;
    }
    if (nameCtl) nameCtl.abort();
    nameCtl = new AbortController(); var ctl = nameCtl;
    go('naming'); msg('Looking at what it is.');
    var slow = setTimeout(function () { if (t === S.token && S.screen === 'naming' && !S.eyes) msg('Still looking. If Claude asked your permission, answer it, or go back.'); }, 14000);
    S.animalPhoto.toBlob(function (blob) {
      if (t !== S.token) { clearTimeout(slow); return; }
      if (!blob) { clearTimeout(slow); failName('The photo could not be prepared.'); return; }
      sample.json(PROMPT, { images: [blob], modelTier: 'quick', signal: ctl.signal }).then(function (d) {
        clearTimeout(slow); if (t !== S.token) return;
        if (!d || typeof d !== 'object' || d.found === false) { failName('Nothing alive was found in that photo.'); return; }
        var key = String(d.eyes || 'other'); if (!EYES[key]) key = 'other';
        diag('recognized', key);
        reveal(key, { common: clip(d.common, 60) || handName(key), scientific: clip(d.scientific, 80), by: 'Claude' });
      }).catch(function (e) {
        clearTimeout(slow); if (t !== S.token) return;
        var code = e && e.code; if (code === 'cancelled') return;
        if (['not_granted', 'sampling_disabled', 'not_declared', 'capability_disabled', 'capability_removed', 'images_unavailable'].indexOf(code) >= 0) sample = null;
        diag('claude-error', String(code || 'unknown'));
        failName(code === 'rate_limited' ? 'Claude is busy just now.' : code === 'not_granted' ? 'Claude was not allowed to look.' : 'It could not be recognized this time.');
      });
    }, 'image/jpeg', .86);
  }
  function gotAnimalPhoto(c) {
    S.animalPhoto = c; S.meetingId = null; S.nov = ''; pocket.offers = []; setEyes(null); hideName();
    if (S.src === 'cam') { S.freeze = true; if (engine) engine.setImage(c); paintUI(); }
    else showStill(c, false);
    identify();
  }
  function shutter() {
    if (S.screen !== 'finder' || S.src !== 'cam' || S.freeze || !vid.videoWidth) return;
    $('flash').classList.remove('go'); void $('flash').offsetWidth; $('flash').classList.add('go');
    var c = fit(vid, vid.videoWidth, vid.videoHeight, 1280);
    if (S.mirror) { var m = makeCanvas(c.width, c.height), x = m.getContext('2d'); x.translate(c.width, 0); x.scale(-1, 1); x.drawImage(c, 0, 0); c = m; }
    msg(''); pocket.file = null; gotAnimalPhoto(c);
  }

  // ---------- back, wherever something might be done over
  function back() {
    var s = S.screen;
    if (anySheet()) { dismissSheets(); return; }
    S.seq++; hideName(); msg('');
    if (rec) { recDrop = true; stopRec(); }
    if (s === 'naming') {
      S.token++; if (nameCtl) nameCtl.abort();
      setEyes(null);
      if (S.src === 'cam') { thaw(); go('finder'); } else go('askAnimal');
      return;
    }
    if (s === 'animal') {
      setCamZoom(1);
      if (S.src === 'cam') { setEyes(null); go('finder'); }
      else { var key = S.eyes, nm = S.named; if (S.animalPhoto) showStill(S.animalPhoto, false); setEyes(key, nm); go('askView'); }
      return;
    }
    if (s === 'finder') { stopSource(); if (engine) engine.clear(); setEyes(null); go('intro'); return; }
    if (s === 'askView') { setEyes(null); go('askAnimal'); return; }
    if (s === 'askAnimal') { go('intro'); return; }
  }
  // outside Claude, the phone's own back gesture steps back through the app before it leaves the page
  var guard = false;
  function armBack() { if (inViewer || guard) return; try { history.pushState({ seenBack: 1 }, ''); guard = true; } catch (e) {} }
  window.addEventListener('popstate', function () {
    if (!guard) return; guard = false;
    if (S.screen !== 'intro' || anySheet()) { back(); if (S.screen !== 'intro' || anySheet()) armBack(); }
  });

  // ---------- recording and keeping
  var SERIF = '"Instrument Serif", "Iowan Old Style", Georgia, serif';
  function fileBase() { return 'seen-back-' + (shownName().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'view'); }
  function overlay(W, H) {           // the name, the caveat and the photo of who was met, laid over anything kept
    var c = makeCanvas(W, H), x = c.getContext('2d'), u = Math.max(W, H) / 100, pad = 3.2 * u, band = 26 * u, side = 0;
    var g = x.createLinearGradient(0, H - band, 0, H); g.addColorStop(0, 'rgba(0,0,0,0)'); g.addColorStop(1, 'rgba(0,0,0,.78)');
    x.fillStyle = g; x.fillRect(0, H - band, W, band);
    if (S.animalPhoto) {
      side = Math.round(Math.min(W, H) * .24);
      var p = S.animalPhoto, px = W - pad - side, py = H - pad - side, k = Math.max(side / p.width, side / p.height), rr = side * .12;
      x.save(); x.beginPath();
      if (x.roundRect) x.roundRect(px, py, side, side, rr); else x.rect(px, py, side, side);
      x.clip(); x.drawImage(p, px + (side - p.width * k) / 2, py + (side - p.height * k) / 2, p.width * k, p.height * k); x.restore();
      x.beginPath(); if (x.roundRect) x.roundRect(px, py, side, side, rr); else x.rect(px, py, side, side);
      x.lineWidth = Math.max(1, .28 * u); x.strokeStyle = 'rgba(255,255,255,.9)'; x.stroke();
    }
    var maxW = W - 2 * pad - (side ? side + pad : 0), name = shownName(), size = 5.6 * u;
    var small = Math.max(11, 1.85 * u), note = 'An approximation of what may reach ' + EYES[S.eyes].who + (guessed(S.eyes) ? ', part of it a guess.' : '.') + ' ' + labelDate(new Date());
    x.font = small + 'px system-ui, -apple-system, "Segoe UI", Roboto, sans-serif';
    var words = note.split(' '), lines = [''], i;
    for (i = 0; i < words.length; i++) {
      var tryLine = lines[lines.length - 1] ? lines[lines.length - 1] + ' ' + words[i] : words[i];
      if (x.measureText(tryLine).width > maxW && lines[lines.length - 1]) lines.push(words[i]); else lines[lines.length - 1] = tryLine;
    }
    x.fillStyle = 'rgba(255,255,255,.84)'; x.textBaseline = 'alphabetic';
    for (i = 0; i < lines.length; i++) x.fillText(lines[i], pad, H - pad - (lines.length - 1 - i) * small * 1.3);
    x.font = size + 'px ' + SERIF;
    while (x.measureText(name).width > maxW && size > 2.8 * u) { size -= .2 * u; x.font = size + 'px ' + SERIF; }
    x.fillStyle = '#fff'; x.fillText(name, pad, H - pad - lines.length * small * 1.3 - .6 * u);
    return c;
  }
  function startRec() {
    if (!canRecord() || !isMoving() || !S.eyes) return;
    var W = canvas.width, H = canvas.height, k = Math.min(1, 1280 / Math.max(W, H));
    recCv = makeCanvas(Math.round(W * k / 2) * 2, Math.round(H * k / 2) * 2); recX = recCv.getContext('2d');
    recOver = overlay(recCv.width, recCv.height);
    var types = ['video/mp4;codecs=avc1.42E01E', 'video/mp4', 'video/webm;codecs=vp9', 'video/webm;codecs=vp8', 'video/webm'];
    var type = types.filter(function (t) { try { return MediaRecorder.isTypeSupported(t); } catch (e) { return false; } })[0];
    try { rec = new MediaRecorder(recCv.captureStream(30), type ? { mimeType: type, videoBitsPerSecond: 5e6 } : undefined); }
    catch (e) { rec = null; recX = null; msg('Recording could not start.', 4000); return; }
    recChunks = []; recT0 = performance.now(); recDrop = false;
    var r = rec;
    r.ondataavailable = function (e) { if (e.data && e.data.size) recChunks.push(e.data); };
    r.onstop = function () {
      var mime = r.mimeType || type || 'video/webm', blob = new Blob(recChunks, { type: mime.split(';')[0] }), drop = recDrop;
      rec = null; recX = null; recOver = null; recDrop = false; clearInterval(recTimer); show('timer', false);
      $('btnRec').classList.remove('recording'); $('btnRec').setAttribute('aria-label', 'Record a clip');
      if (!drop && blob.size) keep({ blob: blob, name: fileBase() + (/mp4/.test(mime) ? '.mp4' : '.webm'), video: true });
    };
    r.start(500);
    $('btnRec').classList.add('recording'); $('btnRec').setAttribute('aria-label', 'Stop recording');
    show('timer', true); $('timer').textContent = '0:00'; msg('');
    recTimer = setInterval(function () {
      var s = Math.floor((performance.now() - recT0) / 1000); $('timer').textContent = Math.floor(s / 60) + ':' + ('0' + (s % 60)).slice(-2);
      if (s >= 30) stopRec();
    }, 250);
  }
  function stopRec() { if (rec && rec.state !== 'inactive') rec.stop(); }
  function snap() {
    if (!engine || !S.eyes || S.screen !== 'animal') return;
    var now = performance.now(), fx = fxNow(now, 0);
    engine.draw(mix(HUMAN, eyeP, S.k), fx, now, 16);
    var c = makeCanvas(canvas.width, canvas.height), x = c.getContext('2d');
    x.drawImage(canvas, 0, 0); x.drawImage(overlay(c.width, c.height), 0, 0);
    $('flash').classList.remove('go'); void $('flash').offsetWidth; $('flash').classList.add('go');
    c.toBlob(function (blob) { if (blob) keep({ blob: blob, name: fileBase() + '.jpg', video: false, canvas: c }); }, 'image/jpeg', .92);
  }
  function keep(k) {
    if (kept && kept.url) URL.revokeObjectURL(kept.url);
    kept = k; kept.url = URL.createObjectURL(k.blob);
    $('keepTitle').textContent = k.video ? 'Your clip' : 'Your still';
    $('keepNote').textContent = '';
    show('keepVideo', k.video); show('keepCv', !k.video);
    if (k.video) {
      $('keepVideo').onerror = function () { show('keepVideo', false); $('keepNote').textContent = 'Recorded. It cannot be played back in this view, so save it to watch it.'; };
      $('keepVideo').src = kept.url; $('keepVideo').play().catch(function () {});
    } else { var pv = $('keepCv'); pv.width = k.canvas.width; pv.height = k.canvas.height; pv.getContext('2d').drawImage(k.canvas, 0, 0); }
    var canShare = false;
    try { canShare = !inViewer && !!navigator.canShare && navigator.canShare({ files: [new File([k.blob], k.name, { type: k.blob.type })] }); } catch (e) { canShare = false; }
    show('keepShare', canShare); $('keepSave').className = canShare ? 'pill ghost' : 'pill';
    show('claim', false); show('record', false); show('info', false); openSheet('keep');
  }
  function saveKept() {
    if (!kept) return;
    if (!inViewer) {
      var a = document.createElement('a'); a.href = kept.url; a.download = kept.name; document.body.appendChild(a); a.click(); a.remove();
      $('keepNote').textContent = 'Sent to your downloads.'; return;
    }
    if (!downloads) { $('keepNote').textContent = 'Saving is unavailable in this view.'; return; }
    downloads.save({ filename: kept.name, data: kept.blob }).then(function () { $('keepNote').textContent = 'Saved.'; }).catch(function (e) {
      var code = e && e.code; $('keepNote').textContent = code === 'declined' ? '' : code === 'rate_limited' ? 'A save is already waiting for your answer.' : 'It could not be saved here.';
    });
  }
  function shareKept() {
    if (!kept) return;
    navigator.share({ files: [new File([kept.blob], kept.name, { type: kept.blob.type })] }).catch(function (e) {
      if (!e || e.name !== 'AbortError') $('keepNote').textContent = 'Sharing did not go through. Save it and send it from your files.';
    });
  }

  // ---------- the sheet behind the name
  function openInfo() {
    if (!S.eyes) return;
    var E = EYES[S.eyes];
    $('infoTitle').textContent = shownName();
    $('infoSub').textContent = (S.named && S.named.scientific ? S.named.scientific + '. ' : '') + (S.named && S.named.by === 'Claude' ? 'Recognized by Claude from your photo, which can be wrong.'
      : S.named && S.named.by === 'page' ? 'Recognized on this ' + (coarse ? 'phone' : 'computer') + ' by a small model, which can be wrong.' : 'As you said.');
    var ul = $('rows'); ul.textContent = '';
    E.rows.forEach(function (r) {
      var li = document.createElement('li'), m = document.createElement('i'), d = document.createElement('span'), b = document.createElement('b');
      m.className = 'mk' + (r[0] === 'i' ? '' : ' ' + r[0]); m.setAttribute('role', 'img');
      m.setAttribute('aria-label', r[0] === 'm' ? 'measured in this animal' : r[0] === 'g' ? 'measured in a relative' : r[0] === 'i' ? 'a guess' : 'left out');
      b.textContent = r[1] + '. '; d.appendChild(b); d.appendChild(document.createTextNode(r[2]));
      li.appendChild(m); li.appendChild(d); ul.appendChild(li);
    });
    $('info').scrollTop = 0; show('claim', false); show('record', false); openSheet('info');
  }

  // ---------- wiring
  $('claimForm').addEventListener('submit', function (e) {
    e.preventDefault();
    var t = clip($('claimName').value, 60), key = kindOfName(t);
    if (!t) { $('claimNote').textContent = 'Type what it was first.'; return; }
    if (!key) {                                    // a pet's own name, or a kind this page has no word for
      $('claimNote').textContent = '\u201C' + t + '\u201D is not a kind this page knows. Type what kind of animal or plant it is, such as cat. Its own name can come along: \u201CBiscuit, a cat\u201D.';
      $('claimOther').textContent = 'It is some other living thing. Keep \u201C' + t + '\u201D'; claimKept = t; show('claimOtherRow', true);
      return;
    }
    diag('said', key); reveal(key, { common: cap(t), scientific: '', by: 'you' });
  });
  $('introFine').textContent = engine ? '' : 'This browser cannot run the picture engine (WebGL 2). Try a current Chrome or Safari.';
  $('btnBegin').disabled = !engine;
  if (!coarse) { $('lblAnimalCam').hidden = true; $('lblAnimalPick').className = 'pill'; $('lblViewClip').hidden = true; $('lblViewCam').hidden = true; $('lblViewPick').className = 'pill'; $('lblViewPick').firstChild.nodeValue = 'Choose a clip or a photo'; }

  function toAskAnimal() {
    $('askFine').textContent = inViewer ? 'Inside Claude the camera is closed to this page, so it works from a photo of who you met and a clip of your view. If nothing opens when you tap, open this page in a browser in place of the Claude app.'
      : S.camRefused ? 'The camera was refused or missing, so this works from a photo of who you met and a clip of your view.' : '';
    go('askAnimal');
  }
  $('btnBegin').addEventListener('click', function () {
    armBack();
    if (!hasCamera || S.camRefused) { toAskAnimal(); return; }
    var btn = $('btnBegin'); btn.disabled = true;
    openCamera('environment').then(function () {
      btn.disabled = false; setEyes(null); go('finder'); msg('Photograph something alive, or choose a photo of it.', 4500);
    }, function () { btn.disabled = false; toAskAnimal(); });
  });
  $('btnShutter').addEventListener('click', shutter);
  $('btnBack').addEventListener('click', back);
  $('backAskAnimal').addEventListener('click', back);
  $('backAskView').addEventListener('click', back);
  var claimKept = '';
  $('claimOther').addEventListener('click', function () { if (claimKept) { diag('said', 'other'); reveal('other', { common: cap(claimKept), scientific: '', by: 'you' }); } });
  $('changeAskView').addEventListener('click', function () { openClaim(''); });
  $('claimBack').addEventListener('click', dismissSheets);
  $('recordClose').addEventListener('click', dismissSheets);
  $('introRec').addEventListener('click', openRecord);
  $('recAskAnimal').addEventListener('click', openRecord);
  $('btnRecF').addEventListener('click', openRecord);
  $('scrim').addEventListener('click', dismissSheets);
  $('btnWho').addEventListener('click', openInfo);
  $('infoClose').addEventListener('click', dismissSheets);
  $('infoChange').addEventListener('click', function () { openClaim(''); });
  $('btnFlip').addEventListener('click', function () {
    var f = S.facing === 'user' ? 'environment' : 'user';
    startCamera(f).then(paintUI).catch(function () { msg('The other camera could not be opened.', 4000); });
  });
  function hold(on) { return function (e) { if (e && e.cancelable) e.preventDefault(); S.holding = on; $('btnEyes').classList.toggle('on', on); if (on) msg('Your own eyes.'); else msg(''); }; }
  $('btnEyes').addEventListener('pointerdown', hold(true));
  ['pointerup', 'pointerleave', 'pointercancel'].forEach(function (ev) { $('btnEyes').addEventListener(ev, hold(false)); });
  $('btnEyes').addEventListener('keydown', function (e) { if ((e.key === ' ' || e.key === 'Enter') && !e.repeat) hold(true)(e); });
  $('btnEyes').addEventListener('keyup', function (e) { if (e.key === ' ' || e.key === 'Enter') hold(false)(e); });
  $('btnEyes').addEventListener('contextmenu', function (e) { e.preventDefault(); });
  $('btnRec').addEventListener('click', function () { if (rec) stopRec(); else startRec(); });
  $('btnSnap').addEventListener('click', snap);
  $('keepClose').addEventListener('click', dismissSheets);
  $('keepSave').addEventListener('click', saveKept);
  $('keepShare').addEventListener('click', shareKept);

  // a tap on the picture moves the focus, for eyes that have a shallow one
  var tap = null;
  canvas.addEventListener('pointerdown', function (e) { tap = { x: e.clientX, y: e.clientY, t: performance.now() }; });
  canvas.addEventListener('pointerup', function (e) {
    var t0 = tap; tap = null;
    if (!t0 || S.screen !== 'animal' || S.tr || !S.eyes || !EYES[S.eyes].dof) return;
    if (Math.hypot(e.clientX - t0.x, e.clientY - t0.y) > 12 || performance.now() - t0.t > 500) return;
    var r = canvas.getBoundingClientRect(), ring = $('focusRing');
    S.focusGoal = clamp(1 - (e.clientY - r.top) / r.height, .05, .95);
    ring.style.left = (e.clientX - r.left) + 'px'; ring.style.top = (e.clientY - r.top) + 'px';
    ring.classList.remove('go'); void ring.offsetWidth; ring.classList.add('go');
  });

  function onAnimalFile(e) {
    var f = e.target.files && e.target.files[0]; e.target.value = ''; if (!f) return;
    decode(f).then(function (c) { pocket.file = f; gotAnimalPhoto(c); }).catch(function () { if (S.screen === 'finder') msg('That file could not be read as a photo.', 5000); else $('askFine').textContent = 'That file could not be read as a photo.'; });
  }
  function onViewFile(e) {
    var f = e.target.files && e.target.files[0]; e.target.value = ''; if (!f || !S.eyes || !engine) return;
    var key = S.eyes, nm = S.named, isVideo = /^video\//.test(f.type) || /\.(mp4|mov|webm|m4v|3gp|mkv)$/i.test(f.name || '');
    S.seq++; $('askViewFine').textContent = 'Opening it.';
    (isVideo ? startClip(f) : decode(f).then(function (c) { showStill(c, true); })).then(function () {
      $('askViewFine').textContent = ''; setEyes(key, nm); go('animal'); showName(); later(startChange, calm ? 150 : 900);
    }).catch(function () {
      if (S.animalPhoto) showStill(S.animalPhoto, false);
      setEyes(key, nm); $('askViewFine').textContent = 'That file could not be opened. Try another.';
    });
  }
  $('inLib').addEventListener('change', onAnimalFile);
  $('inAnimalCam').addEventListener('change', onAnimalFile);
  $('inAnimalPick').addEventListener('change', onAnimalFile);
  $('inViewClip').addEventListener('change', onViewFile);
  $('inViewCam').addEventListener('change', onViewFile);
  $('inViewPick').addEventListener('change', onViewFile);
  window.addEventListener('pagehide', function () { if (S.stream) S.stream.getTracks().forEach(function (t) { t.stop(); }); });

  paintUI(); paintRecordBits();
  requestAnimationFrame(loop);
  window.__seenBack = { S: S, EYES: EYES, state: function () { return engine ? engine.state() : null; }, record: function () { return record; }, kindOfName: kindOfName,
    rec: pocket, diag: function () { return diagLog; }, about: aboutText,
    pose: function (t) { S.tr = t === null ? null : { t0: 0, dur: 1, fixed: t }; if (t === null) S.k = 1; } };   // hold the change of eyes at one instant, for checking

  // ---------- about this build: one block to copy from a real phone, to say how it ran there
  var frameMs = [], frameLast = 0;
  (function watchFrames2(now) {                    // how long the last frames took, measured here and not in the engine
    requestAnimationFrame(watchFrames2);
    if (frameLast && now - frameLast < 1000) { frameMs.push(now - frameLast); if (frameMs.length > 90) frameMs.shift(); }
    frameLast = now;
  })(0);
  function aboutText() {
    var a = pocket.about(), st = engine ? engine.state() : null, L = ['Seen Back, build ' + BUILD + '.'], r = a.last, avg = 0;
    frameMs.forEach(function (x) { avg += x; });
    avg = frameMs.length ? avg / frameMs.length : 0;
    if (inViewer) L.push('Recognizer: Claude, inside Claude’s viewer.');
    else if (a.state === 'ready') L.push('Recognizer: ' + a.model + ', ' + a.backend + (a.threads ? ', ' + a.threads + (a.threads === 1 ? ' thread' : ' threads') : '') + ', ready in ' + (a.loadMs / 1000).toFixed(1) + ' s.');
    else if (a.state === 'loading') L.push('Recognizer: loading' + (a.total ? ', ' + Math.round(a.got / 1e6) + ' of ' + Math.round(a.total / 1e6) + ' MB' : '') + '.');
    else if (a.state === 'idle') L.push('Recognizer: not started yet.');
    else L.push('Recognizer: not running. ' + (a.fail || a.why) + '.');
    if (r) L.push('Last photo: ' + r.kind + ' ' + r.kindP.toFixed(2) + (r.species[0] ? ', ' + r.species[0].sci + ' ' + r.species[0].p.toFixed(2) : '') + '; ' + (r.ms.load ? 'waited ' + r.ms.load + ' ms, ' : '') + 'prepared in ' + r.ms.pre + ' ms from ' + r.from + ', recognized in ' + r.ms.run + ' ms.');
    L.push('Picture: ' + canvas.width + ' by ' + canvas.height + (st && st.sw ? ', source ' + st.sw + ' by ' + st.sh : '') + (engine ? ', limit ' + engine.side() : ', no engine') +
      (avg ? ', ' + avg.toFixed(1) + ' ms a frame over the last ' + frameMs.length + '.' : '.'));
    L.push('Screen: ' + window.innerWidth + ' by ' + window.innerHeight + ' at ' + (window.devicePixelRatio || 1) + '. ' + (coarse ? 'Touch.' : 'Pointer.') + (S.camOK ? ' Camera open.' : S.camRefused ? ' Camera refused.' : ''));
    L.push(String(navigator.userAgent || '').slice(0, 200));
    return L.join('\n');
  }
  function paintAbout() { $('buildMark').textContent = aboutText(); $('aboutNote').textContent = ''; }
  $('about').addEventListener('toggle', function () { if ($('about').open) paintAbout(); });
  $('aboutCopy').addEventListener('click', function () {
    var text = aboutText(), note = $('aboutNote');
    $('buildMark').textContent = text;
    function byHand() {
      try {
        var sel = window.getSelection(), range = document.createRange(); range.selectNodeContents($('buildMark')); sel.removeAllRanges(); sel.addRange(range);
        note.textContent = document.execCommand('copy') ? 'Copied.' : 'It could not be copied from here. The lines are selected, so copy them by hand.';
      } catch (e) { note.textContent = 'It could not be copied from here. Select the lines and copy them by hand.'; }
    }
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(function () { note.textContent = 'Copied.'; }, byHand); else byHand();
  });
  pocket.warm();
  if (inViewer) {
    window.claude.use('sample').then(function (s) {
      if (!s) return;
      return s.limits().then(function (lim) { sample = s; canImages = !!(lim && lim.images); }, function () { sample = s; canImages = false; });
    }).catch(function () {}).then(capsDone);
    setTimeout(capsDone, 8000);                     // a viewer that never answers is treated as having no Claude
    window.claude.use('downloads').then(function (d) { downloads = d; }).catch(function () {});
    initRemote();
  }
