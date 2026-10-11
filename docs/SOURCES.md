# Sources

Every line the app shows about an animal's sight carries one of four grades: measured in this animal, measured in a relative or a wider group, a guess, or left out. This file lists what stands behind the measured lines, and names the conventions that are this project's own. The lines themselves are in `src/cam.a.js`; this file was last checked against build 8 (commit `8037aec`) on 11 October 2026.

## Measured, with the source

| Claim used in the app | Source |
|---|---|
| Sharpness across about 600 species: people about 60 cycles per degree, eagles about 140, most birds under 30, most insects under 1, dogs and cats four to seven times coarser than people | Caves, Brandley and Johnsen, *Trends in Ecology & Evolution*, 2018. [Duke University summary](https://today.duke.edu/2018/05/details-look-sharp-people-may-be-blurry-their-pets) |
| Cats: field about 200 degrees, sharpness 20/100 to 20/200, six to eight times the dim-light sensitivity, cones near 450 and 555 nm, very slow movement missed | Figures checked by veterinary eye specialists for Nickolay Lamm, 2013. [What Do Cats See?](https://nickolaylamm.com/art-for-clients/what-do-cats-see/) |
| Pupil shape and way of life in 214 species: vertical slits in ambush hunters, horizontal bars in grazing prey | Banks and colleagues, *Science Advances*, 2015. [Summary](https://www.sci.news/biology/science-pupils-shape-eyes-animals-03112.html) |
| Dogs: a visual streak in long-nosed dogs, a central area in short-nosed ones | McGreevy, Grassi and Harman, *Brain, Behavior and Evolution*. [Record](https://openpolar.no/Record/crskarger:10.1159%2F000073756) |
| Deer: cones at 450 to 460 and 537 nm in white-tailed deer; field about 310 degrees; a laterally set oval pupil | Jacobs and colleagues, 1994, and Heffelfinger, 2006, as gathered by [Wildlife Online](https://www.wildlifeonline.me.uk/animals/article/deer-overview-senses-vision) |
| Crocodiles: a horizontal streak of high acuity; three kinds of single cone | Nagloo and colleagues, 2016. [Science News](https://www.sciencenews.org/blog/wild-things/crocodile-eyes-are-optimized-lurking). Alligators were not in that study. |
| Flicker fusion: cane toad 6.7 Hz, ground squirrel 108, pigeon 143, honeybee 200, one beetle 400, people about 60 | Inger and colleagues, *PLoS ONE*, 2014. [The paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0098631) |
| Raptors: peregrine 129 Hz, saker 102, Harris's hawk 77 | Potier and Kelber, 2019. [Lund University](https://www.lunduniversity.lu.se/article/falcons-see-prey-speed-formula-1-car) |
| Head-bobbing: a hold and a thrust; thrust 100 to 150 ms; present in pigeons, chickens, cranes, herons and egrets; absent in ducks, cormorants and raptors | Necker, 2007. [The review](https://www.reinhold-necker.de/Head%20bobbing%20print.pdf) |
| Frogs do not register stationary detail | Lettvin, Maturana, McCulloch and Pitts, 1959. [Lecture notes](https://www.cns.nyu.edu/~david/courses/perception/lecturenotes/brain/lettvin.html) |
| Ground squirrels: two cone types near 437 and 518 nm | Jacobs, Neitz and Crognale, 1985. [The paper](https://link.springer.com/article/10.1007/BF00613974) |
| Bees: ultraviolet, blue and green receptors; none for far red | [DLR Insect Vision](https://insectvision.dlr.de/flying-insects/bee-photoreceptor-model) |
| Ultraviolet cannot be recorded by an ordinary camera | Vasas and colleagues, 2024. [University of Sussex](https://www.sussex.ac.uk/news/article/63262-new-video-camera-system-captures-the-coloured-world-that-animals-see) |
| Plants read red against far-red light and detect neighbours before being shaded | Fraser, Hayes and Franklin, 2016. [The review](https://research-information.bris.ac.uk/ws/files/71767370/COPLBI_D_16_00008_2_.pdf) |

## What the page claims for each kind of eye, and what backs it

The table gives each line of `src/cam.a.js` graded as measured (m) or as measured in a relative or a wider group (g), with the row above that backs it. Lines graded as a guess or as left out are named under the last column.

| Kind | Measured lines, and their source | Guesses and lines left out |
|---|---|---|
| `cat` | Sharpness, a fifth to a tenth of yours (m), colour (m), field (m) and dim light (m): the 2013 cat figures in the second row. Pupil, a vertical slit (m): Banks and colleagues, 2015 | Where it is sharp, depth; slow movement is left out |
| `dog` | Sharpness, a quarter to a seventh of yours (m): Caves and colleagues, 2018. Where it is sharp (m): McGreevy and colleagues | Colour, field, dim light, depth |
| `squirrel` | Colour (g): Jacobs, Neitz and Crognale, 1985. Pace, 108 a second (g): Inger and colleagues, 2014 | Field, sharpness |
| `deer` | Colour, near 455 and 537 nm (m), and field (m): Wildlife Online. Pupil, a horizontal bar (g): Banks and colleagues, 2015, and Wildlife Online | Sharpness, dim light, depth |
| `rabbit` | none | All of it |
| `hawk` | Sharpness, an eagle's 140 (g): Caves and colleagues, 2018. Pace, peregrine 129 and Harris's hawk 77 (m): Potier and Kelber, 2019 | Field; the gait is left out, after Necker, 2007 |
| `wader` | Gaze, the held head (m), and tempo, the thrust (g): Necker, 2007. Sharpness, under 30 (g): Caves and colleagues, 2018 | The length of the hold, ultraviolet, field |
| `bird` | Pace (g): Inger and colleagues, 2014, and Potier and Kelber, 2019. Sharpness, under 30 (g): Caves and colleagues, 2018 | Ultraviolet, field |
| `alligator` | Where it is sharp (g) and colour (g): Nagloo and colleagues, 2016. Pupil, a vertical slit (g): no row above names crocodilians | Field, sharpness, dim light, depth |
| `reptile` | none | All of it |
| `frog` | Movement (m): Lettvin and colleagues, 1959. Pace, under 7 a second (g): Inger and colleagues, 2014 | Field, sharpness, pupil |
| `bee` | Sharpness, under 1 (g): Caves and colleagues, 2018. Red (m): DLR Insect Vision. Pace, 200 a second (m): Inger and colleagues, 2014 | Ultraviolet; the false colour is a way of drawing |
| `insect` | Sharpness, under 1 (g): Caves and colleagues, 2018. Pace, one beetle to 400 (g): Inger and colleagues, 2014 | Ultraviolet |
| `plant` | Neighbours (m): Fraser, Hayes and Franklin, 2016. No picture (g): no row above | Green and time |
| `other` | none | No account yet |
| `person` | Same eyes (m): the viewer's own, and no source is needed | none |

### Words in the page that no row above backs yet

A check of `src/cam.a.js` against the table on 11 October found these. Each needs a source or a change of words.

- Deer: the page says that the horizontal pupil "cuts glare from above".
- Alligator: the page grades the vertical slit pupil as measured in a relative.
- Other birds: the page says "Birds follow flicker at 40 to 140 a second, the faster movers higher". The rows above give a pigeon's 143 and the raptors' 77 to 129, and nothing for 40.
- Insects: the page says "Flies and dragonflies follow flicker past 100 a second".
- Bees: the page gives the honeybee's 200 a second "in bright light", a condition the row above does not state.
- Hawks: the page says "against your 50 to 60", where the other lines about pace say that you stop near 60.
- Plants: the page grades "A plant has nothing to focus light" as measured in a wider group.

## Entered from memory, still unchecked

These were entered from memory and have not been checked against a source:

- The two-cone colour arithmetic (Viénot, Brettel and Mollon, 1999).
- Two cone types in dogs.
- The rabbit's field, streak and cones.
- A central sharp spot in cats.
- Ultraviolet vision in lizards and turtles.

## Which kind of eye a species takes

A recognized species takes its kind of eye from its taxonomy, by the rules in `docs/CONTRACTS.md`, which `tools/species/eyes.py` carries out and `tools/species/test_eyes.py` tests. A name the person types is matched by the word table in `src/cam.r.js`.

- **New World vultures take the generic bird eyes.** The `hawk` eyes draw sight sharper than a person's, and that is not established for vultures, so vultures (family Cathartidae, order Cathartiformes) go to `bird`. The decision was made on 10 October (`docs/LOG.md`, 20:35). `tools/species/eyes.py` applies it before the `hawk` rule, because the GBIF backbone may file Cathartidae under Accipitriformes, and the word table sends "vulture" and "condor" to `bird`.

## Conventions that are this project's own

- **Sharpness is drawn against the viewer's eye.** The screen's long side is assumed to fill 24 degrees of view on a phone (a coarse pointer) and 34 degrees on a computer (`VIEW_DEG` in `src/cam.a.js`), and the picture is blurred to what the animal's eye would keep of that screen. Drawn against the scene, a cat's blur would be about one pixel, because a phone picture of a 70 degree field already discards most of what a human eye resolves.
- **A faster eye is suggested by slowing the picture,** then jumping to catch up. For squirrels and bees the picture runs at 60 divided by the measured flicker rate (0.56 and 0.3). For hawks, other birds and insects the factors in the code (0.6, 0.5 and 0.45) equal none of the measured rates in the table above, and the page says only that the picture is slowed to suggest the faster eye. A higher flicker rate does not establish that time feels slower.
- **Only what moves is drawn for a frog,** and the cane toad's slow flicker is drawn as trails.
- **Depth is guessed from height in the frame**, and a tap moves the focus. A camera feed carries no distances.
- **The wide field is shown by shrinking the camera's picture** and inventing the rest from mirrored, blurred edges.
- **Ultraviolet is invented**: violet for birds, reptiles and insects other than bees, and blue for bees. Bees are drawn in false colour.
- **A plant's view removes green and averages away anything quick.** The page says that both choices are invented.
- **Something else is shown as light and dark only,** because nothing sourced says how it meets light.
- **The hexagon mosaic appears only during the change of eyes.** An insect does not see hexagons.
- **The length of a wading bird's hold is a guess.** The thrust length is from pigeons.
