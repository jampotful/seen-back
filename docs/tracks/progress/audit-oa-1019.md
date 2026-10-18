# OA audit 1019, 18 October 2026

Scope: the 2,898 evidence lines that branch `oa-ctl-1018` at `cfa41e56` adds to `docs/views/evidence/` (oa-1 649, oa-2 815, oa-5 47, oa-6 118, oa-9 400, oa-10 773, oa-11 96), compared with `main` at `a429301`. The lines were listed in `git diff --unified=0 origin/main cfa41e56 -- docs/views/evidence/` order (files oa-1, oa-10, oa-11, oa-2, oa-5, oa-6, oa-9; lines in file order), then `random.seed(1019)` and `random.sample(lines, 40)`. The earlier audit used seed 1018; its report and verdicts were not read. Because ten of the forty could not be checked (Coverage, below), ten more were drawn with `random.seed(10191)` from the 2,858 lines outside the first draw; they are reported separately, as audit 31 reported its extension.

## Sample (written before any record was checked)

First draw: oa-1:5298, oa-10:712, oa-10:229, oa-1:5572, oa-10:336, oa-2:3626, oa-9:1, oa-2:4006, oa-9:277, oa-10:286, oa-10:559, oa-2:3338, oa-2:3381, oa-10:526, oa-10:415, oa-10:275, oa-10:421, oa-1:5584, oa-9:176, oa-11:12, oa-2:3472, oa-1:5357, oa-10:109, oa-2:3618, oa-10:533, oa-2:3732, oa-9:179, oa-2:3737, oa-1:5337, oa-1:5652, oa-2:3821, oa-1:5799, oa-6:748, oa-10:129, oa-2:3957, oa-9:274, oa-2:3431, oa-2:3473, oa-2:3832, oa-10:43. They come from 20 papers.

Extension: oa-10:494, oa-2:4117, oa-9:327, oa-2:3789, oa-9:219, oa-1:5581, oa-9:370, oa-2:3527, oa-6:675, oa-2:3566.

## Method

Texts came from the `oa` job with this audit's own key (kept in `/tmp/oa-audit-1019` with the texts, outside the repository): branch `run/oa/audit-1019`, made from `main` with only `ci/oa/pub.pem` and a cut `ci/oa/list.jsonl` changed; commits `056e5af` (the 20 papers, runs 15), `992ccac` and `7bda324` (oa-10 entry 25 again, runs 16 and 17) `2848010` (the extension's five new papers and entry 25 a fourth time, runs 18) and `c547cb6` (entry 25 a fifth time after a 15-minute gap, runs 20). Every text decrypted with no checksum mismatch. For each record: `python3 -I tools/views/quotecheck.py` on its text, then the sentence or table row read in place (table rows in the `=== LAYOUT ===` part where the plain part breaks columns), with the column heads, captions and footnotes that define the value.

The rules applied are those of the launch prompt and `docs/tracks/prompts/oa-read.md`. Grade: `m` for a value on the record's own taxon, measured in this paper or cited, or for the group the record names when the passage states it for that group as a whole (typical members, and a common or genus name for the study animal, included: `docs/views/audit/SAMPLE.md`, "The rule decided"); `g` for a taxon mismatch (a subset or one species standing for a group, a wider group, a relative) and for a value predicted or presumed rather than measured (BRIEF line 170). `partial` for anything cited, compiled or from a review, and for a value read off a figure; a value stated in a legend's text from the paper's own data is not partial. A quote is verbatim, cut only with a marked "…", one sentence or one table row (or whole consecutive sentences), and holds the value. Typographic differences (glyphs the PDF font lost, spacing, quotation marks) count as confirm, as in audit 31. Errors are `requote`, `correct` and `retract`; metadata faults are listed and not counted.

## Verdicts, first draw

