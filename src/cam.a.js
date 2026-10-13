  'use strict';
  var $ = function (id) { return document.getElementById(id); };

  // ---------- where is this running?
  // Inside Claude's viewer the camera is normally refused, and only there can Claude name a photo.
  var inViewer = !!(window.claude && typeof window.claude.use === 'function');
  var hasCamera = !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);
  var coarse = !!(window.matchMedia && window.matchMedia('(pointer: coarse)').matches);
  var calm = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var BUILD = '23';
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

  // ---------- views being tried (build 23): reached only with ?try=<key> (several with ?try=a,b), offered nowhere else yet
  // An entry here becomes a view in EYES for that visit only, so a photo or a typed name in its group then opens it too. The fields
  // added for these views (zones, salience, gaze, glow, senses) are described in docs/ENGINE.md with the evidence each one serves.
  // A jumping spider's receptors from linear camera RGB, as fitted on open spectra in research/methods (draft section 2.4, its author's own
  // computation, to be refitted on a larger library before shipping): the green class (531 nm in Habronattus, near the 526 to 540 of other
  // genera) and Habronattus's red-filtered class (628 nm), each divided by its sum so that white stays white. Ultraviolet cannot be estimated
  // from a phone picture (same section), so the engine's guess stands in for it, and is invented.
  var SALT_G = [.017 / .982, .732 / .982, .233 / .982], SALT_L = [.554 / .989, .171 / .989, .264 / .989];
  function tinted(c, r) { return [c[0] * r[0], c[0] * r[1], c[0] * r[2], c[1] * r[0], c[1] * r[1], c[1] * r[2], c[2] * r[0], c[2] * r[1], c[2] * r[2]]; }
  var SIDE_GREEN = tinted([.42, .78, .46], SALT_G);                          // the side eyes' one green class, as a dim green (the tint is invented)
  var UV_GREEN = tinted([.5, 1, 0], SALT_G);                                 // green as green and ultraviolet as blue, with red their mean (uvR .5): the convention of Vasas and colleagues 2024 for two classes, as research/methods gives it
  var UV_GREEN_RED = SALT_L.concat(SALT_G, [0, 0, 0]);                       // the red-filtered class as red, green as green, ultraviolet as blue
  var TRY = {
    // Jumping spiders (family Salticidae), from docs/views/drafts/jumper.md and its log, docs/views/evidence/jumper.jsonl, on research/jumper.
    // The surround is the side eyes: the rear pair (PLE) at 0.5 cycles a degree, the front pair (ALE) at 1.1, both green only (Land 1969;
    // Gote and colleagues 2019; Yamashita and Tateda 1976). The cross is the two principal retinae at rest (Land 1969), at the acuity of
    // Phidippus (3.3 to 3.8 cycles a degree: Land 1969; Harland and colleagues 2012). docs/ENGINE.md gives every value and its source.
    jumper: { chip: 'Jumping spider', who: 'a jumping spider', fov: 350, cpd: .5, pupil: 'o', M: SIDE_GREEN, glow: .9, living: 0, glowC: [.78, 1, .62],
      salience: 1, senses: { motion: 1 },
      cue: 'Things that move glow. The sharp cross jumps to them, looks them over, and then leaves that place alone for a few seconds.',
      zones: [
        // both front side eyes: each about 70 degrees across and 98 high, overlapping by 25 in front (Gote 2019; Land 1969; Blest 1981)
        { id: 'front', shape: 'ellipse', deg: [114, 98], soft: .2, cpd: 1.1, living: 1.6 },
        // the principal retinae: each a strip about 2 degrees wide and 21 high, bent 30 degrees at its centre; the upper arms 40 to 45
        // degrees apart, the lower 15 to 20, the inner edges 1 to 2 degrees apart (Land 1969); the arms see less sharply toward their ends
        // (Williams and McIntyre 1980). Drawn 2.5 degrees wide (invented, for the screen) and magnified a little (invented).
        { id: 'gaze', shape: 'cross', deg: [2.5, 21], tilt: [21, 8.5], gap: .75, tip: .45, soft: .01, cpd: 3.6, M: UV_GREEN, uv: 1, uvR: .5, glow: 0, living: 0, mag: 1.25, gaze: 1 },
        // the centre of each principal retina, where Habronattus has its red-filtered receptors (Zurek and colleagues 2015); dichromatic elsewhere
        { id: 'fovea', shape: 'ellipse', deg: [5, 4], soft: .01, cpd: 3.6, M: UV_GREEN, uv: 1, uvR: .5, glow: 0, living: 0, mag: 1.25, gaze: 1 }],
      gaze: { saccade: [40, 4], sweep: [2, 1.2], twist: [25, 2000, 3500], examine: [4000, 12000], hold: 1500, back: .8, pursuit: 10,
        ior: 5000, iorDeg: 6, habit: .75, surround: .6, any: .6, living: 1.8, distract: 1.5, wander: [8000, 20000], floor: .06, trackDeg: 9,
        sleep: { after: 3500, bout: [6000, 12000], gap: [20000, 40000] } },
      byGenus: {
        Habronattus: { zones: { fovea: { M: UV_GREEN_RED, uvR: 0 } } },
        Portia: { zones: { gaze: { cpd: 12.5, deg: [1.5, 21] }, fovea: { cpd: 12.5 } } } },   // Portia fimbriata: 12.4 cycles a degree (Williams and McIntyre 1980)
      rows: [
        ['m', 'Eight eyes, one picture', 'Six of a jumping spider’s eyes watch for movement all around it, and two large front eyes swing toward whatever they report to look closely. This view draws all eight as one picture.'],
        ['m', 'The side eyes', 'The six side eyes see in green only, and with little detail: under a hundredth of yours at the back and about a fiftieth in front. They answer only to movement, so here the surround is a dim green and whatever moves in it glows.'],
        ['m', 'Living things stand out', 'The front side eyes pick out the jointed, rhythmic movement of living things, and the rear side eyes answer to anything that moves. In front, this view makes living movement glow brighter.'],
        ['m', 'The front eyes', 'Each large front eye sees a narrow upright strip about 2 degrees wide and 21 high, bent in the middle, and the two strips cross like an X. In Phidippus they see about a sixteenth of the detail you do, and in Portia about a fifth.'],
        ['m', 'Jumps and scans', 'The front eyes jump to a new target in about a tenth of a second and follow it if it moves. While they look, they sweep side to side across it and slowly twist back and forth, and this view does the same.'],
        ['m', 'Looking away on purpose', 'Once the front eyes lock on, the side eyes ignore that spot and watch elsewhere, and their interest in it returns over about five seconds. Here the glow fades from a place just looked at and comes back as slowly.'],
        ['m', 'Colour', 'Most jumping spiders, Phidippus among them, see ultraviolet and green. Habronattus also sees red, in a small patch at the centre of each front eye, and this view adds red there when it knows the genus.'],
        ['m', 'Sleep', 'At night a resting jumping spider’s retinas twitch in bouts, much like the eye movements of a person dreaming. When the phone lies still in the dark, this view twitches its cross in bouts, closer together than a spider’s.'],
        ['i', 'How the picture is drawn', 'No one knows how a jumping spider joins what its eyes report. Drawing the front eyes’ cross inside the side eyes’ surround, as one picture, is the app’s own choice.'],
        ['i', 'Living movement', 'This view treats movement that holds together over a small patch and swings back and forth, as walking legs do, as the movement of something alive. That test is the app’s own approximation.'],
        ['i', 'How the colours are shown', 'A phone camera records almost no ultraviolet light, so the ultraviolet in this view is a guess made from bluish and bright surfaces. Inside the cross the spider’s green shows as green and the guessed ultraviolet as blue, with red for their mix.'],
        ['x', 'Hearing', 'A jumping spider senses low sounds in the air through hairs on its legs. The picture leaves this out.']] }
  };
  // Prototypes of effects the research drafts propose (docs/ENGINE.md, "Prototypes"). Their rows come from the drafts named, with a row of
  // grade i for each drawing of the app's own; the research threads write the final rows.
  // Sea fish, from docs/views/drafts/fish-shark.md (research/fish-shark), section 3: two eyes that each look their own way.
  TRY.reef = { chip: 'Sea fish', who: 'a sea fish', fov: 335, cpd: 2, pupil: 'o', M: [.35, 0, 0, 0, 1, 0, 0, 0, 1], sheen: .6, rate: .86,
    salience: 1, glow: .3, living: .5, glowC: [.55, .85, 1], water: [1.5, .45, .25, 1], waterC: [.03, .2, .26],
    cue: 'Reds fade to grey, the water is blue, and each eye looks its own way.',
    zones: [{ id: 'left', shape: 'ellipse', deg: [9, 9], soft: .025, cpd: 4, gaze: 1 }, { id: 'right', shape: 'ellipse', deg: [9, 9], soft: .025, cpd: 4, gaze: 2 }],
    gaze: [{ region: [0, .5], saccade: [40, 3], sweep: [0, 1], twist: [0, 1, 1], examine: [1200, 3500], hold: 600, back: 3, pursuit: 20, ior: 2500, iorDeg: 8, wander: [2000, 6000], floor: .05, distract: 1.2 },
      { region: [.5, 1], saccade: [40, 3], sweep: [0, 1], twist: [0, 1, 1], examine: [1200, 3500], hold: 600, back: 3, pursuit: 20, ior: 2500, iorDeg: 8, wander: [2000, 6000], floor: .05, distract: 1.2 }],
    rows: [
      ['m', 'Colour', 'Damselfish, the family of the clownfish, have four kinds of colour-sensing cells, one of them for ultraviolet light, and many wear ultraviolet patterns that they show one another. A triggerfish has three kinds, tuned to violet, blue and green. Neither has a cell tuned to red, so this view darkens reds and adds an invented violet sheen for ultraviolet.'],
      ['g', 'Red light fades', 'Sea water swallows red light within the first 10 to 20 metres, so deeper down a red fish looks dark grey and a reef turns blue-green. This view tints the picture blue-green and fades reds with distance.'],
      ['m', 'Sharpness', 'Small reef fish see coarsely. An Ambon damselfish and a dottyback resolved about a fortieth as much detail as you do, though the cells in their eyes are packed tightly enough for about three times more. This view blurs the picture to match.'],
      ['m', 'Eyes that move apart', 'Wrasses, blennies, pufferfish, triggerfish and seahorses can turn each eye on its own, and each eye has a small sharp centre, called a fovea. One eye can follow a passing fish while the other searches the reef. This view gives each half of the screen its own sharp spot, and the two wander separately.'],
      ['m', 'Pace', 'A squirrelfish, a reef fish that hunts at night, follows a flickering light up to 70 flashes a second in bright light, faster than you can, and only about 40 at night. This view runs slightly slow in daylight and then jumps ahead to catch up.'],
      ['i', 'How the eyes are drawn', 'How fast each eye jumps and how long it stays are the app’s own choices. That the two eyes move independently is measured.'],
      ['i', 'Distance', 'A phone camera can’t measure distance, so this view takes things higher in the picture to be farther away when it fades their reds.'],
      ['x', 'Moving water', 'Rows of sensors along a fish’s head and body, called the lateral line, feel the flow and pressure of moving water within one or two body lengths. The picture leaves this sense out.']] };
  // Sharks, from the same draft, section 4: grey, a band of sharpness, trails, the head's sweep, and an invented glow for the electric sense up close.
  TRY.shark = { chip: 'Shark', who: 'a shark', fov: 300, cpd: 5, topoS: 1, fall: 1.5, pupil: 'o', M: [0, 1, 0, 0, 1, 0, 0, 1, 0], gain: 1.3, persist: .04,
    salience: 1, glow: 0, living: 0, glowC: [.5, .85, 1], shimmer: .6, sweep: [15, 4.5],
    cue: 'There is no colour, only light and dark, and movement leaves trails.',
    zones: [{ id: 'near', shape: 'band', at: [.5, .17], frac: [.5, .17], soft: .06, glow: .9, living: 2.4 }],
    rows: [
      ['m', 'Colour', 'Every shark studied so far has only one kind of colour-sensing cell, so sharks are probably colour blind. They can tell apart shades of brightness that differ by less than 2 percent. This view shows the world in shades of grey.'],
      ['m', 'Sharpness', 'Sharks see between a twentieth and a sixth as much detail as you do. Fast hunters of open water, like the bigeye thresher, are at the sharp end, and bottom-dwelling night hunters, like the Port Jackson shark, are at the coarse end. This view uses the middle of that range.'],
      ['m', 'Sharpest band', 'Many sharks, such as the lemon shark, see most sharply along a band level with the horizon, which lets them scan the sea floor or the open water without moving their eyes. This view sharpens a band along the horizon.'],
      ['m', 'Pace', 'Sharks follow a flickering light up to 16 to 31 flashes a second, a quarter to a half of your rate, so quick movement smears for them. This view leaves trails behind anything that moves.'],
      ['m', 'Two eyes', 'A shark’s eyes sit on the sides of its head, and in a lemon shark the two fields overlap by only about 10 degrees in front. Hammerheads swing their heads from side to side as they swim. This view sweeps slowly from side to side, at a pace the app has chosen, and holds still while you turn the phone.'],
      ['m', 'Electric sense', 'Sharks feel the faint electric fields around living animals through gel-filled pores on the snout, called the ampullae of Lorenzini. A young hammerhead turns toward a prey-like field from about 30 centimetres away.'],
      ['i', 'The glow', 'No phone can sense an electric field. In the lower part of this view, where things are taken to be close, living movement shimmers to stand in for one, and that glow is the app’s own invention.'],
      ['x', 'Smell first', 'A hunting shark usually smells its prey first and follows the scent upstream, then turns to sight, the lateral line, the electric sense and touch as it closes in. The picture leaves smell out.']] };
  // Web-building spiders, from docs/views/sheets/spider.md (sections 2 and 3), with its proposed stand-ins for the web's shaking and for hearing through silk.
  TRY.spider = { chip: 'Spider', who: 'a spider', fov: 300, cpd: .5, pupil: 'o', gate: 1, persist: .15, ripple: 1, senses: { motion: 1, jolt: 1, mic: [60, 400] },
    cue: 'Hold still, as a spider holds its web. Only what moves reaches you.',
    rows: [
      ['m', 'The web', 'A Golden Silk Spider feels its prey through the silk, and a trapped insect shakes the web 5 to 30 times a second. The shaking arrives ten to thirty times stronger on some legs than on others, which gives the direction.'],
      ['g', 'Eyes', 'Most spiders have eight eyes and few see well. Most register little more than changes between light and dark, and spiders that build webs lean on the shaking of the silk.'],
      ['g', 'Sharpness', 'A wandering spider resolves nothing finer than about 2 degrees, under a hundredth of your sharpness. The picture borrows that figure for web builders.'],
      ['g', 'Pace', 'A wandering spider stops following flicker between 4.3 and 8.6 times a second, a seventh of your rate or less, so movement smears into trails.'],
      ['i', 'Knocks and low sounds', 'Where the phone’s motion sensors or its microphone are switched on, a knock on the phone or on the table it lies on, or a low sound, sends ripples across the picture. They stand in for a shaking web, and the ripples are the app’s own drawing.'],
      ['x', 'Hearing through silk', 'A bridge spider turns toward a loudspeaker three metres away, because its web moves with the air and works as a listening surface up to 10,000 times larger than its body.'],
      ['x', 'Wolf spiders', 'Wolf spiders have four large rear eyes backed by a mirror layer, which shines back in a flashlight beam and helps them spot movement in dim light. This picture leaves that out.']] };
  var TRY_KEYS = ((/[?&]try=([a-z,]+)/.exec(location.search || '') || [0, ''])[1]).split(',').filter(function (k) { return TRY.hasOwnProperty(k); });
  if (/[?&]selftest=1(?:&|$)/.test(location.search || '') && !TRY_KEYS.length) TRY_KEYS = Object.keys(TRY);   // the self-test draws them all
  TRY_KEYS.forEach(function (k) { EYES[k] = TRY[k]; });

  function clamp(x, a, b) { return x < a ? a : x > b ? b : x; }
  function lerp(a, b, t) { return a + (b - a) * t; }
  function ease(t) { t = clamp(t, 0, 1); return t * t * (3 - 2 * t); }
  var SHAPES = { whole: 0, strip: 1, ellipse: 2, annulus: 3, band: 4, cross: 5 };
  // A zone's size is a fraction of the camera picture's long side (size: [half width, half height]), or degrees of the world (deg: [width,
  // height]), taking the long side of a phone camera's picture to span CAM_DEG degrees. An assumption: main cameras span about 60 to 70.
  var CAM_DEG = 64;
  // A zone states only what differs from its view; everything it leaves out is the view's own value (docs/ENGINE.md).
  function zoneOf(z, P) {
    var at = z.at || [.5, .5], size = z.deg ? [z.deg[0] / 2 / CAM_DEG, z.deg[1] / 2 / CAM_DEG] : z.size || [.5, .5];
    var tilt = z.tilt || [0, 0];
    return { id: z.id || '', shape: SHAPES[z.shape] || 0, cx: at[0], cy: at[1], hw: size[0], hh: size[1], inner: z.inner || 0, soft: z.soft === undefined ? .04 : z.soft,
      rot: (z.rot || 0) * Math.PI / 180, gaze: z.gaze ? +z.gaze || 1 : 0, frac: z.frac || null, tiltU: tilt[0] * Math.PI / 180, tiltD: tilt[1] * Math.PI / 180, gap: (z.gap || 0) / CAM_DEG, tip: z.tip === undefined ? 1 : z.tip,
      inv: z.cpd ? 1 / z.cpd : P.inv, M: z.M || P.M, sat: z.sat === undefined ? P.sat : z.sat, gain: z.gain || P.gain, gate: z.gate === undefined ? P.gate : z.gate,
      rate: z.rate || P.rate, glow: z.glow === undefined ? P.glow : z.glow, living: z.living === undefined ? P.living : z.living,
      uv: z.uv === undefined ? P.uvBlue : z.uv, uvR: z.uvR === undefined ? P.uvR : z.uvR, sheen: z.sheen === undefined ? P.sheen : z.sheen, mag: z.mag || 1 };
  }
  var ZNUM = ['inv', 'sat', 'gain', 'gate', 'glow', 'living', 'uv', 'uvR', 'sheen', 'mag'];
  function neutralZone(z, P) {                     // the same place and shape, drawn as the other view would draw it there
    var o = {}, k; for (k in z) o[k] = z[k];
    o.inv = P.inv; o.M = P.M; o.sat = P.sat; o.gain = P.gain; o.gate = P.gate; o.rate = P.rate; o.glow = P.glow; o.living = P.living; o.uv = P.uvBlue; o.uvR = P.uvR; o.sheen = P.sheen; o.mag = 1;
    return o;
  }
  function withGenus(m, named) {                  // a view's settings for one genus, where the view lists any (byGenus)
    var g = named && typeof named.scientific === 'string' ? named.scientific.trim().split(/\s+/)[0] : '';
    var v = m && m.byGenus && g && m.byGenus.hasOwnProperty(g) ? m.byGenus[g] : null, o, k;
    if (!v) return m;
    o = {}; for (k in m) o[k] = m[k];
    for (k in v) if (k !== 'zones') o[k] = v[k];
    if (v.zones && m.zones) o.zones = m.zones.map(function (z) { var w = v.zones[z.id], r = {}, j; if (!w) return z; for (j in z) r[j] = z[j]; for (j in w) r[j] = w[j]; return r; });
    return o;
  }
  function paramsOf(m, named) {
    m = withGenus(m || {}, named);
    var s = clamp(180 / (m.fov || 180), .45, 1);
    var P = { zoom: s, barrel: (1 - s) * .9, fovea: m.fovea || 1, inv: 1 / (m.cpd || HUMAN_CPD), fall: m.fall || 0, wA: m.topoA || 0, wS: m.topoS || 0,
      dof: m.dof || 0, ax: m.pupil === 'v' ? .3 : 1, ay: m.pupil === 'h' ? .3 : 1, M: m.M || I3, uvBlue: m.uvBlue || 0, sheen: m.sheen || 0,
      gain: m.gain || 1, sat: m.sat === undefined ? 1 : m.sat, noGreen: m.noGreen || 0, gate: m.gate || 0, field: m.field || 0,
      persist: m.persist || 0, hold: m.hold || 0, thrust: m.thrust || 0, rate: m.rate || 1,
      glow: m.glow || 0, living: m.living || 0, uvR: m.uvR || 0, sal: m.salience ? 1 : 0, ripple: m.ripple || 0, shimmer: m.shimmer || 0,
      pan: m.sweep ? m.sweep[0] : 0, panS: m.sweep ? m.sweep[1] : 1 };
    P.glowC = m.glowC || [1, 1, 1];
    P.zones = m.zones ? m.zones.slice(0, 4).map(function (z) { return zoneOf(z, P); }) : null;
    P.gz = m.gaze || null; P.senses = m.senses || null; P.water = m.water || null; P.waterC = m.waterC || null;
    return P;
  }
  var HUMAN = paramsOf(null);
  function mixZones(a, b, t) {
    var za = a.zones || [], zb = b.zones || [], n = Math.max(za.length, zb.length), out = [], i;
    for (i = 0; i < n; i++) {
      var A = za[i] || neutralZone(zb[i], a), B = zb[i] || neutralZone(za[i], b), z = {}, k;
      for (k in B) z[k] = B[k];
      ZNUM.forEach(function (f) { z[f] = lerp(A[f], B[f], t); });
      z.M = A.M.map(function (x, j) { return lerp(x, B.M[j], t); });
      z.rate = t > .5 ? B.rate : A.rate;
      out.push(z);
    }
    return out;
  }
  function mix(a, b, t) {
    var o = {}, k;
    for (k in a) if (typeof a[k] === 'number') o[k] = lerp(a[k], b[k], t);
    o.M = a.M.map(function (x, i) { return lerp(x, b.M[i], t); });
    var src = t > .5 ? b : a;                      // the pace of movement switches whole, half way
    o.persist = src.persist; o.hold = src.hold; o.thrust = src.thrust; o.rate = src.rate; o.gate = t > .5 ? b.gate * clamp(t * 2 - 1, 0, 1) : 0;
    var z = b.zones || b.sal ? b : a;               // what comes with zones keeps to the view that has them
    o.glowC = z.glowC; o.gz = z.gz; o.senses = z.senses; o.waterC = (b.water ? b : a).waterC;
    o.water = a.water || b.water ? [0, 1, 2, 3].map(function (i) { return lerp(a.water ? a.water[i] : 0, b.water ? b.water[i] : 0, t); }) : null;
    o.zones = a.zones || b.zones ? mixZones(a, b, t) : null;
    return o;
  }
