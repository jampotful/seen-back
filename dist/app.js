(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };

  // ---------- where is this running?
  // Inside Claude's viewer the camera is normally refused, and only there can Claude name a photo.
  var inViewer = !!(window.claude && typeof window.claude.use === 'function');
  var hasCamera = !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);
  var coarse = !!(window.matchMedia && window.matchMedia('(pointer: coarse)').matches);
  var calm = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var BUILD = '24';
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
  var EYES = {
    cat: { chip: 'Cat', who: 'a cat', fov: 200, cpd: 8, topoA: 1, fall: 2.0, pupil: 'v', dof: 26, M: DEUTAN, gain: 1.7, sat: .8,
      cue: 'Out-of-focus things smear up and down. Tap the screen to move the focus.', rows: [
      ['m', 'Sharpness', 'Cats see about a fifth to a tenth as much detail as people do. This view is blurred to match.'],
      ['m', 'Colour', 'Cats have two kinds of colour-sensing cells in their eyes, where people have three. Reds and greens are hard for them to tell apart, so reds look olive or grey to a cat.'],
      ['m', 'Pupil', 'A cat’s pupil closes to a narrow vertical slit, a shape common in animals that hunt by ambush. A slit like this smears out-of-focus things up and down, and this view does the same.'],
      ['m', 'Field of view', 'A cat takes in about 200 degrees around itself, and a person about 180. A phone camera sees far less than either, so this view bends the picture at its edges to suggest the wider sweep.'],
      ['m', 'Dim light', 'Cats can see in light six to eight times dimmer than people need. This view brightens the shadows to show it.'],
      ['i', 'Depth', 'A phone camera can’t measure distance, so this view assumes that things lower in the picture are closer. Tap the screen to move the focus.'],
      ['i', 'Sharpest spot', 'This view assumes that a cat sees most sharply straight ahead.']] },
    dog: { chip: 'Dog', who: 'a dog', fov: 240, cpd: 11, topoS: 1, fall: 1.6, pupil: 'o', dof: 10, M: DEUTAN, gain: 1.3, sat: .85,
      cue: 'The sharpest part is a band along the horizon. Tap the screen to move the focus.', rows: [
      ['m', 'Sharpness', 'Dogs see about a quarter to a seventh as much detail as people do. This view is blurred to match.'],
      ['m', 'Sharpest spot', 'Dogs with long noses see most sharply along a band level with the horizon. Dogs with short noses see most sharply in one central spot. This view shows the band.'],
      ['i', 'Colour', 'Dogs have two kinds of colour-sensing cells, where people have three. This view shows colours as a person with two kinds would see them.'],
      ['i', 'Field of view, dim light and depth', 'These parts of the view are guesses. This view treats things lower in the picture as closer.']] },
    squirrel: { chip: 'Squirrel', who: 'a squirrel', fov: 270, cpd: 6, topoS: 1, fall: 1.0, pupil: 'o', dof: 4, M: PROTAN, rate: .56,
      cue: 'The picture runs slowly, then jumps ahead to catch up.', rows: [
      ['g', 'Colour', 'Ground squirrels have two kinds of colour-sensing cells in their eyes, where people have three.'],
      ['g', 'Speed', 'A ground squirrel can see a light flicker on and off up to 108 times a second. To a person, a light that flickers faster than about 60 times a second looks steady. Fast movements look slower to a squirrel, so this view runs slowly and then jumps ahead to catch up.'],
      ['i', 'Field of view and sharpness', 'A squirrel’s eyes sit on the sides of its head, which probably gives it a wide view with less detail than yours. This part of the view is a guess.']] },
    deer: { chip: 'Deer', who: 'a deer', fov: 310, cpd: 8, topoS: 1, fall: 2.2, pupil: 'h', dof: 22, M: DEUTAN, gain: 1.5, sat: .85,
      cue: 'You see a wide band of ground. Out-of-focus things smear sideways.', rows: [
      ['m', 'Colour', 'White-tailed deer have two kinds of colour-sensing cells, where people have three. Reds and oranges look yellow or grey to them.'],
      ['m', 'Field of view', 'A deer takes in about 310 degrees around itself, almost a full circle. A phone camera sees less than a quarter of that, so this view bends the picture at its edges to suggest it.'],
      ['g', 'Pupil', 'Grazing animals have pupils shaped like horizontal bars. The shape widens their view along the ground and cuts glare from the sky. It also smears out-of-focus things sideways, and this view does the same.'],
      ['i', 'Sharpness, dim light and depth', 'These parts of the view are guesses. This view treats things lower in the picture as closer.']] },
    rabbit: { chip: 'Rabbit', who: 'a rabbit', fov: 350, cpd: 3, topoS: 1, fall: 2.0, pupil: 'o', dof: 6, M: DEUTAN,
      cue: 'You see almost the whole circle at once, and little of it is sharp.', rows: [
      ['i', 'The whole view', 'This view is a guess that hasn’t yet been checked against research. A rabbit probably sees almost all the way around itself, most sharply along the horizon, in little detail, with two kinds of colour-sensing cells.']] },
    hawk: { chip: 'Hawk, eagle, falcon', who: 'a hawk', fov: 180, cpd: 60, fovea: 2.2, pupil: 'o', rate: .6,
      cue: 'The centre is magnified, and the picture runs slowly, then jumps ahead.', rows: [
      ['g', 'Sharpness', 'Eagles see more than twice as much detail as people do. A phone camera can’t capture that much detail, so this view magnifies the centre to suggest it.'],
      ['m', 'Speed', 'A peregrine falcon can see a light flicker up to 129 times a second, and a Harris’s hawk up to 77. People see flicker up to 50 or 60 times a second. This view runs slowly and then jumps ahead to suggest the difference.'],
      ['i', 'Field of view', 'This view keeps the field of view your camera gives.']] },
    wader: { chip: 'Heron, crane, pigeon', who: 'a wading bird', fov: 300, cpd: 25, topoS: .6, fall: .8, pupil: 'o', sheen: .6, hold: 280, thrust: 120,
      cue: 'Walk. The picture holds still, then lurches forward, the way a heron’s head does.', rows: [
      ['m', 'Head movement', 'Herons, egrets, cranes, pigeons and chickens hold their heads still while they walk, so their eyes stay fixed on the world. Then the head darts forward to catch up with the body. This view does the same while you walk.'],
      ['g', 'Speed', 'In pigeons, each dart forward takes about a tenth of a second.'],
      ['g', 'Sharpness', 'Most birds see half as much detail as people do, or less.'],
      ['i', 'Ultraviolet', 'Some birds can see ultraviolet light, which people can’t. Phone cameras capture very little of it, so the violet tint in this view stands in for it.'],
      ['i', 'Field of view', 'Eyes on the sides of the head probably give a wide view. This part of the view is a guess.']] },
    bird: { chip: 'Other bird', who: 'a bird', fov: 300, cpd: 25, topoA: .5, fall: .6, pupil: 'o', sheen: .8, rate: .5,
      cue: 'The picture runs slowly, then jumps ahead to catch up.', rows: [
      ['g', 'Speed', 'Birds can see a light flicker 40 to 140 times a second, and the fastest fliers are at the top of that range. People see flicker up to about 60 times a second. This view runs slowly and then jumps ahead to suggest the difference.'],
      ['g', 'Sharpness', 'Most birds see half as much detail as people do, or less.'],
      ['i', 'Ultraviolet', 'Some birds can see ultraviolet light, which people can’t. Phone cameras capture very little of it, so the violet tint in this view stands in for it.'],
      ['i', 'Field of view', 'Eyes on the sides of the head probably give a wide view. This part of the view is a guess.']] },
    alligator: { chip: 'Alligator', who: 'an alligator', fov: 280, cpd: 9, topoS: 1, fall: 2.6, pupil: 'v', dof: 24, gain: 1.6, sat: .9,
      cue: 'The sharpest part is a band along the waterline.', rows: [
      ['g', 'Sharpest spot', 'Crocodiles see most sharply along a band level with the horizon. It lets them scan the waterline without turning their heads.'],
      ['g', 'Colour', 'Crocodiles have three kinds of colour-sensing cells, as people do, so this view leaves colours as your camera shows them.'],
      ['g', 'Pupil', 'An alligator’s pupil is a vertical slit. It smears out-of-focus things up and down, and this view does the same.'],
      ['i', 'Field of view, sharpness, dim light and depth', 'These parts of the view are guesses.']] },
    reptile: { chip: 'Lizard, snake, turtle', who: 'a reptile', fov: 280, cpd: 15, topoA: 1, fall: 1.2, pupil: 'o', sheen: .6,
      cue: '', rows: [
      ['i', 'The whole view', 'This whole view is a guess. It assumes eyes on the sides of the head, one sharp spot straight ahead, and the ability to see ultraviolet light, which appears here as a violet tint.']] },
    frog: { chip: 'Frog, toad', who: 'a frog or toad', fov: 340, cpd: 4, pupil: 'h', persist: .15, gate: 1,
      cue: 'Hold still, as a frog does. Only things that move show up.', rows: [
      ['m', 'Movement', 'A frog takes little notice of the parts of its world that stay still, and it can starve beside food that never moves. This view shows only what changes, so hold your phone as still as a frog holds itself.'],
      ['g', 'Speed', 'A cane toad can see a light flicker only about 7 times a second, a ninth as often as a person can. Anything that moves smears into a trail.'],
      ['i', 'Field of view, sharpness and pupil', 'These parts of the view are guesses.']] },
    bee: { chip: 'Bee', who: 'a bee', fov: 320, cpd: 1, pupil: 'none', M: BEE, uvBlue: 1, rate: .3,
      cue: 'Red turns dark, and the picture runs slowly, then jumps ahead.', rows: [
      ['g', 'Sharpness', 'Most insects see less than a sixtieth as much detail as people do.'],
      ['m', 'Red', 'Bees have no colour-sensing cells for red, so red flowers and objects look dark to them.'],
      ['m', 'Speed', 'In bright light, a honeybee can see a light flicker up to 200 times a second, where people stop at about 60. This view runs slowly and then jumps ahead to suggest the difference.'],
      ['i', 'Ultraviolet', 'Bees can see ultraviolet light, which people can’t. Phone cameras capture very little of it, so the blue in this view stands in for it.'],
      ['i', 'How the colours are shown', 'A bee sees green, blue and ultraviolet. Since a screen can’t show ultraviolet, this view moves every colour over by one: a bee’s green appears as red, its blue as green, and its ultraviolet as blue.']] },
    insect: { chip: 'Butterfly, other insect', who: 'an insect', fov: 320, cpd: 1, pupil: 'none', sheen: .8, rate: .45,
      cue: 'The view is wide and blurry, and it runs slowly, then jumps ahead.', rows: [
      ['g', 'Sharpness', 'Most insects see less than a sixtieth as much detail as people do.'],
      ['g', 'Speed', 'Flies and dragonflies can see a light flicker more than 100 times a second, and one beetle up to 400. People stop at about 60. This view runs slowly and then jumps ahead to suggest the difference.'],
      ['i', 'Ultraviolet', 'Bees and some other insects can see ultraviolet light, which people can’t. Phone cameras capture very little of it, so the violet tint in this view stands in for it.']] },
    plant: { chip: 'Plant', who: 'a plant', pupil: 'none', field: 1, noGreen: 1, persist: 2.5,
      cue: 'There’s no picture here, only how much light there is, what colour it is, and where it comes from.', rows: [
      ['g', 'No picture', 'A plant has nothing like a lens to focus light into an image. It senses how much light there is, what colour it is, and which direction it comes from.'],
      ['m', 'Neighbours', 'Plants compare red light with far-red light, a colour just past the edge of what people can see. The balance tells a plant that a neighbour is growing close by, even before the neighbour shades it. Phone cameras capture very little far-red light.'],
      ['i', 'Green and time', 'This view removes green, because leaves reflect most green light away, and it smooths out anything quick. Both are the app’s own choices.']] },
    // `other` and `person` are never views (build 22): a creature with no view of its own, and a human, each get a notice and the
    // identifying screen stays as it is. The entries remain so that encounters kept by older builds still read.
    other: { chip: null, who: 'this creature', pupil: 'none', field: 1, sat: 0, cue: '', rows: [
      ['i', 'No view yet', 'Regards doesn’t have the ability to view the world as this creature right now.']] },
    person: { chip: null, who: 'a human', pupil: 'o', cue: '', rows: [
      ['m', 'Same eyes', 'That’s a human. You already see the world as one.']] }
  };
  var ORDER = ['cat', 'dog', 'squirrel', 'deer', 'rabbit', 'wader', 'bird', 'hawk', 'alligator', 'reptile', 'frog', 'bee', 'insect', 'plant'];
  // Groups the app can name and cannot yet view the world as (docs/COVERAGE.md, decided by the owner on 12 October 2026).
  // A photo or a typed name in one of them gets the notice that Regards can't view the world as that creature yet, and no
  // encounter is kept. A group moves into EYES when its view is drawn from its sheet (docs/views/sheets/).
  var GROUPS = { fungus: 'a fungus', slime: 'a slime mould', spider: 'a spider', jumper: 'a jumping spider', fish: 'a fish', shark: 'a shark or ray',
    snail: 'a snail or slug', sealife: 'a sea creature', crab: 'a crustacean', salamander: 'a salamander or newt', worm: 'a worm, millipede or centipede',
    scorpion: 'a scorpion or harvestman', tick: 'a tick', mammal: 'a mammal', primate: 'a monkey or ape', whale: 'a whale, dolphin or seal',
    bat: 'a bat', flyingfox: 'a flying fox', cephalopod: 'an octopus or squid' };
  function noView(key) { return key === 'other' || (!!GROUPS[key] && !EYES[key]); }
  function noViewOrPerson(key) { return key === 'person' || noView(key); }   // neither becomes a view, and neither is kept as an encounter

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
  // A species' English name in sentence case: the first letter a capital, the rest small, except words that are names of
  // places or people ("North American river otter", "Cooper's hawk"). A scientific name passes through unchanged in effect.
  var PROPER = ' african alaskan american andean antarctic antillean appalachian arabian arctic argentine asian asiatic atlantic australian bahama bahaman baltic bermuda bolivian brazilian british burmese california californian canada canadian caribbean carolina carolinian chilean chinese colombian colorado cuban dutch egyptian english eurasian european florida floridian french georgia german greek guatemalan gulf haitian hawaiian himalayan hispaniolan indian indies indonesian irish italian jamaican japanese javan korean louisiana madagascar malayan mediterranean mexican mississippi new nile norway norwegian pacific panama panamanian persian peruvian philippine polynesian portuguese puerto rican russian scotia scottish siberian spanish sumatran swedish swiss tasmanian texas texan thai turkish virginia virginian world york zealand amazon bolivia china peru lanka keys st. augustine charles sebastian william susan maria lizzie jones hentz caesar hercules jesus venus quaker confederate january february march april june july august september october november december ';
  function nameCase(name) {
    name = String(name || ''); if (!name) return name;
    var first = true;
    return name.replace(/[^\s-]+/g, function (w, at) {
      var keep = /['’]s?$/.test(w) || PROPER.indexOf(' ' + w.toLowerCase() + ' ') >= 0 || (w.length <= 3 && w === w.toUpperCase() && /[A-Z]/.test(w) && at > 0);
      if (first) { first = false; return w.charAt(0).toUpperCase() + w.slice(1); }
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
    return fx;
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
  // Used only where nothing can look at the photo, or to correct a name that came out wrong. In most names of creatures the
  // last word says what the creature is ("fox squirrel", "rat snake", "crane fly", "turkey vulture", "fish crow", "oakworm
  // moth"), so the word of the table that ends last in the name decides. Where two end at the same letter the longer decides
  // ("sea lion" over "lion", "silverfish" over "fish"), then the entry higher in the table. Vultures are among the other birds:
  // the hawk's sharper sight is not established for them. The groups with no view yet are in GROUPS in cam.a.js.
  // Each word is written out whole, with no group of three or more choices inside it: lexWords() below reads the table for the
  // words a slip of the keys is matched against.
  var LEX = [
    ['person', /\b(person|people|humans?|man|woman|men|women|boy|girl|child|children|kids?|bab(y|ies)|me|myself|selfie)\b/],
    // names whose last word belongs to another kind, or names that end in no word of the table
    ['other', /(\bmites?|chiggers?|tardigrades?|water ?bears?|moss ?piglets?|rotifers?|velvet ?worms?|amoebas?|bacteria|microbes?|plankton)\b/],
    ['sealife', /(man[ -]?o'?[ -]?war|sea ?lil(y|ies)|sea ?wasps?|sea ?pens?|shipworms?)\b/],
    ['fungus', /(chicken[ -]?of[ -]?the[ -]?woods|hen[ -]?of[ -]?the[ -]?woods|old[ -]?man[ -]?of[ -]?the[ -]?woods|turkey[ -]?tails?|deer ?moss|reindeer ?moss|dead ?man's ?fingers?|dead ?man's ?foot|jack-?o'?-?lanterns?|destroying ?angels?|shaggy ?manes?|witch's ?butter|slippery ?jacks?|slippery ?jills?|sulphur ?shel(f|ves)|sulfur ?shel(f|ves))\b/],
    ['slime', /(slime ?mou?lds?|\bslimes?|dog ?vomit|wolf's ?milk)\b/],
    ['crab', /(sea ?spiders?|water ?fleas?|pill[ -]?bugs?|sow[ -]?bugs?)\b/],
    ['snail', /(sea ?hares?|sea ?butterfl(y|ies)|sea ?angels?)\b/],
    ['jumper', /(jumping ?spiders?|zebra ?spiders?|peacock ?spiders?)\b/],
    ['scorpion', /(camel ?spiders?|sun ?spiders?|whip ?spiders?)\b/],
    ['spider', /(black ?widows?|brown ?widows?)\b/],
    ['salamander', /(congo ?eels?)\b/],
    ['flyingfox', /(flying[ -]?fox(es)?|fruit ?bats?)\b/],
    ['whale', /(sea ?lions?|sea ?cows?)\b/],
    ['squirrel', /(prairie ?dogs?|guinea ?pigs?)\b/],
    ['primate', /(bush ?bab(y|ies))\b/],
    ['fish', /(sea ?horses?|sea ?robins?|sea ?dragons?)\b/],
    ['reptile', /(slow ?worms?|gila ?monsters?)\b/],
    ['bird', /(nighthawks?|bee-?eaters?|oyster ?catchers?|brown ?creepers?|treecreepers?|wallcreepers?)\b/],
    ['bee', /(velvet ?ants?|cicada ?killers?|cow ?killers?|tarantula ?hawks?|longhorn-?cuckoos?)\b/],
    ['insect', /(silverfish|white ?peacocks?|pondhawks?|monkey ?slugs?|woolly ?bears?|bee-?killers?|inch ?worms?|silk ?worms?|meal ?worms?|glow[ -]?worms?|army ?worms?|cut ?worms?|horn ?worms?|bag ?worms?|web ?worms?|wire ?worms?|canker ?worms?|bud ?worms?|boll ?worms?|ear ?worms?|wood ?worms?|screw ?worms?|root ?worms?|fruit ?worms?|leaf ?worms?)\b/],
    ['plant', /(monkey ?puzzles?|elephant ?ears?|alligator ?flags?|lamb's ?quarters|wood ?anemones?|japanese ?anemones?|madagascar ?periwinkles?|green ?dragons?|wakerobins?|kangaroo ?paws?|crane's-?bills?|spider ?brakes?|rattlesnake ?masters?|greater ?periwinkles?|lesser ?periwinkles?|rosy ?periwinkles?|forget-?me-?nots?|dragon-?tails?|black ?locusts?|honey ?locusts?|devil's ?walking-?sticks?|'s[ -]?foot|'s[ -]?feet|'s[ -]?ears?|'s[ -]?tails?|'s[ -]?tongues?|'s[ -]?claws?|'s[ -]?beards?|'s[ -]?feathers?|'s[ -]?seals?)\b/],
    // the groups with no view yet
    ['worm', /(\bworms?|earthworms?|flatworms?|roundworms?|tapeworms?|hookworms?|lugworms?|ragworms?|bloodworms?|fireworms?|tubeworms?|\bleech(es)?|nematodes?|planarians?|millipedes?|centipedes?|polychaetes?|feather ?dusters?)\b/],
    ['flyingfox', /(megabats?)\b/],
    ['shark', /(sharks?|hammerheads?|\brays?|stingrays?|mantas?|sawfish|guitarfish|dogfish|ratfish|chimaeras?|\bskates?)\b/],
    ['bat', /(\bbats?|microbats?|myotis)\b/],
    ['cephalopod', /(octopus(es)?|octopi|squids?|cuttlefish|nautilus(es)?|argonauts?|cephalopods?)\b/],
    ['sealife', /(starfish|sea ?stars?|brittle ?stars?|feather ?stars?|basket ?stars?|corals?|anemones?|jellyfish|comb ?jell(y|ies)|moon ?jell(y|ies)|box ?jell(y|ies)|sea ?urchins?|urchins?|sea ?cucumbers?|sand ?dollars?|sea ?biscuits?|\bclams?|mussels?|oysters?|scallops?|cockles?|quahogs?|geoducks?|sponges?|sea ?squirts?|tunicates?|\bsalps?|sea ?fans?|hydroids?|\bhydras?|siphonophores?|bryozoans?|lamp ?shells?|brachiopods?|crinoids?)\b/],
    ['crab', /(crabs?|crayfish|crawfish|crawdads?|lobsters?|shrimps?|prawns?|krill|barnacles?|woodlice|woodlouse|roly[ -]?pol(y|ies)|isopods?|amphipods?|copepods?)\b/],
    ['snail', /(snails?|slugs?|whelks?|conch(es)?|conchs|nudibranchs?|limpets?|periwinkles?|chitons?|abalones?|cowr(y|ie)s?|murex(es)?|ramshorns?|tusk ?shells?)\b/],
    ['jumper', /(\bjumpers?|salticids?)\b/],
    ['scorpion', /(scorpions?|harvestm(a|e)n|daddy[ -]?long[ -]?legs|vinegaroons?|amblypygids?|solifugids?|solifugae)\b/],
    ['spider', /(spiders?|tarantulas?|orb[ -]?weavers?|recluses?|huntsm(a|e)n|funnel-?webs?|sheet ?weavers?|sheetweavers?|hacklemesh ?weavers?|funnel ?weavers?|cobweb ?weavers?|micrathenas?)\b/],
    ['tick', /(\bticks?)\b/],
    ['slime', /(myxomycetes?)\b/],
    ['fungus', /(mushrooms?|toadstools?|fung(us|i)|lichens?|\bmou?lds?|mildews?|puffballs?|morels?|chanterelles?|boletes?|polypores?|stinkhorns?|truffles?|earthstars?|earthballs?|agarics?|amanitas?|russulas?|\bbrackets?|parasols?|inkcaps?|ink ?caps?|milkcaps?|milk ?caps?|waxcaps?|waxy ?caps?|webcaps?|fibrecaps?|fibercaps?|\brusts?|rustgills?|sawgills?|mazegills?|brittlegills?|rosegills?|splitgills?|dapperlings?|lepidellas?|deceivers?|shii?takes?|suillus|reishis?|candlesnuffs?|xylarias?|trametes|oysterlings?|\bcrusts?|matsutakes?|grisettes?|brittlestems?|fieldcaps?|elfcups?|pinwheels?|earthtongues?)\b/],
    ['salamander', /(salamanders?|\bnewts?|axolotls?|mudpupp(y|ies)|waterdogs?|amphiumas?|hellbenders?|\bsirens?|\bolms?|caecilians?|\befts?)\b/],
    ['whale', /(whales?|dolphins?|porpoises?|orcas?|\bseals?|walrus(es)?|manatees?|dugongs?|narwhals?|belugas?|humpbacks?|pinnipeds?|cetaceans?)\b/],
    ['primate', /(monkeys?|\bapes?|gorillas?|chimps?|chimpanzees?|orangutans?|bonobos?|gibbons?|baboons?|macaques?|lemurs?|marmosets?|tamarins?|capuchins?|loris(es)?|langurs?|colobus(es)?|mandrills?|tarsiers?|galagos?|howlers?|aye-?ayes?|sifakas?|primates?)\b/],
    ['mammal', /(raccoons?|opossums?|possums?|armadillos?|\bbears?|\botters?|weasels?|\bminks?|ferrets?|stoats?|ermines?|polecats?|\bfishers?|skunks?|badgers?|wolverines?|martens?|\bpigs?|\bhogs?|boars?|warthogs?|peccar(y|ies)|javelinas?|hippos?|hippopotamus(es)?|rhinos?|rhinoceros(es)?|tapirs?|kangaroos?|wallab(y|ies)|koalas?|wombats?|quokkas?|quolls?|bandicoots?|bilb(y|ies)|numbats?|tasmanian ?devils?|sugar ?gliders?|hedgehogs?|\bmoles?|shrews?|tenrecs?|sloths?|anteaters?|pangolins?|aardvarks?|aardwol(f|ves)|elephants?|platypus(es)?|echidnas?|hyrax(es)?|mongooses?|meerkats?|hyenas?|civets?|genets?|binturongs?|fossas?|coatis?|coatimundis?|kinkajous?|\bringtails?|pandas?|mammals?)\b/],
    ['fish', /(fish(es)?|\beels?|minnows?|\bbass|trout|salmon|\bcarps?|bluegills?|perch(es)?|gupp(y|ies)|gob(y|ies)|wrasses?|tunas?|\bcods?|herrings?|sardines?|anchov(y|ies)|\bpikes?|pickerels?|muskies|muskellunges?|walleyes?|\bgars?|mullets?|snappers?|groupers?|snooks?|tarpons?|bowfins?|sturgeons?|\bshads?|menhadens?|sheepshead|lampreys?|piranhas?|barracudas?|marlins?|mackerels?|halibuts?|flounders?|\bkoi|bettas?|tetras?|cichlids?|tilapias?|blenn(y|ies)|sculpins?|sticklebacks?|\bbarbs?|loach(es)?|darters?|shiners?|crappies?|morays?|madtoms?|bullheads?|silversides?|warmouths?|hogchokers?|chubsuckers?|mudskippers?|snakeheads?)\b/],
    // the kinds with views
    ['bee', /(bees?|wasps?|hornets?|yellowjackets?|yellow ?jackets?|daubers?|beewol(f|ves)|ichneumons?|sawfl(y|ies)|horntails?|leaf-?cutters?)\b/],
    ['insect', /(butterfl(y|ies)|\bmoths?|hawkmoths?|silkmoths?|sphinx(es)?|beetles?|scarabs?|chafers?|borers?|sawyers?|engravers?|clerids?|weevils?|curculios?|fl(y|ies)|\bants?|antlions?|crickets?|cicadas?|mantis(es)?|mantids?|bugs?|ladybirds?|assassins?|skippers?|monarchs?|fritillar(y|ies)|swallowtails?|longwings?|birdwings?|hairstreaks?|satyrs?|wood-?nymphs?|leafwings?|clearwings?|daggers?|veneers?|hooktips?|leaftiers?|leaf ?tiers?|buckeyes?|clubtails?|darners?|cruisers?|spreadwings?|forktails?|sprites?|katydids?|coneheads?|locusts?|wetas?|lubbers?|roach(es)?|aphids?|psyllids?|mirids?|phylloxeras?|sharpshooters?|\bscales?|gallmakers?|\bkeds?|thrips|caterpillars?|loopers?|spanworms?|grubs?|maggots?|chrysalis(es)?|mosquito(es)?|gnats?|midges?|fleas?|\blice|\blouse|termites?|walkingsticks?|walking ?sticks?|earwigs?|hoppers?|lacewings?|hellgrammites?|springtails?|leaf ?miners?|leafminers?|insects?)\b/],
    ['frog', /(frogs?|toads?|peepers?|tadpoles?|polliwogs?)\b/],
    ['alligator', /\b(alligators?|gators?|crocodiles?|crocs?|caimans?|gharials?|gavials?)\b/],
    ['reptile', /(lizards?|anoles?|geckos?|skinks?|snakes?|\bracers?|turtles?|tortoises?|terrapins?|sliders?|cooters?|softshells?|loggerheads?|leatherbacks?|hawksbills?|ridleys?|iguanas?|chameleons?|\bdragons?|agamas?|basilisks?|tuataras?|reptiles?|cottonmouths?|moccasins?|copperheads?|rattlers?|hognoses?|pythons?|\bboas?|anacondas?|vipers?|\badders?|cobras?|mambas?|kraits?|taipans?)\b/],
    ['squirrel', /(squirrels?|chipmunks?|\brats?|\bmice|\bmouse|dormouse|dormice|\bvoles?|gophers?|beavers?|porcupines?|capybaras?|hamsters?|gerbils?|chinchillas?|groundhogs?|woodchucks?|marmots?|muskrats?|woodrats?|nutrias?|coypus?|agoutis?|\bpacas?|lemmings?|jerboas?|rodents?)\b/],
    ['bird', /(vultures?|condors?)\b/],
    ['hawk', /(hawks?|eagles?|falcons?|\bkites?|ospreys?|kestrels?|harriers?|buzzards?|caracaras?|merlins?)\b/],
    ['wader', /\b(herons?|egrets?|ibis(es)?|storks?|cranes?|limpkins?|coots?|moorhens?|gallinules?|rails?|crakes?|soras?|jacanas?|shoebills?|pigeons?|doves?|chickens?|roosters?|hens?|turkeys?|pheasants?|quails?|bobwhites?|grouse|partridges?|ptarmigans?|guineafowl|guinea ?fowl|peacocks?|peafowl|peahens?|junglefowl|fowls?|bitterns?|spoonbills?)\b/],
    ['bird', /(birds?|\bducks?|\bgeese|\bgoose|\bswans?|waterfowl|gulls?|\bterns?|pelicans?|cormorants?|anhingas?|cardinals?|warblers?|sparrows?|\bwrens?|\bjays?|\bcrows?|ravens?|\brooks?|jackdaws?|magpies?|robins?|finch(es)?|siskins?|canar(y|ies)|grosbeaks?|juncos?|phoebes?|pewees?|kingbirds?|grackles?|woodpeckers?|flickers?|\bswallows?|\bswifts?|\bowls?|parrots?|parakeets?|macaws?|cockatoos?|cockatiels?|lorikeets?|budgies?|budgerigars?|starlings?|mynas?|mynahs?|bulbuls?|thrush(es)?|thrashers?|vireos?|titmouse|titmice|\btits?|chickadees?|nuthatch(es)?|orioles?|tanagers?|flycatchers?|kingfishers?|kookaburras?|hoopoes?|hornbills?|toucans?|trogons?|quetzals?|motmots?|cuckoos?|roadrunners?|nightjars?|\bloons?|grebes?|penguins?|puffins?|albatross(es)?|petrels?|shearwaters?|gannets?|\bboob(y|ies)|skuas?|flamingos?|flamingoes|sandpipers?|plovers?|killdeers?|avocets?|stilts?|curlews?|godwits?|turnstones?|willets?|yellowlegs|dowitchers?|oystercatchers?|shrikes?|gnatcatchers?|sapsuckers?|towhees?|waxwings?|kinglets?|buntings?|meadowlarks?|\blarks?|wagtails?|pipits?|redstarts?|nightingales?|babblers?|weavers?|honeyeaters?|mallards?|\bteals?|wigeons?|mergansers?|\bscaups?|eiders?|ostrich(es)?|\bemus?|cassowar(y|ies)|kiwis?|\brheas?|bustards?)\b/],
    ['cat', /\b(cats?|kittens?|kitty|kitties|bobcats?|wildcats?|lynx|panthers?|cougars?|pumas?|lions?|tigers?|leopards?|cheetahs?|ocelots?|jaguars?|servals?|caracals?|margays?)\b/],
    ['dog', /\b(dogs?|pupp(y|ies)|fox(es)?|coyotes?|wol(f|ves)|jackals?|dingos?|dingoes|fennecs?|dholes?)\b/],
    ['deer', /\b(deer|reindeer|caribou|fawns?|bucks?|does?|stags?|horses?|pon(y|ies)|cows?|cattle|bulls?|ox|oxen|cal(f|ves)|goats?|sheep|lambs?|elk|moose|bison|buffalo(es)?|yaks?|donkeys?|mules?|zebras?|giraffes?|okapis?|camels?|llamas?|alpacas?|guanacos?|vicunas?|antelopes?|gazelles?|impalas?|kudus?|elands?|oryx(es)?|springboks?|gemsboks?|gnus?|wildebeests?|hartebeests?|duikers?|waterbucks?|dik-?diks?|muntjacs?|chamois|pronghorns?|bighorns?|ibex(es)?)\b/],
    ['rabbit', /\b(rabbits?|bunn(y|ies)|hares?|cottontails?|pikas?)\b/],
    ['plant', /(plants?|trees?|flowers?|\bmoss(es)?|ferns?|grass(es)?|\bvines?|shrubs?|bush(es)?|weeds?|palms?|palmettos?|\boaks?|\bpines?|magnolias?|sweetgums?|maples?|cypress|cedars?|holl(y|ies)|azaleas?|camellias?|berr(y|ies)|worts?|lil(y|ies)|roses?|orchids?|cactus|cacti|succulents?|\biv(y|ies)|creepers?|sumacs?|indigo|catbrier|greenbrier|catnip|cattails?|grapes?|apples?|plums?|\bpeas?|peanuts?|beans?|fruits?|chestnuts?|ardisia|beggarticks|bidens|lea(f|ves)|\bherbs?|basil|fennels?|tomato(es)?|\bmints?|\bsages?|balms?|blossoms?|seedlings?|saplings?|dais(y|ies)|clover|trefoils?|sorrels?|catchfl(y|ies)|sphagnum|bamboo|lantana|hibiscus|honeysuckles?|bromeliads?|tillandsia|dandelions?|thistles?|nettles?|tulips?|daffodils?|popp(y|ies)|lotus(es)?|agaves?|aloes?|yuccas?|eucalyptus|acacias?|baobabs?|birch(es)?|willows?|\belms?|beech(es)?|spruces?|\bfirs?|sequoias?|junipers?|mangroves?|lavender|\breeds?|sedges?|rushes|horsetails?|foxtails?|tickseeds?|frogfruits?|vincas?|\bfigs?|bananas?|wood|seaweeds?|kelp|alga(e)?)\b/]
  ];

  // global copies of the table's patterns, for finding every match in a name
  var LEXG = null;
  function kindOfName(text) {
    var t = String(text || '').toLowerCase().replace(/[‘’ʼ]/g, '\'').replace(/[^a-z' -]+/g, ' '), best = '', end = -1, len = 0, m, e;   // a phone's curly apostrophe is a plain one
    if (!LEXG) LEXG = LEX.map(function (L) { return new RegExp(L[1].source, 'g'); });
    for (var i = 0; i < LEX.length; i++) {
      LEXG[i].lastIndex = 0;
      while ((m = LEXG[i].exec(t))) {
        e = m.index + m[0].length;
        if (e > end || (e === end && m[0].length > len)) { best = LEX[i][0]; end = e; len = m[0].length; }
        if (!m[0].length) LEXG[i].lastIndex++;
      }
    }
    return best;                                   // '' where no word in it is a kind this page knows
  }

  // The words of the table, one plain form each, for catching a slip of the keys ("herron"). Made once from the patterns above.
  var LEXW = null;
  function lexWords() {
    if (LEXW) return LEXW; LEXW = [];
    LEX.forEach(function (L) {
      if (L[0] === 'person') return;
      L[1].source.replace(/\\b/g, '').replace(/^\(/, '').replace(/\)$/, '').replace(/\((\w+)\|\w+\)\??/g, '$1').replace(/\(\w+\)\?/g, '').replace(/(\w)\?/g, function (a, ch) { return ch === 's' ? '' : ch; })
        .split('|').forEach(function (w) { if (/^[a-z]{3,}$/.test(w)) LEXW.push([w, L[0]]); });
    });
    return LEXW;
  }
  function nearWords(text) {                       // kinds whose word is a slip of the keys from a word that was typed
    var out = [], seen = {};
    plain(text).split(' ').forEach(function (t) {
      if (t.length < 3) return; var lim = t.length <= 5 ? 1 : 2;
      lexWords().forEach(function (w) { if (!seen[w[0]] && Math.abs(w[0].length - t.length) <= lim && slips(t, w[0], lim) <= lim) { seen[w[0]] = 1; out.push({ en: w[0], sci: '', kind: w[1] }); } });
    });
    return out.slice(0, 3);
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
  // who gave the name: Claude, this page's small model, the full database on a server, the full database on this device, or the person
  function byOf(by) { return by === 'Claude' || by === 'page' || by === 'service' || by === 'device-large' ? by : 'you'; }
  function cleanMeeting(v, id) {
    if (!v || typeof v !== 'object') return null;
    var key = String(v.key || ''), mid = String(id || v.id || '');
    if (!EYES[key] || key === 'person' || !/^[A-Za-z0-9_-]{4,40}$/.test(mid)) return null;
    var thumb = typeof v.thumb === 'string' && v.thumb.length < 24000 && /^data:image\/jpeg;base64,[A-Za-z0-9+\/=]+$/.test(v.thumb) ? v.thumb : '';
    if (typeof v.common === 'string' && !v.sci && (v.common.toLowerCase() === handName(key).toLowerCase() || /^(a person|something alive)$/i.test(v.common))) v.common = v.common.toLowerCase();   // a group's name kept from an older build loses its capital
    if (typeof v.common === 'string' && v.sci) v.common = nameCase(v.common);   // a species' name kept from an older build is set in sentence case
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
    // the full database's place (placeOf in cam.rec.js) learns from a creature it named with confidence; a name corrected later is taken back
    if (typeof large !== 'undefined' && large.met) large.met(m.id, m.by === 'device-large' ? m.sci : '');
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
    if (ms <= 0) return 'This creature’s view has disappeared';
    d = Math.ceil(ms / 864e5);
    return ms <= 36e5 ? 'This is the last hour with this creature’s view' : ms <= 864e5 ? 'This is the last day with this creature’s view' : d >= 7 ? 'This creature’s view is yours for a week' : 'This creature’s view is yours for ' + d + ' more days';
  }
  function lentLine(m) {                           // the same, in a few words, for the moment of meeting and of looking again
    var ms = lentLeft(m), d = Math.ceil(ms / 864e5);
    return ms <= 0 ? '' : d >= 7 ? 'You can now see the world through this creature\u2019s eyes for a week.' : ms <= 864e5 ? 'The last day' : d + ' days left';
  }
  function ringOf(m, cls) {                        // a ring that empties over the week
    var f = Math.max(0, Math.min(1, lentLeft(m) / LEND_MS)), r = 6, c = 2 * Math.PI * r, s = svgEl('svg', { viewBox: '0 0 16 16', 'aria-hidden': 'true' });
    s.appendChild(svgEl('circle', { cx: 8, cy: 8, r: r, 'class': 'rest' }));
    s.appendChild(svgEl('circle', { cx: 8, cy: 8, r: r, 'class': 'left', 'stroke-dasharray': (c * f).toFixed(2) + ' ' + c.toFixed(2), transform: 'rotate(-90 8 8)' }));
    return s;
  }
  function latestOf(key) { for (var i = 0; i < record.length; i++) if (record[i].key === key) return record[i]; return null; }
  function paintRecordBits() {
    var t = 'Encounters' + (record.length ? ': ' + record.length : ''), n = record.length ? String(record.length) : '';
    $('introRecN').textContent = n; $('recAskAnimalN').textContent = n; $('introRec').setAttribute('aria-label', t); $('recAskAnimal').setAttribute('aria-label', t);
  }
  function renderRecord() {
    var met = {}, once = {}, n = record.length, k = 0, have = {};
    record.forEach(function (m) { if (KINDS.indexOf(m.key) >= 0) { once[m.key] = 1; if (lent(m)) met[m.key] = 1; } var g = g60Of(m); if (g) have[g] = 1; });
    KINDS.forEach(function (key) { if (met[key]) k++; });
    $('recordSub').textContent = '';
    var strip = $('eyeStrip'); strip.textContent = '';
    KINDS.forEach(function (key) {
      var b = el('button', 'eye'); b.type = 'button'; b.disabled = !met[key];
      b.setAttribute('aria-label', met[key] ? 'Look as ' + EYES[key].who : once[key] ? 'A creature you’ve already viewed the world as' : 'A creature you haven’t met yet');
      var g = eyeGlyph(key, !!once[key]), lm = latestOf(key), f, c = 2 * Math.PI * 11;   // a kind met once keeps its pupil, dimmed when This creature’s view has disappeared
      if (met[key]) { f = Math.max(.02, lentLeft(lm) / LEND_MS); g.appendChild(svgEl('circle', { cx: 12, cy: 12, r: 11, 'class': 'loan', 'stroke-dasharray': (c * f).toFixed(2) + ' ' + c.toFixed(2), transform: 'rotate(-90 12 12)' })); }
      b.appendChild(g);                                    // the outer ring is the week, emptying
      if (met[key]) b.addEventListener('click', function () { lookAgain(latestOf(key)); });
      strip.appendChild(b);
    });
    var ul = $('metList'); ul.textContent = '';
    record.slice(0, 150).forEach(function (m) {
      var li = el('li'), th, tx = el('div'), look = el('button', 'ico sm'), x = el('button', 'x', '×');
      if (m.thumb) { th = el('img', 'th'); th.alt = ''; th.src = m.thumb; } else th = el('span', 'th');
      tx.appendChild(el('span', 'nm', m.common));
      // what the eye reads is the name, the scientific name and the date; who named it and how long the eyes remain are said to a screen reader in words,
      // and shown as a ring with the days left
      var sm = el('span', 'sm', [m.sci, labelDate(new Date(m.at))].filter(Boolean).join(' · ')), days = el('span', 'days'), dl = Math.ceil(lentLeft(m) / 864e5);
      sm.appendChild(el('span', 'vh', ' · ' + [m.by === 'Claude' ? 'recognized by Claude' : m.by === 'page' ? 'named by this app' : m.by === 'service' ? 'named by the full database on a server' : m.by === 'device-large' ? 'named on this device by the full database' : '', lentSays(m)].filter(Boolean).join(' · ')));
      tx.appendChild(sm); days.appendChild(ringOf(m)); days.appendChild(document.createTextNode(dl + 'd')); days.setAttribute('aria-hidden', 'true');
      if (!lent(m)) li.className = 'gone';
      look.type = 'button'; look.setAttribute('aria-label', 'Look as ' + m.common);
      var sv = svgEl('svg', { viewBox: '0 0 24 24' }); sv.appendChild(svgEl('path', { d: 'M2.5 12s3.5-6.5 9.5-6.5S21.5 12 21.5 12s-3.5 6.5-9.5 6.5S2.5 12 2.5 12z' })); sv.appendChild(svgEl('circle', { cx: 12, cy: 12, r: 2.8 })); look.appendChild(sv);
      look.addEventListener('click', function () { lookAgain(m); });
      x.type = 'button'; x.setAttribute('aria-label', 'Forget the encounter with ' + m.common);
      x.addEventListener('click', function () {
        var yes = el('button', 'mini', 'Forget'), no = el('button', 'mini', 'Keep');
        yes.type = no.type = 'button'; li.textContent = ''; li.className = 'ask';
        li.appendChild(el('span', 'q', 'Forget the encounter with ' + m.common + '?')); li.appendChild(yes); li.appendChild(no);
        yes.addEventListener('click', function () { forgetMeeting(m.id); });
        no.addEventListener('click', renderRecord);
      });
      li.appendChild(th); li.appendChild(tx); if (lent(m) && !noViewOrPerson(m.key)) { li.appendChild(days); li.appendChild(look); } li.appendChild(x); ul.appendChild(li);   // no way to look where the eyes have gone back, or where there were never any
    });
    $('g60Sum').textContent = 'Gainesville’s sixty: ' + Object.keys(have).length + ' met';
    var ol = $('g60List'); ol.textContent = '';
    G60.forEach(function (r, i) { var li = el('li', have[i + 1] ? 'on' : '', have[i + 1] ? r[2] + ', ' + r[0] + ' records' : r[0] + ' records'); ol.appendChild(li); });
  }
  function openRecord() { renderRecord(); bigDelAsked = false; paintBig(); try { $('buildMark').textContent = aboutText(); } catch (e) {} show('claim', false); show('info', false); show('keep', false); openSheet('record'); $('record').scrollTop = 0; }

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
    if (!m || !EYES[m.key] || noViewOrPerson(m.key) || !lent(m)) return;      // encounters kept by older builds with a human or a creature of no group have no view
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

  // ---------- recognition in the page itself: the pocket recognizer, and the full database the person may fetch once
  // Outside Claude's viewer the page names the photo by itself: an image encoder run by ONNX Runtime Web in a worker
  // (vendor/rec-worker.js), and label vectors worked out beforehand. The files are described by models/<slot>/manifest.json
  // (docs/CONTRACTS.md). Nothing here is fetched before the opening screen is up, and nothing about a photo leaves the device.
  // Kept copies: every file is asked for with ?v=<version> and kept under that address, so a new version is a new address.
  // The runtime's version is its release number; a slot's version is a fingerprint of its manifest, which is always asked of the network first.
  // From build 9 the encoder is the exception where the manifest gives its checksum: it is asked for with ?v=sha256-<checksum>, so that
  // new heads or new settings (a new manifest) do not cost a second download of an encoder whose bytes have not changed.
  // There are two slots. The pocket one (models/pocket) is fetched by the page itself once the opening screen is up. The larger one
  // (models/naturalist) is some hundreds of megabytes, in parts that may live on another origin: nothing of it is fetched until the
  // person has said so, its parts are kept one by one so that a download carries on where it stopped, and its worker is started only
  // when a photo needs it and let go after a minute with nothing to do.
  var ORT = { v: '1.30.0', dir: 'vendor/ort/', js: 'ort.wasm.min.js', mjs: 'ort-wasm-simd-threaded.mjs', wasm: 'ort-wasm-simd-threaded.wasm', wasmBytes: 14239897, ep: 'wasm' };
  var KIND_ORDER = ['cat', 'dog', 'squirrel', 'deer', 'rabbit', 'hawk', 'wader', 'bird', 'alligator', 'reptile', 'frog', 'bee', 'insect', 'plant', 'other', 'person'];   // the order of KINDS in tools/fusion/fuse.py
  var onThisMachine = /^(localhost|127\.0\.0\.1)$/.test(location.hostname);
  function plain(x) { return String(x || '').toLowerCase().replace(/[^a-z' -]+/g, ' ').replace(/\s+/g, ' ').trim(); }
  function slips(a, b, lim) {                          // how many slips of the keys turn one word into the other: a letter wrong, missing, added, or two swapped
    var n = a.length, m = b.length, i, j, p2 = null, p = [], c, low;
    for (j = 0; j <= m; j++) p[j] = j;
    for (i = 1; i <= n; i++) {
      c = [i]; low = i;
      for (j = 1; j <= m; j++) {
        c[j] = Math.min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (a.charCodeAt(i - 1) === b.charCodeAt(j - 1) ? 0 : 1));
        if (p2 && i > 1 && j > 1 && a.charCodeAt(i - 1) === b.charCodeAt(j - 2) && a.charCodeAt(i - 2) === b.charCodeAt(j - 1)) c[j] = Math.min(c[j], p2[j - 2] + 1);
        if (c[j] < low) low = c[j];
      }
      if (low > lim) return lim + 1;
      p2 = p; p = c;
    }
    return p[m];
  }
  // ---------- where the phone probably is, for the full database of the whole world (docs/tracks/worlddb.md)
  // The same arithmetic as tools/world/place.py, which says why it is so. The page reads the phone's time zone and nothing else about the
  // place: no location is asked, and a photo's own location is never read. The first guess is the cells of the time zone (zones.json, from
  // the tz database and Natural Earth's countries); each creature the full database names with confidence in that zone moves it, by the
  // share of that species' records round each cell (place.bin). Those creatures are kept on this device, under their scientific names.
  //   place.bin: "RGPL", then little-endian u32 version, f32 res, u32 rows of cells, u32 columns, u32 species, u32 pairs, u32 bytes; the
  //   records of each cell (f32 a cell); then for each species a varint count of cells and, for each cell, the varint step from the cell
  //   before and the varint count of records (tools/world/prior.py writes it).
  var PLACE_KEY = 'seenback.place.v1', PLACE_KEEP = 200;
  function zoneNow() { try { return String(Intl.DateTimeFormat().resolvedOptions().timeZone || ''); } catch (e) { return ''; } }
  function placeOf(buf, zbuf, set, table, mine) {
    function bad(what) { var e = new Error('The full database’s download is damaged.'); e.code = 'damaged'; e.sentence = e.message; e.detail = what; throw e; }
    if (!buf || buf.byteLength < 32) bad('place file too short');
    var dv = new DataView(buf), b = new Uint8Array(buf), Z;
    if (b[0] !== 82 || b[1] !== 71 || b[2] !== 80 || b[3] !== 76 || dv.getUint32(4, true) !== 1) bad('not a place file');
    var res = dv.getFloat32(8, true), nr = dv.getUint32(12, true), nc = dv.getUint32(16, true), S = dv.getUint32(20, true), npairs = dv.getUint32(24, true), nbytes = dv.getUint32(28, true), n = nr * nc;
    if (S !== table.length || buf.byteLength !== 32 + 4 * n + nbytes || Math.abs(nr * res - 180) > 1e-3 || Math.abs(nc * res - 360) > 1e-3) bad('place file does not fit the table');
    try { Z = JSON.parse(new TextDecoder('utf-8').decode(zbuf)); } catch (e) { bad('zones are not JSON'); }
    if (!Z || typeof Z.zones !== 'object' || Math.abs((+Z.res || 0) - res) > 1e-6) bad('zones do not fit the place file');
    var T = new Float64Array(n), i, P0 = 32 + 4 * n, start = new Uint32Array(S + 1), p = P0, s, k, m, v, mul, cnt;
    for (i = 0; i < n; i++) T[i] = dv.getFloat32(32 + 4 * i, true);
    function vint() { var x = 0; mul = 1; do { v = b[p++]; x += (v & 127) * mul; mul *= 128; } while (v & 128); return x; }
    for (s = 0, cnt = 0; s < S; s++) { start[s] = p; m = vint(); cnt += m; for (k = 0; k < m; k++) { vint(); vint(); } }
    start[S] = p;
    if (p !== P0 + nbytes || cnt !== npairs) bad('place file of the wrong length');
    var R = 6371.0088, D = Math.PI / 180, lat = new Float64Array(nr), radius = set.radius_km, eps = set.eps, K = new Int32Array(nr * nr), span;
    for (i = 0; i < nr; i++) lat[i] = -90 + (i + 0.5) * res;
    (function () {                                     // K[r * nr + r2]: the columns of row r2 within the radius of a cell of row r, by how far they may lie
      var r, r2, j, h, d, last, half = Math.floor(nc / 2);
      for (r = 0; r < nr; r++) for (r2 = 0; r2 < nr; r2++) {
        last = -1;
        for (j = 0; j <= half; j++) {
          h = Math.pow(Math.sin((lat[r2] - lat[r]) * D / 2), 2) + Math.cos(lat[r] * D) * Math.cos(lat[r2] * D) * Math.pow(Math.sin(j * res * D / 2), 2);
          d = 2 * R * Math.asin(Math.sqrt(Math.min(1, h)));
          if (d <= radius) last = j; else break;
        }
        K[r * nr + r2] = last >= half ? nc : last;
      }
    })();
    span = Math.ceil(radius / (111.19 * res)) + 1;
    function discSum(x) {                              // for every cell, the sum of x over the cells whose centres lie within the radius of its centre
      var out = new Float64Array(n), cs = new Float64Array(3 * nc + 1), r, r2, c, kk, tot, base;
      for (r2 = 0; r2 < nr; r2++) {
        base = r2 * nc; tot = 0;
        for (c = 0; c < nc; c++) tot += x[base + c];
        if (tot === 0) continue;
        cs[0] = 0; for (c = 0; c < 3 * nc; c++) cs[c + 1] = cs[c] + x[base + (c % nc)];
        for (r = Math.max(0, r2 - span); r <= Math.min(nr - 1, r2 + span); r++) {
          kk = K[r * nr + r2]; if (kk < 0) continue;
          if (kk >= nc || 2 * kk + 1 >= nc) { for (c = 0; c < nc; c++) out[r * nc + c] += tot; continue; }
          for (c = 0; c < nc; c++) out[r * nc + c] += cs[nc + c + kk + 1] - cs[nc + c - kk];
        }
      }
      return out;
    }
    var N = discSum(T), world = new Float64Array(n), sumT = 0;
    for (i = 0; i < n; i++) sumT += T[i] + 1;
    for (i = 0; i < n; i++) world[i] = (T[i] + 1) / sumT;
    function zoneName(z) { if (!z) return ''; if (Z.zones[z]) return z; var a = Z.alias && Z.alias[z]; return a && Z.zones[a] ? a : ''; }
    function firstGuess(z) {
      var zz = zoneName(z), P = new Float64Array(n), w, cells, j, tot = 0;
      if (!zz) { P.set(world); return P; }
      cells = Z.zones[zz][0]; w = Z.zones[zz][1];
      for (j = 0; j < n; j++) P[j] = eps * world[j];
      for (j = 0; j < cells.length; j++) P[cells[j]] += (1 - eps) * w[j];
      for (j = 0; j < n; j++) tot += P[j];
      for (j = 0; j < n; j++) P[j] /= tot;
      return P;
    }
    function localCounts(sp) {
      var x = new Float64Array(n), cell = 0, mm, j;
      p = start[sp]; mm = vint();
      for (j = 0; j < mm; j++) { cell += vint(); x[cell] += vint(); }
      return discSum(x);
    }
    function update(P, sp) {                           // the encounter rule: P(c) times the share of sp round c, normalized
      var L = localCounts(sp), lp = new Float64Array(n), mx = -Infinity, j, tot = 0;
      for (j = 0; j < n; j++) { lp[j] = Math.log(Math.max(P[j], 1e-300)) + Math.log((L[j] + 1) / (N[j] + S)); if (lp[j] > mx) mx = lp[j]; }
      for (j = 0; j < n; j++) { lp[j] = Math.exp(lp[j] - mx); tot += lp[j]; }
      for (j = 0; j < n; j++) lp[j] /= tot;
      return lp;
    }
    function logShare(P) {                             // log share(s), share(s) = sum over cells of P(c) (n_c(s) + 1) / (N_c + S)
      var w = new Float64Array(n), W, sw = 0, out = new Float64Array(S), j, mm, cell, acc, sp;
      for (j = 0; j < n; j++) { w[j] = P[j] / (N[j] + S); sw += w[j]; }
      W = discSum(w); p = P0;
      for (sp = 0; sp < S; sp++) { mm = vint(); cell = 0; acc = 0; for (j = 0; j < mm; j++) { cell += vint(); acc += vint() * W[cell]; } out[sp] = Math.log(acc + sw); }
      return out;
    }
    // the creatures met, kept on this device: {id (the meeting's), sci, zone, at}
    var rowOf = null, cache = { key: null, prior: null, P: null };
    function row(sci) { if (!rowOf) { rowOf = new Map(); table.forEach(function (t, j) { if (!rowOf.has(t.sci)) rowOf.set(t.sci, j); }); } return rowOf.has(sci) ? rowOf.get(sci) : -1; }
    function kept() { try { var j = JSON.parse(localStorage.getItem(PLACE_KEY) || 'null'); return j && Array.isArray(j.met) ? j.met.filter(function (x) { return x && typeof x.sci === 'string' && typeof x.zone === 'string'; }) : []; } catch (e) { return []; } }
    function keep(list) { try { localStorage.setItem(PLACE_KEY, JSON.stringify({ v: 1, met: list.slice(-PLACE_KEEP) })); } catch (e) {} }
    function metHere(z) {                              // the rows of the creatures met in this time zone, each species once, in the order met
      var seen = {}, out = [];
      kept().forEach(function (x) { var r = x.zone === z ? row(x.sci) : -1; if (r >= 0 && !seen[r]) { seen[r] = 1; out.push(r); } });
      return out;
    }
    function now() {
      var z = zoneNow(), met = metHere(z), key = z + '|' + met.join(','), P, j;
      if (cache.key !== key) {
        P = firstGuess(z);
        for (j = 0; j < met.length; j++) P = update(P, met[j]);
        cache = { key: key, P: P, prior: null, zone: z, known: !!zoneName(z), met: met.length };
      }
      return cache;
    }
    return {
      prior: function () { var c = now(); if (!c.prior) c.prior = logShare(c.P); return c.prior; },
      // a meeting named, renamed or unnamed: only a name the full database gave with confidence counts, once a meeting
      met: function (id, sci) {
        if (!mine) return;
        var list = kept().filter(function (x) { return x.id !== id; });
        if (sci && row(sci) >= 0) list.push({ id: String(id || ''), sci: sci, zone: zoneNow(), at: Date.now() });
        keep(list);
      },
      about: function () { var c = now(); return { zone: c.zone, known: c.known, met: c.met, cells: n, res: res }; },
      test: { firstGuess: firstGuess, update: update, logShare: logShare, now: function () { return now().P; }, row: row, discSum: discSum, N: N, T: T }
    };
  }
  function recognizer(o) {                             // o.slot: where the manifest is, or 'off'; o.big: the full database
    var big = !!o.big, slot = o.slot;
    var manifestUrl = /\.json$/.test(slot) ? slot : slot.replace(/\/$/, '') + '/manifest.json';
    var cannot = inViewer ? 'off' : slot === 'off' || /\.\.|^\/|\/\//.test(slot) ? 'off'
      : (typeof Worker !== 'function' || typeof WebAssembly !== 'object' || typeof fetch !== 'function' || typeof Float32Array !== 'function') ? 'browser'
      : (big && !window.caches) ? 'browser' : '';      // the full database has to be kept, and this browser keeps nothing
    var SAY = {
      off: 'IDing is turned off.',
      absent: 'This app can’t ID photos yet.',
      missing: 'Some of this app’s files are missing. Close the app and open it again.',
      network: 'This app’s download is incomplete. Check your connection, then close the app and open it again.',
      damaged: 'This app’s download is damaged. Close the app and open it again.',
      unfit: 'This app’s files are out of date. Close the app and open it again to update.',
      browser: 'This browser is too old to ID photos. Try a current Chrome, Safari, or other browser.',
      died: 'This app’s IDing has crashed. Check that your device has enough memory.',
      slow: 'The IDing timed out. Try again.',
      photo: 'That photo couldn’t be read. Try again.'
    };
    if (big) {
      SAY.off = 'The full database is switched off.'; SAY.absent = 'This app has no full database yet.'; SAY.missing = 'The full database\u2019s files are missing.';
      SAY.network = 'The full database’s download was interrupted.'; SAY.damaged = 'The full database\u2019s download is damaged.'; SAY.unfit = 'The full database does not fit this build of the app. Download the latest version of the app.';
      SAY.browser = 'This browser cannot run the full database.'; SAY.died = 'The full database crashed. Check that your device has enough memory.'; SAY.slow = 'The full database timed out. Try again.'; SAY.photo = 'The full database failed on that photo. Try a different photo. Try a different photo.';
      SAY.room = 'There is not enough storage on this device for the full database.';
      SAY.keep = 'The full database could not be kept on this device.';
      SAY.stopped = 'The download has been stopped.';
    }
    var KEEP = 'keep-v1', EPS = 1e-9;
    var state = cannot ? 'failed' : 'idle', why = cannot, M = null, ver = '', base = '', cur = null, worlds = [], worker = null, loadP = null, loadMs = 0, info = { backend: '', threads: 0 };
    var got = 0, total = 0, pending = {}, nextId = 1, last = null, lastFail = '', onProgress = null, watchMs = big ? 120000 : 45000, netWaitMs = 6000, api;
    // the full database only: what of it is kept, the download under way, and the rest it takes after a minute with nothing to do
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
    // The full database for the whole world (docs/tracks/worlddb.md) brings more than its encoder from another origin: its rows at one byte a
    // number in parts, a scale for each row, its table of names, the records of each species on a world grid and the cells of each time zone.
    // Each is a group of parts, fetched, checked and kept as the encoder's parts are. A file named by a plain address stays in the slot.
    function far(x) { return !!x && typeof x === 'object' && (Array.isArray(x.parts) || typeof x.url === 'string'); }
    function groupsOf(m) {
      var g = [{ key: 'vision', V: m.vision }], sp = m.species, pl = m.place;
      if (sp && Array.isArray(sp.parts)) g.push({ key: 'rows', V: sp });
      if (sp && far(sp.scale)) g.push({ key: 'scale', V: sp.scale });
      if (sp && far(sp.table)) g.push({ key: 'table', V: sp.table });
      if (pl) { g.push({ key: 'place', V: pl }); g.push({ key: 'zones', V: pl.zones }); }
      return g;
    }
    function allParts(m) { var out = []; groupsOf(m).forEach(function (g) { out = out.concat(partsOf(g.V)); }); return out; }
    function bytesOf(m) { return allParts(m).reduce(function (a, p) { return a + p.bytes; }, 0); }
    function okGroup(V) {                              // parts that add up to the whole, each with its length
      var sum = 0, P = partsOf(V);
      return P.length > 0 && num(V.bytes) && P.every(function (p) { sum += p && p.bytes; return p && okPart(p.url) && num(p.bytes) && p.bytes > 0 && (p.sha256 === undefined || typeof p.sha256 === 'string'); }) && sum === V.bytes;
    }
    function readManifest(text) {
      var m; try { m = JSON.parse(text); } catch (e) { throw err('damaged', 'manifest is not JSON'); }
      var v = m && m.vision, f = m && m.fusion, k = m && m.kinds, sp = m && m.species, pl = m && m.place;
      if (!v || !f || !num(m.width) || !num(v.size) || !Array.isArray(v.mean) || !Array.isArray(v.std) || !(v.url || Array.isArray(v.parts))) throw err('unfit', 'manifest lacks a field');
      // a slot may come without a kinds head: then the kind is taken from the species answer, and the species are not optional
      if (k ? !(Array.isArray(k.labels) && k.url && num(f.t_kind)) : !sp) throw err('unfit', 'manifest lacks a field');
      if (k && k.labels.some(function (l) { return l !== 'none' && !EYES[l]; })) throw err('unfit', 'a kind this page does not know');
      if (sp && !((sp.url || Array.isArray(sp.parts)) && sp.table && num(sp.count) && num(f.t_species) && num(f.alpha_prior) && (!k || num(f.w_kind)) && num(f.name_at) && num(f.offer_at))) throw err('unfit', 'species without their settings');
      // rows at one byte a number carry a scale for each row; a database for the world carries its place files, and only the full database may
      if (sp && sp.dtype !== undefined && sp.dtype !== 'f16' && sp.dtype !== 'int8') throw err('unfit', 'species rows of a kind this page does not know');
      if (sp && sp.dtype === 'int8' && !far(sp.scale)) throw err('unfit', 'rows at one byte a number without their scale');
      if (sp && (Array.isArray(sp.parts) || far(sp.scale) || far(sp.table) || pl) && !big) throw err('unfit', 'a database in parts in the pocket slot');
      if (pl && !(far(pl) && far(pl.zones) && num(pl.radius_km) && pl.radius_km > 0 && num(pl.eps) && pl.eps > 0 && pl.eps < 1)) throw err('unfit', 'place files without their settings');
      if (big && sp && !groupsOf(m).slice(1).every(function (g) { return okGroup(g.V); })) throw err('unfit', 'the parts do not add up to the whole');
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
      if (big ? !(num(v.bytes) && v.bytes > 0 && partsOf(v).every(function (p) { return okPart(p.url); })) : v.parts !== undefined) throw err('unfit', big ? 'the full database without its length' : 'a model in parts in the pocket slot');
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
    function encV(V) { return V && !V.parts && typeof V.sha256 === 'string' && /^[0-9a-f]{64}$/i.test(V.sha256) ? 'sha256-' + V.sha256.toLowerCase() : ''; }   // the encoder's own version, where its checksum is given
    function prune(cache, v) {                         // older versions of this slot and of the runtime are let go; the encoder in use stays under its checksum
      if (!cache) return;
      var ev = M ? encV(M.vision) : '';
      cache.keys().then(function (keys) {
        keys.forEach(function (req) {
          var u; try { u = new URL(req.url); } catch (e) { return; }
          var q = /[?&]v=([^&]+)/.exec(u.search), here = u.href.split('?')[0];
          if (!q) return;
          if (here.indexOf(base) === 0 && here.slice(base.length).indexOf('/') < 0 && decodeURIComponent(q[1]) !== v && !(ev && decodeURIComponent(q[1]) === ev && here === abs(M.vision.url, base))) cache.delete(req);
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

    // ---------- a model in parts (the full database)
    // A part is kept under an address of this slot made from its checksum, so the same bytes are never fetched twice, wherever they came from.
    function partKey(p) { return base + 'part/' + (p.sha256 ? String(p.sha256).toLowerCase() : fingerprint(String(p.url))) + '?bytes=' + p.bytes; }
    function wholeKey(V) { return base + 'whole/' + String(V.sha256 || '').toLowerCase(); }
    function unkeepParts() {
      have = 'absent'; keptBytes = 0;
      return Promise.all(allParts(M).map(function (p) { return unkeep(partKey(p)); }).concat(groupsOf(M).map(function (g) { return unkeep(wholeKey(g.V)); })));
    }
    function staleParts(cache) {                       // parts of a model this slot no longer names
      if (!cache || !M) return;
      var now = {}; allParts(M).forEach(function (p) { now[partKey(p).split('?')[0]] = 1; }); groupsOf(M).forEach(function (g) { now[wholeKey(g.V)] = 1; });
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
        if (!V.sha256 || (P.length === 1 && P[0].sha256 === V.sha256)) return;
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
    // What of the full database is on this device: 'none' (there is no such model, or it cannot be used here), 'absent', 'partial', 'getting', 'kept'.
    // The manifest is asked for the first time this is called, and never before.
    function survey(fresh) {
      if (cannot || gone) return Promise.resolve('none');
      if (!fresh && getP) return Promise.resolve('getting');
      if (!fresh && have) return Promise.resolve(have);
      if (!surveyP) surveyP = keepOpen().then(function (cache) {
        return (M ? Promise.resolve() : manifestText(cache).then(adopt)).then(function () {
          var P = allParts(M);
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
        var P = allParts(M), i = 0;
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
        return room(Math.max(0, bytesOf(M) - keptBytes)).then(next);
      }).then(function () {
        have = 'kept'; staleParts(store); notify();
        return ready();
      }).then(function () { getP = null; getCtl = null; diag('large-kept', M.id + ' ' + bytesOf(M)); notify(); }, function (e) {
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
    function rest() {                                  // nothing has needed the full database for a minute: its worker, and the memory it holds, are let go
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
        if (big && M) return null;                     // the full database's worker is started again and again; its manifest is read once
        return manifestText(cache).then(adopt);
      }).then(function () {
        var V = M.vision, nK = M.kinds ? M.kinds.labels.length : 0, sp = M.species, nS = sp ? sp.count : 0, c = cacheRef, i8 = !!sp && sp.dtype === 'int8';
        var inParts = big || !!V.parts, modelUrl = inParts ? '' : encV(V) ? withV(abs(V.url, base), encV(V)) : u(V.url);
        function rowsLen(buf) { if (buf && buf.byteLength !== nS * M.width * (i8 ? 1 : 2)) throw err('damaged', 'species rows of the wrong length'); return buf; }
        return (inParts ? Promise.resolve(true) : kept(c, modelUrl)).then(function (hit) {
          fromKeep.model = !!hit;
          return Promise.all([
            file(c, withV(abs(ORT.dir + ORT.wasm), ORT.v), ORT.wasmBytes),
            inParts ? joined(c, V) : file(c, modelUrl, num(V.bytes) ? V.bytes : 0, sha256(V.sha256)),
            M.kinds ? file(c, u(M.kinds.url), nK * M.width * 2) : null,
            sp ? (Array.isArray(sp.parts) ? joined(c, sp) : file(c, u(sp.url), nS * M.width * (i8 ? 1 : 2))).then(rowsLen) : null,
            sp ? (far(sp.table) ? joined(c, sp.table) : file(c, u(sp.table), 0)) : null,
            sp && sp.bias_url ? file(c, u(sp.bias_url), nS * 4) : null,
            i8 ? (far(sp.scale) ? joined(c, sp.scale) : null) : null,
            M.place ? joined(c, M.place) : null,
            M.place ? joined(c, M.place.zones) : null
          ]);
        }).then(function (b) {
          cur = slotOf(M, sp ? readTable(b[4], nS) : null, b[5] ? floats(b[5], nS) : null);
          if (i8 && (!b[6] || b[6].byteLength !== nS * 4)) throw err('damaged', 'species scales of the wrong length');
          if (M.place) cur.place = placeOf(b[7], b[8], M.place, cur.table, big);   // where the phone probably is: its time zone, and the creatures met
          total = got;                                 // the downloads are over; what remains is starting the encoder
          notify();
          var init = { op: 'init', ep: ORT.ep, ort: { js: withV(abs(ORT.dir + ORT.js), ORT.v), mjs: withV(abs(ORT.dir + ORT.mjs), ORT.v), wasm: withV(abs(ORT.dir + ORT.wasm), ORT.v) },
            wasmBinary: b[0], model: b[1], vision: { input: V.input || 'pixel_values', output: V.output || 'image_embeds', size: V.size, mean: V.mean, std: V.std, resize: V.resize, crop: V.crop || 'center' },
            width: M.width, kinds: b[2], nKinds: nK, species: b[3], nSpecies: nS, speciesType: i8 ? 'int8' : 'f16', speciesScale: i8 ? b[6] : null };
          // a model in parts has passed its checksums by now: if the encoder will not take it, the fault is not in the bytes, and they are kept
          return startWorker(init, [b[0], b[1]].concat(b[2] ? [b[2]] : [], b[3] ? [b[3]] : [], i8 ? [b[6]] : []), inParts && V.sha256 ? 'browser' : 'damaged').catch(function (e) {
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
      if (c.place) return c.place.prior();             // a database for the world: the share of each species where the phone probably is (placeOf)
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
    //   A slot without a kinds head (the full database): kd is not used, and a kind's score is its share of the species answer.
    // The n likeliest rows (that pass `pred`), most likely first and the earlier row first where two are equal: what a stable sort of every
    // row would put first, in one pass, since the full database has hundreds of thousands of rows.
    function top(s, n, pred) {
      var best = [], i, j, v;
      for (i = 0; i < s.length; i++) {
        if (pred && !pred(i)) continue;
        v = s[i];
        if (best.length === n && !(v > s[best[n - 1]])) continue;
        for (j = best.length; j > 0 && s[best[j - 1]] < v; j--);
        best.splice(j, 0, i); if (best.length > n) best.pop();
      }
      return best;
    }
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
        for (i = 0; i < s.length; i++) q[table[i].kind] = (q[table[i].kind] || 0) + s[i];
        order = top(s, 5);
        species = order.map(function (j) { return { sci: table[j].sci, en: table[j].en, p: s[j], kind: table[j].kind }; });
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
          var three = (f.offer_any_kind ? top(s, 3) : top(s, 3, function (j) { return table[j].kind === kind; })).map(function (j) { return { sci: table[j].sci, en: table[j].en, p: s[j], kind: table[j].kind }; });
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
            // a database for the world names anywhere, with the prior of its place (placeOf); a county's list only near the county
            var t = performance.now(), month = new Date().getMonth(), away = pocket.local === false, local = cur.place ? true : !away && !!cur.table;
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
      var p = queue.then(run, run); queue = p.catch(function () {}).then(tire); return p;     // one photo at a time through the full database
    }
    function mb(n) { return Math.max(0, Math.round(n / 1e6)); }
    function line() {
      if (big) return !(getP && M) ? 'Looking more closely\u2026' : have === 'kept' ? 'Checking the full database\u2026' : 'Downloading the full database\u2026 ' + mb(keptBytes + partGot) + ' of ' + Math.max(1, mb(bytesOf(M))) + ' MB';
      if (state === 'loading' && total > got) return 'Downloading\u2026 ' + mb(got) + ' of ' + Math.max(1, mb(total)) + ' MB';
      return 'Looking\u2026';
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
      met: function (id, sci) { if (cur && cur.place) cur.place.met(id, sci); },     // a meeting's name: kept where the full database gave it with confidence
      // A typed name looked up in the species list: the species it names exactly, the species whose names hold every word of it, and the
      // species whose names are a slip of the keys away. The most recorded come first. Empty where there is no list.
      find: function (q) {
        var t = cur && cur.table, s = plain(q), out = { exact: null, has: [], near: [] }, ws, lim, best = -1;
        if (!t || s.length < 3) return out;
        ws = s.split(' '); lim = s.length <= 5 ? 1 : 2;
        t.forEach(function (r) {
          var en = plain(r.en), sci = plain(r.sci), w = 0, i;
          if (r.m) for (i = 0; i < 12; i++) w += r.m[i];
          if (en === s || sci === s) { if (w > best) { best = w; out.exact = r; } return; }
          if (ws.every(function (x) { return (' ' + en + ' ').indexOf(' ' + x) >= 0 || (' ' + sci + ' ').indexOf(' ' + x) >= 0; })) { out.has.push([w, r]); return; }
          if ((en && Math.abs(en.length - s.length) <= lim && slips(s, en, lim) <= lim) || (sci && Math.abs(sci.length - s.length) <= lim && slips(s, sci, lim) <= lim)) out.near.push([w, r]);
        });
        function top(a) { return a.sort(function (x, y) { return y[0] - x[0]; }).slice(0, 3).map(function (x) { return x[1]; }); }
        out.has = top(out.has); out.near = top(out.near); return out;
      },
      progress: function (fn) { onProgress = fn; },
      // the full database: what of it is here, fetching it, stopping, deleting; its size and, where the manifest gives one, a measured time for a photo
      survey: survey, get: get, halt: halt, forget: forget, say: function (code) { return SAY[code] || SAY.died; },
      has: function () { return getP ? 'getting' : have; },
      broken: function () { return state === 'failed' && (why === 'browser' || why === 'unfit'); },   // it has shown that it cannot run here: not tried again for every photo
      size: function () { var n = M ? (big ? bytesOf(M) : M.vision.bytes || 0) : 0; return M ? { bytes: n, kept: keptBytes + partGot, mb: Math.max(1, mb(n)), keptMb: mb(keptBytes + partGot), seconds: M.seconds_a_photo || null } : null; },
      offers: [], kindOffers: [], file: null, local: true, wantPre: false, lastEmb: null, lastPre: null, lastDots: null,
      about: function () { return { state: state, why: why, fail: lastFail, model: M ? M.id : '', rule: M ? (M.fusion.rule || 'product') : '', trained: !!(cur && (cur.kb || cur.sb)), backend: info.backend, threads: info.threads, loadMs: Math.round(loadMs), start: info.ms || null, last: last, got: got, total: total, slot: manifestUrl, fitted: M && M.fitted_on && typeof M.fitted_on === 'object' ? M.fitted_on : null,
        have: getP ? 'getting' : have, keptBytes: keptBytes + partGot, bytes: M ? (big ? bytesOf(M) : M.vision.bytes || 0) : 0, getFail: getFail, place: cur && cur.place ? cur.place.about() : null }; },
      test: { kill: function (how) { if (worker) worker.postMessage({ op: 'die', how: how }); }, watch: function (ms) { watchMs = ms; }, forget: function () { stop('died', 'forgotten by a check'); state = 'idle'; why = ''; },
        idle: function (ms) { idleMs = ms; tire(); }, netWait: function (ms) { netWaitMs = ms; }, running: function () { return !!worker; },
        place: function () { return cur && cur.place ? cur.place.test : null; },
        // the scoring with settings given by a check, through the same readers as a real slot (tools/fusion/parity.py)
        world: function (m, rows, sb) { worlds.push(slotOf(readManifest(JSON.stringify(m)), rows ? readTable(new TextEncoder().encode(JSON.stringify({ species: rows })).buffer, rows.length) : null, sb ? Float64Array.from(sb) : null)); return worlds.length - 1; },
        fuseIn: function (w, kd, sd, month) { return fuseWith(worlds[w], kd, sd, month); } }
    };
    return api;
  }
  var pocket = recognizer({ slot: (/[?&]rec=([A-Za-z0-9_.\/-]+)/.exec(location.search || '') || [0, 'models/pocket'])[1] });
  // The full database's slot. A check on this machine may name another slot, or switch it off; a link to the public page may not.
  var large = recognizer({ big: true, slot: ((onThisMachine ? /[?&]big=([A-Za-z0-9_.\/-]+)/.exec(location.search || '') : null) || [0, 'models/naturalist'])[1] });

  // ---------- the species service (the naturalist): the full database on a server, asked only with the person's say-so
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
  function anySheet() { return !$('claim').hidden || !$('notice').hidden || !$('contact').hidden || !$('aboutSheet').hidden || !$('record').hidden || !$('info').hidden || !$('keep').hidden || !$('ask').hidden || !$('big').hidden; }
  function closeSheets() {
    var wasClaim = !$('claim').hidden || !$('notice').hidden;
    show('notice', false); show('contact', false); show('claim', false); show('record', false); show('aboutSheet', false); show('info', false); show('keep', false); show('ask', false); show('big', false); show('scrim', false);
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
    var kinds = (pocket.kindOffers || []).filter(function (k) { return k !== 'other' && k !== 'none'; }), kbox = $('claimKinds'); kbox.textContent = '';   // not sure of the kind: its likeliest, as buttons above the typed field; a creature of no known group is never a choice (build 22)
    $('claimSub').textContent = sub || ''; $('claimName').value = ''; $('claimNote').textContent = ''; show('claimSuggestRow', false); show('claimAboutRow', false);   // the field's own words say what to type
    kinds.forEach(function (key) {
      var name = key === 'person' ? 'a human' : handName(key), b = el('button', 'pill ghost', name); b.type = 'button';
      b.addEventListener('click', function () { diag('kind-offer', key); reveal(key, { common: name, scientific: '', by: 'you' }); });
      kbox.appendChild(b);
    });
    show('claimKindBox', kinds.length > 0); $('claimOfferNote').textContent = kinds.length ? 'Or one of these species:' : 'Is it one of these?';
    var offers = offerList(pocket.offers || []), box = $('claimOffers'); box.textContent = '';      // what the small model could not choose between
    offers.forEach(function (o) {
      var b = el('button', 'pill ghost', o.label); b.type = 'button';
      b.addEventListener('click', function () { diag('offer', o.kind); reveal(o.kind, { common: nameCase(clip(o.en || o.sci, 60)), scientific: clip(o.sci, 80), by: 'you', local: !!o.local }); });
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
    return keep.map(function (o) { return { sci: o.sci, en: o.en, kind: o.kind, local: o.local, label: o.en && o.sci && n[low(o.en)] > 1 ? nameCase(o.en) + ' (' + o.sci + ')' : (o.sci ? nameCase(o.en) : o.en) || o.sci }; });
  }
  function setViewPrompt(key) {
    $('askViewH').textContent = 'View the world as ' + EYES[key].who + '.';   // EYES.other.who is "this one", which reads badly here
    $('askViewText').textContent = '';
    $('askViewFine').textContent = '';
  }

  var REGARDS = '<em>Regards</em>';
  function tell(html) {                            // a plain notice over the photographing screen; closing it leaves the person where a new photo can be taken or chosen
    msg(''); closeSheets(); dropSvc(); setEyes(null);
    if (S.src === 'cam') go('finder'); else go('naming');
    $('noticeText').innerHTML = html; openSheet('notice'); paintType();
  }
  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function noViewSays(name) { return REGARDS + ' doesn\u2019t have the ability to view the world as ' + (name && !/^this /.test(name) ? esc(aAn(name)) : 'this creature') + ' right now. We\u2019re adding new species all the time. In the meantime, try another creature.'; }
  var HUMAN_SAYS = 'That\u2019s a human. You already see the world as one. Try photographing another creature.';
  function reveal(key, named) {
    if (key === 'person') {                        // a human: no view to change into and no encounter kept; the identifying screen stays (build 22)
      diag('person', ''); S.seq++; tell(HUMAN_SAYS); return;
    }
    if (noView(key)) {                             // a living thing with no view of its own: named where the app knows its group, and no encounter kept
      var nm = named && named.scientific ? named.common : named && named.by === 'you' ? named.common : '';
      if (!nm && key !== 'other') nm = handName(key);
      diag('no-view', clip((named && named.common) || key, 60)); S.seq++; tell(noViewSays(nm)); return;
    }
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
  function failName(why) { askName(why + ' Tell us what’s there.'); }
  // While the recognizer is being downloaded for the first time, the person may type the name and not wait. The download carries on.
  function paintType() { show('barType', !inViewer && S.screen === 'naming' && !S.eyes && !anySheet() && pocket.fetching()); }
  function identify() {
    if (!S.animalPhoto) return;
    var t = ++S.token; S.seq++;
    if (!capsSettled) { go('naming'); msg('Looking\u2026'); }     // Claude's part of the page may still be arriving
    capsReady.then(function () { if (t === S.token) recognize(t); });
  }
  function recognizeHere(t) {                      // outside Claude: the page's own small model, on this device
    go('naming'); msg(pocket.line()); paintType();
    pocket.progress(function () { if (t === S.token && S.screen === 'naming' && !S.eyes && !anySheet()) msg(pocket.line()); paintType(); });
    pocket.recognize(S.animalPhoto, pocket.file).then(function (r) {
      if (t !== S.token) return;
      diag('pocket', JSON.stringify({ kind: r.kind, p: +r.kindP.toFixed(3), sp: r.species.slice(0, 3).map(function (x) { return [x.sci, +x.p.toFixed(3)]; }), ms: r.ms, model: r.model, backend: r.backend }).slice(0, 400));
      if (r.kind === 'none' && r.sure) {             // nothing alive, says the small model: where the full database is on this device it looks before the person is told
        pocket.offers = []; pocket.kindOffers = [];
        large.survey().then(function (h) { if (t !== S.token || S.eyes) return; if (h === 'kept' && !large.broken()) firstLook(t, false); else tell('We can\u2019t find a creature in your photo. Try again.'); });
        return;
      }
      pocket.offers = r.offers.map(function (o) { return { sci: o.sci, en: o.en, kind: o.kind, local: true }; });
      pocket.kindOffers = r.kindOffers || [];
      if (!r.sure) {
        // Not sure is an answer: no kind is asserted and no eyes change. Where the full database is on this device it is asked before the person is.
        diag('not-sure', r.kind + ' ' + r.kindP.toFixed(3));
        large.survey().then(function (h) {
          if (t !== S.token || S.eyes) return;
          if (h === 'kept' && !large.broken()) firstLook(t, true); else askName('We\u2019re not sure what kind of creature that is.');
        });
        return;
      }
      var common = r.kind === 'person' ? 'a human' : r.named ? (r.named.en || r.named.sci) : handName(r.kind);
      reveal(r.kind, { common: (r.named ? nameCase(clip(common, 60)) : clip(common, 60)) || handName(r.kind), scientific: r.named ? clip(r.named.sci, 80) : '', by: 'page', local: !!r.named });
      closer(t, !!r.named);                                                // the kind is in use at once; a finer name may follow from the full database
    }, function (e) {
      if (t !== S.token) return;
      diag('pocket-error', String((e && e.code) || 'unknown'));
      failName((e && e.sentence) || 'The IDing isn’t working right now.');
    });
  }
  function recognize(t) {
    if (!inViewer && pocket.usable()) { recognizeHere(t); return; }
    if (!(sample && canImages)) {
      msg(''); if (S.src !== 'cam') go('naming'); else go('finder');
      diag('no-recognizer', inViewer ? (sample ? 'no-images' : 'no-sample') : 'outside');
      openClaim(inViewer ? 'Claude could not be reached from this view, so you tell it.' : (pocket.whyNot() || 'This page cannot recognize a photo here.') + ' Tell us what’s there.');
      return;
    }
    if (nameCtl) nameCtl.abort();
    nameCtl = new AbortController(); var ctl = nameCtl;
    go('naming'); msg('Looking\u2026');
    var slow = setTimeout(function () { if (t === S.token && S.screen === 'naming' && !S.eyes) msg('Still looking\u2026 If Claude asked your permission, answer it, or go back.'); }, 14000);
    S.animalPhoto.toBlob(function (blob) {
      if (t !== S.token) { clearTimeout(slow); return; }
      if (!blob) { clearTimeout(slow); failName('The photo could not be prepared.'); return; }
      sample.json(PROMPT, { images: [blob], modelTier: 'quick', signal: ctl.signal }).then(function (d) {
        clearTimeout(slow); if (t !== S.token) return;
        if (!d || typeof d !== 'object' || d.found === false) { tell('We can\u2019t find a creature in your photo. Try again.'); return; }
        var key = String(d.eyes || 'other'); if (!EYES[key]) key = 'other';
        diag('recognized', key);
        reveal(key, { common: (d.scientific ? nameCase(clip(d.common, 60)) : clip(d.common, 60)) || handName(key), scientific: clip(d.scientific, 80), by: 'Claude' });
      }).catch(function (e) {
        clearTimeout(slow); if (t !== S.token) return;
        var code = e && e.code; if (code === 'cancelled') return;
        if (['not_granted', 'sampling_disabled', 'not_declared', 'capability_disabled', 'capability_removed', 'images_unavailable'].indexOf(code) >= 0) sample = null;
        diag('claude-error', String(code || 'unknown'));
        failName(code === 'rate_limited' ? 'Claude is busy just now.' : code === 'not_granted' ? 'Claude was not allowed to look.' : 'The IDing isn’t working right now.');
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
    var small = Math.max(11, 1.85 * u), note = 'What ' + EYES[S.eyes].who + (guessed(S.eyes) ? ' might see, based on scientific evidence and informed speculation' : ' sees, based on scientific evidence') + ' \u00B7 ' + labelDate(new Date());
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
      $('keepVideo').onerror = function () { show('keepVideo', false); $('keepNote').textContent = 'Recorded. It can’t be played back in this browser, so save it to watch it.'; };
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
      $('keepNote').textContent = 'Sent to your downloads'; return;
    }
    if (!downloads) { $('keepNote').textContent = 'Saving is unavailable in this view'; return; }
    downloads.save({ filename: kept.name, data: kept.blob }).then(function () { $('keepNote').textContent = 'Saved'; }).catch(function (e) {
      var code = e && e.code; $('keepNote').textContent = code === 'declined' ? '' : code === 'rate_limited' ? '' : 'Save failed';
    });
  }
  function shareKept() {
    if (!kept) return;
    navigator.share({ files: [new File([kept.blob], kept.name, { type: kept.blob.type })] }).catch(function (e) {
      if (!e || e.name !== 'AbortError') $('keepNote').textContent = 'Sharing failed. Save it and send it from your files.';
    });
  }

  // ---------- the sheet behind the name
  function openInfo() {
    if (!S.eyes) return;
    var E = EYES[S.eyes];
    $('infoTitle').textContent = shownName();
    $('infoSub').textContent = S.named && S.named.scientific ? S.named.scientific : '';
    show('infoSub', !!$('infoSub').textContent);
    var ul = $('rows'); ul.textContent = '';
    E.rows.forEach(function (r) {
      var li = document.createElement('li'), m = document.createElement('i'), d = document.createElement('span'), b = document.createElement('b');
      m.className = 'mk' + (r[0] === 'i' ? '' : ' ' + r[0]); m.setAttribute('role', 'img');
      m.setAttribute('aria-label', r[0] === 'm' ? 'known in this animal' : r[0] === 'g' ? 'known in a relative' : r[0] === 'i' ? 'speculative' : 'left out');
      b.textContent = r[1] + ': '; d.appendChild(b); d.appendChild(document.createTextNode(r[2]));
      li.appendChild(m); li.appendChild(d); ul.appendChild(li);
    });
    $('info').scrollTop = 0; show('claim', false); show('record', false); openSheet('info');
  }

  function noteLink(before, word, after, title) {   // a line of the naming sheet with one linked word; the link opens a new report with the typed name as its title
    var n = $('claimNote'), a = document.createElement('a'); n.textContent = before;
    a.href = 'https://github.com/jampotful/seen-back/issues/new?title=' + encodeURIComponent(title); a.target = '_blank'; a.rel = 'noopener'; a.textContent = word;
    contactLink(a, title); n.appendChild(a); n.appendChild(document.createTextNode(after));
  }
  // ---------- wiring
  $('claimForm').addEventListener('submit', function (e) {
    e.preventDefault();
    var t = clip($('claimName').value, 60), hit = pocket.find ? pocket.find(t) : null, sp = hit && hit.exact, key, named, sug, box = $('claimSuggest');
    box.textContent = ''; show('claimSuggestRow', false); show('claimAboutRow', false);
    if (!t) { $('claimNote').textContent = 'Type what it was first.'; return; }
    // a species of the list by its own name, else a word of the table (a pet's own name can come along: "Biscuit, a cat")
    if (sp) { key = sp.kind; named = { common: nameCase(clip(sp.en || sp.sci, 60)), scientific: clip(sp.sci, 80), by: 'you', local: true }; }
    else { key = kindOfName(t); named = { common: t, scientific: '', by: 'you' }; }
    if (key === 'person') { diag('said-person', ''); $('claimNote').textContent = HUMAN_SAYS; return; }
    if (noView(key)) {                             // it exists, and none of the kinds of eye is its own
      diag('said-noview', clip(named.common, 60)); $('claimNote').innerHTML = noViewSays(named.common); return;
    }
    if (key) { diag('said', key); reveal(key, named); return; }
    sug = (hit ? hit.has.concat(hit.near) : []).slice(0, 3); if (!sug.length) sug = nearWords(t);
    if (sug.length) {                              // a slip of the keys, or a name that fits several
      $('claimNote').textContent = 'Did you mean:';
      offerList(sug.map(function (r) { return { sci: r.sci, en: r.en, kind: r.kind, local: !!r.sci }; })).forEach(function (o) {
        var b = el('button', 'pill ghost', o.label); b.type = 'button';
        b.addEventListener('click', function () { diag('suggested', o.kind); reveal(o.kind, { common: nameCase(clip(o.en || o.sci, 60)), scientific: clip(o.sci, 80), by: 'you', local: !!o.local }); });
        box.appendChild(b);
      });
      show('claimSuggestRow', true); return;
    }
    noteLink(cap(t) + ' isn\u2019t a creature we know. If this is a pet\u2019s name, please make sure you include what kind of creature your pet is (e.g. \u201CGarfield, a cat\u201D). If you typed in a real species, let us know about our error ', 'here', '.', 'Not identified: ' + t);
  });
  $('introFine').textContent = engine ? '' : 'This browser is too old to run the picture engine. Try a current Chrome, Safari, or other browser.';
  $('btnBegin').disabled = !engine;
  if (!coarse) { $('lblAnimalCam').hidden = true; $('lblViewClip').hidden = true; $('lblViewCam').hidden = true;    // one way in, so it is said in words
    [['lblAnimalPick', 'Upload a photo'], ['lblViewPick', 'Choose a clip or a photo']].forEach(function (p) { var l = $(p[0]), s = l.querySelector('svg'); l.className = 'pill'; if (s) l.removeChild(s); l.insertBefore(document.createTextNode(p[1]), l.firstChild); }); }

  function toAskAnimal() {
    $('askFine').textContent = inViewer ? 'Inside Claude the camera is closed to this page, so it works from a photo of who you met and a clip of your view. If nothing opens when you tap, open this page in a browser in place of the Claude app.'
      : S.camRefused ? 'If you already have a photo of the species, you can upload it here instead.' : '';
    go('askAnimal');
  }
  $('btnBegin').addEventListener('click', function () {
    armBack();
    if (!hasCamera || S.camRefused) { toAskAnimal(); return; }
    var btn = $('btnBegin'); btn.disabled = true;
    openCamera('environment').then(function () {
      btn.disabled = false; setEyes(null); go('finder'); msg('That didn’t work. Try again or upload a photo of a species.', 4500);
    }, function () { btn.disabled = false; toAskAnimal(); });
  });
  $('btnShutter').addEventListener('click', shutter);

  // ---------- the full database on a server (the naturalist), asked only with the person's say-so
  // One line on the picture carries it: an offer to ask (tappable), "Asking the full database.", the waking sentence, what it said,
  // and, where it sees another kind of creature and is sure enough, an offer to change eyes (tappable). The eyes never change by themselves.
  var SVC_SAY = { offer: 'The full database on a server can try to name the species. Ask it?', asking: 'Asking the full database\u2026', waking: 'The full database is waking up. This can take a minute\u2026', looking: 'Looking more closely\u2026' };
  var svcTimer = 0, svcTap = null, askFirstT = 0, firstJob = null;
  function renewName() { if ($('reveal').classList.contains('show') && (S.screen === 'naming' || S.screen === 'animal') && !anySheet()) showName(); }     // a finer name that arrives while the first is still large on the picture takes its place there; later, the line on the picture says it
  function aAn(name) { return (/^[aeiou]/i.test(name) ? 'an ' : 'a ') + name; }
  function paintSvc() {
    var v = S.svc;
    if (v && (v.t !== S.token || !S.eyes)) { S.svc = null; if (v.job) v.job.cancel(); v = null; }     // it belonged to a photo that is no longer in hand
    var text = v ? (v.text || (v.state === 'get' ? getLine() : SVC_SAY[v.state]) || '') : '', tap = v && (v.state === 'offer' || v.state === 'change' || v.state === 'get') ? tapSvc : null;
    if (!text && bigNote) { text = bigNote.text; tap = bigNote.tap; }     // the full database's download belongs to no one photo: its line shows whenever the photo has none of its own
    svcTap = tap;
    var loupe = !!tap && /^Download the full database|Ask it\?$/.test(text);     // the offer of a finer name is a loupe to tap; its sentence stays for screen readers
    ['svcHud', 'svcView'].forEach(function (id) {
      var b = $(id), sp;
      b.textContent = '';
      if (loupe) { b.insertAdjacentHTML('afterbegin', '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="2.6"/><path d="M12 2.8v4M12 17.2v4M2.8 12h4M17.2 12h4M5.5 5.5l2.6 2.6M15.9 15.9l2.6 2.6M18.5 5.5l-2.6 2.6M8.1 15.9l-2.6 2.6"/></svg>'); sp = document.createElement('span'); sp.className = 'vh'; sp.textContent = text; b.appendChild(sp); }
      else b.textContent = text;
      b.classList.toggle('loupe', loupe); b.disabled = !tap; b.hidden = !text; waitMark(b, loupe ? '' : text);
    });
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
    var named = { common: nameCase(clip(top.en || top.sci, 60)), scientific: clip(top.sci, 80), by: 'service', local: !!a.region };
    var kp = a.kinds.filter(function (k) { return k.key === top.kind; })[0], kindP = kp ? kp.p : top.p;
    if (top.p >= c.nameAt && top.kind === S.eyes) {
      // the same kind of eye, a finer name: on screen, in the sheet behind the name, and in the record
      S.named = named; noteMeeting(S.eyes, named); paintUI(); renewName();
      S.svc = { t: t, state: 'said', text: 'The full database says ' + named.common + '.' };
      svcTimer = setTimeout(function () { if (S.svc && S.svc.state === 'said') { S.svc = null; paintSvc(); } }, 10000);
    } else if (top.p >= c.nameAt && top.kind !== S.eyes && top.kind !== 'person' && c.kindAt !== null && kindP >= c.kindAt) {
      // another kind of creature, and the full database is sure enough by the service's own setting: the change is offered, never made
      if (top.kind === 'other') S.svc = { t: t, state: 'said', text: 'It looks like ' + aAn(named.common) + '. Regards doesn\u2019t have the ability to view the world as one right now.' };
      else S.svc = { t: t, state: 'change', kind: top.kind, named: named, text: 'It looks like ' + aAn(named.common) + ', ' + EYES[top.kind].who + '. Change to this creature?' };
    }
    paintSvc();
  }
  function tapSvc() {
    var v = S.svc; if (!v) return;
    if (v.state === 'offer') {
      var c = naturalist.cfg(); if (!c) return;
      $('askSub').textContent = 'This photo will be temporarily sent to this project\u2019s server, ' + c.where + '.';
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
  // ---------- the full database on this device (models/naturalist): fetched once if the person says so, then every photo is named here
  // The choice is kept in this browser: '' (ask when a photo is left without a species name), 'no' (do not offer it), 'yes' (asked for:
  // a download that was interrupted carries on by itself), 'kept' (it arrived whole: if it is gone later, nothing is fetched unasked).
  var BIG_KEY = 'seenback.large.v1', bigMem = '', bigNote = null, bigNoteTimer = 0, bigDelAsked = false;
  function bigChoice() { try { var v = localStorage.getItem(BIG_KEY); return v === 'yes' || v === 'no' || v === 'kept' ? v : ''; } catch (e) { return bigMem; } }
  function setBigChoice(v) { bigMem = v; try { if (v) localStorage.setItem(BIG_KEY, v); else localStorage.removeItem(BIG_KEY); } catch (e) {} }
  function dev() { return coarse ? 'phone' : 'computer'; }
  function netSays() {                             // what the connection says of itself, where it says anything
    var c = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
    if (!c) return '';
    if (c.saveData) return 'Your device is in data saver mode';
    if (c.metered === true || c.type === 'cellular') return 'Your device\u2019s connection is metered';
    if (/^(slow-2g|2g|3g)$/.test(c.effectiveType || '')) return 'Your device\u2019s connection is slow';
    return '';
  }
  function getLine() {
    var z = large.size(), h = large.has();
    // it had arrived whole and is not here now (the browser cleared it away, or the model was replaced by a newer one): said as it is
    if (bigChoice() === 'kept' && h !== 'kept') return 'The full database is no longer on this device. Get it again?';
    return z && h === 'partial' ? 'The full database is partly downloaded: ' + z.keptMb + ' of ' + z.mb + ' MB. Get the rest?' : 'Download the full database of species?';
  }
  function noteBig(text, tap, ms) {                // one line for the download: its progress, its end, its failure
    clearTimeout(bigNoteTimer); bigNote = text ? { text: text, tap: tap || null } : null;
    if (text && ms) bigNoteTimer = setTimeout(function () { bigNote = null; paintSvc(); }, ms);
    paintSvc(); if (!$('record').hidden) paintBig();
    if (!$('big').hidden && large.has() === 'getting') { $('bigNet').textContent = large.line(); waitMark($('bigNet')); }
  }
  function openBig() {                             // consent first, in plain words; and while it is being fetched, the same sheet stops it
    var z = large.size(), h = large.has(), s = z && z.seconds, n = netSays(), getting = h === 'getting', rest; if (!z) return;
    rest = Math.max(1, z.mb - (h === 'partial' ? z.keptMb : 0));
    $('bigTitle').textContent = getting ? 'Getting the full database' : h === 'partial' ? 'Get the rest of the full database?' : 'Get the full database?';
    $('bigSub').textContent = 'The full database of species is free to download and provides more accuracy in IDing.';
    $('bigNet').textContent = getting ? large.line() : (h === 'partial' ? z.keptMb + ' of ' + z.mb + ' MB have been downloaded. ' : '') + (n ? n + ', and ' + (h === 'partial' ? 'the rest' : 'this download') + ' is about ' + rest + ' MB.' : '');
    waitMark($('bigNet'));
    $('bigYes').textContent = h === 'partial' ? 'Get the rest' : 'Download';
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
      noteBig('The full database has been downloaded.', null, 8000);
      // the photo in hand is looked at now, if the small model's answer is still what stands
      if (S.eyes && S.eyes !== 'person' && S.named && S.named.by === 'page' && !S.svc) lookCloser(S.token);
    }, function (e) {
      var code = (e && e.code) || 'died', z = large.size(), again = /^(network|missing|damaged|died|slow)$/.test(code);
      if (!$('big').hidden) closeSheets();
      if (code === 'stopped') { setBigChoice(''); noteBig('The download has been stopped.' + (z && z.keptMb ? ' ' + z.keptMb + ' of ' + z.mb + ' MB are kept on this device.' : ''), null, 8000); return; }
      if (!again) setBigChoice('');
      noteBig(((e && e.sentence) || large.say(code)) + (again ? ' Try again?' : ''), again ? startBig : null, 30000);
    });
  }
  function five(r) { return r.species.slice(0, 5).map(function (x) { return { sci: x.sci, en: x.en, kind: x.kind, local: true }; }); }
  function largeName(r) { return r.local && r.named ? { common: nameCase(clip(r.named.en || r.named.sci, 60)) || handName(r.kind), scientific: clip(r.named.sci, 80), by: 'device-large', local: true } : null; }
  function noteLarge(r) { diag('large', JSON.stringify({ kind: r.kind, p: +r.kindP.toFixed(3), sure: r.sure, sp: r.species.slice(0, 2).map(function (x) { return [x.sci, +x.p.toFixed(3)]; }), ms: r.ms, model: r.model }).slice(0, 300)); }
  // After the small model's answer is in use. Where the full database is on this device it looks at every photo in the background. Where it
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
      S.svc = { t: t, state: 'said', text: 'The full database says ' + named.common + '.' };
      svcTimer = setTimeout(function () { if (S.svc && S.svc.state === 'said') { S.svc = null; paintSvc(); } }, 10000);
    } else if (r.sure && r.kindAt !== null && r.kind !== S.eyes && r.kind !== 'person' && r.kind !== 'none') {
      // another kind of creature, and the full database is sure enough by its slot's own setting: the change is offered, never made
      if (r.kind === 'other') S.svc = { t: t, state: 'said', text: 'It looks like ' + (named ? aAn(named.common) : 'another creature') + '. Regards doesn\u2019t have the ability to view the world as ' + (named ? 'one' : 'it') + ' right now.' };
      else S.svc = { t: t, state: 'change', kind: r.kind, named: named || { common: handName(r.kind), scientific: '', by: 'device-large', local: false },
        text: 'It looks like ' + (named ? aAn(named.common) + ', ' + EYES[r.kind].who : EYES[r.kind].who) + '. Change to this creature?' };
    }
    paintSvc();
  }
  // Nothing has a name yet: the small model was not sure, or the person asked from the sheet that asks for a name. The full database's
  // answer is waited for, and taken; if it is not sure either, its three likeliest kinds are offered.
  function firstLook(t, unsure) {
    var photo = S.animalPhoto; if (!photo || t !== S.token) return;
    closeSheets(); go('naming'); msg(SVC_SAY.looking); paintType();
    large.recognize(photo, pocket.file).then(function (r) {
      if (t !== S.token || S.eyes) return;
      S.closer = t; noteLarge(r);
      if (r.local && r.species.length) pocket.offers = five(r);
      if (r.sure && r.kind === 'none') { pocket.kindOffers = []; tell('We can\u2019t find a creature in your photo. Try again.'); return; }     // a larger slot with a kinds head can say so
      if (r.sure) { reveal(r.kind, largeName(r) || { common: r.kind === 'person' ? 'a human' : handName(r.kind), scientific: '', by: 'device-large', local: false }); return; }
      pocket.kindOffers = r.kindOffers || [];
      askName(unsure ? 'We’re not sure what kind of creature that is.' : 'We’re not sure what kind of creature that is.');
    }, function (e) {
      if (t !== S.token || S.eyes) return;
      S.closer = t; diag('large-none', String((e && e.code) || 'unknown'));
      askName(unsure ? 'We\u2019re not sure what kind of creature that is.' : ((e && e.sentence) || large.say('photo')) + ' Tell us what’s there.');
    });
  }
  // The same from the server, where that is the full database there is: asked with the person's say-so, and its answer taken as the name.
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
      if (top && c && top.p >= c.nameAt && top.kind !== 'person') { reveal(top.kind, { common: nameCase(clip(top.en || top.sci, 60)), scientific: clip(top.sci, 80), by: 'service', local: !!a.region }); return; }
      askName('The full database can’t ID this photo.');
    }, function (e) {
      if (firstJob === job) firstJob = null;
      if (t !== S.token || S.eyes) return;
      diag('service-none', String((e && e.code) || 'unknown'));
      if (e && e.code === 'cancelled') return;
      askName('The full database timed out. Try again.');
    });
  }
  // From the sheet that asks for a name there is a way to the full database, where there is one: on this device first, else on a server.
  var claimAskHow = '';
  function paintClaimAsk() {
    show('claimAskRow', false); claimAskHow = '';
    if (inViewer || S.eyes || !S.animalPhoto || S.closer === S.token) return;     // not where the full database has had this photo already
    var t = S.token;
    function still() { return t === S.token && !$('claim').hidden && !S.eyes; }
    large.survey().then(function (h) {
      if (!still()) return;
      if (h === 'kept' && !large.broken()) { $('claimAsk').textContent = 'Look more closely, with the full database'; claimAskHow = 'device'; show('claimAskRow', true); return; }
      naturalist.config().then(function (c) {
        if (!c || !still() || navigator.onLine === false || naturalist.choice() === 'no') return;
        $('claimAsk').textContent = 'Ask the full database on a server'; claimAskHow = 'service'; show('claimAskRow', true);
      });
    });
  }
  $('claimAsk').addEventListener('click', function () {
    var t = S.token, c = naturalist.cfg();
    if (claimAskHow === 'device') { diag('large-asked', ''); firstLook(t, false); return; }
    if (claimAskHow !== 'service' || !c) return;
    if (naturalist.choice() === 'yes') { closeSheets(); firstService(t); return; }
    $('askSub').textContent = 'This photo will be temporarily sent to this project\u2019s server, ' + c.where + '.';
    $('askKeep').checked = false;
    closeSheets(); askFirstT = t; openSheet('ask');
  });
  function paintBig() {                            // in the About block: where the full database stands, and the ways to get it, stop it and delete it
    large.survey().then(function () {
      var h = large.has(), z = large.size(), a = large.about(), d = dev(), fail = a.getFail && !/^stopped/.test(a.getFail) ? ' ' + large.say(a.getFail.split(':')[0]) : '';
      if (!z || !h) { show('bigBox', false); return; }
      $('bigState').textContent = bigDelAsked ? 'Delete the full database? It is ' + (h === 'kept' ? z.mb : z.keptMb) + ' MB, and would have to be downloaded again.'
        : h === 'getting' ? large.line()
        : h === 'kept' ? 'You currently have the full database of species downloaded.' + (a.state === 'failed' && a.why ? ' ' + large.say(a.why) : '')
        : h === 'partial' ? 'The full database is partly downloaded: ' + z.keptMb + ' of ' + z.mb + ' MB.' + fail
        : 'The full database of species is free to download and provides more accuracy in IDing.' + fail;
      waitMark($('bigState'));
      $('bigGet').textContent = h === 'partial' ? 'Get the rest' : 'Download'; $('bigDel').textContent = h === 'partial' && !bigDelAsked ? 'Delete any downloaded data' : 'Delete the download';
      show('bigGet', !bigDelAsked && (h === 'absent' || h === 'partial')); show('bigHalt', h === 'getting'); show('bigDel', h === 'kept' || h === 'partial'); show('bigDelNo', bigDelAsked);
      show('bigAskRow', false); $('bigAsk').checked = bigChoice() === 'no';
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
    // the switch is shown where it changes something: this device has a species list, or there is the full database that is told the region
    show('awayRow', false); $('awayBox').checked = pocket.local === false;
    $('awayNote').textContent = 'Species are named from a list of those recorded around ' + pocket.place() + '. With this ticked, this ' + (coarse ? 'phone' : 'computer') + ' names only the kind of animal or plant, and the full database, if asked, is not told the region.';
    show('svcBox', false);
    naturalist.config().then(function (c) {
      show('svcBox', !!c); if (!c) return;
      $('svcChoice').value = naturalist.choice();
      if (false) { $('awayNote').textContent = 'The full database, when asked, is told the region, so that it can choose among species recorded around ' + pocket.place() + '. With this ticked, it is not told.'; }
    });
  }
  $('awayBox').addEventListener('change', function () { pocket.local = !$('awayBox').checked; try { localStorage.setItem(AWAY_KEY, pocket.local ? '0' : '1'); } catch (e) {} diag('away', pocket.local ? 'no' : 'yes'); });
  $('svcChoice').addEventListener('change', function () { naturalist.setChoice($('svcChoice').value); diag('service-choice', $('svcChoice').value || 'each'); });
  $('btnType').addEventListener('click', function () {
    if (S.screen !== 'naming' || S.eyes) return;
    S.token++; S.seq++; diag('type-instead', '');             // the answer for this photo, when it comes, is not waited for
    askName('Your download is finishing in the background.');
  });
  $('btnBack').addEventListener('click', back);
  $('backAskAnimal').addEventListener('click', back);
  $('backAskView').addEventListener('click', back);
  $('claimAbout').addEventListener('click', openAbout);
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
  function hold(on) { return function (e) { if (e && e.cancelable) e.preventDefault(); S.holding = on; $('btnEyes').classList.toggle('on', on); if (on) msg('As a human'); else msg(''); }; }
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
    decode(f).then(function (c) { pocket.file = f; gotAnimalPhoto(c); }).catch(function () { if (S.screen === 'finder') msg('This file could not be read as a photo.', 5000); else $('askFine').textContent = 'This file could not be read as a photo.'; });
  }
  function onViewFile(e) {
    var f = e.target.files && e.target.files[0]; e.target.value = ''; if (!f || !S.eyes || !engine) return;
    var key = S.eyes, nm = S.named, isVideo = /^video\//.test(f.type) || /\.(mp4|mov|webm|m4v|3gp|mkv)$/i.test(f.name || '');
    S.seq++; $('askViewFine').textContent = 'Opening\u2026'; waitMark($('askViewFine'));
    (isVideo ? startClip(f) : decode(f).then(function (c) { showStill(c, true); })).then(function () {
      $('askViewFine').textContent = ''; setEyes(key, nm); go('animal'); showName(); later(startChange, calm ? 150 : 900);
    }).catch(function () {
      if (S.animalPhoto) showStill(S.animalPhoto, false);
      setEyes(key, nm); $('askViewFine').textContent = 'This file could not be opened. Try another.';
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
  window.__seenBack = { S: S, EYES: EYES, state: function () { return engine ? engine.state() : null; }, record: function () { return record; }, kindOfName: kindOfName, offerList: offerList, setViewPrompt: setViewPrompt, lookAgain: lookAgain, openClaim: openClaim,
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
      (b.place ? '; place from ' + (b.place.known ? 'the time zone ' + b.place.zone : 'no known time zone') + ' and ' + b.place.met + (b.place.met === 1 ? ' creature' : ' creatures') + ' met' : '') +
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
    return ' identifies species by comparing with iNaturalist and Flickr photos made available under Creative Commons licenses or in the public domain.';
  }
  function paintAbout() { var fl = fittedLine(), f = pocket.about().fitted, el = $('fittedOn'), a;
    $('buildMark').textContent = aboutText(); $('aboutNote').textContent = '';
    el.textContent = 'v1.' + Math.max(0, (parseInt(BUILD, 10) || 10) - 10);
    if (fl) {
      el.appendChild(document.createElement('br')); el.appendChild(document.createElement('br'));
      el.appendChild(document.createElement('em')).textContent = 'Regards'; el.appendChild(document.createTextNode(fl));
      if (f && typeof f.list === 'string' && /^https:\/\/[^\s"<>]+$/.test(f.list)) {   // the attribution: where each photograph's address and licence can be read
        a = document.createElement('a'); a.href = f.list; a.target = '_blank'; a.rel = 'noopener'; a.textContent = 'here';
        el.appendChild(document.createTextNode(' The full list of photos is ')); el.appendChild(a); el.appendChild(document.createTextNode('.'));
      }
    }
    show('fittedOn', true); paintChoices(); }
  // The contact form sends an email to the app's maker through Web3Forms, a form-to-email service (build 22). The service keeps the
  // address; the page holds only the access key, which can send to that one address and nowhere else, so it may sit in public code.
  var CONTACT_KEY = 'f191b157-47de-402b-9818-23dc36d5bd70', CONTACT_API = 'https://api.web3forms.com/submit';
  function openContact(about) {
    if (!CONTACT_KEY && !/[?&]contact=demo\b/.test(location.search)) return false;
    closeSheets(); ['contactName', 'contactEmail', 'contactMsg'].forEach(function (id) { $(id).parentNode.classList.remove('bad'); });
    $('contactNote').textContent = ''; waitMark($('contactNote')); $('contactSend').disabled = false;
    if (about && !$('contactMsg').value) $('contactMsg').value = about;
    openSheet('contact'); $('contact').scrollTop = 0; return true;
  }
  function contactLink(a, about) { a.addEventListener('click', function (e) { if (openContact(typeof about === 'function' ? about() : about)) e.preventDefault(); }); }
  $('contactClose').addEventListener('click', dismissSheets);
  $('contactForm').addEventListener('submit', function (e) {
    e.preventDefault();
    var name = clip($('contactName').value, 80), email = clip($('contactEmail').value, 120), text = String($('contactMsg').value || '').trim().slice(0, 2000), okMail = !email || /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email), body;
    $('contactEmail').parentNode.classList.toggle('bad', !okMail); $('contactMsg').parentNode.classList.toggle('bad', !text);
    if (!text) { $('contactNote').textContent = 'Write a message first.'; return; }
    if (!okMail) { $('contactNote').textContent = 'That email doesn\u2019t look right.'; return; }
    if (!CONTACT_KEY) { $('contactNote').textContent = 'Sending isn\u2019t set up yet.'; return; }
    body = new FormData();                         // a plain form post, so the browser sends it without asking the service first
    body.append('access_key', CONTACT_KEY); body.append('subject', 'A message from Regards'); body.append('from_name', 'Regards');
    body.append('name', name || '(no name given)'); if (email) body.append('email', email); body.append('message', text);
    body.append('build', 'v1.' + Math.max(0, (parseInt(BUILD, 10) || 10) - 10) + ' (build ' + BUILD + ')');
    if ($('contactBot').checked) body.append('botcheck', 'on');   // a box only a program filling in every field would tick; the service drops such messages
    $('contactSend').disabled = true; $('contactNote').textContent = 'Sending\u2026'; waitMark($('contactNote'));
    fetch(CONTACT_API, { method: 'POST', body: body, headers: { Accept: 'application/json' } }).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || !j || j.success !== true) throw new Error((j && j.message) || ('HTTP ' + r.status)); });
    }).then(function () {
      diag('contact', 'sent'); $('contactNote').textContent = 'Sent. Thank you.'; waitMark($('contactNote')); $('contactMsg').value = '';
    }, function (err) {
      diag('contact', clip(String(err && err.message), 80)); $('contactSend').disabled = false;
      $('contactNote').textContent = navigator.onLine === false ? 'That didn\u2019t send. Check your connection and try again.' : 'That didn\u2019t send. Try again in a moment.'; waitMark($('contactNote'));
    });
  });
  contactLink($('aboutTellLink'), '');
  $('noticeOk').addEventListener('click', dismissSheets);
  function openAbout() { paintAbout(); show('buildBox', false); show('claim', false); show('record', false); show('info', false); show('keep', false); show('ask', false); show('big', false); openSheet('aboutSheet'); $('aboutSheet').scrollTop = 0; }
  $('recAbout').addEventListener('click', openAbout); $('introAbout').addEventListener('click', openAbout); $('aboutClose').addEventListener('click', dismissSheets);
  $('fittedOn').addEventListener('click', function (e) { if (e.target && e.target.tagName === 'A') return; show('buildBox', $('buildBox').hidden); });   // the block of figures for a report from a real device: a tap on the version line shows it
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
