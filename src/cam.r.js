
  // ---------- a name said by the person, matched to a kind of eye
  // Used only where nothing can look at the photo, or to correct a name that came out wrong. First match wins,
  // so the order settles "fox squirrel", "rat snake", "crane fly" and "turkey vulture". Vultures are among the other birds:
  // the hawk's sharper sight is not established for them.
  var LEX = [
    ['person', /\b(person|people|humans?|man|woman|men|women|boy|girl|child|children|kid|baby|me|myself|selfie)\b/],
    ['other', /(spiders?|fish(es)?|snails?|slugs?|\bworms?|earthworms?|\bbats?|crabs?|crayfish|shrimps?|mushrooms?|fung(us|i)|lichens?|raccoons?|opossums?|possums?|armadillos?|\bbears?|otters?|manatees?|\bpigs?|\bhogs?|monkeys?|millipedes?|centipedes?|scorpions?|\bticks?|\bmites?)\b/],
    ['bee', /(bees?|wasps?|hornets?|yellowjackets?)\b/],
    ['insect', /(butterfl(y|ies)|\bmoths?|beetles?|fl(y|ies)|\bants?|crickets?|cicadas?|mantis|mantids?|\bbugs?|ladybugs?|ladybirds?|lovebugs?|skippers?|monarchs?|fritillar(y|ies)|swallowtails?|longwings?|buckeyes?|katydids?|roach(es)?|weevils?|aphids?|caterpillars?|mosquito(es)?|gnats?|termites?|walkingsticks?|earwigs?|hoppers?|insects?)\b/],
    ['frog', /(frogs?|toads?|peepers?)\b/],
    ['alligator', /\b(alligators?|gators?|crocodiles?|crocs?|caimans?)\b/],
    ['reptile', /(lizards?|anoles?|geckos?|skinks?|snakes?|\bracers?|turtles?|tortoises?|sliders?|cooters?|softshells?|iguanas?|reptiles?|cottonmouths?|moccasins?|copperheads?|pythons?)\b/],
    ['squirrel', /(squirrels?|chipmunks?|\brats?|\bmice|\bmouse|\bvoles?|gophers?)\b/],
    ['bird', /(vultures?|condors?)\b/],
    ['hawk', /(hawks?|eagles?|falcons?|\bkites?|ospreys?|kestrels?|harriers?|buzzards?|caracaras?|merlins?)\b/],
    ['wader', /\b(herons?|egrets?|ibis(es)?|storks?|cranes?|limpkins?|coots?|moorhens?|gallinules?|rails?|pigeons?|doves?|chickens?|roosters?|hens?|turkeys?|bitterns?|spoonbills?)\b/],
    ['bird', /(birds?|\bducks?|\bgeese|\bgoose|\bswans?|gulls?|\bterns?|pelicans?|cormorants?|anhingas?|cardinals?|warblers?|sparrows?|\bwrens?|\bjays?|\bcrows?|ravens?|robins?|finch(es)?|phoebes?|grackles?|woodpeckers?|flickers?|\bswallows?|\bswifts?|\bowls?|parrots?|parakeets?|starlings?|thrush(es)?|thrashers?|vireos?|titmouse|titmice|chickadees?|nuthatch(es)?|orioles?|tanagers?|flycatchers?|kingfishers?|loons?|grebes?|sandpipers?|plovers?|killdeers?|shrikes?|gnatcatchers?|sapsuckers?|towhees?|waxwings?|kinglets?|buntings?|meadowlarks?|\blarks?)\b/],
    ['cat', /\b(cats?|kittens?|kitty|kitties|bobcats?|lynx|panthers?|cougars?|lions?|tigers?|leopards?|ocelots?|jaguars?)\b/],
    ['dog', /\b(dogs?|pupp(y|ies)|fox(es)?|coyotes?|wol(f|ves))\b/],
    ['deer', /\b(deer|fawns?|bucks?|does?|horses?|pon(y|ies)|cows?|cattle|bulls?|cal(f|ves)|goats?|sheep|lambs?|elk|moose|bison|donkeys?|mules?)\b/],
    ['rabbit', /\b(rabbits?|bunn(y|ies)|hares?|cottontails?)\b/],
    ['plant', /(plants?|trees?|flowers?|\bmoss(es)?|ferns?|grass(es)?|\bvines?|shrubs?|bush(es)?|weeds?|palms?|palmettos?|\boaks?|\bpines?|magnolias?|sweetgums?|maples?|cypress|cedars?|holl(y|ies)|azaleas?|camellias?|berr(y|ies)|worts?|lil(y|ies)|roses?|orchids?|cactus|cacti|succulents?|\biv(y|ies)|creepers?|sumacs?|indigo|catbrier|greenbrier|grapes?|ardisia|beggarticks|bidens|lea(f|ves)|\bherbs?|basil|tomato(es)?|\bmints?|\bsages?|blossoms?|seedlings?|saplings?|dais(y|ies)|clover|bamboo|lantana|hibiscus|bromeliads?|tillandsia|wood)\b/]
  ];
  function kindOfName(text) {
    var t = String(text || '').toLowerCase().replace(/[^a-z' -]+/g, ' ');
    for (var i = 0; i < LEX.length; i++) if (LEX[i][1].test(t)) return LEX[i][0];
    return '';                                     // no word in it is a kind this page knows
  }

  // ---------- the record: everyone met so far, and the eyes that came with them
  // Kept in this browser, and beside it in the viewer's own private part of the artifact's store, where one is offered.
  var KINDS = ['cat', 'dog', 'squirrel', 'deer', 'rabbit', 'hawk', 'wader', 'bird', 'alligator', 'reptile', 'frog', 'bee', 'insect', 'plant'];
  var REC_KEY = 'seenback.record.v1', remote = null, diagDoc = null, diagLog = [], diagP = Promise.resolve();
  // A short trace of how recognition went, kept in the viewer's own private part of the store, so a fault on a phone can be read afterwards.
  function diag(what, code) {
    diagLog.push({ at: Date.now(), what: what, code: code || '', build: BUILD, framed: framed, sample: !!sample, images: !!canImages, src: S.src, camRefused: !!S.camRefused,
      ua: String(navigator.userAgent || '').slice(0, 180), w: window.innerWidth, h: window.innerHeight });
    diagLog = diagLog.slice(-12);
    if (!diagDoc) return;
    var ref = diagDoc, log = diagLog.slice();
    diagP = diagP.then(function () { return ref.set({ log: log }); }).catch(function () {});
  }
  var framed = (function () { try { return window.self !== window.top; } catch (e) { return true; } })();
  // who gave the name: Claude, this page's small model, a larger model on a server, a larger model on this device, or the person
  function byOf(by) { return by === 'Claude' || by === 'page' || by === 'service' || by === 'device-large' ? by : 'you'; }
  function cleanMeeting(v, id) {
    if (!v || typeof v !== 'object') return null;
    var key = String(v.key || ''), mid = String(id || v.id || '');
    if (!EYES[key] || key === 'person' || !/^[A-Za-z0-9_-]{4,40}$/.test(mid)) return null;
    var thumb = typeof v.thumb === 'string' && v.thumb.length < 24000 && /^data:image\/jpeg;base64,[A-Za-z0-9+\/=]+$/.test(v.thumb) ? v.thumb : '';
    return { id: mid, key: key, common: clip(v.common, 60) || handName(key), sci: clip(v.sci, 80), by: byOf(v.by), at: +v.at || 0, thumb: thumb, up: v.up ? 1 : 0, loc: v.loc ? 1 : 0 };
  }
  function loadLocal() {
    try { var a = JSON.parse(localStorage.getItem(REC_KEY) || '[]'); return Array.isArray(a) ? a.map(function (v) { return cleanMeeting(v); }).filter(Boolean) : []; }
    catch (e) { return []; }
  }
  var record = loadLocal();
  function saveLocal() {
    try { localStorage.setItem(REC_KEY, JSON.stringify(record.slice(0, 300).map(function (m) { return { id: m.id, key: m.key, common: m.common, sci: m.sci, by: m.by, at: m.at, thumb: m.thumb, up: m.up, loc: m.loc }; }))); } catch (e) {}
  }
  function pushUp(m) {                             // one write at a time for each meeting
    if (!remote) return;
    var col = remote;
    m._p = (m._p || Promise.resolve()).then(function () {
      return col.doc(m.id).set({ key: m.key, common: m.common, sci: m.sci, by: m.by, at: m.at, thumb: m.thumb, loc: m.loc ? 1 : 0 });
    }).then(function () { m.up = 1; saveLocal(); }, function () {});
  }
  function thumbOf(c) {
    var t = makeCanvas(96, 96), x = t.getContext('2d'), k = Math.max(96 / c.width, 96 / c.height);
    x.imageSmoothingQuality = 'high'; x.drawImage(c, (96 - c.width * k) / 2, (96 - c.height * k) / 2, c.width * k, c.height * k);
    try { return t.toDataURL('image/jpeg', .72); } catch (e) { return ''; }
  }
  function noteMeeting(key, named) {               // a photo has its name: keep the meeting, or correct the one already kept for this photo
    S.nov = '';
    if (key === 'person') return;
    var same = function (r) { return r.id !== S.meetingId; }, nm = named.common.toLowerCase();
    S.nov = KINDS.indexOf(key) >= 0 && !record.some(function (r) { return same(r) && r.key === key; }) ? 'kind'
      : !record.some(function (r) { return same(r) && r.common.toLowerCase() === nm; }) ? 'name' : 'again';
    var m = S.meetingId ? record.filter(function (r) { return r.id === S.meetingId; })[0] : null;
    if (!m) {
      m = { id: 'm' + Date.now().toString(36) + Math.floor(Math.random() * 1e9).toString(36), at: Date.now(), thumb: S.animalPhoto ? thumbOf(S.animalPhoto) : '', up: 0 };
      record.unshift(m); S.meetingId = m.id;
    }
    m.key = key; m.common = named.common; m.sci = named.scientific || ''; m.by = byOf(named.by);
    m.loc = named.local ? 1 : 0;                   // the species was chosen from the list of one place
    saveLocal(); pushUp(m); paintRecordBits();
  }
  function forgetMeeting(id) {
    record = record.filter(function (m) { return m.id !== id; });
    if (S.meetingId === id) S.meetingId = null;
    saveLocal(); if (remote) remote.doc(id).delete().catch(function () {});
    paintRecordBits(); renderRecord();
  }
  function initRemote() {
    Promise.all([window.claude.use('db'), window.claude.use('user')]).then(function (r) {
      var db = r[0], user = r[1]; if (!db || !user) return;
      return user.id().then(function (uid) {
        if (!uid) return;
        var col = db.doc('data/users/' + uid + '/record').collection('met');
        return col.orderBy('at', 'desc').limit(300).get().then(function (qs) {
          var there = {}, here = {};
          qs.docs.forEach(function (d) { there[d.id] = d; });
          // what was sent up before and is gone from the store was forgotten on another device
          record = record.filter(function (m) { return !(m.up && !there[m.id]); });
          record.forEach(function (m) { here[m.id] = 1; if (there[m.id]) m.up = 1; });
          qs.docs.forEach(function (d) { if (here[d.id]) return; var m = cleanMeeting(d.data(), d.id); if (m) { m.up = 1; record.push(m); } });
          record.sort(function (a, b) { return b.at - a.at; });
          remote = col; diagDoc = db.doc('data/users/' + uid + '/diag'); saveLocal(); paintRecordBits(); if (!$('record').hidden) renderRecord();
          record.filter(function (m) { return !m.up; }).slice(0, 40).forEach(pushUp);
        });
      });
    }).catch(function () {});
  }

  // ---------- the Gainesville list
  var G60_BY = (function () {
    var o = {}; G60.forEach(function (r, i) { o[r[1].toLowerCase()] = i + 1; o[r[2].toLowerCase()] = i + 1; });
    Object.keys(G60_ALIAS).forEach(function (k) { o[k] = G60_ALIAS[k]; }); return o;
  })();
  function g60Of(m) {
    var sci = (m.sci || '').toLowerCase().split(/\s+/).slice(0, 2).join(' ');
    return G60_BY[sci] || G60_BY[(m.common || '').toLowerCase().trim()] || 0;
  }

  // ---------- the record, drawn
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text !== undefined) e.textContent = text; return e; }
  function svgEl(tag, attrs) { var e = document.createElementNS('http://www.w3.org/2000/svg', tag); for (var k in attrs) e.setAttribute(k, attrs[k]); return e; }
  function eyeGlyph(key, on) {                     // an iris, and once met, the pupil that kind of eye has
    var s = svgEl('svg', { viewBox: '0 0 24 24', 'aria-hidden': 'true' }), p = EYES[key].pupil;
    s.appendChild(svgEl('circle', { cx: 12, cy: 12, r: 9.6, 'class': 'iris' }));
    if (!on) return s;
    if (p === 'v') s.appendChild(svgEl('ellipse', { cx: 12, cy: 12, rx: 1.7, ry: 7.2, 'class': 'pupil' }));
    else if (p === 'h') s.appendChild(svgEl('rect', { x: 5.2, y: 9.7, width: 13.6, height: 4.6, rx: 2.2, 'class': 'pupil' }));
    else if (p === 'o') s.appendChild(svgEl('circle', { cx: 12, cy: 12, r: 3.7, 'class': 'pupil' }));
    else if (key === 'bee' || key === 'insect') s.appendChild(svgEl('path', { d: 'M12 6.6l4.7 2.7v5.4L12 17.4l-4.7-2.7V9.3z', 'class': 'pupil' }));
    else s.appendChild(svgEl('circle', { cx: 12, cy: 12, r: 1.3, 'class': 'pupil' }));
    return s;
  }
  // The rule of the finding game: eyes are lent for a week from a meeting, and then go back. The record of the meeting stays for good.
  // To see as a heron again after the week, a heron has to be met again. A meeting whose time lies ahead of this clock counts as just made.
  var LEND_MS = 7 * 864e5;
  function lentLeft(m) { return m ? LEND_MS - Math.max(0, Date.now() - m.at) : 0; }
  function lent(m) { return lentLeft(m) > 0; }
  function lentSays(m) {
    var ms = lentLeft(m), d;
    if (ms <= 0) return 'its eyes have gone back';
    d = Math.ceil(ms / 864e5);
    return ms <= 36e5 ? 'its eyes go back within the hour' : ms <= 864e5 ? 'its eyes go back within a day' : d >= 7 ? 'its eyes are yours for a week' : 'its eyes are yours for ' + d + ' more days';
  }
  function latestOf(key) { for (var i = 0; i < record.length; i++) if (record[i].key === key) return record[i]; return null; }
  function paintRecordBits() {
    var t = 'Met so far' + (record.length ? ': ' + record.length : '');
    $('introRec').textContent = t; $('recAskAnimal').textContent = t;
  }
  function renderRecord() {
    var met = {}, once = {}, n = record.length, k = 0, have = {};
    record.forEach(function (m) { if (KINDS.indexOf(m.key) >= 0) { once[m.key] = 1; if (lent(m)) met[m.key] = 1; } var g = g60Of(m); if (g) have[g] = 1; });
    KINDS.forEach(function (key) { if (met[key]) k++; });
    $('recordSub').textContent = n ? n + (n === 1 ? ' meeting kept. ' : ' meetings kept. ') + 'Eyes are lent for a week from a meeting, and ' + k + ' of ' + KINDS.length + ' kinds are with you now.' + (k ? ' Tap an eye to look through it.' : ' Meet one again to have its eyes back.')
      : 'No one yet. Photograph something alive: the meeting is kept here, and its eyes are yours for a week.';
    var strip = $('eyeStrip'); strip.textContent = '';
    KINDS.forEach(function (key) {
      var b = el('button', 'eye'); b.type = 'button'; b.disabled = !met[key];
      b.setAttribute('aria-label', met[key] ? 'Look as ' + EYES[key].who : once[key] ? 'A kind of eye that has gone back' : 'A kind of eye not yet met');
      b.appendChild(eyeGlyph(key, !!once[key]));          // a kind met once keeps its pupil, dimmed when its eyes have gone back
      if (met[key]) b.addEventListener('click', function () { lookAgain(latestOf(key)); });
      strip.appendChild(b);
    });
    var ul = $('metList'); ul.textContent = '';
    record.slice(0, 150).forEach(function (m) {
      var li = el('li'), th, tx = el('div'), look = el('button', 'ico sm'), x = el('button', 'x', '×');
      if (m.thumb) { th = el('img', 'th'); th.alt = ''; th.src = m.thumb; } else th = el('span', 'th');
      tx.appendChild(el('span', 'nm', m.common));
      tx.appendChild(el('span', 'sm', [m.sci, labelDate(new Date(m.at)), m.by === 'Claude' ? 'recognized by Claude' : m.by === 'page' ? 'recognized by a small model' : m.by === 'service' ? 'named by a larger model on a server' : m.by === 'device-large' ? 'named on this device by a larger model' : 'on your word', lentSays(m)].filter(Boolean).join(' · ')));
      look.type = 'button'; look.setAttribute('aria-label', 'Look as ' + m.common);
      var sv = svgEl('svg', { viewBox: '0 0 24 24' }); sv.appendChild(svgEl('path', { d: 'M2.5 12s3.5-6.5 9.5-6.5S21.5 12 21.5 12s-3.5 6.5-9.5 6.5S2.5 12 2.5 12z' })); sv.appendChild(svgEl('circle', { cx: 12, cy: 12, r: 2.8 })); look.appendChild(sv);
      look.addEventListener('click', function () { lookAgain(m); });
      x.type = 'button'; x.setAttribute('aria-label', 'Forget the meeting with ' + m.common);
      x.addEventListener('click', function () {
        var yes = el('button', 'mini', 'Forget'), no = el('button', 'mini', 'Keep');
        yes.type = no.type = 'button'; li.textContent = ''; li.className = 'ask';
        li.appendChild(el('span', 'q', 'Forget the meeting with ' + m.common + '?')); li.appendChild(yes); li.appendChild(no);
        yes.addEventListener('click', function () { forgetMeeting(m.id); });
        no.addEventListener('click', renderRecord);
      });
      li.appendChild(th); li.appendChild(tx); if (lent(m)) li.appendChild(look); li.appendChild(x); ul.appendChild(li);   // no way to look where the eyes have gone back
    });
    $('g60Sum').textContent = 'Gainesville’s sixty most recorded in autumn: ' + Object.keys(have).length + ' met';
    var ol = $('g60List'); ol.textContent = '';
    G60.forEach(function (r, i) { var li = el('li', have[i + 1] ? 'on' : '', have[i + 1] ? r[2] + ', ' + r[0] + ' records' : r[0] + ' records'); ol.appendChild(li); });
  }
  function openRecord() { renderRecord(); show('claim', false); show('info', false); show('keep', false); openSheet('record'); $('record').scrollTop = 0; }

  // ---------- looking again through eyes already met
  function photoFromThumb(src) {
    return new Promise(function (res) {
      if (!src) { res(null); return; }
      var im = new Image();
      im.onload = function () { var c = makeCanvas(im.naturalWidth || 96, im.naturalHeight || 96); c.getContext('2d').drawImage(im, 0, 0, c.width, c.height); res(c); };
      im.onerror = function () { res(null); };
      im.src = src;
    });
  }
  function blankStill() { var c = makeCanvas(9, 16), x = c.getContext('2d'); x.fillStyle = '#141414'; x.fillRect(0, 0, 9, 16); return c; }
  function openCamera(facing) {                    // resolves with the camera running; rejects where it is refused, missing, or never answers
    if (!hasCamera || S.camRefused) return Promise.reject(new Error('no camera'));
    return new Promise(function (res, rej) {
      var settled = false;
      function no(e) { if (settled) return; settled = true; stopSource(); S.camRefused = true; rej(e || new Error('refused')); }
      if (inViewer && framed) setTimeout(no, 4000);          // a viewer's frame that neither grants nor refuses is treated as a refusal
      startCamera(facing).then(function () { if (settled) { stopSource(); return; } settled = true; S.camOK = true; res(); }, no);
    });
  }
  function lookAgain(m) {
    if (!m || !EYES[m.key] || !lent(m)) return;
    var named = { common: m.common, scientific: m.sci, by: m.by, again: m.at, local: !!m.loc };
    closeSheets(); S.seq++; S.token++; if (nameCtl) nameCtl.abort(); hideName(); msg(''); pocket.offers = []; pocket.kindOffers = []; paintSvc();
    if (rec) { recDrop = true; stopRec(); }
    armBack();
    photoFromThumb(m.thumb).then(function (c) {
      S.animalPhoto = c; S.meetingId = m.id; S.nov = '';
      function live() { thaw(); setEyes(m.key, named); go('animal'); showName(); later(startChange, calm ? 150 : 750); }
      function still() { showStill(c || blankStill(), false); setEyes(m.key, named); setViewPrompt(m.key); go('askView'); }
      if (S.src === 'cam') live();
      else if (S.camOK || !(inViewer && framed)) openCamera('environment').then(live, still);
      else still();
    });
  }
