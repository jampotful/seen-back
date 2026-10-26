# Audit 76: rescreen-1 (branch research/rescreen-1)

Gate: `screen_candidates.py --check` on the 18 search records and 16 wanted lines prints "0 problems".

## Sample (seed 76)

The unit holds 18 search records, fewer than 20, so the sample is the whole unit. `random.seed(76)` over lines 1 to 18 gives the order 12, 15, 13, 4, 5, 1, 7, 17, 14, 10, 8, 11, 2, 16, 3, 6, 9, 18. Because the unit is its own sample, the "check 15 more after an error" rule is already met.

## Method

Judged against the unit's brief (right families: Arenaria Scolopacidae, Linaria Fringillidae, Prunella Prunellidae, Morus Sulidae, Aquarius Gerridae, Orthosia and Colocasia Noctuidae, Parnassius Papilionidae, Fowlea for Xenochrophis; wrong-kingdom family-review queries left out of `queries` and named in `note`). `harvest_get.py` was run for the nine genera. Fowlea, Arenaria, Linaria, Prunella and Orthosia match the harvest's query lines word for word and in order; the wrong-kingdom family reviews (Alismataceae for Aquarius, Caryophyllaceae for Arenaria, Plantaginaceae for Linaria, Lamiaceae for Prunella, Apocynaceae for Orthosia) are left out of `queries` and named in `note`, as briefed. Morus and Colocasia are "in no harvest run yet", so their `queries` hold web searches only. `canon` was compared with docs/views/research/canon.jsonl by trait and class: nothing missing. Every DOI in `chased` and every `screened` id is in the harvest output. Screened abstracts were read for Fowlea, Parnassius, Arenaria, Orthosia and Prunella entries (none reports the trait). I ran 23 WebSearches (a pair per genus and trait group for most, a third for the moths and snakes) and about 20 fetches of URLs my searches returned; five came back as a verification page, a redirect or binary data and stayed unread. No ResearchGate, academia.edu, Sci-Hub, LibGen or library proxy page was opened.

## Verdicts

| Line | Record | Verdict |
|---|---|---|
| 1 | Fowlea acuity_cpd; fovea | ok. Queries match; the three screened works are eye-size and opsin studies with no acuity or fovea. Searches found keelback natural-history notes only. |
| 2 | Parnassius cff_hz; corner_hz | **error (queries).** The harvest ran the family review "Parnasiinae vision review" (1 hit, same kingdom, a misspelled subfamily), and the record drops it ("discarded, not listed in queries"). The brief excuses only wrong-kingdom reviews, and desk-screen point 7 asks for every harvest query that ran. The content is not affected: my flicker searches returned Chatterjee et al. (canon, named) and no Parnassius value. |
| 3 | Aquarius cff_hz; corner_hz | **error (queries, the lesser one).** `chased` and `note` rely on a web search "Gerridae vision review" and report its results, but `queries` does not list it (every other family-step record lists its "web: ... vision review"). The omitted Alismataceae review is rightly left out. Content unaffected: my water-strider flicker search found no Aquarius value. |
| 4 | Arenaria binocular_deg; fov_h_deg | ok. My searches returned the Laridae/Procellariidae seabird fields (canon, named), Cantlay et al. on three gulls (no Arenaria), and a plover and sandpiper foraging paper. No turnstone field. |
| 5 | Arenaria cff_hz | ok. No turnstone flicker value found. |
| 6 | Linaria cff_hz | ok. Finch flicker hits were the canon compilations and the budgerigar paper. |
| 7 | Linaria lambda_max_nm; spectral_range_nm | ok. Eight screened plant papers hold no bird pigment. Stavenga and Wilts 2014 covers Carduelis feathers and a blue tit model, not Linaria. |
| 8 | Prunella acuity_cpd; interreceptor_deg | ok. Eleven screened works (herbal myopia studies, machine vision, migration) hold no accentor retina. |
| 9 | Prunella cff_hz | ok. |
| 10 | Prunella lambda_max_nm; spectral_range_nm | ok. |
| 11 | Morus binocular_deg; fov_h_deg | ok. Searches returned the canon seabird fields, Cantlay et al. (gulls), the Australasian gannet accommodation paper (on the wanted list) and no gannet field value. |
| 12 | Morus cff_hz | ok. No gannet flicker value found. |
| 13 | Orthosia acuity_cpd; interommatidial_deg | ok. Searches returned a Triphosa dubitata thesis (Ljubljana, 2020), a Grapholita eye paper and a Lepidoptera eye review; none names Orthosia. |
| 14 | Orthosia cff_hz; corner_hz | ok. |
| 15 | Orthosia lambda_max_nm | ok. A JGP 1967 ERG paper turned up for the search is on Limulus. |
| 16 | Colocasia acuity_cpd; interommatidial_deg | ok. |
| 17 | Colocasia cff_hz; corner_hz | ok. |
| 18 | Colocasia lambda_max_nm | ok. |

Errors: 2 of 18, 11.1% (line 3 alone would be the weaker call; with line 2 alone the rate is 5.6%, still over 5%). Pooled with audits 43 to 51 and 55 to 73 (8 errors in 664 records) and audit 75 (0 in 9): 10 in 691, 1.4%. The unit itself is over 5%, so under the desk's rule the error records are dropped and the rest merged: **drop lines 2 and 3; merge lines 1 and 4 to 18.**

## Claims about main

- Fowlea lambda_max_nm: held. Xenochrophis piscator lambda_max_nm at oa-1:5253 (476 and 489 nm) and oa-1:5362 (560 nm), diel at oa-1:5507; no Fowlea row, no acuity or fovea row.
- Aquarius interommatidial_deg: held as Gerris paludum, 2.1 deg at insect:244 and methods:55; Aquarius paludum acuity_cpd at canon-4:87 (0.24).
- Morus: held. sws1_type VS for M. bassanus and M. serrator at oa-2:2902-2903; ocular media block UV for M. serrator at recheck-5-fixed:10 and sweep-6:11; colour_vision at sweep-13:10. No Morus row for acuity, fields or flicker, as the note says.
- Arenaria interpres eye_movement only (canon-3:561); no Linaria row; the only Prunella rows are the plant light responses (harvest-15:1, oa-12:329-330); Parnassius glacialis lambda_max_nm at methods:451-453. All as the notes say.

## Wanted lines (faults listed, not counted)

- Line 2 (Awata et al. 2010, JEB 213(23): 4023-4029): the Soken repository page names four authors, the line three (Kentaro Arikawa missing); its page gives PubMed ID 21075944 and no DOI, so the DOI 10.1242/jeb.048678 is unchecked. The paper studies P. glacialis and the line's `for` is P. apollo.
- Line 3 (Matsushita et al. 2012, Proc R Soc B 279(1742): 3482-3490): DOI 10.1098/rspb.2012.0475 and title confirmed on the Soken page; five authors there, three on the line (Takemura and Arikawa missing). Same P. glacialis versus P. apollo mismatch.
- Lines 1, 4 to 15: authors and years blank by design; not checked against pages (the Karger, Springer, PMC and Purdue pages came back as verification pages or were not returned by my searches).
- Line 16 (Pérez i de Lanuza and Font 2014, jeb.104281): not opened.

## Leads

- Karger 10.1159/000551766 (ocular media of birds, title cut off): may list a Sulidae species; held on the wanted list.
- Springer 10.1007/BF00193552 and BF00340945 (Aquarius): not opened.
