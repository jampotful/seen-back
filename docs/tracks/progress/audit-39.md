# Precision audit 39, 18 October 2026

Scope: the 6 evidence records of harvest-23, -24 and -25, and 20 of the 144 search records of the same units, drawn with `random.seed(39)` over the three searched files in file order (harvest-23, then -24, then -25). No evidence, searched or wanted file was edited. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.

Method. Evidence records follow audit 16: the title was searched, a URL the search returned was fetched, and the quote, value, grade, partial flag, authors and journal were compared. Search records: `queries` were compared with the lines `python3 -I tools/views/harvest_get.py <Genus>` prints; each DOI in `chased` was looked for in that output; `where` was read against what the harvest printed; and one WebSearch (scientific name plus trait words) per genus looked for an open-access measurement of the record's trait.

## (a) Evidence records

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| harvest-23:1 | Apus apus / spectral_range_nm | g, partial | requote | Authors, J Exp Biol 224(20): jeb243129 and DOI confirmed on PMC8601714. The Discussion sentence is longer than the quote, which joins "the common swift, the European nightjar ... have lambda T0.5 of 380 nm or higher" with internal and outer ellipses, so it is not one complete sentence. The value (T0.5 at 380 nm or higher) stands as a group bound, so `g` and `partial` are right. Table 1 is an image and was not read |
| harvest-24:1 | Helianthus annuus / sense_light_nonvisual | m, partial | confirm | Verbatim in the abstract on the MDPI page; authors Vinterhalter, Motyka, Vinterhalter; Int J Plant Biol 16(1): 8 (2025), 10.3390/ijpb16010008 |
| harvest-24:2 | Calypte anna / binocular_deg | g, partial | confirm | Quote is verbatim in the abstract (the page prints "~30°", the record "~30 degrees", a typographic difference). The value's second half, 22 to 23 degrees with eyes at rest, is in the Results of the Frontiers PDF ("between 22 and 23 degrees"), pooled for Anna's and rufous hummingbirds, so `g` is right. The quote supports only the 30 degrees figure. Authors and Front Neurosci 12: 16 confirmed |
| harvest-24:3 | Nymphaea candida / sense_light_nonvisual | m, partial | requote | Quote is the first 20 words of a conclusion sentence and ends in an ellipsis, so it is not a complete sentence. The abstract's conclusion 2 says opening follows an endogenous rhythm, and conclusion 1 names solar radiation as the main natural factor, so the value holds. Field observation of the white water-lily (Volkova 2002, White Sea Expedition materials vol. 2, on herba.msu.ru) |
| harvest-25:1 | Veratrum californicum / sense_light_nonvisual | m | confirm | Verbatim in the Oregon State PDF; Shock, Parris and Shock; day lengths 12, 14 and 16 h. The series name and year are inferred from the file name, as the record says, and the PDF states neither |
| harvest-25:2 | Empetrum rubrum / sense_light_nonvisual | m, partial | requote | Abstract point 5 (CONICET repository) holds the words, but the quote opens with an ellipsis and "nor", the tail of a longer sentence. Authors, J Ecol 90(4): 704-713, 2002 and DOI confirmed. The "20% of ambient" and "three growing seasons" detail was not checked against the full text |

Evidence records: 6 checked, 3 with a verdict other than confirm (all three requote, none a wrong value), **error rate 50% by the audit 16 definition (3 of 6)**; wrong values or grades: 0 of 6. Every requote is a quote that is not one complete sentence, the form rule of the method, so the rate says the quotes need repair and does not say the measurements are false.

## (b) Search records (20 of 144)

Check columns: Q is the share of the record's `queries` that harvest_get prints; chased is whether the named DOI is in the harvest output. Every one of the 20 has one to three queries beyond what the harvest printed; those are the WebSearch queries added by the agent (a common-name query with trait words, and a family review query), which the harvest cannot print, so they are noted and not counted as errors.

