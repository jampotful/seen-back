# Precision audit 26, 16 October 2026

Scope: the three records of harvest-20, all partial abstract reads. Every record of harvest-17 to harvest-19 was already covered by audit 25 (its table and `recheck-25.jsonl`), so none were left from those files. Seventeen further records were drawn from evidence files that no earlier audit table, recheck file or retract row of `docs/views/audit/ALL.jsonl` had touched, all graded `m`: ten insects (five butterflies, a sawfly, a bee, two damselflies and a mantis) and seven vertebrates (four mammals, two birds and a snake). Because more than one record was in error, eleven more were checked from the same files (mammals-met, external-6, sweep-18, sweep-28 and sweep-46); they are listed separately and do not enter the rate.

Method as in audit 25. Each source was opened with WebFetch and asked first whether the exact quote string appears, then for value, units, grade, partial flag, method, the setup as the paper states it, the complete author list as printed, year, volume and DOI. Where the publisher page would not open, the OpenAlex work record was read, with the abstract rebuilt from its inverted index and suspect tokens checked by position, and authors were taken from `raw_author_name` or the Crossref record, never from the OpenAlex author `display_name`. A change to the partial flag, the grade, the method, the setup or a bibliographic field counts as `correct`; a journal field without its volume counts as a bibliographic error, as in audit 25. Corrections are in `docs/views/recheck/recheck-26.jsonl`. No evidence file, no wanted file and not `docs/views/audit/ALL.jsonl` was edited. No web searches were run, because the session's search budget was spent.

## Table

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| harvest-20:1 | Phacelia tanacetifolia / sense_light_nonvisual | m | confirm | OpenAlex: sentence verbatim at positions 40 to 60; "negatively photoblastic" is in the abstract's first sentence. Raw names Iskender Tiryaki and Huseyin Keles match; the Keleş form is only the OpenAlex author profile. 52(3): 332-339 |
| harvest-20:2 | Phacelia tanacetifolia / sense_light_nonvisual | m | confirm | OpenAlex: quote verbatim after "Abstract—". The far-red and phytochrome statements are pooled across species, as the note says. P. Rollin, 5(5-6): 375-376 |
| harvest-20:3 | Osmunda cinnamomea / sense_light_nonvisual | m | confirm | OpenAlex: sentence verbatim with the U+2010 hyphen in far‐red; P420 and the five light colours confirmed. Two authors, 23(4): 704-714 |
| sweep-9:2 | Castor fiber / acuity_cpd | m | confirm | OpenAlex: phrase verbatim; 17' in air and 9' in water confirmed. A. M. Mass and A. Ya. Supin, Doklady Biological Sciences 473(1): 35-38 |
| mammals-met:1 | Ovis aries / fovea | m | correct | OpenAlex: both sentences verbatim. Journal field lacked 518(12): 2305-2315; partial flag absent on an abstract-only record. Both corrected |
| sweep-67:1 | Glis glis / receptor_classes | m | confirm | Lynx PDF: the sentence is printed "shortwavesensitive" across a line break, so the record's hyphen is a fair reading. Five authors with Glösmann, 53: 185-205 |
| external-6:8 | Tharsalea heteronea / lambda_max_nm 568 | m | correct | OpenAlex: sentence verbatim. Journal field lacked 88(7): 2783-2787. Added |
| sweep-28:1 | Graphium sarpedon / receptor_classes | m | confirm | The Frontiers article page prints "15" in its abstract, as quoted; the OpenAlex abstract and the page's metadata spell it "fifteen". Five authors, 4: 18 |
| external-2:4 | Arge similis / eye_type | m | correct | OpenAlex and MDPI: phrase verbatim; ages and dark adaptation confirmed. Journal field lacked 13(2): 152. Added |
| sweep-18:12 | Accipiter cooperii / binocular_deg 39 | m | correct | OpenAlex abstract has no field widths and the PLoS page could not be read, so the quote was not seen. Raw name Esteban Fernández-Juricic; the record lost the accent. Corrected |
| canon-7:5 | Mnais costalis / opsin_gene_count 1 | m | confirm | PubMed Central: sentence verbatim (italics aside); M. costalis was read by RNA-seq. Seven authors, 112(11): E1247-E1256 |
| sweep-52:3 | Ischnura heterosticta / lambda_max_nm 525 | m | correct | PubMed Central: sentence verbatim; intracellular recordings. Journal field lacked 9(1): e87972. Added |
| sweep-25:3 | Osmia rufa / spectral_range_nm | m | correct | OpenAlex: phrase verbatim at positions 17 to 21; 348, 436 and 572 nm confirmed. The abstract names a fast voltage-clamp technique; method corrected |
| sweep-46:3 | Callophrys sheridanii / lambda_max_nm 520-530 | m | correct | OpenAlex: clause verbatim at positions 65 to 80. Author field stopped at ten names "and others" (fifteen in all) and the title field carried a bracketed note. Both corrected |
| sweep-53:6 | Hymenopus coronatus / lambda_max_nm | m | unverifiable | Springer page and PDF returned fetch errors; the OpenAlex abstract calls H. coronatus dichromatic but does not mention the 530 nm adaptation. Three authors and 212(1): 79-85 agree |
| sweep-74:6 | Helicops leopardinus / lambda_max_nm 411 | m | confirm | OUP page: phrase verbatim (italic n); two wild-caught individuals for MSP. Eight authors, 38(12): 5225-5240 |
| sweep-35:3 | Fratercula arctica / fov_h_deg | m | confirm | NERC manuscript: sentence verbatim, 167 printed without a degree sign as the where says; Isle of May, ophthalmoscopic reflex technique. Ibis 157(4): 798-807 |
| canon-4:160 | Parthenos sylvia / acuity_cpd 0.56 | m | confirm | NSF PAR manuscript: Table 1 row as logged; 0.56 is 1/Dr by the paper's rule. Seven authors. The manuscript prints no volume, so 60 was not checked |
| sweep-56:8 | Cerdocyon thous / tapetum | m | correct | Journal page: phrase verbatim. The abstract describes a young orphan male fox from the wild, about 45 days old, referred to a veterinary hospital; the record called it captive. Conditions corrected |
| oa-3:585 | Argynnis sagana / filter_pigments | m | unverifiable | Europe PMC PDF disallowed by robots and the PMC page asked for a permission step; the OpenAlex abstract gives uniform yellow female eyeshine but not the sentence. Eight authors with Ilić, Pirih, Meglič, Prevc and Belušič accented, 377(1862): 20210276 |

