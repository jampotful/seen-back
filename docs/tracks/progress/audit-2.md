# Precision audit 2, 14 October 2026 (sweeps 5 to 31, web and intake files)

Second run of the precision test of `docs/views/research/THOROUGH.md`, by Opus, after `audit-2026-10-14.md` and `recheck-1.md`.

## Sample

Pool: `docs/views/evidence/sweep-*.jsonl` for sweeps 5 to 31 (sweep 23 and 24 have no evidence file; sweep-21 and sweep-25 were rechecked whole in recheck 1 and are left out), the web method files `birds-met`, `herps-met`, `insects-met`, `mammals-met`, and `intake-2` to `intake-8` (the `-failed` files, `reread-1`, `jumper` and `recheck-1-fixed` left out). The 20 records of the first audit and the records retracted in `docs/views/audit/ALL.jsonl` are skipped. Records of fish, sharks, spiders, scorpions, cephalopods, stomatopods and the few with no order are outside the five views and not drawn (59 records).

View by order: insects (the insect orders), birds (the avian orders), mammals, herps (Testudines, Crocodylia, Anura, Caudata, Squamata), plants (orders ending in -ales). Seed 20261014 (`random.Random`), 12 per view without replacement, weight 3 for partial records and 1 otherwise, weight divided by 4 once a file already has three records in the view. 31 of the 60 are partial. An id is `<file>:<line>`.

Each source URL was opened with WebFetch, which returns a summary, so each quote was checked by asking for the exact string and the nearest verbatim sentence; where a page was blocked the record is `unverifiable`. Verdicts: `correct`; `requote` (value right, quote not on the page or stitched); `regrade`; `retarget` (value is on another page or in another work); `retract` (the page does not support the value); `unverifiable`. Corrections are in `docs/views/recheck/recheck-2.jsonl`; no evidence file is edited.

## Results

