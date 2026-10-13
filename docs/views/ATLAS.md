# Atlas of sensing mechanisms

Written 13 October 2026 by the design agent (branch `agent/design`) from the ten checked sheets in `docs/views/sheets/`, the jumping spider draft `docs/views/drafts/jumper.md`, and the drafts on `research/birds`, `research/cat-dog` and `research/ground-invertebrates` (cited as the birds, cat-dog and ground-invertebrates drafts). `docs/ENGINE-DESIGN.md` turns this atlas into engine modules.

## How to read an entry

- **Mechanism** says what the animal does, in plain words.
- **Evidence** names the sheet or draft and the source it cites. Nothing here adds a new source; where a statement rests on general knowledge with no sheet behind it, the entry says so.
- **Who has it** gives each view's share of all world records, counted as iNaturalist research-grade records in GBIF read on 11 October 2026 (169,720,759 in all; `docs/VIEWS.md` for the fourteen existing views, `docs/COVERAGE.md` for the nineteen new groups). The weight at the end of the line is the sum of shares of the views that would use the mechanism. Shares for proposed sub-views (owl, duck, woodlouse, millipede) come from the drafts and are rough. Bird is counted at 18.2% (the `bird` view's 30.9 million records in `docs/VIEWS.md`); owls are about 0.22% of all records and ducks about 2.1% (birds draft).
- **Phone in, phone out** lists what the phone can sense in place of the animal and what it can give back. The web build can read the camera, the microphone (after a tap and a plain-words request), motion and orientation (after a tap on iOS), the compass heading, the clock and the time zone, the touch screen, and the camera's exposure where `getSettings()` reports it. It can write the screen and the speaker, and the vibration motor only where `navigator.vibrate` exists (Android browsers; iOS Safari has none). A native build adds depth on LiDAR phones and finer haptics.
- **Ways to draw it** gives two or three ways that differ in kind: a continuous frame, a sequence of held moments, something felt through the hand or done with the body, or a change in what the view is. Each has a cost on a phone (low, medium or high, in graphics time and build effort together). The option marked **reframe** changes what the view is. The owner picks one per mechanism, or none.
- **Invented** marks what the app would make up. Every option in this atlas is the app's own drawing; the mark names the parts that no source fixes.

## The mechanisms, by weight

| # | Mechanism | Weight (share of world records) |
|---:|---|---:|
| 1 | Sharpness and where it is sharp | about 58% |
| 8 | Flicker and pace | about 50% |
| 5 | More colour classes, and ultraviolet | about 46% |
| 13 | Light sensed with no image | about 42% |
| 2 | Field shape and blind areas | about 40% |
| 11 | Head stabilization and bobbing | about 19% |
| 21 | Magnetic fields | about 16%, nearly all as a left-out or invented row |
| 4 | Fewer colour classes | about 7% |
| 9 | Sight that registers only motion | about 3.1% |
| 7 | Dim light and photon noise | about 3.0% |
| 16 | Airflow and water flow | about 3.8% |
| 24 | Gravity and growth time | about 2.9% |
| 14 | Shadows and looming | about 2.5% |
| 10 | A gaze that jumps between targets | about 2.2% |
| 3 | Pupils, focus and depth | about 2.8% |
| 17 | Hearing and sound localization | about 2.1% |
| 25 | Clocks: day, night and moon | about 2.0% |
| 15 | Substrate and web vibration | about 1.9% |
| 22 | Chemistry: smell, taste, breath | about 2% as rows; nothing drawable measured |
| 23 | Touch | about 1.4% |
| 12 | Several eyes aimed several ways | about 0.9% |
| 6 | Polarization | about 0.8% from the sheets; much more if insects are added |
| 18 | Echolocation | about 0.2% with whales; 0.05% for bats alone |
| 20 | Electric fields | about 0.1% |
| 19 | Heat | about 0.05% |

The weights overlap, since one view uses many mechanisms.

---

## 1. Sharpness and where it is sharp

**Mechanism.** Every eye resolves detail down to some limit, and most are sharper in one region: a central spot, a horizontal streak, an upright strip, two spots to the sides, or a patch off centre. Some eyes also lose faint contrast before they lose fine detail.

