  'use strict';
  var $ = function (id) { return document.getElementById(id); };

  // ---------- where is this running?
  // Inside Claude's viewer the camera is normally refused, and only there can Claude name a photo.
  var inViewer = !!(window.claude && typeof window.claude.use === 'function');
  var hasCamera = !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);
  var coarse = !!(window.matchMedia && window.matchMedia('(pointer: coarse)').matches);
  var calm = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var BUILD = '21';
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
      cue: 'Out-of-focus things smear up and down. Tap to move the focus.', rows: [
      ['m', 'Sharpness', 'A cat sees about a fifth to a tenth of the detail you do. We blur the picture to match.'],
      ['m', 'Colour', 'Cats have two kinds of colour sensor in their eyes, and you have three. Reds look olive or grey to a cat.'],
      ['m', 'Pupil', 'A cat’s pupil is a vertical slit, like those of many hunters that ambush their prey. It makes out-of-focus things smear up and down.'],
      ['m', 'Field of view', 'A cat sees about 200 degrees around it, and you see about 180. Your camera captures less than that, so we fill in the edges ourselves.'],
      ['m', 'Dim light', 'A cat needs six to eight times less light than you do to see. We brighten the shadows to show it.'],
      ['i', 'Depth', 'A phone camera can’t measure distance. We guess that things lower in the picture are closer, and you can tap to set the focus.'],
      ['i', 'Sharpest spot', 'We assume a cat sees most sharply in the centre of its view.']] },
    dog: { chip: 'Dog', who: 'a dog', fov: 240, cpd: 11, topoS: 1, fall: 1.6, pupil: 'o', dof: 10, M: DEUTAN, gain: 1.3, sat: .85,
      cue: 'Sharpest along the horizon. Tap to move the focus.', rows: [
      ['m', 'Sharpness', 'A dog sees about a quarter to a seventh of the detail you do. We blur the picture to match.'],
      ['m', 'Sharpest spot', 'Long-nosed dogs see most sharply in a band along the horizon, and short-nosed dogs in a single spot. We show the band.'],
      ['i', 'Colour', 'Dogs have two kinds of colour sensor in their eyes, and you have three. We show colours the way a person with only two kinds sees them.'],
      ['i', 'Field of view, dim light and depth', 'These are our best guesses. We treat things lower in the picture as closer.']] },
    squirrel: { chip: 'Squirrel', who: 'a squirrel', fov: 270, cpd: 6, topoS: 1, fall: 1.0, pupil: 'o', dof: 4, M: PROTAN, rate: .56,
      cue: 'Each moment runs slow, then the picture catches up.', rows: [
      ['g', 'Colour', 'Ground squirrels have two kinds of colour sensor in their eyes, and you have three.'],
      ['g', 'Speed', 'A ground squirrel’s eyes can follow a light flashing up to 108 times a second, and yours give up at about 60. Fast things look slower to it. We slow the picture down to suggest it, then let it jump to catch up.'],
      ['i', 'Field of view and sharpness', 'Our best guess is that eyes on the sides of the head give a wide view, with less detail than you see.']] },
    deer: { chip: 'Deer', who: 'a deer', fov: 310, cpd: 8, topoS: 1, fall: 2.2, pupil: 'h', dof: 22, M: DEUTAN, gain: 1.5, sat: .85,
      cue: 'A wide band of ground. Out-of-focus things smear sideways.', rows: [
      ['m', 'Colour', 'White-tailed deer have two kinds of colour sensor in their eyes, and you have three. Reds and oranges look yellow or grey to a deer.'],
      ['m', 'Field of view', 'A deer sees about 310 degrees around it, which is nearly a full circle. Your camera captures less than a quarter of that, so we fill in the rest ourselves.'],
      ['g', 'Pupil', 'Grazing animals have a pupil shaped like a horizontal bar. It widens their view along the ground and cuts the glare from the sky. It makes out-of-focus things smear sideways.'],
      ['i', 'Sharpness, dim light and depth', 'These are our best guesses. We treat things lower in the picture as closer.']] },
    rabbit: { chip: 'Rabbit', who: 'a rabbit', fov: 350, cpd: 3, topoS: 1, fall: 2.0, pupil: 'o', dof: 6, M: DEUTAN,
      cue: 'Nearly the whole circle at once, and little of it sharp.', rows: [
      ['i', 'The whole view', 'Everything here is our best guess, and we haven’t checked it yet. A rabbit likely sees nearly all the way around itself, most sharply along the horizon, with little detail and two kinds of colour sensor.']] },
    hawk: { chip: 'Hawk, eagle, falcon', who: 'a hawk', fov: 180, cpd: 60, fovea: 2.2, pupil: 'o', rate: .6,
      cue: 'The centre is pulled close, and each moment runs slow.', rows: [
      ['g', 'Sharpness', 'An eagle sees more than twice the detail you do. A phone can’t capture that much, so we magnify the centre of the picture to suggest it.'],
      ['m', 'Speed', 'A peregrine falcon’s eyes can follow a light flashing up to 129 times a second, and a Harris’s hawk’s up to 77. Yours give up at 50 to 60. We slow the picture down to suggest it, then let it jump to catch up.'],
      ['i', 'Field of view', 'We leave the field of view as your camera gives it.']] },
    wader: { chip: 'Heron, crane, pigeon', who: 'a wading bird', fov: 300, cpd: 25, topoS: .6, fall: .8, pupil: 'o', sheen: .6, hold: 280, thrust: 120,
      cue: 'Walk. The picture holds still, then lurches forward, the way a heron’s head does.', rows: [
      ['m', 'Head movement', 'Herons, egrets, cranes, pigeons and chickens hold their head still while they walk, so their eyes stay fixed on the world. Then the head darts forward to catch up with the body.'],
      ['g', 'Speed', 'In pigeons, each dart forward takes about a tenth of a second.'],
      ['g', 'Sharpness', 'Most birds see about half the detail you do, or less.'],
      ['i', 'Ultraviolet', 'Some birds can see ultraviolet light, which is invisible to us. A phone can’t capture it, so the violet tint here stands in for it.'],
      ['i', 'Field of view', 'Our best guess is that eyes on the sides of the head give a wide view.']] },
    bird: { chip: 'Other bird', who: 'a bird', fov: 300, cpd: 25, topoA: .5, fall: .6, pupil: 'o', sheen: .8, rate: .5,
      cue: 'Each moment runs slow, then the picture catches up.', rows: [
      ['g', 'Speed', 'Birds’ eyes can follow a light flashing 40 to 140 times a second, and the fastest fliers are at the high end. Yours give up at about 60. We slow the picture down to suggest it, then let it jump to catch up.'],
      ['g', 'Sharpness', 'Most birds see about half the detail you do, or less.'],
      ['i', 'Ultraviolet', 'Some birds can see ultraviolet light, which is invisible to us. A phone can’t capture it, so the violet tint here stands in for it.'],
      ['i', 'Field of view', 'Our best guess is that eyes on the sides of the head give a wide view.']] },
    alligator: { chip: 'Alligator', who: 'an alligator', fov: 280, cpd: 9, topoS: 1, fall: 2.6, pupil: 'v', dof: 24, gain: 1.6, sat: .9,
      cue: 'One sharp band along the waterline.', rows: [
      ['g', 'Sharpest spot', 'Crocodiles see most sharply in a band along the horizon. It lets them scan the waterline without turning their head.'],
      ['g', 'Colour', 'Crocodiles have three kinds of colour sensor in their eyes, as you do, so we leave colours as your camera gives them.'],
      ['g', 'Pupil', 'An alligator’s pupil is a vertical slit. It makes out-of-focus things smear up and down.'],
      ['i', 'Field of view, sharpness, dim light and depth', 'These are our best guesses.']] },
    reptile: { chip: 'Lizard, snake, turtle', who: 'a reptile', fov: 280, cpd: 15, topoA: 1, fall: 1.2, pupil: 'o', sheen: .6,
      cue: '', rows: [
      ['i', 'The whole view', 'Everything here is our best guess. We assume eyes on the sides of the head, one sharp spot in the centre, and the ability to see ultraviolet light, which we show as a violet tint.']] },
    frog: { chip: 'Frog, toad', who: 'a frog or toad', fov: 340, cpd: 4, pupil: 'h', persist: .15, gate: 1,
      cue: 'Hold still, as a frog does. Only things that move show up.', rows: [
      ['m', 'Movement', 'A frog doesn’t notice the parts of its world that stay still. It can starve next to food that doesn’t move. So we only show what changes. Hold your phone as still as a frog holds itself.'],
      ['g', 'Speed', 'A cane toad’s eyes can follow a light flashing only about 7 times a second, a ninth of what yours can. Anything that moves smears into a trail.'],
      ['i', 'Field of view, sharpness and pupil', 'These are our best guesses.']] },
    bee: { chip: 'Bee', who: 'a bee', fov: 320, cpd: 1, pupil: 'none', M: BEE, uvBlue: 1, rate: .3,
      cue: 'Red goes dark, and each moment runs slow.', rows: [
      ['g', 'Sharpness', 'Most insects see less than a sixtieth of the detail you do.'],
      ['m', 'Red', 'Bees can’t see red. Red things look dark to them.'],
      ['m', 'Speed', 'In bright light, a honeybee’s eyes can follow a light flashing up to 200 times a second, and yours give up at about 60. We slow the picture down to suggest it, then let it jump to catch up.'],
      ['i', 'Ultraviolet', 'Bees can see ultraviolet light, which is invisible to us. A phone can’t capture it, so the blue here stands in for it.'],
      ['i', 'How we show the colours', 'A bee sees green, blue and ultraviolet. We can’t show you ultraviolet, so we shift every colour over by one: a bee’s green appears as red, its blue as green, and its ultraviolet as blue.']] },
    insect: { chip: 'Butterfly, other insect', who: 'an insect', fov: 320, cpd: 1, pupil: 'none', sheen: .8, rate: .45,
      cue: 'Blurry and wide, and each moment runs slow.', rows: [
      ['g', 'Sharpness', 'Most insects see less than a sixtieth of the detail you do.'],
      ['g', 'Speed', 'The eyes of flies and dragonflies can follow a light flashing more than 100 times a second, and one beetle’s up to 400. Yours give up at about 60. We slow the picture down to suggest it, then let it jump to catch up.'],
      ['i', 'Ultraviolet', 'Bees and some other insects can see ultraviolet light, which is invisible to us. A phone can’t capture it, so the violet tint here stands in for it.']] },
    plant: { chip: 'Plant', who: 'a plant', pupil: 'none', field: 1, noGreen: 1, persist: 2.5,
      cue: 'No picture here. Only how much light there is, what colour it is, and where it comes from.', rows: [
      ['g', 'No picture', 'A plant has nothing like a lens to focus light into a picture. It senses how much light there is, what colour it is, and which direction it comes from.'],
      ['m', 'Neighbours', 'Plants compare red light with far-red light, a colour just beyond what we can see. That tells them a neighbour is growing close by, before it shades them. A phone can’t capture far-red light.'],
      ['i', 'Green and time', 'We take out the green, because leaves reflect most of it away, and we blur out anything quick. Both are our own choices.']] },
    other: { chip: 'Something else', who: 'this one', pupil: 'none', field: 1, sat: 0,
      cue: '', rows: [
      ['i', 'No view yet', 'Regards doesn’t have the ability to view the world as this creature right now.']] },
    person: { chip: null, who: 'a human', pupil: 'o', cue: '', rows: [
      ['m', 'Same eyes', 'That’s a human. You already see the world as one.']] }
  };
  var ORDER = ['cat', 'dog', 'squirrel', 'deer', 'rabbit', 'wader', 'bird', 'hawk', 'alligator', 'reptile', 'frog', 'bee', 'insect', 'plant', 'other'];
  // Groups the app can name and cannot yet view the world as (docs/COVERAGE.md, decided by the owner on 12 October 2026).
  // A photo or a typed name in one of them gets the notice that Regards can't view the world as that creature yet, and no
  // encounter is kept. A group moves into EYES when its view is drawn from its sheet (docs/views/sheets/).
  var GROUPS = { fungus: 'a fungus', slime: 'a slime mould', spider: 'a spider', jumper: 'a jumping spider', fish: 'a fish', shark: 'a shark or ray',
    snail: 'a snail or slug', sealife: 'a sea creature', crab: 'a crustacean', salamander: 'a salamander or newt', worm: 'a worm, millipede or centipede',
    scorpion: 'a scorpion or harvestman', tick: 'a tick', mammal: 'a mammal', primate: 'a monkey or ape', whale: 'a whale, dolphin or seal',
    bat: 'a bat', flyingfox: 'a flying fox', cephalopod: 'an octopus or squid' };
  function noView(key) { return key === 'other' || (!!GROUPS[key] && !EYES[key]); }

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
