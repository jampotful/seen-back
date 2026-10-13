# Engine design

Written 13 October 2026 by the design agent (branch `agent/design`). It turns `docs/views/ATLAS.md` into engine modules, a spec format that makes a view into data, a tuning panel with a compare slider, and a method for measuring the smallest visible change of each parameter. The engine today is `src/cam.b.js` (three passes: the frame ring, the time pass, the view pass), fed by `paramsOf` and `mix` in `src/cam.a.js` and by the per-frame `fx` object from `src/cam.c1.js`.

## 1. Principles

- **One view pass stays one pass.** Every module that changes how a pixel looks adds terms to the existing view pass (`FS_VIEW`). The 16-tap blur loop runs once per pixel whatever the number of zones: zones blend their parameters first, then the loop samples once with the blended radius. This keeps today's frame time within a few per cent.
- **Controllers live on the processor and write uniforms.** Anything that needs a decision (where the gaze goes, how bright the room is, whether a knock arrived) runs in JavaScript at a few updates a second and hands numbers to the shaders. Reads from the graphics chip go through a pixel buffer and a fence (`readPixels` into a `PIXEL_PACK_BUFFER`, then `clientWaitSync` polled with a zero timeout), so no frame waits.
- **Inputs stay behind flags and a person's tap.** Motion, compass, microphone and vibration each sit behind a flag that the app thread turns on. Nothing asks for a permission without the person's own action, and every view still draws with every input refused.
- **A view is data.** After module 0 below, adding a view means adding one JSON file. Code changes only when a mechanism needs a module that does not exist.

## 2. The modules, in build order

