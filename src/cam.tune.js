
  // ---------- the tuning panel and the compare slider (docs/ENGINE-DESIGN.md, section 4), only with ?try=<view>&tune=1
  // Every parameter of the view's spec gets a slider over its range. The slider steps by the parameter's visibility floor where
  // docs/views/floor.json has one, so each step is a change a person can see, and by a two-hundredth of the range otherwise. Copy puts
  // a patch of the changed values on the clipboard; Keep stores it in this browser (wrapped, since storage can be refused).
  (function tunePanel() {
    if (!TUNE.on) return;
    var key = TRY_KEYS[0], work = JSON.parse(JSON.stringify(SPECS[key])), changed = {}, rows = [];
    var store = { get: function (k) { try { return window.localStorage.getItem(k); } catch (e) { return null; } },
      set: function (k, v) { try { window.localStorage.setItem(k, v); return true; } catch (e) { return false; } } };
    function el(tag, css, text) { var e = document.createElement(tag); if (css) e.style.cssText = css; if (text !== undefined) e.textContent = text; return e; }
    function walk(x, path, out, label) {
      if (isParam(x)) { if (typeof x.value === 'number' || (Array.isArray(x.value) && x.value.every(function (n) { return typeof n === 'number'; }))) out.push({ path: path, label: label, o: x }); return; }
      if (Array.isArray(x)) x.forEach(function (v, i) { walk(v, path.concat(i), out, label + '.' + ((v && v.id) || i)); });
      else if (x && typeof x === 'object') Object.keys(x).forEach(function (k) { if (k !== 'by' && k !== 'rows' && k !== 'matrices') walk(x[k], path.concat(k), out, label ? label + '.' + k : k); });
    }
    function at(path) { var o = work; path.forEach(function (p) { o = o[p]; }); return o; }
    function apply() {
      EYES[key] = viewOf(work);
      if (S.eyes === key) eyeP = paramsOf(EYES[key], S.named);
    }
    function stepOf(label, v, lo, hi) {
      var f = (FLOOR[key] || {})[label] || FLOOR[label];
      if (f && f.length) { var best = f[0]; f.forEach(function (q) { if (Math.abs(q[0] - v) < Math.abs(best[0] - v)) best = q; }); if (typeof best[1] === 'number' && best[1] > 0) return best[1]; }
      return (hi - lo) / 200;
    }
    var list = []; walk({ params: work.params, zones: work.zones, gaze: work.gaze }, [], list, '');
    var box = el('div', 'position:fixed;left:0;right:0;bottom:0;max-height:33vh;overflow:auto;background:rgba(0,0,0,.82);color:#eee;font:12px/1.3 system-ui,sans-serif;z-index:60;padding:6px 10px calc(6px + env(safe-area-inset-bottom,0px));-webkit-overflow-scrolling:touch');
    box.id = 'tunePanel';
    var head = el('div', 'display:flex;gap:6px;align-items:center;flex-wrap:wrap;position:sticky;top:0;background:rgba(0,0,0,.9);padding:2px 0 6px');
    var title = el('b', 'flex:1;min-width:8em', (work.chip || key) + ' · ' + list.length + ' parameters');
    var note = el('div', 'color:#bbb;min-height:1.3em;padding:2px 0', 'Hold a row for its source. ● marks an invented value; ? marks a value not yet graded.');
    function btn(text, fn) { var b = el('button', 'background:#333;color:#fff;border:1px solid #666;border-radius:12px;padding:4px 10px;font:inherit', text); b.addEventListener('click', fn); return b; }
    var fold = btn('Hide', function () { var hid = body.style.display === 'none'; body.style.display = hid ? '' : 'none'; note.style.display = body.style.display; fold.textContent = hid ? 'Hide' : 'Tune'; });
    function patch() { return JSON.stringify({ key: key, version: work.version, set: changed }); }
    var copy = btn('Copy', function () {
      var t = patch();
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(function () { note.textContent = 'Copied the changes.'; }, function () { note.textContent = t; });
      else note.textContent = t;
    });
    var keep = btn('Keep', function () { note.textContent = store.set('tune:' + key, patch()) ? 'Kept on this phone for this view.' : 'This browser refused to keep it.'; });
    var cmp = btn('Compare', function () { TUNE.cmp = TUNE.cmp ? 0 : .5; place(); });
    head.appendChild(title); head.appendChild(cmp); head.appendChild(copy); head.appendChild(keep); head.appendChild(fold);
    var body = el('div');
    box.appendChild(head); box.appendChild(note); box.appendChild(body);
    list.forEach(function (it) {
      var vals = Array.isArray(it.o.value) ? it.o.value : [it.o.value];
      vals.forEach(function (v0, j) {
        var lab = it.label + (vals.length > 1 ? '[' + j + ']' : ''), r = it.o.range, lo, hi;
        if (r) { lo = r[0]; hi = r[1]; } else if (v0 >= 0) { lo = 0; hi = Math.max(1, v0 * 3); } else { lo = v0 * 3; hi = -v0 * 3; }
        var row = el('div', 'display:flex;align-items:center;gap:6px;padding:3px 0;border-top:1px solid #222');
        var g = it.o.grade, inv = it.o.invented;
        row.appendChild(el('span', 'width:1.2em;text-align:center;font-weight:700;color:' + (g === 'm' ? '#8f8' : g === 'g' ? '#fd6' : g === 'i' ? '#f88' : '#999'), g));
        row.appendChild(el('span', 'width:.8em;color:#f93', inv ? '●' : ''));
        var name = el('span', 'flex:1 1 40%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap', lab);
        var s = el('input'); s.type = 'range'; s.min = lo; s.max = hi; s.step = stepOf(lab, v0, lo, hi); s.value = v0; s.style.cssText = 'flex:1 1 45%;min-width:80px';
        var out = el('span', 'width:3.6em;text-align:right;font-variant-numeric:tabular-nums', String(+v0.toPrecision(4)));
        var reset = btn('↺', function () { set(v0); s.value = v0; });
        function set(v) {
          var o = at(it.path); if (Array.isArray(o.value)) o.value[j] = v; else o.value = v;
          out.textContent = String(+(+v).toPrecision(4));
          changed[it.path.join('.')] = o.value; apply();
        }
        s.addEventListener('input', function () { set(+s.value); });
        var press = 0;
        row.addEventListener('pointerdown', function () { press = setTimeout(function () { note.textContent = lab + ': ' + ((it.o.src || []).join('; ') || 'no source') + (it.o.note ? ' (' + it.o.note + ')' : ''); }, 450); });
        ['pointerup', 'pointercancel', 'pointerleave'].forEach(function (ev) { row.addEventListener(ev, function () { clearTimeout(press); }); });
        row.appendChild(name); row.appendChild(s); row.appendChild(out); row.appendChild(reset);
        body.appendChild(row); rows.push({ lab: lab, s: s, set: set });
      });
    });
    // a patch kept on this phone comes back on load
    try {
      var kept = JSON.parse(store.get('tune:' + key) || 'null');
      if (kept && kept.key === key) Object.keys(kept.set || {}).forEach(function (p) {
        var o = at(p.split('.').map(function (q) { return /^\d+$/.test(q) ? +q : q; })); if (o && isParam(o)) { o.value = kept.set[p]; changed[p] = kept.set[p]; }
      });
      if (Object.keys(changed).length) { apply(); note.textContent = 'Kept changes loaded: ' + Object.keys(changed).length + '.'; }
    } catch (e) { /* a kept patch that no longer fits is left alone */ }
    // the compare divider: drag it; a double tap swaps nothing yet, a long press hides it
    var bar = el('div', 'position:fixed;top:0;bottom:0;width:28px;margin-left:-14px;z-index:59;touch-action:none;display:none;cursor:ew-resize');
    bar.id = 'tuneDivider';
    bar.appendChild(el('div', 'position:absolute;left:13px;top:0;bottom:0;width:2px;background:rgba(255,255,255,.85);box-shadow:0 0 4px #000'));
    var tag = el('div', 'position:absolute;top:40%;left:-30px;width:88px;display:flex;justify-content:space-between;color:#fff;font:600 11px system-ui;text-shadow:0 0 3px #000;pointer-events:none');
    tag.appendChild(el('span', '', 'you')); tag.appendChild(el('span', '', 'it')); bar.appendChild(tag);
    function place() { bar.style.display = TUNE.cmp ? '' : 'none'; bar.style.left = (TUNE.cmp * 100) + '%'; }
    var drag = false, hold = 0;
    bar.addEventListener('pointerdown', function (e) { drag = true; bar.setPointerCapture(e.pointerId); hold = setTimeout(function () { drag = false; TUNE.cmp = 0; place(); }, 900); e.stopPropagation(); });
    bar.addEventListener('pointermove', function (e) { if (!drag) return; clearTimeout(hold); TUNE.cmp = clamp(e.clientX / window.innerWidth, .02, .98); place(); });
    bar.addEventListener('pointerup', function () { drag = false; clearTimeout(hold); });
    document.body.appendChild(bar); document.body.appendChild(box);
    setInterval(function () {   // the panel and the divider belong to the creature's picture and stay out of every other screen
      var on = S.screen === 'animal' && S.eyes === key;
      box.style.display = on ? '' : 'none'; bar.style.display = on && TUNE.cmp ? '' : 'none';
    }, 250);
    box.style.display = 'none';
    window.__seenBack.tune = { key: key, list: function () { return rows.map(function (r) { return r.lab; }); }, set: function (lab, v) { var r = rows.filter(function (q) { return q.lab === lab; })[0]; if (!r) return false; r.s.value = v; r.set(v); return true; }, patch: patch };
  })();
