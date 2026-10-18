# Precision audit 36, 18 October 2026

Scope: the latest version of each record in `docs/views/evidence/recheck-42-fixed.jsonl` to `recheck-52-fixed.jsonl`, traced through `docs/views/audit/ALL.jsonl` retractions to the replacements in recheck-53-fixed (journal volume and issue), recheck-54-fixed (grade m to g) and recheck-55-fixed (strict review). A retraction with no correction removes the record. The rebuilt population is 493 records (each traced back to an id in files 42 to 52). `docs/views/fixes/requote-partial.jsonl` was applied as the `partial: true` override. The worktree was cut from `research/repair-crossref`. Records are named by their latest id; the original id is in brackets.

Draw: `random.seed(36)`, `random.sample(range(493), 493)` as the order, skipping Kott et al. 2010 and every record named in audits 33, 34 and 35. The first 20 usable records fall in eleven origin files (42, 43, 44, 45, 46, 48, 49, 50, 51, 52 and 47 via the recheck-53 to 55 replacements). Because errors were found, the next 15 usable records were checked.

Method as in audits 16 and 35: WebSearch on the title, then WebFetch on a page the search or the record returned. The fetch tool gives about 125 characters per quote, so each quote was read back in consecutive pieces. No library login, proxy, Sci-Hub, LibGen, academia.edu or ResearchGate page was opened, and no paper text is committed. Typographic differences (a colon character, a hyphen, a missing space) count as `confirm`.

## First 20

| # | record | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 1 | recheck-53-fixed:69 [45:40] | Hasarius adansoni / opsin_localization | m | confirm | verbatim and complete (NSF copy, 3.4); seven authors; Vision Research 217: 108367 |
| 2 | recheck-43-fixed:51 | Crocodylia / opsin_status | i | error (value, journal) | the sentence is verbatim and complete (Whittier PDF) and says OPN5L2 "was not recovered". The value adds "likely deleted", which only the next sentence ("suggests OPN5L2 was deleted in crocodylians") supports. Journal "34: 666-676" lacks the issue (34(3)) |
| 3 | recheck-55-fixed:13 [44:9] | Honckenya peploides / sense_chemical | m | error (journal) | verbatim and complete (MDPI, Results, Propagation stage; the page wraps "Table 1" in a link, which is typographic). The record has no journal field at all (Plants 9(11): 1526) |
| 4 | recheck-55-fixed:68 [50:64] | Deinopis spinosa / sense_hearing | g | confirm | verbatim and complete (UNL PDF, Results, Field Behavioral Assays); five authors; 30(24): 5033-5039.e3 |
| 5 | recheck-53-fixed:46 [45:17] | Hasarius adansoni / opsin_localization | m | confirm | verbatim and complete (NSF copy, 3.3) |
| 6 | recheck-55-fixed:51 [49:14] | Otus asio / retinal_composition | g | confirm | verbatim and complete (USF PDF, Discussion); both owls, so `g`; 18(2): 62-66 |
| 7 | recheck-46-fixed:26 | Gavia immer / diel | g | confirm | verbatim and complete (p. 118-119); cites Barr 1996 and McIntyre and Barr 1997, so `g`; 31(2): 110-124 (the journal field prints "Ornis Hungarica31", a missing space) |
| 8 | recheck-54-fixed:37 [43:38] | Alligator sinensis / opsin_status | g | error (journal) | verbatim and complete (all four crocodylians and four testudines, so `g` is right). Journal "34: 666-676" lacks the issue (34(3)) |
| 9 | recheck-51-fixed:4 | Parabuteo unicinctus / binocular_peak_elevation_above_bill_deg | m | error (journal) | verbatim and complete (Silverchair, Results, Experiment 2); 26 deg is the Harris's hawk value. Journal "Journal of Experimental Biology219:2639-2649" lacks the issue (219(17)) and a space |
| 10 | recheck-54-fixed:50 [44:8] | Rhus typhina / diel | g | confirm | verbatim and complete (English abstract, journal site); five trees, `g`; `partial` true. The page lists no authors, journal or pages; the issue listing gives Vol. 28, No. 2, so authors and pages are unchecked |
| 11 | recheck-53-fixed:147 [50:6] | Salticidae / tapetum | g | confirm | verbatim with the marked end cut (the page continues "due to increased stray light scattering..."); Magazine article, `partial` true; 30(17): R975-R980 per Crossref (the PDF header prints R963-R983, the whole magazine section) |
| 12 | recheck-53-fixed:97 [47:16] | Lycaena heteronea / receptor_classes | g | confirm | verbatim and complete; the sentence covers L. heteronea and L. rubidus, `g`; Annual Review, `partial` true; 46(1): 471-510 |
| 13 | recheck-54-fixed:1 [42:2] | Trigonisca pipioli / eye_topography | g | confirm | verbatim and complete (Springer, Results, Eye morphology); it names no species and speaks for all eight, so `g` |
| 14 | recheck-55-fixed:80 [52:11] | Deilephila elpenor / acceptance_deg | g | confirm | verbatim and complete (KOPS copy); three authors; 26(6): 821-826 |
| 15 | recheck-53-fixed:234 [52:20] | Deilephila elpenor / neural_spatial_pool_ommatidia | i | confirm | verbatim and complete; 109 is a model-derived estimate, so `i` |
| 16 | recheck-46-fixed:25 | Chamaeleo dilepis / ocular_media_cutoff_nm | m | confirm | verbatim and complete (Springer abstract); three authors; 191(10): 925-932; `partial` true |
| 17 | recheck-54-fixed:9 [42:18] | Oxalis stricta / diel | g | error (journal, quote) | Maxapress PDF, Discussion: the sentence reads "nighttime" where the quote has "night-time" (the "..." replaces the citation marker [24], a marked cut). The journal field ends "3(1): 0-0"; the paper is article 11 (3:11), so the pages are a placeholder |
| 18 | recheck-53-fixed:131 [48:5] | Myctophiformes / filter_pigments | g | confirm | verbatim and complete (JEB PDF); five authors; 223(8): jeb193334; review, `partial` true |
| 19 | recheck-55-fixed:26 [46:32] | Stellaria media / sense_chemical | m | error (authors) | the abstract sentence is verbatim and complete (repository record). The record lists five authors; the repository record lists six (Jovanović, Giba, Djoković, Milosavljević, Grubišić and Konjević). The publisher page did not open, so the sixth name rests on the repository |
| 20 | recheck-53-fixed:178 [50:37] | Littorina / eye_role | g | confirm | verbatim and complete (Cambridge PDF, section "Relating sensory tasks to sensory structure"); single author; 30(1-2): 5-20; review, `partial` true |