| # | id (file:line) | taxon / trait | value | grade | quotecheck | verdict | reason |
|---|---|---|---|---|---|---|---|
| 1 | oa-1:5298 | Amphisbaena infraorbitale / lambda_max_nm | UVS | g | verbatim | confirm | Table S4 layout row exact (caption: all λmax predicted from sequence except values in parentheses; UVS = c. 360 nm); `g` for a prediction, no `partial` for the paper's own estimate |
| 2 | oa-10:712 | Pelecyphora strobiliformis / sense_light_nonvisual | 1 | m, partial | no text | unverifiable | Flores et al. 2011 not returned (see Coverage). Checks without the text pass: value is the RLG column of the quoted row (74, 0, 1); References names Flores et al. (2006) and `partial` is set |
| 3 | oa-10:229 | Echinocereus enneacanthus / sense_light_nonvisual | 1 | m | no text | unverifiable | Flores et al. 2011 not returned (see Coverage). Checks without the text pass: RLG column (42, 0, 1); "New data", no `partial` |
| 4 | oa-1:5572 | Apis mellifera / diel | most active at high light levels | m, partial | verbatim | confirm | Table A1 layout row exact; the caption defines the column as the light level the insect is most active at (H = high); compiled from four cited studies, so `m` with `partial` |
| 5 | oa-10:336 | Myrtillocactus geometrizans / sense_light_nonvisual | 0 | m | no text | unverifiable | Flores et al. 2011 not returned (see Coverage). Checks without the text pass: Darkness column (63, 0, 1); "New data" |
| 6 | oa-2:3626 | birds with violet-sensitive SWS1 pigments / lambda_max_nm | [400, 420] | m, partial | fail (typographic) | confirm | Fig. 5 legend; the text prints "lmax" and "(400 –420 nm)" (λ lost in the PDF font), a typographic difference and the reason quotecheck fails; the legend states the range for the birds whose SWS1 is violet as a whole; review, `partial` right |
| 7 | oa-9:1 | Gymnophiona / pupil_shape | non-elongated, circular | g | verbatim | confirm | verbatim (the "…" stands where the preprint prints line number 274, no word cut); nine species stand for the whole order, so `g`; the paper's own scoring of photographs, so no `partial` |
| 8 | oa-2:4006 | Plexippus validus / lambda_max_nm | 535 | m, partial | table (typographic) | confirm | both cuts inside one sentence and marked; "1978 )" against "1978)" is typographic; ERG value of the named species cited from Hardie and Duelli 1978, so `m` with `partial` |
| 9 | oa-9:277 | Lomariopsidaceae / sense_chemical | tested species did not appear to produce or r... | g, partial | verbatim | confirm | verbatim whole sentence; "tested representatives" stand for the family, so `g`; meta-analysis of published studies, `partial` right |
| 10 | oa-10:286 | Gymnocalycium monvillei / sense_light_nonvisual | 1 | m, partial | no text | unverifiable | Flores et al. 2011 not returned (see Coverage). Checks without the text pass: RLG column (20, 0, 1); Gurvich et al. (2008), `partial` set |
| 11 | oa-10:559 | Ferocactus flavovirens / sense_light_nonvisual | 1 | m, partial | no text | unverifiable | Flores et al. 2011 not returned (see Coverage). Checks without the text pass: RLG column (80, 0, 1); Rojas-Aréchiga et al. (1997), `partial` set |
| 12 | oa-2:3338 | Australian crocodiles / acuity_cpd | 8 | m, partial | verbatim | confirm | verbatim, cut at the end marked; the passage gives ~8 cycles/degree for juvenile Australian crocodiles as a group (Nagloo et al. 2016, whose reference names C. porosus and C. johnstoni); cited, `m` with `partial` by the group rule |
| 13 | oa-2:3381 | most flying insects / polarization | ocelli detect polarized light | m, partial | verbatim | confirm | verbatim whole sentence; a statement about most flying insects as a group (typical members), cited [38-40], so `m` with `partial`. `doi` field holds the Dryad dataset DOI (metadata row) |
| 14 | oa-10:526 | Eriosyce occulta / sense_light_nonvisual | 0.625 | m | no text | unverifiable | Flores et al. 2011 not returned (see Coverage). Checks without the text pass: 75 / (75 + 45) = 0.625; "New data" |
| 15 | oa-10:415 | Astrophytum myriostigma / sense_light_nonvisual | 0.878 | m | no text | unverifiable | Flores et al. 2011 not returned (see Coverage). Checks without the text pass: 86 / (86 + 12) = 0.878; "New data" |
| 16 | oa-10:275 | Gymnocalycium bruchii / sense_light_nonvisual | 38 | m, partial | no text | unverifiable | Flores et al. 2011 not returned (see Coverage). Checks without the text pass: Light column (38, 0, 1); Gurvich et al. (2008), `partial` set |
| 17 | oa-10:421 | Cereus hankeanus / sense_light_nonvisual | 1 | m | no text | unverifiable | Flores et al. 2011 not returned (see Coverage). Checks without the text pass: RLG column (94, 0, 1); "New data" |
| 18 | oa-1:5584 | Saturnia pavonia / diel | most active at low light levels | m, partial | verbatim | confirm | Table A1 layout row exact; L = most active at low light; compiled, `m` with `partial` |
| 19 | oa-9:176 | Asplenium cuneifolium / sense_chemical | responds to antheridiogen from a Pteridium aq... | m | verbatim | confirm | Table 1 row exact; the paper's own cultivation assay; conditions match the Methods (Bold's medium, 25 °C, 12 h : 12 h, 65 µmol m-2 s-1, weekly for 12 wk) |
| 20 | oa-11:12 | Corvus macrorhynchos / binocular_deg | 48.4 | m | verbatim | confirm | same sentence, both cuts marked; 48.4 ± 1.6 deg, four birds, eyes at rest; own measurement |
| 21 | oa-2:3472 | marsupials (metatherians) / oil_droplets | colourless oil droplets | m, partial | verbatim | confirm | verbatim whole sentence; stated for marsupials as a whole; review, `partial` right |
| 22 | oa-1:5357 | Natriciteres sylvatica / lambda_max_nm | 560 | g | verbatim | confirm | Table S5 layout row exact; predicted (no value in parentheses), so `g` |
| 23 | oa-10:109 | Anthidium manicatum / fovea | acute zone (frontal), organized like those of... | m | verbatim | requote | the sentence logged says only that A. manicatum showed "a similar organization"; neither "acute zone" nor the frontal location is in it, so the quote does not hold the value. The value stands on the sentence before it; new quote in the recheck file |
| 24 | oa-2:3618 | birds / receptor_classes | 4 | m, partial | verbatim | confirm | verbatim whole sentence; four spectral classes of single cone stated for birds as a whole; review, `partial` right |
| 25 | oa-10:533 | Eriosyce subgibbosa castanea / sense_light_nonvisual | 81 | m | no text | unverifiable | Flores et al. 2011 not returned (see Coverage). Checks without the text pass: Light column (81, 0, 1); "New data"; printed "Eriosyce subgibbosa ssp. castanea", logged without "ssp." |
| 26 | oa-2:3732 | rat / diel | nocturnal | m, partial | verbatim | confirm | sentence start, cut at the end marked; "the nocturnal rat" names the record's (common-name) taxon; review, `m` with `partial` by the common-name rule |
| 27 | oa-9:179 | Asplenium septentrionale / sense_chemical | responds to antheridiogen from a Pteridium aq... | m | verbatim | confirm | Table 1 row exact; own cultivation assay |
| 28 | oa-2:3737 | ground squirrel / receptor_classes | 2 | m, partial | verbatim | confirm | sentence start, cut at the end marked; two cone types in the ground squirrel, formally tested; review, `m` with `partial` |
| 29 | oa-1:5337 | Python regius / lambda_max_nm | 551 | m, partial | verbatim | confirm | Table S5 layout row "560 (551 )"; the parenthesised value is measured (MSP or in vitro) and footnote 2 is Sillman et al. 1999, so `m` with `partial` |
| 30 | oa-1:5652 | Pavo cristatus / lambda_max_nm | VS | m, partial | verbatim | confirm | verbatim caption sentence naming the peafowl as the VS example, cited [68]; `m` with `partial`. The copy's reference list is empty, so the method "microspectrophotometry" is not checkable here (uncounted) |
| 31 | oa-2:3821 | galegoid clade / sense_light_nonvisual | long-day plants (flowering), in general | m, partial | verbatim | confirm | sentence start, cut marked; "in general" species of the galegoid clade are long-day plants, the typical-member rule; cited, `partial` right |
| 32 | oa-1:5799 | Canis lupus familiaris / cone_density_mm2 | 26000 | m | verbatim | confirm | German sentence verbatim, as the thesis prints it (4.2.6 Chihuahua); 26000 receptors per mm² is the value the sentence gives (Tab. 1's 24500 is noted); own count, `m` |
| 33 | oa-6:748 | Pythonidae and Boidae (some members) / sense_infrared | detect IR with 5–10 fold lower sensitivity th... | g, partial | verbatim | confirm | verbatim whole sentence; "some members" of two families is a subset standing for them, so `g`; cited refs 3, 12, 13, `partial` right |
| 34 | oa-10:129 | Quercus ithaburensis / sense_light_nonvisual | significantly higher root fibrosity under NS1... | m | verbatim | confirm | verbatim abstract sentence; conditions match the Methods (17 h, 150 ± 10 µmol m-2 s-1) and Table 1 (R:FR 8.2 and 5.7) |
| 35 | oa-2:3957 | humans / acuity_cpd | 60 | m, partial | verbatim | confirm | verbatim whole sentence; humans 60 cpd cited to Campbell and Gubisch [76]; `m` with `partial` by the common-name rule |
| 36 | oa-9:274 | Culcitaceae / sense_chemical | tested species did not appear to produce or r... | g, partial | verbatim | confirm | same sentence as oa-9:277; `g` and `partial` right |
| 37 | oa-2:3431 | Panthera leo bleyenberghi / tapetum | 16.041 | m | verbatim | confirm | Table 4 row, the skipped columns marked with "…"; TLW2 is the 18th of 19 columns, 16.041 ± 0.7 mm in the male; own measurement on one animal |
| 38 | oa-2:3473 | monotremes / oil_droplets | colourless oil droplets | m, partial | verbatim | confirm | same sentence as oa-2:3472, stated for monotremes as a whole |
| 39 | oa-2:3832 | phaseoloid clade / sense_light_nonvisual | cryptochrome gene CRY1 duplicated | g, partial | verbatim | confirm | verbatim whole sentence; a gene duplication predicts a photoreceptor and does not measure one (BRIEF line 170), so `g`; cited Platten et al. 2005b, `partial` right |
| 40 | oa-10:43 | Bothrops jararaca / fovea | rods concentrated in a dorsal area | m | verbatim | confirm | verbatim legend sentence; the sentence before names B. jararaca, whose juveniles it describes; stated in the legend text and the paper's own maps, so no `partial` |

## Verdicts, extension (seed 10191)

| # | id (file:line) | taxon / trait | value | grade | quotecheck | verdict | reason |
|---|---|---|---|---|---|---|---|
| E1 | oa-10:494 | Echinopsis leucantha / sense_light_nonvisual | 80 | m | no text | unverifiable | Flores et al. 2011 not returned (see Coverage). Checks without the text pass: Light column (80, 14, 0.851; 80 / 94 = 0.851); "New data" |
| E2 | oa-2:4117 | Pteridophyta / sense_light_nonvisual | phototropins present | g | verbatim | confirm | verbatim whole sentence ("Pterydophytes" as printed); a database search finds phot sequences, which predict a photoreceptor and do not measure one, so `g`; the paper's own search, no `partial` needed |
| E3 | oa-9:327 | Ipomopsis aggregata / diel | alpha-pinene emission rate tripled from day t... | m | fail (typographic) | confirm | the PDF prints "a-pinene" (α lost in the font), a typographic difference and the reason quotecheck fails; whole sentence; own headspace sampling (Results: day-night increase in I. aggregata, F1,30 = 11.46, P = 0.0020) |
| E4 | oa-2:3789 | ark clams / eye_type | lens-less compound eyes | m, partial | verbatim | confirm | verbatim, the legend's two sentences whole; lens-less compound eyes stated for ark clams as a group; review, `m` with `partial` by the group rule |
| E5 | oa-9:219 | Goniopteris curta / sense_chemical | no response to antheridiogen from a conspecif... | m | verbatim | confirm | Table 1 row exact; column "Response to self" = No; own cultivation assay |
| E6 | oa-1:5581 | Periplaneta americana / cff_hz | [25, 60] | m, partial | verbatim | confirm | Table A1 layout row exact; CFF 25-60 Hz; compiled, `m` with `partial` |
| E7 | oa-9:370 | Gallus gallus and Columba livia / lambda_max_nm | 467 | m, partial | fail (typographic) | confirm | pieces of one sentence, cuts marked; quotecheck fails only on "( Gallus gallus )" spacing and "lmax" for λ max; the sentence gives the four λmax values for chicken and pigeon together, the two species the record names; cited [4,5], `partial` right |
| E8 | oa-2:3527 | Lemur / lambda_max_nm | 558 | g, partial | table | confirm | Table 1 row (558, 543 for the ring-tailed lemur); the text says Tan & Li (1999) estimated both λmax values from allele sequences, so `g`; review, `partial` right |
| E9 | oa-6:675 | Theopropus elegans / lambda_max_nm | 525 | m | verbatim | confirm | Table 1 row exact, in the T. elegans block (the row carries no name, as printed); template λmax fitted to the paper's own ERG, `m` |
| E10 | oa-2:3566 | Epomophorus gambianus / receptor_classes | L cones but no S cones | m, partial | fail (typographic) | confirm | pieces of one sentence, cuts marked; quotecheck fails only on the spaces before commas; cited Muller et al. 2007, `m` with `partial` |

## Error count and rate

| | sampled | verifiable | requote | correct | retract | errors | rate | exact 95% interval |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| first draw (seed 1019) | 40 | 30 | 1 | 0 | 0 | 1 | 3.3% | 0.1% to 17.2% |
| with the extension | 50 | 39 | 1 | 0 | 0 | 1 | 2.6% | 0.1% to 13.5% |

The interval is Clopper-Pearson, the one audit 39 used. The point estimate is under 5%, and the upper end of the interval is above it in both rows, so this many records cannot show the pool is under 5%. No value, taxon, grade or `partial` flag was found wrong in the 39 verifiable records; the one error is a quote. One verdict depends on reading: `oa-audit.md` lists "a figure" among the sources that need `partial`, while `oa-read.md` limits that to a value read off a figure and not stated in text. oa-10:43 is a legend sentence describing the paper's own maps, confirmed here under the second reading; under the first it is a `correct` (partial missing), which makes 2 errors: 6.7% of 30 (0.8% to 22.1%) and 5.1% of 39 (0.6% to 17.3%).

## Metadata and other faults (not counted)

| id | fault |
|---|---|
| oa-2:3381 | `source.doi` is the Dryad dataset DOI (10.5061/dryad.nzs7h44v8); the article read is PLoS ONE 17(9): e0257779, doi 10.1371/journal.pone.0257779, which the `url` already points at. The note says so, and the field still carries the dataset's DOI |
| oa-1:5652 | the Europe PMC copy has an empty reference list, so ref [68] and the record's method ("cited microspectrophotometry") cannot be checked against this text |
| oa-2:4117 | the note says "so graded i" and then "Graded g by the control room"; the grade field is `g`, so the first clause is stale |
| oa-2:3431, oa-9:327, oa-1:5572, oa-1:5584, oa-10:43 | trait keys used past their listed values: a tapetum width in mm under `tapetum` (a string key for the layer and its kind), a floral-scent day-night rhythm and "most active at high/low light levels" under `diel`, a dorsal rod concentration under `fovea`. The values match their quotes, so none is counted |
| oa-2:3626, oa-9:327, oa-9:370, oa-2:3566 | quotes that fail `quotecheck.py` on typography alone (the readers restored λ and α where the PDF prints "lmax" and "a-pinene", and spaced brackets and commas). `oa-read.md` asks for the text as the file holds it and for failing quotes to be fixed before commit |

## Coverage

Flores et al. 2011 (oa-10 entry 25, doi 10.1016/j.envexpbot.2010.10.025) holds 592 of the 2,898 lines, 20% of the pool, and 11 of the 50 sampled records. The readers' runs (2, 8 and 13) read the CONICET Digital submitted version; in this audit's five runs (21:33 to 22:09 UTC) the CONICET handle gave no answer (status 0) and ScienceDirect returned 403, and this session's proxy refuses both hosts. Those 11 rows pass every check that needs no text: each value is the column its `units` names in the quoted row, the computed RLG equals Gl / (Gl + Gd) where the counts allow the check, `partial` is set on exactly the rows whose References column names another study, and all are `m`. Their quotes are unverified. A rerun of `run/oa/audit-1019` with the list cut to oa-10 entry 25, once the repository answers, closes this; the eleven rows are oa-10:712, 229, 336, 286, 559, 526, 415, 275, 421, 533 and 494.

## Fault patterns

1. The one error is a quote that leans on the sentence before it. oa-10:109 quotes "In A. manicatum and B. terrestris, induction of a fluorescent pseudopupil (Materials and Methods) confirmed a similar organization", while "acute zone", the frontal location and the two species compared all sit in the previous sentence. The value is right; the quote cannot show it.
2. Every other verified quote is in its paper, cut only at marked points and inside one sentence or one table row. Four fail the mechanical check on typography (listed above), which a reader following `oa-read.md` would have caught before committing.
3. Grades hold under the rule as given. The eleven sampled records the control room set to `m` (oa-2:3626, 3338, 3381, 3472, 3473, 3618, 3732, 3737, 3821, 3957, 3789) each state the value for the group the record names or name the animal by its common name ("the nocturnal rat", "humans"). Every `g` in the sample is either a prediction from sequence (Simões et al. Tables S4 and S5, CRY1 in the phaseoloid legumes, phot sequences in ferns, Tan & Li's lemur alleles) or a subset standing for its group (nine caecilians for Gymnophiona, "tested representatives" for a fern family, "some members" of Pythonidae and Boidae).
4. `partial` is right on all 39 verifiable records under `oa-read.md`'s figure rule (oa-10:43 is the one that turns on the reading, above): set on the thesis compilation rows, the review rows and the cited sentences inside research papers, and absent on each paper's own data.
5. The open risk is coverage. One paper is a fifth of the pool, and its rows could not be read against the text here.

## Rows written

`docs/views/recheck/recheck-oa-1019.jsonl`: one row, `requote` of oa-10:109 in the recheck-5 schema (the full corrected record with `unit`, `supersedes`, `action` and `reason`), with `field`, `old` and `new` added for the quote. The new quote takes the two consecutive sentences from their starts with three marked cuts (36 words, 39 with the cut marks, which `check.py` counts) and passes `quotecheck.py` as verbatim and `check.py` with no problem; the note now states the frontal location the new quote's "this" refers to (BRIEF puts a `fovea` location in `note`), and the value is unchanged. No evidence file was edited, and no paper text or key is in the repository.
