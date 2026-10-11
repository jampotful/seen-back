  'use strict';
  var $ = function (id) { return document.getElementById(id); };

  // ---------- where is this running?
  // Inside Claude's viewer the camera is normally refused, and only there can Claude name a photo.
  var inViewer = !!(window.claude && typeof window.claude.use === 'function');
  var hasCamera = !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);
  var coarse = !!(window.matchMedia && window.matchMedia('(pointer: coarse)').matches);
  var calm = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var BUILD = '10';
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
