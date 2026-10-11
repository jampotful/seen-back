
  // ---------- the engine: three passes on the phone's graphics chip
  // 1. every second camera frame is kept in a short ring of past moments
  // 2. time: trails, held gazes and slowed moments are mixed from that ring
  // 3. space and colour: field, sharpness, pupil, light, colour, and the aperture
  var VS = '#version 300 es\nin vec2 a; out vec2 v; void main(){ v = a * 0.5 + 0.5; gl_Position = vec4(a, 0.0, 1.0); }';
  var FS_COPY = '#version 300 es\nprecision highp float; in vec2 v; out vec4 o; uniform sampler2D u_src; void main(){ o = vec4(texture(u_src, v).rgb, 1.0); }';
  var FS_TIME = [
    '#version 300 es', 'precision highp float; precision highp sampler2DArray;', 'in vec2 v; out vec4 o;',
    'uniform sampler2D u_src, u_prev; uniform sampler2DArray u_ring; uniform vec2 u_px;',
    'uniform float u_n, u_head, u_lag, u_useRing, u_now, u_a, u_gate, u_decay, u_enc, u_reset;',
    'float lum(vec3 c){ return dot(c, vec3(0.2126, 0.7152, 0.0722)); }',
    'vec3 layer(vec2 uv, float i){ return texture(u_ring, vec3(uv, mod(u_head - i + 2.0 * u_n, u_n))).rgb; }',
    'vec3 ring(float back){',
    '  float f = clamp(back, 0.0, u_n - 2.0), i0 = floor(f), t = f - i0;',
    '  vec3 a = layer(v, i0);',
    '  return t < 0.002 ? a : mix(a, layer(v, i0 + 1.0), t);',
    '}',
    'float soft(float i){',   // a small box, so sensor noise does not read as movement
    '  vec2 d = u_px * 1.5;',
    '  return sqrt(lum(layer(v + d, i) + layer(v - d, i) + layer(v + vec2(d.x, -d.y), i) + layer(v + vec2(-d.x, d.y), i)) * 0.25);',
    '}',
    'void main(){',
    '  vec3 base = texture(u_src, v).rgb;',
    '  if (u_useRing > 0.5) base = mix(ring(u_lag), base, u_now);',
    '  vec4 pv = texture(u_prev, v);',
    '  vec3 prev = u_enc > 0.5 ? pv.rgb * pv.rgb : pv.rgb;',
    '  vec3 col = mix(prev, base, u_reset > 0.5 ? 1.0 : u_a);',
    '  float trail = 0.0;',
    '  if (u_gate > 0.5) {',
    '    float d = abs(soft(0.0) - soft(1.0)) - 0.03;',
    '    trail = max(u_reset > 0.5 ? 0.0 : pv.a * u_decay, clamp(d * 9.0, 0.0, 1.0));',
    '  }',
    '  o = vec4(u_enc > 0.5 ? sqrt(max(col, 0.0)) : col, trail);',
    '}'].join('\n');
  var FS_VIEW = [
    '#version 300 es', 'precision highp float;', 'in vec2 v; out vec4 o;',
    'uniform sampler2D u_t;',
    'uniform vec2 u_res, u_aniso, u_apC; uniform float u_srcAspect, u_texLong, u_maxLod, u_enc, u_mirror;',
    'uniform float u_zoom, u_barrel, u_fovea, u_blur, u_fall, u_wA, u_wS, u_dof, u_focus, u_soft;',
    'uniform mat3 u_M; uniform float u_uvBlue, u_sheen, u_gain, u_sat, u_noGreen, u_gateMix, u_field, u_expo;',
    'uniform float u_ap, u_mosaic; uniform int u_shape;',
    'vec3 dec(vec4 s){ return u_enc > 0.5 ? s.rgb * s.rgb : s.rgb; }',
    'vec3 srgb(vec3 c){ c = clamp(c, 0.0, 1.0); return mix(c * 12.92, 1.055 * pow(c, vec3(1.0 / 2.4)) - 0.055, step(0.0031308, c)); }',
    'vec2 hexC(vec2 p, float s){ vec2 r = vec2(1.0, 1.7320508), h = r * 0.5; vec2 a = mod(p / s, r) - h, b = mod(p / s - h, r) - h; vec2 g = dot(a, a) < dot(b, b) ? a : b; return p - g * s; }',
    'void main(){',
    '  float A = u_res.x / u_res.y, longPx = max(u_res.x, u_res.y);',
    '  vec2 p = (v - 0.5) * vec2(A, 1.0);',
    '  vec2 pa = p - u_apC;',
    '  float facet = 0.0;',
    '  if (u_mosaic > 0.001) { float cell = mix(0.010, 0.058, u_mosaic); vec2 c = hexC(p, cell); facet = length(p - c) / cell; p = mix(p, c, smoothstep(0.0, 0.25, u_mosaic)); }',
    '  float r = length(p);',
    '  float rn = clamp(r / (0.45 * sqrt(A * A + 1.0)), 0.0, 1.0);',
    '  float mag = 1.0 / mix(1.0 / u_fovea, 1.0, rn * rn);',   // a smooth bulge: the centre pulled close, the corners left where they were
    '  vec2 q = p * (1.0 + u_barrel * r * r) / (u_zoom * mag);',
    '  float k = max(1.0, A / u_srcAspect);',
    '  vec2 span = vec2(k * u_srcAspect, k);',
    '  vec2 uv = q / span + 0.5;',
    '  uv.x = mix(uv.x, 1.0 - uv.x, u_mirror);',
    '  float outside = max(max(max(-uv.x, uv.x - 1.0), max(-uv.y, uv.y - 1.0)), 0.0);',
    '  float topo = u_wA * (r / 0.5) + u_wS * (abs(p.y) / 0.5);',
    '  float ra = u_blur * (1.0 + u_fall * topo * topo) + u_soft;',
    '  float rd = u_dof * min(abs(v.y - u_focus) * 2.0, 1.2);',   // GUESSED depth: height in the frame stands in for distance
    '  vec2 rad = sqrt(vec2(ra * ra) + (rd * u_aniso) * (rd * u_aniso)) + vec2(outside * 0.22 * longPx);',
    '  float pxTex = u_texLong / (longPx * u_zoom);',
    '  float lod = clamp(log2(max(sqrt(rad.x * rad.y) * pxTex * 0.7, 1.0)), 0.0, u_maxLod);',
    '  vec2 toUv = 1.0 / (u_res.y * span * u_zoom * mag);',
    '  vec3 acc = vec3(0.0); float trail = 0.0;',
    '  for (int i = 0; i < 16; i++) {',
    '    float fi = float(i), rr = sqrt((fi + 0.5) / 16.0), th = fi * 2.39996323;',
    '    vec4 s = textureLod(u_t, uv + rr * vec2(cos(th), sin(th)) * rad * toUv, lod);',
    '    acc += dec(s); trail += s.a;',
    '  }',
    '  acc /= 16.0; trail /= 16.0;',
    '  if (u_field > 0.001) acc = mix(acc, dec(textureLod(u_t, uv, max(u_maxLod - 2.0, 0.0))), u_field);',
    '  acc *= mix(1.0, 0.5, smoothstep(0.0, 0.35, outside)) * u_expo;',
    '  vec3 c = acc * u_gain / (1.0 + (u_gain - 1.0) * acc);',
    '  float mn = min(c.r, min(c.g, c.b));',
    '  float uvg = clamp(1.6 * (c.b - 0.5 * (c.r + c.g)) + 2.5 * max(mn - 0.6, 0.0), 0.0, 1.0);',   // INVENTED ultraviolet
    '  vec3 m = u_M * c;',
    '  m.b = mix(m.b, uvg, u_uvBlue);',
    '  m = mix(m, vec3(0.62, 0.12, 1.0), 0.45 * uvg * u_sheen);',
    '  m.g *= 1.0 - 0.9 * u_noGreen;',
    '  m = mix(vec3(dot(m, vec3(0.2126, 0.7152, 0.0722))), m, u_sat);',
    '  m *= mix(1.0, 0.035 + 1.7 * trail, u_gateMix);',
    '  m *= 1.0 - 0.35 * u_mosaic * smoothstep(0.35, 0.5, facet);',
    '  if (u_ap < 0.999) {',
    '    float d; float ra2 = length(pa);',
    '    if (u_shape == 1) { float a = mix(0.030, 0.9 * A + 0.35, u_ap * u_ap), b = mix(0.40, 2.2, u_ap); d = abs(pa.x) / a + (pa.y / b) * (pa.y / b); }',
    '    else if (u_shape == 2) { float a = mix(0.34, 2.6, u_ap), b = mix(0.075, 1.2, u_ap * u_ap); d = pow(pow(abs(pa.x) / a, 4.0) + pow(abs(pa.y) / b, 4.0), 0.25); }',
    '    else { d = ra2 / mix(0.085, 1.5, u_ap * u_ap); }',
    '    m *= 1.0 - smoothstep(0.93, 1.05, d);',
    '  }',
    '  o = vec4(srgb(m), 1.0);',
    '}'].join('\n');

  function Engine(canvas) {
    var gl = canvas.getContext('webgl2', { alpha: false, antialias: false, powerPreference: 'high-performance' });
    if (!gl) return null;
    var floatOK = !!gl.getExtension('EXT_color_buffer_float');
    function shader(type, src) { var s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s); if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s)); return s; }
    function prog(fs) {
      var p = gl.createProgram(); gl.attachShader(p, shader(gl.VERTEX_SHADER, VS)); gl.attachShader(p, shader(gl.FRAGMENT_SHADER, fs));
      gl.bindAttribLocation(p, 0, 'a'); gl.linkProgram(p);
      if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p));
      var u = {}, n = gl.getProgramParameter(p, gl.ACTIVE_UNIFORMS);
      for (var i = 0; i < n; i++) { var info = gl.getActiveUniform(p, i); u[info.name] = gl.getUniformLocation(p, info.name); }
      return { p: p, u: u };
    }
    var pCopy = prog(FS_COPY), pTime = prog(FS_TIME), pView = prog(FS_VIEW);
    var vao = gl.createVertexArray(); gl.bindVertexArray(vao);
    var buf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    gl.enableVertexAttribArray(0); gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);

    var N = 12, STRIDE = 2, MAXSIDE = 1280;
    var texSrc = gl.createTexture(), ring = null, tA = null, tB = null, fbT = gl.createFramebuffer(), fbR = gl.createFramebuffer();
    var sw = 0, sh = 0, levels = 1, head = 0, frames = 0, writes = 0, tHead = 0, stepMs = 66, reset = true;
    var lag = 0, holdT0 = 0, holdAt = -1, hasFrame = false, moving = false;
    gl.bindTexture(gl.TEXTURE_2D, texSrc);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);

    function makeTime() {
      var t = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, t);
      gl.texStorage2D(gl.TEXTURE_2D, levels, floatOK ? gl.RGBA16F : gl.RGBA8, sw, sh);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.MIRRORED_REPEAT); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.MIRRORED_REPEAT);
      return t;
    }
    function resetTime() { head = 0; frames = 0; writes = 0; lag = 0; holdAt = -1; tHead = 0; reset = true; }
    function alloc(w, h) {
      sw = w; sh = h; levels = Math.floor(Math.log2(Math.max(sw, sh))) + 1;
      [tA, tB, ring].forEach(function (t) { if (t) gl.deleteTexture(t); });
      tA = makeTime(); tB = makeTime();
      ring = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D_ARRAY, ring);
      gl.texStorage3D(gl.TEXTURE_2D_ARRAY, 1, gl.SRGB8_ALPHA8, sw, sh, N);
      gl.texParameteri(gl.TEXTURE_2D_ARRAY, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D_ARRAY, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D_ARRAY, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D_ARRAY, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      resetTime();
    }
    function upload(source, w, h) {
      if (!w || !h) return false;
      var k = Math.min(1, MAXSIDE / Math.max(w, h)), nw = Math.max(2, Math.round(w * k)), nh = Math.max(2, Math.round(h * k));
      if (nw !== sw || nh !== sh || !tA) alloc(nw, nh);
      gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, texSrc);
      gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, true);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.SRGB8_ALPHA8, gl.RGBA, gl.UNSIGNED_BYTE, source);
      gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false);
      hasFrame = true; return true;
    }
    function pushRing(now) {
      frames++;
      if (frames % STRIDE) return;
      head = (head + 1) % N; writes++;
      if (tHead) stepMs = lerp(stepMs, clamp(now - tHead, 20, 200), .15);
      tHead = now;
      gl.bindVertexArray(vao);
      gl.bindFramebuffer(gl.FRAMEBUFFER, fbR);
      gl.framebufferTextureLayer(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, ring, 0, head);
      gl.viewport(0, 0, sw, sh); gl.useProgram(pCopy.p);
      gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, texSrc); gl.uniform1i(pCopy.u.u_src, 0);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
    }
    return {
      floatOK: floatOK,
      setImage: function (cv) { moving = false; if (upload(cv, cv.width, cv.height)) reset = true; },
      setFrame: function (source, w, h, now) { if (!moving) { moving = true; resetTime(); } if (upload(source, w, h)) pushRing(now); },
      resetTime: resetTime,
      setSide: function (n) { MAXSIDE = Math.max(240, Math.round(n)); },
      side: function () { return MAXSIDE; },
      clear: function () { hasFrame = false; },
      hasFrame: function () { return hasFrame; },
      state: function () { return { sw: sw, sh: sh, writes: writes, stepMs: stepMs, moving: moving, floatOK: floatOK, err: gl.getError() }; },
      resize: function () {
        var dpr = Math.min(window.devicePixelRatio || 1, 2), w = canvas.clientWidth * dpr, h = canvas.clientHeight * dpr, k = Math.min(1, MAXSIDE / Math.max(w, h, 1));
        w = Math.max(2, Math.round(w * k)); h = Math.max(2, Math.round(h * k));
        if (canvas.width !== w || canvas.height !== h) { canvas.width = w; canvas.height = h; }
      },
      draw: function (P, fx, now, dt) {
        gl.bindVertexArray(vao);
        if (!hasFrame) { gl.bindFramebuffer(gl.FRAMEBUFFER, null); gl.viewport(0, 0, canvas.width, canvas.height); gl.clearColor(0, 0, 0, 1); gl.clear(gl.COLOR_BUFFER_BIT); return; }
        var useRing = 0, back = 0, nowMix = 0, a = 1;
        if (moving && writes > N) {
          if (P.hold > 0) {
            var ph = now - holdT0;
            if (holdAt < 0 || ph >= P.hold + P.thrust) { holdT0 = now; ph = 0; holdAt = writes; }   // the gaze fixes on this moment
            if (ph < P.hold) { back = Math.min(N - 2, writes - holdAt); useRing = 1; }
            else a = .3;                                                                             // the thrust: the picture runs, smeared
            lag = 0;
          } else if (P.rate < .999) {
            var top = N - 3;
            lag += (1 - P.rate) * dt / stepMs;
            if (lag >= top) lag = 0;                                // the stretch has run out: back to now
            nowMix = lag > top - 1.5 ? (lag - (top - 1.5)) / 1.5 : 0;
            back = clamp(lag - (now - tHead) / stepMs, 0, N - 2); useRing = 1;
          } else { lag = 0; holdAt = -1; }
        } else { lag = 0; holdAt = -1; }
        if (moving && P.persist > 0) { a = 1 - Math.exp(-(dt / 1000) / P.persist); if (!floatOK) a = Math.max(a, .2); }
        gl.bindFramebuffer(gl.FRAMEBUFFER, fbT);
        gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, tB, 0);
        gl.viewport(0, 0, sw, sh); gl.useProgram(pTime.p);
        var ut = pTime.u;
        gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, texSrc); gl.uniform1i(ut.u_src, 0);
        gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, tA); gl.uniform1i(ut.u_prev, 1);
        gl.activeTexture(gl.TEXTURE2); gl.bindTexture(gl.TEXTURE_2D_ARRAY, ring); gl.uniform1i(ut.u_ring, 2);
        gl.uniform2f(ut.u_px, 1 / sw, 1 / sh);
        gl.uniform1f(ut.u_n, N); gl.uniform1f(ut.u_head, head); gl.uniform1f(ut.u_lag, back); gl.uniform1f(ut.u_useRing, useRing); gl.uniform1f(ut.u_now, nowMix);
        gl.uniform1f(ut.u_a, a); gl.uniform1f(ut.u_gate, moving && writes > 2 && P.gate > .5 ? 1 : 0); gl.uniform1f(ut.u_decay, Math.exp(-dt / 420));
        gl.uniform1f(ut.u_enc, floatOK ? 0 : 1); gl.uniform1f(ut.u_reset, reset ? 1 : 0);
        gl.drawArrays(gl.TRIANGLES, 0, 3);
        reset = false;
        var t = tA; tA = tB; tB = t;
        gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, tA); gl.generateMipmap(gl.TEXTURE_2D);
        gl.bindFramebuffer(gl.FRAMEBUFFER, null);
        gl.viewport(0, 0, canvas.width, canvas.height); gl.useProgram(pView.p);
        var u = pView.u, longPx = Math.max(canvas.width, canvas.height), sc = longPx / 1280;
        var blur = P.inv > 1 / (HUMAN_CPD - 1) ? .6 * (longPx / VIEW_DEG) * P.inv : 0;   // 0.6 of one cycle at that eye's limit
        gl.uniform1i(u.u_t, 0);
        gl.uniform2f(u.u_res, canvas.width, canvas.height); gl.uniform2f(u.u_aniso, P.ax, P.ay);
        gl.uniform2f(u.u_apC, fx.apX || 0, fx.apY || 0);
        gl.uniform1f(u.u_srcAspect, sw / sh); gl.uniform1f(u.u_texLong, Math.max(sw, sh)); gl.uniform1f(u.u_maxLod, levels - 1);
        gl.uniform1f(u.u_enc, floatOK ? 0 : 1); gl.uniform1f(u.u_mirror, fx.mirror ? 1 : 0);
        gl.uniform1f(u.u_zoom, P.zoom / (fx.camZoom || 1)); gl.uniform1f(u.u_barrel, P.barrel); gl.uniform1f(u.u_fovea, P.fovea);
        gl.uniform1f(u.u_blur, blur); gl.uniform1f(u.u_fall, P.fall); gl.uniform1f(u.u_wA, P.wA); gl.uniform1f(u.u_wS, P.wS);
        gl.uniform1f(u.u_dof, P.dof * sc); gl.uniform1f(u.u_focus, fx.focus === undefined ? .5 : fx.focus); gl.uniform1f(u.u_soft, (fx.soft || 0) * sc);
        gl.uniformMatrix3fv(u.u_M, true, new Float32Array(P.M));
        gl.uniform1f(u.u_uvBlue, P.uvBlue); gl.uniform1f(u.u_sheen, P.sheen); gl.uniform1f(u.u_gain, P.gain); gl.uniform1f(u.u_sat, P.sat);
        gl.uniform1f(u.u_noGreen, P.noGreen); gl.uniform1f(u.u_gateMix, moving ? P.gate : 0); gl.uniform1f(u.u_field, P.field);
        gl.uniform1f(u.u_expo, fx.expo === undefined ? 1 : fx.expo);
        gl.uniform1f(u.u_ap, fx.ap === undefined ? 1 : fx.ap); gl.uniform1i(u.u_shape, fx.shape || 0); gl.uniform1f(u.u_mosaic, fx.mosaic || 0);
        gl.drawArrays(gl.TRIANGLES, 0, 3);
      }
    };
  }