First 20: 0 unverifiable, 20 verifiable, 6 errors (3 journal-only: 3, 8, 9).

## Extension, 15 more

| # | record | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 21 | recheck-53-fixed:113 [47:32] | Homo sapiens / lambda_max_nm | g | confirm | verbatim (Annual Review); 557 nm is the Ser180Ala polymorphism value; `partial` true |
| 22 | recheck-53-fixed:85 [47:4] | Notonecta glauca / receptor_classes | g | confirm | verbatim with marked cuts at both ends; four taxa pooled, `g` |
| 23 | recheck-54-fixed:110 [49:17] | Bubo virginianus / dark_adaptation_time_min | g | confirm | verbatim and complete (USF PDF, Results); "both subjects", `g` |
| 24 | recheck-55-fixed:15 [44:13] | Androctonus australis / retinula_arhabdomeric_cell_ratio | g | error (journal) | abstract sentence verbatim (Springer; the page prints a colon character in "2 ∶ 1", typographic). Journal field "Cell and Tissue Research 206(1)" has no pages (95-114) |
| 25 | recheck-53-fixed:118 [47:37] | Lucilia / colour_vision | g | confirm | verbatim with a marked opening cut (Annual Review) |
| 26 | recheck-55-fixed:58 [50:36] | Littorina / eye_type | g | confirm | same sentence as #20 |
| 27 | recheck-52-fixed:53 | Bothrops jararaca / diel | g | confirm | verbatim with marked cuts (Frontiers PDF, Discussion, Photoreceptor Population); two species, `g` |
| 28 | recheck-53-fixed:114 [47:33] | Homo sapiens / lambda_max_nm | g | confirm | verbatim (Annual Review); 552 nm for the alanine variant |
| 29 | recheck-50-fixed:73 | Lasioglossum leucozonium / diel | g | confirm | verbatim and complete (Smithsonian repository PDF, Results and Discussion); three authors; 18(5): 349-353 |
| 30 | recheck-47-fixed:58 | Medicago truncatula / sense_light_nonvisual | g | confirm | verbatim and complete (Frontiers review, Response to Vernalization); `partial` true; the authors field prints surnames first (formatting, not counted) |
| 31 | recheck-53-fixed:192 [50:51] | Polyplacophora / behaviour_vision | g | confirm | verbatim and complete (chitons, Cambridge PDF) |
| 32 | recheck-53-fixed:183 [50:42] | Asteroidea / eye_type | g | confirm | verbatim with a marked opening cut |
| 33 | recheck-54-fixed:78 [45:64] | Ophiocoma pumila / sense_light_nonvisual | g | confirm | abstract sentence; the abstract has a comma after "We show that" which the quote omits (typographic). Two species, `g`; four authors; 30(2): 319-327.e4 |
| 34 | recheck-54-fixed:114 [49:21] | Bubo virginianus / dark_adaptation | g | confirm | verbatim and complete (Discussion); "either owl", `g` |
| 35 | recheck-51-fixed:18 | Howella sherborni / fovea | g | error (value) | IntechOpen chapter: the quote (leading "This specialization", marked cut) is verbatim, but the specialization it refers to is the vertical streak (the preceding sentence defines it), while the value says "visual streak" |