| # | id | view | taxon / trait | grade | partial | verdict | note |
|---|---|---|---|---|---|---|---|
| 1 | sweep-19:14 | plants | Helianthus annuus / sense_light_nonvisual | m | yes | requote | value confirmed (16L:8D entrainment, eastward anticipation from lights-off, erratic under 30 h); quote is a stitched summary; page: "After several days in a 24-hour T-cycle (16L:8D), plants bent toward the light source during the day" and "reestablished anticipatory nighttime movement that began when lights were turned off" |
| 2 | sweep-9:13 | plants | Arisaema triphyllum / diel | m | no | correct | quote verbatim (hyphenated across a line); six plants, 10 min logging, 0610-1800 pooling and "no obvious temperature pattern" confirmed |
| 3 | sweep-20:1 | plants | Centranthus ruber / sense_chemical | m | yes | correct | all seven compound names on the Pherobase page; 12 entries, Andersson et al. 2002 cited |
| 4 | sweep-20:8 | plants | Chamaecrista fasciculata / diel | m | yes | correct | quote verbatim; "Flowers normally bloom July-September" confirmed |
| 5 | sweep-16:9 | plants | Passiflora foetida / diel | m | yes | correct | quote verbatim in the English abstract; Ptiloglossa tarsata named as main pollinator |
| 6 | sweep-12:4 | plants | Dactylorhiza majalis / sense_chemical | m | yes | requote | quote verbatim, but the value clause "compounds named in later work include p-hydroxybenzyl alcohol and nonanal" is not on the page and names no source; value trimmed to what the page says (alkanes and aldehydes shared, benzenoids and esters taxon-specific) |
| 7 | sweep-13:4 | plants | Ulmus pumila / sense_light_nonvisual | m | yes | correct | quote verbatim; six clones, Florence, chilling and thermal time confirmed |
| 8 | sweep-15:11 | plants | Crataegus monogyna / sense_chemical | m | yes | correct | quote verbatim on the Hutton abstract page; the 62-compound count rests on the Pherobase listing, not checked |
| 9 | sweep-20:5 | plants | Ornithogalum umbellatum / diel | m | yes | correct | quote verbatim ("The petals exhibit photoperiodism, often opening at noon and closing at night or on cloudy days") |
| 10 | sweep-29:8 | plants | Marchantia polymorpha / sense_light_nonvisual | m | yes | correct | quote verbatim; the sentence ends "and temperature"; DOAJ record gives no DOI |
| 11 | sweep-14:1 | plants | Jacobaea vulgaris / sense_light_nonvisual | m | yes | correct | quote verbatim; 55.6% and 13.9%, 150 samples, 20 C confirmed |
| 12 | sweep-11:7 | plants | Athyrium filix-femina / sense_light_nonvisual | m | yes | requote | value confirmed (high germination, marked drop at 1 umol m-2 s-1, more in Athyrium); quote is not on the page; page: "Final germination percentages were generally high" and "decreasing markedly at 1 µmol m-2 s-1, notably in Athyrium" |
| 13 | sweep-29:2 | insects | Gryllus bimaculatus / lambda_max_nm | m | yes | correct | quote verbatim; blue receptors recorded only in the dorsal rim area, which the eye field could say |
| 14 | sweep-15:13 | insects | Colias eurytheme / fov_h_deg | m | yes | requote | 93%, 4.5% and no sex difference confirmed; quote not on the page; page: "The visual field of C. eurytheme is large, encompassing 93% of the spherical space around the butterflies"; DOI 10.1016/j.jinsphys.2005.11.002 |
| 15 | sweep-8:9 | insects | Halyomorpha halys / spectral_range_nm | m | yes | requote | 371/523, 367/519, 14 LEDs 368-743 nm, 743 nm the only non-positive wavelength and the dichromacy conclusion confirmed; quote not on the page; page: "None of the chromatic-adapted ERG recordings resulted in the emergence of a sensitivity peak in the blue spectral range." |
| 16 | intake-2:28 | insects | Paravespula vulgaris / lambda_max_nm | m | no | unverifiable | closed paper; Springer page shows only the abstract (peaks at 340, 430, 535 nm, consistent); Table 1 row needs the PDF; doi.org link blocked at the permission step |
| 17 | insects-met:37 | insects | Callophrys sheridanii / lambda_max_nm | m | no | retarget | the quoted sentence is in the abstract of the bioRxiv preprint v2 (10.1101/2020.04.06.027102), not in the published PNAS text, which (PMC8017955) names neither Callophrys sheridanii nor Celastrina ladon and reports only Eumaeus atala and Arhopala japonica; the preprint measures Ca. sheridanii at 518 +- 3.7 nm in vivo and 519.2 +- 1.1 nm in vitro |
| 18 | intake-5:39 | insects | Solenopsis invicta / new trait | m | no | unverifiable | closed paper (Zool Anz); no reachable page; the column reading (Male, Queen, Major, Minor) is plausible but unchecked |
| 19 | insects-met:4 | insects | Heliconius erato / filter_pigments | m | no | correct | quote verbatim in the JEB Summary (cob.silverchair page); method on the page is eye glow under orthodromic illumination, not microspectrophotometry |
| 20 | insects-met:24 | insects | Popillia japonica / receptor_classes | m | no | unverifiable | Wiley page blocked at the permission step; no other copy found before the search budget ran out |
| 21 | sweep-31:1 | insects | Deilephila elpenor / interommatidial_deg | m | yes | correct | Table 1 row verbatim (+- for ±); delta-phi column has no unit on the page, defined as the mean angular separation of a cone axis from its six neighbours |
| 22 | sweep-12:10 | insects | Chauliognathus pulchellus / spectral_range_nm | m | yes | requote | three types with peaks near 360, 450 and 520-530 nm and the 3 degree acceptance angle confirmed; quote not on the page; page: "The retinula cells are of three spectral types with peaks near 360, 450 and 520--530 nm." |
| 23 | sweep-11:15 | insects | Lymantria xylina / interommatidial_deg | m | yes | requote | 3.49 and 3.62 confirmed; quote is a rendering; page: "The inter-ommatidial angle is 3.49 ± 0.27° for males and 3.62 ± 0.25° for females"; counts are 7752.83 ± 119.87 and 7062.17 ± 42.33 |
| 24 | sweep-22:6 | insects | Heliconius erato cyrbia / interommatidial_deg | m | yes | requote | the preprint gives 0.379 ± 0.003 cpd, not 0.378 ± 0.004; the quote string is not on the page; 1/(2 x 0.379) = 1.32, so 1.3 degrees stands; the preprint derives the angle as (23818/n)^0.5 from the ommatidia count, so this is a count-based estimate; the published Biology Letters text (PMC10716659) has no morphological value |
| 25 | sweep-15:6 | birds | Cuculus poliocephalus / oil_droplets | m | yes | correct | quote verbatim in Results; the Table II row is OCR-garbled and the Discussion groups the Little Cuckoo with birds rich in pale green droplets, so the paper may disagree with itself |
| 26 | sweep-6:16 | birds | Podiceps cristatus / binocular_deg | m | no | correct | Table 1 values 24, 143, 167, 50, 310 confirmed (rows by trait, columns by species); skull-model estimate, as the method says |
| 27 | sweep-19:10 | birds | Gyps africanus / binocular_deg | m | yes | correct | quote verbatim; two birds per species, pooled, within 5 deg, blind areas 50 and 74 confirmed |
| 28 | sweep-11:10 | birds | Sturnella magna / acuity_cpd | m | yes | correct | page: "Our estimate of maximum spatial resolving power was 10.3 ± 0.3 cycles/degree"; 32,863, 10.2 mm, 32.5 and 4.3 deg confirmed |
| 29 | sweep-6:32 | birds | Selasphorus platycercus / spectral_range_nm | m | no | requote | the quote is from a news page, not the cited PNAS page, and the source lacks title and DOI; paper is "Wild hummingbirds discriminate nonspectral colors", 10.1073/pnas.1919377117; Princeton news page: "hummingbirds readily distinguished ultraviolet+green from pure ultraviolet or pure green"; PNAS page itself returned a fetch error |
| 30 | intake-3:40 | birds | Grus americana / lambda_max_nm | m | no | correct | quote verbatim in the abstract (USGS record); in vitro expression and reconstitution |
| 31 | sweep-6:10 | birds | Sterna striata / colour_vision | m | no | regrade | quote is a rewording; page: "The Caspian tern (Hydroprogne caspia) and White-fronted tern (Sterna striata), however, were found to have VSs, suggesting an evolutionary reversion to the ancestral state within Sternidae."; SWS1 sequence tuning sites predict the pigment and do not measure it (BRIEF: grade and method say so), the same evidence graded g for Morus serrator (sweep-13:10) and Meliphagidae (recheck 1), so m becomes g |
| 32 | sweep-19:9 | birds | Gyps fulvus / binocular_deg | m | yes | correct | quote verbatim; pooled values as the record says |
| 33 | intake-8:6 | birds | Strix aluco / lambda_max_nm | m | no | pending | not reached: WebSearch budget ran out at record 33 |
| 34 | intake-4:30 | birds | Grus americana / eye_movement | m | no | pending | not reached: WebSearch budget ran out at record 33 |
| 35 | intake-8:15 | birds | Bubo virginianus / cff_hz | m | no | correct | abstract: "Scotopic fusion frequency was approximately 16 Hz." (archive.org copy); four owls, eight retinae, acepromazine and ketamine confirmed |
| 36 | sweep-12:8 | birds | Platycercus elegans / lambda_max_nm | m | yes | requote | 365, 440, 509, 567 and rod 510 nm, six P. e. adelaidae birds confirmed; quote not on the page; page: "Indeed, all five pigments peak at longer wavelengths than expected."; DOI 10.1242/jeb.094136; the SWS2 value rests on one cell and the SWS1 365 nm is an in vitro expression value |
| 37 | intake-7:27 | mammals | Camelus dromedarius / tapetum | m | no | pending | not reached: WebSearch budget ran out at record 33 |
| 38 | sweep-29:4 | mammals | Oryctolagus cuniculus / tapetum | m | yes | pending | not reached: WebSearch budget ran out at record 33 |
| 39 | intake-6:18 | mammals | Myocastor coypus / fovea | m | yes | pending | not reached: WebSearch budget ran out at record 33 |
| 40 | intake-8:35 | mammals | Capra hircus / tapetum | m | yes | pending | not reached: WebSearch budget ran out at record 33 |
| 41 | intake-5:31 | mammals | Capra hircus / fov_h_deg | m | no | pending | not reached: WebSearch budget ran out at record 33 |
| 42 | intake-6:16 | mammals | Myocastor coypus / pupil_shape | m | yes | pending | not reached: WebSearch budget ran out at record 33 |
| 43 | intake-3:3 | mammals | Bos taurus / acuity_cpd | m | no | pending | not reached: WebSearch budget ran out at record 33 |
| 44 | intake-3:5 | mammals | Bos taurus / fov_h_deg | m | no | pending | not reached: WebSearch budget ran out at record 33 |
| 45 | intake-5:24 | mammals | Bos taurus / lambda_max_nm | m | no | pending | not reached: WebSearch budget ran out at record 33 |
| 46 | sweep-27:9 | mammals | Equus caballus / receptor_classes | m | yes | pending | not reached: WebSearch budget ran out at record 33 |
| 47 | mammals-met:7 | mammals | Kerodon rupestris / pupil_shape | m | no | pending | not reached: WebSearch budget ran out at record 33 |
| 48 | intake-7:24 | mammals | Bos taurus / colour_vision | m | no | pending | not reached: WebSearch budget ran out at record 33 |
| 49 | herps-met:19 | herps | Bufo bufo / lambda_max_nm | m | no | pending | not reached: WebSearch budget ran out at record 33 |
| 50 | sweep-6:5 | herps | Trachemys scripta elegans / lambda_max_nm | m | no | pending | not reached: WebSearch budget ran out at record 33 |
| 51 | intake-8:28 | herps | Triturus cristatus / depth_cue | m | no | pending | not reached: WebSearch budget ran out at record 33 |
| 52 | sweep-19:2 | herps | Rhinella marina / motion | m | yes | pending | not reached: WebSearch budget ran out at record 33 |
| 53 | sweep-7:12 | herps | Bufo japonicus / motion | m | no | pending | not reached: WebSearch budget ran out at record 33 |
| 54 | herps-met:23 | herps | Dryophytes cinereus (as Hyla cinerea) / receptor_classes | g | no | pending | not reached: WebSearch budget ran out at record 33 |
| 55 | intake-3:50 | herps | Anura / pupil_shape | g | no | pending | not reached: WebSearch budget ran out at record 33 |
| 56 | herps-met:17 | herps | Rana temporaria / lambda_max_nm | m | no | pending | not reached: WebSearch budget ran out at record 33 |
| 57 | sweep-6:35 | herps | Trachemys scripta elegans (as Pseudemys scripta elegans) / acuity_cpd | m | no | pending | not reached: WebSearch budget ran out at record 33 |
| 58 | sweep-17:14 | herps | Chelonia mydas / lambda_max_nm | m | yes | pending | not reached: WebSearch budget ran out at record 33 |
| 59 | sweep-17:12 | herps | Chelonia mydas / fovea | m | yes | pending | not reached: WebSearch budget ran out at record 33 |
| 60 | sweep-7:10 | herps | Bufo bufo / motion | m | no | pending | not reached: WebSearch budget ran out at record 33 |

