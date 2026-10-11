(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };

  // ---------- where is this running?
  // Inside Claude's viewer the camera is normally refused, and only there can Claude name a photo.
  var inViewer = !!(window.claude && typeof window.claude.use === 'function');
  var hasCamera = !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);
  var coarse = !!(window.matchMedia && window.matchMedia('(pointer: coarse)').matches);
  var calm = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var BUILD = '8';
  // Sharpness is drawn against the viewer's own eye: the long side of the screen is taken to fill
  // this many degrees of their view (a phone at arm's length, a laptop on a desk). An assumption.
  var VIEW_DEG = coarse ? 24 : 34;
  var HUMAN_CPD = 60;

  // ---------- the eyes
  // rows: [grade, title, text]. m = measured in this animal, g = measured in a relative or a wider group,
  // i = a guess, x = left out. Every number is a first entry for a vision scientist to correct.
  var I3 = [1, 0, 0, 0, 1, 0, 0, 0, 1];
  var PROTAN = [0.11238, 0.88762, 0, 0.11238, 0.88762, 0, 0.00401, -0.00401, 1];   // Vienot, Brettel & Mollon 1999, from memory
  var DEUTAN = [0.29275, 0.70725, 0, 0.29275, 0.70725, 0, -0.02234, 0.02234, 1];
  var BEE = [0, 1, 0, 0, 0, 1, 0, 0, 0];   // their green drawn as red, their blue as green; ultraviolet (invented) goes to blue
  var SLOW = ' The picture is slowed to that ratio, then jumps to catch up. That rendering is this app’s invention.';
  var EYES = {
    cat: { chip: 'Cat', who: 'a cat', fov: 200, cpd: 8, topoA: 1, fall: 2.0, pupil: 'v', dof: 26, M: DEUTAN, gain: 1.7, sat: .8,
      cue: 'What leaves focus smears up and down. Tap to move the focus.', rows: [
      ['m', 'Sharpness', 'About a fifth to a tenth of yours. The screen is blurred to what such an eye would keep of it at arm’s length.'],
      ['m', 'Colour', 'Two cone types, near 450 and 555 nanometres. Reds fall toward olive and grey.'],
      ['m', 'Pupil', 'A vertical slit, as in other ambush hunters. What is out of focus smears up and down.'],
      ['m', 'Field', 'About 200 degrees to your 180. The camera holds a slice of it, and the edges are invented.'],
      ['m', 'Dim light', 'Six to eight times your sensitivity. Shadows are lifted to suggest it.'],
      ['i', 'Depth', 'A camera feed carries no distances. Near and far are guessed from height in the frame, and a tap sets the focus.'],
      ['i', 'Where it is sharp', 'One central spot, entered from memory.'],
      ['x', 'Movement', 'Cats are reported to miss very slow movement. Left out.']] },
    dog: { chip: 'Dog', who: 'a dog', fov: 240, cpd: 11, topoS: 1, fall: 1.6, pupil: 'o', dof: 10, M: DEUTAN, gain: 1.3, sat: .85,
      cue: 'Sharpest along the horizon. Tap to move the focus.', rows: [
      ['m', 'Sharpness', 'A quarter to a seventh of yours, blurred as that share of what this screen gives you.'],
      ['m', 'Where it is sharp', 'A band along the horizon in long-nosed dogs, a single spot in short-nosed ones. The band is drawn.'],
      ['i', 'Colour', 'Two cone types, entered from memory and drawn with a model of human two-cone vision.'],
      ['i', 'Field, dim light and depth', 'Guesses. Near and far come from height in the frame.']] },
    squirrel: { chip: 'Squirrel', who: 'a squirrel', fov: 270, cpd: 6, topoS: 1, fall: 1.0, pupil: 'o', dof: 4, M: PROTAN, rate: .56,
      cue: 'Each moment runs slow, then the picture catches up.', rows: [
      ['g', 'Colour', 'Two cone types, measured in ground squirrels near 437 and 518 nanometres.'],
      ['g', 'Pace', 'Ground squirrels follow flicker to 108 a second, and you stop near 60.' + SLOW],
      ['i', 'Field and sharpness', 'Guesses: eyes on the sides of the head, and coarser detail than yours.']] },
    deer: { chip: 'Deer', who: 'a deer', fov: 310, cpd: 8, topoS: 1, fall: 2.2, pupil: 'h', dof: 22, M: DEUTAN, gain: 1.5, sat: .85,
      cue: 'A wide band of ground, smeared sideways where it leaves focus.', rows: [
      ['m', 'Colour', 'Two cone types, near 455 and 537 nanometres in white-tailed deer. Reds and oranges fall toward yellow and grey.'],
      ['m', 'Field', 'About 310 degrees. The camera holds under a quarter of it, and the rest is invented.'],
      ['g', 'Pupil', 'A horizontal bar. In grazing animals it widens the view along the ground and cuts glare from above. What is out of focus smears sideways.'],
      ['i', 'Sharpness, dim light and depth', 'Guesses. Near and far come from height in the frame.']] },
    rabbit: { chip: 'Rabbit', who: 'a rabbit', fov: 350, cpd: 3, topoS: 1, fall: 2.0, pupil: 'o', dof: 6, M: DEUTAN,
      cue: 'Nearly the whole circle at once, and little of it sharp.', rows: [
      ['i', 'All of it', 'Entered from memory and unchecked: a field nearly all the way round, a sharp band along the horizon, coarse detail, two cone types.']] },
    hawk: { chip: 'Hawk, eagle, falcon', who: 'a hawk', fov: 180, cpd: 60, fovea: 2.2, pupil: 'o', rate: .6,
      cue: 'The centre is pulled close, and each moment runs slow.', rows: [
      ['g', 'Sharpness', 'An eagle resolves about 140 cycles per degree to your 60. The centre is magnified to suggest it, though a phone cannot supply the detail.'],
      ['m', 'Pace', 'A peregrine follows flicker to 129 a second and a Harris’s hawk to 77, against your 50 to 60.' + SLOW.replace('that ratio', 'suggest it')],
      ['x', 'Gait', 'Raptors do not walk with a held head, so the picture does not step.'],
      ['i', 'Field', 'Left as the camera gives it.']] },
    wader: { chip: 'Heron, crane, pigeon', who: 'a wading bird', fov: 300, cpd: 25, topoS: .6, fall: .8, pupil: 'o', sheen: .6, hold: 280, thrust: 120,
      cue: 'Walk. The picture holds, then lurches, as a heron’s head does.', rows: [
      ['m', 'Gaze', 'Herons, egrets, cranes, pigeons and chickens walk with a held head: the eye stays fixed on the world, then the head thrusts forward. The picture holds, then lurches.'],
      ['g', 'Tempo', 'The thrust lasts 100 to 150 milliseconds in pigeons. The length of the hold is a guess.'],
      ['g', 'Sharpness', 'Most birds resolve under 30 cycles per degree to your 60.'],
      ['i', 'Ultraviolet', 'Some birds see it and no phone records it. The violet is invented.'],
      ['i', 'Field', 'A guess: eyes on the sides of the head.']] },
    bird: { chip: 'Other bird', who: 'a bird', fov: 300, cpd: 25, topoA: .5, fall: .6, pupil: 'o', sheen: .8, rate: .5,
      cue: 'Each moment runs slow, then the picture catches up.', rows: [
      ['g', 'Pace', 'Birds follow flicker at 40 to 140 a second, the faster movers higher, and you stop near 60.' + SLOW.replace('that ratio', 'suggest it')],
      ['g', 'Sharpness', 'Most birds resolve under 30 cycles per degree to your 60.'],
      ['i', 'Ultraviolet', 'Some birds see it and no phone records it. The violet is invented.'],
      ['i', 'Field', 'A guess: eyes on the sides of the head.']] },
    alligator: { chip: 'Alligator', who: 'an alligator', fov: 280, cpd: 9, topoS: 1, fall: 2.6, pupil: 'v', dof: 24, gain: 1.6, sat: .9,
      cue: 'One sharp band along the waterline.', rows: [
      ['g', 'Where it is sharp', 'A band along the horizon, measured in crocodiles. It lets them scan the waterline without turning the head.'],
      ['g', 'Colour', 'Crocodiles have three kinds of single cone, so colour is left as the camera gives it.'],
      ['g', 'Pupil', 'A vertical slit. What is out of focus smears up and down.'],
      ['i', 'Field, sharpness, dim light and depth', 'Guesses.']] },
    reptile: { chip: 'Lizard, snake, turtle', who: 'a reptile', fov: 280, cpd: 15, topoA: 1, fall: 1.2, pupil: 'o', sheen: .6,
      cue: '', rows: [
      ['i', 'All of it', 'Guesses: eyes on the sides of the head, one sharp central spot, and ultraviolet, drawn here as invented violet.']] },
    frog: { chip: 'Frog, toad', who: 'a frog or toad', fov: 340, cpd: 4, pupil: 'h', persist: .15, gate: 1,
      cue: 'Hold still, as a frog does. Only what moves is drawn.', rows: [
      ['m', 'Movement', 'A frog does not register the still parts of its world, and can starve beside food that keeps still. Only what changes is drawn, so hold the phone as still as a frog holds itself.'],
      ['g', 'Pace', 'A cane toad follows flicker to under 7 a second, a ninth of your rate, so movement smears into trails.'],
      ['i', 'Field, sharpness and pupil', 'Guesses.']] },
    bee: { chip: 'Bee', who: 'a bee', fov: 320, cpd: 1, pupil: 'none', M: BEE, uvBlue: 1, rate: .3,
      cue: 'Red goes dark, and each moment runs slow.', rows: [
      ['g', 'Sharpness', 'Most insects resolve under 1 cycle per degree to your 60.'],
      ['m', 'Red', 'Bees have no receptor for it. Red things go dark.'],
      ['m', 'Pace', 'A honeybee follows flicker to 200 a second in bright light, and you stop near 60.' + SLOW],
      ['i', 'Ultraviolet', 'Bees see it and no phone records it. The blue here is invented.'],
      ['x', 'Drawn as', 'False colour: their green as red, their blue as green, ultraviolet as blue.']] },
    insect: { chip: 'Butterfly, other insect', who: 'an insect', fov: 320, cpd: 1, pupil: 'none', sheen: .8, rate: .45,
      cue: 'Coarse and wide, and each moment runs slow.', rows: [
      ['g', 'Sharpness', 'Most insects resolve under 1 cycle per degree to your 60.'],
      ['g', 'Pace', 'Flies and dragonflies follow flicker past 100 a second, and one beetle to 400.' + SLOW.replace('that ratio', 'suggest it')],
      ['i', 'Ultraviolet', 'Bees and some other insects see it and no phone records it. The violet is invented.']] },
    plant: { chip: 'Plant', who: 'a plant', pupil: 'none', field: 1, noGreen: 1, persist: 2.5,
      cue: 'There is no picture here, only how much light, what colour, and from where.', rows: [
      ['g', 'No picture', 'A plant has nothing to focus light. It gets how much there is, what colour, and from where.'],
      ['m', 'Neighbours', 'Plants read red against far-red light and detect neighbours before being shaded. A phone does not record that band.'],
      ['i', 'Green and time', 'Green is removed because leaves throw most of it back, and anything quick is averaged away. Both choices are invented.']] },
    other: { chip: 'Something else', who: 'this one', pupil: 'none', field: 1, sat: 0,
      cue: '', rows: [
      ['i', 'No account yet', 'Nothing sourced on how this one meets light. It is shown as light and dark only.']] },
    person: { chip: null, who: 'a person', pupil: 'o', cue: '', rows: [
      ['m', 'Same eyes', 'That is a person. You have those eyes already.']] }
  };
  var ORDER = ['cat', 'dog', 'squirrel', 'deer', 'rabbit', 'wader', 'bird', 'hawk', 'alligator', 'reptile', 'frog', 'bee', 'insect', 'plant', 'other'];

  function clamp(x, a, b) { return x < a ? a : x > b ? b : x; }
  function lerp(a, b, t) { return a + (b - a) * t; }
  function ease(t) { t = clamp(t, 0, 1); return t * t * (3 - 2 * t); }
  function paramsOf(m) {
    m = m || {};
    var s = clamp(180 / (m.fov || 180), .45, 1);
    return { zoom: s, barrel: (1 - s) * .9, fovea: m.fovea || 1, inv: 1 / (m.cpd || HUMAN_CPD), fall: m.fall || 0, wA: m.topoA || 0, wS: m.topoS || 0,
      dof: m.dof || 0, ax: m.pupil === 'v' ? .3 : 1, ay: m.pupil === 'h' ? .3 : 1, M: m.M || I3, uvBlue: m.uvBlue || 0, sheen: m.sheen || 0,
      gain: m.gain || 1, sat: m.sat === undefined ? 1 : m.sat, noGreen: m.noGreen || 0, gate: m.gate || 0, field: m.field || 0,
      persist: m.persist || 0, hold: m.hold || 0, thrust: m.thrust || 0, rate: m.rate || 1 };
  }
  var HUMAN = paramsOf(null);
  function mix(a, b, t) {
    var o = {}, k;
    for (k in a) if (k !== 'M') o[k] = lerp(a[k], b[k], t);
    o.M = a.M.map(function (x, i) { return lerp(x, b.M[i], t); });
    var src = t > .5 ? b : a;                      // the pace of movement switches whole, half way
    o.persist = src.persist; o.hold = src.hold; o.thrust = src.thrust; o.rate = src.rate; o.gate = t > .5 ? b.gate * clamp(t * 2 - 1, 0, 1) : 0;
    return o;
  }

  // ---------- what Gainesville photographs in October and November: iNaturalist research-grade records gathered by GBIF,
  // latitude 29.55 to 29.75, longitude -82.45 to -82.20, all years. [records, scientific name, English name], most recorded first.
  var G60 = [[719,"Alligator mississippiensis","American alligator"],[588,"Ardea herodias","Great blue heron"],[518,"Anhinga anhinga","Anhinga"],[466,"Tillandsia usneoides","Spanish moss"],[437,"Bidens alba","Beggarticks"],[411,"Dione vanillae","Gulf fritillary"],[399,"Anolis sagrei","Brown anole"],[397,"Eudocimus albus","White ibis"],[394,"Ardea alba","Great egret"],[326,"Gallinula chloropus","Gallinule"],[315,"Callicarpa americana","American beautyberry"],[290,"Sciurus carolinensis","Eastern gray squirrel"],[272,"Egretta caerulea","Little blue heron"],[250,"Anolis carolinensis","Green anole"],[242,"Dryophytes cinereus","Green treefrog"],[239,"Buteo lineatus","Red-shouldered hawk"],[238,"Setophaga palmarum","Palm warbler"],[236,"Harmonia axyridis","Asian lady beetle"],[229,"Aramus guarauna","Limpkin"],[222,"Osteopilus septentrionalis","Cuban treefrog"],[193,"Cardinalis cardinalis","Northern cardinal"],[192,"Vitis rotundifolia","Muscadine grape"],[187,"Desarmillaria caespitosa","Ringless honey mushroom"],[184,"Grus canadensis","Sandhill crane"],[183,"Sayornis phoebe","Eastern phoebe"],[180,"Egretta tricolor","Tricolored heron"],[171,"Odocoileus virginianus","White-tailed deer"],[169,"Egretta thula","Snowy egret"],[160,"Sabal palmetto","Cabbage palm"],[156,"Bombus impatiens","Common eastern bumble bee"],[155,"Urbanus proteus","Long-tailed skipper"],[154,"Liquidambar styraciflua","Sweetgum"],[152,"Apis mellifera","Western honey bee"],[150,"Mycteria americana","Wood stork"],[146,"Phalacrocorax auritus","Double-crested cormorant"],[142,"Smilax bona-nox","Catbrier"],[139,"Anaxyrus terrestris","Southern toad"],[136,"Apalone ferox","Florida softshell turtle"],[132,"Verbesina virginica","Frostweed"],[132,"Danaus plexippus","Monarch"],[130,"Quiscalus major","Boat-tailed grackle"],[128,"Anisomorpha buprestoides","Florida stick insect"],[127,"Mimus polyglottos","Northern mockingbird"],[126,"Magnolia grandiflora","Southern magnolia"],[115,"Urena lobata","Caesar weed"],[112,"Parthenocissus quinquefolia","Virginia creeper"],[110,"Coluber constrictor","Black racer"],[109,"Pleopeltis michauxiana","Resurrection fern"],[107,"Junonia coenia","Common buckeye"],[105,"Cathartes aura","Turkey vulture"],[105,"Rhus copallina","Winged sumac"],[104,"Heliconius charithonia","Zebra longwing"],[104,"Arilus cristatus","Wheel bug"],[102,"Phytolacca americana","American pokeweed"],[101,"Indigofera spicata","Creeping indigo"],[98,"Tadarida brasiliensis","Brazilian free-tailed bat"],[98,"Baccharis halimifolia","Groundsel tree"],[97,"Sylvilagus palustris","Marsh rabbit"],[97,"Ardisia crenata","Coral ardisia"],[97,"Agelaius phoeniceus","Red-winged blackbird"]];
  var G60_ALIAS = {"gallinula galeata":10,"hyla cinerea":15,"agraulis vanillae":6,"antigone canadensis":24,"nannopterum auritum":35,"nannopterum auritus":35,"armillaria tabescens":23,"pleopeltis polypodioides":48,"rhus copallinum":51,"bidens pilosa":5,"ardea alba egretta":9};   // later names for the same species, entered from memory

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
  function msg(t, ms) { clearTimeout(msgTimer); $('msg').textContent = t || ''; if (t && ms) msgTimer = setTimeout(function () { $('msg').textContent = ''; }, ms); }
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
  function labelDate(d) { var R = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii']; return d.getDate() + '.' + R[d.getMonth()] + '.' + d.getFullYear(); }
  function handName(key) { return key === 'other' ? 'Something alive' : cap(EYES[key].who.replace(/^an? /, '')); }
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
    $('rvCount').textContent = S.named && S.named.again ? 'Met ' + labelDate(new Date(S.named.again)) : S.nov === 'kind' ? 'A new kind of eye' : S.nov === 'name' ? 'First meeting' : S.nov === 'again' ? 'Met before' : '';
    $('rvWarn').textContent = S.eyes !== 'person' && guessed(S.eyes) ? 'Part of what follows is a guess.' : '';
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
    var E = EYES[S.eyes], line = S.eyes === 'person' ? 'That is a person. You have those eyes already.'
      : (isMoving() || !/slow|still|Walk/.test(E.cue)) && E.cue ? E.cue : 'Part of this is a guess. Tap the name to see which part.';
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
  function latestOf(key) { for (var i = 0; i < record.length; i++) if (record[i].key === key) return record[i]; return null; }
  function paintRecordBits() {
    var t = 'Met so far' + (record.length ? ': ' + record.length : '');
    $('introRec').textContent = t; $('recAskAnimal').textContent = t;
  }
  function renderRecord() {
    var met = {}, n = record.length, k = 0, have = {};
    record.forEach(function (m) { if (KINDS.indexOf(m.key) >= 0) met[m.key] = 1; var g = g60Of(m); if (g) have[g] = 1; });
    KINDS.forEach(function (key) { if (met[key]) k++; });
    $('recordSub').textContent = n ? n + (n === 1 ? ' meeting, and ' : ' meetings, and ') + k + ' of ' + KINDS.length + ' kinds of eye. Tap an eye to look through it again.'
      : 'No one yet. Photograph something alive: the meeting is kept here, and its eyes come with it.';
    var strip = $('eyeStrip'); strip.textContent = '';
    KINDS.forEach(function (key) {
      var b = el('button', 'eye'); b.type = 'button'; b.disabled = !met[key];
      b.setAttribute('aria-label', met[key] ? 'Look as ' + EYES[key].who : 'A kind of eye not yet met');
      b.appendChild(eyeGlyph(key, !!met[key]));
      if (met[key]) b.addEventListener('click', function () { lookAgain(latestOf(key)); });
      strip.appendChild(b);
    });
    var ul = $('metList'); ul.textContent = '';
    record.slice(0, 150).forEach(function (m) {
      var li = el('li'), th, tx = el('div'), look = el('button', 'ico sm'), x = el('button', 'x', '×');
      if (m.thumb) { th = el('img', 'th'); th.alt = ''; th.src = m.thumb; } else th = el('span', 'th');
      tx.appendChild(el('span', 'nm', m.common));
      tx.appendChild(el('span', 'sm', [m.sci, labelDate(new Date(m.at)), m.by === 'Claude' ? 'recognized by Claude' : m.by === 'page' ? 'recognized by a small model' : m.by === 'service' ? 'named by a larger model on a server' : m.by === 'device-large' ? 'named on this device by a larger model' : 'on your word'].filter(Boolean).join(' · ')));
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
      li.appendChild(th); li.appendChild(tx); li.appendChild(look); li.appendChild(x); ul.appendChild(li);
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
    if (!m || !EYES[m.key]) return;
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

  // ---------- recognition in the page itself: the pocket recognizer, and a larger model the person may fetch once
  // Outside Claude's viewer the page names the photo by itself: an image encoder run by ONNX Runtime Web in a worker
  // (vendor/rec-worker.js), and label vectors worked out beforehand. The files are described by models/<slot>/manifest.json
  // (docs/CONTRACTS.md). Nothing here is fetched before the opening screen is up, and nothing about a photo leaves the device.
  // Kept copies: every file is asked for with ?v=<version> and kept under that address, so a new version is a new address.
  // The runtime's version is its release number; a slot's version is a fingerprint of its manifest, which is always asked of the network first.
  // There are two slots. The pocket one (models/pocket) is fetched by the page itself once the opening screen is up. The larger one
  // (models/naturalist) is some hundreds of megabytes, in parts that may live on another origin: nothing of it is fetched until the
  // person has said so, its parts are kept one by one so that a download carries on where it stopped, and its worker is started only
  // when a photo needs it and let go after a minute with nothing to do.
  var ORT = { v: '1.30.0', dir: 'vendor/ort/', js: 'ort.wasm.min.js', mjs: 'ort-wasm-simd-threaded.mjs', wasm: 'ort-wasm-simd-threaded.wasm', wasmBytes: 14239897, ep: 'wasm' };
  var KIND_ORDER = ['cat', 'dog', 'squirrel', 'deer', 'rabbit', 'hawk', 'wader', 'bird', 'alligator', 'reptile', 'frog', 'bee', 'insect', 'plant', 'other', 'person'];   // the order of KINDS in tools/fusion/fuse.py
  var onThisMachine = /^(localhost|127\.0\.0\.1)$/.test(location.hostname);
  function recognizer(o) {                             // o.slot: where the manifest is, or 'off'; o.big: the larger model
    var big = !!o.big, slot = o.slot;
    var manifestUrl = /\.json$/.test(slot) ? slot : slot.replace(/\/$/, '') + '/manifest.json';
    var cannot = inViewer ? 'off' : slot === 'off' || /\.\.|^\/|\/\//.test(slot) ? 'off'
      : (typeof Worker !== 'function' || typeof WebAssembly !== 'object' || typeof fetch !== 'function' || typeof Float32Array !== 'function') ? 'browser'
      : (big && !window.caches) ? 'browser' : '';      // the larger model has to be kept, and this browser keeps nothing
    var SAY = {
      off: 'This page’s recognizer is switched off.',
      absent: 'This page has no recognizer yet.',
      missing: 'The recognizer’s files are missing.',
      network: 'The recognizer could not be downloaded.',
      damaged: 'The recognizer’s file arrived damaged.',
      unfit: 'The recognizer’s files do not fit this build of the page.',
      browser: 'This browser cannot run the recognizer.',
      died: 'The recognizer stopped working.',
      slow: 'The recognizer took too long.',
      photo: 'The recognizer failed on that photo.'
    };
    if (big) {
      Object.keys(SAY).forEach(function (k) { SAY[k] = SAY[k].replace('recognizer', 'larger model'); });
      SAY.room = 'There is not enough room on this device for the larger model.';
      SAY.keep = 'The larger model could not be kept on this device.';
      SAY.stopped = 'The download was stopped.';
    }
    var KEEP = 'keep-v1', EPS = 1e-9;
    var state = cannot ? 'failed' : 'idle', why = cannot, M = null, ver = '', base = '', cur = null, worlds = [], worker = null, loadP = null, loadMs = 0, info = { backend: '', threads: 0 };
    var got = 0, total = 0, pending = {}, nextId = 1, last = null, lastFail = '', onProgress = null, watchMs = big ? 120000 : 45000, netWaitMs = 6000, api;
    // the larger model only: what of it is kept, the download under way, and the rest it takes after a minute with nothing to do
    var have = '', gone = false, keptBytes = 0, partGot = 0, getP = null, getCtl = null, getFail = '', surveyP = null, idleMs = 60000, idleTimer = 0, queue = Promise.resolve(), asked = 0;

    function err(code, detail) { var e = new Error(SAY[code] || code); e.code = code; e.sentence = SAY[code] || SAY.died; e.detail = String(detail || ''); return e; }
    function abs(u, b) { try { return new URL(u, b || location.href).href; } catch (e) { return u; } }
    function withV(u, v) { return u + (u.indexOf('?') < 0 ? '?' : '&') + 'v=' + encodeURIComponent(v); }
    function fingerprint(text) {                       // two rounds of FNV-1a: enough to tell one manifest from the next
      var a = 0x811c9dc5, b = 0x01000193 ^ text.length, i, c;
      for (i = 0; i < text.length; i++) { c = text.charCodeAt(i); a = Math.imul(a ^ c, 0x01000193); b = Math.imul(b ^ (c + i), 0x85ebca6b); }
      return ('0000000' + (a >>> 0).toString(16)).slice(-8) + ('0000000' + (b >>> 0).toString(16)).slice(-8);
    }
    function keepOpen() { try { return window.caches ? caches.open(KEEP).catch(function () { return null; }) : Promise.resolve(null); } catch (e) { return Promise.resolve(null); } }
    // A kept copy, looked for in every way there is. Nothing here differs by what a request's headers say, so a copy kept with a Vary header
    // (GitHub Pages sends "Vary: Accept-Encoding") is matched whatever the asking request carries; and where this page's own store
    // will not open or will not answer, every store of this site is asked, the service worker's among them.
    function kept(cache, url) {
      function one(c) { try { return c.match(url, { ignoreVary: true }).then(function (hit) { return hit || null; }, function () { return null; }); } catch (e) { return Promise.resolve(null); } }
      return (cache ? one(cache) : Promise.resolve(null)).then(function (hit) { return hit || (window.caches ? one(caches) : null); });
    }
    function unkeep(url) {                             // out of every store of this site
      if (!window.caches) return Promise.resolve();
      return caches.keys().then(function (names) {
        return Promise.all(names.map(function (n) { return caches.open(n).then(function (c) { return c.delete(url, { ignoreVary: true }); }); }));
      }).catch(function () {});
    }
    function notify() { if (onProgress) onProgress(); }
    function tick(n) { got += n; notify(); }
    function readAll(res, expect, count) {             // the whole body, counted as it arrives
      if (!res.body || !res.body.getReader) return res.arrayBuffer().then(function (b) { count(b.byteLength); return b; });
      var reader = res.body.getReader(), buf = expect ? new Uint8Array(expect) : null, chunks = [], n = 0;
      function pump() {
        return reader.read().then(function (r) {
          if (r.done) return;
          var c = r.value;
          if (buf && n + c.length <= buf.length) buf.set(c, n); else { if (buf) { chunks.push(buf.slice(0, n)); buf = null; } chunks.push(c); }
          n += c.length; count(c.length); return pump();
        });
      }
      return pump().then(function () {
        if (buf) return n === buf.length ? buf.buffer : buf.slice(0, n).buffer;
        var out = new Uint8Array(n), o = 0; chunks.forEach(function (c) { out.set(c, o); o += c.length; }); return out.buffer;
      });
    }
    // One file: the kept copy if there is one, otherwise the network, counted toward the progress line.
    function file(cache, url, expect, check, fresh) {
      function again() { return unkeep(url).then(function () { return file(cache, url, expect, check, true); }); }
      return (fresh ? Promise.resolve(null) : kept(cache, url)).then(function (res) {
        if (res) return res.arrayBuffer().then(function (b) {
          if (expect && b.byteLength !== expect) return again();        // a kept copy cut short is thrown away
          return b;
        }, again);                                                     // and so is one that cannot be read
        total += expect || 0; notify();
        return fetch(url).then(function (r) {
          if (!r.ok) throw err(r.status === 404 ? 'missing' : 'network', url + ' ' + r.status);
          if (!expect) { var len = +r.headers.get('content-length') || 0; total += len; }
          return readAll(r, expect, tick).catch(function (e) { throw e && e.code ? e : err('network', url); }).then(function (b) {
            if (expect && b.byteLength !== expect) throw err('damaged', url + ' is ' + b.byteLength + ' bytes, not ' + expect);
            return (check ? check(b) : Promise.resolve()).then(function () {
              if (!cache) return b;
              // kept by the page itself, unless the service worker has kept the same bytes under the same address already
              return kept(cache, url).then(function (there) {
                if (there) return b;
                var copy = new Response(b, { headers: { 'Content-Type': r.headers.get('content-type') || 'application/octet-stream', 'Content-Length': String(b.byteLength) } });
                return cache.put(url, copy).catch(function () {}).then(function () { return b; });   // a full disk is no reason to fail
              });
            });
          });
        }, function (e) { throw e && e.code ? e : err('network', url); });
      });
    }
    function sha256(want) {
      return function (b) {
        if (!want || !(window.crypto && crypto.subtle && crypto.subtle.digest)) return Promise.resolve();
        return crypto.subtle.digest('SHA-256', b).then(function (d) {
          var h = Array.prototype.map.call(new Uint8Array(d), function (x) { return ('0' + x.toString(16)).slice(-2); }).join('');
          if (h !== String(want).toLowerCase()) throw err('damaged', 'sha256 is ' + h);
        });
      };
    }
    function num(x) { return typeof x === 'number' && isFinite(x); }
    function okPart(u) {                               // a part may live on another origin, over https; a check on this machine may use its own ports
      return typeof u === 'string' && !!u && (/^https:\/\/[^\/]+\//.test(u) || (!/^[a-z][a-z0-9+.-]*:/i.test(u) && !/^\/\//.test(u)) || (onThisMachine && /^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?\//.test(u)));
    }
    function partsOf(V) { return Array.isArray(V.parts) ? V.parts : [{ url: V.url, bytes: V.bytes, sha256: V.sha256 }]; }
    function readManifest(text) {
      var m; try { m = JSON.parse(text); } catch (e) { throw err('damaged', 'manifest is not JSON'); }
      var v = m && m.vision, f = m && m.fusion, k = m && m.kinds, sp = m && m.species;
      if (!v || !f || !num(m.width) || !num(v.size) || !Array.isArray(v.mean) || !Array.isArray(v.std) || !(v.url || Array.isArray(v.parts))) throw err('unfit', 'manifest lacks a field');
      // a slot may come without a kinds head: then the kind is taken from the species answer, and the species are not optional
      if (k ? !(Array.isArray(k.labels) && k.url && num(f.t_kind)) : !sp) throw err('unfit', 'manifest lacks a field');
      if (k && k.labels.some(function (l) { return l !== 'none' && !EYES[l]; })) throw err('unfit', 'a kind this page does not know');
      if (sp && !(sp.url && sp.table && num(sp.count) && num(f.t_species) && num(f.alpha_prior) && (!k || num(f.w_kind)) && num(f.name_at) && num(f.offer_at))) throw err('unfit', 'species without their settings');
      // a trained head carries a bias for each row; a manifest may choose how the two heads are combined. Anything this build does not know is refused, not guessed at.
      if (k && k.bias !== undefined && k.bias !== null && !(Array.isArray(k.bias) && k.bias.length === k.labels.length && k.bias.every(num))) throw err('unfit', 'kinds.bias does not match the labels');
      if (f.rule !== undefined && f.rule !== 'product' && f.rule !== 'mix') throw err('unfit', 'a combination rule this page does not know');
      if (f.guard !== undefined && !(num(f.guard) && f.guard > 0)) throw err('unfit', 'fusion.guard is not a positive number');
      if (f.kind_at !== undefined && f.kind_at !== null && !num(f.kind_at)) throw err('unfit', 'fusion.kind_at is not a number');
      // a model in parts: every part with its length, the lengths adding up to the whole
      if (v.parts !== undefined) {
        var sum = 0;
        if (!Array.isArray(v.parts) || !v.parts.length || !num(v.bytes) || !v.parts.every(function (p) { sum += p && p.bytes; return p && okPart(p.url) && num(p.bytes) && p.bytes > 0 && (p.sha256 === undefined || typeof p.sha256 === 'string'); }) || sum !== v.bytes) throw err('unfit', 'the parts do not add up to the whole');
      }
      if (big ? !(num(v.bytes) && v.bytes > 0 && partsOf(v).every(function (p) { return okPart(p.url); })) : v.parts !== undefined) throw err('unfit', big ? 'the larger model without its length' : 'a model in parts in the pocket slot');
      return m;
    }
    function readTable(buf, count) {                   // rows: [scientific, English, kind, twelve monthly weights], or the same as objects
      var t, rows; try { t = JSON.parse(new TextDecoder('utf-8').decode(buf)); } catch (e) { throw err('damaged', 'species table is not JSON'); }
      rows = Array.isArray(t) ? t : t && t.species;
      if (!Array.isArray(rows) || rows.length !== count) throw err('unfit', 'species table has ' + (rows ? rows.length : 0) + ' rows, not ' + count);
      return rows.map(function (r) {
        var a = Array.isArray(r) ? r : [r.sci, r.en, r.kind || r.eyes, r.m], kind = EYES[a[2]] ? a[2] : 'other', m = Array.isArray(a[3]) && a[3].length === 12 ? a[3] : null;
        return { sci: clip(a[0], 80), en: clip(a[1], 60), kind: kind, m: m };
      });
    }
    function floats(buf, count) {                      // a trained head's biases for the species: little-endian float32, one for each row
      if (!buf || buf.byteLength !== count * 4) throw err('damaged', 'species biases of the wrong length');
      var dv = new DataView(buf), out = new Float64Array(count), i;
      for (i = 0; i < count; i++) out[i] = dv.getFloat32(i * 4, true);
      return out;
    }
    function slotOf(m, rows, sb) {                     // everything the scoring needs: the settings, the labels, the species table, the biases
      var has = {};
      if (rows) rows.forEach(function (r) { has[r.kind] = 1; });
      if (sb && (!rows || sb.length !== rows.length)) throw err('unfit', 'species biases do not match the table');
      if (!m.kinds && !rows) throw err('unfit', 'neither kinds nor species');
      // without a kinds head the labels are the kinds the table has, in the one fixed order
      return { f: m.fusion, head: !!m.kinds, labels: m.kinds ? m.kinds.labels : KIND_ORDER.filter(function (k) { return has[k]; }), table: rows, has: has,
        kb: m.kinds && m.kinds.bias ? Float64Array.from(m.kinds.bias) : null, sb: sb || null, prior: {} };
    }
    function prune(cache, v) {                         // older versions of this slot and of the runtime are let go
      if (!cache) return;
      cache.keys().then(function (keys) {
        keys.forEach(function (req) {
          var u; try { u = new URL(req.url); } catch (e) { return; }
          var q = /[?&]v=([^&]+)/.exec(u.search), here = u.href.split('?')[0];
          if (!q) return;
          if (here.indexOf(base) === 0 && here.slice(base.length).indexOf('/') < 0 && decodeURIComponent(q[1]) !== v) cache.delete(req);
          if (here.indexOf(abs(ORT.dir)) === 0 && decodeURIComponent(q[1]) !== ORT.v) cache.delete(req);
        });
      }).catch(function () {});
    }
    function stop(code, detail) {                      // the worker is gone or cannot be trusted: everything waiting hears of it
      var w = worker, p = pending; worker = null; pending = {};
      if (w) { w.onmessage = w.onerror = null; try { w.terminate(); } catch (e) {} }
      state = 'failed'; why = code; lastFail = code + (detail ? ': ' + detail : ''); loadP = null;
      Object.keys(p).forEach(function (id) { clearTimeout(p[id].timer); p[id].rej(err(code, detail)); });
    }
    function startWorker(init, transfer, sessionCode) {
      return new Promise(function (res, rej) {
        var w, hello = false, settled = false, timer;
        function no(code, detail) { if (settled) { stop(code, detail); return; } settled = true; clearTimeout(timer); stop(code, detail); rej(err(code, detail)); }
        try { w = new Worker('vendor/rec-worker.js?v=' + BUILD); } catch (e) { rej(err('browser', e && e.message)); return; }
        worker = w;
        timer = setTimeout(function () { no('slow', 'starting'); }, Math.max(watchMs, 60000) * (big ? 2 : 1));
        w.onerror = function (e) { if (e && e.preventDefault) e.preventDefault(); no(hello ? (big && !settled ? 'browser' : 'died') : 'network', e && e.message); };
        w.onmessage = function (ev) {
          var m = ev.data || {}, p;
          if (m.op === 'hello') { hello = true; return; }
          if (m.op === 'ready') { settled = true; clearTimeout(timer); info = { backend: m.backend, threads: m.threads, ms: m.ms }; res(); return; }
          if (m.op === 'fail' && !m.id) { no(m.stage === 'runtime' ? 'network' : m.stage === 'browser' ? 'browser' : m.stage === 'unfit' ? 'unfit' : m.stage === 'session' ? sessionCode : 'died', m.stage + ' ' + m.name + ' ' + m.message); return; }
          p = pending[m.id]; if (!p) return;
          delete pending[m.id]; clearTimeout(p.timer);
          if (m.op === 'done') p.res(m); else p.rej(err('photo', m.message));
        };
        w.postMessage(init, transfer);
      });
    }
    // The manifest: the network first, so that a new model is noticed; the kept copy where there is no network, where the server is
    // having a bad moment, where the answer breaks off, or where none comes in six seconds. The kept copy is the last resort, so it is
    // looked for more than once before the load is given up, and what was missing is written into the reason.
    function keptText(cache, url, detail) {
      var tries = 0;
      function look() {
        return (cache ? Promise.resolve(cache) : keepOpen()).then(function (c) { return kept(c, url); }).then(function (hit) { return hit ? hit.text() : null; }, function () { return null; }).then(function (text) {
          if (text) return text;
          if (++tries < 3) return new Promise(function (res) { setTimeout(res, 150 * tries); }).then(look);
          throw err('network', detail + (window.caches ? '; no kept copy found' : '; this browser keeps no copies'));
        });
      }
      return look();
    }
    function manifestText(cache) {
      var url = abs(manifestUrl), ctl = typeof AbortController === 'function' ? new AbortController() : null, late = false;
      var timer = ctl ? setTimeout(function () { kept(cache, url).then(function (hit) { if (hit) { late = true; try { ctl.abort(); } catch (e) {} } }); }, netWaitMs) : 0;
      return fetch(manifestUrl, { cache: 'no-cache', signal: ctl ? ctl.signal : undefined }).then(function (r) {
        clearTimeout(timer);
        if (r.status === 404) throw err('absent', manifestUrl);            // taken away on purpose, or never there
        if (!r.ok) return keptText(cache, url, manifestUrl + ' ' + r.status);           // a server having a bad moment
        return r.text().then(function (text) {
          if (cache) cache.put(url, new Response(text, { headers: { 'Content-Type': 'application/json' } })).catch(function () {});
          return text;
        }, function () { return keptText(cache, url, manifestUrl + ' broke off'); });
      }, function () { clearTimeout(timer); return keptText(cache, url, manifestUrl + (late ? ' did not answer in time' : '')); });
    }
    function adopt(text) { M = readManifest(text); ver = fingerprint(text); base = abs(manifestUrl).replace(/[^\/]*$/, ''); cur = null; }
    function u(rel) { return withV(abs(rel, base), ver); }

    // ---------- a model in parts (the larger model)
    // A part is kept under an address of this slot made from its checksum, so the same bytes are never fetched twice, wherever they came from.
    function partKey(p) { return base + 'part/' + (p.sha256 ? String(p.sha256).toLowerCase() : fingerprint(String(p.url))) + '?bytes=' + p.bytes; }
    function wholeKey(V) { return base + 'whole/' + String(V.sha256 || '').toLowerCase(); }
    function unkeepParts() {
      var V = M.vision; have = 'absent'; keptBytes = 0;
      return Promise.all(partsOf(V).map(function (p) { return unkeep(partKey(p)); }).concat([unkeep(wholeKey(V))]));
    }
    function staleParts(cache) {                       // parts of a model this slot no longer names
      if (!cache || !M) return;
      var now = {}; partsOf(M.vision).forEach(function (p) { now[partKey(p).split('?')[0]] = 1; }); now[wholeKey(M.vision)] = 1;
      cache.keys().then(function (keys) {
        keys.forEach(function (req) { var here = req.url.split('?')[0]; if ((here.indexOf(base + 'part/') === 0 || here.indexOf(base + 'whole/') === 0) && !now[here]) cache.delete(req); });
      }).catch(function () {});
    }
    function readInto(res, buf, at, n) {               // a kept part, straight into its place in the whole
      function wrong(len) { return err('damaged', 'a kept part is ' + len + ' bytes, not ' + n); }
      if (!res.body || !res.body.getReader) return res.arrayBuffer().then(function (b) { if (b.byteLength !== n) throw wrong(b.byteLength); buf.set(new Uint8Array(b), at); });
      var reader = res.body.getReader(), done = 0;
      function pump() {
        return reader.read().then(function (r) {
          if (r.done) { if (done !== n) throw wrong(done); return; }
          if (done + r.value.length > n) throw wrong(done + r.value.length);
          buf.set(r.value, at + done); done += r.value.length; return pump();
        });
      }
      return pump();
    }
    function joined(cache, V) {                        // the parts as they are kept, put together; the whole is verified the first time
      var buf, off = 0, i = 0, P = partsOf(V);
      try { buf = new Uint8Array(V.bytes); } catch (e) { return Promise.reject(err('browser', 'no room in memory for ' + V.bytes + ' bytes')); }
      function next() {
        if (i >= P.length) return Promise.resolve();
        var p = P[i++], at = off; off += p.bytes;
        return kept(cache, partKey(p)).then(function (res) {
          if (!res) { have = ''; throw err('missing', 'a part is no longer kept on this device'); }
          return readInto(res, buf, at, p.bytes).catch(function (e) { have = ''; return unkeep(partKey(p)).then(function () { throw e && e.code ? e : err('damaged', 'a kept part could not be read'); }); });
        }).then(next);
      }
      return next().then(function () {
        if (!V.sha256) return;
        return kept(cache, wholeKey(V)).then(function (ok) {
          if (ok) return;
          return sha256(V.sha256)(buf.buffer).then(function () { if (cache) return cache.put(wholeKey(V), new Response('verified')).catch(function () {}); },
            function (e) { return unkeepParts().then(function () { throw e; }); });      // every part passed and the whole does not: nothing of it can be trusted
        });
      }).then(function () { return buf.buffer; });
    }
    function room(need) {                              // is there room to keep it? Where the browser will not say, the download finds out
      try {
        if (navigator.storage && navigator.storage.estimate) return navigator.storage.estimate().then(function (e) {
          if (e && num(e.quota) && num(e.usage) && e.quota - e.usage < need) throw err('room', 'room for ' + Math.max(0, e.quota - e.usage) + ' bytes, and ' + need + ' are needed');
        }, function () {});
      } catch (e) {}
      return Promise.resolve();
    }
    // What of the larger model is on this device: 'none' (there is no such model, or it cannot be used here), 'absent', 'partial', 'getting', 'kept'.
    // The manifest is asked for the first time this is called, and never before.
    function survey(fresh) {
      if (cannot || gone) return Promise.resolve('none');
      if (!fresh && getP) return Promise.resolve('getting');
      if (!fresh && have) return Promise.resolve(have);
      if (!surveyP) surveyP = keepOpen().then(function (cache) {
        return (M ? Promise.resolve() : manifestText(cache).then(adopt)).then(function () {
          var P = partsOf(M.vision);
          return Promise.all(P.map(function (p) { return kept(cache, partKey(p)); })).then(function (hits) {
            var n = 0; keptBytes = 0; hits.forEach(function (h, i) { if (h) { keptBytes += P[i].bytes; n++; } });
            have = n === P.length ? 'kept' : n ? 'partial' : 'absent';
            if (have !== 'kept') staleParts(cache);
            return have;
          });
        });
      }).then(function (h) { surveyP = null; return h; }, function (e) {
        surveyP = null;
        if (e && e.code === 'absent') gone = true; else lastFail = ((e && e.code) || 'died') + (e && e.detail ? ': ' + e.detail : '');
        return 'none';
      });
      return surveyP.then(function (h) { return h !== 'none' && getP ? 'getting' : h; });
    }
    // Fetch what is missing, one part after another, each verified and kept before the next is asked for; then start the encoder once, which
    // verifies the whole and shows that it runs on this device. Stopped by halt(); a later call carries on from the parts already kept.
    function get() {
      if (cannot) return Promise.reject(err(cannot));
      if (getP) return getP;
      var ctl = typeof AbortController === 'function' ? new AbortController() : null, store = null;
      function halted() { return !!(ctl && ctl.signal.aborted); }
      getCtl = ctl; getFail = ''; partGot = 0;
      var p = survey(true).then(function (h) {
        if (h === 'none') throw err(gone ? 'absent' : 'network', manifestUrl);
        return keepOpen();
      }).then(function (cache) {
        if (!cache) throw err('keep', 'this browser gave no store to keep it in');
        store = cache;
        var P = partsOf(M.vision), i = 0;
        function next() {
          if (i >= P.length) return Promise.resolve();
          var part = P[i++], key = partKey(part);
          return kept(cache, key).then(function (hit) {
            if (hit) return;                           // already here: not fetched again
            if (halted()) throw err('stopped');
            partGot = 0; notify();
            return fetch(abs(part.url, base), { mode: 'cors', credentials: 'omit', cache: 'no-store', referrerPolicy: 'no-referrer', signal: ctl ? ctl.signal : undefined }).then(function (r) {
              if (!r.ok) throw err(r.status === 404 ? 'missing' : 'network', part.url + ' ' + r.status);
              return readAll(r, part.bytes, function (n) { partGot += n; notify(); });
            }).then(function (b) {
              if (b.byteLength !== part.bytes) throw err('damaged', part.url + ' is ' + b.byteLength + ' bytes, not ' + part.bytes);
              return sha256(part.sha256)(b).then(function () {
                return cache.put(key, new Response(b, { headers: { 'Content-Type': 'application/octet-stream', 'Content-Length': String(b.byteLength) } })).catch(function (e) {
                  throw err(e && e.name === 'QuotaExceededError' ? 'room' : 'keep', e && e.message);
                });
              });
            }).then(function () { keptBytes += part.bytes; partGot = 0; notify(); }, function (e) {
              partGot = 0;
              throw halted() ? err('stopped') : e && e.code ? e : err('network', part.url + ' ' + ((e && e.message) || ''));
            });
          }).then(next);
        }
        return room(Math.max(0, M.vision.bytes - keptBytes)).then(next);
      }).then(function () {
        have = 'kept'; staleParts(store); notify();
        return ready();
      }).then(function () { getP = null; getCtl = null; diag('large-kept', M.id + ' ' + M.vision.bytes); notify(); }, function (e) {
        getP = null; getCtl = null;
        if (!e || !e.code) e = err('died', e && e.message);
        if (have !== 'kept') have = keptBytes ? 'partial' : 'absent';
        getFail = e.code + (e.detail ? ': ' + e.detail : ''); diag('large-get', getFail.slice(0, 160)); notify();
        throw e;
      });
      getP = p; p.catch(function () {});
      return p;
    }
    function halt() { if (getCtl) try { getCtl.abort(); } catch (e) {} }
    function rest() {                                  // nothing has needed the larger model for a minute: its worker, and the memory it holds, are let go
      clearTimeout(idleTimer); idleTimer = 0;
      if (!worker || state !== 'ready' || Object.keys(pending).length) return;
      var w = worker; worker = null; w.onmessage = w.onerror = null; try { w.terminate(); } catch (e) {}
      state = 'idle'; loadP = null; diag('large-rest', '');
    }
    function tire() { if (!big) return; clearTimeout(idleTimer); idleTimer = setTimeout(rest, idleMs); }
    function forget() {                                // off this device: the parts, the rows and the table, and the worker
      halt();
      return (getP ? getP.catch(function () {}) : Promise.resolve()).then(function () {
        var w = worker, p = pending; worker = null; pending = {}; clearTimeout(idleTimer);
        if (w) { w.onmessage = w.onerror = null; try { w.terminate(); } catch (e) {} }
        Object.keys(p).forEach(function (id) { clearTimeout(p[id].timer); p[id].rej(err('died', 'deleted')); });
        state = cannot ? 'failed' : 'idle'; why = cannot; loadP = null;
        return keepOpen();
      }).then(function (cache) {
        if (!cache || !base) return;
        return cache.keys().then(function (keys) { return Promise.all(keys.map(function (req) { return req.url.split('?')[0].indexOf(base) === 0 ? cache.delete(req) : null; })); });
      }).catch(function () {}).then(function () { have = M ? 'absent' : ''; keptBytes = 0; partGot = 0; getFail = ''; diag('large-deleted', ''); notify(); });
    }

    function load() {
      var t0 = performance.now(), cacheRef = null, fromKeep = { model: false };
      state = 'loading'; why = ''; got = 0; total = 0;
      return keepOpen().then(function (cache) {
        cacheRef = cache;
        if (big && M) return null;                     // the larger model's worker is started again and again; its manifest is read once
        return manifestText(cache).then(adopt);
      }).then(function () {
        var V = M.vision, nK = M.kinds ? M.kinds.labels.length : 0, nS = M.species ? M.species.count : 0, c = cacheRef;
        var inParts = big || !!V.parts, modelUrl = inParts ? '' : u(V.url);
        return (inParts ? Promise.resolve(true) : kept(c, modelUrl)).then(function (hit) {
          fromKeep.model = !!hit;
          return Promise.all([
            file(c, withV(abs(ORT.dir + ORT.wasm), ORT.v), ORT.wasmBytes),
            inParts ? joined(c, V) : file(c, modelUrl, num(V.bytes) ? V.bytes : 0, sha256(V.sha256)),
            M.kinds ? file(c, u(M.kinds.url), nK * M.width * 2) : null,
            M.species ? file(c, u(M.species.url), nS * M.width * 2) : null,
            M.species ? file(c, u(M.species.table), 0) : null,
            M.species && M.species.bias_url ? file(c, u(M.species.bias_url), nS * 4) : null
          ]);
        }).then(function (b) {
          cur = slotOf(M, M.species ? readTable(b[4], nS) : null, b[5] ? floats(b[5], nS) : null);
          total = got;                                 // the downloads are over; what remains is starting the encoder
          notify();
          var init = { op: 'init', ep: ORT.ep, ort: { js: withV(abs(ORT.dir + ORT.js), ORT.v), mjs: withV(abs(ORT.dir + ORT.mjs), ORT.v), wasm: withV(abs(ORT.dir + ORT.wasm), ORT.v) },
            wasmBinary: b[0], model: b[1], vision: { input: V.input || 'pixel_values', output: V.output || 'image_embeds', size: V.size, mean: V.mean, std: V.std, resize: V.resize, crop: V.crop || 'center' },
            width: M.width, kinds: b[2], nKinds: nK, species: b[3], nSpecies: nS };
          // a model in parts has passed its checksums by now: if the encoder will not take it, the fault is not in the bytes, and they are kept
          return startWorker(init, [b[0], b[1]].concat(b[2] ? [b[2]] : [], b[3] ? [b[3]] : []), inParts && V.sha256 ? 'browser' : 'damaged').catch(function (e) {
            // a kept model that will not start is thrown away, so the next try fetches it afresh
            if (e.code === 'damaged' && c) return (inParts ? unkeepParts() : unkeep(modelUrl)).then(function () { throw e; });
            throw e;
          });
        });
      }).then(function () {
        state = 'ready'; loadMs = performance.now() - t0; if (!big) prune(cacheRef, ver);
        tire();
        diag(big ? 'large-ready' : 'pocket-ready', M.id + ' ' + Math.round(loadMs) + 'ms ' + (fromKeep.model ? 'kept' : 'fetched'));
      }, function (e) {
        if (!e || !e.code) e = err('died', e && e.message);
        if (state !== 'failed' || !why) { state = 'failed'; why = e.code; lastFail = e.code + (e.detail ? ': ' + e.detail : ''); }
        loadP = null;
        diag(big ? 'large-failed' : 'pocket-failed', lastFail.slice(0, 160));
        throw e;
      });
    }
    function ready() {
      if (cannot) return Promise.reject(err(cannot));
      if (state === 'ready' && worker) return Promise.resolve();
      if (!loadP) { loadP = load(); loadP.catch(function () {}); }
      return loadP;
    }

    // ---------- from the encoder's numbers to a name
    function softmax(z) {
      var n = z.length, out = new Float64Array(n), m = -Infinity, s = 0, i;
      for (i = 0; i < n; i++) if (z[i] > m) m = z[i];
      for (i = 0; i < n; i++) { out[i] = Math.exp(z[i] - m); s += out[i]; }
      for (i = 0; i < n; i++) out[i] /= s;
      return out;
    }
    function priorFor(c, month) {                      // log of each species' share of this month's records, with a floor so that an unrecorded month is unlikely and not impossible
      var key = (typeof month === 'number' && month === Math.floor(month) && month >= 0 && month < 12) ? month : 'none';   // no month known: no prior
      if (c.prior[key]) return c.prior[key];
      var t = c.table, n = t.length, out = new Float64Array(n), sum = 0, i, floor = num(c.f.prior_floor) ? c.f.prior_floor : 1e-6;
      if (key !== 'none') {
        for (i = 0; i < n; i++) sum += t[i].m ? Math.max(0, +t[i].m[key] || 0) : 0;
        if (sum > 0) for (i = 0; i < n; i++) out[i] = Math.log(Math.max(t[i].m ? Math.max(0, +t[i].m[key] || 0) / sum : 0, floor));
      }
      c.prior[key] = out; return out;
    }
    // From the two heads' scores to a kind of eye, a name and offers. tools/fusion/fuse.py is the same arithmetic in numpy, line for line,
    // and tools/fusion/parity.py holds the two to the same answers; a change here is a change there.
    //   kd, sd: row . e for each kind row and each species row, e being the unit image vector. The rows are used as they are: a trained
    //   head's rows are weights, not unit vectors, and it adds a bias to each score.
    //   A slot without a kinds head (the larger model): kd is not used, and a kind's score is its share of the species answer.
    function fuseWith(c, kd, sd, month) {
      var f = c.f, labels = c.labels, table = c.table, n = labels.length, z, i, p = null, q = {}, s = null, order = [], comb, kinds = [], species = [];
      if (c.head) {
        z = new Float64Array(n);
        for (i = 0; i < n; i++) z[i] = f.t_kind * kd[i] + (c.kb ? c.kb[i] : 0);
        p = softmax(z);
      }
      if (table && sd) {
        var pr = f.alpha_prior ? priorFor(c, month) : null, zs = new Float64Array(table.length);
        for (i = 0; i < zs.length; i++) zs[i] = f.t_species * sd[i] + (c.sb ? c.sb[i] : 0) + (pr ? f.alpha_prior * pr[i] : 0);
        s = softmax(zs);
        for (i = 0; i < s.length; i++) { q[table[i].kind] = (q[table[i].kind] || 0) + s[i]; order.push(i); }
        order.sort(function (a, b) { return s[b] - s[a]; });
        species = order.slice(0, 5).map(function (j) { return { sci: table[j].sci, en: table[j].en, p: s[j], kind: table[j].kind }; });
      }
      // a kind the species list can speak for is scored by both heads; one it has no rows for (nothing alive, a person) by the kinds alone
      function speaks(i) { return !!(s && c.has[labels[i]]); }
      if (!c.head) {
        if (!s) throw err('unfit', 'a slot without a kinds head was given no species scores');
        comb = new Float64Array(n);
        for (i = 0; i < n; i++) comb[i] = q[labels[i]] || 0;
      } else if (f.rule === 'mix') {
        // mixing: the species head re-divides the share the kinds head gave to the kinds it can speak for, and moves at most 1 - w_kind of it
        var A = 0, tot = 0; comb = new Float64Array(n);
        for (i = 0; i < n; i++) if (speaks(i)) A += p[i];
        for (i = 0; i < n; i++) { comb[i] = speaks(i) ? f.w_kind * p[i] + (1 - f.w_kind) * A * (q[labels[i]] || 0) : p[i]; tot += comb[i]; }
        if (tot > 0) for (i = 0; i < n; i++) comb[i] /= tot; else comb = p;
      } else {
        // the product (the rule of build 6): a weighted sum of logarithms, with a guard under each so that a zero is unlikely and not impossible
        var g = num(f.guard) ? f.guard : EPS, score = new Float64Array(n);
        for (i = 0; i < n; i++) score[i] = speaks(i) ? f.w_kind * Math.log(Math.max(p[i], g)) + (1 - f.w_kind) * Math.log(Math.max(q[labels[i]] || 0, g)) : Math.log(Math.max(p[i], g));
        comb = softmax(score);
      }
      for (i = 0; i < n; i++) kinds.push({ key: labels[i], p: comb[i], head: p ? p[i] : null, list: speaks(i) ? (q[labels[i]] || 0) : null });
      kinds.sort(function (a, b) { return b.p - a.p; });
      // Not sure is an answer. Under fusion.kind_at no kind is asserted and no species named: the three likeliest kinds of living thing are
      // offered instead (the species offers are worked out as ever). Without fusion.kind_at every answer is asserted, as before build 8.
      var kind = kinds[0].key, named = null, offers = [], sure = !(num(f.kind_at) && kinds[0].p < f.kind_at), kindOffers = [];
      if (!sure) kindOffers = kinds.filter(function (k) { return k.key !== 'none'; }).slice(0, 3).map(function (k) { return k.key; });
      if (species.length && kind !== 'none' && kind !== 'person') {
        if (sure && species[0].p >= f.name_at && species[0].kind === kind) named = species[0];
        else {
          // the three likeliest are kept as offers. They are taken from the kind that won, so that a flower is not offered a turtle;
          // a manifest that sets fusion.offer_any_kind takes the three likeliest of any kind.
          var three = (f.offer_any_kind ? order : order.filter(function (j) { return table[j].kind === kind; })).slice(0, 3).map(function (j) { return { sci: table[j].sci, en: table[j].en, p: s[j], kind: table[j].kind }; });
          if (three.reduce(function (a, r) { return a + r.p; }, 0) >= f.offer_at) offers = three;
        }
      }
      return { kind: kind, kindP: kinds[0].p, sure: sure, kinds: kinds, kindOffers: kindOffers, species: species, named: named, offers: offers };
    }
    // The photo's pixels for the encoder. The canvas the page shows was brought down to 1280 by the browser's own scaling, which differs
    // from one browser to the next; so a photo chosen as a file is read again at its full size where a canvas can hold it (16 million
    // pixels is the smallest limit among phones), and the one resize that follows is Pillow's. A camera frame is used as it is.
    function pixels(canvas, file) {
      function shown() { var d = canvas.getContext('2d').getImageData(0, 0, canvas.width, canvas.height); return { buf: d.data.buffer, w: d.width, h: d.height, full: false }; }
      if (!file || typeof createImageBitmap !== 'function') return Promise.resolve().then(shown);
      return createImageBitmap(file).then(function (bmp) {
        var w = bmp.width, h = bmp.height, c, x, d;
        if (Math.max(w, h) <= Math.max(canvas.width, canvas.height) || w * h > 16e6) { if (bmp.close) bmp.close(); return shown(); }
        c = document.createElement('canvas'); c.width = w; c.height = h; x = c.getContext('2d', { willReadFrequently: true });
        x.drawImage(bmp, 0, 0); if (bmp.close) bmp.close();
        d = x.getImageData(0, 0, w, h); c.width = c.height = 1;
        return { buf: d.data.buffer, w: w, h: h, full: true };
      }).catch(shown);
    }
    function recognize(canvas, file) {
      var tAsk = performance.now(), wasReady = state === 'ready', shot = pixels(canvas, file), mine = ++asked;   // read now: the canvas may show something else by the time the encoder is ready
      shot.catch(function () {});
      function run() {
        if (big && mine !== asked) return Promise.reject(err('photo', 'a newer photo is waiting'));   // only the photo in hand is worth the seconds
        clearTimeout(idleTimer);
        return ready().then(function () { return shot.catch(function (e) { throw err('photo', e && e.message); }); }).then(function (px) {
          var tRun = performance.now();
          return new Promise(function (res, rej) {
            var id = nextId++;
            pending[id] = { res: res, rej: rej, timer: setTimeout(function () { if (pending[id]) stop('slow', 'no answer in ' + watchMs + ' ms'); }, watchMs) };
            worker.postMessage({ op: 'run', id: id, rgba: px.buf, w: px.w, h: px.h, wantPre: !!api.wantPre }, [px.buf]);
          }).then(function (m) {
            // far from the species list's place: a slot with a kinds head leaves the list out; one without still takes the kind from it, with no month's weight
            var t = performance.now(), month = new Date().getMonth(), away = pocket.local === false, local = !away && !!cur.table;
            var r = fuseWith(cur, m.kinds, local || !cur.head ? m.species : null, local ? month : null);
            r.month = month; r.local = local;                // local: the species list of this slot's region was consulted for a name
            r.kindAt = num(cur.f.kind_at) ? cur.f.kind_at : null;
            r.ms = { load: wasReady ? 0 : Math.round(tRun - tAsk), pre: Math.round(m.ms.pre), run: Math.round(m.ms.run), post: Math.round((m.ms.post + performance.now() - t) * 10) / 10 };
            r.backend = info.backend; r.model = M.id; r.at = Date.now(); r.from = px.w + 'x' + px.h;
            last = r; if (api.wantPre) { api.lastEmb = m.emb; api.lastPre = m.pre; api.lastDots = { kinds: m.kinds, species: m.species }; }
            return r;
          });
        });
      }
      if (!big) return run();
      var p = queue.then(run, run); queue = p.catch(function () {}).then(tire); return p;     // one photo at a time through the larger model
    }
    function mb(n) { return Math.max(0, Math.round(n / 1e6)); }
    function line() {
      if (big) return !(getP && M) ? 'Looking more closely.' : have === 'kept' ? 'Checking the larger model.' : 'Getting the larger model: ' + mb(keptBytes + partGot) + ' of ' + Math.max(1, mb(M.vision.bytes)) + ' MB.';
      if (state === 'loading' && total > got) return 'Getting the recognizer: ' + mb(got) + ' of ' + Math.max(1, mb(total)) + ' MB.';
      return 'Looking at what it is.';
    }
    function warm() {                                  // once the opening screen is up and the page has nothing else to do
      if (big || cannot || (navigator.connection && navigator.connection.saveData)) return;
      function go() { if (state === 'idle') ready().catch(function () {}); }
      function soon() { if (window.requestIdleCallback) requestIdleCallback(go, { timeout: 4000 }); else setTimeout(go, 1200); }
      if (document.readyState === 'complete') soon(); else window.addEventListener('load', soon);
    }
    api = {
      usable: function () { return !cannot; }, whyNot: function () { return SAY[cannot] || ''; },
      recognize: recognize, line: line, warm: warm, ready: ready, fuse: function (kd, sd, month) { return fuseWith(cur, kd, sd, month); },
      fetching: function () { return state === 'loading' && total > got; },      // the first download is under way
      place: function () { return (M && M.species && typeof M.species.place === 'string' && clip(M.species.place, 60)) || 'Gainesville, Florida'; },   // where the species list is from
      listed: function () { return !!(cur && cur.table); },
      progress: function (fn) { onProgress = fn; },
      // the larger model: what of it is here, fetching it, stopping, deleting; its size and, where the manifest gives one, a measured time for a photo
      survey: survey, get: get, halt: halt, forget: forget, say: function (code) { return SAY[code] || SAY.died; },
      has: function () { return getP ? 'getting' : have; },
      broken: function () { return state === 'failed' && (why === 'browser' || why === 'unfit'); },   // it has shown that it cannot run here: not tried again for every photo
      size: function () { return M ? { bytes: M.vision.bytes || 0, kept: keptBytes + partGot, mb: Math.max(1, mb(M.vision.bytes || 0)), keptMb: mb(keptBytes + partGot), seconds: M.seconds_a_photo || null } : null; },
      offers: [], kindOffers: [], file: null, local: true, wantPre: false, lastEmb: null, lastPre: null, lastDots: null,
      about: function () { return { state: state, why: why, fail: lastFail, model: M ? M.id : '', rule: M ? (M.fusion.rule || 'product') : '', trained: !!(cur && (cur.kb || cur.sb)), backend: info.backend, threads: info.threads, loadMs: Math.round(loadMs), start: info.ms || null, last: last, got: got, total: total, slot: manifestUrl,
        have: getP ? 'getting' : have, keptBytes: keptBytes + partGot, bytes: M && M.vision.bytes || 0, getFail: getFail }; },
      test: { kill: function (how) { if (worker) worker.postMessage({ op: 'die', how: how }); }, watch: function (ms) { watchMs = ms; }, forget: function () { stop('died', 'forgotten by a check'); state = 'idle'; why = ''; },
        idle: function (ms) { idleMs = ms; tire(); }, netWait: function (ms) { netWaitMs = ms; }, running: function () { return !!worker; },
        // the scoring with settings given by a check, through the same readers as a real slot (tools/fusion/parity.py)
        world: function (m, rows, sb) { worlds.push(slotOf(readManifest(JSON.stringify(m)), rows ? readTable(new TextEncoder().encode(JSON.stringify({ species: rows })).buffer, rows.length) : null, sb ? Float64Array.from(sb) : null)); return worlds.length - 1; },
        fuseIn: function (w, kd, sd, month) { return fuseWith(worlds[w], kd, sd, month); } }
    };
    return api;
  }
  var pocket = recognizer({ slot: (/[?&]rec=([A-Za-z0-9_.\/-]+)/.exec(location.search || '') || [0, 'models/pocket'])[1] });
  // The larger model's slot. A check on this machine may name another slot, or switch it off; a link to the public page may not.
  var large = recognizer({ big: true, slot: ((onThisMachine ? /[?&]big=([A-Za-z0-9_.\/-]+)/.exec(location.search || '') : null) || [0, 'models/naturalist'])[1] });

  // ---------- the species service (the naturalist): a larger model on a server, asked only with the person's say-so
  // Where it lives is told by a small file at the site's root, service.json, fetched only when it is first needed:
  //   {"api": "gradio", "call": "https://<space>.hf.space/gradio_api/call/identify", "region": "us-fl-alachua", "model": "bioclip2-l14",
  //    "health": "<an address that answers {"ready": true}>" (optional), "kind_at": 0.9, "name_at": 0.5, "top": 5, "wake_s": 90, "answer_s": 60}
  // No such file: the feature does not exist, and nothing on the page mentions it. Nothing is sent before the person has said yes.
  // The call is Gradio's two steps: POST <call> {"data": [photo as base64 JPEG, month 1-12, region or "", top]} -> {"event_id"};
  // GET <call>/<event_id> is a stream of events, and the one named "complete" carries [answer].
  var naturalist = (function () {
    var KEY = 'seenback.service.v1', mem = '', cfg = null, cfgP = null, known = false;
    var local = /^(localhost|127\.0\.0\.1)$/.test(location.hostname);
    var asked = local ? /[?&]svc=(off|[A-Za-z0-9_.\/-]+\.json)/.exec(location.search || '') : null;   // a check on this machine may name another file; a link to the public page may not
    var T = { wake: 90000, answer: 60000, post: 20000, poll: 3000 };
    function num(x) { return typeof x === 'number' && isFinite(x); }
    function okUrl(u) { return typeof u === 'string' && (/^https:\/\/[^\/]+\//.test(u) || (local && /^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?\//.test(u))); }
    function readConfig(j) {
      if (!j || typeof j !== 'object' || j.api !== 'gradio' || !okUrl(j.call) || (j.health !== undefined && !okUrl(j.health))) return null;   // an arrangement this build does not know is as good as none
      var host = ''; try { host = new URL(j.call).host; } catch (e) { return null; }
      if (num(j.wake_s)) T.wake = j.wake_s * 1000;
      if (num(j.answer_s)) T.answer = j.answer_s * 1000;
      return { call: j.call.replace(/\/+$/, ''), health: j.health || '', region: typeof j.region === 'string' ? j.region : '', model: clip(j.model, 60), host: host,
        where: /(^|\.)hf\.space$|(^|\.)huggingface\.co$/.test(host) ? 'hosted by Hugging Face' : 'at ' + host,
        kindAt: num(j.kind_at) ? j.kind_at : null, nameAt: num(j.name_at) ? j.name_at : 0, top: num(j.top) ? Math.max(1, Math.min(10, Math.round(j.top))) : 5 };
    }
    function config() {                                // resolves with the service's particulars, or null where there is none
      if (inViewer || (asked && asked[1] === 'off')) return Promise.resolve(null);
      if (known) return Promise.resolve(cfg);
      if (!cfgP) cfgP = fetch(asked ? asked[1] : 'service.json', { cache: 'no-cache', credentials: 'omit' }).then(function (r) {
        if (r.status === 404) { known = true; return null; }               // no such file: there is no service
        if (!r.ok) throw new Error('service.json ' + r.status);
        return r.json().then(function (j) { cfg = readConfig(j); known = true; return cfg; });
      }).catch(function () { cfgP = null; return null; });                  // no network just now, or not JSON: look again another time
      return cfgP;
    }
    function choice() { try { var v = localStorage.getItem(KEY); return v === 'yes' || v === 'no' ? v : ''; } catch (e) { return mem; } }
    function setChoice(v) { mem = v === 'yes' || v === 'no' ? v : ''; try { if (mem) localStorage.setItem(KEY, mem); else localStorage.removeItem(KEY); } catch (e) {} }
    function fail(code, detail) { var e = new Error(code); e.code = code; e.detail = String(detail || '').slice(0, 120); return e; }
    // What leaves the device: the photo with its longest side at most 512, as a JPEG under 1 MB. Nothing else about the photo or the person.
    function jpeg(canvas) {
      var k = Math.min(1, 512 / Math.max(canvas.width, canvas.height)), c = makeCanvas(canvas.width * k, canvas.height * k), x = c.getContext('2d'), q = [.85, .7, .5, .3], i, url = '';
      x.imageSmoothingQuality = 'high'; x.drawImage(canvas, 0, 0, c.width, c.height);
      for (i = 0; i < q.length; i++) { url = c.toDataURL('image/jpeg', q[i]); if (url.length * .75 < 1e6) break; }
      c.width = c.height = 1;
      if (url.indexOf('data:image/jpeg;base64,') !== 0 || url.length * .75 >= 1e6) throw fail('photo', 'not a small JPEG');
      return url.slice(23);
    }
    function clean(out) {                              // the answer, with nothing taken on trust
      if (typeof out === 'string') { try { out = JSON.parse(out); } catch (e) { out = null; } }
      if (!out || typeof out !== 'object' || !Array.isArray(out.species)) throw fail(out && (out.error || out.refused) ? 'refused' : 'garbled', out && (out.error || out.refused));
      var species = out.species.slice(0, 10).map(function (s) {
        return s && typeof s === 'object' && num(s.p) ? { sci: clip(s.sci, 80), en: clip(s.en, 60), kind: EYES[s.eyes] ? s.eyes : 'other', p: Math.max(0, Math.min(1, s.p)) } : null;
      }).filter(function (s) { return s && (s.sci || s.en); });
      var kinds = (Array.isArray(out.kinds) ? out.kinds : []).map(function (k) { return k && typeof k === 'object' && num(k.p) && (EYES[k.key] || k.key === 'none') ? { key: k.key, p: Math.max(0, Math.min(1, k.p)) } : null; }).filter(Boolean);
      species.sort(function (a, b) { return b.p - a.p; }); kinds.sort(function (a, b) { return b.p - a.p; });
      return { species: species, kinds: kinds, region: typeof out.region === 'string' ? out.region : '', model: clip(out.model, 60), ms: num(out.ms) ? out.ms : 0 };
    }
    function opts(signal, more) {                      // no cookies, no address of the page it came from
      var o = { mode: 'cors', credentials: 'omit', cache: 'no-store', referrerPolicy: 'no-referrer', signal: signal }, k;
      for (k in more) o[k] = more[k];
      return o;
    }
    function listen(url, signal) {                     // the stream of events for one question, until the one that completes it
      return fetch(url, opts(signal, { headers: { Accept: 'text/event-stream' } })).then(function (r) {
        if (!r.ok) throw fail('failed', 'GET ' + r.status);
        var dec = new TextDecoder('utf-8'), buf = '', found = null;
        function take(final) {
          var parts = buf.split(/\r?\n\r?\n/), i, ev, data;
          buf = final ? '' : parts.pop();
          for (i = 0; i < parts.length && !found; i++) {
            ev = (/^event:\s*(.*)$/m.exec(parts[i]) || [])[1]; data = parts[i].split(/\r?\n/).filter(function (l) { return /^data:/.test(l); }).map(function (l) { return l.replace(/^data:\s?/, ''); }).join('\n');
            if (ev === 'complete') found = { data: data }; else if (ev === 'error') found = { error: data };
          }
          return found;
        }
        function finish() {
          if (!found) throw fail('garbled', 'the stream ended with no answer');
          if (found.error !== undefined) throw fail('failed', found.error);
          var j; try { j = JSON.parse(found.data); } catch (e) { throw fail('garbled', 'the answer is not JSON'); }
          return clean(Array.isArray(j) ? j[0] : j);
        }
        if (!r.body || !r.body.getReader) return r.text().then(function (t) { buf = t; take(true); return finish(); });
        var reader = r.body.getReader();
        function pump() {
          return reader.read().then(function (x) {
            if (x.value) buf += dec.decode(x.value, { stream: true });
            if (take(x.done)) { try { reader.cancel(); } catch (e) {} return finish(); }
            if (x.done) return finish();
            return pump();
          });
        }
        return pump();
      });
    }
    // One question. say('asking' | 'waking') tells the page what to show. Returns { promise, cancel }.
    function ask(canvas, o, say) {
      var ctl = typeof AbortController === 'function' ? new AbortController() : null, signal = ctl ? ctl.signal : undefined, t0 = performance.now(), tries = 0, over = false, net = false, timers = [];
      function left() { return T.wake - (performance.now() - t0); }
      function wait(ms) { return new Promise(function (res) { timers.push(setTimeout(res, ms)); }); }
      function within(p, ms, code) {                   // p, or a failure once ms have passed
        return new Promise(function (res, rej) { var t = setTimeout(function () { rej(fail(code)); }, ms); timers.push(t); p.then(function (v) { clearTimeout(t); res(v); }, function (e) { clearTimeout(t); rej(e); }); });
      }
      // "Waking up" is said only where it is the likely truth: the service did not answer, and this site itself can still be reached.
      // (A request the service worker leaves alone, so that a kept copy cannot answer for a network that is gone.)
      function reachable() {
        if (net) return Promise.resolve(true);
        return within(fetch(location.href.split('#')[0], { method: 'HEAD', cache: 'no-store', credentials: 'omit' }).then(function (r) { net = r.ok; return net; }), 8000, 'offline').catch(function () { return false; });
      }
      function sayWaking() { return reachable().then(function (yes) { if (over) throw fail('cancelled'); if (!yes) throw fail('offline', 'this site cannot be reached either'); say('waking'); }); }
      function awake() {                               // where the service names an address that says whether it is ready, that is asked first
        if (!cfg.health) return Promise.resolve();
        return within(fetch(cfg.health, opts(signal)).then(function (r) { return r.ok ? r.json() : null; }), T.post, 'asleep').catch(function () { return null; }).then(function (h) {
          if (over) throw fail('cancelled');
          if (h && h.ready !== false && h.ok !== false) return;
          if (left() <= 0) throw fail('asleep', 'not ready in time');
          return (h ? Promise.resolve(say('waking')) : sayWaking()).then(function () { return wait(Math.min(T.poll, Math.max(200, left()))); }).then(awake);
        });
      }
      function post(body) {
        tries++; if (tries === 1) say('asking');
        return within(fetch(cfg.call, opts(signal, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: body })).then(function (r) {
          if (!r.ok) throw fail(r.status === 429 ? 'busy' : (r.status >= 500 || r.status === 404) ? 'asleep' : 'refused', 'POST ' + r.status);
          return r.json().catch(function () { throw fail('garbled', 'no event id'); });
        }, function (e) { throw e && e.code ? e : fail(over ? 'cancelled' : 'asleep', e && e.message); }), T.post, 'asleep').then(function (j) {
          var id = j && j.event_id;
          if (typeof id !== 'string' || !/^[A-Za-z0-9_.-]{1,120}$/.test(id)) throw fail('garbled', 'no event id');
          say('asking');
          return within(listen(cfg.call + '/' + id, signal), T.answer, 'slow');
        }, function (e) {
          // no answer at the door: a server that sleeps when nobody calls takes a while to wake. Try again, less and less often, for as long as the wait allows.
          if (e.code !== 'asleep' || over || left() <= 0) throw e;
          return sayWaking().then(function () { return wait(Math.min(T.poll * Math.min(tries, 5), Math.max(200, left()))); }).then(function () { if (over) throw fail('cancelled'); return awake(); }).then(function () { return post(body); });
        });
      }
      var promise = config().then(function (c) {
        if (!c) throw fail('absent');
        if (navigator.onLine === false) throw fail('offline');
        var body = JSON.stringify({ data: [jpeg(canvas), o.month, o.local ? c.region : '', c.top] });
        return awake().then(function () { return post(body); });
      });
      function end() { over = true; timers.forEach(clearTimeout); }
      promise.then(end, function () { end(); if (ctl) try { ctl.abort(); } catch (e) {} });
      return { promise: promise, cancel: function () { end(); if (ctl) try { ctl.abort(); } catch (e) {} } };
    }
    return { config: config, choice: choice, setChoice: setChoice, ask: ask, cfg: function () { return cfg; },
      test: { times: function (t) { for (var k in t) T[k] = t[k]; return T; }, read: function (j) { return readConfig(j); } } };
  })();

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
    $('claimSub').textContent = (sub ? sub + ' ' : '') + (kinds.length ? 'Choose one below, or type' : 'Type') + ' the kind of animal or plant, such as cat, heron or oak.'; $('claimName').value = ''; $('claimNote').textContent = ''; show('claimOtherRow', false);
    kinds.forEach(function (key) {
      var name = key === 'person' ? 'A person' : handName(key), b = el('button', 'pill ghost', name); b.type = 'button';
      b.addEventListener('click', function () { diag('kind-offer', key); reveal(key, { common: name, scientific: '', by: 'you' }); });
      kbox.appendChild(b);
    });
    show('claimKindBox', kinds.length > 0); $('claimOfferNote').textContent = kinds.length ? 'Or one of these species.' : 'It may be one of these.';
    var offers = pocket.offers || [], box = $('claimOffers'); box.textContent = '';      // what the small model could not choose between
    offers.forEach(function (o) {
      var b = el('button', 'pill ghost', o.en || o.sci); b.type = 'button';
      b.addEventListener('click', function () { diag('offer', o.kind); reveal(o.kind, { common: clip(o.en || o.sci, 60), scientific: clip(o.sci, 80), by: 'you', local: !!o.local }); });
      box.appendChild(b);
    });
    show('claimOfferBox', offers.length > 0);
    show('info', false); show('record', false); show('keep', false); show('ask', false); show('big', false); openSheet('claim');
    paintClaimAsk();
    setTimeout(function () { try { if (!$('claim').hidden) $('claimName').focus(); } catch (e) {} }, 80);
  }
  function setViewPrompt(key) {
    $('askViewText').textContent = (coarse ? 'Record a few seconds of what is in front of you, or photograph it.' : 'Choose a clip or a photo of what is in front of you.') +
      (key === 'person' ? '' : ' It returns as ' + EYES[key].who + ' may take it in.');
    $('askViewFine').textContent = '';
  }

  function reveal(key, named) {
    S.seq++; closeSheets(); setEyes(key, named); msg(''); noteMeeting(key, named); paintType();
    if (named && (named.by === 'service' || named.by === 'device-large')) paintSvc(); else dropSvc();     // a name said by the person, or a new photo, ends any question still out
    if (S.hasView) { thaw(); go('animal'); showName(); later(startChange, calm ? 150 : 750); return; }
    if (S.animalPhoto) showStill(S.animalPhoto, false);
    setViewPrompt(key);
    go('naming'); showName();
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

  // ---------- the larger model on a server (the naturalist), asked only with the person's say-so
  // One line on the picture carries it: an offer to ask (tappable), "Asking the larger model.", the waking sentence, what it said,
  // and, where it sees another kind of creature and is sure enough, an offer to change eyes (tappable). The eyes never change by themselves.
  var SVC_SAY = { offer: 'A larger model on a server can try to name the species. Ask it?', asking: 'Asking the larger model.', waking: 'The larger model is waking up, which can take a minute.', looking: 'Looking more closely.' };
  var svcTimer = 0, svcTap = null, askFirstT = 0, firstJob = null;
  function renewName() { if ($('reveal').classList.contains('show')) showName(); }     // a finer name that arrives while the first is still large on the screen takes its place there too
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
    var z = large.size();
    return z && large.has() === 'partial' ? 'The larger model is partly on this ' + dev() + ': ' + z.keptMb + ' of ' + z.mb + ' MB. Get the rest?' : 'A larger model can name the species on this ' + dev() + '. Get it?';
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
    $('bigSub').textContent = 'It is a larger model that names the species: about ' + z.mb + ' MB, downloaded once and kept on this ' + dev() + '. Photos are not sent anywhere. ' +
      (s && coarse && typeof s.phone === 'number' ? 'On a phone it takes about ' + Math.round(s.phone) + (Math.round(s.phone) === 1 ? ' second' : ' seconds') + ' a photo.'
        : s && !coarse && typeof s.computer === 'number' ? 'On a computer it takes about ' + Math.round(s.computer) + (Math.round(s.computer) === 1 ? ' second' : ' seconds') + ' a photo.'
        : 'On a phone it takes several seconds a photo.');
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
      if (r.sure && r.kind !== 'none') { reveal(r.kind, largeName(r) || { common: r.kind === 'person' ? 'A person' : handName(r.kind), scientific: '', by: 'device-large', local: false }); return; }
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
      if (h === 'none' || h === 'kept' || h === 'getting') return;
      if (ch === 'kept') { setBigChoice(''); return; }
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
  window.__seenBack = { S: S, EYES: EYES, state: function () { return engine ? engine.state() : null; }, record: function () { return record; }, kindOfName: kindOfName,
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
    var a = pocket.about(), st = engine ? engine.state() : null, L = ['Seen Back, build ' + BUILD + '.'], r = a.last, avg = 0;
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
  function paintAbout() { $('buildMark').textContent = aboutText(); $('aboutNote').textContent = ''; paintChoices(); }
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
  // ---------- self-test hook: with ?selftest=1 the page fetches selftest.js and hands it the bindings it reads (build.py)
  if (/[?&]selftest=1(?:&|$)/.test(location.search || '')) {
    S.selftest = true;   // at once, as the self-test did when it was part of this script: the page's loop leaves the drawing to it
    window.__seenBackSelftest = { '$': $, 'BUILD': BUILD, 'EYES': EYES, 'Engine': Engine, 'HUMAN': HUMAN, 'HUMAN_CPD': HUMAN_CPD, 'ORDER': ORDER, 'S': S, 'calm': calm, 'canvas': canvas, 'clamp': clamp, 'coarse': coarse, 'decode': decode, 'engine': engine, 'fxNow': fxNow, 'go': go, 'hasCamera': hasCamera, 'lerp': lerp, 'makeCanvas': makeCanvas, 'mix': mix, 'paramsOf': paramsOf, 'pocket': pocket, 'setEyes': setEyes, 'showStill': showStill, 'vid': vid };
    var selftestScript = document.createElement('script'); selftestScript.src = 'selftest.js?v=' + encodeURIComponent(BUILD);
    document.head.appendChild(selftestScript);
  }
})();
