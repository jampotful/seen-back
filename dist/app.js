(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };

  // ---------- where is this running?
  // Inside Claude's viewer the camera is normally refused, and only there can Claude name a photo.
  var inViewer = !!(window.claude && typeof window.claude.use === 'function');
  var hasCamera = !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);
  var coarse = !!(window.matchMedia && window.matchMedia('(pointer: coarse)').matches);
  var calm = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var BUILD = '5';
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
    return createImageBitmap(file).then(function (bmp) { var c = fit(bmp, bmp.width, bmp.height, 1280); if (bmp.close) bmp.close(); return c; }, viaImg);
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
    if (!engine) return;
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
  // so the order settles "fox squirrel", "rat snake", "crane fly" and "turkey vulture".
  var LEX = [
    ['person', /\b(person|people|humans?|man|woman|men|women|boy|girl|child|children|kid|baby|me|myself|selfie)\b/],
    ['other', /(spiders?|fish(es)?|snails?|slugs?|\bworms?|earthworms?|\bbats?|crabs?|crayfish|shrimps?|mushrooms?|fung(us|i)|lichens?|raccoons?|opossums?|possums?|armadillos?|\bbears?|otters?|manatees?|\bpigs?|\bhogs?|monkeys?|millipedes?|centipedes?|scorpions?|\bticks?|\bmites?)\b/],
    ['bee', /(bees?|wasps?|hornets?|yellowjackets?)\b/],
    ['insect', /(butterfl(y|ies)|\bmoths?|beetles?|fl(y|ies)|\bants?|crickets?|cicadas?|mantis|mantids?|\bbugs?|ladybugs?|ladybirds?|lovebugs?|skippers?|monarchs?|fritillar(y|ies)|swallowtails?|longwings?|buckeyes?|katydids?|roach(es)?|weevils?|aphids?|caterpillars?|mosquito(es)?|gnats?|termites?|walkingsticks?|earwigs?|hoppers?|insects?)\b/],
    ['frog', /(frogs?|toads?|peepers?)\b/],
    ['alligator', /\b(alligators?|gators?|crocodiles?|crocs?|caimans?)\b/],
    ['reptile', /(lizards?|anoles?|geckos?|skinks?|snakes?|\bracers?|turtles?|tortoises?|sliders?|cooters?|softshells?|iguanas?|reptiles?|cottonmouths?|moccasins?|copperheads?|pythons?)\b/],
    ['squirrel', /(squirrels?|chipmunks?|\brats?|\bmice|\bmouse|\bvoles?|gophers?)\b/],
    ['hawk', /(hawks?|eagles?|falcons?|\bkites?|ospreys?|vultures?|kestrels?|harriers?|buzzards?|caracaras?|merlins?)\b/],
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
  function cleanMeeting(v, id) {
    if (!v || typeof v !== 'object') return null;
    var key = String(v.key || ''), mid = String(id || v.id || '');
    if (!EYES[key] || key === 'person' || !/^[A-Za-z0-9_-]{4,40}$/.test(mid)) return null;
    var thumb = typeof v.thumb === 'string' && v.thumb.length < 24000 && /^data:image\/jpeg;base64,[A-Za-z0-9+\/=]+$/.test(v.thumb) ? v.thumb : '';
    return { id: mid, key: key, common: clip(v.common, 60) || handName(key), sci: clip(v.sci, 80), by: v.by === 'Claude' ? 'Claude' : 'you', at: +v.at || 0, thumb: thumb, up: v.up ? 1 : 0 };
  }
  function loadLocal() {
    try { var a = JSON.parse(localStorage.getItem(REC_KEY) || '[]'); return Array.isArray(a) ? a.map(function (v) { return cleanMeeting(v); }).filter(Boolean) : []; }
    catch (e) { return []; }
  }
  var record = loadLocal();
  function saveLocal() {
    try { localStorage.setItem(REC_KEY, JSON.stringify(record.slice(0, 300).map(function (m) { return { id: m.id, key: m.key, common: m.common, sci: m.sci, by: m.by, at: m.at, thumb: m.thumb, up: m.up }; }))); } catch (e) {}
  }
  function pushUp(m) {                             // one write at a time for each meeting
    if (!remote) return;
    var col = remote;
    m._p = (m._p || Promise.resolve()).then(function () {
      return col.doc(m.id).set({ key: m.key, common: m.common, sci: m.sci, by: m.by, at: m.at, thumb: m.thumb });
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
    m.key = key; m.common = named.common; m.sci = named.scientific || ''; m.by = named.by === 'Claude' ? 'Claude' : 'you';
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
      tx.appendChild(el('span', 'sm', [m.sci, labelDate(new Date(m.at)), m.by === 'Claude' ? 'recognized by Claude' : 'on your word'].filter(Boolean).join(' · ')));
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
    var named = { common: m.common, scientific: m.sci, by: m.by, again: m.at };
    closeSheets(); S.seq++; S.token++; if (nameCtl) nameCtl.abort(); hideName(); msg('');
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

  // ---------- recognition in the page itself (the pocket recognizer)
  // Filled in by the recognizer work. See docs/CONTRACTS.md.

  // ---------- naming
  var PROMPT = [
    'The attached photograph was taken by someone who wants to know what living thing is in it.',
    'Name the main living subject. Reply with only one JSON object, no other text, in this shape:',
    '{"found": true, "common": "Domestic cat", "scientific": "Felis catus", "eyes": "cat"}',
    'Rules:',
    '- "common" is the everyday English name, as fine as the photo supports. "scientific" is the Latin name at that level, or "" if you have none.',
    '- "eyes" is exactly one of: "cat" (any cat), "dog" (dogs, foxes, coyotes), "squirrel" (squirrels, chipmunks, rats, mice), "deer" (deer, horses, cattle, goats, sheep), "rabbit" (rabbits, hares), "hawk" (hawks, eagles, falcons, kites, ospreys, vultures), "wader" (herons, egrets, ibis, storks, cranes, limpkins, coots, moorhens, pigeons, doves, chickens, turkeys), "bird" (any other bird, owls and ducks included), "alligator" (alligators, crocodiles), "reptile" (lizards, snakes, turtles), "frog" (frogs, toads), "bee" (bees, wasps), "insect" (any other insect), "plant" (plants, trees, flowers, mosses, ferns), "person" (a human being), "other" (anything else alive: fungi, spiders, fish, snails, other mammals).',
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
  function recognize(t) {
    if (!(sample && canImages)) {
      msg(''); if (S.src !== 'cam') go('naming'); else go('finder');
      diag('no-recognizer', inViewer ? (sample ? 'no-images' : 'no-sample') : 'outside');
      openClaim(inViewer ? 'Claude could not be reached from this view, so you tell it.' : 'Outside Claude this page cannot recognize a photo yet, so you tell it.');
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
    S.animalPhoto = c; S.meetingId = null; S.nov = ''; setEyes(null); hideName();
    if (S.src === 'cam') { S.freeze = true; if (engine) engine.setImage(c); paintUI(); }
    else showStill(c, false);
    identify();
  }
  function shutter() {
    if (S.screen !== 'finder' || S.src !== 'cam' || S.freeze || !vid.videoWidth) return;
    $('flash').classList.remove('go'); void $('flash').offsetWidth; $('flash').classList.add('go');
    var c = fit(vid, vid.videoWidth, vid.videoHeight, 1280);
    if (S.mirror) { var m = makeCanvas(c.width, c.height), x = m.getContext('2d'); x.translate(c.width, 0); x.scale(-1, 1); x.drawImage(c, 0, 0); c = m; }
    msg(''); gotAnimalPhoto(c);
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
    $('infoSub').textContent = (S.named && S.named.scientific ? S.named.scientific + '. ' : '') + (S.named && S.named.by === 'Claude' ? 'Recognized by Claude from your photo, which can be wrong.' : 'As you said.');
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
    decode(f).then(gotAnimalPhoto).catch(function () { if (S.screen === 'finder') msg('That file could not be read as a photo.', 5000); else $('askFine').textContent = 'That file could not be read as a photo.'; });
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
    pose: function (t) { S.tr = t === null ? null : { t0: 0, dur: 1, fixed: t }; if (t === null) S.k = 1; } };   // hold the change of eyes at one instant, for checking
  $('buildMark').textContent = 'Build ' + BUILD + '.';
  if (inViewer) {
    window.claude.use('sample').then(function (s) {
      if (!s) return;
      return s.limits().then(function (lim) { sample = s; canImages = !!(lim && lim.images); }, function () { sample = s; canImages = false; });
    }).catch(function () {}).then(capsDone);
    setTimeout(capsDone, 8000);                     // a viewer that never answers is treated as having no Claude
    window.claude.use('downloads').then(function (d) { downloads = d; }).catch(function () {});
    initRemote();
  }

  // ---------- self-test: open the page with ?selftest=1 and it checks its own picture engine
  // Filled in by the engines work. See docs/CONTRACTS.md.
})();
