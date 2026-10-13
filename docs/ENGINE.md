# The picture engine: fields added in build 23

This file describes what the engine in `src/cam.b.js` understands beyond the fields listed in `docs/views/research/BRIEF.md`, what each field draws, what it costs, and the evidence it serves. The evidence named here is in the log of the senses research: `docs/views/evidence/jumper.jsonl` on the branch `research/jumper` (211 lines when this was written, 13 October 2026), with the draft `docs/views/drafts/jumper.md`. A value marked *invented* is the app's own choice.

## How to see it and how to measure it

- **A view being tried** is reached only with `?try=<key>` (several with `?try=a,b`) and is offered nowhere else. Its entry lives in `TRY` in `src/cam.a.js` and joins `EYES` for that visit only, so a photo or a typed name in its group then opens it too. With `?try=`, Start opens the view on the camera at once, with no photograph first and no encounter kept; where the camera is closed it asks for a clip or a photo of the person's view. `&genus=Habronattus` (or any genus a view lists under `byGenus`) chooses that genus's settings, as a name from the recognizer does.
- **The About block** (tap the version line under About) now carries a line `Engine: … ms of script a frame, … ms on the graphics chip (timer query, n frames)`. The graphics chip's time comes from `EXT_disjoint_timer_query_webgl2` where the browser offers it; the answer arrives a few frames later and is polled, never waited for. Where the extension is missing the line says so, and the frame interval on the `Picture` line is the measure.
- **`node test/check4.js perf`** runs every view in `EYES` (and the views named by `TRY`, `jumper` by default) for `PERF_FRAMES` frames (60) on `test/assets/scene.webm` and prints a table. A frame's cost is measured from outside the page: the page's own animation callbacks plus a one-pixel read that waits for the graphics work. The same harness therefore measures any build, `main` included. Headless software graphics are slow and share the machine, so its numbers only compare views and builds with each other, on one machine.
- **`node test/check4.js try`** opens `?try=jumper` on the scene clip, slowed (`PLAYBACK`, 0.15) so that each frame drawn in software is about one clip frame after the last, as a camera delivers them, and checks that the movement map is read, that the gaze jumps, and what each fixation landed on, using `test/assets/scene.json` (written by `test/make_scene.py` with the clip). Screenshots go to `test/shots/engine/`.

## Zones

A view may carry `zones`: up to four regions drawn in one pass, layered in order over the view's own settings, each blended in by a weight with soft edges. Each zone states only what differs from its view.

| Field | Meaning |
|---|---|
| `shape` | `'whole'`, `'strip'` (a rectangle), `'ellipse'`, `'annulus'`, `'band'` (a horizontal band across the field), `'cross'` (two narrow fields, each bent in the middle, crossing like an X without touching) |
| `at` | centre, as fractions of the camera picture `[x, y]` (default the middle) |
| `size` or `deg` | half width and half height as fractions of the picture's long side, or full width and height in degrees of the world, taking the long side to span `CAM_DEG` (64) degrees, an assumption about phone cameras |
| `soft`, `inner`, `rot` | edge softness (fraction of the long side), the inner edge of an annulus (fraction of its size), and a turn in degrees |
| `tilt`, `gap`, `tip` | for a cross: the tilt from upright of its upper and lower arms in degrees, half the gap between its halves in degrees, and the weight kept at an arm's tip |
| `cpd`, `M`, `sat`, `gain`, `gate`, `rate`, `uv`, `sheen` | sharpness, colour matrix, saturation, dim-light lift, motion gating, pace, invented ultraviolet in blue, and violet sheen, as for a view |
| `glow`, `living` | how strongly movement glows here, and the extra weight of living movement (see Salience) |
| `mag` | magnification of what the zone holds, about its centre |
| `gaze` | 1: the gaze moves this zone (see Gaze) |

