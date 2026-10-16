# Precision audit 25, 16 October 2026

Scope: all six records in harvest-17 (2), harvest-18 (2) and harvest-19 (2), every one a partial abstract read. There is no harvest-14 or harvest-16 file, and all eight harvest-15 records were already covered by audit 24 and `recheck-24.jsonl`, so none were left from those files. Fourteen further records were drawn from evidence files that no earlier audit table, recheck file or row of `docs/views/audit/ALL.jsonl` had touched, all of them vertebrates: four birds, one bird order, four mammals and five squamates. Candidates whose pages could not be opened at all were dropped and replaced (see Blocked pages); the fourteen are the first fourteen that opened, in the order tried.

Method as in audit 24. Each source was opened with WebFetch and asked first whether the exact quote string appears, then for value, units, grade, partial flag, method, the complete author list as printed, year, volume and DOI. Publisher pages, PubMed Central and the Frontiers and Company of Biologists sites asked for a permission step that was not answered, so every reading came from the OpenAlex work record, with the abstract rebuilt from its inverted index token by token, and from the Crossref record for bibliographic fields. Where OpenAlex holds no abstract the quote could not be checked; such a record is `unverifiable` unless a bibliographic field could be checked and was wrong, in which case it is `correct` and the reason says the quote was not seen. A change to the partial flag, the grade, the method or a bibliographic field counts as `correct`; lost diacritics, dropped or invented initials and a journal field without its volume count as bibliographic errors. Corrections are in `docs/views/recheck/recheck-25.jsonl`. No evidence file, no wanted file and not `docs/views/audit/ALL.jsonl` was edited. No web searches were run, because the session's search budget was spent.

## Table

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| harvest-17:1 | Papaver radicatum / sense_light_nonvisual | m | confirm | OpenAlex: sentence verbatim at positions 11 to 22, the first token fused as "plants.Only" just as the record's `where` says. Kevan PG, 86: 41-44, 1972 |
| harvest-17:2 | Papaver somniferum / sense_light_nonvisual | m | confirm | OpenAlex: first sentence verbatim, including "( Papaver" and the backtick. Three authors, 31(4): 681 |
| harvest-18:1 | Dryopteris filix-mas / sense_light_nonvisual | m | correct | OpenAlex: sentence verbatim with the U+2010 hyphen. OpenAlex raw name and Crossref both print R. Scheuerlein; the W came from the OpenAlex author profile. Corrected to Scheuerlein R |
| harvest-18:2 | Dianthus caryophyllus / sense_light_nonvisual | m | confirm | OpenAlex: sentence verbatim with the curly quotes; 6 μmol·m−2·s−1 and the four continuous treatments confirmed. Nine authors, 95(4): 666-673 |
| harvest-19:1 | Scrophularia kakudensis / sense_light_nonvisual | m | confirm | OpenAlex: "Interestingly" sentence verbatim; red LED flavonoid sentence, 4 weeks and the cool white fluorescent control confirmed. Four authors, 11: 607007 |
| harvest-19:2 | Cakile edentula / sense_chemical | m | confirm | OpenAlex: "Here we show" sentence verbatim. Two authors, 3(4): 435-438 |
| intake-3:1 | Falco sparverius / acuity_cpd 46 | m | unverifiable | OpenAlex has no abstract for this Elsevier paper, so the quote was not seen. Authors, 43(19): 2053-2059 and 2003 agree with the record |
| intake-7:1 | Camelus dromedarius / tapetum absent | m | confirm | OpenAlex: the sentence ends "and the tapetum is absent." (positions 185 to 189). The abstract names gross examination, ultrasound and CT but no sample size, so the five camels were not checked. Four authors, 63(153): 231-236 |
| sweep-56:2 | Trochilidae / binocular_deg 30 | g | confirm | OpenAlex: sentence verbatim. Five authors with Fernández-Juricic accented, 12: 16. The species pooling is outside the abstract and was not checked |
| intake-5:33 | Giraffa camelopardalis / acuity_cpd 25-27 | m | correct | OpenAlex: phrase verbatim inside the "mean peak of 14,271 cells/mm(2)" sentence. The journal field had no volume; Crossref gives 521(9): 2042-2057, print June 2013. Added |
| intake-7:21 | Tiliqua rugosa / acuity_cpd 6.8 | m | unverifiable | OpenAlex has no abstract, so the quote was not seen. New STD and Bull CM, 197(6): 703-709 and 2011 agree with the record |
| intake-8:1 | Asio otus / opsin_transcripts | m | unverifiable | OpenAlex has no abstract, so the quote was not seen. Eight authors with Höglund accented, 158: 109-119 and 2019 agree with the record |
| oa-5:52 | Trigonoceps occipitalis / binocular_deg 30 | m | correct | Crossref gives the version-of-record title in the singular ("White-headed Vulture … shows") and Ibis 159(2): 463-466. Title and journal corrected. The published abstract has "White-headed Vultures (30°)" with a capital V; the manuscript the quote came from was not opened, so the quote is flagged and left |
| sweep-75:2 | Hydrophis major / acuity_cpd 1.1 | m | confirm | OpenAlex: wording and values verbatim; the abstract writes "deg⁻¹" with superscripts and ends on "respectively;". Four authors with Coimbra's João, 520(6): 1246-1261 |
| sweep-47:8 | Viperidae / receptor_classes | g | correct | OpenAlex and Crossref print the last author as Bruno F Simões; the record's Simoes lost the tilde. Corrected. OpenAlex's abstract field holds placeholder text, so the quote itself was not seen |
| sweep-58:4 | Ctenophorus ornatus / fovea | m | confirm | OpenAlex: sentence verbatim with the colon; the six species and their two habitat groups confirmed. Six authors, 528(4): 542-558 |
| intake-6:21 | Pteroclidiformes / sws1_type UVS | i | correct | OpenAlex: phrase verbatim at positions 91 to 111. The record has "Odeen A, Hastad O"; the byline is Anders Ödeen and Olle Håstad. Corrected |
| canon-7:27 | Serpentes / pupil_shape | g | correct | OpenAlex: sentence verbatim. The abstract ties vertical pupils to ambush predation and polyphasic activity; "nocturnal" occurs only in a sentence on why a variable aperture helps nocturnal species. Value's "or nocturnal" removed |
| intake-4:11 | Vulpes vulpes / receptor_classes 2 | m | correct | OpenAlex: phrase verbatim at the end of the M/L-majority, S-minority sentence. Journal field "J Comp Neurol (2018)" had no volume; 526(13): 2078-2098 added |
| intake-6:27 | Rattus norvegicus / eye_movement | m | correct | OpenAlex has no abstract, so the quote was not seen. The last author is Jason N. D. Kerr (record: Kerr JN) and the journal field "Nature" lacked 498(7452): 65-69. Both corrected |

