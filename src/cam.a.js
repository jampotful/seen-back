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
