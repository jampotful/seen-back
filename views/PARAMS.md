# Parameter glossary

What each setting of a view's spec controls, which part of the picture it acts on, its units, and which eye or region of the animal its value comes from. `tools/views/compile.py` sends the entries a view needs with that view's request, so each entry is written to be read alone. The sources are `src/cam.a.js` (`paramsOf`, `zoneOf`), the shader in `src/cam.b.js`, and `docs/ENGINE.md`. A person's own values in the engine are the defaults: 60 cycles a degree, a field of 180 degrees, the pace 1.

The rule that decides most mistakes: **a setting written at the top of `params` acts on the whole picture, so its value comes from the eyes that cover most of the field. A region with its own eye (a sharp strip, a fovea, the middle of a cross) states its own values in `zones`, and a measurement of that eye goes there.** A jumping spider's large front eyes see 3.3 to 12.5 cycles a degree, but they cover a strip about 2 degrees wide, so that value belongs to the zone for those eyes. The side eyes, at 0.5 to 1.1 cycles a degree, cover almost the whole field and give the top-level value.

An entry is headed by the name as a spec writes it (`### name`). Groups: whole-picture settings (`params.<name>`), zone keys (`zones[i].<key>`), gaze keys (`gaze.<key>`), and the keys of the blocks (`spectrum`, `pace`, `motion`, `slow`, `tilt`, `magnet`, `remap`, `overlay`, `sound`, `haptic`).

## Whole-picture settings

### fov
The width of the animal's whole visual field, in degrees, added over all its eyes (a person is 180). Above 180 the picture is squeezed toward the middle and curved at the edges. Take it from the total field of both eyes together (the sum of the monocular fields, counting any overlap once), and never from one eye's own field or from the binocular overlap. Range 40 to 360.

