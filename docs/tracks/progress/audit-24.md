# Precision audit 24, 16 October 2026

Scope: all 16 records in harvest-12 (1), harvest-13 (7) and harvest-15 (8), every one a partial abstract read, plus four records from other files that no earlier audit table, recheck file, retract row or row of `docs/views/audit/ALL.jsonl` had touched. The seven oa-8 Egri et al. records (oa-8:52 to 8:58) were already corrected for the Mészáros accent in `recheck-23.jsonl`, so all seven were skipped. The four untouched records are canon-2:83 (a bird), sweep-52:5 (a leafhopper), sweep-10:2 (a tiger beetle larva) and sweep-38:4 (an ant). Mammal, amphibian and reptile candidates were tried first and could not be opened (see Blocked pages), which left the extra draw with one vertebrate.

Method as in audit 23: each source opened with WebFetch and asked first whether the exact quote string appears, then for value, units, grade, partial flag, method, the complete author list as printed, year, volume and DOI. Where the publisher page would not load, the OpenAlex work record was used, with the abstract rebuilt from its inverted index; this gives the words in order and is treated as a reading of the abstract. A change to the partial flag, the grade, the method or a bibliographic field counts as `correct`, and lost diacritics in an author list count as a bibliographic error. Corrections are in `docs/views/recheck/recheck-24.jsonl` in the recheck-5 schema. No evidence file, no wanted file and not `docs/views/audit/ALL.jsonl` was edited. No web searches were run: the session's search budget was already spent, so every page came from a URL in the records.

## Table

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| harvest-12:1 | Pinus pinaster / sense_light_nonvisual | m | correct | MDPI page: the quote is verbatim and sits in the Abstract, which the record had left unidentified. The page prints Pablo Martínez-Zurimendi with the accent (OpenAlex raw name agrees), so the record's note that the page drops it is wrong. Author and `where` corrected; 8(10): 383 confirmed |
| harvest-13:1 | Fagus sylvatica / sense_light_nonvisual | m | confirm | OpenAlex: sentence verbatim; the abstract closes on phytochrome-mediated photoperiod control as the record says. Two authors, 208(4): 1023-1030 |
| harvest-13:2 | Fagus crenata / sense_light_nonvisual | m | confirm | OpenAlex: final sentence verbatim; twigs collected February 2020, four conditions. 16(12): 1982562 |
| harvest-13:3 | Euonymus japonicus / sense_light_nonvisual | m | requote | OpenAlex index: "Furthermore, blue and red light significantly decreased the stomatal conductance of E. japonicus." The logged quote dropped "and red". Requoted, value amended. The green-light clause covers "the above indices" as a group |
| harvest-13:4 | Oxalis triangularis / diel | m | confirm | Maxapress article page: fragment verbatim, continuing "expanding about 30°"; flowers stay closed in constant darkness and the clock plays no significant role in their movement |
| harvest-13:5 | Oxalis triangularis / sense_light_nonvisual | m | confirm | Same page: fragment verbatim, continuing "whereas floral movement was mainly affected by temperature"; "The stronger the light intensity, the lesser time it took for the leaves to fully expand after closing" confirms the detail the note left unchecked. Seven authors; the journal field lacks article 11 |
| harvest-13:6 | Medicago truncatula / sense_chemical | m | requote | OpenAlex index has "and receptors involved in both CO and LCO perception are necessary for mycorrhizal establishment", with no "arbuscular" and no capital. Requoted as a fragment. Authors corrected to Radhakrishnan GV and Bozsóki Z |
| harvest-13:7 | Fragaria vesca / sense_chemical | m | confirm | OpenAlex: fifth sentence verbatim; two greenhouse experiments, no contact with the substrate, stolons extend toward live substrate, volatiles proposed in the last sentence. 6: 814 |
| harvest-15:1 | Prunella vulgaris / sense_light_nonvisual | m | confirm | MDPI: sentence verbatim; Methods give 70 and 340 μmol m−2 s−1 far-red at 740 nm, 30 d, three nutrient levels. Four authors, 13(9): 2250 |
| harvest-15:2 | Epipactis veratrifolia / sense_light_nonvisual | m | confirm | MDPI: sentence verbatim with the one logged cut; the next sentence gives the red-versus-blue-and-dark comparison; both spellings of the epithet occur as the record notes. 9(9): 1007 |
| harvest-15:3 | Geranium robertianum / sense_light_nonvisual | m | requote | OpenAlex index: "Shade‐tolerant G. robertianum does not display the change in hormone levels upon FR light enrichment, resulting in the lack of a shade avoidance response." The logged clause was a paraphrase. Requoted; Banda J corrected to Banda JP |
| harvest-15:4 | Silene gallica / sense_light_nonvisual | m | confirm | OpenAlex: opening sentence verbatim; c.15 days after emergence at LAI below one, CuSO4 filtering and R:FR of 0·95 and 0·8 all confirmed. 14(2): 195-202 |
| harvest-15:5 | Medicago truncatula / sense_chemical | m | correct | OpenAlex: fourth sentence verbatim and the receptors named in the fifth. Authors corrected: Tak Lee carries no second initial (the record had Lee TH), and Bozsóki regains its accent |
| harvest-15:6 | Achillea gypsicola / sense_light_nonvisual | m | confirm | OpenAlex: sentence verbatim; four authors with Turkish characters, 25(6): 1234-1242. The abstract's flavonol figure ("0.5 times") is ambiguous beside the record's "raised"; not counted |
| harvest-15:7 | Cirsium setidens / sense_light_nonvisual | m | confirm | OpenAlex: sentence verbatim; purple LED with about 17.6 percent far-red increased leaf length and width. Eight authors, 28(6): 799-823 |
| harvest-15:8 | Euonymus japonicus / sense_light_nonvisual | m | correct | MDPI: quote verbatim. The Methods say the plants were set directly into the soil in a field experiment under three LED intensities (about 22, 57 and 94 lux); the record's "potted plants" is wrong. Method and conditions corrected; five authors, 15(4): 659 |
| canon-2:83 | Bubo scandiacus / binocular_deg 34 | m | confirm | Birmingham repository PDF, section 3(a): "The width of the maximum binocular overlap across all 23 species … ranged from 34° in the Snowy Owl Bubo scandiaca to 54.5° …"; ophthalmoscopic reflex technique. Nine authors, 290: 20230664 |
| sweep-52:5 | Empoasca onukii / acuity_cpd 0.14 | m | confirm | MDPI: sentence verbatim. Peak behavioural angle 7.3°, reciprocal about 0.14 cpd, yellow/black grating in a dark chamber. The 30 cm yellow/red clause comes from a separate simulation. Seven authors, 14(4): 370 |
| sweep-10:2 | Cicindela chinensis / lambda_max_nm 525 | m | confirm | Springer abstract: "The stemmata possessed a single type of retinular cell with a maximal spectral sensitivity at 525 nm"; the fragment carries the value. Journal field lacks pages 591-599 |
| sweep-38:4 | Solenopsis invicta / eye_type | m | confirm | Springer abstract: last sentence verbatim in the two logged pieces; alates only. The page truncates the authors after three names, so the full list of six could not be checked; 5: 570-575 |