| unit:line | genus / trait | Q | chased | WebSearch-only steps | my own check (open-access measurement?) | verdict |
|---|---|---|---|---|---|---|
| 24:26 | Foeniculum / diel, eye_type, sense_chemical | harvest queries all; 2 added | DOI in output | common name, family review (plant) | Only the general circadian volatile review (PMC5713376), not fennel; none found | weak |
| 25:9 | Plutella / cff_hz | all; 1 added | in output | one added query | No flicker, acuity or spectral paper on Plutella surfaced; a 1981 NTU thesis on photoreceptor morphology (about 1,500 to 2,000 ommatidia; closed-adjusted pigment migration) bears on none of the open traits. Two Zool Stud PDFs (21(1): 75, 26(2): 165) came back as binary data and stay unread | confirm |
| 25:8 | Plutella / acuity_cpd | all; 1 added | in output | one added query | same as above | confirm |
| 25:41 | Cuculus / lambda_max_nm | all; 2 added | none-reason | common name, family review | Cuckoo hits are egg or UV-passerine papers; none found. The harvest did print a Cuculidae family review (116 hits), so "no family review found" misdescribes it | weak |
| 25:36 | Cuculus / acuity_cpd | all; 2 added | none-reason | same | same | weak |
| 23:7 | Puma / 8 traits | all; 1 added | in output | one common-name query | Search returned only clinic and popular pages; none found | confirm |
| 24:22 | Nymphaea / eye_type, sense_chemical | all; 2 added | none-reason | common name, family review (plant) | Floral-scent emission papers (PMC11013332) measure emission, not perception; none found | weak |
| 24:29 | Draba / four traits | all; 3 added | none-reason | common name, family review (plant) | Generic seed-light papers, none naming Draba; none found | weak |
| 25:44 | Haliastur / binocular_deg | all; 1 added | in output | one common-name query | Potier et al. 2018, "Visual field shape and foraging ecology in diurnal raptors" (J Exp Biol 221, 10.1242/jeb.177295), measures 15 Accipitriformes; the abstract names none, and the full text was blocked, so I cannot say whether Haliastur is among them. Open lead, unresolved | weak |
| 23:2 | Ramphocelus / 7 traits | all; 2 added | none-reason | common name, family review | Search returned opsin papers on other taxa; none found | weak |
| 24:18 | Callospermophilus / acuity, binocular, fov, fovea, receptor_classes | all; 2 added | in output | common name, family review | **Measurement exists.** A PMC article on cones of Citellus lateralis (PMC1190822; title and authors not printed by the fetch) records from single cones and reports two cone classes peaking near 520 and 435 nm plus a rod near 500 nm. Citellus lateralis is the golden-mantled ground squirrel, now Callospermophilus lateralis, so receptor_classes is measured. The record's `where` opened Jacobs et al. 1980 and says "no cone-class count", which is the wrong source to have stopped on | error |
| 25:18 | Hierodula / acuity_cpd | all; 2 added | none-reason | common name, family review | None found. The record cites mantid measurements (Qian et al. 2026, Rossel 1979) on other genera, so "no measured relative" in `chased` contradicts its own `where` | weak |
| 23:19 | Agelastica / 6 traits | all; 2 added | none-reason | common name, family review | None found | weak |
| 23:3 | Amazilia / 6 traits | all; 1 added | in output | one added query; the harvest family review returned no hits ("None"), so the family step is WebSearch only | Tyrrell et al. 2018 covers Calypte and Selasphorus only; none found | weak |
| 23:28 | Cistus / 4 traits | all; 2 added | none-reason | common name, family review (plant) | Pherobase and flower-colour hits; none found | weak |
| 25:51 | Nucifraga / fov_h_deg | all; 3 added | none-reason | common name, family review | Only natural-history pages; none found | weak |
| 25:34 | Coccyzus / lambda_max_nm | all; 2 added | none-reason | common name, family review | Cowbird and hummingbird papers; none found | weak |
| 25:32 | Coccyzus / fov_h_deg | all; 2 added | none-reason | same | same | weak |
| 23:25 | Amazona / 7 traits | all; 1 added | both DOIs in output | one added query; harvest family review (253 hits) ran | Only veterinary ophthalmic tests and a plumage paper; none found | confirm |
| 25:43 | Haliastur / acuity_cpd | all; 1 added | in output | one added query | as 25:44 | weak |

Verdict counts for the 20: **confirm 4, weak 15, error 1**. Weak or error: 16 of 20, **80%**. The 95% interval on a share from 20 draws is wide (roughly 56% to 94%), but even its lower end is above half.

Pattern behind the weak verdicts. In the three files the harvest header and output show that the harvest itself sent only scientific-name queries, never a common-name query, so the common-name step is WebSearch for all 144 records. Of the 144 records, 92 have no harvest family review with hits and 87 have no harvest citation step, so for those the family review or citation step also exists only as title-level WebSearch (or as nothing: 83 records give a none-reason for `chased`). 61 records have a harvest header with no family printed (the family review was then searched by hand), and 45 are plant records, which have neither a common-name search nor a family review in the harvest.

## Counts across all 144 search records

- Records saying the steps the harvest left out ran as WebSearch because api.openalex.org was refused (403 or fetch refusal): **144 of 144**, in all three files.
- Records whose `queries` are all printed by harvest_get: 0 of 144; each has 1 to 4 added queries (85 have 2, 38 have 1, 19 have 3, 2 have 4). That is the expected shape when WebSearch steps are appended, and is listed here as a deviation from "word for word".
- Chased DOI absent from the harvest output: 3 of the records with a DOI (24:5 Sphaerophoria 10.1007/s00359-014-0895-1; 25:67 Claytosmunda and 25:68 Amauropelta, both 10.1073/pnas.1319929111). None is in the 20-record draw, so these are extra findings. They should be checked before the cells they settle stand.
- Aquarius (25:24 to 25:28): the harvest header lists Alismataceae and its family review ran on that name; the records say the Gerridae review was searched by hand. These five are weak, as the brief stated. Two of them name Dahmen 1991 (Gerris lacustris, a relative, about 920 ommatidia), which is a relative's value and settles nothing for Aquarius.
- Chased reads "none: no measured relative and no family review found" in 83 records. At least in Cuculus and Coccyzus the harvest did print a family review, so the phrase misstates the protocol.

## Recommendation

The search records should not settle cells as they do now. In this draw 4 of 20 survive as credibly complete, 15 rest on common-name and family-review steps that were title-level WebSearch (the harvest never ran a common-name query, and 92 of 144 records lack a harvest family review with hits), and 1 missed an open measurement outright (Callospermophilus, receptor_classes). Hold the 144 records as unsettled until the OpenAlex steps run from the build machine, and release a record only once its common-name search, family review and citation step exist as OpenAlex results; in the meantime the drop from 51,081 to 3,885 open cells overstates settled coverage by whatever share of those cells the weak and error records closed. If the owner prefers a faster route, release only the records of the confirm type (the harvest ran the citation step and a family review with hits, and the agent added a single common-name query), re-open the three records with a missing chased DOI, and re-search the Callospermophilus receptor_classes cell and the Haliastur raptor-visual-field lead before anything else. The three requotes in (a) should be repaired to whole sentences, which changes no value.

## Blocked pages and unread leads

- PMC pages for Tyrrell et al. 2018 and the Plutella eye paper PMC12070478 returned bot checks; the Frontiers PDF served the Tyrrell text.
- journals.biologists.com (Potier 2018) and the HAL copy: permission not answered, bot protection.
- zoolstud.sinica.edu.tw PDFs 21.1/75 and 26.2/165 returned binary data.
