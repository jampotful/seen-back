# Sensing sheet: snail, slug and chiton (class Gastropoda, with Polyplacophora and Scaphopoda)

This sheet was written on 12 October 2026, from 14:05 to 14:37 EDT, and audited the same afternoon. The corrections are listed in `snail.audit.md`. Unfinished items are marked **[unfinished]**, and they are these:

- The GBIF and iNaturalist APIs were refused in this session. In the shell, the proxy refused api.gbif.org and api.inaturalist.org (CONNECT 403). Through WebFetch, api.gbif.org was rate limited (HTTP 429) and I did not retry it. I therefore have no family or species counts, and the counts below are the assignment's and the repository's. The audit re-fetched Stylommatophora from GBIF and got 916,884, which matches the repository.
- BioOne blocked automated reading, so I could not open the review by Zieger and Meyer-Rochow (2008) or the paper by Gál and colleagues (2004) on snail eye optics. PMC also showed a captcha.
- The red slug's 52 degrees comes from Irwin and colleagues (2022), who cite it to Zieger, Vakoliuk, Tuchina, Zhukov and Meyer-Rochow (2009). That primary paper was not opened.
- The angles from Serb and Eernisse (2008) were taken from their Table 1, whose column mixes resolution and inter-receptor angle. I did not open the primary papers behind that table (Hamilton and Winter, 1982; Zieger and Meyer-Rochow, 2008; Land and Nilsson, 2002; Land, 1981). The review's reference list titles Hamilton and Winter (1982) as a study of the snail *Littorina irrorata*, so the source it names for the garden snail's 14.5 degrees is a study of a different snail.
- I found no flicker-fusion measurement for any member of the group. I found no measurement of how land snails respond to moving objects, and none of a land snail's response to shadows (the shadow row is from the pond snail).
- For whelks, cone snails, top snails, abalones, nerites and apple snails I found nothing beyond a thesis summary on apple snails.
- The page I opened for the 2018 IKBFU Vestnik paper did not show its authors. The audit could not open the Berghia preprint, so its figures are removed below.
- The audit could not open Chase and Hall (1996) or the abstract of Alkon and Fuortes (1972), so the tentacle-withdrawal reflex is removed from the rows.

## 1. Scope

**What the view holds.** The assignment's 2,085,365 records are the repository's "snail and slug" view (2,013,896 records, `docs/VIEWS.md`) plus "chiton and other mollusc" (71,469). I checked that the order counts in `docs/views/world-orders.csv` sum to both totals. They fall into four parts:

| Part | Orders (records) | Records | Share |
|---|---|---:|---:|
| Land snails and slugs | Stylommatophora 916,884; Systellommatophora 14,933 | 931,817 | 44.7% |
| Sea slugs | Nudibranchia 430,262; Aplysiida 31,543; Cephalaspidea 26,769; Pleurobranchida 7,282; Umbraculida 2,424; Pteropoda 1,262; Runcinida 134 | 499,676 | 24.0% |
| Sea and freshwater snails | Neogastropoda 195,258; Littorinimorpha 194,664; Trochida 89,982; Lepetellida 39,977; Cycloneritida 26,567; Architaenioglossa 24,565; Siphonariida 6,902; Ellobiida 2,891; three small orders 1,597 | 582,403 | 27.9% |
| Chitons, tusk shells and others | Chitonida 70,075; Lepidopleurida 547; Callochitonida 466; Dentaliida 367; Gadilida 9; two orders 5 | 71,469 | 3.4% |

No freshwater pulmonate order (the pond snails and ramshorns) appears in `world-orders.csv`, and I did not check why. In Alachua County the most recorded are the Manatee Treesnail, the Rosy Wolfsnail, the Florida Leatherleaf Slug, the Asian Tramp Snail and the Island Apple Snail (assignment). Four are land snails and slugs, and the apple snail is in Architaenioglossa.

**What is measured, by part.** Every figure below comes from a page I opened in this session (sources in section 5), and several of those pages cite older work. To compare them I convert each to cycles per degree in one way, and the conversion is mine. An inter-receptor angle gives a sampling limit of 1 / (2 × angle). An object that was just detected is read as half a cycle, 1 / (2 × width), as the tick sheet did. Irwin and colleagues' anatomical figures are already a full cycle (2Δφ), so they convert as 1 / angle. Their behavioural 1.06 degrees is also a full cycle, twice the narrowest check width of 0.53 degrees, so it converts as 1 / 1.06.