**Rate: 8 errors in 20 records, 40%**, with 2 unverifiable; among the 18 records that could be checked the rate is 44%. By verdict: 8 correct, 0 requote, 0 retract; 10 confirm; 2 unverifiable. The three harvest-20 records had no error. The seventeen older records had eight (47%), none of them in a quote that could be seen.

## Further records from the same files

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| mammals-met:2 | Ovis aries / tapetum | m | correct | OpenAlex: sentence verbatim at positions 61 to 81. Journal field lacked 518(12): 2305-2315; partial flag absent; method narrowed to the macroscopic fundus observation the abstract names |
| mammals-met:3 | Ovis aries / receptor_classes | m | correct | OpenAlex: the three pieces verbatim and in order. Journal volume added, empty method filled from the abstract, partial set true |
| mammals-met:11 | Lycaon pictus / tapetum | m | correct | OpenAlex: sentence verbatim at positions 112 to 133. Second author Klećkowska-Nawrot JE (initial E dropped), title cut short and 16(4): e0249368 missing. Corrected |
| mammals-met:13 | Cavia porcellus / acuity_cpd 0.75-1.65 | m | correct | OpenAlex: sentence verbatim in the structured abstract's Results. Journal field lacked 104(4): 523-531; partial set true |
| external-6:3 | Tharsalea rubidus / lambda_max_nm 500 | m | correct | OpenAlex: sentence verbatim with the stored "lambdamax=" tokens. Journal field lacked 209(16): 3079-3090. Added |
| external-6:4 | Tharsalea rubidus / lambda_max_nm 568 | m | correct | Same sentence and same fault as external-6:3 |
| external-6:6 | Tharsalea heteronea / lambda_max_nm 437 | m | correct | Same sentence and same fault as external-6:8 |
| external-6:7 | Tharsalea heteronea / lambda_max_nm 500 | m | correct | Same sentence and same fault as external-6:8 |
| sweep-18:11 | Spizelloides arborea / binocular_deg 24.64 | m | correct | JEB PDF: Table 1 gives 24.64±0.72 deg. The logged quote was a summariser's paraphrase and Fernández-Juricic had lost the accent. Quote and author corrected |
| sweep-28:2 | Graphium sarpedon / lambda_max_nm | m | confirm | Frontiers page: sentence verbatim in Results; GsUV at 354 nm confirmed |
| sweep-46:14 | Trybliographa rapae / colour_vision | m | confirm | OpenAlex: sentence verbatim; 15 bands from 340 to 670 nm. Four authors, 88(3): 239-245 |