### cpd
How sharp the whole picture is, in cycles per degree (a person's best is 60 in the engine, a normal eye reads about 30 on a chart). Larger is sharper. It blurs the picture everywhere that no zone says otherwise, so take it from the eyes that cover most of the field, at the acuity they have there. Take it from the typical or best acuity of the main eyes, never from a small specialised eye or a fovea (those go to `zones[i].cpd`). Never write a pixels-per-degree or a per-receptor figure here. Range 0.1 to 60.

### fovea
How much larger the middle of the picture is drawn than the edge, as a magnification (1 is a person; 2.2 for a hawk). It acts on the centre of the whole picture only. Take it from a measured ratio of receptor density or magnification between the fovea and the periphery of the main eyes. Range 1 to 4.

### topoA
How much sharper the picture is in the middle than at its edge, as a fraction (0 flat, 1 the edge is as blurred as the fall allows). It describes a round area centred in the picture, such as a fovea or area centralis, and works with `fall`. Take it from the ratio of peak to peripheral acuity or cell density of the main eyes. Range 0 to 1.

### topoS
The same as `topoA`, for a horizontal band across the picture (a visual streak, as in a rabbit or a horse), in place of a round middle. Use one of `topoA` and `topoS`. Range 0 to 1.

### fall
How steeply sharpness drops from the sharp middle to the edge, a pure number that multiplies the blur with the square of the distance from the middle (0 none, 2 strong). It matters only where `topoA` or `topoS` is above 0. It is almost always the app's choice. Range 0 to 4.

### pupil
The shape of the pupil, which shapes how out-of-focus points are blurred: `o` round, `v` upright slit, `h` horizontal bar, `none`. Take it from the pupil of the main eyes in daylight. Its value is one of those four words.

### dof
How strongly things that are far from the focused distance are blurred, from 0 (everything in focus) to 1. The distance is guessed from height in the picture. It is almost always the app's choice; a measured depth of field or accommodation range can inform it. Range 0 to 1.

### M
The name of the colour matrix (a key of `matrices`) applied to the whole picture, which turns the camera's red, green and blue (and the invented ultraviolet channel) into the colours the animal's receptors would pick. Its peaks come from the receptors of the eyes that cover most of the field. A region whose eyes have other pigments (the front eyes of a jumping spider, a dorsal retina) has its own matrix in `zones[i].M`.

### uvBlue
How much of the camera's blue is read as ultraviolet, a number from 0 to 1. Phone cameras record almost no ultraviolet, so this is a guess made from bluish and bright surfaces. Use it when records show the main eyes see ultraviolet; it is always the app's choice.

### sat
Colour saturation of the whole picture, 0 grey to 1 as a person sees. Take it from the number of cone classes of the main eyes: one class gives 0, two classes less than 1. Range 0 to 1.

### gain
A lift of the whole picture's brightness for dim light (1 is none). Take it from a measured sensitivity advantage of the main eyes over a person in dim light, and treat it as the app's choice. Range 0.5 to 4.

### noGreen
Removes the green channel from the whole picture (0 none, 1 all). For an eye that lacks a green receptor class. Range 0 to 1.

### sheen
A reflective glow of the eye shine (tapetum), 0 to 1. Use it only for eyes with a measured reflecting layer.

### gate
How much still things fade away from the whole picture, from 0 (everything shown) to 1 (only movement is shown). Use it only where records say the main eyes answer to movement alone. Range 0 to 1.

### field
1 draws no picture at all, only the amount, colour and direction of light. For a plant. Do not use it for an animal.

### persist
How long a moment lingers in the whole picture, as a trail, from 0 to 1. Take it from slow temporal resolution of the main eyes; usually the app's choice. Range 0 to 1.

### hold
For a walking bird's head: the number of frames the picture is held still between thrusts. Used with `thrust` for birds that bob the head.

### thrust
Milliseconds of the quick move after a hold, used with `hold`.

### rate
The pace of the picture against a person's: 1 is a person; below 1 the animal sees faster than a person, so the picture steps and lags behind the world. It is a person's flicker fusion (60 hertz) divided by the animal's flicker fusion frequency in the main eyes in bright light (0.3 for 200 hertz). A slower animal is left at 1. Range 0.2 to 1.

### glow
How brightly movement glows in the whole picture, 0 to 2. Used with `salience`. The app's choice; records say only whether the eyes respond to movement.

### living
Extra weight given to movement that looks alive, 0 to 4, in the whole picture. Used with `salience`. Take it from a record that the eyes in question pick out biological motion.

### glowC
The colour of the glow, three numbers from 0 to 1 for red, green and blue. The app's choice.

### salience
1 computes the map of where things move and lets a gaze or a glow use it. Needed for `gaze`, `glow` and `living`.

### ripple
Rings that run out across the picture at a knock or a sound, 0 to 1. The app's choice.

### shimmer
A faint shimmer where the animal sees no colour and a person does, 0 to 1. The app's choice.

### uvR
How much of the invented ultraviolet channel is added to the red of the picture, 0 to 1. For an eye with a receptor sensitive to both ultraviolet and red. A region with such an eye has its own `zones[i].uvR`. The app's choice.

### water
Four numbers, the red, green and blue strength of absorption by water and the depth scale, which tint distant parts of the picture the colour `waterC`. Use it only for an animal that looks through water, and only with records of the water's absorption.

### waterC
The colour of the water that the distance fades into, three numbers from 0 to 1.

### sweep
A scanning sweep of the whole picture as two numbers, degrees across and seconds for one cycle. Use `gaze.sweep` for an eye that scans on its own.

## Zone keys

A view has up to four zones. A zone is a region of the picture with its own eye. It states only what differs from the whole picture; every key it leaves out takes the whole picture's value.

### zones.id
A short name for the region, such as `front`, `gaze` or `fovea`, which other parts of the spec use.

### zones.shape
`whole`, `strip` (a rectangle), `ellipse`, `annulus`, `band` (level, across the field) or `cross` (two narrow fields, each bent in the middle, crossing like an X).

### zones.at
Where the centre is, as fractions of the camera's picture, `[x, y]`. The middle is `[0.5, 0.5]`.

### zones.deg
The size of the region as full width and height in degrees of the world, taking the long side of a phone picture as 64 degrees. Take it from the angular size of the field of that eye or retina (for a jumping spider's principal eye, about 2 by 21 degrees).

### zones.cpd
How sharp this region is, in cycles per degree, as for the whole picture. Take it from the acuity of the eye or retina that this zone stands for, and from no other eye. The front eyes of a jumping spider are a zone at 3.3 to 3.8 cycles a degree (12.5 for Portia); the side eyes belong to the whole picture.

### zones.M
The colour matrix of this region's eye, a key of `matrices`.

### zones.size
The size of the region as half its width and half its height, as fractions of the picture's long side. Use `zones.deg` when the region has a size in degrees.

### zones.inner
For an annulus, the inner edge as a fraction of its size.

### zones.rot
A turn of the region in degrees.

### zones.frac
The half width and half height of the region as fractions of the picture's own width and height, `[w, h]`, in place of `zones.size` or `zones.deg`.

### zones.sat
### zones.gain
### zones.gate
### zones.rate
### zones.sheen
The same settings as the whole picture's `sat`, `gain`, `gate`, `rate` and `sheen`, for this region only, taking the value from the eye that the region stands for.

### zones.soft
How softly the region's edge blends into the rest, as a fraction of the picture's long side. The app's choice.

### zones.mag
Magnification of what the region holds, about its centre. Take it from a measured magnification of that eye, otherwise the app's choice.

### zones.gaze
1 lets the gaze move this region, as the eyes of a jumping spider move.

### zones.tilt
For a cross, the tilt of its upper and lower arms from upright, in degrees.

### zones.gap
For a cross, half the gap between its halves, in degrees.

### zones.tip
For a cross, the weight kept at the tip of an arm, 0 to 1.

### zones.glow
How strongly movement glows in this region, 0 to 2.

### zones.living
Extra weight of living movement in this region, 0 to 4. Take it from a record that these eyes pick out biological motion.

### zones.uv
### zones.uvR
How much ultraviolet, and how much red, this region adds (0 to 1). Take it from the pigments of the eye this zone stands for.

## Gaze keys

For an eye that moves to look at things (the principal eyes of a jumping spider). Times are in milliseconds unless the entry says seconds.

### gaze.saccade
The time of a jump to a new target as `[base ms, ms per degree]`. Take it from a measured jump time and speed.

### gaze.sweep
The side-to-side scan across a target as `[degrees across, seconds a cycle]`.

### gaze.twist
Rotation of the scanning retinae as `[degrees each way, ms to turn, ms held at each end]`.

### gaze.examine
How long a target is looked over, as `[least ms, most ms]`.

### gaze.hold
How long the gaze stays after the target is gone, in ms.

### gaze.back
How fast the gaze drifts back to the middle afterward, in degrees a second.

### gaze.pursuit
The fastest smooth following of a moving target, in degrees a second.

### gaze.ior
How long a place just looked at is ignored, in ms (inhibition of return).

### gaze.iorDeg
The size of the ignored place, in degrees. The app's choice.

### gaze.any
### gaze.living
### gaze.habit
### gaze.surround
### gaze.distract
### gaze.floor
### gaze.wander
### gaze.sleep
### gaze.trackDeg
Weights and timings of what calls the gaze: how strongly any movement and living movement call it, how much a repeated movement at one place loses, how much a mover counts for less where movement fills its surroundings, how strongly a distraction must call while a target is examined, the least pull that still calls, the spontaneous scanning with nothing moving, the sleep-like twitching when the picture is dark and still, and how far a target may be followed. The records give the behaviour; the weights are the app's.

## Block keys

### spectrum.q
The name of the matrix that holds the animal's receptor classes, used for the colour wheel and the neutral band. Take its peaks from the same receptors as `params.M`.

### spectrum.neutral
The strength, 0 to 2, of a faint shimmer where the animal sees no colour but a person does. The app's choice.

### spectrum.dark
### spectrum.adaptAt
The name of a dark-adapted colour matrix (rods), and the two light levels (log10) between which the eye goes over to it. Take the matrix from rod pigment peaks.

### pace.ratio
How many times slower the replay plays a kept moment. The app's choice.

### motion.holdMs
### motion.maxDeg
### motion.thrust
### motion.thrustMs
For the head-stabilising reflex: how long the picture is held still against the turn of the phone, how far a turn is held, whether the picture moves only on a forward thrust, and for how long. Take them from records of head stabilisation; mostly the app's choice.

### slow.everyMs
### slow.windowS
### slow.stillS
### slow.developS
### slow.moveK
### slow.rightS
### slow.mix
The timings of the slow views (fungus, slime mould, long exposure): how often a frame is kept, the averaging window in seconds, how long the phone must lie still before the picture develops, how long it takes to develop, how much change counts as movement, the time for righting after a roll, and the mix with the live picture. All are the app's choice.

### tilt.fromDeg
### tilt.fullDeg
The camera elevation in degrees at which the view begins to turn into a disc seen through the water's surface, and at which it is complete (Snell's window, for animals that look up from under water).

### magnet.k
The strength of the magnetic drawing, 0 to 1. The app's choice.

### remap.blindAt
### remap.blindDeg
### remap.blindSoft
Where a blind wedge lies, in degrees from the way the phone faced when the view opened; how wide it is in degrees; and how softly its edge fades. Take them from the blind area behind the head or between the eyes; blindAt is measured from straight ahead.

### remap.fold
### remap.horizon
How strongly the sky is pressed toward the top of the picture, and the height of the horizon in the picture (0 bottom, 1 top).

### remap.band
### remap.fadeS
The height of the strip along the bottom that keeps what the phone faced, and how long its memory fades, in seconds.

### overlay.polar
### overlay.web
### overlay.shadow
The strength, 0 to 1, of the pattern of polarised light in the sky, of the drawn web that knocks ripple through, and of the dark ring where the light has fallen. The app's choice.

### sound.k
### sound.dark
### sound.flashS
### sound.holdS
### sound.steady
### sound.clickHz
### sound.say
How strongly sound lights the picture (k), how dark the picture rests, how long a flash of light lasts, how long a clap keeps the picture lit, how much steady sound lifts it, the rate of clicks sent through the speaker, and the plain words the app uses to ask for the microphone. Take bands of hearing from records of the animal's hearing; the weights are the app's choice.

### haptic.on
### haptic.pattern
### haptic.edge
What sets the vibration off (`onset` of a sound, a `knock`, a `shock` of darkening), the pattern in milliseconds, and the strength of the pulse of light drawn at the edge where the phone cannot vibrate.