Extension: 0 unverifiable, 15 verifiable, 2 errors (1 journal-only: 24).

## Error rate

- First 20: 6 errors in 20 verifiable records (30.0%).
- Both draws: **8 errors in 35 verifiable records, 22.9%** (0 unverifiable; every record had at least its quote page open, though the author list and pages of #10 and the publisher list for #19 were not checked against a primary page).
- Excluding journal-only faults (records 3, 8, 9 and 24): **4 errors in 35, 11.4%**.
- The threshold of 5% is not met on either counting.

## Fault patterns

1. **Journal field incomplete or placeholder** (ids recheck-43-fixed:51, recheck-54-fixed:37, recheck-51-fixed:4, recheck-55-fixed:13, recheck-54-fixed:9, recheck-55-fixed:15). Missing issue: Emerling 2017, 34(3), in two records (the same field as audits 34 and 35 found; recheck-53 and 54 did not change it) and Potier 2016, 219(17). No journal field: Kulpa et al. 2020 (Plants 9(11): 1526). No pages: Schliwa and Fleissner 1980 (206: 95-114). Placeholder pages "0-0": You et al. 2023 (article 3:11). A missing space between journal and volume recurs (Ornis Hungarica31, Journal of Experimental Biology219) and is typographic.
2. **Value goes past the quote** (recheck-43-fixed:51). The quote says the gene was not recovered; the value adds an inference ("likely deleted") from the next sentence.
3. **Value names a different structure than the quote's referent** (recheck-51-fixed:18). The passage defines a vertical streak; the value says "visual streak".
4. **Incomplete author list** (recheck-55-fixed:26). Five of six names; the sixth rests on the repository record, since the publisher page did not open.
5. **Quote wording differs from the page** (recheck-54-fixed:9). "night-time" for "nighttime", a spelling change inside a quoted sentence.
6. **No grade faults and no partial faults this time.** All 17 group or multi-species sentences were `g`, and all abstract or review reads carried `partial: true`. The recheck-54 and recheck-55 passes appear to have cleared the grade and partial patterns of audits 33 to 35. Eleven records carry `partial: true` on full-text reads of a single paper (#14, #15, #16 and others); that flag errs on the safe side and is not counted.

## Blocked pages

pmc.ncbi.nlm.nih.gov (browser check or permission step unanswered) for Kulpa et al. and Streinzer et al.; hal.umontpellier.fr (bot protection) for Potier et al.; europepmc.org and the Europe PMC REST service (permission step unanswered) for several; the publisher page of Jovanović et al. (no fetch). Substitute open pages (MDPI, Springer full text, Silverchair, Frontiers PDF) were read in each case.

No evidence file was edited and no correction rows were written.
