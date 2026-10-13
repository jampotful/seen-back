
  // ---------- the engine: passes on the phone's graphics chip
  // 1. every second camera frame is kept in a short ring of past moments
  // 2. time: trails, held gazes and slowed moments are mixed from that ring (with zones, each zone at its own pace)
  // 3. space and colour: field, sharpness, pupil, light, colour, and the aperture (with zones, each region its own)
  // For a view with salience (build 23), each new camera frame also passes through four small steps: a grey copy about 64 cells
  // on its long side, the phone's own shift between that copy and the last, a map of movement energy with a cue for the movement
  // of living things, and a few times a second a read of that map which the gaze answers. docs/ENGINE.md describes every field.
  var VS = '#version 300 es\nin vec2 a; out vec2 v; void main(){ v = a * 0.5 + 0.5; gl_Position = vec4(a, 0.0, 1.0); }';
  var FS_COPY = '#version 300 es\nprecision highp float; in vec2 v; out vec4 o; uniform sampler2D u_src; void main(){ o = vec4(texture(u_src, v).rgb, 1.0); }';
  // Where a zone lies, in the camera picture's own coordinates (as the time and view passes both sample it), with soft edges.
  var ZONE_GLSL = [
    'uniform vec4 u_zG[4];',   // centre x, y; half width, half height, in units of the picture's height
    'uniform vec4 u_zH[4];',   // shape (1 strip, 2 ellipse, 3 annulus, 4 band, 0 the whole field), soft edge, inner edge of an annulus
    'uniform vec4 u_zR[4];',   // cos and sin of the zone's turn
    'uniform int u_nz;',
    'float zoneW(int i, vec2 uv){',
    '  vec4 g = u_zG[i], h = u_zH[i], r = u_zR[i];',
    '  if (h.x < 0.5) return 1.0;',
    '  vec2 d = (uv - g.xy) * vec2(u_srcAspect, 1.0);',
    '  d = vec2(r.x * d.x + r.y * d.y, -r.y * d.x + r.x * d.y);',
    '  float s = max(h.y, 1e-4);',
    '  if (h.x < 1.5) { vec2 e = abs(d) - g.zw; return (1.0 - smoothstep(-s, s, e.x)) * (1.0 - smoothstep(-s, s, e.y)); }',
    '  if (h.x > 3.5) return 1.0 - smoothstep(-s, s, abs(d.y) - g.w);',
    '  vec2 sz = max(g.zw, vec2(1e-4)); float q = length(d / sz), sr = s / min(sz.x, sz.y);',
    '  float w = 1.0 - smoothstep(1.0 - sr, 1.0 + sr, q);',
    '  if (h.x > 2.5) w *= smoothstep(h.z - sr, h.z + sr, q);',
    '  return w;',
    '}'].join('\n');
  function withZones(src, z) { var i = src.indexOf('\n'); return src.slice(0, i + 1) + '#define ZONES ' + (z ? 1 : 0) + '\n' + src.slice(i + 1); }
  var FS_TIME = [
    '#version 300 es', 'precision highp float; precision highp sampler2DArray;', 'in vec2 v; out vec4 o;',
    'uniform sampler2D u_src, u_prev; uniform sampler2DArray u_ring; uniform vec2 u_px;',
    'uniform float u_n, u_head, u_lag, u_useRing, u_now, u_a, u_gate, u_decay, u_enc, u_reset;',
    '#if ZONES', 'uniform float u_srcAspect; uniform vec4 u_zT[4];', ZONE_GLSL, '#endif',
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
    '#if ZONES',
    '  vec3 now0 = base;',
    '#endif',
    '  if (u_useRing > 0.5) base = mix(ring(u_lag), base, u_now);',
    '#if ZONES',   // each zone at its own pace: its own place in the ring, layered over the view's own
    '  for (int i = 0; i < 4; i++) {',
    '    if (i >= u_nz) break;',
    '    float w = zoneW(i, v); vec4 zt = u_zT[i];',
    '    if (w > 0.001) base = mix(base, zt.y > 0.5 ? mix(ring(zt.x), now0, zt.z) : now0, w);',
    '  }',
    '#endif',
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
    '#if ZONES', ZONE_GLSL,
    'uniform vec4 u_zP[4];',   // blur radius in pixels, saturation, gain, gate
    'uniform vec4 u_zQ[4];',   // glow, living, ultraviolet, magnification
    'uniform vec4 u_zS[4];',   // sheen
    'uniform mat3 u_zM[4];',
    'uniform sampler2D u_sal; uniform float u_salOn; uniform vec2 u_base; uniform vec3 u_glowC;',   // the movement map; the view\'s own glow and living weight
    'uniform vec4 u_ior[6];',  // places the side eyes are ignoring: x, y, reach, strength
    'uniform vec4 u_rip[4]; uniform float u_ripK;',   // ripples on the screen: x, y, age in seconds, strength
    'vec2 ripple(vec2 p){',
    '  vec2 s = vec2(0.0);',
    '  for (int i = 0; i < 4; i++) {',
    '    vec4 R = u_rip[i]; if (R.w <= 0.0) continue;',
    '    vec2 d = p - R.xy; float r = length(d) + 1e-5, x = r - R.z * 0.55;',   // the ring runs out at about half a screen height a second
    '    s += d / r * (R.w * 0.016 * exp(-x * x / 0.007 - R.z * 1.4) * sin(x * 64.0));',
    '  }',
    '  return s * u_ripK;',
    '}',
    '#endif',
    'vec3 dec(vec4 s){ return u_enc > 0.5 ? s.rgb * s.rgb : s.rgb; }',
    'vec3 srgb(vec3 c){ c = clamp(c, 0.0, 1.0); return mix(c * 12.92, 1.055 * pow(c, vec3(1.0 / 2.4)) - 0.055, step(0.0031308, c)); }',
    'vec2 hexC(vec2 p, float s){ vec2 r = vec2(1.0, 1.7320508), h = r * 0.5; vec2 a = mod(p / s, r) - h, b = mod(p / s - h, r) - h; vec2 g = dot(a, a) < dot(b, b) ? a : b; return p - g * s; }',
    'void main(){',
    '  float A = u_res.x / u_res.y, longPx = max(u_res.x, u_res.y);',
    '  vec2 p = (v - 0.5) * vec2(A, 1.0);',
    '#if ZONES',
    '  if (u_ripK > 0.0) p += ripple(p);',
    '#endif',
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
    '  float gain = u_gain, sat = u_sat, gateMix = u_gateMix, uvB = u_uvBlue, sheen = u_sheen, zmag = 1.0; mat3 M = u_M;',
    '#if ZONES',   // the zones, layered over the view in order, each blended in by its soft-edged weight at this place
    '  vec2 uv0 = uv; vec2 gl0 = u_base;',
    '  for (int i = 0; i < 4; i++) {',
    '    if (i >= u_nz) break;',
    '    float w = zoneW(i, uv0);',
    '    if (w > 0.0005) {',
    '      vec4 zp = u_zP[i], zq = u_zQ[i];',
    '      ra = mix(ra, zp.x + u_soft, w); sat = mix(sat, zp.y, w); gain = mix(gain, zp.z, w); gateMix = mix(gateMix, zp.w, w);',
    '      gl0 = mix(gl0, zq.xy, w); uvB = mix(uvB, zq.z, w); sheen = mix(sheen, u_zS[i].x, w);',
    '      M = M + (u_zM[i] - M) * w;',
    '      if (zq.w > 1.001) { float zm = mix(1.0, zq.w, w); vec2 c = u_zG[i].xy; uv = c + (uv - c) / zm; zmag *= zm; }',   // a zone that magnifies what it holds
    '    }',
    '  }',
    '#endif',
    '  float rd = u_dof * min(abs(v.y - u_focus) * 2.0, 1.2);',   // GUESSED depth: height in the frame stands in for distance
    '  vec2 rad = sqrt(vec2(ra * ra) + (rd * u_aniso) * (rd * u_aniso)) + vec2(outside * 0.22 * longPx);',
    '  float pxTex = u_texLong / (longPx * u_zoom * zmag);',
    '  float lod = clamp(log2(max(sqrt(rad.x * rad.y) * pxTex * 0.7, 1.0)), 0.0, u_maxLod);',
    '  vec2 toUv = 1.0 / (u_res.y * span * u_zoom * mag * zmag);',
    '  vec3 acc = vec3(0.0); float trail = 0.0;',
    '  for (int i = 0; i < 16; i++) {',
    '    float fi = float(i), rr = sqrt((fi + 0.5) / 16.0), th = fi * 2.39996323;',
    '    vec4 s = textureLod(u_t, uv + rr * vec2(cos(th), sin(th)) * rad * toUv, lod);',
    '    acc += dec(s); trail += s.a;',
    '  }',
    '  acc /= 16.0; trail /= 16.0;',
    '  if (u_field > 0.001) acc = mix(acc, dec(textureLod(u_t, uv, max(u_maxLod - 2.0, 0.0))), u_field);',
    '  float edge = mix(1.0, 0.5, smoothstep(0.0, 0.35, outside));',
    '  acc *= edge * u_expo;',
    '  vec3 c = acc * gain / (1.0 + (gain - 1.0) * acc);',
    '  float mn = min(c.r, min(c.g, c.b));',
    '  float uvg = clamp(1.6 * (c.b - 0.5 * (c.r + c.g)) + 2.5 * max(mn - 0.6, 0.0), 0.0, 1.0);',   // INVENTED ultraviolet
    '  vec3 m = M * c;',
    '  m.b = mix(m.b, uvg, uvB);',
    '  m = mix(m, vec3(0.62, 0.12, 1.0), 0.45 * uvg * sheen);',
    '  m.g *= 1.0 - 0.9 * u_noGreen;',
    '  m = mix(vec3(dot(m, vec3(0.2126, 0.7152, 0.0722))), m, sat);',
    '#if ZONES',   // movement glows, where the view asks for it, except at the places the side eyes are ignoring
    '  if (u_salOn > 0.001) {',
    '    vec4 sl = texture(u_sal, uv0);',
    '    float g = (sl.r + gl0.y * sl.g) * gl0.x * u_salOn, ig = 0.0;',
    '    for (int j = 0; j < 6; j++) { vec4 I = u_ior[j]; if (I.w > 0.0) { vec2 dd = (uv0 - I.xy) * vec2(u_srcAspect, 1.0); ig = max(ig, I.w * exp(-dot(dd, dd) / (I.z * I.z))); } }',
    '    m += u_glowC * (g * (1.0 - ig) * edge * u_expo);',
    '  }',
    '#endif',
    '  m *= mix(1.0, 0.035 + 1.7 * trail, gateMix);',
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

  // ---- salience: four small passes on each new camera frame, for views that ask for it
  // 1. a grey copy of the frame, about 64 cells on its long side (square roots of brightness, so that dark noise counts for less)
  var FS_LOW = ['#version 300 es', 'precision highp float; in vec2 v; out vec4 o;', 'uniform sampler2D u_src; uniform vec2 u_cell;',
    'void main(){',
    '  float s = 0.0;',
    '  for (int j = 0; j < 4; j++) for (int i = 0; i < 4; i++) s += dot(texture(u_src, v + (vec2(float(i), float(j)) - 1.5) * 0.25 * u_cell).rgb, vec3(0.2126, 0.7152, 0.0722));',
    '  o = vec4(sqrt(s / 16.0), 0.0, 0.0, 1.0);',
    '}'].join('\n');
  // 2. how well this copy matches the last one for each of 7 by 7 shifts around the expected one: the phone's own movement
  var FS_SHIFT = ['#version 300 es', 'precision highp float; out vec4 o;', 'uniform sampler2D u_a, u_b; uniform ivec2 u_n; uniform vec2 u_prior;',
    'void main(){',
    '  ivec2 s = ivec2(gl_FragCoord.xy) - 3 + ivec2(floor(u_prior + 0.5));',
    '  float acc = 0.0, n = 0.0;',
    '  for (int y = 4; y < u_n.y - 4; y += 2) for (int x = 4; x < u_n.x - 4; x += 2) {',
    '    ivec2 c = ivec2(x, y);',
    '    acc += abs(texelFetch(u_a, c, 0).r - texelFetch(u_b, clamp(c + s, ivec2(0), u_n - 1), 0).r); n += 1.0;',
    '  }',
    '  o = vec4(acc / max(n, 1.0) * 8.0, 0.0, 0.0, 1.0);',
    '}'].join('\n');
  // 3. the best of those shifts, to a fraction of a cell (cell 0), and the frame's mean brightness (cell 1)
  var FS_RES = ['#version 300 es', 'precision highp float; out vec4 o;', 'uniform sampler2D u_shift, u_a; uniform ivec2 u_n; uniform vec2 u_prior;',
    'void main(){',
    '  int px = int(gl_FragCoord.x);',
    '  if (px == 0) {',
    '    float best = 1e9; ivec2 b = ivec2(3);',
    '    for (int j = 0; j < 7; j++) for (int i = 0; i < 7; i++) { float e = texelFetch(u_shift, ivec2(i, j), 0).r; if (e < best) { best = e; b = ivec2(i, j); } }',
    '    vec2 f = vec2(0.0);',
    '    if (b.x > 0 && b.x < 6) { float l = texelFetch(u_shift, b - ivec2(1, 0), 0).r, r = texelFetch(u_shift, b + ivec2(1, 0), 0).r, d = l - 2.0 * best + r; if (d > 1e-5) f.x = clamp(0.5 * (l - r) / d, -0.5, 0.5); }',
    '    if (b.y > 0 && b.y < 6) { float l = texelFetch(u_shift, b - ivec2(0, 1), 0).r, r = texelFetch(u_shift, b + ivec2(0, 1), 0).r, d = l - 2.0 * best + r; if (d > 1e-5) f.y = clamp(0.5 * (l - r) / d, -0.5, 0.5); }',
    '    vec2 s = vec2(b - 3) + floor(u_prior + 0.5) + f;',
    '    o = vec4(clamp(0.5 + s / 16.0, 0.0, 1.0), clamp(best, 0.0, 1.0), clamp(texelFetch(u_shift, ivec2(3), 0).r, 0.0, 1.0));',
    '  } else if (px == 1) {',
    '    float acc = 0.0, n = 0.0;',
    '    for (int y = 1; y < u_n.y; y += 3) for (int x = 1; x < u_n.x; x += 3) { acc += texelFetch(u_a, ivec2(x, y), 0).r; n += 1.0; }',
    '    o = vec4(acc / max(n, 1.0), 0.0, 0.0, 1.0);',
    '  } else o = vec4(0.0);',
    '}'].join('\n');
  // 4. the movement map: (energy, living, slow energy, rhythm). Energy is the change from the last frame once the phone's own shift is
  // taken out, above the noise and above what a slightly wrong shift leaves at an edge. Living is the app's own cue for the movement of
  // living things (INVENTED): local movement that keeps one direction over the 3 by 3 patch (coherence of normal flow) and pulses
  // (energy that changes from frame to frame more than its slow average would), as walking legs do.
  var FS_SAL = ['#version 300 es', 'precision highp float; in vec2 v; out vec4 o;',
    'uniform sampler2D u_a, u_b, u_res, u_prev; uniform vec2 u_cell; uniform vec4 u_k; uniform float u_damp, u_fresh;',
    'float L(sampler2D t, vec2 q){ return texture(t, q).r; }',
    'void main(){',
    '  vec4 rs = texelFetch(u_res, ivec2(0, 0), 0);',
    '  vec2 sc = (rs.xy - 0.5) * 16.0, s = sc * u_cell;',
    '  vec2 F = vec2(0.0); float Fm = 0.0, dc = 0.0;',
    '  for (int j = -1; j <= 1; j++) for (int i = -1; i <= 1; i++) {',
    '    vec2 q = v + vec2(float(i), float(j)) * u_cell, qb = q + s;',
    '    float a = L(u_a, q), b = L(u_b, qb);',
    '    float gx = 0.5 * (L(u_a, q + vec2(u_cell.x, 0.0)) - L(u_a, q - vec2(u_cell.x, 0.0)));',
    '    float gy = 0.5 * (L(u_a, q + vec2(0.0, u_cell.y)) - L(u_a, q - vec2(0.0, u_cell.y)));',
    '    float it = a - b, g2 = gx * gx + gy * gy;',
    '    float d = max(abs(it) - 0.02 - 0.4 * sqrt(g2), 0.0);',
    '    if (qb.x < 0.0 || qb.y < 0.0 || qb.x > 1.0 || qb.y > 1.0) d = 0.0;',
    '    vec2 fl = -it * vec2(gx, gy) / (g2 + 0.0004);',
    '    F += fl * d; Fm += length(fl) * d;',
    '    if (i == 0 && j == 0) dc = d;',
    '  }',
    '  float coh = Fm > 1e-5 ? length(F) / Fm : 0.0;',
    '  vec4 P = texture(u_prev, v);',
    '  float e = clamp(dc * 6.0, 0.0, 1.0) * u_damp * (1.0 - smoothstep(2.2, 4.0, length(sc))) * u_fresh;',   // a phone turned fast: its movement is not trusted to be gone
    '  float E = mix(P.r, e, u_k.x), Es = mix(P.b, e, u_k.y), Rh = mix(P.a, abs(e - P.r), u_k.z);',
    '  float liv = coh * clamp(Rh * 3.0 / (Es + 0.08), 0.0, 1.0) * clamp(E * 3.0, 0.0, 1.0);',
    '  float Lv = mix(P.g, liv, u_k.w);',
    '  o = vec4(max(E - 0.004, 0.0), max(Lv - 0.004, 0.0), Es, Rh);',   // at least one step of decay, so that nothing sticks in eight bits
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
    var pCopy = prog(FS_COPY), pTime = prog(withZones(FS_TIME, 0)), pView = prog(withZones(FS_VIEW, 0));
    // The programs for zones and salience are compiled the first time a view needs them, so a phone that never meets one pays nothing.
    var pTimeZ = null, pViewZ = null, pLow = null, pShift = null, pRes = null, pSal = null, zErr = '';
    function zonePrograms() {
      if (pViewZ || zErr) return !!pViewZ;
      try { pTimeZ = prog(withZones(FS_TIME, 1)); pViewZ = prog(withZones(FS_VIEW, 1)); pLow = prog(FS_LOW); pShift = prog(FS_SHIFT); pRes = prog(FS_RES); pSal = prog(FS_SAL); }
      catch (e) { zErr = String(e && e.message || e).slice(0, 300); pViewZ = null; if (window.console) console.error(e); }
      return !!pViewZ;
    }
    var vao = gl.createVertexArray(); gl.bindVertexArray(vao);

    // ---- the frame-time probe: the graphics chip's own time for a frame where the browser offers a timer query
    // (EXT_disjoint_timer_query_webgl2), and the script's time inside draw() everywhere. A query's answer arrives a few frames
    // later and is polled, never waited for; a frame the driver marks as disjoint is dropped.
    var tq = null; try { tq = gl.getExtension('EXT_disjoint_timer_query_webgl2'); } catch (e) { tq = null; }
    var qFree = [], qWait = [], qNow = null, gpuMs = [], cpuMs = [];
    function keep(a, x) { a.push(x); if (a.length > 90) a.shift(); }
    function avg(a) { if (!a.length) return null; var s = 0; for (var i = 0; i < a.length; i++) s += a[i]; return s / a.length; }
    function qBegin() { if (!tq || qNow || qWait.length > 6) return; qNow = qFree.pop() || gl.createQuery(); gl.beginQuery(tq.TIME_ELAPSED_EXT, qNow); }
    function qEnd() { if (!qNow) return; gl.endQuery(tq.TIME_ELAPSED_EXT); qWait.push(qNow); qNow = null; }
    function qPoll() {
      if (!tq || !qWait.length) return;
      var lost = gl.getParameter(tq.GPU_DISJOINT_EXT);
      while (qWait.length && gl.getQueryParameter(qWait[0], gl.QUERY_RESULT_AVAILABLE)) {
        var q = qWait.shift(), ns = gl.getQueryParameter(q, gl.QUERY_RESULT); qFree.push(q);
        if (!lost) keep(gpuMs, ns / 1e6);
      }
    }
    var buf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    gl.enableVertexAttribArray(0); gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);

    var N = 12, STRIDE = 2, MAXSIDE = 1280;
    var texSrc = gl.createTexture(), ring = null, tA = null, tB = null, fbT = gl.createFramebuffer(), fbR = gl.createFramebuffer();
    var sw = 0, sh = 0, levels = 1, head = 0, frames = 0, writes = 0, tHead = 0, stepMs = 66, reset = true;
    var lag = 0, holdT0 = 0, holdAt = -1, hasFrame = false, moving = false, fresh = false, freshAt = 0;
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
    function resetTime() { head = 0; frames = 0; writes = 0; lag = 0; holdAt = -1; tHead = 0; reset = true; zLag = [0, 0, 0, 0]; salReset(); }
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

    // ---- the movement map and its read-back (salience)
    var SAL_SIDES = [64, 48, 32], salStep = 0, ws = 0, hs = 0, lowT = [null, null], lowN = 0, lowAt = 0, shiftT = null, resT = null, salT = [null, null], salAt = 0;
    var fbS = gl.createFramebuffer(), pbo = null, map = null, sync = null, readAt = 0, readMs = 160, salFrames = 0, lastFreshAt = 0;
    var mapInfo = { at: 0, maxE: 0, maxL: 0, meanE: 0, lum: 0, shift: [0, 0], fit: 0, still: 0, reads: 0 };
    function tex2(w, h, fmt, filt) {
      var t = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, t); gl.texStorage2D(gl.TEXTURE_2D, 1, fmt, w, h);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, filt); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, filt);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      return t;
    }
    function salAlloc() {
      var side = SAL_SIDES[salStep], w = sw >= sh ? side : Math.max(8, Math.round(side * sw / sh)), h = sw >= sh ? Math.max(8, Math.round(side * sh / sw)) : side;
      if (w === ws && h === hs && salT[0]) return;
      [lowT[0], lowT[1], shiftT, resT, salT[0], salT[1]].forEach(function (t) { if (t) gl.deleteTexture(t); });
      ws = w; hs = h;
      lowT = [tex2(ws, hs, gl.R8, gl.LINEAR), tex2(ws, hs, gl.R8, gl.LINEAR)];
      shiftT = tex2(7, 7, floatOK ? gl.RGBA16F : gl.RGBA8, gl.NEAREST); resT = tex2(4, 1, gl.RGBA8, gl.NEAREST);
      salT = [tex2(ws, hs, gl.RGBA8, gl.LINEAR), tex2(ws, hs, gl.RGBA8, gl.LINEAR)];
      gl.bindTexture(gl.TEXTURE_2D, salT[0]); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.MIRRORED_REPEAT); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.MIRRORED_REPEAT);
      gl.bindTexture(gl.TEXTURE_2D, salT[1]); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.MIRRORED_REPEAT); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.MIRRORED_REPEAT);
      if (pbo) gl.deleteBuffer(pbo);
      pbo = gl.createBuffer(); gl.bindBuffer(gl.PIXEL_PACK_BUFFER, pbo); gl.bufferData(gl.PIXEL_PACK_BUFFER, (ws * hs + 4) * 4, gl.STREAM_READ); gl.bindBuffer(gl.PIXEL_PACK_BUFFER, null);
      map = new Uint8Array((ws * hs + 4) * 4);
      if (sync) { gl.deleteSync(sync); sync = null; }
      salReset();
    }
    function clearTex(t) { gl.bindFramebuffer(gl.FRAMEBUFFER, fbS); gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, t, 0); gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT); }
    function salReset() { lowN = 0; salFrames = 0; if (salT[0]) { clearTex(salT[0]); clearTex(salT[1]); clearTex(resT); gl.bindFramebuffer(gl.FRAMEBUFFER, null); } mapInfo.maxE = mapInfo.maxL = mapInfo.meanE = 0; }
    function target(t, w, h) { gl.bindFramebuffer(gl.FRAMEBUFFER, fbS); gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, t, 0); gl.viewport(0, 0, w, h); }
    function bindT(unit, t, loc) { gl.activeTexture(gl.TEXTURE0 + unit); gl.bindTexture(gl.TEXTURE_2D, t); gl.uniform1i(loc, unit); }
    function salience(now, damp, prior) {
      salAlloc();
      var cur = lowN % 2, prev = 1 - cur, frameMs = lastFreshAt ? clamp(now - lastFreshAt, 8, 200) : 33;
      lastFreshAt = now;
      gl.bindVertexArray(vao);
      target(lowT[cur], ws, hs); gl.useProgram(pLow.p); bindT(0, texSrc, pLow.u.u_src); gl.uniform2f(pLow.u.u_cell, 1 / ws, 1 / hs); gl.drawArrays(gl.TRIANGLES, 0, 3);
      lowN++;
      if (lowN < 2) return;
      target(shiftT, 7, 7); gl.useProgram(pShift.p); bindT(0, lowT[cur], pShift.u.u_a); bindT(1, lowT[prev], pShift.u.u_b);
      gl.uniform2i(pShift.u.u_n, ws, hs); gl.uniform2f(pShift.u.u_prior, prior[0], prior[1]); gl.drawArrays(gl.TRIANGLES, 0, 3);
      target(resT, 4, 1); gl.useProgram(pRes.p); bindT(0, shiftT, pRes.u.u_shift); bindT(1, lowT[cur], pRes.u.u_a);
      gl.uniform2i(pRes.u.u_n, ws, hs); gl.uniform2f(pRes.u.u_prior, prior[0], prior[1]); gl.drawArrays(gl.TRIANGLES, 0, 3);
      var sIn = salT[salAt], sOut = salT[1 - salAt];
      target(sOut, ws, hs); gl.useProgram(pSal.p); bindT(0, lowT[cur], pSal.u.u_a); bindT(1, lowT[prev], pSal.u.u_b); bindT(2, resT, pSal.u.u_res); bindT(3, sIn, pSal.u.u_prev);
      var f = function (tau) { return 1 - Math.exp(-frameMs / tau); };
      gl.uniform2f(pSal.u.u_cell, 1 / ws, 1 / hs); gl.uniform4f(pSal.u.u_k, f(70), f(650), f(240), f(260)); gl.uniform1f(pSal.u.u_damp, damp); gl.uniform1f(pSal.u.u_fresh, salFrames > 1 ? 1 : 0);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      salAt = 1 - salAt; salFrames++;
      if (!sync && now - readAt >= readMs) {          // a few reads a second, into a buffer the chip fills when it gets there; nothing waits
        readAt = now;
        gl.bindBuffer(gl.PIXEL_PACK_BUFFER, pbo);
        gl.readPixels(0, 0, ws, hs, gl.RGBA, gl.UNSIGNED_BYTE, 0);
        target(resT, 4, 1); gl.readPixels(0, 0, 4, 1, gl.RGBA, gl.UNSIGNED_BYTE, ws * hs * 4);
        gl.bindBuffer(gl.PIXEL_PACK_BUFFER, null);
        sync = gl.fenceSync(gl.SYNC_GPU_COMMANDS_COMPLETE, 0); readW = ws; readH = hs;
      }
    }
    var readW = 0, readH = 0;
    function readPoll(now) {
      if (!sync) return;
      if (gl.getSyncParameter(sync, gl.SYNC_STATUS) !== gl.SIGNALED) return;
      gl.deleteSync(sync); sync = null;
      if (readW !== ws || readH !== hs) return;        // the map changed size since this read began
      gl.bindBuffer(gl.PIXEL_PACK_BUFFER, pbo); gl.getBufferSubData(gl.PIXEL_PACK_BUFFER, 0, map); gl.bindBuffer(gl.PIXEL_PACK_BUFFER, null);
      var n = ws * hs, o = n * 4, maxE = 0, maxL = 0, sum = 0;
      for (var i = 0; i < n; i++) { var e = map[i * 4], l = map[i * 4 + 1]; sum += e; if (e > maxE) maxE = e; if (l > maxL) maxL = l; }
      mapInfo.at = now; mapInfo.reads++; mapInfo.maxE = maxE / 255; mapInfo.maxL = maxL / 255; mapInfo.meanE = sum / n / 255;
      mapInfo.shift = [(map[o] / 255 - .5) * 16, (map[o + 1] / 255 - .5) * 16]; mapInfo.fit = map[o + 2] / 255; mapInfo.lum = map[o + 4] / 255;
      gaze.onMap(map, ws, hs, now);
    }

    // ---- the gaze: a zone moved to the most salient place outside the places it has just looked at
    // It jumps fast, dwells, sweeps a little while it dwells (jumping spider retinas scan), and leaves an inhibition of return at
    // each place it looked, fading over gz.ior milliseconds (about five seconds: Ferrante and colleagues 2024). When the picture is dark
    // and still for a while, it twitches in bouts (Rossler and colleagues 2022). docs/ENGINE.md gives the fields.
    var gaze = (function () {
      var G = { x: .5, y: .5, mode: 'rest', t0: 0, fx: .5, fy: .5, tx: .5, ty: .5, until: 0, jumps: 0, ior: [], cfg: null, pinned: null, rot: 0, sx: 0,
        dark: 0, sleep: false, bout: 0, boutEnd: 0, nextBout: 0, twitchAt: 0, jx: 0, jy: 0, jr: 0, lastMap: 0, aspect: 1, best: 0 };
      function cfgOf(gz) {
        return { jump: gz.jump || 80, dwell: gz.dwell || [700, 1600], follow: gz.follow || .14, scan: gz.scan || [.01, 1.2, 10], ior: gz.ior || 5000, iorR: gz.iorR || .08,
          floor: gz.floor || .07, living: gz.living === undefined ? 1.5 : gz.living, sleep: !!gz.sleep, margin: gz.margin || [.05, .06] };
      }
      function iorAt(x, y, now) {
        var k = 0, c = G.cfg;
        for (var i = 0; i < G.ior.length; i++) {
          var I = G.ior[i], age = (now - I.t) / c.ior; if (age >= 1) continue;
          var dx = (x - I.x) * G.aspect, dy = y - I.y, s = 1 - ease(clamp((age - .55) / .45, 0, 1));
          k = Math.max(k, s * Math.exp(-(dx * dx + dy * dy) / (c.iorR * c.iorR)));
        }
        return k;
      }
      function jumpTo(x, y, now) { G.mode = 'jump'; G.t0 = now; G.fx = G.x; G.fy = G.y; G.tx = x; G.ty = y; G.jumps++; }
      return {
        G: G,
        reset: function () { G.x = G.y = G.fx = G.fy = G.tx = G.ty = .5; G.mode = 'rest'; G.ior = []; G.jumps = 0; G.sleep = false; G.dark = 0; G.lastMap = 0; G.pinned = null; G.best = 0; },
        pin: function (x, y) { G.pinned = x === null ? null : [x, y]; },
        onMap: function (m, w, h, now) {
          var c = G.cfg; if (!c) return;
          G.aspect = sw / Math.max(1, sh);
          var dtm = G.lastMap ? now - G.lastMap : 0; G.lastMap = now;
          var o = w * h * 4, sx = (m[o] / 255 - .5) * 16, sy = (m[o + 1] / 255 - .5) * 16, lum = m[o + 4] / 255;
          var still = Math.abs(sx) < .35 && Math.abs(sy) < .35 && mapInfo.meanE < .02 && senses.still();
          G.dark = lum < .17 && still ? G.dark + dtm : 0;
          var wasSleep = G.sleep; G.sleep = c.sleep && G.dark > 3500;
          if (G.sleep && !wasSleep) { G.nextBout = now + 1500 + Math.random() * 3000; G.mode = 'rest'; }
          if (G.sleep || G.pinned) return;
          // the most salient place outside the places just looked at, inside the camera's own picture
          var best = 0, bx = 0, by = 0, near = 0, nx = 0, ny = 0, mx = c.margin[0], my = c.margin[1], R = .14;
          for (var y = 0; y < h; y++) {
            var v = (y + .5) / h; if (v < my || v > 1 - my) continue;
            for (var x = 0; x < w; x++) {
              var u = (x + .5) / w; if (u < mx || u > 1 - mx) continue;
              var i = (y * w + x) * 4, s = (m[i] + c.living * m[i + 1]) / 255;
              if (s <= c.floor * .5) continue;
              var dx = (u - G.x) * G.aspect, dy = v - G.y, d2 = dx * dx + dy * dy;
              if (d2 < R * R && s > near) { near = s; nx = u; ny = v; }
              s *= 1 - iorAt(u, v, now);
              if (s > best) { best = s; bx = u; by = v; }
            }
          }
          G.best = best;
          if (G.mode === 'dwell') {
            if (near > c.floor) { G.tx = nx; G.ty = ny; }                    // the target moved: the gaze follows it while it dwells
            if (now < G.until) return;
          }
          if (G.mode === 'jump') return;
          var ddx = (bx - G.x) * G.aspect, ddy = by - G.y;
          if (best > c.floor && best > mapInfo.meanE * 3 && ddx * ddx + ddy * ddy > .0025) jumpTo(bx, by, now);
          else if (G.mode === 'dwell') G.mode = 'rest';
        },
        // where the gaze zone is now: centre and turn, moved a little every frame
        at: function (gz, now, dt) {
          if (!gz) return null;
          if (!G.cfg || G.cfg.src !== gz) { G.cfg = cfgOf(gz); G.cfg.src = gz; }
          var c = G.cfg, t = now / 1000, j = calm ? 450 : c.jump;
          if (G.pinned) { G.x = G.pinned[0]; G.y = G.pinned[1]; return { x: G.x, y: G.y, rot: 0 }; }
          if (G.mode === 'jump') {
            var p = clamp((now - G.t0) / j, 0, 1), e = calm ? ease(p) : 1 - Math.pow(1 - p, 3);
            G.x = lerp(G.fx, G.tx, e); G.y = lerp(G.fy, G.ty, e);
            if (p >= 1) {
              G.mode = 'dwell'; G.until = now + c.dwell[0] + Math.random() * (c.dwell[1] - c.dwell[0]);
              G.ior.push({ x: G.tx, y: G.ty, t: now }); if (G.ior.length > 6) G.ior.shift();
            }
          } else if (G.mode === 'dwell') {
            var a = 1 - Math.exp(-(dt || 16) / (c.follow * 1000));
            G.x = lerp(G.x, G.tx, a); G.y = lerp(G.y, G.ty, a);
          } else if (!G.sleep) {
            var b = 1 - Math.exp(-(dt || 16) / 2500);                    // nothing calls: the gaze settles slowly back toward the front
            G.x = lerp(G.x, .5, b); G.y = lerp(G.y, .5, b);
          }
          var sx = 0, rot = 0;
          if (!calm && !G.sleep && G.mode !== 'jump') {                  // the small sweeps of a scanning retina
            sx = c.scan[0] * Math.sin(2 * Math.PI * c.scan[1] * t) * (G.mode === 'dwell' ? 1 : .5);
            rot = c.scan[2] * Math.sin(2 * Math.PI * c.scan[1] * .53 * t + 1.1) * Math.PI / 180;
          }
          if (G.sleep) {                                                 // in the dark and still: bouts of twitching
            if (!G.bout && now >= G.nextBout) { G.bout = 1; G.boutEnd = now + 1500 + Math.random() * 2500; G.twitchAt = 0; }
            if (G.bout) {
              if (now >= G.twitchAt) { G.twitchAt = now + 70 + Math.random() * 160; G.jx = (Math.random() - .5) * .05; G.jy = (Math.random() - .5) * .06; G.jr = (Math.random() - .5) * .5; }
              if (now >= G.boutEnd) { G.bout = 0; G.nextBout = now + 6000 + Math.random() * 9000; G.jx = G.jy = G.jr = 0; }
            }
            if (calm) { G.jx *= .2; G.jy *= .2; G.jr *= .2; }
            sx += G.jx; rot += G.jr;
          }
          return { x: G.x + sx, y: G.y + (G.sleep ? G.jy : 0), rot: rot };
        },
        iorList: function (now) {
          var c = G.cfg, out = []; if (!c) return out;
          for (var i = 0; i < G.ior.length; i++) { var I = G.ior[i], age = (now - I.t) / c.ior; if (age < 1) out.push([I.x, I.y, c.iorR, 1 - ease(clamp((age - .55) / .45, 0, 1))]); }
          return out;
        }
      };
    })();

    // ---- uniforms for the zones, reused frame after frame
    var zG = new Float32Array(16), zH = new Float32Array(16), zR = new Float32Array(16), zP = new Float32Array(16), zQ = new Float32Array(16), zS = new Float32Array(16), zM = new Float32Array(36), zT = new Float32Array(16);
    var iorU = new Float32Array(24), ripU = new Float32Array(16), zLag = [0, 0, 0, 0], lastG = null;
    function blurOf(inv, longPx) { return inv > 1 / (HUMAN_CPD - 1) ? .6 * (longPx / VIEW_DEG) * inv : 0; }   // 0.6 of one cycle at that eye's limit
    function zoneUniforms(Z, P, now, dt, longPx) {
      var nz = Math.min(4, Z.length), i, gz = null;
      for (i = 0; i < nz; i++) {
        var z = Z[i], cx = z.cx, cy = z.cy, rot = z.rot;
        if (z.gaze && P.gz) { gz = gz || gaze.at(P.gz, now, dt); if (gz) { cx = gz.x; cy = gz.y; rot += gz.rot; } lastG = gz; }
        zG[i * 4] = cx; zG[i * 4 + 1] = cy; zG[i * 4 + 2] = z.hw; zG[i * 4 + 3] = z.hh;
        zH[i * 4] = z.shape; zH[i * 4 + 1] = z.soft; zH[i * 4 + 2] = z.inner; zH[i * 4 + 3] = 0;
        zR[i * 4] = Math.cos(rot); zR[i * 4 + 1] = Math.sin(rot);
        zP[i * 4] = blurOf(z.inv, longPx); zP[i * 4 + 1] = z.sat; zP[i * 4 + 2] = z.gain; zP[i * 4 + 3] = moving ? z.gate : 0;
        zQ[i * 4] = z.glow; zQ[i * 4 + 1] = z.living; zQ[i * 4 + 2] = z.uv; zQ[i * 4 + 3] = z.mag;
        zS[i * 4] = z.sheen;
        for (var j = 0; j < 9; j++) zM[i * 9 + j] = z.M[j];
      }
      return nz;
    }

    var api = {
      floatOK: floatOK,
      setImage: function (cv) { moving = false; if (upload(cv, cv.width, cv.height)) reset = true; },
      setFrame: function (source, w, h, now) { if (!moving) { moving = true; resetTime(); } if (upload(source, w, h)) { pushRing(now); fresh = true; freshAt = now; } },
      resetTime: resetTime,
      setSide: function (n) { MAXSIDE = Math.max(240, Math.round(n)); },
      side: function () { return MAXSIDE; },
      // a slow phone gives up detail in the movement map before it gives up any of the picture (64, then 48, then 32 cells)
      lighten: function () { if (pViewZ && salFrames && salStep < SAL_SIDES.length - 1) { salStep++; return true; } return false; },
      clear: function () { hasFrame = false; },
      hasFrame: function () { return hasFrame; },
      newView: function () { gaze.reset(); salReset(); zLag = [0, 0, 0, 0]; },
      state: function () { return { sw: sw, sh: sh, writes: writes, stepMs: stepMs, moving: moving, floatOK: floatOK, err: gl.getError() }; },
      // what the last frames cost: script time inside draw() and, where offered, the graphics chip's time (both in ms, means of up to 90)
      probe: function () { return { cpu: avg(cpuMs), gpu: avg(gpuMs), timer: !!tq, n: cpuMs.length, gpuN: gpuMs.length, sal: ws ? ws + 'x' + hs : '', zones: !!pViewZ, zErr: zErr }; },
      // for the checks: the gaze, the movement map's last read, and a way to hold the gaze in one place
      gazeState: function () { var G = gaze.G; return { x: G.x, y: G.y, mode: G.mode, jumps: G.jumps, ior: G.ior.length, sleep: G.sleep, best: G.best, map: mapInfo, sal: [ws, hs], salFrames: salFrames, pending: !!sync }; },
      pinGaze: function (x, y) { gaze.pin(x === undefined ? null : x, y); },
      resize: function () {
        var dpr = Math.min(window.devicePixelRatio || 1, 2), w = canvas.clientWidth * dpr, h = canvas.clientHeight * dpr, k = Math.min(1, MAXSIDE / Math.max(w, h, 1));
        w = Math.max(2, Math.round(w * k)); h = Math.max(2, Math.round(h * k));
        if (canvas.width !== w || canvas.height !== h) { canvas.width = w; canvas.height = h; }
      },
      draw: function (P, fx, now, dt) {
        var c0 = performance.now();
        qPoll(); qBegin();
        drawFrame(P, fx, now, dt);
        qEnd(); keep(cpuMs, performance.now() - c0);
      }
    };
    return api;

    function drawFrame(P, fx, now, dt) {
        gl.bindVertexArray(vao);
        if (!hasFrame) { gl.bindFramebuffer(gl.FRAMEBUFFER, null); gl.viewport(0, 0, canvas.width, canvas.height); gl.clearColor(0, 0, 0, 1); gl.clear(gl.COLOR_BUFFER_BIT); return; }
        var Z = P.zones && P.zones.length ? P.zones : null, zoned = (Z || P.sal > .001) && zonePrograms();
        if (zoned) readPoll(now);
        var useRing = 0, back = 0, nowMix = 0, a = 1, zPace = false;
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
          if (zoned && Z) for (var zi = 0; zi < Math.min(4, Z.length); zi++) {   // a zone at its own pace keeps its own place in the ring
            var zr = Z[zi].rate, zt = zi * 4;
            zT[zt] = 0; zT[zt + 1] = 0; zT[zt + 2] = 0;
            if (zr < .999 && Math.abs(zr - P.rate) > .001) {
              var top2 = N - 3; zPace = true;
              zLag[zi] += (1 - zr) * dt / stepMs; if (zLag[zi] >= top2) zLag[zi] = 0;
              zT[zt] = clamp(zLag[zi] - (now - tHead) / stepMs, 0, N - 2); zT[zt + 1] = 1; zT[zt + 2] = zLag[zi] > top2 - 1.5 ? (zLag[zi] - (top2 - 1.5)) / 1.5 : 0;
            } else if (Math.abs(zr - P.rate) <= .001 && useRing) { zT[zt] = back; zT[zt + 1] = 1; zT[zt + 2] = nowMix; }
          }
        } else { lag = 0; holdAt = -1; }
        if (moving && P.persist > 0) { a = 1 - Math.exp(-(dt / 1000) / P.persist); if (!floatOK) a = Math.max(a, .2); }
        // the movement map, once for each new camera frame
        if (zoned && P.sal > .001 && moving && fresh) {
          var sp = senses.turning();
          salience(now, 1 - clamp((sp - 25) / 70, 0, .85), [0, 0]);
        }
        fresh = false;
        var gateAny = P.gate > .5 || (Z && Z.some(function (z) { return z.gate > .01; }));
        var tp = zoned && zPace ? pTimeZ : pTime;
        gl.bindFramebuffer(gl.FRAMEBUFFER, fbT);
        gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, tB, 0);
        gl.viewport(0, 0, sw, sh); gl.useProgram(tp.p);
        var ut = tp.u;
        gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, texSrc); gl.uniform1i(ut.u_src, 0);
        gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, tA); gl.uniform1i(ut.u_prev, 1);
        gl.activeTexture(gl.TEXTURE2); gl.bindTexture(gl.TEXTURE_2D_ARRAY, ring); gl.uniform1i(ut.u_ring, 2);
        gl.uniform2f(ut.u_px, 1 / sw, 1 / sh);
        gl.uniform1f(ut.u_n, N); gl.uniform1f(ut.u_head, head); gl.uniform1f(ut.u_lag, back); gl.uniform1f(ut.u_useRing, useRing); gl.uniform1f(ut.u_now, nowMix);
        gl.uniform1f(ut.u_a, a); gl.uniform1f(ut.u_gate, moving && writes > 2 && gateAny ? 1 : 0); gl.uniform1f(ut.u_decay, Math.exp(-dt / 420));
        gl.uniform1f(ut.u_enc, floatOK ? 0 : 1); gl.uniform1f(ut.u_reset, reset ? 1 : 0);
        var longPx = Math.max(canvas.width, canvas.height), sc = longPx / 1280, nz = 0;
        if (zoned && Z) nz = zoneUniforms(Z, P, now, dt, longPx);
        else if (zoned && P.gz) lastG = gaze.at(P.gz, now, dt);
        if (tp === pTimeZ) {
          gl.uniform1f(ut.u_srcAspect, sw / sh); gl.uniform1i(ut.u_nz, nz);
          gl.uniform4fv(ut['u_zG[0]'], zG); gl.uniform4fv(ut['u_zH[0]'], zH); gl.uniform4fv(ut['u_zR[0]'], zR); gl.uniform4fv(ut['u_zT[0]'], zT);
        }
        gl.drawArrays(gl.TRIANGLES, 0, 3);
        reset = false;
        var t = tA; tA = tB; tB = t;
        gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, tA); gl.generateMipmap(gl.TEXTURE_2D);
        gl.bindFramebuffer(gl.FRAMEBUFFER, null);
        var vp = zoned ? pViewZ : pView;
        gl.viewport(0, 0, canvas.width, canvas.height); gl.useProgram(vp.p);
        var u = vp.u;
        var blur = blurOf(P.inv, longPx);
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
        if (zoned) {
          gl.uniform1i(u.u_nz, nz);
          gl.uniform4fv(u['u_zG[0]'], zG); gl.uniform4fv(u['u_zH[0]'], zH); gl.uniform4fv(u['u_zR[0]'], zR);
          gl.uniform4fv(u['u_zP[0]'], zP); gl.uniform4fv(u['u_zQ[0]'], zQ); gl.uniform4fv(u['u_zS[0]'], zS); gl.uniformMatrix3fv(u['u_zM[0]'], true, zM);
          var salOn = moving && salT[0] && salFrames > 1 ? P.sal : 0;
          gl.uniform1f(u.u_salOn, salOn); gl.uniform2f(u.u_base, P.glow, P.living); gl.uniform3f(u.u_glowC, P.glowC[0], P.glowC[1], P.glowC[2]);
          gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, salT[salAt] || tA); gl.uniform1i(u.u_sal, 1);
          var L = P.gz ? gaze.iorList(now) : [];
          for (var ii = 0; ii < 6; ii++) { var I = L[ii]; iorU[ii * 4] = I ? I[0] : 0; iorU[ii * 4 + 1] = I ? I[1] : 0; iorU[ii * 4 + 2] = I ? I[2] : 1; iorU[ii * 4 + 3] = I ? I[3] * salOn : 0; }
          gl.uniform4fv(u['u_ior[0]'], iorU);
          var R = fx.rip || [];
          for (var ri = 0; ri < 4; ri++) { var rr = R[ri]; ripU[ri * 4] = rr ? rr[0] : 0; ripU[ri * 4 + 1] = rr ? rr[1] : 0; ripU[ri * 4 + 2] = rr ? rr[2] : 0; ripU[ri * 4 + 3] = rr ? rr[3] : 0; }
          gl.uniform4fv(u['u_rip[0]'], ripU); gl.uniform1f(u.u_ripK, (fx.ripK || 0) * P.ripple);
        }
        gl.drawArrays(gl.TRIANGLES, 0, 3);
        if (zoned) gl.activeTexture(gl.TEXTURE0);
    }
  }
