# Audit of the OA reading pass oa-ctl-1018, 18 October 2026

Scope: the 2,802 evidence lines that branch `oa-ctl-1018` adds to `docs/views/evidence/oa-1`, `oa-2`, `oa-5`, `oa-6`, `oa-9` and `oa-10` `.jsonl` (diff against `main`). Sample: all added lines in diff order (oa-1, oa-10, oa-2, oa-5, oa-6, oa-9, each in line order), then Python `random.seed(1018)` and `random.sample(lines, 40)`.

Sample (file:line, drawn before any record was checked): oa-2:3506, oa-9:228, oa-2:3509, oa-1:5568, oa-9:370, oa-10:255, oa-9:15, oa-10:650, oa-10:254, oa-10:117, oa-2:4050, oa-2:3576, oa-10:238, oa-1:5621, oa-2:3482, oa-2:4100, oa-9:351, oa-10:75, oa-1:5750, oa-6:773, oa-2:3471, oa-1:5370, oa-6:762, oa-2:3650, oa-1:5794, oa-9:32, oa-9:37, oa-2:3480, oa-2:3384, oa-1:5597, oa-10:174, oa-1:5371, oa-10:655, oa-9:143, oa-10:688, oa-2:3879, oa-2:3891, oa-10:405, oa-1:5219, oa-2:3373.

## Content judged and rules applied

The sample was drawn at commit 51a4456. During the audit the control room pushed a second grade pass (cf645cb, "OA pass, second grade pass after audits oa-1018-b and -c"), which keeps every line in place. Each sampled position was judged as it stands at **cf645cb**; nine of the 40 lines changed there (oa-2:3506, 3509 and 3471 to `m`; oa-2:3576, 3482 and 4100 and oa-1:5370, 5371 and 5219 to `g`), and all nine agree with the rule below.

- Grade, as the control room corrected it mid-audit: `m` for one named species measured, its own value or a cited one (a cited value is also `partial`); a statement about the group the record names, with no subset or member standing for it, is also `m`. `g` when the passage's taxon differs from the record's (a wider or narrower group, one member standing for a group, a relative), and for a value the paper predicts or presumes (an opsin gene predicts a pigment; a presumed dichromat), following `docs/views/audit/SAMPLE.md` ("The rule decided", "a presumption or hypothesis") and BRIEF line 170.
- `partial: true` for anything from a review, a compilation, a cited study or a figure.
- Quotes: a whole sentence or table row, cuts marked with " … ", never starting mid-sentence; table rows may sit after the `=== LAYOUT ===` marker. Typographic differences count as `confirm` (audit 31).
- Errors are `requote`, `correct` and `retract`. Metadata faults are listed and not counted.

## Texts

The key was made on this machine and kept in `/tmp/oa-audit-all`, outside the repository. Branch `run/oa/audit-1018-all` (8e66a6e) changed only `ci/oa/pub.pem` and cut `ci/oa/list.jsonl` to the 20 papers behind the 40 records. Run 13 returned all 20 texts (oa-1 x3, oa-2 x7, oa-6 x1, oa-9 x5, oa-10 x4), decrypted with 0 checksum mismatches. No text or key was committed.

For four papers the oa job served this audit a different kind of copy from the one `ci/oa/sources-r1.jsonl` records for the readers: Hunt et al. 2009 (oa-2 entry 30), Jacobs 2009 (oa-2 entry 31) and Hart et al. 2016 (oa-9 entry 53) came back as PDF where the readers had HTML, and Johnson and Rutowski 2022 (oa-2 entry 22) came back as Europe PMC XML where the readers had the PDF. Four quotes from Hunt and Hart (oa-9:370, oa-2:3576, oa-2:3482, oa-9:351) therefore fail `quotecheck.py` on this copy, for glyphs (the PDF text prints λ as "l" and "=" as "¼") and spaces inside parentheses only. The words match the sentences, so they count as typographic.

## Verdicts

Grade and partial are as they stand at cf645cb. "qc" is the result of `python3 -I tools/views/quotecheck.py` on this audit's text.