## Error rate

Checked 34 of 60; verifiable 31; wrong (requote, regrade, retarget or retract) 12: **39%**.

By batch (wrong / verifiable sampled):

| batch | sampled | verifiable | wrong | rate |
|---|---|---|---|---|
| herps-met | 3 | 0 | 0 | 0% |
| insects-met | 3 | 2 | 1 | 50% |
| intake-2 | 1 | 0 | 0 | 0% |
| intake-3 | 4 | 1 | 0 | 0% |
| intake-4 | 1 | 0 | 0 | 0% |
| intake-5 | 3 | 0 | 0 | 0% |
| intake-6 | 2 | 0 | 0 | 0% |
| intake-7 | 2 | 0 | 0 | 0% |
| intake-8 | 4 | 1 | 0 | 0% |
| mammals-met | 1 | 0 | 0 | 0% |
| sweep-6 | 5 | 3 | 2 | 67% |
| sweep-7 | 2 | 0 | 0 | 0% |
| sweep-8 | 1 | 1 | 1 | 100% |
| sweep-9 | 1 | 1 | 0 | 0% |
| sweep-11 | 3 | 3 | 2 | 67% |
| sweep-12 | 3 | 3 | 3 | 100% |
| sweep-13 | 1 | 1 | 0 | 0% |
| sweep-14 | 1 | 1 | 0 | 0% |
| sweep-15 | 3 | 3 | 1 | 33% |
| sweep-16 | 1 | 1 | 0 | 0% |
| sweep-17 | 2 | 0 | 0 | 0% |
| sweep-19 | 4 | 3 | 1 | 33% |
| sweep-20 | 3 | 3 | 0 | 0% |
| sweep-22 | 1 | 1 | 1 | 100% |
| sweep-27 | 1 | 0 | 0 | 0% |
| sweep-29 | 3 | 2 | 0 | 0% |
| sweep-31 | 1 | 1 | 0 | 0% |