**Evidence.** Spot, streak and fall-off already drive `cpd`, `topoA`, `topoS` and `fall` in `src/cam.a.js`. New shapes: an upright strip in jumping spider principal eyes (`spider.md` section 4, item 3; `jumper.md`); two streaks just above and below the horizon in fiddler and ghost crabs, and vertical detail five times finer than horizontal (`crab.md` section 4, after Bagheri and colleagues 2020); a sharp area in the upper retina, looking down, in Daubenton's bat (`bat.md`, Cechetto and colleagues 2020; the direction is the sheet's inference); foveae at plus and minus 75 degrees and a lower-centre patch in pigeons, two side spots in songbirds and four in swallows (birds draft, Kano and colleagues 2022; Tyrrell and Fernández-Juricic 2017); a deep and a shallow fovea in hawks (birds draft). Contrast: a Bluegill needs about 3% contrast at its best spatial frequency (`fish.md` section 4, Northmore and colleagues 2007).

**Who has it.** Every view with an image: insect 21.6%, bird 18.2%, reptile and alligator 2.8%, bee 2.7%, fish 1.6%, hawk 1.5%, spider 1.3%, snail 1.2%, frog 1.2%, wader 1.1%, the mammals with views about 1.9%, crab 0.7%, mammal 0.6%, jumper 0.4%, and the rest. Weight about 58%.

**Phone in, phone out.** The camera; the screen. The touch screen can steer.

**Ways to draw it.**
- **A painted map** (continuous frame; low). One small texture holds the blur for every point of the screen, so any shape is possible: the strip, the two streaks, the hawk's two foveae, the pigeon's side spots. The picture looks like today's views with the sharpness in the right places.
- **Loupes** (held insets; medium). Each sharp region is lifted out as a small magnified window floating at its place in the coarse field, the way a jeweller's loupe sits on a page. A hawk has two loupes, one strong and one weak; a pigeon has two at the far sides and one low in the middle. The person sees at a glance how many places the animal looks closely at once.
- **The thumb as fovea** (reframe; low). The whole screen is coarse. Wherever the person's thumb rests, a sharp area opens in the animal's own shape (a tall thin strip for the jumping spider, a long slit for the deer, a dot for the cat), and when the thumb lifts it drifts back to where the animal's sharp area sits. The person's hand does the work of the eye's muscles, which makes the size and shape of the sharp area felt as well as seen.

**Invented.** The sharpness of each patch where the sheets give only its place; the strength of the loupes' magnification; the drift back.

## 2. Field shape and blind areas