| # | id | taxon / trait | value | grade | qc | verdict | reason |
|---|---|---|---|---|---|---|---|
| 1 | oa-2:3506 | Callicebus / lambda_max_nm | 562 | m, partial | table | confirm | Hunt et al. 2009 Table 1, layout row "Pitheciidae Callicebus titi monkey 1 5 562, 550, 542, 535, 530"; a genus row with no member named, so `m`; review, so `partial` |
| 2 | oa-9:228 | Lygodium microphyllum / sense_chemical | responds to conspecific antheridiogen | m | verbatim | confirm | Table 1 row, "Yes" under Response to self; the paper's own cultivation test; conditions match Methods (1% agar, Bold's medium, 25 °C, 12:12 h, 65 µmol m−2 s−1) |
| 3 | oa-2:3509 | Callicebus / lambda_max_nm | 535 | m, partial | table | confirm | same row as #1 |
| 4 | oa-1:5568 | Gallus gallus domesticus / cff_hz | [90, 100] | m, partial | verbatim | confirm | section 1.4 sentence, individual range cited from Lisney et al. 2011; the preceding sentence names domestic chickens |
| 5 | oa-9:370 | Gallus gallus and Columba livia / lambda_max_nm | 467 | g, partial | fail (glyphs) | **correct** | the Introduction sentence matches apart from glyphs and gives the four λmax values for "the chicken (Gallus gallus) and pigeon (Columba livia)", the pair the record names (refs 4, 5: Bowmaker 1977; Bowmaker and Knowles 1977). No subset stands for it, so the grade is `m` |
| 6 | oa-10:255 | Eriosyce confinis var. kunzei / sense_light_nonvisual | 2 (% in darkness) | m | verbatim | confirm | Flores et al. 2011 Table 1 layout row marked "New data"; Methods match the conditions field |
| 7 | oa-9:15 | Thoropa miliaris / pupil_shape (new trait) | circular (larvae) | m | verbatim | confirm | Results sentence in the bioRxiv text; the first cut drops only an interleaved line number; the paper's own photo survey |
| 8 | oa-10:650 | Mammillaria supertexta / sense_light_nonvisual | 95 (% in light) | m, partial | verbatim | confirm | Table 1 row citing Benítez-Rodríguez et al. (2004) |
| 9 | oa-10:254 | Eriosyce confinis var. kunzei / sense_light_nonvisual | 41 (% in light) | m | verbatim | confirm | same row as #6 |
| 10 | oa-10:117 | Heliophobius argenteocinereus / colour_vision | no evidence for colour discrimination | m | verbatim | confirm | Discussion sentence; the next sentence says both species chose randomly (blue against green, blue against green-yellow) |
| 11 | oa-2:4050 | Anolis carolinensis / lambda_max_nm | 625 | m, partial | verbatim | confirm | Introduction sentence citing Provencio et al. 1992; the reference list matches the note |
| 12 | oa-2:3576 | Mirza coquereli / receptor_classes | functional gene retained | g, partial | fail (spacing) | confirm | the sentence matches apart from spaces inside parentheses; a retained SWS1 gene predicts a pigment, so `g`; review, so `partial` |
| 13 | oa-10:238 | Echinopsis ancistrophora / sense_light_nonvisual | RLG 0.978 | m | verbatim | confirm | Table 1 row, New data; RLG = Gl/(Gd + Gl) as the caption defines it (44 and 1) |
| 14 | oa-1:5621 | Delias eucharis / cff_hz | 225 | m, partial | verbatim | confirm | Table A1 row; the caption names the four compiled studies the note lists |
| 15 | oa-2:3482 | Ornithorhynchus anatinus / receptor_classes | dichromacy | g, partial | fail (spacing) | confirm | the sentence matches apart from spacing; dichromacy is inferred from two cone pigments, so `g` |
| 16 | oa-2:4100 | Gymnospermae / sense_light_nonvisual | no ZTL homologue found | g | verbatim | confirm | Results sentence; a database search predicts and measures nothing, so `g`; the paper's own analysis |
| 17 | oa-9:351 | Dromaius novaehollandiae / lambda_max_nm | 367 (UVS) | m | fail (glyphs) | confirm | Results sentence ("lmax ¼ 367 nm" in the PDF text); own MSP; the note's remark that the abstract prints 376 nm is right |
| 18 | oa-10:75 | Amegilla murrayensis / acceptance_deg | 1.39 | m | verbatim | confirm | Table 1, Δρ row for males, last column; mean ± 95% CI per the table note; 10 male cells per the Fig. 2 legend |
| 19 | oa-1:5750 | Canis lupus familiaris / eye_diameter_mm (new trait) | 24 | m | verbatim | confirm | Tab. 1 row "Border Collie 24 22,5 12 6,5 1827 6755", column BD; caliper ("Schiebelehre") in Methods; the thesis uses this name |
| 20 | oa-6:773 | Dromaius novaehollandiae / relative_eye_size (new trait) | somewhat smaller than predicted | g | verbatim | confirm | two sentences joined by a marked cut; the statement covers the four ratites together, so `g` for the emu holds; the eye sizes are the paper's own Plasticine measurements, so no `partial` |
| 21 | oa-2:3471 | birds / oil_droplets | coloured oil droplets, ubiquitous | m, partial | verbatim | confirm | a statement about birds as a group, so `m` |
| 22 | oa-1:5370 | Boiga ceylonensis / lambda_max_nm | 536 (LWS) | g | verbatim | confirm | Table S5 layout row "A H Y A A 536"; the caption says the values are predicted from sequence |
| 23 | oa-6:762 | Columba livia / eye_axial_length_mm (new trait) | 11.6 | m, partial | verbatim | confirm | Table 1 row; axial length from the literature (footnotes a and d: Martin & Katzir 1995, Martin 1998) |
| 24 | oa-2:3650 | Cavia / lambda_max_nm | S | g, partial | table | confirm | Jacobs 2009 Table 1 row "Cavia (guinea pig) S M Parry & Bowmaker (2002)"; the guinea pig, one species, stands for the genus, so `g` holds |
| 25 | oa-1:5794 | Canis lupus familiaris / fovea | area centralis temporal, flat streak (most likely) | m | verbatim | confirm | German sentence verbatim in 5.1.2; the English in the note is faithful and flags that 4.2.4 found no streak |
| 26 | oa-9:32 | Caretta caretta / binocular_deg | 60 | m | verbatim | confirm | Results 3.1 sentence; n = 10; ages 4 to 7 weeks in Methods |
| 27 | oa-9:37 | Caretta caretta / behaviour_vision | 17 of 23 bit the small target | m | verbatim | confirm | Results 3.2 sentence; squid odour for loggerheads in Methods |
| 28 | oa-2:3480 | Ornithorhynchus anatinus / lambda_max_nm | 451 (SWS2) | m, partial | verbatim | confirm | the preceding sentence names SWS2 then LWS and cites Davies et al. 2007 and Wakefield et al. 2008 |
| 29 | oa-2:3384 | Myrmecocystus / eyes_count | ocelli present in workers | g | verbatim | confirm | Introduction sentence on the paper's own examination; the genus claim rests on the species examined, and in one clade of pale species "some to most workers lacked the anterior ocellus", so `g` holds |
| 30 | oa-1:5597 | Papilio demoleus / cff_hz | [90, 110] | m, partial | verbatim | confirm | Table A1 row |
| 31 | oa-10:174 | Viperidae / diel | primarily nocturnal or crepuscular | g, partial | verbatim | **correct** | "Viperids are primarily nocturnal or crepuscular" is a statement about the family the record names, with no subset or member standing for it, so the grade is `m` |
| 32 | oa-1:5371 | Macroprotodon brevis / lambda_max_nm | 555 (LWS) | g | verbatim | confirm | Table S5 row "A H Y T A 555"; predicted |
| 33 | oa-10:655 | Mammillaria winterae / sense_light_nonvisual | RLG 1 | m, partial | verbatim | confirm | Table 1 row citing Maiti et al. (1994) |
| 34 | oa-9:143 | Panogena lingens / sense_hearing | hearing organ on the labial palps, sensitive to ultrasound | m, partial | verbatim | **requote** | the quote holds only the first sentence; "labial palp" and "ultrasound" are in the next sentence, so the value says more than the quote. The value itself is right |
| 35 | oa-10:688 | Oreocereus hempelianus / sense_light_nonvisual | RLG 1 | m | verbatim | confirm | Table 1 row, New data |
| 36 | oa-2:3879 | Ophioglossales / sense_light_nonvisual | two PHY2/4 copies | g | verbatim | confirm | Results sentence; gene content predicts photoreceptors, so `g`; the paper's own analysis |
| 37 | oa-2:3891 | Chironius bicarinatus / acuity_cpd | 2.9 | m | verbatim | confirm | Table 3 layout row, column "Visual acuity (cpd)*" (hexagonal array); the chapter's own 12 snakes from the Butantan Institute, so no `partial` |
| 38 | oa-10:405 | Turbinicarpus schmiedickeanus ssp. rubriflorus / sense_light_nonvisual | 0 (% in darkness) | m, partial | verbatim | confirm | Table 1 row citing Flores et al. (2006) |
| 39 | oa-1:5219 | Amphisbaena infraorbitale / lambda_max_nm | 491-496 (RH1) | g | verbatim | confirm | Table S3 row; predicted |
| 40 | oa-2:3373 | Myrmecocystus navajo / fov_h_deg | 128 | m | verbatim | confirm | Results sentence; five workers a species; the method matches the Methods text |

