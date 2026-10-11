
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
  function anySheet() { return !$('claim').hidden || !$('record').hidden || !$('info').hidden || !$('keep').hidden || !$('ask').hidden || !$('big').hidden; }
  function closeSheets() {
    var wasClaim = !$('claim').hidden;
    show('claim', false); show('record', false); show('info', false); show('keep', false); show('ask', false); show('big', false); show('scrim', false);
    try { $('claimName').blur(); $('keepVideo').pause(); } catch (e) {}
    return wasClaim;
  }
  function dismissSheets() {                       // closed by the person, without saying who it was
    var first = askFirstT; askFirstT = 0;
    if (!closeSheets()) { if (first && first === S.token && !S.eyes) askName(''); return; }   // the question to the server was opened from the sheet that asks for a name: back to it
    if (S.screen === 'finder') { thaw(); paintUI(); }
    else if (S.screen === 'naming' && !S.eyes) go('askAnimal');
    paintType();
  }
  function openClaim(sub) {
    var kinds = pocket.kindOffers || [], kbox = $('claimKinds'); kbox.textContent = '';   // not sure of the kind: its three likeliest, as buttons above the typed field
    $('claimSub').textContent = sub || ''; $('claimName').value = ''; $('claimNote').textContent = ''; show('claimOtherRow', false);   // the field's own words say what to type
    kinds.forEach(function (key) {
      var name = key === 'person' ? 'A person' : handName(key), b = el('button', 'pill ghost', name); b.type = 'button';
      b.addEventListener('click', function () { diag('kind-offer', key); reveal(key, { common: name, scientific: '', by: 'you' }); });
      kbox.appendChild(b);
    });
    show('claimKindBox', kinds.length > 0); $('claimOfferNote').textContent = kinds.length ? 'Or one of these species.' : 'It may be one of these.';
    var offers = offerList(pocket.offers || []), box = $('claimOffers'); box.textContent = '';      // what the small model could not choose between
    offers.forEach(function (o) {
      var b = el('button', 'pill ghost', o.label); b.type = 'button';
      b.addEventListener('click', function () { diag('offer', o.kind); reveal(o.kind, { common: clip(o.en || o.sci, 60), scientific: clip(o.sci, 80), by: 'you', local: !!o.local }); });
      box.appendChild(b);
    });
    show('claimOfferBox', offers.length > 0);
    show('info', false); show('record', false); show('keep', false); show('ask', false); show('big', false); openSheet('claim');
    paintClaimAsk();
    setTimeout(function () { try { if (!$('claim').hidden) $('claimName').focus(); } catch (e) {} }, 80);
  }
  // The offers as buttons: one species twice (one name filed under two keys) is offered once, and two species that share an English
  // name each carry the scientific name, so that no two buttons read the same.
  function offerList(list) {
    var seen = {}, n = {}, low = function (x) { return String(x || '').toLowerCase(); };
    var keep = list.filter(function (o) { var k = low(o.sci || o.en); if (!k || seen[k]) return false; seen[k] = 1; return true; });
    keep.forEach(function (o) { var w = low(o.en || o.sci); n[w] = (n[w] || 0) + 1; });
    return keep.map(function (o) { return { sci: o.sci, en: o.en, kind: o.kind, local: o.local, label: o.en && o.sci && n[low(o.en)] > 1 ? o.en + ' (' + o.sci + ')' : o.en || o.sci }; });
  }
  function setViewPrompt(key) {
    $('askViewH').textContent = key === 'person' ? 'Now your view.' : 'Now see as ' + (key === 'other' ? 'this living thing' : EYES[key].who) + '.';   // EYES.other.who is "this one", which reads badly here
    $('askViewText').textContent = '';
    $('askViewFine').textContent = '';
  }

  function reveal(key, named) {
    S.seq++; closeSheets(); setEyes(key, named); msg(''); noteMeeting(key, named); paintType();
    if (named && (named.by === 'service' || named.by === 'device-large')) paintSvc(); else dropSvc();     // a name said by the person, or a new photo, ends any question still out
    if (S.hasView) { thaw(); go('animal'); showName(); later(startChange, calm ? 150 : 750); return; }
    if (S.animalPhoto) showStill(S.animalPhoto, false);
    setViewPrompt(key);
    go('naming'); showName();
    if (!calm) later(hideName, 1500);              // the name has faded on the picture (half a second) before "Now your view." comes up
    later(function () { hideName(); go('askView'); }, calm ? 1400 : 2100);
  }
  function askName(sub) {
    msg('');
    if (S.src === 'cam') go('finder'); else go('naming');
    openClaim(sub); paintType();
  }
  function failName(why) { askName(why + ' So you tell it.'); }
  // While the recognizer is being downloaded for the first time, the person may type the name and not wait. The download carries on.
  function paintType() { show('barType', !inViewer && S.screen === 'naming' && !S.eyes && !anySheet() && pocket.fetching()); }
  function identify() {
    if (!S.animalPhoto) return;
    var t = ++S.token; S.seq++;
    if (!capsSettled) { go('naming'); msg('Looking at what it is.'); }     // Claude's part of the page may still be arriving
    capsReady.then(function () { if (t === S.token) recognize(t); });
  }
  function recognizeHere(t) {                      // outside Claude: the page's own small model, on this device
    go('naming'); msg(pocket.line()); paintType();
    pocket.progress(function () { if (t === S.token && S.screen === 'naming' && !S.eyes && !anySheet()) msg(pocket.line()); paintType(); });
    pocket.recognize(S.animalPhoto, pocket.file).then(function (r) {
      if (t !== S.token) return;
      diag('pocket', JSON.stringify({ kind: r.kind, p: +r.kindP.toFixed(3), sp: r.species.slice(0, 3).map(function (x) { return [x.sci, +x.p.toFixed(3)]; }), ms: r.ms, model: r.model, backend: r.backend }).slice(0, 400));
      if (r.kind === 'none' && r.sure) { failName('Nothing alive was found in that photo.'); return; }
      pocket.offers = r.offers.map(function (o) { return { sci: o.sci, en: o.en, kind: o.kind, local: true }; });
      pocket.kindOffers = r.kindOffers || [];
      if (!r.sure) {
        // Not sure is an answer: no kind is asserted and no eyes change. Where the larger model is on this device it is asked before the person is.
        diag('not-sure', r.kind + ' ' + r.kindP.toFixed(3));
        large.survey().then(function (h) {
          if (t !== S.token || S.eyes) return;
          if (h === 'kept' && !large.broken()) firstLook(t, true); else askName('The recognizer is not sure what that is.');
        });
        return;
      }
      var common = r.kind === 'person' ? 'A person' : r.named ? (r.named.en || r.named.sci) : handName(r.kind);
      reveal(r.kind, { common: clip(common, 60) || handName(r.kind), scientific: r.named ? clip(r.named.sci, 80) : '', by: 'page', local: !!r.named });
      closer(t, !!r.named);                                                // the kind is in use at once; a finer name may follow from a larger model
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
    S.animalPhoto = c; S.meetingId = null; S.nov = ''; pocket.offers = []; pocket.kindOffers = []; S.closer = 0; askFirstT = 0; if (firstJob) { firstJob.cancel(); firstJob = null; } setEyes(null); hideName(); dropSvc();
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
  function back() { if (firstJob) { firstJob.cancel(); firstJob = null; } backStep(); paintSvc(); }
  function backStep() {
    var s = S.screen;
    if (anySheet()) { dismissSheets(); return; }
    S.seq++; hideName(); msg('');
    if (rec) { recDrop = true; stopRec(); }
    if (s === 'naming') {
      S.token++; if (nameCtl) nameCtl.abort();
      setEyes(null);
      if (S.src === 'cam') { thaw(); go('finder'); } else go('askAnimal');
      paintType();
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
    show('keepShare', canShare); $('keepSave').className = canShare ? 'ico' : 'ico on';
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
      : S.named && S.named.by === 'page' ? 'Recognized on this ' + (coarse ? 'phone' : 'computer') + ' by a small model, which can be wrong.'
      : S.named && S.named.by === 'service' ? 'Named by a larger model on a server, which can be wrong.'
      : S.named && S.named.by === 'device-large' ? 'Named on this device by a larger model, which can be wrong.' : 'As you said.')
      + (S.named && S.named.local ? ' Chosen among species recorded around ' + pocket.place() + '.' : '');
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
  if (!coarse) { $('lblAnimalCam').hidden = true; $('lblViewClip').hidden = true; $('lblViewCam').hidden = true;    // one way in, so it is said in words
    [['lblAnimalPick', 'Choose a photo'], ['lblViewPick', 'Choose a clip or a photo']].forEach(function (p) { var l = $(p[0]), s = l.querySelector('svg'); l.className = 'pill'; if (s) l.removeChild(s); l.insertBefore(document.createTextNode(p[1]), l.firstChild); }); }

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

  // ---------- the larger model on a server (the naturalist), asked only with the person's say-so
  // One line on the picture carries it: an offer to ask (tappable), "Asking the larger model.", the waking sentence, what it said,
  // and, where it sees another kind of creature and is sure enough, an offer to change eyes (tappable). The eyes never change by themselves.
  var SVC_SAY = { offer: 'A larger model on a server can try to name the species. Ask it?', asking: 'Asking the larger model.', waking: 'The larger model is waking up, which can take a minute.', looking: 'Looking more closely.' };
  var svcTimer = 0, svcTap = null, askFirstT = 0, firstJob = null;
  function renewName() { if ($('reveal').classList.contains('show') && (S.screen === 'naming' || S.screen === 'animal') && !anySheet()) showName(); }     // a finer name that arrives while the first is still large on the picture takes its place there; later, the line on the picture says it
  function aAn(name) { return (/^[aeiou]/i.test(name) ? 'an ' : 'a ') + name; }
  function paintSvc() {
    var v = S.svc;
    if (v && (v.t !== S.token || !S.eyes)) { S.svc = null; if (v.job) v.job.cancel(); v = null; }     // it belonged to a photo that is no longer in hand
    var text = v ? (v.text || (v.state === 'get' ? getLine() : SVC_SAY[v.state]) || '') : '', tap = v && (v.state === 'offer' || v.state === 'change' || v.state === 'get') ? tapSvc : null;
    if (!text && bigNote) { text = bigNote.text; tap = bigNote.tap; }     // the larger model's download belongs to no one photo: its line shows whenever the photo has none of its own
    svcTap = tap;
    ['svcHud', 'svcView'].forEach(function (id) { var b = $(id); b.textContent = text; b.disabled = !tap; b.hidden = !text; });
  }
  function dropSvc() { var v = S.svc; S.svc = null; clearTimeout(svcTimer); if (v && v.job) v.job.cancel(); paintSvc(); }
  function considerService(t) {
    var photo = S.animalPhoto;
    naturalist.config().then(function (c) {            // service.json is asked for here, the first time a photo is left without a species name
      if (!c || t !== S.token || photo !== S.animalPhoto || !S.eyes || !S.named || S.named.by !== 'page' || navigator.onLine === false) return;
      var ch = naturalist.choice();
      if (ch === 'no') return;
      if (ch === 'yes') askService(t); else { S.svc = { t: t, state: 'offer' }; paintSvc(); }
    });
  }
  function askService(t) {
    var photo = S.animalPhoto; if (!photo || t !== S.token || !S.eyes) return;
    var v = { t: t, state: 'asking' };
    if (S.svc && S.svc.job) S.svc.job.cancel();
    v.job = naturalist.ask(photo, { month: new Date().getMonth() + 1, local: pocket.local !== false }, function (state) { if (S.svc === v && v.state !== state) { v.state = state; paintSvc(); } });
    S.svc = v; paintSvc(); diag('service-ask', pocket.local !== false ? 'region' : 'no-region');
    v.job.promise.then(function (a) { if (S.svc === v) gotService(a, t); }, function (e) {
      diag('service-none', String((e && e.code) || 'unknown'));
      if (S.svc === v) { S.svc = null; paintSvc(); }   // every failure lets go quietly: what the device said stands
    });
  }
  function gotService(a, t) {
    var c = naturalist.cfg(), top = a.species[0];
    S.svc = null; clearTimeout(svcTimer);
    diag('service', JSON.stringify({ top: top ? [top.sci, +top.p.toFixed(3), top.kind] : null, kinds: a.kinds.slice(0, 2).map(function (k) { return [k.key, +k.p.toFixed(3)]; }), ms: a.ms, model: a.model, region: a.region }).slice(0, 300));
    if (!top || !c || !S.eyes) { paintSvc(); return; }
    pocket.offers = a.species.slice(0, 5).map(function (s) { return { sci: s.sci, en: s.en, kind: s.kind, local: !!a.region }; });   // its five likeliest are kept for the sheet that corrects a name
    var named = { common: clip(top.en || top.sci, 60), scientific: clip(top.sci, 80), by: 'service', local: !!a.region };
    var kp = a.kinds.filter(function (k) { return k.key === top.kind; })[0], kindP = kp ? kp.p : top.p;
    if (top.p >= c.nameAt && top.kind === S.eyes) {
      // the same kind of eye, a finer name: on screen, in the sheet behind the name, and in the record
      S.named = named; noteMeeting(S.eyes, named); paintUI(); renewName();
      S.svc = { t: t, state: 'said', text: 'The larger model says ' + named.common + '.' };
      svcTimer = setTimeout(function () { if (S.svc && S.svc.state === 'said') { S.svc = null; paintSvc(); } }, 10000);
    } else if (top.p >= c.nameAt && top.kind !== S.eyes && top.kind !== 'person' && c.kindAt !== null && kindP >= c.kindAt) {
      // another kind of creature, and the larger model is sure enough by the service's own setting: the change is offered, never made
      S.svc = { t: t, state: 'change', kind: top.kind, named: named, text: 'It looks like ' + aAn(named.common) + (top.kind === 'other' ? '' : ', ' + EYES[top.kind].who) + '. Change eyes?' };
    }
    paintSvc();
  }
  function tapSvc() {
    var v = S.svc; if (!v) return;
    if (v.state === 'offer') {
      var c = naturalist.cfg(); if (!c) return;
      $('askSub').textContent = 'This one photo, made smaller, would be sent to a server run for this project, ' + c.where + '. ' +
        (pocket.local !== false && c.region ? 'The month and the name of this region go with it. ' : 'The month goes with it. ') + 'The photo is not kept there.';
      $('askKeep').checked = false;
      show('claim', false); show('record', false); show('info', false); show('keep', false); openSheet('ask');
    } else if (v.state === 'change') { S.svc = null; diag(v.named.by === 'service' ? 'service-eyes' : 'large-eyes', v.kind); reveal(v.kind, v.named); }
    else if (v.state === 'get') openBig();
  }
  function answerAsk(yes) {
    if ($('askKeep').checked) naturalist.setChoice(yes ? 'yes' : 'no');
    var first = askFirstT; askFirstT = 0;
    closeSheets(); diag('service-say', (yes ? 'yes' : 'no') + ($('askKeep').checked ? '-kept' : ''));
    if (first) { if (first === S.token && !S.eyes) { if (yes) firstService(first); else askName(''); } return; }
    var v = S.svc; if (!v || v.state !== 'offer') return;
    if (yes) askService(v.t); else { S.svc = null; paintSvc(); }
  }
  $('svcHud').addEventListener('click', function () { if (svcTap) svcTap(); }); $('svcView').addEventListener('click', function () { if (svcTap) svcTap(); });
  $('askYes').addEventListener('click', function () { answerAsk(true); });
  $('askNo').addEventListener('click', function () { answerAsk(false); });
  $('askClose').addEventListener('click', dismissSheets);
  // ---------- the larger model on this device (models/naturalist): fetched once if the person says so, then every photo is named here
  // The choice is kept in this browser: '' (ask when a photo is left without a species name), 'no' (do not offer it), 'yes' (asked for:
  // a download that was interrupted carries on by itself), 'kept' (it arrived whole: if it is gone later, nothing is fetched unasked).
  var BIG_KEY = 'seenback.large.v1', bigMem = '', bigNote = null, bigNoteTimer = 0, bigDelAsked = false;
  function bigChoice() { try { var v = localStorage.getItem(BIG_KEY); return v === 'yes' || v === 'no' || v === 'kept' ? v : ''; } catch (e) { return bigMem; } }
  function setBigChoice(v) { bigMem = v; try { if (v) localStorage.setItem(BIG_KEY, v); else localStorage.removeItem(BIG_KEY); } catch (e) {} }
  function dev() { return coarse ? 'phone' : 'computer'; }
  function netSays() {                             // what the connection says of itself, where it says anything
    var c = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
    if (!c) return '';
    if (c.saveData) return 'This ' + dev() + ' is set to save data';
    if (c.metered === true || c.type === 'cellular') return 'This connection reports itself as metered';
    if (/^(slow-2g|2g|3g)$/.test(c.effectiveType || '')) return 'This connection reports itself as slow';
    return '';
  }
  function getLine() {
    var z = large.size(), h = large.has();
    // it had arrived whole and is not here now (the browser cleared it away, or the model was replaced by a newer one): said as it is
    if (bigChoice() === 'kept' && h !== 'kept') return 'The larger model is no longer on this ' + dev() + '. Get it again?';
    return z && h === 'partial' ? 'The larger model is partly on this ' + dev() + ': ' + z.keptMb + ' of ' + z.mb + ' MB. Get the rest?' : 'A larger model can name the species on this ' + dev() + '. Get it?';
  }
  function noteBig(text, tap, ms) {                // one line for the download: its progress, its end, its failure
    clearTimeout(bigNoteTimer); bigNote = text ? { text: text, tap: tap || null } : null;
    if (text && ms) bigNoteTimer = setTimeout(function () { bigNote = null; paintSvc(); }, ms);
    paintSvc(); if ($('about').open) paintBig();
    if (!$('big').hidden && large.has() === 'getting') $('bigNet').textContent = large.line();
  }
  function openBig() {                             // consent first, in plain words; and while it is being fetched, the same sheet stops it
    var z = large.size(), h = large.has(), s = z && z.seconds, n = netSays(), getting = h === 'getting', rest; if (!z) return;
    rest = Math.max(1, z.mb - (h === 'partial' ? z.keptMb : 0));
    $('bigTitle').textContent = getting ? 'Getting the larger model' : h === 'partial' ? 'Get the rest of the larger model?' : 'Get a larger model?';
    $('bigSub').textContent = 'It names the species. About ' + z.mb + ' MB, downloaded once, kept on this ' + dev() + '. Photos stay here. ' +
      (s && coarse && typeof s.phone === 'number' ? 'On a phone it takes about ' + Math.round(s.phone) + (Math.round(s.phone) === 1 ? ' second' : ' seconds') + ' a photo.'
        : s && typeof s.computer === 'number' ? 'On a computer it takes about ' + Math.round(s.computer) + (Math.round(s.computer) === 1 ? ' second' : ' seconds') + ' a photo.' + (coarse ? ' No phone has been timed yet.' : '')
        : 'It takes several seconds a photo on a computer. No phone has been timed yet.');   // what was measured, and nothing else
    $('bigNet').textContent = getting ? large.line() : (h === 'partial' ? z.keptMb + ' of ' + z.mb + ' MB are here already. ' : '') + (n ? n + ', and ' + (h === 'partial' ? 'the rest' : 'this download') + ' is about ' + rest + ' MB.' : '');
    $('bigYes').textContent = h === 'partial' ? 'Get the rest' : 'Get it';
    show('bigYes', !getting); show('bigNo', !getting); show('bigNever', !getting); show('bigStop', getting);
    show('claim', false); show('record', false); show('info', false); show('keep', false); show('ask', false); openSheet('big');
  }
  function answerBig(what) {
    var v = S.svc;
    closeSheets(); diag('large-say', what);
    if (v && v.state === 'get') { S.svc = null; paintSvc(); }
    if (what === 'yes') startBig(); else if (what === 'never') setBigChoice('no');
  }
  function startBig() {
    if (large.has() === 'getting') return;
    setBigChoice('yes');
    try { if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(function () {}); } catch (e) {}   // so that the browser does not clear it away by itself
    large.progress(function () { if (large.has() === 'getting') noteBig(large.line(), openBig); });
    var p = large.get(); noteBig(large.line(), openBig);
    p.then(function () {
      setBigChoice('kept'); if (!$('big').hidden) closeSheets();
      noteBig('The larger model is on this ' + dev() + '.', null, 8000);
      // the photo in hand is looked at now, if the small model's answer is still what stands
      if (S.eyes && S.eyes !== 'person' && S.named && S.named.by === 'page' && !S.svc) lookCloser(S.token);
    }, function (e) {
      var code = (e && e.code) || 'died', z = large.size(), again = /^(network|missing|damaged|died|slow)$/.test(code);
      if (!$('big').hidden) closeSheets();
      if (code === 'stopped') { setBigChoice(''); noteBig('The download was stopped.' + (z && z.keptMb ? ' ' + z.keptMb + ' of ' + z.mb + ' MB are kept on this ' + dev() + '.' : ''), null, 8000); return; }
      if (!again) setBigChoice('');
      noteBig(((e && e.sentence) || large.say(code)) + (again ? ' Try again?' : ''), again ? startBig : null, 30000);
    });
  }
  function five(r) { return r.species.slice(0, 5).map(function (x) { return { sci: x.sci, en: x.en, kind: x.kind, local: true }; }); }
  function largeName(r) { return r.local && r.named ? { common: clip(r.named.en || r.named.sci, 60) || handName(r.kind), scientific: clip(r.named.sci, 80), by: 'device-large', local: true } : null; }
  function noteLarge(r) { diag('large', JSON.stringify({ kind: r.kind, p: +r.kindP.toFixed(3), sure: r.sure, sp: r.species.slice(0, 2).map(function (x) { return [x.sci, +x.p.toFixed(3)]; }), ms: r.ms, model: r.model }).slice(0, 300)); }
  // After the small model's answer is in use. Where the larger model is on this device it looks at every photo in the background. Where it
  // is not, a photo left without a species name raises the offer to get it. Where there is no such model, or the person wants none,
  // the server is considered, as before: so the device comes first where both exist.
  function closer(t, named) {
    var photo = S.animalPhoto;
    large.survey().then(function (h) {
      if (t !== S.token || photo !== S.animalPhoto || !S.eyes || !S.named || S.named.by !== 'page') return;
      if (h === 'kept' && !large.broken()) { if (S.eyes !== 'person') lookCloser(t); return; }
      if (named || S.eyes === 'person') return;
      if (h === 'none' || h === 'kept' || bigChoice() === 'no') { considerService(t); return; }
      if (h === 'getting') { paintSvc(); return; }
      if (navigator.onLine === false) return;
      S.svc = { t: t, state: 'get' }; paintSvc();
    });
  }
  function lookCloser(t) {                         // in the background: the eyes are in use already
    var photo = S.animalPhoto; if (!photo || t !== S.token || !S.eyes) return;
    var v = { t: t, state: 'looking' };
    if (S.svc && S.svc.job) S.svc.job.cancel();
    S.svc = v; paintSvc();
    large.recognize(photo, pocket.file).then(function (r) { if (S.svc === v) gotCloser(r, t); }, function (e) {
      diag('large-none', String((e && e.code) || 'unknown'));
      if (S.svc === v) { S.svc = null; paintSvc(); }   // every failure lets go quietly: what the small model said stands
    });
  }
  function gotCloser(r, t) {
    var named = largeName(r);
    S.svc = null; clearTimeout(svcTimer); S.closer = t; noteLarge(r);
    if (!S.eyes) { paintSvc(); return; }
    if (r.local && r.species.length) pocket.offers = five(r);          // its five likeliest are kept for the sheet that corrects a name
    if (r.sure && r.kind === S.eyes && named) {
      // the same kind of eye, a finer name: on screen, in the sheet behind the name, and in the record
      S.named = named; noteMeeting(S.eyes, named); paintUI(); renewName();
      S.svc = { t: t, state: 'said', text: 'The larger model says ' + named.common + '.' };
      svcTimer = setTimeout(function () { if (S.svc && S.svc.state === 'said') { S.svc = null; paintSvc(); } }, 10000);
    } else if (r.sure && r.kindAt !== null && r.kind !== S.eyes && r.kind !== 'person' && r.kind !== 'none') {
      // another kind of creature, and the larger model is sure enough by its slot's own setting: the change is offered, never made
      S.svc = { t: t, state: 'change', kind: r.kind, named: named || { common: handName(r.kind), scientific: '', by: 'device-large', local: false },
        text: 'It looks like ' + (named ? aAn(named.common) + (r.kind === 'other' ? '' : ', ' + EYES[r.kind].who) : r.kind === 'other' ? 'some other living thing' : EYES[r.kind].who) + '. Change eyes?' };
    }
    paintSvc();
  }
  // Nothing has a name yet: the small model was not sure, or the person asked from the sheet that asks for a name. The larger model's
  // answer is waited for, and taken; if it is not sure either, its three likeliest kinds are offered.
  function firstLook(t, unsure) {
    var photo = S.animalPhoto; if (!photo || t !== S.token) return;
    closeSheets(); go('naming'); msg(SVC_SAY.looking); paintType();
    large.recognize(photo, pocket.file).then(function (r) {
      if (t !== S.token || S.eyes) return;
      S.closer = t; noteLarge(r);
      if (r.local && r.species.length) pocket.offers = five(r);
      if (r.sure && r.kind === 'none') { pocket.kindOffers = []; failName('Nothing alive was found in that photo.'); return; }     // a larger slot with a kinds head can say so
      if (r.sure) { reveal(r.kind, largeName(r) || { common: r.kind === 'person' ? 'A person' : handName(r.kind), scientific: '', by: 'device-large', local: false }); return; }
      pocket.kindOffers = r.kindOffers || [];
      askName(unsure ? 'The recognizer and the larger model are both not sure what that is.' : 'The larger model is not sure what that is.');
    }, function (e) {
      if (t !== S.token || S.eyes) return;
      S.closer = t; diag('large-none', String((e && e.code) || 'unknown'));
      askName(unsure ? 'The recognizer is not sure what that is.' : ((e && e.sentence) || large.say('photo')) + ' So you tell it.');
    });
  }
  // The same from the server, where that is the larger model there is: asked with the person's say-so, and its answer taken as the name.
  function firstService(t) {
    var photo = S.animalPhoto; if (!photo || t !== S.token) return;
    go('naming'); msg(SVC_SAY.asking); paintType(); S.closer = t;
    var job = naturalist.ask(photo, { month: new Date().getMonth() + 1, local: pocket.local !== false }, function (state) { if (t === S.token && !S.eyes && S.screen === 'naming' && !anySheet()) msg(SVC_SAY[state] || ''); });
    firstJob = job; diag('service-ask', 'first');
    job.promise.then(function (a) {
      if (firstJob === job) firstJob = null;
      if (t !== S.token || S.eyes) return;
      var c = naturalist.cfg(), top = a.species[0];
      pocket.offers = a.species.slice(0, 5).map(function (x) { return { sci: x.sci, en: x.en, kind: x.kind, local: !!a.region }; });
      if (top && c && top.p >= c.nameAt && top.kind !== 'person') { reveal(top.kind, { common: clip(top.en || top.sci, 60), scientific: clip(top.sci, 80), by: 'service', local: !!a.region }); return; }
      askName('The larger model could not name it.');
    }, function (e) {
      if (firstJob === job) firstJob = null;
      if (t !== S.token || S.eyes) return;
      diag('service-none', String((e && e.code) || 'unknown'));
      if (e && e.code === 'cancelled') return;
      askName('The larger model could not be asked just now.');
    });
  }
  // From the sheet that asks for a name there is a way to a larger model, where there is one: on this device first, else on a server.
  var claimAskHow = '';
  function paintClaimAsk() {
    show('claimAskRow', false); claimAskHow = '';
    if (inViewer || S.eyes || !S.animalPhoto || S.closer === S.token) return;     // not where a larger model has had this photo already
    var t = S.token;
    function still() { return t === S.token && !$('claim').hidden && !S.eyes; }
    large.survey().then(function (h) {
      if (!still()) return;
      if (h === 'kept' && !large.broken()) { $('claimAsk').textContent = 'Look more closely, with the larger model on this ' + dev(); claimAskHow = 'device'; show('claimAskRow', true); return; }
      naturalist.config().then(function (c) {
        if (!c || !still() || navigator.onLine === false || naturalist.choice() === 'no') return;
        $('claimAsk').textContent = 'Ask a larger model on a server'; claimAskHow = 'service'; show('claimAskRow', true);
      });
    });
  }
  $('claimAsk').addEventListener('click', function () {
    var t = S.token, c = naturalist.cfg();
    if (claimAskHow === 'device') { diag('large-asked', ''); firstLook(t, false); return; }
    if (claimAskHow !== 'service' || !c) return;
    if (naturalist.choice() === 'yes') { closeSheets(); firstService(t); return; }
    $('askSub').textContent = 'This one photo, made smaller, would be sent to a server run for this project, ' + c.where + '. ' +
      (pocket.local !== false && c.region ? 'The month and the name of this region go with it. ' : 'The month goes with it. ') + 'The photo is not kept there.';
    $('askKeep').checked = false;
    closeSheets(); askFirstT = t; openSheet('ask');
  });
  function paintBig() {                            // in the About block: where the larger model stands, and the ways to get it, stop it and delete it
    large.survey().then(function () {
      var h = large.has(), z = large.size(), a = large.about(), d = dev(), fail = a.getFail && !/^stopped/.test(a.getFail) ? ' ' + large.say(a.getFail.split(':')[0]) : '';
      if (!z || !h) { show('bigBox', false); return; }
      $('bigState').textContent = bigDelAsked ? 'Delete the larger model from this ' + d + '? It is ' + (h === 'kept' ? z.mb : z.keptMb) + ' MB, and would have to be downloaded again.'
        : h === 'getting' ? large.line()
        : h === 'kept' ? 'The larger model is on this ' + d + ' (' + z.mb + ' MB). It names the species here, and photos are not sent anywhere.' + (a.state === 'failed' && a.why ? ' ' + large.say(a.why) : '')
        : h === 'partial' ? 'The larger model is partly on this ' + d + ': ' + z.keptMb + ' of ' + z.mb + ' MB.' + fail
        : 'A larger model that names the species can be kept on this ' + d + ': about ' + z.mb + ' MB, downloaded once. Photos are not sent anywhere.' + fail;
      $('bigGet').textContent = h === 'partial' ? 'Get the rest' : 'Get it'; $('bigDel').textContent = bigDelAsked ? 'Delete it' : h === 'partial' ? 'Delete what is here' : 'Delete it';
      show('bigGet', !bigDelAsked && (h === 'absent' || h === 'partial')); show('bigHalt', h === 'getting'); show('bigDel', h === 'kept' || h === 'partial'); show('bigDelNo', bigDelAsked);
      show('bigAskRow', !bigDelAsked && (h === 'absent' || h === 'partial')); $('bigAsk').checked = bigChoice() === 'no';
      show('bigBox', true);
    });
  }
  $('bigYes').addEventListener('click', function () { answerBig('yes'); });
  $('bigNo').addEventListener('click', function () { answerBig('no'); });
  $('bigNever').addEventListener('click', function () { answerBig('never'); });
  $('bigStop').addEventListener('click', function () { closeSheets(); diag('large-say', 'stop'); large.halt(); });
  $('bigClose').addEventListener('click', dismissSheets);
  $('bigGet').addEventListener('click', function () { large.survey().then(openBig); });
  $('bigHalt').addEventListener('click', function () { diag('large-say', 'stop'); large.halt(); });
  $('bigDel').addEventListener('click', function () {
    if (!bigDelAsked) { bigDelAsked = true; paintBig(); return; }                // a second thought first, as with a meeting
    bigDelAsked = false; diag('large-say', 'delete');
    large.forget().then(function () { setBigChoice('no'); noteBig(''); if (S.svc && (S.svc.state === 'get' || S.svc.state === 'looking')) { S.svc = null; paintSvc(); } paintBig(); });
  });
  $('bigDelNo').addEventListener('click', function () { bigDelAsked = false; paintBig(); });
  $('bigAsk').addEventListener('change', function () { setBigChoice($('bigAsk').checked ? 'no' : ''); diag('large-choice', $('bigAsk').checked ? 'no' : 'each'); });
  // A download the person asked for and that was interrupted carries on by itself at the next visit, unless the connection says of itself
  // that it is metered or slow, or the device is set to save data: then it waits to be asked. One that had arrived whole and is gone is not fetched again unasked.
  function resumeBig() {
    var ch = bigChoice(); if (inViewer || (ch !== 'yes' && ch !== 'kept')) return;
    large.survey().then(function (h) {
      if (h === 'none' || h === 'kept' || h === 'getting' || ch === 'kept') return;     // 'kept' and gone: the next photo's line says so, and asks
      if (!netSays() && navigator.onLine !== false) startBig(); else setBigChoice('');
    });
  }

  // ---------- where the species list applies: it is one town's. No location is asked of the device; the person says if they are elsewhere.
  var AWAY_KEY = 'seenback.away.v1';
  try { pocket.local = localStorage.getItem(AWAY_KEY) !== '1'; } catch (e) {}
  function paintChoices() {
    // the switch is shown where it changes something: this device has a species list, or there is a larger model that is told the region
    show('awayRow', !inViewer && pocket.listed()); $('awayBox').checked = pocket.local === false;
    $('awayNote').textContent = 'Species are named from a list of those recorded around ' + pocket.place() + '. With this ticked, this ' + (coarse ? 'phone' : 'computer') + ' names only the kind of animal or plant, and a larger model, if asked, is not told the region.';
    show('svcBox', false); bigDelAsked = false; paintBig();
    naturalist.config().then(function (c) {
      show('svcBox', !!c); if (!c) return;
      $('svcChoice').value = naturalist.choice();
      if (!pocket.listed() && c.region) { show('awayRow', true); $('awayNote').textContent = 'A larger model, when asked, is told the region, so that it can choose among species recorded around ' + pocket.place() + '. With this ticked, it is not told.'; }
    });
  }
  $('awayBox').addEventListener('change', function () { pocket.local = !$('awayBox').checked; try { localStorage.setItem(AWAY_KEY, pocket.local ? '0' : '1'); } catch (e) {} diag('away', pocket.local ? 'no' : 'yes'); });
  $('svcChoice').addEventListener('change', function () { naturalist.setChoice($('svcChoice').value); diag('service-choice', $('svcChoice').value || 'each'); });
  $('btnType').addEventListener('click', function () {
    if (S.screen !== 'naming' || S.eyes) return;
    S.token++; S.seq++; diag('type-instead', '');             // the answer for this photo, when it comes, is not waited for
    askName('The recognizer keeps downloading meanwhile.');
  });
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
  window.__seenBack = { S: S, EYES: EYES, state: function () { return engine ? engine.state() : null; }, record: function () { return record; }, kindOfName: kindOfName, offerList: offerList, setViewPrompt: setViewPrompt, lookAgain: lookAgain,
    rec: pocket, big: large, bigChoice: bigChoice, svc: naturalist, diag: function () { return diagLog; }, about: aboutText,
    pose: function (t) { S.tr = t === null ? null : { t0: 0, dur: 1, fixed: t }; if (t === null) S.k = 1; } };   // hold the change of eyes at one instant, for checking

  // ---------- about this build: one block to copy from a real phone, to say how it ran there
  var frameMs = [], frameLast = 0;
  (function watchFrames2(now) {                    // how long the last frames took, measured here and not in the engine
    requestAnimationFrame(watchFrames2);
    if (frameLast && now - frameLast < 1000) { frameMs.push(now - frameLast); if (frameMs.length > 90) frameMs.shift(); }
    frameLast = now;
  })(0);
  function aboutText() {
    var a = pocket.about(), st = engine ? engine.state() : null, L = ['Regards, build ' + BUILD + '.'], r = a.last, avg = 0;
    frameMs.forEach(function (x) { avg += x; });
    avg = frameMs.length ? avg / frameMs.length : 0;
    if (inViewer) L.push('Recognizer: Claude, inside Claude’s viewer.');
    else if (a.state === 'ready') L.push('Recognizer: ' + a.model + ', ' + a.backend + (a.threads ? ', ' + a.threads + (a.threads === 1 ? ' thread' : ' threads') : '') + ', ready in ' + (a.loadMs / 1000).toFixed(1) + ' s.');
    else if (a.state === 'loading') L.push('Recognizer: loading' + (a.total ? ', ' + Math.round(a.got / 1e6) + ' of ' + Math.round(a.total / 1e6) + ' MB' : '') + '.');
    else if (a.state === 'idle') L.push('Recognizer: not started yet.');
    else L.push('Recognizer: not running. ' + (a.fail || a.why) + '.');
    if (r) L.push('Last photo: ' + r.kind + ' ' + r.kindP.toFixed(2) + (r.species[0] ? ', ' + r.species[0].sci + ' ' + r.species[0].p.toFixed(2) : '') + '; ' + (r.ms.load ? 'waited ' + r.ms.load + ' ms, ' : '') + 'prepared in ' + r.ms.pre + ' ms from ' + r.from + ', recognized in ' + r.ms.run + ' ms.');
    var b = large.about();
    if (b.have) L.push('Larger model: ' + (b.model || 'unnamed') + ', ' + (b.have === 'kept' ? 'on this device' : b.have === 'getting' ? 'being fetched' : b.have === 'partial' ? 'partly on this device' : 'not on this device') + ', ' + Math.round(b.keptBytes / 1e6) + ' of ' + Math.round(b.bytes / 1e6) + ' MB' +
      (b.last ? '; last photo ' + b.last.kind + ' ' + b.last.kindP.toFixed(2) + (b.last.species[0] ? ', ' + b.last.species[0].sci + ' ' + b.last.species[0].p.toFixed(2) : '') + ', in ' + (b.last.ms.run / 1000).toFixed(1) + ' s' + (b.last.ms.load ? ' after ' + (b.last.ms.load / 1000).toFixed(1) + ' s to start' : '') : '') +
      (b.state === 'failed' && b.fail ? '; ' + b.fail : '') + '.');
    L.push('Picture: ' + canvas.width + ' by ' + canvas.height + (st && st.sw ? ', source ' + st.sw + ' by ' + st.sh : '') + (engine ? ', limit ' + engine.side() : ', no engine') +
      (avg ? ', ' + avg.toFixed(1) + ' ms a frame over the last ' + frameMs.length + '.' : '.'));
    L.push('Screen: ' + window.innerWidth + ' by ' + window.innerHeight + ' at ' + (window.devicePixelRatio || 1) + '. ' + (coarse ? 'Touch.' : 'Pointer.') + (S.camOK ? ' Camera open.' : S.camRefused ? ' Camera refused.' : ''));
    L.push(String(navigator.userAgent || '').slice(0, 200));
    return L.join('\n');
  }
  function fittedLine() {                          // where the pocket slot's rows came from, said only when its manifest carries a fitted_on block
    var f = pocket.about().fitted; if (!f) return '';
    var n = typeof f.photos === 'number' && isFinite(f.photos) && f.photos >= 1 ? String(Math.round(f.photos)).replace(/\B(?=(\d{3})+(?!\d))/g, ',') + ' ' : '';
    var rule = typeof f.rule === 'string' ? clip(f.rule.trim(), 300) : '';
    return 'The rows the recognizer compares a photo with were fitted on ' + n + 'photographs shared on iNaturalist and Flickr under Creative Commons licences or in the public domain.' + (rule ? ' ' + rule + (/[.!?]$/.test(rule) ? '' : '.') : '');
  }
  function paintAbout() { var fl = fittedLine(), f = pocket.about().fitted, el = $('fittedOn'), a;
    $('buildMark').textContent = aboutText(); $('aboutNote').textContent = ''; el.textContent = fl;
    if (fl && f && typeof f.list === 'string' && /^https:\/\/[^\s"<>]+$/.test(f.list)) {   // the attribution: where each photograph's address and licence can be read
      a = document.createElement('a'); a.href = f.list; a.target = '_blank'; a.rel = 'noopener'; a.textContent = 'The list of them';
      el.appendChild(document.createTextNode(' ')); el.appendChild(a); el.appendChild(document.createTextNode(' gives each one’s address and licence' + (typeof f.list_mb === 'number' && f.list_mb >= 1 ? ' (a file of about ' + Math.round(f.list_mb) + ' MB)' : '') + '.'));
    }
    show('fittedOn', !!fl); paintChoices(); }
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
  if (document.readyState === 'complete') setTimeout(resumeBig, 1500); else window.addEventListener('load', function () { setTimeout(resumeBig, 1500); });
  if (inViewer) {
    window.claude.use('sample').then(function (s) {
      if (!s) return;
      return s.limits().then(function (lim) { sample = s; canImages = !!(lim && lim.images); }, function () { sample = s; canImages = false; });
    }).catch(function () {}).then(capsDone);
    setTimeout(capsDone, 8000);                     // a viewer that never answers is treated as having no Claude
    window.claude.use('downloads').then(function (d) { downloads = d; }).catch(function () {});
    initRemote();
  }