**Mechanism.** Eyes on the sides of the head see almost all the way round, with a blind wedge behind or above. Under water, the whole sky above is squeezed into a circle about 97 degrees across (Snell's window). A dabbling duck sees over its own crown.

**Evidence.** `fov` in `src/cam.a.js` already squeezes the frame. Snell's window: `fish.md` section 4, item 1. The duck's binocular strip running 210 to 220 degrees over the crown and the sky overhead: birds draft (Guillemain and colleagues 2002; Cantlay and colleagues 2023). The blind area above a ground predator's head, drawn as a top shade: birds draft for `hawk` (Potier and colleagues 2018). A person's field of 200 degrees: cat-dog draft section 3.3.

**Who has it.** Every view with `fov` above 180: insect, bird, bee, reptile, fish, frog, wader, squirrel, deer, rabbit, crab, jumper and more. Weight about 40% after leaving out views that keep the camera's field. Snell's window alone: fish 1.6%, shark 0.08%, whale 0.16%.

**Phone in, phone out.** The camera; the gyroscope and compass for where the phone points; tilt for looking up; the screen.

**Ways to draw it.**
- **The squeeze, with a blind wedge** (continuous frame; low). Today's barrel squeeze, with the blind area drawn as a soft dark wedge at the right edge of the frame: behind for a rabbit, above for a hawk, below the bill for a duck.
- **The panorama ribbon** (held moments; medium to high). The screen shows the animal's whole field as one long ribbon. The live camera is a bright window inside it, and the rest is filled from frames the phone gathered as the person turned, placed by the gyroscope, fading as they age. The person sees how much of the circle the animal holds at once, and how little of it a phone sees.
- **Looking up from under water** (reframe; medium). When the phone tilts toward the sky in the fish view, the scene above collapses into a bright disc in a dark, mirror-like surround, as Snell's window does; level the phone and the disc slides to the top of the frame. For the duck the same tilt folds the sky into the top of the frame without losing the forward view. The view becomes a place to look up from.

**Invented.** The panorama's fade; what fills the ring outside Snell's window (`fish.md` says no source gives it); the width of every blind wedge.

## 3. Pupils, focus and depth

**Mechanism.** Slit pupils smear out-of-focus things along the slit and close further in bright light; bar pupils do the same sideways. Some eyes measure distance from blur (the jumping spider's layered retina), some cannot focus close (a cat below about 25 cm), and tongue-shooters keep one distance sharp.

**Evidence.** `pupil`, `dof` and the depth guess already exist in `src/cam.a.js` and `src/cam.b.js`. A pupil that answers to light and a numeric aspect per genus (lynx, gray fox): cat-dog draft, sections 2.1 and 2.5. The near point: cat-dog draft (25 cm for cats, 33 to 50 cm for dogs, secondary sources). Depth from defocus: `spider.md` section 4, item 5 (Nagata and colleagues 2012). The tongue's reach: `salamander.md` section 4.

**Who has it.** Cat 0.10%, deer 0.59%, reptile and alligator 2.8% (alligator a small part), frog 1.2% (bar pupil, invented), dog 0.17%, salamander 0.37%, jumper 0.40%. Weight about 2.8% with the frog's guessed bar pupil, about 1.6% without it.

**Phone in, phone out.** The camera; the camera's exposure and `focusDistance` where reported; a depth model or LiDAR in a native build; the screen.

**Ways to draw it.**
- **Blur that breathes with the light** (continuous frame; low). The out-of-focus smear stretches into tall thin streaks in bright light and evens out in the dark, as the cat-dog draft proposes. Bright points out of focus turn into short upright lines for a cat and short level bars for a deer, like the highlights in a film shot through an anamorphic lens.
- **The pupil as the frame** (reframe; low). The visible picture itself closes into a vertical slit of screen in bright light (cat, fox, alligator) or a horizontal letterbox (deer), and opens toward a full circle as the room darkens. The person looks out through the animal's pupil at the scale of the whole screen. The engine's aperture mask (`u_ap`, `u_shape`) already draws these shapes.
- **The strike distance** (held moments; low). One depth band is sharp and everything nearer and farther is soft; when the camera's focus distance enters the band, the picture snaps and holds for a beat, as a salamander strikes. For a cat the same machinery softens everything nearer than 25 cm, so bringing the phone to a cat's nose blurs the view.

**Invented.** The aspect of the streaks where no genus is measured; the strike band's distance; the depth guess from height in the frame.

## 4. Fewer colour classes

**Mechanism.** Two kinds of cone (most mammals, fiddler crabs, bass), one kind (sharks, raccoons, many snails and slugs), or one with a shift between day and night (the land snail's peak moves from about 496 nm in the dark to about 420 in light).

**Evidence.** `M` matrices in `src/cam.a.js` (`DEUTAN`, `PROTAN`, entered from memory, a point the cat-dog draft section 6 and `spider.md` both raise). Bass: `fish.md` (Mitchem and colleagues 2019). Crabs: `crab.md`. Raccoon and mammal split: `mammal.md`. Snail and the day-night shift: ground-invertebrates draft, section 2.1 (the new field `adaptM`). The dog's neutral point near 480 nm: cat-dog draft section 3.4.

**Who has it.** Squirrel 0.83%, deer 0.59%, rabbit 0.20%, dog 0.17%, cat 0.10%, fish 1.6%, snail 1.2%, crab 0.73%, mammal 0.60%, jumper 0.40% (ultraviolet and green), salamander unknown, shark 0.08%, starfish, tick, flying fox. Weight about 7%.

**Phone in, phone out.** The camera; the screen; the vibration motor on Android.

**Ways to draw it.**
- **The matrix** (continuous frame; low). Today's method, with matrices rebuilt from each animal's measured pigments and a slow drift for eyes that adapt (`adaptM`).
- **The neutral band** (continuous frame; medium). Every pixel the animal would see as colourless shimmers faintly, like heat haze: for a dog, the blue-greens near 480 nm; for a bass, the colours along its confusion line. The person sees exactly where colour disappears for the animal, laid over the colours they still see.
- **Same or different, by touch** (reframe; low). The person taps two things on the screen. The phone answers with one pulse if the animal would see them as the same colour and two if it would see them as different (with a small mark on screen where vibration is missing). The view becomes a sorting game played with the hand: the red ball and the green lawn give one pulse for a dog.

**Invented.** Every matrix entered from memory until rebuilt from pigment curves; the shimmer's look; the threshold for "same".

## 5. More colour classes, and ultraviolet

**Mechanism.** Four or more cone classes (most birds), cones reaching into ultraviolet (most birds, bees, many insects, lizards, jumping spiders, fiddler crabs), and the mantis shrimp's twelve.

**Evidence.** The invented ultraviolet channel and `sheen` and `uvBlue` in `src/cam.b.js`. Birds: ultraviolet against violet-sensitive families, 58 to 62% of `bird` records ultraviolet-sensitive (birds draft, Ödeen and Håstad 2003, 2013). Jumping spider receptors near 370 and 532 nm (`spider.md`, De Voe 1975), red in *Habronattus* (`jumper.md`). Fiddler crab ultraviolet claws; mantis shrimp (`crab.md`, Thoen and colleagues 2014). A phone lens passed 1.1% of ultraviolet A at 340 nm and 18.9% at 390 nm, and the sensor responds weakly (`crab.md`, Igoe, Parisi and Carter 2012), so the camera records a trace that mixes into its blue.

**Who has it.** Insect 21.6%, bird about 16% (owls and ducks out), bee 2.7%, reptile 2.8%, hawk 1.5%, wader 1.1%, crab 0.73%, jumper 0.40%. Weight about 46%.

**Phone in, phone out.** The camera's blue channel and its trace of ultraviolet A; the screen; the vibration motor on Android.

**Ways to draw it.**
- **The shifted spectrum** (continuous frame; low). Today's bee method made general: each class of the animal is mapped onto one of the screen's three, and the invented ultraviolet channel takes the bluest slot. Stable and readable.
- **Turning the colour wheel by hand** (held moments; medium). A tetrachromat's four channels (ultraviolet, blue, green, red) cannot all reach a three-colour screen. Dragging a finger across the picture rotates which three of the four are shown, so the person scrubs through the bird's colour space three channels at a time and watches a plain flower split into rings.
- **A colour felt in the palm** (reframe; low on Android, none on iOS). The screen keeps the person's own colours. Wherever the invented ultraviolet channel is strong, a soft buzz runs under the thumb as it slides across the picture, so the person feels an extra colour the screen has no way to show. On iOS the same places glow with a fine moving grain, a texture with no hue.

**Invented.** The ultraviolet channel itself (built from the blue channel and surface cues); every mapping of four or more classes to three; the buzz.

## 6. Polarization

**Mechanism.** Some eyes read the angle of polarized light: from the sky's pattern for direction, and from glare off water and mud for contrast.

**Evidence.** Fiddler crabs use polarization contrast on mud and water (`crab.md`, How and colleagues 2012, 2015). Night-migrating songbirds use skylight polarization for direction, with conflicting evidence for vision (birds draft, Cochran and colleagues 2004; Able 1989; Hart 2001; drawn there as an `x` row). Bees, ants and cephalopods use it too; no sheet in this repository yet covers them, so that is general knowledge with no sheet behind it.

**Who has it.** Crab 0.73% and songbirds as a left-out row in the sheets. Weight about 0.8% from the sheets; it would rise past 20% if the bee and insect sheets confirm it.

**Phone in, phone out.** A web page cannot measure polarization. The clock, the time zone, the compass and the tilt together give the sun's position, and the sky's polarization pattern follows from the sun's position by the standard single-scattering model (general physics; no sheet). The screen.

**Ways to draw it.**
- **The computed sky** (continuous frame; medium). When the phone points at the sky, a bright band arcs across it 90 degrees from the sun, where polarization is strongest, combed with fine lines along the angle of the light. The pattern is computed from the clock and compass, and it lines up with the real sky.
- **Turn the phone like a filter** (reframe; low). The person rotates the phone about the camera's axis as if it were a polarizing filter, and the band brightens and darkens with the angle (by the square of the cosine). The view becomes an instrument turned in the hand, and the sky answers.
- **Glare struck from water** (continuous frame; medium). For the crab, bright flat highlights low in the frame (wet mud, puddles) are redrawn as a striped texture with high contrast, standing for the horizontally polarized glare a crab reads.

**Invented.** The glare detection; the look of the band and lines; the assumption of a clear sky. The sky pattern is physics and the place is a guess from the time zone.

## 7. Dim light and photon noise

**Mechanism.** Night eyes gain sensitivity by pooling light over space and time, with a reflecting layer (the tapetum) behind the retina in many; detail falls and grain rises as light fades, and colour drains as rods take over.

**Evidence.** `gain` in `src/cam.a.js`. Dogs fall from about 9 cycles per degree in room light to about 2.6 near moonlight while people fall from 32 to 44 to 6 to 10, a ratio near a third throughout (cat-dog draft section 2.3, effect 3). Cat threshold about seven times lower than a person's; tapetum up to 15 layers; eyeshine as a bloom (cat-dog draft section 2.1). Owls near the vertebrate limit, the barn owl sharpest at twilight (birds draft, Martin 1986; Orlowski and colleagues 2012). Scorpion eyes a thousand times more sensitive at night (ground-invertebrates draft section 2.5). Crab, crayfish and horseshoe crab eyes at night (`crab.md`).

**Who has it.** Cat 0.10%, dog 0.17%, deer 0.59%, alligator, owl 0.22%, crab 0.73%, mammal 0.60%, scorpion 0.14%, bat 0.04%, flying fox 0.01%, frog 1.2% (night pooling, from general knowledge). Weight about 3% without the frog.

**Phone in, phone out.** The camera's brightness and, where reported, its exposure time and ISO; the clock; the screen.

**Ways to draw it.**
- **Grain and lift** (continuous frame; low). Shadows lift, sharpness falls with the logarithm of the light as the dog measurements say, colour drains, and a fine living grain rises in the dark like film pushed three stops. A bloom around bright points stands for eyeshine.
- **The long exposure** (held moments; low). In the dark the view pools light over time: still things sharpen as seconds pass and moving things leave ghosts, as a long photograph does. The person learns that a night eye trades time for light.
- **Two eyes racing the dark** (reframe; low). The compare slider ties itself to the room's light: as the person dims a lamp or walks into a dark room, their own half of the screen drowns in noise and black while the animal's half holds. The view becomes a contest with a winner.

**Invented.** The grain's size; the bloom's strength (the cat-dog draft names Land and Nilsson's chapter 6 as the source still wanted); the pooling time.

## 8. Flicker and pace

**Mechanism.** Eyes differ in how fast they follow change: a bee to about 200 flashes a second, a peregrine to 129, a person to 50 to 100, a cane toad to about 7, a spider's eye to 4 to 9. Fast eyes see a slowed world; slow eyes see smears.

**Evidence.** `rate` and `persist` in `src/cam.a.js`. Birds: 75 to 146 by family (birds draft, Boström and colleagues 2016; Potier and colleagues 2020). Crab 73.6 (`crab.md`). Shark 26.1 (`fish.md`). Spider 4.3 to 8.6 (`spider.md`, Fenk and Schmid 2011). Starfish 1 to 2 (`sealife.md`). Jumping spider about 40, to be confirmed (`jumper.md`).

**Who has it.** Insect 21.6%, bird 18.2%, bee 2.7%, hawk 1.5%, spider 1.3%, frog 1.2%, wader 1.1%, squirrel 0.83%, crab 0.73%, starfish about 0.24%, dog 0.17%, shark 0.08%. Weight about 50%.

**Phone in, phone out.** The camera at 30 to 60 frames a second in a browser (more in a native build); the screen.

**Ways to draw it.**
- **Slow, then catch up** (continuous frame; low). Today's method: the picture lags and jumps ahead, and slow eyes smear.
- **The replayed second** (held moments; medium). A tap keeps the last second of video and replays it stretched by the animal's ratio (three times slower for a bee), then returns to live. The person sees a single wingbeat or a ball's flight the way the faster eye has time for it.
- **The kitchen strobes** (reframe; medium). Mains lighting flickers 100 or 120 times a second, which people see as steady; a phone at short exposures records it as rolling bands. For fast eyes the view finds those bands and turns them into a visible strobe across lamps and screens, so the fly's kitchen is a disco. For slow eyes the bands vanish and a waved hand becomes a fan. The view shows the person their own room's hidden flicker.

**Invented.** The strength of the strobe; the replay's length; the mapping from flicker fusion to the lag.

## 9. Sight that registers only motion

**Mechanism.** Some eyes, or some parts of an eye, report change and ignore what stays still: a frog's prey detectors, a web spider's eyes, a jumping spider's side eyes, a dog's blindness to very slow movement.

**Evidence.** `gate` in `src/cam.a.js` (frog, Ewert as cited there). Web spiders register little beyond changes of light and dark (`spider.md`). The side eyes of jumping spiders, and living motion picked out by the front side eyes (`jumper.md`, De Agrò and colleagues 2024). Dogs miss movement slower than about 0.8 degrees a second (cat-dog draft section 2.3, effect 2).

**Who has it.** Frog 1.2%, spider 1.3%, jumper 0.40% (the surround), dog 0.17%. Weight about 3.1%.

**Phone in, phone out.** The camera and the frame ring; the gyroscope to remove the phone's own movement; the screen.

**Ways to draw it.**
- **The dark pond** (continuous frame; low). Today's gate: still things fade to black and moving things glow with trails, with the phone's own motion removed by the gyroscope so the person need not hold perfectly still.
- **Ink of movement** (held moments; medium). The still world is a blank white page; every movement leaves a stroke of ink, and the strokes build over a minute into a drawing of everything that moved, like a long-exposure of only the moving parts. The person can leave the phone propped and come back to a picture of the garden's traffic.
- **The freeze and the step** (reframe; medium). For the dog, everything moving slower than the threshold holds still on an earlier frame and then jumps into place, so a distant walker freezes and steps while a thrown ball moves smoothly. The person learns that stillness for this animal is a speed, and a slow cat is invisible.

**Invented.** The trail decay; the ink's look; the frog's threshold.

## 10. A gaze that jumps between targets

**Mechanism.** A narrow sharp region moves to whatever the wider field flags, holds, scans, and leaves; some animals also ignore a place they have just inspected for a while.

**Evidence.** Jumping spiders: six eyes flag motion and the two principal eyes are turned to it (De Agrò, Rößler and Shamble 2024); after the principal eyes take a target the side eyes ignore that place for about five seconds (Ferrante and colleagues 2024); the retinas scan (`jumper.md`; `docs/tracks/engine.md`). A goshawk pursues with its fovea at a fixed angle to the target (birds draft, Kane and colleagues 2015). Owls barely move their eyes and turn the head up to about 270 degrees (birds draft, Potier and colleagues 2023).

**Who has it.** Jumper 0.40%, hawk 1.5%, owl 0.22%. Weight about 2.2%.

**Phone in, phone out.** The camera's motion map; the gyroscope; the front camera; the screen; the vibration motor on Android.

**Ways to draw it.**
- **The hunting strip** (continuous frame; medium). As `jumper.md` proposes: a narrow upright strip, sharp and coloured, jumps to the strongest glow in the coarse surround, scans it with small sweeps, and holds while that place fades from the surround's attention for five seconds.
- **Stamps of attention** (held moments; medium). Each fixation leaves a sharp thumbnail fixed where it was taken, laid over the coarse field like a stamp, and each fades over five seconds as the side eyes allow that place back. The screen becomes a record of what drew the eye in the last few seconds, and the person sees the spider's Times Square as a scatter of crisp pieces.
- **Being looked at** (reframe; low beyond the hunting strip). The view switches to the front camera. The person's own face and hands are the moving things, and the spider's strip finds them, holds on them, and loses interest for five seconds. The view turns the app's question round: the person is the one seen.

**Invented.** The scanning sweep's size and speed; the salience rule's weights; the use of the front camera.

## 11. Head stabilization and bobbing

**Mechanism.** Many birds hold the head still in the world while the body moves, then thrust it forward; a hovering kestrel locks its eyes over the ground; a ghost crab keeps its streak on the horizon as the ground tilts.

**Evidence.** `hold` and `thrust` in `src/cam.a.js` (Necker 2007 for 100 to 150 ms thrusts, birds draft). Bobbing only at slow long strides (birds draft, `wader`). A perched hawk holds up to about two seconds (Tucker 2000); a kestrel holds its eyes over the ground (Videler and colleagues 1983); songbird head jumps with holds of about 90 ms (Eckmeier and colleagues 2008), all in the birds draft. The crab's level band (`crab.md`, Zeil 1990). Ducks do not bob (birds draft).

**Who has it.** Bird about 16% (ducks out), hawk 1.5%, wader 1.1%, owl 0.22%, crab 0.73% for the level band. Weight about 19%.

**Phone in, phone out.** The gyroscope and accelerometer; the step detector the app already has; the screen; the vibration motor on Android.

**Ways to draw it.**
- **The locked world** (continuous frame; medium). Between jumps the picture is held still in the world against the phone's rotation and small shifts, then snaps to catch up. Held over a lawn, the picture locks like a kestrel's while the hand trembles.
- **Held frames** (held moments; low). Today's method: the frame freezes for the hold and smears through the thrust, driven by walking.
- **The arm as the neck** (reframe; low). The picture updates only when the person jerks the phone forward, as a pigeon thrusts; between thrusts it holds, and on Android each thrust lands with a short pulse. The person plays the bird's head with their arm, and learns its rhythm by doing it.

**Invented.** The lock's strength against sensor drift; the hold lengths where no duration was found (wader); the pulse.

## 12. Several eyes aimed several ways

**Mechanism.** Some animals carry separate eyes or eye groups that look in different directions or do different tasks: a tick's two eyes up and out, a harvestman's two sideways fields from one turret, a scorpion's median and lateral eyes, a starfish's five arm-tip eyes, a scallop's or giant clam's row of small eyes.

**Evidence.** Tick: two windows 39 degrees out and 33 up, each about 43 by 49 degrees (`tick.md`; ground-invertebrates draft section 2.7). Harvestman: two side windows with a dim seam (ground-invertebrates draft section 2.6). Scorpion: median zone sharper than lateral zones, the lateral eyes ten times more sensitive at night (ground-invertebrates draft section 2.5). Starfish: five windows 100 by 30 degrees (`sealife.md`). Scallop and clam: many small windows that light when something dark moves through (`sealife.md`). Horseshoe crab: two windows sideways (`crab.md`).

**Who has it.** Starfish about 0.24%, scorpion and harvestman 0.14%, tick 0.04%, jumper 0.40% (as eye tasks), clams within sealife, horseshoe crab 0.01%. Weight about 0.9%.

**Phone in, phone out.** The camera; the gyroscope; the screen.

**Ways to draw it.**
- **Windows on one frame** (continuous frame; low). The aperture mask grows shapes with several openings: two soft windows up and out for the tick, two sideways with a dim seam for the harvestman, each with its own blur and gain.
- **A row of lamps** (held moments; medium). For the scallop, the screen is a dark band with a row of small round lamps along its lower edge. Each lamp holds the average of its tile of the camera and flares when something dark crosses it. The person sees the clam's world as a string of lights that blink at passing shadows.
- **Turning to fill the ring** (reframe; medium to high). For the starfish, the screen shows a ring of five windows. Only the one facing where the camera points is live; the person turns slowly on the spot and each window fills as it passes, then holds. The person's body becomes the starfish, one arm at a time.

**Invented.** Everything outside the camera's own field; the dim seam's depth; the lamp count, which should follow the measured eye count where known.