| Animal | Part | Figure | Kind | Cycles per degree (my conversion) |
|---|---|---|---|---:|
| Garden snail, *Helix aspersa* | land snail | 14.5 degrees | resolution or inter-receptor angle, the table does not say which (Serb and Eernisse, 2008, citing Hamilton and Winter, 1982, whose title in the review names *Littorina irrorata*) | 0.034 |
| Grove snail, *Cepaea nemoralis* | land snail | 8.0 degrees | same column (Serb and Eernisse, citing Zieger and Meyer-Rochow, 2008) | 0.063 |
| Red slug, *Arion rufus* | land slug | 52 degrees | behaviour (Irwin and colleagues, 2022, citing Zieger and colleagues, 2009) | 0.010 |
| *Berghia stephanieae* | nudibranch | approached a black stripe set outside its arena; the abstract I opened gives no width | behaviour (Quinlan, Cho and Katz, 2021) | not known |
| *Acanthopleura granulata* | chiton with shell eyes | about 9 to 12 degrees; clamped down at a 9 degree disc overhead | optics and behaviour (Speiser and colleagues, 2011) | 0.04 to 0.06 |
| *Chiton tuberculatus* | chiton with eyespots | 10 degrees or finer, in orientation tests with still dark targets at the side | behaviour (Kingston and colleagues, 2018) | 0.05 or more |
| Common periwinkle, *Littorina littorea* | sea snail | 3.6 degrees (Irwin, citing Seyer, 1992); 4.5 degrees (Serb and Eernisse, citing Land and Nilsson, 2002) | anatomy | 0.11 to 0.28 |
| *Conomurex luhuanus* | strombid conch | 1.06 degrees by behaviour; 1.04 degrees by anatomy | behaviour and anatomy (Irwin and colleagues, 2022) | 0.94 to 0.96 |
| *Lobatus raninus* | strombid conch | 0.94 degrees (2Δφ) | anatomy (Irwin, citing Seyer, 1994) | 1.1 |

The periwinkle's upper value of 0.28 assumes that Seyer's 3.6 degrees is a 2Δφ, and I have not confirmed that. Two figures disagree. Serb and Eernisse list *Strombus luhuanus* (now *Conomurex*) at 0.23 degrees, citing Land (1981), while Irwin and colleagues measure 1.04 degrees for 2Δφ, which is 0.52 degrees between receptors. I use Irwin's, because it is newer and agrees with their behavioural test.

**One view can be true for land snails and slugs, nudibranchs and chitons together.** Their measured sharpness falls between 0.01 and 0.06 cycles per degree. In this engine that is a blur radius from a third of the screen's long side to more than the whole of it, so at this sharpness the three pictures would look nearly the same. They differ in ways the picture does not carry:

- **Land snails and slugs** carry their eyes on the tips of the upper tentacles and also sense light outside the eyes. A slug without eyes senses light with its brain (Nishiyama and colleagues, 2019).
- **Nudibranchs** have eyes deep under the skin (Rudman, 1999).
- **Chitons with shell eyes** look upward through hundreds of eyes across the shell. Those eyes tell a dark shape from an even dimming. Chitons with eyespots respond to both alike, and every chiton has light-sensing aesthetes in the shell (Kingston and colleagues, 2018). Shell eyes occur in only a few genera (Liu, Sigwart and Sun, 2022). I could not count how many chiton records fall in those genera. **[unfinished]**
- **Tusk shells** (376 records) have no eyes by the account of Serb and Eernisse, who say that four of the seven molluscan classes have eyes and name them as gastropods, bivalves, chitons and cephalopods.

For the eyeless chitons and the tusk shells the picture overstates sight. They hold under 3.4% of records.

**One view is false for the sea snails with large camera eyes.** The measured conchs see about 30 times finer than the garden snail, and the periwinkle 3 to 8 times finer. In the engine, the conch's 0.95 cycles per degree blurs over 2% of the screen's long side, where the snail's 0.035 blurs over half of it. So the line falls between the sea snails with large camera eyes, starting with the strombid conchs, and everything else. The commonest members are on the coarse side: land snails and slugs (44.7%) and sea slugs (24.0%). The sea and freshwater snails (27.9%) are measured only in periwinkles and strombids. Seyer's thesis (1998) adds that the apple snail's eye has a lens with severe aberrations and pools many receptors on each nerve fibre, which gains sensitivity and loses resolution, while the periwinkle's eye shows a reasonable match between optics and retina.