## Error count

**3 errors in 40, 7.5%** (Wilson 95% interval 2.6% to 19.9%): 1 `requote` (oa-9:143), 2 `correct` (oa-9:370 and oa-10:174, both grade `g` to `m`), 0 `retract`. Every value, taxon and `partial` flag in the sample is right; only one quote and two grades are wrong. The rate is above the 5% line audit 31 used, and both grade errors come from the corrected group rule (see pattern 1).

## Metadata faults (not counted)

| id | field | fault |
|---|---|---|
| oa-2:3384, oa-2:3373 | source.doi | holds the Dryad dataset DOI 10.5061/dryad.nzs7h44v8; the text read is the PLoS ONE article that the record's own url names (10.1371/journal.pone.0257779) |
| oa-9:143 | source.journal | "Journal of Comparative Physiology A" with no volume, issue or pages. `sources-r1.jsonl` lists volume and pages as gaps, and the Europe PMC XML read prints neither, so the reader could not fill them from the text |
| oa-9:15 | source | the quote comes from the bioRxiv preprint (the url), while authors, journal and pages describe the published version, whose wording was not checked. The note says so |

## Fault patterns

1. **Group statements still graded `g` after the second pass.** Both counted grade errors are of this kind (oa-9:370, oa-10:174). Outside the sample, and not audited: oa-2:3323 ("Caimans are arrhythmic animals."), oa-10:166 (Collembola, diurnal) and oa-10:175 (Viperidae, receptor classes) still carry `g`, and the one sentence behind oa-10:146 and 147 gives woodcocks `m` and mallards `g`. A rough filter finds about 220 group-rank records at `g` whose taxon, method and note carry no prediction or subset word. That is an upper bound, since it also catches rightful cases such as the Jacobs 2009 exemplar rows (#24).
2. **A value that draws on the next sentence.** oa-9:143 takes "labial palps" and "ultrasound" from the sentence after its quote. This is the only content fault in the sample.
3. **Copy drift between oa runs.** The job chose a different kind of copy for four of the 20 papers, and four quotes fail the mechanical check on this audit's copy for glyphs and spacing alone. Recording the url read in `sources-r1.jsonl` and fetching that url again would let later audits run `quotecheck.py` against the readers' exact text.
4. **Trait keys holding values of another kind** (not counted): `receptor_classes` holds "functional gene retained" (oa-2:3576) and "dichromacy" (oa-2:3482), `lambda_max_nm` holds the category "S" (oa-2:3650), and `eyes_count` holds the presence of ocelli (oa-2:3384). Each value is faithful to its quote, but a numeric key carrying a gene statement or a category can be misread downstream.
5. **Minor, not counted.** The rank word is dropped from printed names (oa-10:254, 255 and 405 print "var." and "ssp."; the notes say so). Two notes keep a stale grade sentence before the control room's: oa-2:4100 ("so graded i") and oa-9:143 ("Graded g, not m").

## Rows written

`docs/views/recheck/recheck-oa-1018.jsonl`: 3 rows in the recheck-5 schema (`unit`, `supersedes`, `action`, `reason` and the full corrected record), with `field`, `old` and `new` added. These are oa-9:370 (grade g to m), oa-10:174 (grade g to m) and oa-9:143 (requote, 40 words, which passes `quotecheck.py` verbatim and `check.py`). Each corrected record's note ends with a "Corrected by audit oa-1018 (18 Oct)" sentence. No evidence file was edited.

## Recommendation

Apply the three rows. Before merging, run one more pass of the group rule over the group-rank records still at `g` (pattern 1), since that pass would also close the two grade errors found here. Quotes, values, taxa and `partial` flags held in 39 of 40, so the reading itself needs no second pass.