Zones are evaluated in the camera picture's own coordinates, so the time pass and the view pass agree on them, and the movement map and the gaze use the same coordinates. A zone with its own `rate` keeps its own place in the frame ring (the time pass then uses a second program that blends the zones' moments); every other zone field costs nothing in the time pass. In the view pass the blur radius, gain, saturation, gating, colour matrix and ultraviolet are blended per pixel before the 16 samples are taken, so a zone adds arithmetic and no samples.

During the change of eyes a zone is blended from the view the person had (the same place and shape, drawn with that view's settings) to the new one, so a sharp strip fades in where it stands.

*Evidence served.* A jumping spider's eyes divide the work: six watch for movement around the animal and two inspect what they report (De Agrò, Rößler and Shamble 2024, `eye_role`), the front side eyes span about 100 to 114 degrees and the rear side eyes the rest of the circle (De Agrò and colleagues 2024; Land 1969; Goté and colleagues 2019, `fov_h_deg`), and the side eyes resolve 0.5 to 1.1 cycles a degree where the principal eyes resolve 3 to 12.5 (Land 1969; Goté and colleagues 2019; Williams and McIntyre 1980, `interreceptor_deg`, `acuity_cpd`). One picture with regions that differ in detail, colour and what draws attention is what the draft asks for (`docs/views/drafts/jumper.md`, section 2).

## Salience: the movement map

A view with `salience: 1` gets, on each new camera frame, four small passes (`FS_LOW`, `FS_SHIFT`, `FS_RES`, `FS_SAL` in `src/cam.b.js`):

1. a grey copy of the frame, 64 cells on its long side (square roots of brightness, so that noise in the dark counts for less);
2. how well this copy matches the last for each of 7 by 7 whole-cell shifts, and
3. the best of them to a fraction of a cell: the phone's own movement between the two frames, and the frame's mean brightness;
4. the map itself, in two outputs: energy (the change from the last frame once the phone's shift is taken out, above a noise floor and above what a slightly wrong shift leaves at an edge), a slow average of energy, a pulse term, a living term, and the recent direction of movement with a count of its reversals.

The **living** term is the app's own approximation (*invented*) of a cue for the movement of living things: movement whose direction holds across a 3 by 3 patch at each moment (coherence of normal flow) and swings back and forth over time (reversals of that direction), with a little weight on energy that pulses. A rolling ball keeps one direction, walking legs and beating wings do not, and random flicker has no coherent direction.

When the phone turns fast, energy is trusted less: by the shift found in the picture, and by the motion sensors where they are on (see Senses). The map's time constants follow the clip's own clock where there is one. The view pass samples the map with filtering, so movement glows as soft light.

A few times a second (every 160 ms at most) the map is copied into a pixel buffer behind a fence; a later frame checks the fence and reads the buffer only once the chip has finished, so no frame waits. A slow phone gives up detail in the map (64, then 48, then 32 cells) before it gives up any of the picture.

| Field | Meaning |
|---|---|
| `salience` | 1: compute the map for this view |
| `glow`, `living` | how strongly any movement glows, and the extra weight of living movement, for the view itself; zones may differ |
| `glowC` | the colour of the glow |

*Evidence served.* The side eyes respond only to movement (Land 1971, `motion`); the rear side eyes answer to any translating stimulus and the front side eyes are needed to tell biological from random motion (De Agrò, Rößler and Shamble 2024, `eye_role`, `motion`); moving gratings did not evoke orienting while small moving targets did, so whole-field motion is treated as background (Zurek and colleagues 2010, `motion`), which is why the phone's own movement is taken out.

## Gaze

A view with a `gaze` block moves every zone marked `gaze: 1`. The gaze reads the movement map each time a read arrives and moves a little every frame. Each figure below is the jumping spider view's value and the measurement behind it.

| Field | Jumping spider | Behind it |
|---|---|---|
| what calls it | movement only; `any` 0.6 for any movement and `living` 1.8 for living movement | stationary targets never start a saccade, a small movement of a target already in view does (Land 1969, `motion`); the weights are *invented* |
| `habit` | 0.75: movement that goes on at one place loses that share of its pull | habituation tied to retinal location: repeated movement at one place stops evoking turns within one or two movements (Land 1971, `motion`) |
| `surround` | 0.6: a mover counts for less where movement fills its surroundings | small moving targets evoke orienting and moving gratings do not (Zurek and colleagues 2010) |
| `saccade` | 40 ms plus 4 ms a degree; direct, with no overshoot | a 15 degree saccade is complete within 0.1 s, goes by the most direct route and does not overshoot (Land 1969, `eye_movement`) |
| `sweep` | 2 degrees across, one cycle in 1.2 s | side-to-side scanning sweeps about as wide as the target and never under 2 degrees, each cycle 1.1 to 1.3 s for small targets (Land 1969) |
| `twist` | 25 degrees each way, 2 s to turn, holding about 3.5 s at each end | both retinae rotate together 20 to 30 degrees each way, holding each extreme 2 to 5 s and taking about 2 s to turn (Land 1969) |
| `pursuit` | follows a moving target at up to 10 degrees a second; a faster one is caught with a new jump | once acquired, the retinae follow a target smoothly over at least 25 degrees, tested below 10 degrees a second (Land 1969) |
| `examine` | looks a target over for 4 to 12 s unless something else calls | scanning bouts last 5 to 94 s, most 20 to 40 s, broken after 10 to 20 s by excursions elsewhere (Land 1969); shortened for the screen (*invented*) |
| `distract` | 1.5: while a living target is looked over, a distraction must call this much more strongly | spiders examining a cricket image shifted their gaze to a distractor less often (Bruce and colleagues 2021, `motion`); a distractor moving in the front side eyes' field pulls the gaze by its motion alone (De Agrò and colleagues 2024) |
| `ior`, `iorDeg` | the place just looked at is left alone, its pull coming back steadily over 5 s, within about 6 degrees | after a principal-eye saccade the front side eyes withdraw attention from that place; detection there is poor about 0.2 s after and recovers steadily over about 5 s (Ferrante and colleagues 2024, `motion`); the reach of 6 degrees is *invented* |
| `hold`, `back` | when the target is gone, the gaze holds 1.5 s, then drifts back at 0.8 degrees a second | after a saccade without scanning, fixation holds 1 to 2 s and the retinae drift back; a 10 degree return takes 10 to 15 s (Land 1969) |
| `wander` | with nothing moving, a bout of sweeps every 8 to 20 s, 6 to 14 degrees each way | spontaneous side-to-side sweeps in bouts, up to 45 to 50 degrees, with a blank field (Land 1969); amplitude and spacing kept within the camera's picture (*invented*) |
| `sleep` | when the picture is dark and still for 3.5 s, bouts of twitching of 6 to 12 s every 20 to 40 s | sleep-like bouts of retinal movement at night, a median 77 s every 17 minutes in spiderlings (Rößler and colleagues 2022, `eye_movement`); the bouts here are much closer together (*invented*) |

The places just looked at (up to six) also dim the glow there, so the surround is seen to forget them. With `prefers-reduced-motion` the jumps glide over 0.45 s, and the sweeps, the twist, the wandering and the twitching are left out.

## Colour by genus

`byGenus: { <Genus>: { <field>: …, zones: { <zone id>: { … } } } }` replaces a view's settings for one genus, taken from the first word of the scientific name the recognizer or the person gave. The jumping spider view uses it twice: *Habronattus* gets a red-capable matrix in its `fovea` zone, the centre of the cross (Zurek and colleagues 2015: a red-filtered receptor class only in a small patch at the retina's centre, in five *Habronattus* species, `filter_pigments`, `colour_vision`), and *Portia* gets 12.5 cycles a degree (Williams and McIntyre 1980, `acuity_cpd`). Every other genus keeps ultraviolet and green (DeVoe 1975 for *Phidippus regius*; Zurek and colleagues 2015: no red filter in *Phidippus* and *Salticus*).

## Senses: the phone's own inputs

`senses: { motion: 1, mic: [low, high], jolt: 1 }` asks for the phone's own inputs. Each stays off behind `SENSE_ON` in `src/cam.c1.js` until the app's thread turns it on; a visit with `?try=` may turn them on with `&sense=motion,mic`. Nothing asks for a permission until the person taps the line on the picture that says, in plain words, what the input is for.

- **Motion sensors** (`devicemotion`; on an iPhone through `DeviceMotionEvent.requestPermission`, asked on that tap). The rate of turning makes the movement map trust its energy less while the phone turns fast, and stillness lets the gaze fall asleep in the dark. With `jolt`, a knock on the phone or on the table it lies on starts a ripple from that side, standing in for a web's vibration (`docs/views/sheets/spider.md`, section 4, item 1).
- **Microphone** (`getUserMedia` for sound only, after the tap). Sound is filtered to the band `[low, high]` in hertz, and each sudden rise starts a ripple from near the centre, since one microphone gives no direction. Nothing is recorded or kept, and the microphone is let go when the view changes. It stands in for hearing through hairs and through the web (`docs/views/sheets/spider.md`, section 4, item 2).
- **Ripples** (`ripple` on a view, from 0 to 1) are rings that run out across the picture at about half a screen height a second and fade over two seconds, drawn by displacing the picture.

## The jumping spider view (`?try=jumper`)

| Part | Values | Behind it |
|---|---|---|
| field | `fov` 350 | the side eyes cover almost the whole circle (Land 1969; De Agrò and colleagues 2024; Harland and colleagues 2012) |
| surround (rear side eyes) | 0.5 cycles a degree, green only, dim | posterior lateral eye 1.0 degree between receptors (Land 1969, *Phidippus johnsoni*); the side eyes carry one green receptor class near 535 to 540 nm (Yamashita and Tateda 1976) and see monochromatically (Goté and colleagues 2019); the dimness, so that glow can be seen, is *invented* |
| front zone (front side eyes) | an ellipse 114 by 98 degrees, 1.1 cycles a degree, living movement 1.6 times brighter | one front side eye about 70 by 98 degrees (Goté and colleagues 2019), the pair overlapping 25 degrees (Land 1969; Blest and colleagues 1981); 0.46 degrees in its acute zone (Goté and colleagues 2019), 0.47 in *P. johnsoni* (Land 1969); biological motion picked out by these eyes (De Agrò and colleagues 2024) |
| the cross (principal eyes) | two arms 2.5 degrees wide and 21 high, upper arms tilted 21 degrees, lower 8.5, inner edges 1.5 degrees apart, weight falling to 0.45 at the tips; 3.6 cycles a degree; ultraviolet and green; magnified 1.25 times | each principal retina about 2 degrees wide and 21 high, bent about 30 degrees, the two fields crossing with upper arms 40 to 45 and lower arms 15 to 20 degrees apart and inner edges 1 to 2 degrees apart (Land 1969); 3.3 to 3.8 cycles a degree in *Phidippus* (Land 1969; Harland and colleagues 2012); the arms at lower magnification and blurred (Williams and McIntyre 1980); the width (2.5 degrees for the screen) and the magnification are *invented* |
| colour in the cross | green drawn yellow-green, the guessed ultraviolet drawn blue | ultraviolet near 359 to 377 nm and green near 526 to 532 nm (Glenszczyk and colleagues 2021; DeVoe 1975; Zurek and colleagues 2015); the matrix and the ultraviolet guess are *invented* |
| gaze | as in the Gaze table | as in the Gaze table |

## What a real phone must judge

- The frame time of the zone and salience programs on a phone's graphics chip, and whether the map's read-back arrives within a frame or two (in headless software graphics a fence takes seconds to signal, because the chip's queue lags).
- Whether the phone's own movement is taken out well enough when the phone is held by hand, and how strongly a camera's own noise and exposure changes register as movement.
- The direction of a knock read from the motion sensors, and whether a phone's microphone records low sounds well enough for ripples.
- Whether the gaze's pace reads as a spider's on a phone held at arm's length.