**How smell and moisture compare with sight.** In the sources I opened, a land snail's sight reaches only light, shade and very large shapes. Its smell steers it to food from a distance and along trails. A giant African land snail finds a distant smell in still air with its upper tentacles, follows a slime trail with its lower ones, and learns which food smells to approach (Chase and Croll, 1981; Croll and Chase, 1980). Garden snails are most active at night and right after rain, and in one study they came out of hibernation after the first heavy rain, whatever the air temperature (Kwiecien, Breitenbach and Kozielska, 2022). A nudibranch's rhinophores smell chemicals in the water (Rudman, 1999). My reading is that smell guides a snail's day far more than sight does. That reading is my own construction from these sources, and none of them measures smell against sight.

**Recommendation.** Build one view, `snail`, for the whole assignment: Gastropoda, Polyplacophora and Scaphopoda. Draw it at the land snail's sharpness, and say in a row that conchs and periwinkles see more. There are three implementation notes.

- The word table in `src/cam.r.js` already sends snails, slugs, nudibranchs, conchs, periwinkles, limpets, chitons and tusk shells to `snail`, and `GROUPS` in `src/cam.a.js` already labels it "a snail or slug".
- The species routing tested in `tools/species/test_eyes.py` currently expects *Pomacea* (Gastropoda) to give `other`. It would need to send the three classes to `snail`. I did not find the routing file itself.
- `tools/species/views_todo.py` keeps chitons and tusk shells in "chiton and other mollusc", so that table would move them into `snail` as well.

If the group ever splits, the second view should be a sharper `conch` for family Strombidae (cpd about .95). Periwinkles could join it at a lower sharpness once whelks, cone snails and top snails are measured.

## 2. The rows

```
['m', 'Eyes', 'A land snail or slug has a small eye with a lens at the tip of each upper tentacle. In the White-lipped Snail each eye is about a quarter of a millimetre across.'],
```
Source: Nishiyama and colleagues, 2019, describe a lens eye on the tip of each superior tentacle in the slug *Limax valentianus* (my paraphrase of the summary I read). Shepeleva, 2023, Table 1, gives the eye of *Cepaea hortensis* as 233 µm across, citing her own 2006 paper.

```
['m', 'Sharpness', 'The garden snail’s eye resolves about 15 degrees, so it keeps under a thousandth of the detail you see. Behaviour tests put a red slug’s resolution at about 52 degrees, the width of a metre-wide shape seen from a metre away.'],
```
Source: Serb and Eernisse, 2008, Table 1 ("Spatial resolution of a selection of animal eyes", column "Resolution/inter-receptor angle"), give 14.5 degrees for *Helix aspersa*, citing Hamilton and Winter (1982), which I did not open. The review's reference list titles that paper "Behavoural responses to visual stimuli by the snail, Littorina irrorata", so the garden snail figure cannot be traced to a measurement in *Helix* through this review. Read either as an inter-receptor angle or as a just-resolved object, 1 / (2 × 14.5) = 0.034 cycles per degree, which is 1/1,760 of 60. Irwin and colleagues, 2022, give a spatial resolution of 52 degrees from behavioural data for *Arion rufus*, citing Zieger, Vakoliuk, Tuchina, Zhukov and Meyer-Rochow (2009), which I did not open. I do not know what task the slugs were given. A shape 1 m wide at 1 m spans 53 degrees.

```
['m', 'Colour', 'A slug’s eye is most sensitive to blue near 480 nanometres in the dark and to violet near 420 in daylight. In dim light slugs fled only from the shorter wavelengths, and the picture is drawn in grey weighted to blue, which is this app’s own choice.'],
```
Source: Matsuo and colleagues, 2023, in *Limax valentianus*, report an electroretinogram peak at 480 nm when dark-adapted and at 420 nm when light-adapted. Nishiyama and colleagues, 2019: "they escaped only from short wavelength light if the irradiance was low (10 μW cm−2)".

```
['m', 'Light without eyes', 'A slug whose eyes have been removed still crawls away from bright light, which it senses with its brain.'],
```
Source: Nishiyama and colleagues, 2019, "Light avoidance by a non-ocular photosensing system" in *Limax valentianus*. Blinded slugs entered the dark side under white light near 503 μW cm−2. Lighting the head with blue light worked and lighting the tail did not, opsin messages were found in the brain, and the isolated suboesophageal ganglia responded to 400 to 480 nm. The authors treat the skin as a less likely site. In the pond snail, van Duivenboden, 1982, found that removing the eyes, the tentacles or both had only minor effects on turning toward light.

