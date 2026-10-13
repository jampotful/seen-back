
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
    'uniform vec4 u_zG[4];',   // centre x, y; half width, half height, as fractions of the picture's long side
    'uniform vec4 u_zH[4];',   // shape (1 strip, 2 ellipse, 3 annulus, 4 band, 5 cross, 0 the whole field), soft edge, inner edge of an annulus
    'uniform vec4 u_zR[4];',   // cos and sin of the zone's turn
    'uniform vec4 u_zX[4];',   // a cross: the tilt of its upper and of its lower arms (radians from upright), half the gap between its two halves, weight kept at an arm's tip
    'uniform vec2 u_zScale;',  // the picture's width and height as fractions of its long side
    'uniform int u_nz;',
    'float armW(vec2 d, vec2 dir, float hw, float len, float s, float tip){',   // one arm of a cross, from its root along dir
    '  float t = dot(d, dir), n = abs(dot(d, vec2(-dir.y, dir.x)));',
    '  return (1.0 - smoothstep(-s, s, n - hw)) * (1.0 - smoothstep(-s, s, t - len)) * smoothstep(-s, s, t + hw) * mix(1.0, tip, clamp(t / len, 0.0, 1.0));',
    '}',
    'float zoneW(int i, vec2 uv){',
    '  vec4 g = u_zG[i], h = u_zH[i], r = u_zR[i];',
    '  if (h.x < 0.5) return 1.0;',
    '  vec2 d = (uv - g.xy) * u_zScale;',
    '  d = vec2(r.x * d.x + r.y * d.y, -r.y * d.x + r.x * d.y);',
    '  float s = max(h.y, 1e-4);',
    '  if (h.x < 1.5) { vec2 e = abs(d) - g.zw; return (1.0 - smoothstep(-s, s, e.x)) * (1.0 - smoothstep(-s, s, e.y)); }',
    '  if (h.x > 4.5) {',   // two narrow fields, each bent in the middle, that cross like an X without touching (a jumping spider's principal retinae at rest)
    '    vec4 x = u_zX[i]; float w = 0.0, gap = x.z + g.z;',
    '    for (int k = 0; k < 2; k++) {',
    '      float sx = k == 0 ? -1.0 : 1.0; vec2 q = d - vec2(sx * gap, 0.0);',
    '      w = max(w, armW(q, vec2(sx * sin(x.x), cos(x.x)), g.z, g.w, s, x.w));',
    '      w = max(w, armW(q, vec2(sx * sin(x.y), -cos(x.y)), g.z, g.w, s, x.w));',
    '    }',
    '    return w;',
    '  }',
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
    '#if ZONES', 'uniform vec4 u_zT[4];', ZONE_GLSL,
    'uniform sampler2D u_store; uniform vec4 u_slow;',   // module 12, slow: the store of frames kept every few seconds, how much of it is shown, and the paper of a print not yet developed
    '#endif',
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
    '  if (u_slow.x > 0.0) base = mix(base, texture(u_store, v).rgb, u_slow.x);',
    '  if (u_slow.y > 0.0) base = mix(base, vec3(0.80, 0.78, 0.73), u_slow.y);',
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
    'uniform vec4 u_zS[4];',   // sheen, the guessed ultraviolet added to red
    'uniform mat3 u_zM[4];',
    'uniform sampler2D u_sal; uniform float u_salOn; uniform vec4 u_base; uniform vec3 u_glowC;',   // the movement map; the view\'s own glow, living weight and ultraviolet in red
    'uniform vec4 u_ior[6];',  // places the side eyes are ignoring: x, y, reach, strength
    'uniform vec4 u_rip[4]; uniform float u_ripK;',   // ripples on the screen: x, y, age in seconds, strength
    'uniform float u_pan, u_shimmer, u_time, u_palm;',   // u_palm: the guessed ultraviolet felt as a fine moving grain (&draw=palm, invented)        // a sideways sweep of the whole picture (in the picture\'s width), a shimmer on the glow, the clock
    'uniform vec4 u_water; uniform vec3 u_waterC;',
    // module 2, spectrum (docs/ENGINE-DESIGN.md): the ultraviolet column of the colour matrix, view and zones; the animal's classes from
    // the four inputs (u_Q, for the colour wheel and the neutral band); the wheel's turn (below 0 when off); the neutral band's strength
    'uniform vec3 u_U; uniform vec4 u_zU[4]; uniform mat4 u_Q; uniform float u_rot4, u_neutral;',
    'uniform vec2 u_stab;',
    // module 12, slow: the picture turned back toward true vertical (u_spin, radians); module 5, tilt and heading: Snell\'s window
    // (strength, the window\'s centre in screen heights from the middle) and the magnetic options (grain, tide, the grain\'s angle)
    'uniform float u_spin; uniform vec3 u_snell, u_mag;',
    // modules 8 to 11 (docs/ENGINE.md): the field (mode 1 wedge, 2 fold, 4 ribbon; its numbers), the ribbon and the age of each of its
    // 32 sectors, the overlays (polarization, web, sound rings, shadow rings; the sky's numbers; up to eight events: x, y, age, strength
    // with a shadow below 0), sound (three bands and breath; the flash's age, mode, floor and strength) and the haptic edge pulse
    'uniform vec4 u_fld, u_fld2; uniform sampler2D u_rib; uniform vec4 u_ribT[8];',
    'uniform vec4 u_ov, u_ovP; uniform vec4 u_evt[8]; uniform vec4 u_snd, u_hear; uniform float u_pulse;',   // module 5, motion: the shift that holds the world still against the hand (the locked world, &draw=lock)
    'vec3 wheel(vec4 q, float k){ vec4 s = k < 0.5 ? q : k < 1.5 ? q.yzwx : k < 2.5 ? q.zwxy : q.wxyz; return s.zyx; }',   // light lost in water: per channel, and how far the top of the picture is taken to be (GUESSED from height); the water\'s own colour
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
    '  if (u_spin != 0.0) { float cs = cos(u_spin), sn = sin(u_spin); p = mat2(cs, sn, -sn, cs) * p; }',
    '  if (u_hear.y > 0.5 && u_hear.y < 1.5) { p.x += u_snd.w * 0.014 * sin(p.y * 38.0 + u_time * 9.0) * (0.6 + 0.4 * sin(p.x * 11.0 - u_time * 3.0)); p.y += u_snd.w * 0.006 * sin(p.x * 29.0 - u_time * 7.0); }',   // breath and moving air ruffle the picture (atlas 16, 22; invented)
    '  if (u_hear.y > 1.5 && u_hear.y < 2.5) { float sh = u_snd.x * u_snd.x * smoothstep(0.3, -0.5, p.y); p += sh * vec2(0.004 * sin(u_time * 41.0), 0.011 * sin(u_time * 57.0)); }',   // the mole\'s rumble shakes the ground first (atlas 15; invented)
    '  if (u_fld.x > 1.5 && u_fld.x < 2.5 && p.y > u_fld.z) p.y = u_fld.z + (p.y - u_fld.z) * (1.0 + u_fld.y);',   // the sky fold: what lies above the horizon pressed into the top of the screen (invented)
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
    '#if ZONES',
    '  uv.x += u_pan; uv += u_stab;',
    '  float snellDim = 1.0;',
    '  if (u_snell.x > 0.001) {',   // Snell\'s window: the sky above water squeezed into a disc about 97 degrees across (fish.md section 4, item 1)
    '    vec2 d = p - vec2(0.0, u_snell.y); float dl = length(d), rw = radians(dl / 0.42 * 48.6), sa = 1.333 * sin(min(rw, 1.5));',
    '    float inside = 1.0 - smoothstep(0.96, 1.0, sa), ta = asin(min(sa, 1.0));',
    '    float L = max(u_srcAspect, 1.0), t = tan(min(ta, 1.25)) / tan(radians(32.0));',   // the camera\'s long side taken to span 64 degrees
    '    vec2 uvS = 0.5 + (d / max(dl, 1e-5)) * t * 0.5 * vec2(L / u_srcAspect, L);',
    '    uv = mix(uv, uvS, u_snell.x * inside); snellDim = mix(1.0, 0.22, u_snell.x * (1.0 - inside));',
    '  }',
    '#endif',
    '  float outside = max(max(max(-uv.x, uv.x - 1.0), max(-uv.y, uv.y - 1.0)), 0.0);',
    '  float topo = u_wA * (r / 0.5) + u_wS * (abs(p.y) / 0.5);',
    '  float ra = u_blur * (1.0 + u_fall * topo * topo) + u_soft;',
    '  float gain = u_gain, sat = u_sat, gateMix = u_gateMix, uvB = u_uvBlue, sheen = u_sheen, zmag = 1.0; mat3 M = u_M;',
    '#if ZONES',   // the zones, layered over the view in order, each blended in by its soft-edged weight at this place
    '  vec2 uv0 = uv; vec2 gl0 = u_base.xy; float uvR = u_base.z; vec3 U = u_U;',
    '  for (int i = 0; i < 4; i++) {',
    '    if (i >= u_nz) break;',
    '    float w = zoneW(i, uv0);',
    '    if (w > 0.0005) {',
    '      vec4 zp = u_zP[i], zq = u_zQ[i];',
    '      ra = mix(ra, zp.x + u_soft, w); sat = mix(sat, zp.y, w); gain = mix(gain, zp.z, w); gateMix = mix(gateMix, zp.w, w);',
    '      gl0 = mix(gl0, zq.xy, w); uvB = mix(uvB, zq.z, w); sheen = mix(sheen, u_zS[i].x, w); uvR = mix(uvR, u_zS[i].y, w);',
    '      M = M + (u_zM[i] - M) * w; U = mix(U, u_zU[i].xyz, w);',
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
    '#if ZONES',
    '  acc *= snellDim;',
    '#endif',
    '  vec3 c = acc * gain / (1.0 + (gain - 1.0) * acc);',
    '  float mn = min(c.r, min(c.g, c.b));',
    '  float uvg = clamp(1.6 * (c.b - 0.5 * (c.r + c.g)) + 2.5 * max(mn - 0.6, 0.0), 0.0, 1.0);',   // INVENTED ultraviolet
    '  vec3 m = M * c;',
    '  m.b = mix(m.b, uvg, uvB);',
    '#if ZONES',
    '  m += U * uvg;',
    '  if (u_rot4 >= 0.0) { vec4 qv = u_Q * vec4(c, uvg); float k0 = floor(u_rot4); m = mix(wheel(qv, mod(k0, 4.0)), wheel(qv, mod(k0 + 1.0, 4.0)), u_rot4 - k0); }',
    '  if (u_neutral > 0.0) {',   // the neutral band: where the animal sees no colour and a person does, a faint shimmer like heat haze (invented)
    '    float chA = (max(m.r, max(m.g, m.b)) - min(m.r, min(m.g, m.b))) / (max(m.r, max(m.g, m.b)) + 0.02);',
    '    float chH = (max(c.r, max(c.g, c.b)) - mn) / (max(c.r, max(c.g, c.b)) + 0.02);',
    '    float nb = (1.0 - smoothstep(0.03, 0.12, chA)) * smoothstep(0.08, 0.3, chH);',
    '    float gn = fract(sin(dot(floor(gl_FragCoord.xy * 0.33) + floor(u_time * 18.0) * vec2(3.1, 7.7), vec2(12.9898, 78.233))) * 43758.5453);',
    '    m += (gn - 0.5) * 0.3 * nb * u_neutral + 0.05 * nb * u_neutral * sin(u_time * 9.0 + gl_FragCoord.y * 0.08);',
    '  }',
    '  m.r += uvR * uvg;',
    '  if (u_palm > 0.0) { float gr = fract(sin(dot(floor(gl_FragCoord.xy * 0.5) + floor(u_time * 24.0) * vec2(7.13, 3.71), vec2(12.9898, 78.233))) * 43758.5453); m += (gr - 0.5) * 0.7 * uvg * uvB * u_palm; }',
    '#endif',
    '  m = mix(m, vec3(0.62, 0.12, 1.0), 0.45 * uvg * sheen);',
    '  m.g *= 1.0 - 0.9 * u_noGreen;',
    '  m = mix(vec3(dot(m, vec3(0.2126, 0.7152, 0.0722))), m, sat);',
    '#if ZONES',
    '  if (u_mag.x > 0.0) {',   // the grain of the world: fine streaks that run along magnetic north (atlas 21, invented)
    '    vec2 dg = vec2(cos(u_mag.z), sin(u_mag.z)); float al = dot(gl_FragCoord.xy, dg), ac = floor(dot(gl_FragCoord.xy, vec2(-dg.y, dg.x)) * 0.5);',
    '    float nz = fract(sin(ac * 12.9898) * 43758.5453), gr = 0.5 + 0.5 * sin(al * 0.015 + nz * 6.283);',
    '    m *= 1.0 - u_mag.x * 0.3 * nz * gr; m += u_mag.x * 0.08 * (1.0 - nz) * gr;',
    '  }',
    '  if (u_mag.y > 0.0) m *= 1.0 - u_mag.y * smoothstep(0.5, 1.0, v.y);',   // the tide of shade across the sky
    '  if (u_water.w > 0.0) { vec3 tr = exp(-u_water.rgb * u_water.w * clamp(v.y, 0.0, 1.0)); m = m * tr + u_waterC * (1.0 - tr); }',   // movement glows, where the view asks for it, except at the places the side eyes are ignoring
    '  if (u_salOn > 0.001) {',
    '    vec2 st = 0.6 / vec2(textureSize(u_sal, 0));',   // four samples a little apart, so the coarse map glows as soft light
    '    vec4 sl = 0.25 * (texture(u_sal, uv0 + st) + texture(u_sal, uv0 - st) + texture(u_sal, uv0 + vec2(st.x, -st.y)) + texture(u_sal, uv0 + vec2(-st.x, st.y)));',
    '    float g = gl0.x * (1.0 - exp(-1.8 * (sl.r + gl0.y * sl.g))) * u_salOn, ig = 0.0;',
    '    for (int j = 0; j < 6; j++) { vec4 I = u_ior[j]; if (I.w > 0.0) { vec2 dd = (uv0 - I.xy) * u_zScale; ig = max(ig, I.w * exp(-dot(dd, dd) / (I.z * I.z))); } }',
    '    if (u_shimmer > 0.0) g *= 1.0 - u_shimmer * (0.5 + 0.5 * sin(u_time * 13.0 + 40.0 * (uv0.x * 1.3 + uv0.y)));',   // a flicker that runs over the glow
    '    m += u_glowC * (g * (1.0 - ig) * edge * u_expo);',
    '  }',
    '#endif',
    '  m *= mix(1.0, 0.035 + 1.7 * trail, gateMix);',
    '  m *= 1.0 - 0.35 * u_mosaic * smoothstep(0.35, 0.5, facet);',
    '#if ZONES',
    '  if (u_hear.y > 2.5 && u_hear.y < 4.5) {',   // owl hearing and clap and see: the picture stays near dark until a sound lights it (invented)
    '    float lit = u_hear.y < 3.5 ? u_hear.w * (1.0 - smoothstep(u_hear.x * 1.4, u_hear.x * 1.4 + 0.3, length(p))) : u_hear.w;',
    '    m *= mix(u_hear.z, 1.0, clamp(lit, 0.0, 1.0));',
    '  }',
    '  if (u_fld.x > 0.5 && u_fld.x < 1.5) {',   // the blind wedge: the part of the animal\'s circle it cannot see, fixed in the world as the phone turns
    '    float dd = abs(mod(u_fld.y + p.x * u_fld2.y - u_fld.z + 540.0, 360.0) - 180.0), bl = 1.0 - smoothstep(u_fld.w, u_fld.w + u_fld2.x, dd);',
    '    m = mix(m, m * 0.05 + vec3(0.015), bl);',
    '  }',
    '  if (u_ov.x > 0.0) {',   // polarization: sky light is most polarized 90 degrees from the sun (Rayleigh), drawn as fine strokes along the e-vector
    '    float az = u_ovP.x + p.x * u_ovP.w, el = u_ovP.y + p.y * u_ovP.w, hs = u_ovP.z;',
    '    float cd = sin(el) * sin(hs) + cos(el) * cos(hs) * cos(az), dop = (1.0 - cd * cd) / (1.0 + cd * cd) * smoothstep(-0.05, 0.12, el);',
    '    vec2 sp = vec2(-u_ovP.x, hs - u_ovP.y) / u_ovP.w - p; vec2 nd = sp / (length(sp) + 1e-5);',
    '    float stp = 0.5 + 0.5 * sin(dot(gl_FragCoord.xy, nd) * 0.9);',
    '    m = mix(m, m * (0.5 + 0.5 * stp) + vec3(0.02, 0.04, 0.09) * stp, dop * u_ov.x);',
    '  }',
    '  float pluck = 0.0;',
    '  for (int i = 0; i < 8; i++) {',   // sound circles (strength above 0) and shadow rings (below 0) running out from where each event began
    '    vec4 E = u_evt[i]; if (E.w == 0.0) continue;',
    '    float x = length(p - E.xy) - E.z * 0.45, ring = exp(-x * x / 0.0005 - E.z * 1.3);',
    '    if (E.w > 0.0) m += vec3(0.85, 0.9, 1.0) * ring * E.w * u_ov.z; else m *= 1.0 - ring * min(-E.w, 1.0) * u_ov.w;',
    '    pluck = max(pluck, abs(E.w) * exp(-E.z * 2.5));',
    '  }',
    '  if (u_ov.y > 0.0) {',   // the web: spokes and a spiral drawn on the picture; knocks and sounds displace and brighten it (atlas 15, invented)
    '    float a = atan(p.y, p.x), rr = length(p), spk = abs(fract(a / 6.2831853 * 14.0 + 0.5) - 0.5) * rr * 0.4488;',
    '    float rg = abs(fract(rr / 0.045 - a / 6.2831853) - 0.5) * 0.045;',
    '    float wb = max(1.0 - smoothstep(0.0, 0.0028, spk), (1.0 - smoothstep(0.0, 0.0022, rg)) * step(0.06, rr)) * (1.0 - smoothstep(0.55, 0.7, rr));',
    '    m = mix(m, vec3(0.93), wb * u_ov.y * (0.3 + 0.7 * pluck));',
    '  }',
    '  if (u_pulse > 0.0) { vec2 ev = min(v, 1.0 - v); m += vec3(0.9) * (1.0 - smoothstep(0.0, 0.05, min(ev.x, ev.y))) * u_pulse; }',   // the haptic pulse drawn at the frame\'s edge
    '  if (u_fld.x > 3.5 && v.y < u_fld.y) {',   // the panorama ribbon: every direction the phone has faced, fading with age, centred on where it faces now
    '    float ux = fract(u_fld.z + v.x - 0.5), sec = floor(ux * 32.0); vec4 T4 = u_ribT[int(sec / 4.0)]; float j = mod(sec, 4.0);',
    '    float age = j < 0.5 ? T4.x : j < 1.5 ? T4.y : j < 2.5 ? T4.z : T4.w;',
    '    vec3 rb = pow(texture(u_rib, vec2(ux, v.y / u_fld.y)).rgb, vec3(2.2)) * exp(-age / u_fld.w) * step(age, 1e5);',
    '    float mk = 1.0 - smoothstep(0.0, 0.004, abs(abs(v.x - 0.5) - u_fld2.z * 0.5));',
    '    m = mix(rb, vec3(1.0), mk * 0.6);',
    '  }',
    '#endif',
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
  // 4. the movement map, two outputs: (energy, living, slow energy, pulse) and (the patch's recent direction of movement, reversals).
  // Energy is the change from the last frame once the phone's own shift is taken out, above the noise and above what a slightly wrong
  // shift leaves at an edge. Living is the app's own cue for the movement of living things (INVENTED): movement that holds one direction
  // across the 3 by 3 patch at each moment (coherence of normal flow) and swings back and forth over time (reversals of that direction,
  // with some weight on energy that pulses), as walking legs and beating wings do, where a rolling ball keeps one direction.
  var FS_SAL = ['#version 300 es', 'precision highp float; in vec2 v;', 'layout(location = 0) out vec4 o; layout(location = 1) out vec4 o2;',
    'uniform sampler2D u_a, u_b, u_res, u_prev, u_flow; uniform vec2 u_cell; uniform vec4 u_k; uniform float u_damp, u_fresh;',
    'float L(sampler2D t, vec2 q){ return texture(t, q).r; }',
    'void main(){',
    '  vec4 rs = texelFetch(u_res, ivec2(0, 0), 0);',
    '  vec2 sc = (rs.xy - 0.5) * 16.0, s = sc * u_cell; float sl = length(sc);',
    '  vec2 F = vec2(0.0); float Fm = 0.0, Fw = 0.0, dc = 0.0;',
    '  for (int j = -1; j <= 1; j++) for (int i = -1; i <= 1; i++) {',
    '    vec2 q = v + vec2(float(i), float(j)) * u_cell, qb = q + s;',
    '    float a = L(u_a, q), b = L(u_b, qb);',
    '    float gx = 0.5 * (L(u_a, q + vec2(u_cell.x, 0.0)) - L(u_a, q - vec2(u_cell.x, 0.0)));',
    '    float gy = 0.5 * (L(u_a, q + vec2(0.0, u_cell.y)) - L(u_a, q - vec2(0.0, u_cell.y)));',
    '    float it = a - b, g2 = gx * gx + gy * gy;',
    '    float d = max(abs(it) - 0.02 - (0.45 + 0.2 * sl) * sqrt(g2), 0.0);',
    '    if (qb.x < 0.0 || qb.y < 0.0 || qb.x > 1.0 || qb.y > 1.0) d = 0.0;',
    '    vec2 fl = -it * vec2(gx, gy) / (g2 + 0.0004);',
    '    F += fl * d; Fm += length(fl) * d; Fw += d;',
    '    if (i == 0 && j == 0) dc = d;',
    '  }',
    '  float coh = Fm > 1e-5 ? length(F) / Fm : 0.0;',
    '  vec4 P = texture(u_prev, v), Q = texture(u_flow, v);',
    '  float e = clamp(dc * 6.0, 0.0, 1.0) * u_damp * (1.0 - smoothstep(2.2, 4.0, sl)) * u_fresh;',   // a phone turned fast: its movement is not trusted to be gone
    '  float E = mix(P.r, e, u_k.x), Es = mix(P.b, e, u_k.y), Rh = mix(P.a, abs(e - P.r), u_k.z);',
    '  vec2 fn = Fw > 1e-5 ? F / Fw : vec2(0.0), pv = Q.xy * 2.0 - 1.0;',
    '  float mn = length(fn), mp = length(pv), rev = 0.0;',
    '  if (mn > 0.04 && mp > 0.2 && e > 0.03) rev = max(0.0, -dot(fn / mn, pv / mp));',   // this moment\'s direction against the recent one
    '  float Rv = mix(Q.z, rev, u_k.z);',
    '  vec2 nv = mn > 0.04 && e > 0.03 ? mix(pv, fn / mn, 0.5) : pv * 0.92;',
    '  float pulse = clamp(Rh * 3.0 / (Es + 0.08), 0.0, 1.0);',
    '  float liv = coh * clamp(2.6 * Rv + 0.35 * pulse, 0.0, 1.0) * clamp(E * 3.0, 0.0, 1.0);',
    '  float Lv = mix(P.g, liv, u_k.w);',
    '  o = vec4(max(E - 0.004, 0.0), max(Lv - 0.004, 0.0), Es, Rh);',   // at least one step of decay, so that nothing sticks in eight bits
    '  o2 = vec4(clamp(nv * 0.5 + 0.5, 0.0, 1.0), max(Rv - 0.004, 0.0), 1.0);',
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
    var FS_SLOWP = '#version 300 es\nprecision highp float; in vec2 v; out vec4 o; uniform sampler2D u_src, u_prev; uniform float u_w; void main(){ o = vec4(mix(texture(u_prev, v).rgb, texture(u_src, v).rgb, u_w), 1.0); }';
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

    // ---- module 12, slow (docs/ENGINE.md): a store at half the picture's width and height (a quarter of its pixels) that takes one frame
    // every few seconds and keeps their running mean, then a mean that forgets over the view's window. It accumulates in a 16-bit float
    // target where the phone renders to one, so it holds many more frames than the time pass's averaging, which floors at 0.2 without
    // float textures (fungus.md section 4). The time pass then takes its picture from the store.
    var pSlow = null, slowT = [null, null], slowW = 0, slowH = 0, slowN = 0, slowAt = -1e12, slowFb = null, slowMode = '', spinS = 0, spinAt = 0;
    var lastSn = 0, watchAt = 0, develop = 0, lastCells = null, lastCellRead = 0, picMove = 0;
    window.addEventListener('pointerdown', function () { watchAt = performance.now(); }, { passive: true });
    // modules 8 to 11: the field's starting heading, the ribbon (1024 by 128, 32 sectors with the time each was last written), the
    // overlays' events, the sound flash and the haptic pulse
    var fldRef = null, ribTex = null, ribFb = null, ribAt = 0, ribTimes = new Float64Array(32), ribT = new Float32Array(32), evts = [], evtU = new Float32Array(32);
    var seenOnset = 0, seenKnock = 0, seenShock = 0, pulse = 0, hapAt = 0, lastFld = null;
    function fieldReset() { fldRef = null; for (var i = 0; i < 32; i++) ribTimes[i] = -1e12; evts = []; pulse = 0; }
    function slowReset() { slowN = 0; slowAt = -1e12; develop = 0; watchAt = performance.now(); }
    function picChange() {                         // how much the picture changed between the light module's reads (0 still, 1 a lot)
      var C = LIGHT.cells; if (!C || LIGHT.reads === lastCellRead) return picMove;
      lastCellRead = LIGHT.reads; var d = C.data, n = C.w * C.h, s = 0, i;
      if (lastCells && lastCells.length === d.length) { for (i = 0; i < n; i++) s += Math.abs((d[i * 4] + d[i * 4 + 1] + d[i * 4 + 2]) - (lastCells[i * 4] + lastCells[i * 4 + 1] + lastCells[i * 4 + 2])); s /= n * 3 * (d instanceof Uint8Array ? 255 : 1); }
      lastCells = d.slice(0); picMove = lerp(picMove, s, .5); return picMove;
    }
    function slowTick(P, now) {                    // returns [how much of the store is shown, how much paper covers it]
      var S = P.slow, mode = P.slowMode;
      if (mode !== slowMode) { slowMode = mode; slowReset(); }
      if (mode === 'righting') {                   // the slow righting (atlas 24): the picture turns back to true vertical
        var pose = senses.pose(), dts = spinAt ? Math.min((now - spinAt) / 1000, .25) : 0; spinAt = now;
        spinS += (pose.roll - spinS) * (1 - Math.exp(-dts / Math.max(.1, S.rightS || 20)));
        return null;
      }
      if (!pSlow) pSlow = prog(FS_SLOWP);
      var w = Math.max(2, sw >> 1), h = Math.max(2, sh >> 1);
      if (w !== slowW || h !== slowH || !slowT[0]) {
        slowT.forEach(function (t) { if (t) gl.deleteTexture(t); }); slowW = w; slowH = h; slowN = 0;
        slowT = [0, 1].map(function () { var t = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, t); gl.texStorage2D(gl.TEXTURE_2D, 1, floatOK ? gl.RGBA16F : gl.RGBA8, w, h);
          gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
          gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE); return t; });
        if (!slowFb) slowFb = gl.createFramebuffer();
      }
      var every = mode === 'exposure' ? 0 : Math.max(50, S.everyMs || 3000), win = Math.max(.5, S.windowS || 600), still = true, show = 1, paper = 0;
      if (mode === 'patient') {                    // the patient view (atlas 24): nothing develops while the person watches
        var mv = picChange();
        if (senses.turning() > 6 || mv > (S.moveK || .03)) watchAt = now;
        var quiet = (now - watchAt) / 1000 - (S.stillS || 8);
        still = quiet > 0;
        if (still) develop = Math.max(develop, clamp(quiet / Math.max(1, S.developS || 30), 0, 1));
        paper = slowN ? 1 - develop : 1;
      }
      if (mode === 'exposure') show = clamp(S.mix === undefined ? 1 : S.mix, 0, 1);   // the long exposure (atlas 7): shown as the light falls
      if (still && fresh && now - slowAt >= every) {
        slowAt = now; slowN++;
        var wt = Math.max(1 / slowN, 1 - Math.exp(-(every || stepMs) / 1000 / win)); if (!floatOK) wt = Math.max(wt, 1 / 64);
        gl.bindFramebuffer(gl.FRAMEBUFFER, slowFb); gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, slowT[1], 0);
        gl.viewport(0, 0, slowW, slowH); gl.useProgram(pSlow.p);
        gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, texSrc); gl.uniform1i(pSlow.u.u_src, 0);
        gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, slowT[0]); gl.uniform1i(pSlow.u.u_prev, 1);
        gl.uniform1f(pSlow.u.u_w, wt); gl.drawArrays(gl.TRIANGLES, 0, 3);
        var t = slowT[0]; slowT[0] = slowT[1]; slowT[1] = t;
      }
      return slowN ? [show, paper] : [0, paper];
    }

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
    var lag = 0, holdT0 = 0, holdAt = -1, hasFrame = false, moving = false, fresh = false, freshMedia = -1;
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
    // module 4, pace: the replayed second (&draw=replay). A tap keeps the ring of past frames (N layers, about three quarters of a
    // second) and plays it back stretched by the view's ratio, then returns to live. The ring is not written while it plays.
    // Module 5's arm as the neck (&draw=arm) uses the same ring: it is written only for a moment after each thrust of the phone, and the
    // picture shows its newest layer, so the world moves only when the person jerks the phone forward.
    var replayT0 = -1, replayK = 3, kickAt = -1e12;
    function pushRing(now) {
      if (replayT0 >= 0 || (lastP && lastP.arm && writes > N && now - kickAt > lastP.thrust)) return;
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
    var SAL_SIDES = [64, 48, 32], salStep = 0, ws = 0, hs = 0, lowT = [null, null], lowN = 0, shiftT = null, resT = null, salT = [null, null], flowT = [null, null], salAt = 0;
    var fbS = gl.createFramebuffer(), fbM = gl.createFramebuffer(), pbo = null, map = null, sync = null, readAt = 0, readMs = 160, salFrames = 0, lastFreshAt = 0, lastMedia = -1;
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
      [lowT[0], lowT[1], shiftT, resT, salT[0], salT[1], flowT[0], flowT[1]].forEach(function (t) { if (t) gl.deleteTexture(t); });
      ws = w; hs = h;
      lowT = [tex2(ws, hs, gl.R8, gl.LINEAR), tex2(ws, hs, gl.R8, gl.LINEAR)];
      shiftT = tex2(7, 7, floatOK ? gl.RGBA16F : gl.RGBA8, gl.NEAREST); resT = tex2(4, 1, gl.RGBA8, gl.NEAREST);
      salT = [tex2(ws, hs, gl.RGBA8, gl.LINEAR), tex2(ws, hs, gl.RGBA8, gl.LINEAR)];
      flowT = [tex2(ws, hs, gl.RGBA8, gl.NEAREST), tex2(ws, hs, gl.RGBA8, gl.NEAREST)];
      gl.bindTexture(gl.TEXTURE_2D, salT[0]); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.MIRRORED_REPEAT); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.MIRRORED_REPEAT);
      gl.bindTexture(gl.TEXTURE_2D, salT[1]); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.MIRRORED_REPEAT); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.MIRRORED_REPEAT);
      if (pbo) gl.deleteBuffer(pbo);
      pbo = gl.createBuffer(); gl.bindBuffer(gl.PIXEL_PACK_BUFFER, pbo); gl.bufferData(gl.PIXEL_PACK_BUFFER, (ws * hs + 4) * 4, gl.STREAM_READ); gl.bindBuffer(gl.PIXEL_PACK_BUFFER, null);
      map = new Uint8Array((ws * hs + 4) * 4);
      if (sync) { gl.deleteSync(sync); sync = null; }
      salReset();
    }
    function clearTex(t, c) { gl.bindFramebuffer(gl.FRAMEBUFFER, fbS); gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, t, 0); gl.clearColor(c || 0, c || 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT); }
    function salReset() {
      lowN = 0; salFrames = 0; lastMedia = -1;
      if (salT[0]) { clearTex(salT[0]); clearTex(salT[1]); clearTex(flowT[0], .5); clearTex(flowT[1], .5); clearTex(resT); gl.bindFramebuffer(gl.FRAMEBUFFER, null); }
      mapInfo.maxE = mapInfo.maxL = mapInfo.meanE = 0;
    }
    function target(t, w, h) { gl.bindFramebuffer(gl.FRAMEBUFFER, fbS); gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, t, 0); gl.viewport(0, 0, w, h); }
    function bindT(unit, t, loc) { gl.activeTexture(gl.TEXTURE0 + unit); gl.bindTexture(gl.TEXTURE_2D, t); gl.uniform1i(loc, unit); }
    function salience(now, damp, prior, media) {
      salAlloc();
      // the time between the two frames compared: the clip's own clock where there is one (a clip played slowly is still a clip), else the page's
      var cur = lowN % 2, prev = 1 - cur, frameMs = media >= 0 && lastMedia >= 0 && media > lastMedia ? media - lastMedia : lastFreshAt ? now - lastFreshAt : 33;
      frameMs = clamp(frameMs, 8, 200); lastFreshAt = now; lastMedia = media;
      gl.bindVertexArray(vao);
      target(lowT[cur], ws, hs); gl.useProgram(pLow.p); bindT(0, texSrc, pLow.u.u_src); gl.uniform2f(pLow.u.u_cell, 1 / ws, 1 / hs); gl.drawArrays(gl.TRIANGLES, 0, 3);
      lowN++;
      if (lowN < 2) return;
      target(shiftT, 7, 7); gl.useProgram(pShift.p); bindT(0, lowT[cur], pShift.u.u_a); bindT(1, lowT[prev], pShift.u.u_b);
      gl.uniform2i(pShift.u.u_n, ws, hs); gl.uniform2f(pShift.u.u_prior, prior[0], prior[1]); gl.drawArrays(gl.TRIANGLES, 0, 3);
      target(resT, 4, 1); gl.useProgram(pRes.p); bindT(0, shiftT, pRes.u.u_shift); bindT(1, lowT[cur], pRes.u.u_a);
      gl.uniform2i(pRes.u.u_n, ws, hs); gl.uniform2f(pRes.u.u_prior, prior[0], prior[1]); gl.drawArrays(gl.TRIANGLES, 0, 3);
      var sIn = salT[salAt], sOut = salT[1 - salAt];
      gl.bindFramebuffer(gl.FRAMEBUFFER, fbM);
      gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, sOut, 0); gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT1, gl.TEXTURE_2D, flowT[1 - salAt], 0);
      gl.drawBuffers([gl.COLOR_ATTACHMENT0, gl.COLOR_ATTACHMENT1]); gl.viewport(0, 0, ws, hs);
      gl.useProgram(pSal.p); bindT(0, lowT[cur], pSal.u.u_a); bindT(1, lowT[prev], pSal.u.u_b); bindT(2, resT, pSal.u.u_res); bindT(3, sIn, pSal.u.u_prev); bindT(4, flowT[salAt], pSal.u.u_flow);
      var f = function (tau) { return 1 - Math.exp(-frameMs / tau); };
      gl.uniform2f(pSal.u.u_cell, 1 / ws, 1 / hs); gl.uniform4f(pSal.u.u_k, f(70), f(650), f(240), f(260)); gl.uniform1f(pSal.u.u_damp, damp); gl.uniform1f(pSal.u.u_fresh, salFrames > 1 ? 1 : 0);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      salAt = 1 - salAt; salFrames++;
      if (!sync && now - readAt >= readMs) {          // a few reads a second, into a buffer the chip fills when it gets there; nothing waits
        readAt = now;
        gl.bindBuffer(gl.PIXEL_PACK_BUFFER, pbo);
        gl.readBuffer(gl.COLOR_ATTACHMENT0);
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

    // ---- the gaze: a zone moved by the movement map, as a jumping spider's principal eyes are moved by what its side eyes report
    // Every figure comes from the view's `gaze` block, and docs/ENGINE.md names the measurement behind each. In outline (Land 1969 and
    // 1971, Ferrante and colleagues 2024, Zurek and colleagues 2010, Bruce and colleagues 2021, Rossler and colleagues 2022): only movement
    // starts a jump; movement that goes on at one place loses its pull, and a small mover counts for more than movement over a wide field;
    // a jump is fast and direct; on arrival the eyes sweep side to side across the target and twist slowly back and forth, and follow it
    // if it moves; the place just looked at is left alone and its pull comes back steadily over about five seconds; with nothing there the
    // eyes hold, then drift back; with nothing moving at all they sweep on their own now and then; in the dark and still, they twitch in bouts.
    function makeGaze() {
      var G = { x: .5, y: .5, mode: 'rest', t0: 0, dur: 1, fx: .5, fy: .5, tx: .5, ty: .5, until: 0, jumps: 0, ior: [], log: [], cfg: null, pinned: null,
        dark: 0, sleep: false, bout: 0, boutEnd: 0, nextBout: 0, twitchAt: 0, jx: 0, jy: 0, jr: 0, lastMap: 0, ax: 1, ay: 1, best: 0, held: 0,
        wander: 0, wanderEnd: 0, nextWander: 0, wa: 0, wf: .3, lookT0: 0, pri: null, tl: 0 };
      function deg(d) { return d / CAM_DEG; }
      function cfgOf(gz) {
        function or(v, d) { return v === undefined ? d : v; }
        return { saccade: or(gz.saccade, [40, 4]), sweep: or(gz.sweep, [2, 1.2]), twist: or(gz.twist, [25, 2000, 3500]), examine: or(gz.examine, [4000, 12000]),
          hold: or(gz.hold, 1500), back: or(gz.back, .8), pursuit: or(gz.pursuit, 10), ior: or(gz.ior, 5000), iorR: deg(or(gz.iorDeg, 6)), habit: or(gz.habit, .75),
          surround: or(gz.surround, .6), any: or(gz.any, .6), living: or(gz.living, 1.8), distract: or(gz.distract, 1.5), wander: or(gz.wander, [8000, 20000]),
          floor: or(gz.floor, .06), sleep: gz.sleep || null, margin: or(gz.margin, [.05, .06]), track: deg(or(gz.trackDeg, 9)), region: or(gz.region, [0, 1]) };
      }
      function iorK(age, c) { return age < 0 || age >= c.ior ? 0 : age < 200 ? age / 200 : 1 - (age - 200) / (c.ior - 200); }   // poor at once, recovering steadily (Ferrante 2024)
      function iorAt(x, y, now) {
        var k = 0, c = G.cfg;
        for (var i = 0; i < G.ior.length; i++) {
          var I = G.ior[i], s = iorK(now - I.t, c); if (s <= 0) continue;
          var dx = (x - I.x) * G.ax, dy = (y - I.y) * G.ay;
          k = Math.max(k, s * Math.exp(-(dx * dx + dy * dy) / (c.iorR * c.iorR)));
        }
        return k;
      }
      function saccade(x, y, now) {
        var c = G.cfg, d = Math.sqrt(Math.pow((x - G.x) * G.ax, 2) + Math.pow((y - G.y) * G.ay, 2)) * CAM_DEG;
        G.mode = 'saccade'; G.t0 = now; G.dur = calm ? 450 : c.saccade[0] + c.saccade[1] * d; G.fx = G.x; G.fy = G.y; G.tx = x; G.ty = y; G.jumps++;
      }
      // what calls the gaze, cell by cell: movement that is new at its place, and living movement, above the movement around it
      function priority(m, w, h) {
        var c = G.cfg, n = w * h, P = G.pri && G.pri.length === n ? G.pri : (G.pri = new Float32Array(n)), I = G.integ && G.integ.length === (w + 1) * (h + 1) ? G.integ : (G.integ = new Float32Array((w + 1) * (h + 1)));
        for (var i = 0; i < n; i++) { var e = m[i * 4] / 255, l = m[i * 4 + 1] / 255, es = m[i * 4 + 2] / 255; P[i] = c.any * Math.max(e - c.habit * es, 0) + c.living * l; }
        for (var y = 0; y < h; y++) { var row = 0; for (var x = 0; x < w; x++) { row += P[y * w + x]; I[(y + 1) * (w + 1) + x + 1] = I[y * (w + 1) + x + 1] + row; } }
        var r = 3, out = G.pri2 && G.pri2.length === n ? G.pri2 : (G.pri2 = new Float32Array(n));
        for (y = 0; y < h; y++) for (x = 0; x < w; x++) {
          var x0 = Math.max(0, x - r), x1 = Math.min(w, x + r + 1), y0 = Math.max(0, y - r), y1 = Math.min(h, y + r + 1);
          var box = (I[y1 * (w + 1) + x1] - I[y0 * (w + 1) + x1] - I[y1 * (w + 1) + x0] + I[y0 * (w + 1) + x0]) / ((x1 - x0) * (y1 - y0));
          out[y * w + x] = Math.max(P[y * w + x] - c.surround * box, 0);
        }
        return out;
      }
      return {
        G: G,
        reset: function () { var rx = G.cfg ? (G.cfg.region[0] + G.cfg.region[1]) / 2 : .5; G.x = G.fx = G.tx = rx; G.y = G.fy = G.ty = .5; G.mode = 'rest'; G.ior = []; G.log = []; G.jumps = 0; G.sleep = false; G.dark = 0; G.lastMap = 0; G.pinned = null; G.best = 0; G.wander = 0; G.nextWander = 0; G.bout = 0; },
        pin: function (x, y) { G.pinned = x === null ? null : [x, y]; },
        onMap: function (m, w, h, now) {
          var c = G.cfg; if (!c) return;
          G.ax = sw / Math.max(sw, sh, 1); G.ay = sh / Math.max(sw, sh, 1);
          var dtm = G.lastMap ? Math.min(now - G.lastMap, 1000) : 0; G.lastMap = now;
          var o = w * h * 4, sx = (m[o] / 255 - .5) * 16, sy = (m[o + 1] / 255 - .5) * 16, lum = m[o + 4] / 255;
          var still = Math.abs(sx) < .35 && Math.abs(sy) < .35 && mapInfo.meanE < .02 && senses.still();
          G.dark = lum < .17 && still ? G.dark + dtm : 0;
          var wasSleep = G.sleep; G.sleep = !!c.sleep && G.dark > (c.sleep.after || 3500);
          if (G.sleep && !wasSleep) { G.nextBout = now + 1500 + Math.random() * 2500; G.mode = 'rest'; G.bout = 0; }
          if (G.sleep || G.pinned) return;
          var P = priority(m, w, h), best = 0, bx = .5, by = .5, near = 0, nx = G.tx, ny = G.ty, sum = 0, cnt = 0, mx = c.margin[0], my = c.margin[1];
          for (var y = 0; y < h; y++) {
            var v = (y + .5) / h; if (v < my || v > 1 - my) continue;
            for (var x = 0; x < w; x++) {
              var u = (x + .5) / w; if (u < Math.max(mx, c.region[0]) || u > Math.min(1 - mx, c.region[1])) continue;
              var s = P[y * w + x]; sum += s; cnt++;
              if (s <= c.floor * .5) continue;
              var dx = (u - G.tx) * G.ax, dy = (v - G.ty) * G.ay;
              if (dx * dx + dy * dy < c.track * c.track) { if (s > near) { near = s; nx = u; ny = v; } continue; }   // the target itself, wherever it has moved
              s *= 1 - iorAt(u, v, now);
              if (s > best) { best = s; bx = u; by = v; }
            }
          }
          var mean = cnt ? sum / cnt : 0, calls = best > c.floor && best > mean * 4;
          G.best = best;
          if (G.mode === 'saccade') return;
          if (G.mode === 'look') {
            if (near > c.floor * .6) { G.tx = nx; G.ty = ny; G.held = now; }   // the target moved: the eyes follow it
            else if (now - G.held > 300) { G.mode = 'hold'; G.until = now + c.hold; }
            if (G.mode === 'look' && calls && (now > G.until || best > Math.max(near, c.floor) * (G.tl > .5 ? c.distract : 1.15))) { saccade(bx, by, now); return; }   // a distraction, or done looking
            return;
          }
          if (calls) { saccade(bx, by, now); return; }
          if (G.mode === 'hold' && now > G.until) G.mode = 'rest';
        },
        // where the gaze zone is now, and its turn: moved a little every frame
        at: function (gz, now, dt) {
          if (!gz) return null;
          if (!G.cfg || G.cfg.src !== gz) { var fresh0 = !G.cfg; G.cfg = cfgOf(gz); G.cfg.src = gz; if (fresh0) { G.x = G.fx = G.tx = (G.cfg.region[0] + G.cfg.region[1]) / 2; } }
          var c = G.cfg, t = now / 1000, ddt = Math.min(dt || 16, 100);
          if (G.pinned) { G.x = G.pinned[0]; G.y = G.pinned[1]; return { x: G.x, y: G.y, rot: 0 }; }
          if (G.mode === 'saccade') {
            var p = clamp((now - G.t0) / G.dur, 0, 1), e = calm ? ease(p) : 1 - Math.pow(1 - p, 3);   // direct, and it does not overshoot
            G.x = lerp(G.fx, G.tx, e); G.y = lerp(G.fy, G.ty, e);
            if (p >= 1) {
              G.mode = 'look'; G.lookT0 = now; G.held = now; G.until = now + c.examine[0] + Math.random() * (c.examine[1] - c.examine[0]);
              var li = G.pri ? Math.min(G.pri.length - 1, Math.floor(G.ty * hs) * ws + Math.floor(G.tx * ws)) : -1; G.tl = li >= 0 && map ? map[li * 4 + 1] / 255 : 0;
              G.ior.push({ x: G.tx, y: G.ty, t: now }); if (G.ior.length > 6) G.ior.shift();
              G.log.push([+G.tx.toFixed(3), +G.ty.toFixed(3), Math.round(now), Math.round(freshMedia)]); if (G.log.length > 40) G.log.shift();
            }
          } else if (G.mode === 'look') {                                 // smooth pursuit, up to c.pursuit degrees a second
            var dx = (G.tx - G.x) * G.ax, dy = (G.ty - G.y) * G.ay, d = Math.sqrt(dx * dx + dy * dy), step = c.pursuit / CAM_DEG * ddt / 1000;
            if (d > 1e-6) { var k = Math.min(1, step / d, 1 - Math.exp(-ddt / 120)); G.x += (G.tx - G.x) * k; G.y += (G.ty - G.y) * k; }
          } else if (G.mode === 'rest' && !G.sleep) {                     // nothing calls: the eyes drift back to rest at c.back degrees a second
            var rx = (c.region[0] + c.region[1]) / 2, bx = (rx - G.x) * G.ax, by = (.5 - G.y) * G.ay, bd = Math.sqrt(bx * bx + by * by), bs = c.back / CAM_DEG * ddt / 1000;
            if (bd > 1e-6) { var kb = Math.min(1, bs / bd); G.x += (rx - G.x) * kb; G.y += (.5 - G.y) * kb; }
          }
          var ox = 0, rot = 0;
          if (!calm && G.mode === 'look') {                               // scanning: side-to-side sweeps, and a slow twist that holds at each end
            ox = deg(c.sweep[0] / 2) / G.ax * Math.sin(2 * Math.PI * (now - G.lookT0) / 1000 / c.sweep[1]);
            var turn = c.twist[1], holdT = c.twist[2], per = 2 * (turn + holdT), half = turn / (turn + holdT), ph = (((now - G.lookT0) / per * 2) + half / 2) % 2;   // it starts upright, half way through a turn
            var side = ph < 1 ? ph : ph - 1, sign = ph < 1 ? 1 : -1, tw = side < half ? -1 + 2 * ease(side / half) : 1;   // from one end to the other, then a hold
            rot = sign * tw * c.twist[0] * Math.PI / 180;
          }
          if (!calm && G.mode === 'rest' && !G.sleep && c.wander) {        // with nothing moving, a bout of sweeps now and then
            if (!G.nextWander) G.nextWander = now + c.wander[0] + Math.random() * (c.wander[1] - c.wander[0]);
            if (!G.wander && now > G.nextWander) { G.wander = now; G.wanderEnd = now + 3000 + Math.random() * 5000; G.wa = deg(6 + Math.random() * 8) / G.ax; G.wf = .15 + Math.random() * .35; }
            if (G.wander) {
              var wt = (now - G.wander) / 1000, env = Math.sin(Math.PI * clamp((now - G.wander) / (G.wanderEnd - G.wander), 0, 1));
              ox += G.wa * env * Math.sin(2 * Math.PI * G.wf * wt);
              if (now > G.wanderEnd) { G.wander = 0; G.nextWander = now + c.wander[0] + Math.random() * (c.wander[1] - c.wander[0]); }
            }
          } else if (G.mode !== 'rest') { G.wander = 0; G.nextWander = 0; }
          if (G.sleep) {                                                  // in the dark and still: bouts of twitching, closer together than a spider's
            var sl = c.sleep, bl = sl.bout || [6000, 12000], gp = sl.gap || [20000, 40000];
            if (!G.bout && now >= G.nextBout) { G.bout = 1; G.boutEnd = now + bl[0] + Math.random() * (bl[1] - bl[0]); G.twitchAt = 0; }
            if (G.bout) {
              if (now >= G.twitchAt) { G.twitchAt = now + 70 + Math.random() * 180; G.jx = deg((Math.random() - .5) * 5) / G.ax; G.jy = deg((Math.random() - .5) * 5) / G.ay; G.jr = (Math.random() - .5) * .6; }
              if (now >= G.boutEnd) { G.bout = 0; G.nextBout = now + gp[0] + Math.random() * (gp[1] - gp[0]); G.jx = G.jy = G.jr = 0; }
            }
            var q = calm ? .15 : 1; ox += G.jx * q; rot += G.jr * q;
            return { x: G.x + ox, y: G.y + G.jy * q, rot: rot };
          }
          return { x: G.x + ox, y: G.y, rot: rot };
        },
        iorList: function (now) {
          var c = G.cfg, out = []; if (!c) return out;
          for (var i = 0; i < G.ior.length; i++) { var I = G.ior[i], k = iorK(now - I.t, c); if (k > 0) out.push([I.x, I.y, c.iorR, k]); }
          return out;
        }
      };
    }
    // A view may move several zones with gazes of their own (`gaze` as a list of blocks, a zone's `gaze` naming its block from 1): two
    // fish eyes that each watch their own half of the field, say. Each has its own places to leave alone.
    var gazes = [];
    function gazeN(i) { return gazes[i] || (gazes[i] = makeGaze()); }
    var gaze = {
      onMap: function (m, w, h, now) { for (var i = 0; i < gazes.length; i++) gazes[i].onMap(m, w, h, now); },
      reset: function () { gazes.forEach(function (g) { g.reset(); }); },
      pin: function (x, y) { gazeN(0).pin(x, y); for (var i = 1; i < gazes.length; i++) gazes[i].pin(x, y); },
      iorList: function (now) { var out = []; gazes.forEach(function (g) { out = out.concat(g.iorList(now)); }); return out.slice(-6); },
      G: function () { return gazeN(0).G; }
    };

    // ---- uniforms for the zones, reused frame after frame
    var zG = new Float32Array(16), zH = new Float32Array(16), zR = new Float32Array(16), zX = new Float32Array(16), zP = new Float32Array(16), zQ = new Float32Array(16), zS = new Float32Array(16), zM = new Float32Array(36), zT = new Float32Array(16), zU = new Float32Array(16);
    var iorU = new Float32Array(24), ripU = new Float32Array(16), zLag = [0, 0, 0, 0], lastG = null;
    function blurOf(inv, longPx) { return inv > 1 / (HUMAN_CPD - 1) ? .6 * (longPx / VIEW_DEG) * inv : 0; }   // 0.6 of one cycle at that eye's limit
    // a sideways sweep of the whole picture (a shark swinging its head): P.pan degrees each way over P.panS seconds; it waits while the phone turns
    var panPh = 0;
    function panOf(P, now, dt) {
      if (!P.pan || calm) return 0;
      if (senses.turning() < 20) panPh += (dt || 16) / 1000 / P.panS;
      return P.pan / CAM_DEG * Math.sin(2 * Math.PI * panPh) * Math.max(sw, sh, 1) / Math.max(sw, 1);
    }
    var gzAt = [];
    function zoneUniforms(Z, P, now, dt, longPx) {
      var nz = Math.min(4, Z.length), i; gzAt.length = 0;
      for (i = 0; i < nz; i++) {
        var z = Z[i], cx = z.cx, cy = z.cy, rot = z.rot;
        if (z.gaze && P.gz) { var gi = z.gaze - 1, cf = P.gz.length ? P.gz[gi] : gi ? null : P.gz; if (cf) { if (!gzAt[gi]) gzAt[gi] = gazeN(gi).at(cf, now, dt); var gz = gzAt[gi]; cx = gz.x; cy = gz.y; rot += gz.rot; lastG = gz; } }
        var L0 = Math.max(sw, sh, 1);
        zG[i * 4] = cx; zG[i * 4 + 1] = cy; zG[i * 4 + 2] = z.frac ? z.frac[0] * sw / L0 : z.hw; zG[i * 4 + 3] = z.frac ? z.frac[1] * sh / L0 : z.hh;
        zH[i * 4] = z.shape; zH[i * 4 + 1] = z.soft; zH[i * 4 + 2] = z.inner; zH[i * 4 + 3] = 0;
        zR[i * 4] = Math.cos(rot); zR[i * 4 + 1] = Math.sin(rot);
        zX[i * 4] = z.tiltU; zX[i * 4 + 1] = z.tiltD; zX[i * 4 + 2] = z.gap; zX[i * 4 + 3] = z.tip;
        zP[i * 4] = blurOf(z.inv, longPx); zP[i * 4 + 1] = z.sat; zP[i * 4 + 2] = z.gain; zP[i * 4 + 3] = moving ? z.gate : 0;
        zQ[i * 4] = z.glow; zQ[i * 4 + 1] = z.living; zQ[i * 4 + 2] = z.uv; zQ[i * 4 + 3] = z.mag;
        zS[i * 4] = z.sheen; zS[i * 4 + 1] = z.uvR;
        for (var j = 0; j < 9; j++) zM[i * 9 + j] = z.M[j];
        zU[i * 4] = z.U ? z.U[0] : 0; zU[i * 4 + 1] = z.U ? z.U[1] : 0; zU[i * 4 + 2] = z.U ? z.U[2] : 0;
      }
      return nz;
    }

    var api = {
      floatOK: floatOK,
      setImage: function (cv) { moving = false; if (upload(cv, cv.width, cv.height)) reset = true; },
      // media: the frame's own time in ms where it has one (a clip's), so that the movement map's time constants follow the clip's clock
      setFrame: function (source, w, h, now, media) { if (!moving) { moving = true; resetTime(); } if (upload(source, w, h)) { pushRing(now); fresh = true; freshMedia = media === undefined ? -1 : media; } },
      resetTime: resetTime,
      setSide: function (n) { MAXSIDE = Math.max(240, Math.round(n)); },
      side: function () { return MAXSIDE; },
      // a slow phone gives up detail in the movement map before it gives up any of the picture (64, then 48, then 32 cells)
      lighten: function () { if (pViewZ && salFrames && salStep < SAL_SIDES.length - 1) { salStep++; return true; } return false; },
      clear: function () { hasFrame = false; },
      hasFrame: function () { return hasFrame; },
      newView: function () { gaze.reset(); salReset(); zLag = [0, 0, 0, 0]; slowReset(); fieldReset(); },
      fieldState: function () { return lastFld; },
      slowState: function () { return { mode: slowMode, n: slowN, develop: +develop.toFixed(3), spin: +spinS.toFixed(2), move: +picMove.toFixed(4), w: slowW, h: slowH, snell: lastSn, loc: !!(pViewZ && pViewZ.u.u_snell) }; },
      state: function () { return { sw: sw, sh: sh, writes: writes, stepMs: stepMs, moving: moving, floatOK: floatOK, err: gl.getError() }; },
      // what the last frames cost: script time inside draw() and, where offered, the graphics chip's time (both in ms, means of up to 90)
      probe: function (clear) { var r = { cpu: avg(cpuMs), gpu: avg(gpuMs), timer: !!tq, n: cpuMs.length, gpuN: gpuMs.length, sal: ws ? ws + 'x' + hs : '', zones: !!pViewZ, zErr: zErr, glErr: gl.getError(), stamps: stampSlots.filter(function (q) { return q.got && !q.live; }).length, light: LIGHT.reads, lum: +LIGHT.lum.toFixed(3) }; if (clear) { cpuMs = []; gpuMs = []; } return r; },
      // for the checks: the gaze, the movement map's last read, and a way to hold the gaze in one place
      gazeState: function () { var G = gaze.G(); return { x: G.x, y: G.y, mode: G.mode, jumps: G.jumps, ior: G.ior.length, sleep: G.sleep, best: G.best, map: mapInfo, sal: [ws, hs], salFrames: salFrames, pending: !!sync, log: G.log.slice(), gazes: gazes.map(function (g) { return [+g.G.x.toFixed(3), +g.G.y.toFixed(3), g.G.mode, g.G.jumps]; }) }; },
      replay: function (k) { if (writes > N) { replayT0 = performance.now(); replayK = k || 3; } }, replaying: function () { return replayT0 >= 0; },
      kick: function () { kickAt = performance.now(); },
      pinGaze: function (x, y) { gaze.pin(x === undefined ? null : x, y); },
      toPic: toPic, toScreen: toScreen, stampCount: function () { return stampSlots.filter(function (q) { return q.got && !q.live; }).length; },
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
    // ---- the screen and the camera picture. toScreen inverts the view pass's remap (squeeze and zoom; the fovea bulge is taken as 1),
    // in fractions of the canvas with y up; toPic is the forward remap, for a thumb on the screen.
    var lastP = null, lastMirror = 0, lastCamZoom = 1;
    function spanOf() { var A = canvas.width / canvas.height, sa = sw / Math.max(1, sh), k = Math.max(1, A / sa); return [k * sa, k, A]; }
    function toPic(fx, fy) {
      if (!lastP || !sw) return null;
      var S = spanOf(), px = (fx - .5) * S[2], py = fy - .5, r2 = px * px + py * py, z = lastP.zoom / lastCamZoom;
      var u = px * (1 + lastP.barrel * r2) / z / S[0] + .5, v = py * (1 + lastP.barrel * r2) / z / S[1] + .5;
      return [lastMirror ? 1 - u : u, v];
    }
    function toScreen(u, v) {
      if (!lastP || !sw) return null;
      var S = spanOf(), z = lastP.zoom / lastCamZoom, qx = ((lastMirror ? 1 - u : u) - .5) * S[0] * z, qy = (v - .5) * S[1] * z, px = qx, py = qy;
      for (var i = 0; i < 4; i++) { var r2 = px * px + py * py; px = qx / (1 + lastP.barrel * r2); py = qy / (1 + lastP.barrel * r2); }
      return [px / S[2] + .5, py + .5, S[1] * z];   // the last: one unit of the picture's long side, in canvas heights
    }

    // ---- stamps of attention (&draw=, the default gaze drawing for the jumping spider; docs/views/ATLAS.md, entry 10). While the gaze
    // looks a place over, what the strip shows there is copied into a slot; when the gaze jumps away the copy stays where it was taken
    // and fades over the view's ignoring time (gaze.ior, about 5 s: Ferrante and colleagues 2024). The thumbnail and its fade are invented.
    var STAMP_N = 6, STAMP_W = 96, STAMP_H = 224, stampTex = null, stampSlots = [], stampJumps = -1, stampAt = 0, pStamp = null;
    var FS_STAMP = '#version 300 es\nprecision highp float; in vec2 v; out vec4 o; uniform sampler2D u_s; uniform vec4 u_src; uniform float u_a;\n' +
      'void main(){ vec2 t = u_src.xy + v * u_src.zw; vec2 e = min(v, 1.0 - v); float m = smoothstep(0.0, 0.12, min(e.x, e.y * 0.45));\n' +
      '  float rim = (1.0 - smoothstep(0.0, 0.03, min(e.x, e.y * 0.45))) * 0.5; o = vec4(mix(texture(u_s, t).rgb, vec3(1.0), rim), u_a * max(m, rim)); }';
    function stamps(P, now) {
      var G = gaze.G(), z = null, i;
      for (i = 0; i < (P.zones || []).length; i++) if (P.zones[i].gaze === 1) { z = P.zones[i]; break; }
      if (!z) return;
      if (!stampTex) {
        stampTex = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, stampTex);
        gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA8, STAMP_W * STAMP_N, STAMP_H, 0, gl.RGBA, gl.UNSIGNED_BYTE, null);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
        try { pStamp = prog(FS_STAMP); } catch (e) { zErr = zErr || String(e.message || e).slice(0, 200); return; }
      }
      var ior = (G.cfg && G.cfg.ior) || 5000, sc = toScreen(G.x, G.y);
      if (!sc) return;
      var H = canvas.height, hh = Math.min(.45, z.hh * 1.15 * sc[2]) * H, hw = Math.max(hh * .42, 8);   // the cross and a little round it
      var rect = [Math.round(sc[0] * canvas.width - hw), Math.round(sc[1] * H - hh), Math.round(hw * 2), Math.round(hh * 2)];
      var looking = G.mode === 'look' || G.mode === 'hold';
      if (G.jumps !== stampJumps) { stampJumps = G.jumps; if (stampSlots.length && stampSlots[stampSlots.length - 1].live) stampSlots[stampSlots.length - 1].live = false; }
      var cur = stampSlots[stampSlots.length - 1];
      if (looking && (!cur || !cur.live)) {
        var used = stampSlots.map(function (q) { return q.slot; }), slot = 0;
        while (used.indexOf(slot) >= 0 && slot < STAMP_N) slot++;
        if (slot >= STAMP_N) { slot = stampSlots[0].slot; stampSlots.shift(); }
        cur = { slot: slot, live: true, rect: rect, left: 0, got: 0 }; stampSlots.push(cur);
      }
      if (cur && cur.live) {
        cur.rect = rect; cur.left = now;
        if (now - stampAt > 120) {   // copy what the strip shows now, scaled into its slot (a blit from the picture just drawn)
          stampAt = now; cur.got = 1;
          var x0 = Math.max(0, rect[0]), y0 = Math.max(0, rect[1]), x1 = Math.min(canvas.width, rect[0] + rect[2]), y1 = Math.min(H, rect[1] + rect[3]);
          if (x1 - x0 > 2 && y1 - y0 > 2) {
            if (!stampFb) stampFb = gl.createFramebuffer();
            gl.bindFramebuffer(gl.DRAW_FRAMEBUFFER, stampFb); gl.framebufferTexture2D(gl.DRAW_FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, stampTex, 0);
            gl.bindFramebuffer(gl.READ_FRAMEBUFFER, null);
            gl.blitFramebuffer(x0, y0, x1, y1, cur.slot * STAMP_W, 0, (cur.slot + 1) * STAMP_W, STAMP_H, gl.COLOR_BUFFER_BIT, gl.LINEAR);
            gl.bindFramebuffer(gl.FRAMEBUFFER, null);
            cur.rect = [x0, y0, x1 - x0, y1 - y0];
          }
        }
      }
      stampSlots = stampSlots.filter(function (q) { return q.live || now - q.left < ior; });
      gl.useProgram(pStamp.p); gl.enable(gl.BLEND); gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
      gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, stampTex); gl.uniform1i(pStamp.u.u_s, 0);
      stampSlots.forEach(function (q) {
        if (q.live || !q.got) return;                  // the live look is the strip itself
        var a = 1 - (now - q.left) / ior; if (a <= 0) return;
        gl.viewport(q.rect[0], q.rect[1], q.rect[2], q.rect[3]);
        gl.uniform4f(pStamp.u.u_src, q.slot / STAMP_N, 0, 1 / STAMP_N, 1); gl.uniform1f(pStamp.u.u_a, .92 * a * a);
        gl.drawArrays(gl.TRIANGLES, 0, 3);
      });
      gl.disable(gl.BLEND); gl.viewport(0, 0, canvas.width, canvas.height);
    }
    var stampFb = null;
    // the ribbon's texture, made on first use
    function ribbon() {
      if (ribTex) return ribTex;
      ribTex = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, ribTex); gl.texStorage2D(gl.TEXTURE_2D, 1, gl.RGBA8, 1024, 128);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.REPEAT); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      ribFb = gl.createFramebuffer(); return ribTex;
    }
    // every 100 ms, the picture just drawn (above the ribbon's band) is copied into the ribbon at the heading the phone faces
    function ribbonWrite(P, now) {
      if (now - ribAt < 100) return; ribAt = now; ribbon();
      var po = senses.pose(), yw = senses.yaw(), hd = po.heading !== null ? po.heading : yw !== null ? yw : 0, F = P.field || {};
      var wdeg = CAM_DEG * Math.min(canvas.width / canvas.height, 1), W = Math.max(2, Math.round(wdeg / 360 * 1024)), x0 = Math.round(hd / 360 * 1024 - W / 2), y0 = Math.round(canvas.height * (F.band || .22));
      gl.bindFramebuffer(gl.DRAW_FRAMEBUFFER, ribFb); gl.framebufferTexture2D(gl.DRAW_FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, ribTex, 0);
      gl.bindFramebuffer(gl.READ_FRAMEBUFFER, null);
      [x0, x0 - 1024, x0 + 1024].forEach(function (x) { if (x + W > 0 && x < 1024) gl.blitFramebuffer(0, y0, canvas.width, canvas.height, x, 0, x + W, 128, gl.COLOR_BUFFER_BIT, gl.LINEAR); });
      gl.bindFramebuffer(gl.FRAMEBUFFER, null);
      for (var k = Math.floor(x0 / 32); k <= Math.floor((x0 + W - 1) / 32); k++) ribTimes[((k % 32) + 32) % 32] = now;
    }
    // events for the overlays and the haptic module: sound onsets, knocks and the light's sudden darkenings
    function addOnsTo(P, now, dt) {
      var so = senses.sound(), kn = senses.knock(), H = P.hap || {}, fire = false;
      if (so.onsetAt && so.onsetAt !== seenOnset) {
        seenOnset = so.onsetAt;
        if (P.ovlMode === 'rings' || P.sndMode === 'rings' || P.ovlMode === 'web') evts.push({ x: (Math.random() - .5) * .25, y: (Math.random() - .5) * .25, t: now, a: clamp(.4 + so.band[so.onsetBand], .4, 1) });
        if (H.on === 'onset') fire = true;
      }
      if (kn && kn !== seenKnock) { seenKnock = kn; if (P.ovlMode === 'web' || P.ovlMode === 'rings') evts.push({ x: 0, y: 0, t: now, a: 1 }); if (H.on === 'knock') fire = true; }
      if (LIGHT.shock > .5 && now - seenShock > 600) { seenShock = now; if (P.ovlMode === 'shadow') evts.push({ x: (LIGHT.dir[0] - .5) * canvas.width / canvas.height, y: LIGHT.dir[1] - .5, t: now, a: -1 }); if (H.on === 'shock') fire = true; }
      if (fire && P.hapMode && now - hapAt > 120) {
        hapAt = now; var pat = H.pattern || [30], buzzed = false;
        if (P.hapMode === 'buzz' && navigator.vibrate) try { buzzed = navigator.vibrate(pat); } catch (x) { buzzed = false; }
        if (!buzzed) pulse = H.edge === undefined ? 1 : H.edge;   // where the browser cannot vibrate (iOS), the edge of the picture pulses
      }
      pulse *= Math.exp(-(dt || 16) / 180);
    }

    // ---- the light module (docs/ENGINE-DESIGN.md, module 3), first part: four times a second the smallest levels of the picture's
    // mip chain (8 by 8 cells or fewer) are read back behind a fence, never waited for. They give the mean light (LIGHT.lum, 0 to 1 of
    // the camera's own exposure, smoothed over about 2.5 s; a phone's exposure control means this is relative light, not lux), the
    // mean colour, the direction of the brightest cell, a darkening shock, and the colour at any place (for &draw=palm).
    var light = (function () {
      var fb = null, pbo = null, sync = null, at = 0, lvl = 0, w = 0, h = 0, buf = null;
      function tick(now) {
        if (!sw || !tA) return;
        if (sync && gl.getSyncParameter(sync, gl.SYNC_STATUS) === gl.SIGNALED) {
          gl.deleteSync(sync); sync = null;
          gl.bindBuffer(gl.PIXEL_PACK_BUFFER, pbo); gl.getBufferSubData(gl.PIXEL_PACK_BUFFER, 0, buf, 0, w * h * 4); gl.bindBuffer(gl.PIXEL_PACK_BUFFER, null);
          var n = w * h, r = 0, g = 0, b = 0, best = -1, bi = 0, i, sc = floatOK ? 1 : 1 / 255;
          for (i = 0; i < n; i++) { var R = buf[i * 4] * sc, Gc = buf[i * 4 + 1] * sc, B = buf[i * 4 + 2] * sc, Y = .2126 * R + .7152 * Gc + .0722 * B; r += R; g += Gc; b += B; if (Y > best) { best = Y; bi = i; } }
          r /= n; g /= n; b /= n;
          var lum = .2126 * r + .7152 * g + .0722 * b, k = LIGHT.reads ? Math.min(1, (now - LIGHT.at) / 2500) : 1;
          LIGHT.shock = Math.max(LIGHT.shock * .5, LIGHT.raw > 0 && lum < LIGHT.raw * .5 && now - LIGHT.at < 400 ? 1 : 0);
          LIGHT.raw = lum; LIGHT.lum += (lum - LIGHT.lum) * k; LIGHT.col = [r, g, b]; LIGHT.dir = [(bi % w + .5) / w, (Math.floor(bi / w) + .5) / h];
          LIGHT.cells = { w: w, h: h, scale: sc, data: buf.slice(0, n * 4) }; LIGHT.at = now; LIGHT.reads++;
        }
        if (sync || now - at < 250) return;
        at = now;
        if (!fb) { fb = gl.createFramebuffer(); pbo = gl.createBuffer(); buf = floatOK ? new Float32Array(64 * 4) : new Uint8Array(64 * 4); gl.bindBuffer(gl.PIXEL_PACK_BUFFER, pbo); gl.bufferData(gl.PIXEL_PACK_BUFFER, buf.byteLength, gl.STREAM_READ); gl.bindBuffer(gl.PIXEL_PACK_BUFFER, null); }
        lvl = Math.max(0, levels - 4); w = Math.max(1, sw >> lvl); h = Math.max(1, sh >> lvl);
        while (w * h > 64) { lvl++; w = Math.max(1, sw >> lvl); h = Math.max(1, sh >> lvl); }
        gl.bindFramebuffer(gl.FRAMEBUFFER, fb); gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, tA, lvl);
        gl.bindBuffer(gl.PIXEL_PACK_BUFFER, pbo); gl.readPixels(0, 0, w, h, gl.RGBA, floatOK ? gl.FLOAT : gl.UNSIGNED_BYTE, 0); gl.bindBuffer(gl.PIXEL_PACK_BUFFER, null);
        gl.bindFramebuffer(gl.FRAMEBUFFER, null);
        sync = gl.fenceSync(gl.SYNC_GPU_COMMANDS_COMPLETE, 0);
      }
      return { tick: tick };
    })();
    return api;

    function drawFrame(P, fx, now, dt) {
        lastP = P; lastMirror = fx.mirror ? 1 : 0; lastCamZoom = fx.camZoom || 1;
        gl.bindVertexArray(vao);
        if (!hasFrame) { gl.bindFramebuffer(gl.FRAMEBUFFER, null); gl.viewport(0, 0, canvas.width, canvas.height); gl.clearColor(0, 0, 0, 1); gl.clear(gl.COLOR_BUFFER_BIT); return; }
        var Z = P.zones && P.zones.length ? P.zones : null, zoned = (Z || P.sal > .001 || P.ripple > .001 || P.pan || P.water || P.spec || P.lock || P.slowMode || P.snell || P.magMode || P.fieldMode || P.ovlMode || P.sndMode || P.hapMode) && zonePrograms();
        var ad = adaptOf(P);
        if (ad > .001) { var M0 = P.M, U0 = P.U, Pa = {}, pk; for (pk in P) Pa[pk] = P[pk]; Pa.M = M0.map(function (x, j) { return lerp(x, P.adapt.M[j], ad); }); Pa.U = U0.map(function (x, j) { return lerp(x, P.adapt.U[j], ad); }); P = Pa; }
        if (zoned) readPoll(now);
        var useRing = 0, back = 0, nowMix = 0, a = 1, zPace = false;
        if (replayT0 >= 0 && (!P.replay || !moving)) replayT0 = -1;
        if (moving && writes > N && replayT0 >= 0) {
          back = (N - 2) - (now - replayT0) / replayK / stepMs;
          if (back < 0) { replayT0 = -1; back = 0; } else useRing = 1;
        } else if (moving && writes > N && P.arm) { useRing = 1; back = 0; lag = 0;
        } else if (moving && writes > N) {
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
          salience(now, 1 - clamp((sp - 25) / 70, 0, .85), [0, 0], freshMedia);
        }
        var slowU = zoned && P.slowMode ? slowTick(P, now) : null; if (!(zoned && P.slowMode === 'righting')) spinS = 0;
        fresh = false;
        var gateAny = P.gate > .5 || (Z && Z.some(function (z) { return z.gate > .01; }));
        var tp = zoned && (zPace || slowU) ? pTimeZ : pTime;
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

        if (tp === pTimeZ) {
          gl.uniform2f(ut.u_zScale, sw / Math.max(sw, sh), sh / Math.max(sw, sh)); gl.uniform1i(ut.u_nz, nz);
          gl.uniform4fv(ut['u_zG[0]'], zG); gl.uniform4fv(ut['u_zH[0]'], zH); gl.uniform4fv(ut['u_zR[0]'], zR); gl.uniform4fv(ut['u_zX[0]'], zX); gl.uniform4fv(ut['u_zT[0]'], zT);
          gl.activeTexture(gl.TEXTURE3); gl.bindTexture(gl.TEXTURE_2D, slowU && slowT[0] ? slowT[0] : texSrc); gl.uniform1i(ut.u_store, 3); gl.activeTexture(gl.TEXTURE0);
          gl.uniform4f(ut.u_slow, slowU ? slowU[0] : 0, slowU ? slowU[1] : 0, 0, 0);
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
        function viewU(u, P) {
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
        }
        viewU(u, P);
        if (zoned) {
          gl.uniform1i(u.u_nz, nz); gl.uniform2f(u.u_zScale, sw / Math.max(sw, sh), sh / Math.max(sw, sh));
          gl.uniform4fv(u['u_zG[0]'], zG); gl.uniform4fv(u['u_zH[0]'], zH); gl.uniform4fv(u['u_zR[0]'], zR); gl.uniform4fv(u['u_zX[0]'], zX);
          gl.uniform4fv(u['u_zP[0]'], zP); gl.uniform4fv(u['u_zQ[0]'], zQ); gl.uniform4fv(u['u_zS[0]'], zS); gl.uniformMatrix3fv(u['u_zM[0]'], true, zM);
          var salOn = moving && salT[0] && salFrames > 1 ? P.sal : 0;
          gl.uniform1f(u.u_salOn, salOn); gl.uniform4f(u.u_base, P.glow, P.living, P.uvR, 0); gl.uniform3f(u.u_glowC, P.glowC[0], P.glowC[1], P.glowC[2]);
          gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, salT[salAt] || tA); gl.uniform1i(u.u_sal, 1);
          var L = P.gz ? gaze.iorList(now) : [];
          for (var ii = 0; ii < 6; ii++) { var I = L[ii]; iorU[ii * 4] = I ? I[0] : 0; iorU[ii * 4 + 1] = I ? I[1] : 0; iorU[ii * 4 + 2] = I ? I[2] : 1; iorU[ii * 4 + 3] = I ? I[3] * salOn : 0; }
          gl.uniform4fv(u['u_ior[0]'], iorU);
          var R = fx.rip || [];
          for (var ri = 0; ri < 4; ri++) { var rr = R[ri]; ripU[ri * 4] = rr ? rr[0] : 0; ripU[ri * 4 + 1] = rr ? rr[1] : 0; ripU[ri * 4 + 2] = rr ? rr[2] : 0; ripU[ri * 4 + 3] = rr ? rr[3] : 0; }
          gl.uniform4fv(u['u_rip[0]'], ripU); gl.uniform1f(u.u_ripK, (fx.ripK || 0) * P.ripple);
          gl.uniform1f(u.u_shimmer, calm ? P.shimmer * .3 : P.shimmer); gl.uniform1f(u.u_time, (now / 1000) % 1000);
          gl.uniform1f(u.u_pan, panOf(P, now, dt)); gl.uniform1f(u.u_palm, P.palm || 0);
          gl.uniform3f(u.u_U, P.U[0], P.U[1], P.U[2]); gl.uniform4fv(u['u_zU[0]'], zU);
          if (P.Q) gl.uniformMatrix4fv(u.u_Q, true, new Float32Array(P.Q));
          gl.uniform1f(u.u_rot4, P.rot4 >= 0 && P.Q ? WHEEL.turn : -1); gl.uniform1f(u.u_neutral, calm ? (P.neutral || 0) * .3 : P.neutral || 0);
          var st = P.lock ? senses.stab(P.motion, now) : null; gl.uniform2f(u.u_stab, st ? st[0] / CAM_DEG : 0, st ? st[1] / CAM_DEG : 0);
          gl.uniform1f(u.u_spin, spinS * Math.PI / 180);
          var pose = P.snell || P.magMode ? senses.pose() : null, sn = P.snell && pose ? clamp((pose.elev - (P.tilt.fromDeg || 15)) / ((P.tilt.fullDeg || 45) - (P.tilt.fromDeg || 15)), 0, 1) : 0;
          lastSn = sn; gl.uniform3f(u.u_snell, sn, pose ? clamp((90 - pose.elev) / 97, 0, 1) * .5 : 0, 0);   // the disc slides toward the top as the phone levels
          var mg = P.magMode && pose && pose.heading !== null ? pose.heading : null, red = LIGHT.reads ? clamp(((LIGHT.col[0] - LIGHT.col[2]) / (LIGHT.col[0] + .02) - .3) * 2.5, 0, 1) : 0;   // red or yellow light melts it (birds draft)
          gl.uniform3f(u.u_mag, mg !== null && P.magMode === 'grain' ? (P.magnet.k || 1) * (1 - red) : 0, mg !== null && P.magMode === 'tide' ? (P.magnet.k || 1) * .3 * (.5 + .5 * Math.cos(mg * Math.PI / 180)) * (1 - red) : 0, mg !== null ? -mg * Math.PI / 180 + Math.PI / 2 : 0);
          if (P.snellFixed) gl.uniform3f(u.u_snell, 1, 0, 0);   // Snell's window as a field: always there, centred (&draw=window)
          addOnsTo(P, now, dt);
          var F = P.field || {}, O = P.ovl || {}, SD = P.snd || {}, po = senses.pose(), yw = senses.yaw(), hd = po.heading !== null ? po.heading : yw !== null ? yw : 0;
          if (fldRef === null) fldRef = hd;
          var fc = P.fieldMode === 'wedge' ? 1 : P.fieldMode === 'fold' ? 2 : P.fieldMode === 'ribbon' ? 4 : 0;
          if (fc === 1) gl.uniform4f(u.u_fld, 1, hd - fldRef, F.blindAt === undefined ? 180 : F.blindAt, (F.blindDeg || 30) / 2);
          else if (fc === 2) gl.uniform4f(u.u_fld, 2, F.fold || .6, F.horizon || 0, 0);
          else if (fc === 4) gl.uniform4f(u.u_fld, 4, F.band || .22, hd / 360, F.fadeS || 60);
          else gl.uniform4f(u.u_fld, 0, 0, 0, 0);
          gl.uniform4f(u.u_fld2, F.blindSoft || 6, CAM_DEG, CAM_DEG * Math.min(canvas.width / canvas.height, 1) / 360, 0);
          if (fc === 4) { for (var qi = 0; qi < 32; qi++) ribT[qi] = ribTimes[qi] < -1e11 ? 1e6 : (now - ribTimes[qi]) / 1000; gl.uniform4fv(u['u_ribT[0]'], ribT); gl.activeTexture(gl.TEXTURE5); gl.bindTexture(gl.TEXTURE_2D, ribbon()); gl.uniform1i(u.u_rib, 5); gl.activeTexture(gl.TEXTURE1); }
          var C = P.ovlMode === 'polar' ? clockNow() : null, D2R = Math.PI / 180;
          gl.uniform4f(u.u_ov, C && C.sun > -6 ? (O.polar || 1) : 0, P.ovlMode === 'web' ? O.web || .8 : 0, P.ovlMode === 'rings' || P.sndMode === 'rings' ? O.rings || 1 : 0, P.ovlMode === 'shadow' ? O.shadow || 1 : 0);
          gl.uniform4f(u.u_ovP, C ? (hd - C.az) * D2R : 0, (po.elev || 0) * D2R, C ? C.sun * D2R : 0, CAM_DEG * D2R);
          while (evts.length && (now - evts[0].t > 3000 || evts.length > 8)) evts.shift();
          for (var ei = 0; ei < 8; ei++) { var E = evts[ei]; evtU[ei * 4] = E ? E.x : 0; evtU[ei * 4 + 1] = E ? E.y : 0; evtU[ei * 4 + 2] = E ? (now - E.t) / 1000 : 0; evtU[ei * 4 + 3] = E ? E.a : 0; }
          gl.uniform4fv(u['u_evt[0]'], evtU);
          var so = senses.sound(), sm = so.on ? ({ air: 1, rumble: 2, hear: 3, clap: 4, rings: 5 })[P.sndMode] || 0 : 0, age = so.onsetAt ? (now - so.onsetAt) / 1000 : 99, lit = 0;
          if (sm === 3) lit = (so.onsetBand === 2 ? 1 : .6) * Math.exp(-age / (SD.flashS || .8)) + (SD.steady === undefined ? .4 : SD.steady) * so.band[2];
          if (sm === 4) lit = Math.exp(-age / (SD.holdS || .35));
          gl.uniform4f(u.u_snd, so.band[0] * (SD.k || 1), so.band[1], so.band[2], so.breath * (SD.k || 1)); gl.uniform4f(u.u_hear, age, sm, sm === 4 ? (SD.dark === undefined ? .04 : SD.dark) : (SD.dark === undefined ? .12 : SD.dark), lit);
          gl.uniform1f(u.u_pulse, pulse);
          lastFld = { field: P.fieldMode, ref: fldRef, heading: hd, sound: so.on ? [+so.band[0].toFixed(2), +so.band[1].toFixed(2), +so.band[2].toFixed(2), +so.breath.toFixed(2)] : null, lit: +lit.toFixed(2), events: evts.length, pulse: +pulse.toFixed(2) };
          var W4 = P.water || [0, 0, 0, 0], WC = P.waterC || [0, 0, 0]; gl.uniform4f(u.u_water, W4[0], W4[1], W4[2], W4[3]); gl.uniform3f(u.u_waterC, WC[0], WC[1], WC[2]);
        }
        gl.drawArrays(gl.TRIANGLES, 0, 3);
        if (zoned) gl.activeTexture(gl.TEXTURE0);
        // the compare slider (?tune=1, docs/ENGINE-DESIGN.md section 4): the person's own view drawn again over the left of the divider,
        // from the same picture, so both halves line up at the divider. It reads the time pass's picture, which for today's views
        // holds the live frame; for a view with trails the left side keeps them (a simplification of the design's second read).
        if (TUNE.cmp > 0 && TUNE.cmp < 1) {
          gl.enable(gl.SCISSOR_TEST); gl.scissor(0, 0, Math.round(canvas.width * TUNE.cmp), canvas.height);
          gl.useProgram(pView.p); var hu = mix(HUMAN, HUMAN, 0); hu.zoom = P.zoom; hu.barrel = P.barrel;   // the same squeeze, so the halves meet
          viewU(pView.u, hu); gl.uniform1f(pView.u.u_gateMix, 0); gl.uniform1f(pView.u.u_blur, blurOf(HUMAN.inv, longPx));
          gl.drawArrays(gl.TRIANGLES, 0, 3); gl.disable(gl.SCISSOR_TEST);
        }
        if (zoned && P.gz && P.stamps > .5) stamps(P, now);
        if (zoned && P.fieldMode === 'ribbon') ribbonWrite(P, now);
        light.tick(now);
    }
  }