## Where this run stopped

The shared WebSearch allowance ran out at record 33 (intake-8:6, Strix aluco), after 34 records had been opened. Records 33, 34 and 37 to 60 (26 records) are `pending`; the run stopped at once, as instructed, and did not retry. Three opened records are `unverifiable` (two closed papers with no reachable page, one Wiley page blocked at the permission step). `doi.org` links were refused at the permission step every time; a publisher or repository page found by search opened in their place.

## Batches due a full recheck (from the sampled records so far)

By the THOROUGH rule (over 5% wrong, or two or more wrong records): sweep-6, sweep-8, sweep-11, sweep-12, sweep-15, sweep-19, sweep-22 and insects-met. None has been rechecked yet; a resumed run should finish records 33 to 60 first, then recheck those batches whole.

## Patterns

1. Summariser renderings logged as quotes, again. Eleven of the twelve wrong records are `requote`: the value is on the page, the quote is not. Every one carries "read through a summariser" in `where` or `note`. A quote written by a summariser is not a quote; the sweeps should ask the fetch tool for the verbatim sentence and log that, or log the quote field empty.
2. Preprint and published text drift. Two records cite one version and quote another: insects-met:37 quotes the bioRxiv abstract under the PNAS DOI, and the species is absent from the published paper; sweep-22:6 quotes a figure (0.378) that is on neither version. When a preprint is read, the record must cite the preprint.
3. Opsin-sequence predictions graded m at species rank (sweep-6:10) while the same evidence is g elsewhere. The rule from recheck 1 holds: predicted pigment class is g, never m.
4. Value clauses that outrun the page: sweep-12:4 adds compounds "named in later work" with no source; sweep-6:32 quotes a news page under the paper's address with no title or DOI.
5. The records that were right are almost all abstract-page or table reads where the logger copied a sentence (Springer, Wiley-free repositories, Wikipedia, Pherobase). Verbatim copying from a page the logger could see was reliable; summarised PDFs were not.