```
['g', 'Shadows', 'A pond snail pulls back into its shell when a shadow falls on it. It feels the shadow through its skin, most strongly in blue-green light near 490 nanometres.'],
```
Source: Sunada, Lukowiak and Sakakibara, 2012, in *Lymnaea stagnalis*. The shadow-induced withdrawal is mediated by skin photoreceptors on the foot, the mantle and around the breathing pore. IKBFU's Vestnik, 2018 (authors not shown), reports that the skin's sensitivity, measured by the shadow reflex in young *L. stagnalis*, peaks at 490 nm.

```
['g', 'Sea slugs', 'A nudibranch’s eyes lie deep under the skin behind its rhinophores. Even so, one nudibranch crawled toward a black stripe placed outside its arena.'],
```
Source: Rudman, 1999, says the eyes are "hidden deep beneath the skin, behind the rhinophores". Quinlan, Cho and Katz, 2021, report that *Berghia stephanieae* reliably navigated toward a black stripe on a white background outside the arena, and also approached a stripe matched in brightness to the background. It did not approach when hungry or when food odour was present. The abstract gives no stripe widths.

```
['m', 'Chitons', 'One Caribbean chiton has hundreds of tiny eyes in its shell, with lenses of the mineral aragonite, and it clamps down when a dark disc 9 degrees wide appears overhead. Only a few kinds of chiton have such eyes, and the rest sense light through simpler organs in the shell.'],
```
Source: Speiser, Eernisse and Johnsen, 2011, in *Acanthopleura granulata*, give an angular resolution of "about 9°-12°". The animals responded to black overhead circles 9 degrees wide, and did not respond to uniform dimming of the same amount. Duke Today, 2011, reports "hundreds of tiny lenses". Liu, Sigwart and Sun, 2022, say shell eyes are "restricted to only a few genera". Kingston, Chappell and Speiser, 2018, say all chitons have aesthetes, eyespots occur in Chitoninae and *Callochiton*, and *A. granulata* eyes are about 80 µm across with about 100 photoreceptors. Serb and Eernisse, 2008, say aesthetes "have been demonstrated experimentally to be capable of photoreception".

```
['g', 'Sea snails', 'One conch reacts to objects about 1 degree across, and a periwinkle’s eye holds detail of about 4 degrees. Both see far more than this picture shows, since it follows the land snails and sea slugs.'],
```
Source: Irwin and colleagues, 2022. *Conomurex luhuanus* responded to objects of 1.06 degrees, with an anatomical estimate of 1.04 degrees. They cite 3.6 degrees from anatomy for *Littorina littorea* (Seyer, 1992). Serb and Eernisse, 2008, give 4.5 degrees for *L. littorea* in their resolution or inter-receptor column, citing Land and Nilsson (2002).

```
['m', 'Smell', 'A giant African land snail finds a smell on the air with its upper tentacles and follows a slime trail with its lower ones. It learns the smell of food it has eaten and heads for it.'],
```
Source: Chase and Croll, 1981, in *Achatina fulica*. Snails without both posterior tentacles performed at chance upwind and failed to orient to a distant source in still air. Removing both anterior tentacles impaired trail following. The abstract says "posterior" and "anterior". Reading those as the upper (eye-bearing) and lower pairs is my mapping. Croll and Chase, 1980, found that preferences required eating the food and lasted 21 days after 48 hours of feeding.

```
['x', 'Smell and damp', 'A nudibranch smells the water with its rhinophores, and a garden snail comes out after rain. Neither reaches a camera.'],
```
Source: Rudman, 1999: rhinophores "'smell' chemicals in the water". Kwiecien, Breitenbach and Kozielska, 2022: *Cornu aspersum* "is most active during the night and directly after rainfall".

## 3. The picture

**What the view shows.** The view shows what a camera can carry of a coarse lens eye: a grey field of one or two large soft patches, with the bright sky and large dark masses, weighted to blue. Still things stay in the picture, because the nudibranch approached a still stripe and the eyespot chiton oriented to still dark targets. The view is a near neighbour of the plant's `field: 1`. It keeps a picture because land slugs, nudibranchs and eyed chitons each resolved shapes in behaviour tests (52 degrees in the red slug, 9 in the eyed chiton, and a stripe of unreported width in the nudibranch).

**Drawn from the camera:** brightness and large dark shapes against brighter surroundings.

**Stood in for:** colour is drawn as grey weighted to blue, with invented weights.

**Left out and named in the rows:** the light sense outside the eyes, smell and damp.

**Left out silently:** the eyes' aim on moving tentacles, the chiton's upward dome of eyes, and the sharper eyes of conchs and periwinkles beyond the one row that names them.