The order follows the record share of the views each module lets a spec draw faithfully (the atlas's weights, which sum the shares of world records in `docs/VIEWS.md` and `docs/COVERAGE.md`). Where a module only adds a new option to a view that already draws, the table counts it at the atlas weight of that mechanism, and the "new views" column counts the groups that today get the "no view yet" notice. Weights are my estimate from the atlas, rounded; they overlap.

| Order | Module | New views it unlocks (share) | Atlas mechanisms it serves (weight) | Cost on a phone |
|---:|---|---|---|---|
| 0 | `spec` loader | fungus 2.81, fish 1.55, spider 1.32, snail 1.23, sealife 0.86, crab 0.73, mammal 0.60, salamander 0.37, worm 0.20, shark 0.08, slime 0.07, bat 0.04, tick 0.04, flying fox 0.01: **9.9%** | all, as data | none at run time |
| 1 | `zones` | jumper 0.40 (with 6 and 7), scorpion and harvestman 0.14 | 1 sharpness (58), 3 pupils (2.8), 12 several eyes (0.9); corrects bird, hawk, wader, crab | low |
| 2 | `spectrum` | none new; corrects bird (ultraviolet against violet families), insect, bee, every dichromat | 5 more colours (46), 4 fewer colours (7) | low |
| 3 | `light` | none new; makes owl and duck worth splitting from bird (2.3) | 13 light with no image (42), 7 dim light (3.0), 14 shadows (2.5), 25 clocks (2.0) | low |
| 4 | `pace` | none new | 8 flicker and pace (50) | low to medium |
| 5 | `motion` | none new | 11 stabilization (19), 21 magnetic (16), 2 field by tilt, 15 vibration (1.9), 24 gravity | low |
| 6 | `salience` | jumper (with 1 and 7) | 9 motion only (3.1), 10 gaze (2.2), 16 flow (3.8) | medium |
| 7 | `gaze` | jumper 0.40 complete | 10 gaze (2.2) | low (processor) |
| 8 | `field` | duck setting | 2 field shape (40), Snell's window for fish and shark (1.6) | low |
| 9 | `overlay` | none new | 21 magnetic grain (16), 6 polarization (0.8), 15 web, 14 rings, 17 sound circles | low to medium |
| 10 | `sound` | owl hearing | 17 hearing (2.1), 16 airflow (3.8), 15 the mole's rumble, 18 clap and see, 22 breath | low |
| 11 | `haptic` | none | 4 same or different, 5 colour in the palm, 15 feel it back, 19 warmth | none on the chip |
| 12 | `slow` | none | 24 growth time (2.9), 7 long exposure | low (a small store) |
| 13 | `depth` | bat echo image (native) | 18 echolocation (0.2), 3 depth | high; native build only |

Two notes on the order. Module 0 comes first because about a tenth of all world records belong to groups whose checked sheets already fit today's fields; those views wait only for a way to load them. And `light` sits before `pace` in practice although its weight is lower, because `spectrum`, `zones` and `pace` all read its uniforms (the adapting colour matrix, the night shift, the pupil that answers to light); it is a small module, and building it third costs little.

### Module 0: `spec`

- **What it does.** Loads views from JSON (section 3), turns each into the flat parameter object the engine reads today, and keeps `EYES` working for old encounters.
- **State.** A table of specs keyed by view; a resolver that picks the view from the species, then the genus, then the group (`PLAN.md`, principle 2).
- **How it composes.** `paramsOf(spec)` reads `spec.params[name].value`, falling back to the defaults it uses now. `mix` blends two param objects as it does now, and blends module blocks field by field, switching enumerated fields (zone shapes, input flags) at the half-way point as it does for `hold` and `rate`.
- **Build.** `build.py` inlines every `views/*.json` into the page as one object, so there is no network request at run time. `?try=<view>` reaches any spec, offered or not.

### Module 1: `zones`

- **What it does.** Up to four regions in one view, each with its own sharpness, blur shape, colour matrix, saturation, gain, motion gate and magnification, blended with soft edges. Zone 0 is the whole field and takes the remainder of the weights.
- **Shapes.** `whole`, `spot` (an ellipse), `strip` (upright), `band` (level, with an optional second band for the crabs' two streaks), `annulus`, `window` (a rounded rectangle with its own centre, for the tick, harvestman and starfish), each with a centre, a size, a rotation and a softness. Weights are computed analytically in the shader, so no texture is needed. A painted map (a 64 by 64 texture of four weights) is the fallback for shapes the analytic set cannot make.
- **Uniforms.** `u_zShape[4]` (int), `u_zC[4]` and `u_zS[4]` (vec2 centre and size), `u_zRot[4]`, `u_zSoft[4]`, `u_zBlur[4]` (cycles per degree turned into a radius as `blur` is now), `u_zAniso[4]` (vec2, replacing the global `u_aniso` and serving the crab's five-to-one ratio and the cat-dog draft's numeric pupil aspect), `u_zFall[4]`, `u_zM[4]` (mat3, or the 3 by 4 of module 2), `u_zSat[4]`, `u_zGain[4]`, `u_zGate[4]`, `u_zMag[4]`, `u_zEdge[4]` (a thin border for the loupe option). About 60 uniform vectors, under WebGL2's minimum of 224 for a fragment shader.
- **State.** None on the chip. The zone centres can be moved by `gaze` (module 7), by touch (the thumb-as-fovea option of mechanism 1), or by `motion` (the crab's level band).
- **How it composes.** At the top of the view pass, after the field remap, the shader computes four weights and blends every per-zone value into one set. The existing blur radius line becomes `ra = blendedBlur * (1 + blendedFall * r²) + u_soft`; the 16-tap loop is unchanged. Magnification enters the `mag` term already there. After colour, the blended matrix, saturation and gain replace the global ones, and the gate mix becomes `blendedGate`. The time pass computes its trail for the whole frame as now, and the view pass applies it per zone, which gives the jumping spider a gated surround and an ungated strip.

### Module 2: `spectrum`

- **What it does.** Maps four input channels (red, green, blue and the invented ultraviolet channel the shader already builds as `uvg`) onto the screen's three through a 3 by 4 matrix per zone, and blends between a light-adapted and a dark-adapted matrix by the `light` module's level (the snail's `adaptM`). It adds the neutral-band shimmer of mechanism 4 as an optional term: pixels whose two strongest animal channels are nearly equal get a faint animated noise.
- **Uniforms.** `u_M4` (two `mat3` plus a `vec3` for the ultraviolet column, or a `mat3x4`), `u_M4dark`, `u_adapt`, `u_rotate4` (an integer 0 to 3 for the colour-wheel option, which picks which three of the four channels are shown), `u_neutral` (strength).
- **Data.** Matrices are computed off line from each animal's pigment peaks, a standard pigment template, and a phone camera's spectral response, by a script that writes them into the spec with their sources. The `DEUTAN` and `PROTAN` matrices entered from memory are replaced by this script's output (cat-dog draft, section 6; `spider.md`).
- **How it composes.** It replaces the lines from `vec3 m = u_M * c` to the `sheen` mix. `sheen` and `uvBlue` become entries of the fourth column.

### Module 3: `light`

- **What it does.** Measures the scene: mean luminance, mean colour, the direction of the brightest region, and the rate of darkening, from the smallest mip levels of the time texture (an 8 by 8 level), read back without waiting four times a second. Where `getSettings()` reports exposure time and ISO, it corrects the luminance to an absolute light level; otherwise it uses relative brightness. It also keeps the clock, the time zone, the sun's rough height and the moon's phase computed from the date.
- **Uniforms it writes.** `u_lux` (log light level, smoothed over two to three seconds), `u_lightDir` (vec2), `u_lightCol` (vec3), `u_dark` (a 0 to 1 night factor from the clock with the two-hour ramps the scorpion needs), `u_moon`, `u_shock` (a decaying value set when the frame darkens by more than a spec's threshold within a third of a second).
- **What reads it.** `spectrum` (adaptation), `zones` (gain, saturation and blur that follow light: the dog's sharpness falling with the logarithm of light, the owl's twilight peak, the cat's pupil that opens and closes), the aperture (the flinch and the pupil-as-frame options), the field (the lean toward or away from light, and the compass of light).
- **How it composes.** It adds no pass. A view's parameters may name a curve against `u_lux` (section 3, `curve`), which `paramsOf` evaluates each frame on the processor.

### Module 4: `pace`

- **What it does.** Keeps today's lag-and-catch-up and hold-and-thrust in the time pass, and adds a replay ring: about one second of frames at a quarter of the picture's resolution (about 16 layers at 15 a second), played back stretched by a spec's ratio when the person taps. The strobe option of mechanism 8 is a detector and a drawing: the detector looks for the rolling bands that mains lighting leaves in short exposures (a periodic pattern along the sensor's rows from frame to frame), and the drawing turns them into a visible flash on lamps and screens for fast eyes.
- **Uniforms and state.** `u_replay` (0 or 1), `u_replayT`, a second texture array for the replay ring; `u_strobe` and a small texture of where bands were found.
- **How it composes.** All in the time pass. The replay reads from its own ring in place of the live frame; the strobe adds a term to `base`.
- **Risk.** Whether a browser's camera stream shows the bands at all depends on its exposure, which a web page cannot set on most phones. The strobe needs a test on a phone before anyone builds the drawing.

### Module 5: `motion`

- **What it does.** Reads device orientation and motion (gyroscope, accelerometer, gravity) and the compass heading, after a tap on iOS (`DeviceMotionEvent.requestPermission`). It removes the phone's own movement from the camera's apparent motion for `salience`, gives the tilt for `field`, the knocks and their side for vibration views, the thrusts for the arm-as-neck option, and the heading for the magnetic options. The step detector the app already has joins it.
- **Uniforms it writes.** `u_rot` (a 3 by 3 from the phone's orientation), `u_tilt`, `u_heading`, `u_knock` (vec3: strength and the side of the first jolt, decaying), `u_stab` (the image shift that holds the world still, in screen units).
- **How it composes.** `u_stab` offsets the sampling coordinate at the top of the view pass, which is how the locked-world option holds the picture against the hand's tremor. Accelerometer reads at 60 a second or faster where the phone allows, as `spider.md` asks.

### Module 6: `salience`

- **What it does.** Builds a 64 by 64 map of motion energy from the difference between the newest two ring layers, after shifting by the phone's own motion (from `motion`, or from the mean image shift when sensors are refused). A second channel marks living motion: motion that is coherent over a small patch and changes rhythmically, approximated by local flow coherence over three ring layers (`docs/tracks/engine.md`; `jumper.md`). A third channel holds the inhibition-of-return mask, written by `gaze` and decaying over about five seconds (Ferrante and colleagues 2024).
- **State.** One RGBA8 64 by 64 target, written after the ring each second frame; read back asynchronously a few times a second.
- **How it composes.** A small extra pass between the ring write and the time pass. The time pass can read it to replace its own per-pixel gate (with the phone's motion removed, a frog view no longer needs a perfectly still hand). The view pass can read it for the flow lines and the edge pressure of mechanism 16.

### Module 7: `gaze`

- **What it does.** Moves a zone to the most salient place outside the inhibition mask, with a fast jump, a dwell, small scanning sweeps and a hold, and writes the place it leaves into the mask. It also runs the goshawk's locked pursuit (the zone follows the target at a fixed offset) and the stamps option (each fixation copies a small sharp thumbnail into a stamp texture that fades).
- **State.** A processor-side state machine; spec parameters `jumpMs`, `dwellMs`, `scanDeg`, `scanHz`, `iorSeconds`, `bias` (how much living motion outweighs any motion, and in which zone).
- **How it composes.** It writes `u_zC` for its zone and draws the mask into `salience`. Stamps add one small texture array and a few lines at the end of the view pass.

### Module 8: `field`

- **What it does.** Generalizes the remap at the top of the view pass: today's barrel squeeze, plus a blind wedge (a direction, a width and a softness), Snell's window (when `u_tilt` points upward, the scene is remapped through `arcsin(sin θ / 1.33)` into a disc about 97 degrees across, as `fish.md` gives), the duck's sky fold, and the panorama ribbon. The ribbon keeps a cylinder texture (for example 2048 by 256) into which frames are written at the angle the gyroscope reports, fading with age.
- **Uniforms.** `u_wedge` (vec3), `u_snell` (0 or 1), `u_fold`, `u_pano` (0 or 1) and the cylinder texture.
- **How it composes.** All before the zone weights are computed, since zones live in the animal's field. The ribbon adds one write per ring write.

### Module 9: `overlay`

- **What it does.** Procedural drawing added at the end of the view pass: ripple rings from a point and a time, the drawn web of mechanism 15, shadow rings, the brushed-metal grain aligned to `u_heading`, the polarization band computed from the sun's position and the phone's orientation, the row of lamps, streamlines bent by `salience`, sound circles. Each is a function of a few uniforms and the pixel's position, so each costs a handful of instructions and nothing when switched off.
- **Uniforms.** A small array of events (`u_evt[8]`: position, start time, kind, strength) written by `motion`, `sound` and `light`, plus per-overlay strengths.
- **How it composes.** After colour and before the aperture mask. Overlays that should sit in the world (the polarization band) are positioned with `u_rot`.

### Module 10: `sound`

- **What it does.** Opens the microphone after the person's tap and a plain-words request, runs an `AnalyserNode`, and reports energy in three bands (about 50 to 300 a second for the mole's rumble and spiders' hums, the middle, and above about 5,000 for the owl), onsets, and a breath detector (low, broad, sustained noise). It can also click through the speaker at a spec's rate for the clap-and-see option, and measure the time to the echo where the room allows (untested).
- **Uniforms it writes.** `u_band` (vec3), `u_onset` (decaying), `u_breath`; events into `u_evt`.
- **How it composes.** No pass. It feeds `overlay`, `zones` (the dark owl's flash of light), the aperture and the gate.

### Module 11: `haptic`

- **What it does.** Plays vibration patterns through `navigator.vibrate` where it exists (Android browsers), and draws a pulse at the frame's edge where it does not. A native build would use the platform's finer haptics.
- **State.** A queue of patterns; spec parameters name a pattern and what triggers it (a tap whose two colours the animal confuses, the invented ultraviolet channel under the thumb, a knock, a detected body).
- **How it composes.** No pass, except the edge pulse in `overlay`.

### Module 12: `slow`

- **What it does.** Keeps one frame every few seconds in a small store at a quarter of the resolution and averages them with a weight set by the spec, over ten minutes or more, for the fungus and slime mould and the long-exposure option of dim light. It works around the floor of 0.2 that the time pass puts on its averaging weight when the phone lacks float textures (`fungus.md`), because the store accumulates in its own float or 16-bit target.
- **How it composes.** The time pass can take its `base` from the store in place of the live frame.

### Module 13: `depth`

- **What it does.** Gives a depth map from LiDAR on phones that have it, or from a monocular depth model, at a few maps a second. Native build only for LiDAR; a model in the browser is possible and heavy.
- **How it composes.** Replaces the guess from height in the frame (`rd` in the view pass) with a texture read, and drives the echo image of mechanism 18.

## 3. The spec: a view as data

One JSON file per view in `views/<key>.json`. `build.py` inlines all of them. `paramsOf` turns a spec into the engine's flat parameter object; a `?try=<key>` address loads any of them.

```json
{
  "key": "jumper",
  "version": 1,
  "chip": "Jumping spider",
  "who": "a jumping spider",
  "falls_back_to": "spider",
  "applies_to": { "family": ["Salticidae"] },
  "cue": "The sharp strip jumps to whatever moves. Hold still and watch it hunt.",
  "modules": ["zones", "spectrum", "salience", "gaze"],
  "params": {
    "fov":  { "value": 350, "grade": "m", "invented": false, "src": ["jumper.jsonl:De Agrò 2024"], "range": [180, 360], "floor": null },
    "cpd":  { "value": 1.0, "grade": "g", "invented": true,  "src": ["spider.md#jumper: Morehouse 2020"], "range": [0.1, 60], "note": "surround" },
    "rate": { "value": 1.5, "grade": "g", "invented": false, "src": ["jumper.md: Tan et al. 2023 citing Clark and Uetz 1990"], "range": [0.2, 2] }
  },
  "zones": [
    { "shape": "whole", "cpd": "@cpd", "sat": { "value": 0, "grade": "m", "invented": false, "src": ["spider.md: Shepeleva 2022"] },
      "M": "green_only", "gate": { "value": 1, "grade": "m", "invented": false, "src": ["jumper.jsonl:De Agrò 2024"] } },
    { "shape": "strip", "centre": [0, 0], "size": { "value": [0.06, 0.5], "grade": "g", "invented": true, "src": ["jumper.md"] },
      "cpd": { "value": 8, "grade": "g", "invented": true, "src": ["spider.md: Morehouse 2020; Shepeleva 2022"] },
      "M": "jumper_uv_green", "mag": { "value": 2.5, "grade": "i", "invented": true }, "gate": 0, "driven_by": "gaze" }
  ],
  "gaze": {
    "dwellMs":    { "value": 900,  "grade": "i", "invented": true },
    "iorSeconds": { "value": 5,    "grade": "m", "invented": false, "src": ["jumper.jsonl:Ferrante 2024"] },
    "bias":       { "value": 2,    "grade": "m", "invented": true, "src": ["jumper.jsonl:De Agrò 2024"], "note": "living motion weighted over any motion in the front 100 degrees" }
  },
  "matrices": {
    "green_only":       { "rows": [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]], "grade": "g", "invented": true, "src": ["spider.md"] },
    "jumper_uv_green":  { "from_pigments": [370, 532], "grade": "m", "invented": true, "src": ["spider.md: De Voe 1975"] }
  },
  "by": {
    "genus": { "Habronattus": { "matrices": { "jumper_uv_green": { "from_pigments": [370, 532, 580], "grade": "m", "src": ["jumper.md: Zurek 2015"] } } } }
  },
  "inputs": { "motion": "optional", "sound": "none", "haptic": "none" },
  "rows": [
    ["m", "Eight eyes, one picture", "Six of a jumping spider's eyes watch for movement all around it, and two large front eyes swing toward whatever they report to look closely.", ["jumper.jsonl:De Agrò 2024"]]
  ]
}
```

The values above illustrate the format and are drafts; the research thread and the specialist set the real ones.

Rules of the format:

- **Every number that changes the picture is a parameter object** with `value`, `grade` (`m` measured in this animal, `g` measured in a relative or a wider group, `i` a guess), `invented` (true when the app chose the number, the mapping or the drawing, even if a measurement lies behind it), `src` (log lines or sheet sections; empty for `i`), and optionally `range` (for the tuning panel), `floor` (filled by section 5) and `note`.
- **A plain value** may stand in for a parameter object only where the engine needs a switch with no claim behind it (`"gate": 0` in a zone that never gates).
- **`@name`** refers to another parameter, so a zone can reuse the view's `cpd`.
- **`curve`** in place of `value` gives a value against a measured input: `{ "curve": "lux", "points": [[-2, 2.6], [1.6, 9]] }` interpolates in the logarithm of light, as the dog's measured fall of sharpness asks (cat-dog draft, section 2.3).
- **`by`** overrides by species, genus or family, applied when the full database names the species (`PLAN.md`, principle 2). An override names only what changes.
- **`modules`** lists what the view needs; a view whose module is missing on a build falls back to `falls_back_to`, and failing that to the group's notice.
- **`inputs`** says which phone inputs the view uses and whether it still draws without them (`optional`) or has no sense without them (`required`, in which case the view explains the input before asking).
- **Rows** keep today's form, with a fourth element listing sources, so a row's grade and its parameters' grades can be checked against each other by script.
- **A checker** (`tools/views/check_spec.py`, to write with module 0) refuses a spec where a row says `m` and every parameter it describes says `i`, where a parameter has `grade: m` and no `src`, where a value sits outside its `range`, or where an `invented` parameter has no `i` or `g` row that says so.

## 4. The tuning panel and the compare slider

**Reached by** `?try=<view>&tune=1`, offered nowhere else, as `PLAN.md` describes.

**The panel.** A drawer from the bottom edge that covers at most a third of the screen, so the picture stays visible. It lists every parameter of the spec, grouped by module and zone, each with:

- a slider over its `range`, whose step is the parameter's visibility floor at the current value (section 5), so every step of the slider is a change the person can see and no step is wasted;
- the grade as a letter and a coloured mark for `invented`, so the person sees at once which numbers rest on measurement;
- the source on a long press;
- a reset to the spec's value.

At the top: the view's name, a toggle for each phone input the view uses, and two buttons. **Copy** puts a JSON patch of the changed parameters on the clipboard (only the `value` fields, with the view's key and version), which the owner pastes into a chat or a pull request. **Keep** stores the patch in this phone's browser storage, per view, so the tuning survives a reload; storage is wrapped so that the page works when it is refused.

**The compare slider.** A vertical divider the person drags across the picture. Left of it is the person's own view, right of it the creature's. The engine draws the view pass twice per frame with the scissor test: once with `HUMAN` parameters over the left rectangle, reading the live frame directly with no time pass, and once with the creature's parameters over the right. The fill cost is one full screen, as now, plus the uniform setting of a second draw. The divider's position is a uniform, so the field remap (the squeeze) is computed for the whole screen and both halves line up at the divider. A double tap swaps the sides; a long press on the divider hides it. For views whose sense is not a picture (sound, touch, vibration), the left side shows the camera and the right side the view, and the panel's input toggles let the person switch the sense on and off.

The compare slider doubles as the race of mechanism 7 when the spec asks for it: the human side then takes its own dim-light curve, so a darkening room drowns the left half first.

## 5. The visibility floor

**Purpose.** For each parameter, the smallest change a person can see on a phone-sized render. Research on a value stops once the value's uncertainty is smaller than the floor at that value (`PLAN.md`, principle 5), and the tuning panel steps by the floor.

**The fixed clip.** A clip of 8 seconds, recorded once and kept in the repository's test assets at 720 by 1280, chosen to hold what the parameters act on: a textured near surface and a far one, saturated reds, greens, blues and yellows, a bright window and a deep shadow, a person walking slowly and a hand moving fast, and a pan of the phone. A second, still clip (2 seconds of a still scene) serves the parameters that act on a still picture. A scripted light ramp (the clip's brightness scaled from full to a hundredth over its length) serves the `light` curves.

**The render.** Headless Chromium (`test/check4.js` gains a `floor` mode) draws the view at 390 by 844 CSS pixels at a device pixel ratio of 2, the size of a common phone, with `VIEW_DEG` at 24 as the page uses for a touch screen. The engine's own sensors are replaced by recorded values so that runs repeat exactly.

**The comparison.** For a parameter at value `v`, render the clip at `v` and at `v + d`, frame by frame. Downsample both renders to what a person resolves at arm's length: a phone 7 cm wide at 35 cm subtends about 11.4 degrees, so 780 device pixels span 11.4 degrees and a person's limit of about 60 cycles per degree is 684 cycles across, which is above the render's 390 cycles; the render is therefore compared at full resolution, after a blur matching the eye's contrast sensitivity falloff (my construction; the eye model is the standard one and its constants should be checked). Then compute, per frame, the 95th percentile of the colour difference in CIELAB (ΔE\*ab) between the two renders, and for temporal parameters the same on the frame-to-frame differences. A change counts as visible when that percentile exceeds a threshold in at least 10% of frames.

**The threshold.** Start at ΔE\*ab of 2.3, a commonly cited just-noticeable difference (Mahy, Van Eycken and Oosterlinck 1994; I have not opened it in this session, so the figure should be checked before it is relied on). Then calibrate on a phone with the owner: for a dozen parameters, the panel offers pairs of renders at `v` and `v + d` in a random order with a third identical one (an odd-one-out test), steps `d` up and down, and records where the owner is right two times in three. The ratio between that and the computed threshold rescales the threshold for all parameters.

**The search.** For each parameter, at five values spread over its `range` (and at the spec's value), halve and double `d` until it brackets the threshold, then refine by bisection to within 10%. Write the results to `docs/views/floor.json` as `{ "<param>": [[v, d_visible], ...] }`, by view where a parameter's effect depends on the view (sharpness is easier to see in a view with no other blur). Run on a build machine; it is many renders and no judgement. A parameter whose largest change across its range never crosses the threshold is marked `invisible`, and research on it stops.

**A plain alternative, to compare once.** The same renders compared with the structural similarity index on the luminance channel, with a fixed cut-off. If the two methods agree on most parameters, the cheaper one stays.

## 6. What to build first, and what to check on a phone

1. Module 0 with the spec checker, and the existing fourteen views converted to specs by script with no change to the picture (the test is that every existing check in `test/check4.js` passes and the screenshots match).
2. The tuning panel and the compare slider, since every later module is judged through them.
3. `light`, then `zones`, then `spectrum`, `salience` and `gaze`, which together draw the jumper view the queue puts first (`QUEUE.md`, entry 4).
4. The visibility floor's render harness, run on the jumper's parameters first.

Needs a real phone before anything is built on it: whether a browser's camera stream shows mains flicker (module 4's strobe); how often the accelerometer reports on each phone (vibration views); whether `getSettings()` reports exposure time (module 3's absolute light level); whether `navigator.vibrate` reaches the motor in the owner's browser.
