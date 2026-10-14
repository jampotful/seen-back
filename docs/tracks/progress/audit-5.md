# Precision audit 5, 14 October 2026 (batch recheck)

The batch recheck that audit 4 left unstarted: every record of sweep-12, sweep-6, sweep-11, sweep-8, sweep-22, insects-met, sweep-15, sweep-19, then sweep-7 and sweep-17, checked against its source page, in that order, skipping the ids already corrected in `recheck-2.jsonl` and `recheck-4.jsonl`. Method as in audits 2 to 4: each source URL opened with WebFetch and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces of at most 125 characters (the summariser's cap), with the split points recorded in `where`. A page blocked by a bot wall, a proxy refusal (429) or a paywall that hides the quoted passage is `unverifiable`, never guessed; where a publisher blocks, a repository or PMC copy is tried. Verdicts: `confirm`, `requote` (value right, quote not on the page, stitched or a rendering), `correct` (value, grade, partial flag or source metadata changed), `retract` (the page does not support the value). Opsin-inferred and family-level claims are held to `g` at most; a sampling time is not a diel rhythm. Corrections go to `docs/views/recheck/recheck-5.jsonl` in the recheck-4 schema; no evidence file is edited.

A quote that differs from the page only by typography (curly apostrophes, en dashes, a degree sign written as "deg", an OCR slip, a line-break hyphen) or that is a verbatim reading of a table column is counted `confirm`, as audit 2 did; a `where` that names the wrong section is noted in the table and not counted as an error.

## Batch table

| batch | due | records checked | errors | error rate | unverifiable | status |
|---|---|---|---|---|---|---|
| sweep-12 | 7 | 7 | 4 | 57% | 0 | finished |
| sweep-6 | 32 | 32 | 11 | 34% | 0 | finished |
| sweep-11 | 15 | 15 | 11 | 73% | 0 | finished |
| sweep-8 | 23 | 23 | 17 | 74% | 0 | finished |
| sweep-22 | 5 | 5 | 0 | 0% | 2 | finished |
| insects-met | 51 | 23 | 1 | 5% | 4 | in progress |
| sweep-15 | 13 | 0 | 0 | n/a | 0 | not started |
| sweep-19 | 19 | 0 | 0 | n/a | 0 | not started |
| sweep-7 | 16 | 0 | 0 | n/a | 0 | not started |
| sweep-17 | 12 | 0 | 0 | n/a | 0 | not started |
| all | 193 | 105 | 44 | 44% | 6 | |

Error rate is errors over verifiable records (checked minus unverifiable). Errors are requote, correct, regrade, retarget and retract; confirm is not an error.

## Records

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| sweep-12:1 | Anacamptis morio / sense_chemical | m | confirm | quote verbatim in the Abstract (Key Results); 34 compounds and "no compound elicited a physiological response in the pollinators' antennae" confirmed in Results |
| sweep-12:2 | Commelina communis / sense_light_nonvisual | m | requote | value confirmed; quote is a paraphrase; page: "a reduction in light intensity decreased the magnitude and slowed the kinetics of stomatal responses to pulses of blue light" |
| sweep-12:3 | Commelina communis / diel | m | confirm | quote verbatim in the Abstract (split across a line after "C."), not in the Results as `where` said; Results: "The flowers began to blossom at 3:00~5:00 and in fullblown before 6:00"; nine hours and 12:00~13:00 confirmed |
| sweep-12:5 | Fraxinus pennsylvanica / sense_chemical | m | correct | quote not on the page; the Treesearch page carries only the aims; the OUP abstract gives six compounds and the three named ones, lower under higher light, and "Girdling did not affect the levels of these volatiles", so the value's girdling clause was wrong |
| sweep-12:6 | Arctium lappa / sense_light_nonvisual | m | requote | percentages confirmed (text and Table 2); quote not on the page; page: "Both canopy filtered (shade) light and plastic filtered light inhibited seed germination." |
| sweep-12:7 | Carnegiea gigantea / diel | m | confirm | quote verbatim (body text and photo caption) |
| sweep-12:9 | Nezara viridula / spectral_range_nm | m | requote | values confirmed; quote is a paraphrase; page: "responding strongly to ultraviolet region (peak at 360 nm), and maximally to green region (peak at 520 nm)" |
| sweep-6:1 | Pipilo erythrophthalmus / acuity_cpd | m | requote | 8.35 and 38,188 ± 2152 confirmed in Table 1 of the publisher PDF (the HTML page carries the table as an image); the quote stitches a table cell to a Methods sentence |
| sweep-6:2 | Pipilo erythrophthalmus / binocular_deg | m | confirm | quote verbatim in Results ("from 33 deg in the Eastern towhee to 44 deg in the chipping sparrow"; the page writes deg); Table 1 across-elevations mean 23.41±0.87 and blind area 24.39±1.73 confirmed |
| sweep-6:3 | Calypte anna / acuity_cpd | m | requote | values confirmed; the quote closes with a full stop where the page has a comma and the sentence continues "(fovea: 6.26±0.12 ...; area temporalis: 5.59±0.15 ...; whole eye average: 4.64±0.08)" |
| sweep-6:4 | Calypte anna / cff_hz | m | requote | 70-80 Hz confirmed; the quote is a four-word fragment without the value; page: "The limits of temporal visual resolution were estimated as 70–80 Hz." |
| sweep-6:6 | Trachemys scripta elegans / lambda_max_nm | m | requote | 515 nm confirmed; same absent quote as sweep-6:5 (recheck-4) |
| sweep-6:7 | Trachemys scripta elegans / lambda_max_nm | m | requote | 458 nm confirmed; same absent quote as sweep-6:5 |
| sweep-6:8 | Trachemys scripta elegans / lambda_max_nm | m | requote | 372 nm confirmed; same absent quote as sweep-6:5 |
| sweep-6:9 | Trachemys scripta elegans / receptor_classes | m | confirm | quote verbatim ("At the moment, this is the most complex cone system described for vertebrates."); four pigments and seven cone types confirmed; rods not in the abstract, as the note says |
| sweep-6:11 | Morus serrator / spectral_range_nm | m | requote | 396 nm confirmed (Results and Table 1 of the Karger full text, which is open); the quote is a table-row rendering |
| sweep-6:12 | Phalacrocorax varius / spectral_range_nm | m | requote | 395 nm confirmed; table-row rendering |
| sweep-6:13 | Microcarbo melanoleucos / spectral_range_nm | m | requote | 396 nm confirmed; table-row rendering |
| sweep-6:14 | Anhinga anhinga / binocular_deg | m | confirm | Table 1 column Anhinga: 20°, 148°, 168°, 44°, 316° (species as columns, parameters as rows); Results: "the narrowest horizontal binocular field was measured in Anhinga"; the quote is a reading of the column, as audit 2 accepted for sweep-6:16 |
| sweep-6:15 | Anhinga anhinga / fov_h_deg | m | confirm | cyclopean field 316° confirmed in Table 1 |
| sweep-6:16 | Podiceps cristatus / binocular_deg | m | confirm | rechecked: 24°, 143°, 167°, 50°, 310° confirmed |
| sweep-6:17 | Podiceps cristatus / fov_h_deg | m | confirm | cyclopean field 310° confirmed in Table 1 |
| sweep-6:18 | Plegadis ridgwayi / binocular_deg | m | confirm | quote verbatim in the Discussion (degree symbols lost in the PDF text); blind area 28 confirmed |
| sweep-6:19 | Cyanistes caeruleus / spectral_range_nm | m | correct | 316 nm confirmed in Table 1, but the row cites Hart et al. 2000 for the measurement; secondary citation, held partial |
| sweep-6:20 | Podiceps cristatus / spectral_range_nm | m | confirm | Table 1 row: Podiceps cristatus, VS, 390, 1(2), this study |
| sweep-6:21 | Sephanoides sephaniodes / spectral_range_nm | m | correct | 310 nm confirmed in Table 1, but the row cites Herrera et al. 2008 for the measurement; secondary citation, held partial |
| sweep-6:34 | Plegadis ridgwayi / eye_movement | m | confirm | quote verbatim in Results, Eye movement amplitude: "Maximum eye movement amplitude was 14, which is sufficient to abolition binocularity in the frontal field in all of the species." |
| sweep-6:22 | Fragaria vesca / sense_light_nonvisual | m | confirm | quote verbatim in the Abstract; "end-of-day far-red (FR) and blue (B) light activate the expression of FvFT1" and "low expression levels are detected in red (R) and SD treatments" confirmed |
| sweep-6:23 | Fragaria vesca / sense_light_nonvisual | m | confirm | quote verbatim in the Abstract (BMC page; the Springer page returned 429 and PMC a reCAPTCHA); accession differences (IT1, IT4, NOR2, NOR13) confirmed |
| sweep-6:27 | Rumex crispus / sense_light_nonvisual | m | confirm | quote verbatim in the Abstract; "the response of seeds depended on the fluence rate of solar radiation" and the HIR phytochrome sentence confirmed |
| sweep-6:28 | Tussilago farfara / diel | m | confirm | quote verbatim in the English abstract of the Tübingen record; no clock times |
| sweep-6:29 | Cylindropuntia fulgida (as Opuntia fulgida) / sense_light_nonvisual | m | confirm | quote verbatim; "photoperiods of 10, 11.5, and 14 hours were tested", shoot response 38, 36, 31 under them, and "Shoot response in the same order of treatment was 11, 0, 1, and 1" (normal light, red, far-red, dark) confirmed |
| sweep-6:30 | Lotus japonicus / diel | m | confirm | quote verbatim in the Abstract (species names italicised); CCA1 and PRR5 promoters named |
| sweep-6:31 | Ranunculus asiaticus / sense_light_nonvisual | m | confirm | quote verbatim, but in the Discussion, not the Abstract or Methods as `where` says; "quantitative long day (LD) plant" (Introduction) and "14 h (critical photoperiod for R. asiaticus L.)" (Methods) confirmed |
| sweep-6:33 | Ambrosia artemisiifolia / sense_light_nonvisual | m | confirm | quote verbatim in the Abstract, which also says "the species is a short-day plant that requires long nights to induce bloom formation" and reports a north-south gradient in flowering time |
| sweep-6:36 | Larrea tridentata / diel | m | confirm | quote verbatim in the English abstract; drought and young-leaf closure confirmed; journal is Acta Botanica Mexicana, as inferred |
| sweep-6:24 | Lythrum salicaria / sense_light_nonvisual | m | confirm | quote verbatim in the Abstract (link.springer.com page; the doi.org route returned 429); "plants under 10, 12, or 13 h never produced inflorescences", 4-h NI confirmed |
| sweep-6:25 | Rumex obtusifolius / sense_light_nonvisual | m | confirm | quote verbatim; "A 10-min exposure to far-red light (FR) can reverse the effect of both R" confirmed; authors shown as Hand, Craig, Takaki et al. |
| sweep-6:26 | Rumex obtusifolius / sense_light_nonvisual | m | confirm | quote verbatim in the Summary; "This increase can be reversed if the red light treatment is immediately followed by far-red irradiation." confirmed |
| sweep-11:1 | Mitchella repens / sense_chemical | m | requote | value confirmed (27 molecules, four predominant, morphs similar, 1–2 DAF peak, 5-day cycle); quote is a paraphrase; page: "The VOC profile contained 27 molecules consisting mostly of monoterpenes." |
| sweep-11:2 | Liquidambar styraciflua / sense_light_nonvisual | m | requote | value confirmed; quote is a paraphrase; page: "Duration and rate of shoot growth significantly increased with increases in daylength" |
| sweep-11:3 | Picea abies / sense_light_nonvisual | m | requote | value confirmed; quote is a paraphrase; page: "At equal spectral photon flux, FR was more effective than R light in maintaining growth" |
| sweep-11:4 | Picea abies / diel | m | confirm | quote verbatim, but in the Results (gene regulatory network section) of the full text on the SLU repository, not the abstract; LD/LL rhythmic genes (JTK) and DF dampening after stage IV confirmed |
| sweep-11:5 | Elaeagnus umbellata / diel | m | confirm | quote verbatim in the abstract ("diurnal change showed the maximum activity in the mid-day and the minimum in the mid-night") |
| sweep-11:6 | Tillandsia usneoides / diel | m | requote | value confirmed; quote is a paraphrase; page: "net CO2 uptake occurred throughout most of the photoperiod" |
| sweep-11:8 | Pseudotsuga menziesii / sense_chemical | m | requote | value confirmed (biotic stresses treated together); quote is a paraphrase; page gives 6.8 against 0.8 ± 0.2 μg g(dw)−1 h−1 |
| sweep-11:9 | Hesperis matronalis / diel | m | confirm | quote verbatim in the Pherobase abstract ("both color morphs emitted more scent at dusk than at dawn") |
| sweep-11:10 | Sturnella magna / acuity_cpd | m | requote | value confirmed (audit 2 passed it); quote is a rendering; page: "Our estimate of maximum spatial resolving power was 10.3 ± 0.3 cycles/degree" |
| sweep-11:11 | Sturnella magna / binocular_deg | m | requote | value and 32.7, 45.0, 12.0 confirmed; quote is a rendering; page: "The average binocular field width along the horizontal plane with the eyes at rest was 24.0 ± 0.4°" |
| sweep-11:12 | Phoenicopterus ruber / acuity_cpd | m | requote | value confirmed; quote is a paraphrase; page: "Peak anatomical spatial resolving power in both species is approximately 10–11 cycles/deg." |
| sweep-11:13 | Phoenicopterus chilensis / acuity_cpd | m | requote | as sweep-11:12 |
| sweep-11:14 | Pararge aegeria / acuity_cpd | m | requote | 1° and 1.5° confirmed; quote is a rendering (degree sign, sentence continues); page sentence now the quote |
| sweep-11:16 | Otospermophilus beecheyi / fovea | m | confirm | quote verbatim in the Abstract (OCR: "roughtly fivefold decreasesin"), not the Results as `where` says; 20-24,000, 40-44,000, 5-7% rods, 14-19 cones/rod, 1.8:1, streak 1-2 by 5-6 mm, 2 mm inferior to the optic nerve head confirmed |
| sweep-11:17 | Otospermophilus beecheyi / lambda_max_nm | m | requote | 518.9, 517.0 and 436.7 nm confirmed; quote is a rendering of two sentences |
| sweep-8:1 | Phasianus versicolor / binocular_deg | m | confirm | quote verbatim in Section 3(c); vertical extent 120° confirmed |
| sweep-8:2 | Crocodylus porosus / acuity_cpd | m | requote | 8.8±0.4 and 11,083±448 confirmed; quote is a rendering (page: "cycles deg−1", species in the sentence) |
| sweep-8:3 | Crocodylus johnstoni / acuity_cpd | m | requote | 8.0±0.3 and 11,375±756 confirmed; quote is a rendering |
| sweep-8:4 | Crocodylus porosus / fovea | m | confirm | quote verbatim in the Discussion; "approximately four times that of the peripheral regions" and "approximately 2000 cells mm−2" confirmed in Results |
| sweep-8:5 | Crocodylus porosus / lambda_max_nm | m | confirm | Table 4 rows verbatim (SWS single 424.3±4.5; MWS single 502.4±5.3; LWS single 546.2±4.6; LWS twin 546.4±3.6; rods 502.9±2.6); ocular media 374 nm confirmed |
| sweep-8:6 | Crocodylus porosus / receptor_classes | m | requote | value confirmed; quote is a rendering; page: "Three types of single cones, one type of twin cone and one type of rod were present in both species." |
| sweep-8:7 | Crocodylus porosus / tapetum | m | requote | value confirmed; quote is a rendering; page: "A tapetum lucidum is present in both species and has the highest reflectance behind the furrowed foveal slit." |
| sweep-8:8 | Crocodylus porosus / pupil_shape | m | confirm | quote verbatim in the Introduction |
| sweep-8:10 | Tenodera australasiae / interommatidial_deg | m | requote | 0.6° and 2.5° confirmed; quote is a rendering (the note said so); page sentence now the quote |
| sweep-8:11 | Tenodera australasiae / spectral_range_nm | m | requote | 500-520 and 370 nm confirmed; quote is a rendering; page: "with a maximum in the wavelength range 500 nm to 520 nm, and a weak secondary peak around 370 nm" |
| sweep-8:12 | Sympetrum / interommatidial_deg | m | requote | 0.3° and 1.5°–2° confirmed; quote is a rendering; page sentence now the quote |
| sweep-8:13 | Coccinella septempunctata / spectral_range_nm | m | requote | 360, 420, 520 nm confirmed; quote is a rendering; page: "Three spectral types of photoreceptor with sensitivity maxima in the 360 nm (u.v. light), 420 nm (blue light) and 520 nm (green light)" |
| sweep-8:14 | Deilephila elpenor / spectral_range_nm | m | requote | 350, 450, 525 nm confirmed; quote is a rendering of two sentences |
| sweep-8:15 | Convolvulus arvensis / diel | m | correct | quote verbatim (Methods 2.3), but the value's "close the same day" is contradicted by the Results (mean exposure 14.6 h, range 7.07–42.4 h); value rewritten to the measurement |
| sweep-8:16 | Tsuga canadensis / sense_chemical | m | confirm | quote verbatim in the Pherobase abstract; forest trees "several-fold more abundant" than the plantation setting confirmed |
| sweep-8:17 | Mahonia japonica / diel | m | requote | values confirmed (39.7 and 19.8 microg/h, middle of the light period); quote is a rendering |
| sweep-8:18 | Mahonia japonica / sense_light_nonvisual | m | requote | value confirmed; quote is a rendering; page: "photoperiod was the stimulus for enhanced emission of most volatiles" |
| sweep-8:19 | Allium cepa / sense_light_nonvisual | m | confirm | quote verbatim in the Introduction; "Photoperiods under 11 h muted bulbing in the two tropical onion varieties" and "exceeds 12–15 h" confirmed |
| sweep-8:20 | Hedera helix / sense_light_nonvisual | m | requote | value confirmed; the quote closes with a full stop where the sentence continues ", but during the juvenile phase, this capacity is not fully developed." |
| sweep-8:21 | Onoclea sensibilis / sense_light_nonvisual | m | requote | value confirmed; quote is a rendering (the note said so); page: "spores are most sensitive to irradiation in the red region (620-680 nm)" |
| sweep-8:22 | Onoclea sensibilis / sense_light_nonvisual | m | requote | value confirmed; quote is a rendering; page: "Phytochrome is confirmed to be the photoreceptor pigment in the germination response of Onoclea sensibilis L. by demonstrating red-far-red (R-FR) photoreversibility." |
| sweep-8:23 | Iris pseudacorus / diel | m | requote | value confirmed; the quote closes with a full stop where the sentence continues ", and were available for pollination only through the following day before senescing." |
| sweep-8:24 | Iris versicolor / diel | m | requote | value confirmed and the page gives the counts the note said were missing (15 of 20 flowers); quote is a fragment |
| sweep-22:1 | Dissosteira carolina / interommatidial_deg | m | unverifiable | the repository record shows the abstract only (no PDF link reachable; the export page was refused at the permission step, and the search budget was spent); the abstract says acuity was coarser "parallel to the horizon compared to the perpendicular", consistent with the Table 1 reading |
| sweep-22:2 | Dissosteira carolina / acuity_cpd | m | unverifiable | same record as sweep-22:1; the Table 1 row cannot be checked from the abstract |
| sweep-22:3 | Setaria viridis / sense_light_nonvisual | m | confirm | quote verbatim in the Abstract (sentence continues "whose flowering is delayed by long day lengths ..."); Results: "plants in the 12 h trial flowering first, followed by 10 and 14 h trials, then 8 h and finally the 16 h trial", photoperiod 87% confirmed |
| sweep-22:4 | Buddleja davidii / sense_chemical | m | confirm | quote verbatim in the Abstract, which continues ", most effectively by 4-oxoisophorone and oxoisophorone epoxide." |
| sweep-22:5 | Heliconius erato cyrbia / acuity_cpd | m | confirm | quote verbatim in the abstract; the page names only the genus, the subspecies rests on the preprint as `where` says |
| insects-met:1 | Vanessa atalanta / colour_vision | m | confirm | quote verbatim in the Summary (clause of the sentence beginning "We show here, through behavioral experiments") |
| insects-met:2 | Vanessa atalanta / filter_pigments | m | confirm | quote verbatim in the Summary |
| insects-met:3 | Heliconius erato / colour_vision | m | confirm | quote verbatim in the Summary (same sentence as insects-met:1) |
| insects-met:4 | Heliconius erato / filter_pigments | m | confirm | quote verbatim in the Summary; the sentence continues "seen under orthodromic illumination" |
| insects-met:5 | Junonia coenia / lambda_max_nm | m | confirm | "R510 (J. coenia)" verbatim in the abstract, cited there to a previously published sequence |
| insects-met:6 | Junonia coenia / receptor_classes | g | confirm | quote verbatim but for two missing spaces on the page ("(R3-9)in", "(LWS)opsin"); grade g already |
| insects-met:7 | Inachis io / lambda_max_nm | m | confirm | "R530 (I. io)" verbatim in the abstract |
| insects-met:8 | Nymphalis antiopa / lambda_max_nm | m | confirm | "R534 (N. antiopa)" verbatim in the abstract |
| insects-met:9 | Pararge aegeria / interommatidial_deg | m | confirm | quote verbatim in the abstract (link.springer.com page) |
| insects-met:10 | Pararge aegeria / interommatidial_deg | m | confirm | as insects-met:9 |
| insects-met:11 | Pararge aegeria / fov_h_deg | m | confirm | quote verbatim in Results, Visual field and interommatidial angles; the sentence continues "where the view would anyway be blocked by the animal's own thorax, abdomen and wings" |
| insects-met:12 | Pararge aegeria / eye_movement | m | confirm | quote verbatim in the abstract; the sentence continues "; thus, looking at a rather even and dark background ..." |
| insects-met:13 | Osmia rufa / lambda_max_nm | m | confirm | quote verbatim in the abstract (348nm without a space, as on the page) |
| insects-met:14 | Osmia rufa / lambda_max_nm | m | confirm | as insects-met:13 |
| insects-met:15 | Osmia rufa / lambda_max_nm | m | confirm | as insects-met:13 |
| insects-met:16 | Osmia rufa / receptor_classes | m | confirm | quote verbatim (opening words of the same sentence) |
| insects-met:17 | Osmia rufa / colour_vision | m | confirm | quote verbatim; the sentence continues ", whereas Melipona discriminates less well in the violet-blue region."; dual forced-choice tests confirmed |
| insects-met:18 | Bombus impatiens / acuity_cpd | m | requote | 0.35 and 0.36 confirmed; the unit in the quote is a database rendering ("degree(-)(1)"); page: "cycles degree−1" |
| insects-met:19 | Bombus impatiens / receptor_classes | m | confirm | quote verbatim in the abstract; the sentence continues ",namely ommatidia containing two, one or no UV opsin-immunoreactive cells." |
| insects-met:20 | Harmonia axyridis / behaviour_vision | m | unverifiable | Wiley page returns a fetch error (doi.org and onlinelibrary routes); Europe PMC's REST service and PubMed both answered 429 |
| insects-met:21 | Harmonia axyridis / behaviour_vision | m | unverifiable | as insects-met:20 |
| insects-met:22 | Harmonia axyridis / behaviour_vision | m | unverifiable | as insects-met:20 |
| insects-met:23 | Harmonia axyridis / receptor_classes | m | unverifiable | as insects-met:20 |

## Where this run stopped

Four proxy 429 refusals: the Springer page for sweep-6:23 by its doi.org route, the doi.org route for sweep-6:24 (both later opened by their link.springer.com addresses, so these were per-URL), then, for insects-met:20 to 23, the Europe PMC REST service and PubMed in succession after the Wiley page failed outright. The WebSearch budget message had already arrived at sweep-22:1 (a shared per-turn limit), so no further repository copies could be searched for. The brief says to stop on repeated 429s, so the run stopped after insects-met:23 with 94 fetches used.

Finished whole: sweep-12 (7 records), sweep-6 (32), sweep-11 (15), sweep-8 (23), sweep-22 (5). In progress: insects-met, records 1 to 23 of 51 done; records 24 to 52 (except 37) not opened. Not started: sweep-15, sweep-19, sweep-7, sweep-17. The next run should begin at insects-met:24 (Guignard et al. 2025, Wiley, likely blocked; then Switzer and Eason 2000, Belušič et al. 2021 Table 1 on the Royal Society site, and on).

## Error rate so far

105 records opened, 6 unverifiable, 99 verifiable, 44 wrong: **44%**. Of the 44, 40 are requotes (value right, quote not on the page), 4 are corrects: sweep-12:5 (value said girdling changed volatiles; the abstract says it did not, and the page cited carried only the aims), sweep-8:15 (value said one-day flowers close the same day; the Results give a mean 14.6 h and a range to 42.4 h), and sweep-6:19 and sweep-6:21 (Lind et al. 2014 Table 1 cites the blue tit and firecrown values to Hart et al. 2000 and Herrera et al. 2008, so the records are secondary citations and now carry `partial: true`). No value needed a retract and no grade changed. Audit 2's sample estimates (sweep-6 4 of 5, sweep-12 3 of 3, sweep-11 2 of 3, sweep-8 1 of 1) held: the whole batches run 34% to 74% wrong (sweep-22, which the sample had not drawn, ran clean).

## Patterns (this run)

1. The error has one shape in nearly every case, as audits 3 and 4 said: the quote is the fetch summariser's rendering of the page's sentence (a paraphrase, a stitched table row with colons and semicolons, a unit rewritten as "cycles/deg" or "degree(-)(1)", or two sentences fused). Many records say so in their own note ("the quote field restates the abstract as shown on the publisher page; check against the text"). The values stand.
2. A second, smaller shape: the quote stops at a comma and adds a full stop, dropping a qualifying clause (sweep-6:3, sweep-8:20, sweep-8:23). In sweep-8:20 the dropped clause reverses the emphasis ("but during the juvenile phase, this capacity is not fully developed"). These are counted as requotes.
3. Table-column readings written out as "Species: trait value, trait value" (the Pecsics and Lind tables) were accepted as confirm, as audit 2 did for sweep-6:16; the values are on the page and `where` names the table. A reader of `quotecheck.py` output should expect these to fail a verbatim match.
4. Four `where` fields name the wrong section (sweep-12:3, sweep-6:31, sweep-11:4, sweep-11:16; the quote is in the abstract or the discussion, not where the record says). Not counted as errors; noted in the table.
5. Page delivery: PMC's new host served full text for sweep-12:1 and sweep-22:3 but a reCAPTCHA for sweep-6:23 an hour later, so it is intermittent rather than closed. The Karger page for Heswall et al. carries the full text although the records said abstract. The JEB HTML page serves Table 1 of Moore et al. 2015 as an image; the cob.silverchair PDF has it as text. Springer refuses doi.org routes and accepts link.springer.com routes for the same paper. Wiley fails outright; Europe PMC and PubMed are rate-limited by the proxy, so Wiley-only papers (Qiu et al. 2025, Guignard et al. 2025) need an owner PDF through `quotecheck.py`.