| Field | Value | Behind it |
|---|---|---|
| `chip`, `who` | 'Snail', 'a snail or slug' | `who` is the existing label in `GROUPS`. `chip` is the app's wording, **invented**. |
| `cpd` | .035 | This value rests on the row "Sharpness". It is my conversion of the garden snail's 14.5 degrees, 1 / (2 × 14.5) = 0.034, a figure whose cited source is titled as a study of *Littorina irrorata*. The eyed chiton's 9 degree disc gives 0.056. The red slug's 52 degrees gives 0.010, so the value may flatter slugs. Choosing the snail figure over the coarser slug figure is **invented**. By the blur rule in `src/cam.b.js` (0.6 × long side / `VIEW_DEG` / `cpd`), the blur radius is half the screen's long side at `VIEW_DEG` 34, and 0.71 of it at 24. |
| `M` | [.05, .3, .65, .05, .3, .65, .05, .3, .65] | This value rests on the row "Colour". The peaks at 480 nm (dark) and 420 nm (light) are measured in *Limax valentianus*. Equal rows give grey, and the blue-heavy weights are **invented**. Matsuo and colleagues place all four opsins in the "Type-I photoreceptors", a name that implies other types, and I did not check whether another type could compare colours. Grey is therefore my inference. |
| `pupil` | 'o' | Shepeleva, 2023, measures a pupil in seven land snails at about half the eye's width (relative pupil size 0.5, which matches pupil diameter over eye diameter in her Table 1) and describes it as round. With `dof` unset, 'o' and 'none' give the same output. |
| `field` | unset (0) | I considered `field: 1` and rejected it. Land slugs, nudibranchs and eyed chitons each resolved shapes in behaviour tests, and at `cpd: .035` the picture is already close to what `field: 1` gives. |
| `gate` | unset | The nudibranch approached a still stripe (Quinlan, Cho and Katz, 2021), and the eyespot chiton oriented to still dark targets (Kingston and colleagues, 2018), so the picture keeps still things. |
| `persist`, `rate` | unset | I found no time constant and no flicker-fusion measurement. |
| `gain` | unset | I found no comparison with human dim-light sensitivity. |
| `fov` | unset | I found no field measurement for a snail's eye, and values under 180 change nothing. |
| `topoA`, `topoS`, `fall`, `fovea`, `dof`, `sheen`, `uvBlue`, `noGreen`, `hold`, `thrust` | unset | No source supports them. Matsuo and colleagues report ultraviolet sensitivity in two opsins (Opn5A and Opn5B). I found no ultraviolet measurement of the whole eye or of behaviour, so `uvBlue` stays off. |
| `cue` | 'Hold the phone close to the ground and move it slowly. Only the largest patches of light and dark remain.' | This is the app's wording, **invented**. |

Here is a sketch of the entry for the owner to place. No file was changed.

```
var SNAIL = [.05, .3, .65, .05, .3, .65, .05, .3, .65];   // peaks near 480 nm (dark) and 420 nm (light) in Limax valentianus; grey weighted to blue, weights invented
snail: { chip: 'Snail', who: 'a snail or slug', cpd: .035, pupil: 'o', M: SNAIL,
  cue: 'Hold the phone close to the ground and move it slowly. Only the largest patches of light and dark remain.', rows: [ /* the ten rows above */ ] }
```

## 4. What the engine cannot draw yet

| Effect | What it would show | Phone input that could stand in | Judgement |
|---|---|---|---|
| Light outside the eyes | A glow over the whole picture whenever bright light falls on the animal from any side, with no image, as in the blinded slug's brain and the pond snail's skin. | The camera's average brightness. | It is easy as a blend toward `field: 1` driven by overall brightness. It would be invented in its proportions and should be called so. |
| Tentacle withdrawal at a touch | The picture would shrink to darkness when the person touches the screen and return slowly, as a tentacle pulls in and rises again. | The touch screen. | It is easy. Its grounding in the withdrawal reflex (Chase and Hall, 1996) was not confirmed in the audit, and its timing would be invented, so an `i` row should say so. |
| Smell, scent trails and food learning | These have no visual form. | No phone input senses smell. | It is impossible. |
| Damp and rain | The view would wake after rain and slow in dry air. | No humidity sensor that a web page can read, to my knowledge (no source opened). The weather at the phone's location could stand in, with location permission and a weather service. | It is medium work and wholly invented. I recommend against it. |
| The chiton's dome of shell eyes | Hundreds of small soft patches, each about 10 degrees wide, would cover the sky above the shell. | The camera tilted up and masked into a mosaic of cells by a new aperture shape in the engine. | It is medium work and would serve under 3.4% of records. |
| Two eyes on moving tentacles | Each eye's view would rise, fall and swing as its tentacle moves. | Device motion. | It is medium work and would show little at this sharpness. |
| The conch's sharper eye | A clearer picture at about 1 cycle per degree. | The camera, with no new field. | It is easy, since it needs only a second entry and routing for family Strombidae once counts justify it. |