**Rate: 8 errors in 20 records, 40%**, with 3 unverifiable; among the 17 records that could be checked the rate is 47%. By verdict: 8 correct, 0 requote, 0 retract; 9 confirm; 3 unverifiable. The six harvest records had one error (17%). The fourteen older records from intake, oa, sweep and canon files had seven (50%), all of them in bibliographic or value fields and none in a quote.

## Checks

- **Most common fault: the author field.** Four of the eight errors are in the author list: lost diacritics (Simões in sweep-47:8; Ödeen and Håstad in intake-6:21), a dropped initial (Kerr JND in intake-6:27) and an invented one (Scheuerlein RW in harvest-18:1, taken from the OpenAlex author profile and absent from the byline). This is the same fault audit 24 found most often. The next harvest prompt should say that author names are copied from the byline, or from the OpenAlex `raw_author_name` and Crossref `given`/`family` fields, never from the OpenAlex author `display_name`, and that accents and every printed initial are kept.
- **Journal field without volume.** Four records carried a journal string with no volume (intake-5:33, intake-4:11, intake-6:27, oa-5:52). Audit 24 did not count a missing article number or page range; a missing volume is counted here because the brief names volume as a field to check.
- **Title.** oa-5:52 took its title from the accepted manuscript, which differs from the version of record that its DOI names.
- **Value.** canon-7:27 added "or nocturnal" to the abstract's polyphasic activity.
- **Quotes.** Every quote that could be rebuilt matched verbatim, including the harvest records' careful notes on fused tokens, spacing and special hyphens. The harvest-17 to 19 notes on how each sentence was read were accurate.
- **Grade and partial flag.** No wrong grades or flags. All six harvest records stay `partial: true`.
- **Not counted.** Superscript units flattened to ASCII ("deg-1", sweep-75:2); a missing issue number where volume and pages are present (harvest-17:1); the year where OpenAlex gives the online year and the record gives the print year (intake-5:33, oa-5:52, sweep-75:2, sweep-58:4); Crossref's "Mclamb" against the record's McLamb (sweep-47:8).

## Rows written

`recheck-25.jsonl`: 8 rows, all `correct`: harvest-18:1, intake-5:33, oa-5:52, sweep-47:8, intake-6:21, canon-7:27, intake-4:11, intake-6:27.

## Blocked pages

Candidates that could not be opened were dropped before any check and replaced.

- Permission step not answered: cob.silverchair.com PDF for jeb143883 (canon-3:1) and the article page for jeb.140905 (sweep-46:4); www.frontiersin.org fevo.2019.00321 (canon-2:1); www.ncbi.nlm.nih.gov/pmc/articles/5536890 (canon-3:1).
- Fetch error: onlinelibrary.wiley.com 10.1111/j.1751-1097.1990.tb01757.x (harvest-18:1, read on OpenAlex and Crossref instead).
- Rate limited (HTTP 429): the Europe PMC full-text XML for PMC5536890 (canon-3:1); OpenAlex works for 10.6620/ZS.2022.61-18 (intake-6:17), 10.1016/0042-6989(92)90092-w (intake-5:21), 10.1007/s10344-012-0629-z (sweep-36:2), 10.1002/ece3.8595 (intake-8:21) and 10.1111/vop.12476 (sweep-67:3).
- Opened but past the twentieth record and not counted: intake-4:26 (OpenAlex has no abstract; authors and 148(S2): 563-569 agree).
