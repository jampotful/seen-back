# Precision audit 6, 14 October 2026

Two parts. (a) A random sample of 20 records from the newest sweeps (sweep-44 to sweep-48), each opened at its source and checked for value, grade and a verbatim quote. (b) The batch recheck that audit 5 left in progress, resumed at insects-met:24, then sweep-15, sweep-19, sweep-7 and sweep-17, skipping ids already corrected in `recheck-2.jsonl`, `recheck-4.jsonl` and `recheck-5.jsonl`.

Method as in audit 5: each source URL opened with WebFetch and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces of at most about 125 characters (the summariser's cap), with split points recorded in `where`; corrected quotes are kept to 40 words or fewer. A page blocked by a bot wall, a proxy refusal (429) or a paywall hiding the passage is `unverifiable`, never guessed; repository copies are tried where PMC, Elsevier or Wiley block, and link.springer.com where doi.org is refused. Verdicts: `confirm`, `requote` (value right, quote not on the page), `correct` (value, grade, partial flag or source metadata changed), `retract` (the page does not support the value). Opsin-inferred and family-level claims are held to `g` at most; a sampling time is not a diel rhythm. Typographic differences (spacing artefacts, curly quotes, dashes, degree signs) and verbatim table-column readings count as `confirm`, as in audits 2 to 5. A quote that is an unpunctuated verbatim substring of a longer sentence is `confirm`; a quote that adds a full stop where the page's sentence continues is a `requote`. Corrections go to `docs/views/recheck/recheck-6.jsonl` in the recheck-5 schema; no evidence file is edited.

## Part (a): random sample of sweep-44 to sweep-48

sweep-45 has no records (its run stopped on 429s before writing any), so four records were drawn from each of sweep-44, sweep-46, sweep-47 and sweep-48, and four more from the remainder of those files (Python `random`, seed 20261014). Fifteen of the twenty are abstract-level partial records.

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| sweep-44:6 | Triteleia laxa / sense_light_nonvisual | m | confirm | quote verbatim in the abstract; 18 degrees C in short photoperiods confirmed |
| sweep-44:5 | Bouteloua curtipendula / sense_light_nonvisual | m | confirm | quote verbatim (point 2 of the abstract); critical photoperiod "between 14 and 141/2 hours" confirmed |
| sweep-44:2 | Syringa vulgaris / sense_chemical | m | confirm | sentence verbatim but for the page's spacing artefacts ("S. o blata" as returned against "S. o b lata" in the quote); more than 70 % and 'Bright Centennial' confirmed |
| sweep-44:7 | Scolopax minor / absolute_sensitivity | m | requote | value confirmed; the quote is the middle clause of a sentence that opens "Although they have low rod density compared to that of stilts and plovers," and continues "but rank midway between plovers and dowitchers for the b-wave amplitude." |
| sweep-46:13 | Arctotheca calendula / sense_light_nonvisual | m | confirm | clause verbatim in the abstract |
| sweep-46:8 | Hypoxis hemerocallidea / sense_light_nonvisual | m | confirm | sentence verbatim in the abstract |
| sweep-46:10 | Serenoa repens / sense_chemical | m | confirm | sentence verbatim in the introduction |
| sweep-46:9 | Scirpus lacustris / sense_light_nonvisual | m | confirm | sentence verbatim in the abstract (repository page) |
| sweep-47:6 | Circaetus gallicus / fov_h_deg | m | confirm | verbatim opening of the sentence, which continues ", and the blind area above and behind the head reaches maximum width of 100°" |
| sweep-47:9 | Hylotelephium spectabile / sense_light_nonvisual | m | confirm | first sentence verbatim; 0 to 1 d, 2 to 10 d, after 11 d under 20 h confirmed |
| sweep-47:3 | Caladenia crebra / sense_chemical | m | confirm | sentence verbatim in the abstract |
| sweep-47:5 | Polybia occidentalis / colour_vision | m | confirm | last sentence verbatim; CB card discriminated from cards of similar brightness confirmed |
| sweep-48:3 | Mus musculus / fov_h_deg | m | confirm | verbatim in the Figure 6 caption (panel B) |
| sweep-48:2 | Mus musculus / binocular_deg | m | confirm | verbatim in Results, Transformation to visuotopic coordinates; sentence continues "slightly larger than the 30–40° of Dräger and Hubel" |
| sweep-48:4 | Spheniscus humboldti / spectral_range_nm | m | confirm | verbatim in section 3.1.9 (Retina) of a review, cited to ref. 83 (Bowmaker and Martin); already `partial: true` |
| sweep-48:5 | Puffinus puffinus / fov_h_deg | m | confirm | sentence verbatim in the abstract |
| sweep-47:2 | Bothrops atrox / receptor_classes | g | confirm | sentence verbatim; RH1, LWS full length and most of SWS1 confirmed; opsin-inferred, held at `g` already |
| sweep-47:1 | Bothrops jararaca / fovea | m | confirm | sentence verbatim; juvenile ventral-retina sentence confirmed |
| sweep-46:6 | Nereocystis luetkeana / sense_light_nonvisual | m | confirm | clause verbatim; Fv/Fm fell 40% after 60 min and recovered within 8% after a 300-min dim period confirmed |
| sweep-46:5 | Fulmarus glacialis / acuity_cpd | m | confirm | verbatim in Results, Retinal ganglion cell density and spatial resolving power |

**Part (a) rate: 1 error in 20 verifiable records, 5%** (0 unverifiable). The one error is the clause-cut shape audit 5 named (pattern 2), not the summariser rebuild. The newest sweeps, which asked the fetch tool for the sentence verbatim in pieces, run far cleaner than the old batches (34% to 74% in audit 5).

## Part (b): batch recheck

### Batch table

| batch | due | records checked | errors | error rate | unverifiable | status |
|---|---|---|---|---|---|---|
| insects-met (24 on) | 28 | 0 | 0 | n/a | 0 | in progress |
| sweep-15 | 13 | 0 | 0 | n/a | 0 | not started |
| sweep-19 | 19 | 0 | 0 | n/a | 0 | not started |
| sweep-7 | 16 | 0 | 0 | n/a | 0 | not started |
| sweep-17 | 12 | 0 | 0 | n/a | 0 | not started |

Error rate is errors over verifiable records (checked minus unverifiable).

### Records

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| insects-met:24 | Popillia japonica / receptor_classes | m | unverifiable | the doi.org route to the Wiley page answered 429 with an instruction not to retry; no repository copy found by search |
| insects-met:25 | Popillia japonica / behaviour_vision | m | unverifiable | as insects-met:24 |
| insects-met:26 | Perithemis tenera / behaviour_vision | m | confirm | verbatim opening of the abstract sentence (academic.oup.com), which continues "; they also detected more intruders in front of them than from other angles"; distant-against-near vegetation confirmed |
| insects-met:27 | Danaus plexippus / lambda_max_nm | m | unverifiable | Royal Society page returned a fetch error; PMC8548807 served a reCAPTCHA; the Europe PMC REST copy answered 429; the Zenodo and Dryad records carry data files, not the table |
| insects-met:28 | Heliconius erato / lambda_max_nm | m | unverifiable | as insects-met:27 |
| insects-met:29 | Argynnis paphia / lambda_max_nm | m | unverifiable | as insects-met:27 |
| insects-met:30 | Speyeria aglaja / lambda_max_nm | m | unverifiable | as insects-met:27 |
| insects-met:31 | Melitaea athalia / lambda_max_nm | m | unverifiable | as insects-met:27 |
| insects-met:32 | Morpho peleides / lambda_max_nm | m | unverifiable | as insects-met:27 |
| insects-met:33 | Vanessa atalanta / receptor_classes | m | unverifiable | as insects-met:27 |
| insects-met:34 | Apatura ilia / receptor_classes | m | unverifiable | as insects-met:27 |
| insects-met:35 | Heliconiinae / filter_pigments | m | unverifiable | as insects-met:27 |
| insects-met:36 | Eumaeus atala / lambda_max_nm | m | unverifiable | PNAS (doi.org and pnas.org) returned fetch errors; the MIT DSpace record of the published version shows an abstract that names no species and no nm values, so `where: Abstract` looks wrong, but its PDF bitstream returned a fetch error; the string may be in the Significance statement or Results, unchecked |
| insects-met:38 | Manduca sexta / motion | m | requote | values confirmed; the quote writes "cycles/degree" where the abstract writes "cycles deg−1", and the sentence continues with the 4.5 Hz clause |
| insects-met:39 | Manduca sexta / absolute_sensitivity | m | requote | value confirmed; the quote writes "between 1% to 5%" where the abstract writes "between 1 and 5%" |
| insects-met:40 | Heliothis zea / cff_hz | m | confirm | sentence verbatim but for a line-break hyphen on the page ("laboratory- reared"), counted typography |
| insects-met:41 | Hesperiidae / behaviour_vision | m | unverifiable | the BioOne page's permission request timed out; complete.bioone.org served an Incapsula wall; the journals.flvc.org page found is the supplementary material only |
| insects-met:42 | Danaus plexippus / colour_vision | m | confirm | verbatim clause of the abstract sentence beginning "In addition," |
| insects-met:43 | Danaus plexippus / filter_pigments | m | confirm | verbatim clause of the abstract's last sentence; dark orange pigment "distributed heterogeneously in the eye" confirmed (from colour-space modelling) |
| insects-met:44 | Danaus plexippus / acceptance_deg | m | unverifiable | doi.org returned a fetch error and the bioRxiv page's permission request timed out |
| insects-met:45 | Danaus plexippus / motion | m | unverifiable | as insects-met:44 |
| insects-met:46 | Parantica sita / receptor_classes | m | confirm | sentence verbatim in the abstract (journals.biologists.com) |
| insects-met:47 | Bombus (review) / cff_hz | g | unverifiable | the doi.org route answered 429 |
| insects-met:48 | Bombus (review) / acceptance_deg | g | unverifiable | as insects-met:47; the research.fi record carries no abstract |
| insects-met:49 | Bombus (review) / eyes_count | g | unverifiable | as insects-met:48 |
| insects-met:50 | Libellula quadrimaculata / fovea | m | unverifiable | the eje.cz page's permission request timed out; doi.org avoided after two 429s on that host; no copy found by search |
| insects-met:51 | Callonychium petuniae / receptor_classes | m | unverifiable | the Annual Reviews page shows the abstract and references but not Table 1 ("Full text loading..."); a review table row is a secondary citation and should probably carry `partial: true`, as audit 5 ruled for sweep-6:19, once the cited primary source is known |
| insects-met:52 | Solenopsis saevissima / receptor_classes | m | unverifiable | as insects-met:51 |
| sweep-15:1 | Cytisus scoparius / sense_chemical | m | confirm | verbatim opening of the abstract sentence, which continues "with blends dominated by monoterpenes, aromatics, and fatty acid esters"; 56 VOCs confirmed in Results |
| sweep-15:2 | Berteroa incana / sense_light_nonvisual | m | requote | value confirmed; quote is a rendering; page: "Significant reductions in the share of large leaves, leaf stalk length and root biomass were noted for plants growing under 8 kJ UV-BBE." |
| sweep-15:3 | Campsis radicans / diel | m | confirm | verbatim clause of the abstract sentence beginning "Interestingly,"; ~30% w/w confirmed; the abstract says nectar was characterised by time of day but gives no standing-crop figures |
| sweep-15:4 | Ribes uva-crispa / sense_light_nonvisual | m | confirm | verbatim but for an en dash ("15–16 h"); 10-h SD within 2–3 weeks and 20-h LD for 8 weeks confirmed |
| sweep-15:5 | Argynnis paphia / lambda_max_nm | m | confirm | verbatim but for an en dash ("R1–9"); R9 at 615 nm, R1–2, R3–8 and the male differences confirmed (Prevc 2023 master's thesis, Ljubljana) |
| sweep-15:6 | Cuculus poliocephalus / oil_droplets | m | confirm | verbatim in Results, Observation of oil droplets, p. 130 |
| sweep-15:7 | Tilia cordata / sense_chemical | m | requote | the quote is on the page but in the Discussion and is a background sentence that does not support the value; replaced with the abstract's flowering-stage sentence; 09:00–10:00 is a sampling time |
| sweep-15:8 | Dianthus cruentus / sense_chemical | m | confirm | verbatim in the abstract; 24 constituents and compound classes confirmed |
| sweep-15:9 | Dianthus caryophyllus / diel | m | correct | quote verbatim; value said two compounds "drive the rhythm", but the study took one light-period (09:30) and one dark-period (16:30) sample per day, so it shows a light/dark difference, not a rhythm; value rewritten |
| sweep-15:10 | Calluna vulgaris / sense_light_nonvisual | m | confirm | verbatim in the abstract; 12–16 h and above 14°C confirmed |
| sweep-15:11 | Crataegus monogyna / sense_chemical | m | confirm | verbatim fragment of the abstract sentence; porous polymers and GC-MS confirmed; the Pherobase listing not reopened |
| sweep-15:12 | Celastrus orbiculatus / sense_light_nonvisual | m | confirm | sentence verbatim; elevated FR against neutral shade (height, biomass, leaf mass) confirmed |
| sweep-15:14 | Tachycineta bicolor / fovea | m | confirm | verbatim but for "100°" written "100 degree"; bifoveate, long eye, blind area, narrow binocular field confirmed (Dryad page) |
| sweep-19:1 | Raphanus raphanistrum / sense_light_nonvisual | m | requote | value confirmed; quote not on the page; page: "On the other hand, for accessions with facultative vernalization requirements the photoperiod pathway predominates." |
| sweep-19:2 | Rhinella marina / motion | m | confirm | verbatim in the abstract; strip, right hemifield and 1.7 revolutions/min confirmed |
| sweep-19:3 | Castanea sativa / sense_light_nonvisual | m | confirm | verbatim clause of the abstract's last sentence |
| sweep-19:4 | Castanea mollissima / sense_chemical | m | confirm | verbatim clause; 926 compounds and the three above 5% confirmed |
| sweep-19:5 | Asarum heterotropoides / sense_light_nonvisual | m | requote | value confirmed; the quote adds a full stop where the sentence continues "A. heterotropides volatile oil and this is ascribed to upregulation of key genes" |
| sweep-19:6 | Daptrius chimango / acuity_cpd | m | requote | values confirmed; page: "The visual acuity range from 15.08 to 39.83 cycles/degrees." |
| sweep-19:7 | Gallus gallus domesticus / acuity_cpd | m | requote | values confirmed; quote is a rendering of units and order; page sentence now the quote |
| sweep-19:8 | Gallus gallus / acuity_cpd | m | requote | values confirmed; the quote adds a full stop where the sentence continues "compared with 3.794 c/deg in the jungle light group"; source a 2018 master's thesis |
| sweep-19:9 | Gyps fulvus / binocular_deg | m | confirm | verbatim in Results, General topography of the visual field; species pooled per Methods |
| sweep-19:10 | Gyps africanus / binocular_deg | m | confirm | as sweep-19:9 |
| sweep-19:11 | Serinus canaria / spectral_range_nm | m | confirm | verbatim in the abstract; P567, P501, P442, P366 confirmed |
| sweep-19:12 | Caiman crocodilus / tapetum | m | confirm | verbatim on the DFG page, which lists "presence of a retinal tapetum" |
| sweep-19:13 | Helianthus annuus / diel | m | requote | value confirmed; quote not on the page; page: "these plants maintained their directional growth rhythms for several days" |
| sweep-19:15 | Tragopogon hybridus / diel | m | confirm | table row verbatim; T. pratensis 3 a.m. confirmed |
| sweep-19:16 | Nicotiana sylvestris / diel | m | confirm | verbatim fragment; the review cites Loughrin et al. 1991, already `partial: true` |
| sweep-19:17 | Pastinaca sativa / sense_light_nonvisual | m | confirm | verbatim in the abstract (sentence continues "(imperatorin and sphondin)") |
| sweep-19:18 | Lunaria annua / sense_light_nonvisual | m | confirm | verbatim ("This suggested that annual Lunaria is a long-day plant."); 17 of 18, 0 of 20, 13.8 against 26.9 and 29.3 days confirmed |
| sweep-19:19 | Hypochaeris radicata / diel | m | confirm | verbatim clause; 3–7 hours and rain confirmed |
| sweep-19:20 | Hypochaeris radicata / sense_light_nonvisual | m | confirm | verbatim but for an en dash ("one–hour"); Salisbury 1964 and germination sentence confirmed |