## 5. Sources

- Irwin, A. R., Williams, S. T., Speiser, D. I. and Roberts, N. W., 2022. The marine gastropod *Conomurex luhuanus* (Strombidae) has high-resolution spatial vision and eyes with complex retinas. *Journal of Experimental Biology* 225(16): jeb243927. doi:10.1242/jeb.243927. Findings: *C. luhuanus* responded to objects of 1.06 degrees (twice the narrowest check width of 0.53 degrees) and to Michelson contrast of 0.07, with an anatomical estimate of 1.04 degrees (2Δφ) and an eye 1.2 mm across. They cite 3.6 degrees (anatomy) for *Littorina littorea* (Seyer, 1992), 52 degrees (behaviour) for *Arion rufus* (Zieger and colleagues, 2009) and 0.94 degrees for *Lobatus raninus* (Seyer, 1994). **opened**: the abstract on the Scholar Commons record (https://scholarcommons.sc.edu/biol_facpub/319) and the full text there (https://scholarcommons.sc.edu/cgi/viewcontent.cgi?article=1316&context=biol_facpub). The primary sources for *Littorina*, *Arion* and *Lobatus* are **secondary** (Irwin and colleagues, 2022).
- Zieger, M. V., Vakoliuk, I. A., Tuchina, O. P., Zhukov, V. V. and Meyer-Rochow, V. B., 2009. Eyes and vision in *Arion rufus* and *Deroceras agreste* (Mollusca; Gastropoda; Pulmonata): what role does photoreception play in the orientation of these terrestrial slugs? *Acta Zoologica* 90: 189 to 204. doi:10.1111/j.1463-6395.2008.00369.x. Finding: 52 degrees by behaviour in *A. rufus*. **secondary** (Irwin and colleagues, 2022).
- Seyer, J.-O., 1992. Resolution and sensitivity in the eye of the winkle *Littorina littorea*. *Journal of Experimental Biology* 170: 57 to 69. doi:10.1242/jeb.170.1.57. Finding: 3.6 degrees from anatomy. **secondary** (Irwin and colleagues, 2022).
- Seyer, J.-O., 1994. Structure and optics of the eye of the hawk-wing conch, *Strombus raninus* (L.). *Journal of Experimental Zoology* 268: 200 to 207. doi:10.1002/jez.1402680304. Finding: 0.94 degrees (2Δφ). **secondary** (Irwin and colleagues, 2022).
- Serb, J. M. and Eernisse, D. J., 2008. Charting evolution's trajectory: using molluscan eye diversity to understand parallel and convergent evolution. *Evolution: Education and Outreach* 1(4): 439 to 447. doi:10.1007/s12052-008-0084-1. Findings: Table 1, "Resolution/inter-receptor angle (Δ, °)", gives *Helix aspersa* 14.5 (Hamilton and Winter, 1982), *Cepaea nemoralis* 8.0 (printed "nemorais"; Zieger and Meyer-Rochow, 2008), *Littorina littorea* 4.5 (Land and Nilsson, 2002) and *Strombus luhuanus* 0.23 degrees (Land, 1981). The reference list titles Hamilton and Winter (1982) "Behavoural responses to visual stimuli by the snail, Littorina irrorata" (*Animal Behaviour* 30: 752 to 760). Two chiton lineages have ocelli, with 411 to 1,472 in one *Onithochiton neglectus*. Aesthetes are photoreceptive. "Of the seven molluscan classes, it is these four classes that possess eyes", and the four are gastropods, bivalves, chitons and cephalopods. **opened** (Springer page and PDF at https://link.springer.com/content/pdf/10.1007/s12052-008-0084-1.pdf). The four primary sources of Table 1 are **secondary** (this review), and I give their names and years only as the review gives them.
- Speiser, D. I., Eernisse, D. J. and Johnsen, S., 2011. A chiton uses aragonite lenses to form images. *Current Biology* 21(8): 665 to 670. doi:10.1016/j.cub.2011.03.033. Findings: aragonite lenses, angular resolution about 9 to 12 degrees, and a response to 9 degree black overhead circles with no response to an equal uniform dimming, in *Acanthopleura granulata*. **opened** (abstract at https://scholars.duke.edu/publication/778613).
- Duke Today Staff, 14 April 2011. News release on Speiser and colleagues (2011). https://today.duke.edu/2011/04/chiton.html. Findings: "hundreds of tiny lenses"; chitons clamped down at black disks 3 cm or wider shown 20 cm above them. **opened**.
- Kingston, A. C. N., Chappell, D. R. and Speiser, D. I., 2018. Evidence for spatial vision in *Chiton tuberculatus*, a chiton with eyespots. *Journal of Experimental Biology* 221: jeb183632. doi:10.1242/jeb.183632. Findings: resolution of 10 degrees or finer in orientation tests with still dark lateral targets; all chitons have aesthetes; eyes in Acanthopleurinae, Toniciinae and *Schizochiton*; eyespots in Chitoninae and *Callochiton*; *A. granulata* eyes about 80 µm with about 100 photoreceptors; eyespot chitons responded alike to a 27 degree target and a 17% uniform dimming. **opened** (full text PDF).
- Liu, X., Sigwart, J. D. and Sun, J., 2022. Phylogenomic analyses shed light on the relationships of chiton superfamilies and shell-eye evolution. bioRxiv, doi:10.1101/2022.12.12.520088. Finding: shell eyes are "restricted to only a few genera" (Schizochitonidae, Acanthopleurinae, Toniciinae). **opened** (PDF at https://publikationen.ub.uni-frankfurt.de/files/83424/2022.12.12.520088v1.full.pdf).
- Matsuo, R., Koyanagi, M., Sugihara, T., Shirata, T., Nagata, T., Inoue, K., Matsuo, Y. and Terakita, A., 2023. Functional characterization of four opsins and two G alpha subtypes co-expressed in the molluscan rhabdomeric photoreceptor. *BMC Biology* 21: 291. doi:10.1186/s12915-023-01789-7. Findings: in *Limax valentianus*, the electroretinogram peaks at 480 nm when dark-adapted and at 420 nm when light-adapted. The opsin maxima are about 456, 475, 500 and 470 nm, two opsins show ultraviolet sensitivity, and all four lie in the Type-I photoreceptors. **opened** (full text PDF).
- Nishiyama, H., Nagata, A., Matsuo, Y. and Matsuo, R., 2019. Light avoidance by a non-ocular photosensing system in the terrestrial slug *Limax valentianus*. *Journal of Experimental Biology* 222: jeb208595. doi:10.1242/jeb.208595. Findings: lens eyes on the tips of the superior tentacles; blinded slugs avoid light, and the authors locate that sense in the brain; intact slugs fled only short wavelengths at 10 μW cm−2. **opened** (full text PDF).
- Shepeleva, I. P., 2023. The pupil of the camera-like eyes of terrestrial gastropod mollusks (Heterobranchia, Stylommatophora). *Ruthenica* 33(3): 95 to 104. doi:10.35885/ruthenica.2023.33(3).1. Findings: eye diameters of 147 to 270 µm in seven land snails, including 233 µm in *Cepaea hortensis* (from Shepeleva, 2006, **secondary**), relative pupil sizes near 0.5, and a round pupil. **opened** (PDF).
- Quinlan, P. D., Cho, A. K. and Katz, P. S., 2021. Characterization of visually-guided behaviors by the nudibranch, *Berghia stephanieae*. SICB abstract 82-5, https://sicb.org/?p=43735. Findings: approach to a black stripe outside the arena and to an isoluminant stripe, absent when hungry or with food odour; no widths given. **opened**. A later bioRxiv preprint (doi:10.1101/2022.10.24.513581) reportedly gives stripe widths and photoreceptor counts, but the audit could not open it, and none of its figures is used here.
- Rudman, W. B., 1999 (26 March). The nudibranch head. Sea Slug Forum, Australian Museum. https://www.seaslugforum.net/headeudo.htm. Findings: eyes "hidden deep beneath the skin, behind the rhinophores"; rhinophores "'smell' chemicals in the water". The page also says the eyes "cannot see images", which the stripe approach in Quinlan and colleagues contradicts. **opened**.
- Alkon, D. L. and Fuortes, M. G. F., 1972. Responses of photoreceptors in *Hermissenda*. *Journal of General Physiology* 60(6), from page 631. doi:10.1085/jgp.60.6.631. The audit confirmed the citation (https://modeldb.science/citations/34132, PubMed ID 4645675) but could not open the abstract, so no figure from it is used.
- Sunada, H., Lukowiak, K. and Sakakibara, M., 2012. Repetitive noxious stimulus altered the shadow-induced withdrawal behavior in *Lymnaea*. *Acta Biologica Hungarica* 63 (Suppl. 2): 179 to 189. doi:10.1556/ABiol.63.2012.Suppl.2.23. Finding: shadow withdrawal is mediated by skin photoreceptors on the foot, the mantle and around the breathing pore. **opened** (record at https://real.mtak.hu/72427/).
- The spectral dependence of skin sensitivity to light in immature *Lymnaea stagnalis* L. specimens. *IKBFU's Vestnik, Series Natural Sciences*, 2018, issue 3. https://journals.kantiana.ru/eng/vestnik/nature/13099/71848/. The page did not show the authors. Finding: the skin's sensitivity peaks at 490 nm, measured by the shadow reflex. **opened** (abstract).
- van Duivenboden, Y. A., 1982. Non-ocular photoreceptors and photo-orientation in the pond snail *Lymnaea stagnalis* (L.). *Journal of Comparative Physiology* 149(3): 363 to 368. doi:10.1007/BF00619152. Finding: removing the eyes, the tentacles or both had only minor effects on photo-orientation. **opened** (abstract).
- Chase, R. and Croll, R. P., 1981. Tentacular function in snail olfactory orientation. *Journal of Comparative Physiology A* 143(3): 357 to 362. The DOI was not shown. Findings: posterior tentacles are needed for upwind and still-air orientation and anterior tentacles for trail following, in *Achatina fulica*. **opened** (abstract at https://latam-cl.demo.elsevierpure.com/en/publications/tentacular-function-in-snail-olfactory-orientation).
- Croll, R. P. and Chase, R., 1980. Plasticity of olfactory orientation to foods in the snail *Achatina fulica*. *Journal of Comparative Physiology* 136(3): 267 to 277. doi:10.1007/BF00657543. Findings: learned food-odour preferences; 48 hours of feeding gave a preference kept for 21 days. **opened** (summary).
- Chase, R. and Hall, B., 1996. Nociceptive inputs to C3, a motoneuron of the tentacle withdrawal reflex in *Helix aspersa*. *Journal of Comparative Physiology A* 179(6): 809 to 818. doi:10.1007/BF00207359. The audit could not open it (HTTP 429), so no row rests on it.
- Kwiecien, O., Breitenbach, S. and Kozielska, M., 2022. Monitoring annual snail activity cycles: field-testing paleoenvironmental assumptions. EGU General Assembly 2022, EGU22-5061. https://meetingorganizer.copernicus.org/EGU22/EGU22-5061.html. Findings: *Cornu aspersum* most active at night and directly after rain; emergence from hibernation after the first heavy rainfall. **opened** (abstract).
- Seyer, J.-O., 1998. Comparative optics of prosobranch eyes. PhD thesis, Lund University. https://lup.lub.lu.se/record/38769. Findings: in *Ampularia* (apple snail) a lens with severe aberrations and strong pooling of receptors; in *Littorina* a reasonable match of optics and retina; in *Strombus* significant light spread between receptors. **opened** (abstract).
- This repository: `docs/VIEWS.md`, `docs/views/world-orders.csv`, `src/cam.a.js` (`paramsOf`, `GROUPS`, `VIEW_DEG`), `src/cam.b.js` (blur rule) and `src/cam.r.js` (word table). Findings: order counts, totals, the blur rule and routing. **opened**.
- GBIF occurrence API (dataset 50c9509d-22c7-4a22-a47d-8c48425ef4a7). The audit read Stylommatophora at 916,884 (https://api.gbif.org/v1/occurrence/search?datasetKey=50c9509d-22c7-4a22-a47d-8c48425ef4a7&orderKey=1456&limit=0). The iNaturalist API was **not read**.

## 6. Open questions for a vision or sensory scientist

1. Is the garden snail's 14.5 degrees (Hamilton and Winter, 1982, as Serb and Eernisse cite it, though their reference is titled as a study of *Littorina irrorata*) a behavioural or an anatomical figure, and has resolution been measured by behaviour in *Cepaea* or *Limax maximus*? The red slug's 52 degrees is more than three times coarser.
2. Do land snails respond to a moving or looming object with their eyes, as conchs and chitons do, and how fast do their photoreceptors follow flicker? Either answer would set `gate`, `persist` or `rate`.
3. How narrow a dark stripe will *Berghia* approach, and do the dorid and aeolid nudibranchs people photograph most approach stripes as it does?
4. Do chitons with only aesthetes respond to shapes at all, or only to the amount of light, and which of the chitons people photograph most have shell eyes?
5. What do whelks, cone snails, top snails and moon snails resolve? Measurements there would decide whether the sea snails need a view of their own.