**Rate: 6 errors in 20 records, 30%** (none unverifiable). By verdict: 3 correct, 3 requote, 0 retract; 14 confirm. In the harvest files alone the rate is 6 in 16, 38%; the four untouched records from other files were all clean.

## Checks

- **Quotes from summaries.** All three requotes come from abstracts read through a page summary of the OpenAlex record. Each logged sentence is close to the printed one and differs in a way a summariser produces: a dropped coordinate ("and red"), an added adjective ("arbuscular"), or a clause rewritten into shorter words. The harvest notes were honest about reading through a summary; the quotes themselves were not verbatim.
- **Authors.** Four of the six errors involve the author field: one lost accent the record's own note denied (harvest-12:1), lost accents on Bozsóki (harvest-13:6 and 15:5), and initials either missing (Radhakrishnan GV, Banda JP) or invented (Lee TH). harvest-13:3's "Zhang J-L" for Jiaolong Zhang could not be settled without the publisher page and is left as it is.
- **Method.** harvest-15:8 describes potted plants where the paper describes a field planting. The error sits outside the abstract, which the harvest did not read.
- **Grade and partial flag.** No wrong grades or flags. All 16 harvest records stay `partial: true`, since only abstracts were read.
- **Not counted.** Journal strings that omit an article number or pages (harvest-13:4 and 13:5, sweep-10:2).

## Rows written

`recheck-24.jsonl`: 6 rows. `correct`: harvest-12:1, harvest-15:5, harvest-15:8. `requote`: harvest-13:3, harvest-13:6, harvest-15:3.

## Blocked pages

Candidates for the four-record draw that could not be opened were dropped before any check and replaced.

- Permission step not answered: openaccess.city.ac.uk eprint 15201 (canon-2:99, Malpolon); ndownloader.figshare.com files 47932130 (oa-5:330, Ambystoma) and 8713297 (oa-1:4157, Chiroptera).
- Browser check page with no article text: pmc.ncbi.nlm.nih.gov PMC10994157 (canon-2:105, Callimedusa).
- Fetch error: link.springer.com 10.1007/s00359-025-01776-z (sweep-53:2); www.nature.com s41467-019-12999-5 and onlinelibrary.wiley.com 10.1002/pld3.66 (harvest-13:6, 15:3 and 15:5 were read on OpenAlex instead).
- Rate limited (HTTP 429): doi.org for 10.1186/s13717-023-00449-6 (harvest-13:3, read on OpenAlex instead) and the Europe PMC REST search for 10.1038/s41467-019-12999-5.