Nine of the eleven were wrong, eight of them through the journal field. The mammals-met and external-6 files carry the fault on almost every record, so the rest of both files probably need their volumes filled.

## Checks

- **Most common fault: a journal field without its volume.** Four of the eight errors in the sample (mammals-met:1, external-6:8, external-2:4, sweep-52:3) and eight of the nine in the further records carry a bare journal name such as "J Comp Neurol", "PLoS ONE" or "Insects". This is the fault audit 25 named second. It clusters in files written before the harvest prompts asked for volume and pages, so a script that fills volume, issue and pages from Crossref for every record with a DOI would clear most of it without further reading.
- **Authors.** The accent on Fernández-Juricic was lost in both sweep-18 records, sweep-46:3 stopped its list at ten names of fifteen with "and others", and mammals-met:11 dropped an initial. The Hosaka YZ of the three sheep records was left: Crossref and the OpenAlex raw name print Yoshinao Hosaka with no middle initial, but the byline itself was not seen.
- **Method and setup.** sweep-25:3 said intracellular recording where the abstract names a fast voltage-clamp technique; sweep-56:8 called a wild orphan fox captive; mammals-met:3 had an empty method.
- **Partial flag.** Four mammals-met records read from the abstract alone had no partial flag; each is set true.
- **Quotes.** Every quote that could be seen matched, except sweep-18:11, whose quote was a summariser's sentence and not text from the paper. sweep-28:1 was first marked for requote because the OpenAlex abstract spells "fifteen"; the Frontiers article page prints "15", as logged, so the verdict was changed to confirm and the row, pushed in the first commit, was withdrawn.
- **Harvest-20.** All three records are accurate, including the notes on what the abstract pools across species and the use of raw author names.
- **Not counted.** A missing page range where volume is present (sweep-74:6); title capitalisation in the accepted manuscript (sweep-35:3); Crossref's "De Souza" against the record's de Souza (sweep-25:3); the bioRxiv year 2020 against the merged OpenAlex year 2021 (sweep-46:3).

## Rows written

`recheck-26.jsonl`: 17 rows, all `correct`. From the sample: mammals-met:1, external-6:8, external-2:4, sweep-18:12, sweep-52:3, sweep-25:3, sweep-46:3, sweep-56:8. From the further records: mammals-met:2, mammals-met:3, mammals-met:11, mammals-met:13, external-6:3, external-6:4, external-6:6, external-6:7, sweep-18:11.

## Blocked pages

- Rate limited (HTTP 429): api.crossref.org for 10.1111/j.1600-079x.2011.00947.x (harvest-20:1, read on OpenAlex instead); the Europe PMC REST search for 10.1002/cne.22333; OpenAlex for 10.1007/s00359-025-01759-0 (sweep-40:18, dropped before any check).
- Fetch error: link.springer.com article page and PDF for 10.1007/s00359-025-01776-z (sweep-53:6).
- Permission step not answered: the PLoS ONE printable file for 10.1371/journal.pone.0012169 (sweep-18:12) and www.ncbi.nlm.nih.gov/pmc/articles/9441240 (oa-3:585). The PLoS ONE HTML page for 0012169 returned a different article.
- Robots disallowed: europepmc.org PDF render for PMC9441240 (oa-3:585).
- Browser check: pubmed.ncbi.nlm.nih.gov search for 10.1002/cne.22333.
