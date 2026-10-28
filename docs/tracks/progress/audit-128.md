# Audit 128: desk-d38 (plant genera, batches 29 and 30; branch origin/research/desk-d38, head eb9954b4)

## Lines judged

- Evidence: all 8 lines of docs/views/evidence/desk-d38.jsonl.
- Search records: 58 lines in docs/views/searched/desk-d38.jsonl. Sample drawn first, `random.seed(128)`, `random.sample(range(1, 59), 20)`: lines 2, 5, 8, 9, 10, 16, 17, 20, 21, 24, 26, 31, 33, 35, 36, 37, 41, 43, 48, 55. The sample held errors, so 15 more were drawn from the rest (`random.seed(1128)`): lines 7, 13, 14, 15, 19, 22, 23, 30, 32, 46, 51, 53, 54, 56, 57. 35 records judged in full. The queries check and the check against main ran by script over all 58.
- Wanted lines: all 9, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched (58 lines) and wanted (9 lines) files prints "0 problems".

## Method

I followed desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39, and the rulings in force in the launch prompt (audits 84, 86, 87, 88, 90). Audit 90 served as the format.

- Queries. A script compared each record's unprefixed `queries` with every `query` and `family review` line `harvest_get.py` prints. The nine harvested genera (Larix, Veratrum, Cylindropuntia, Hydrophyllum, Adenostoma, Claytosmunda, Amauropelta, Umbellularia, Malosma; lines 28 to 33 and 40 to 58) match word for word and in order, with "web: " lines after. No harvest shows "gave up". The other genera are in no harvest run and list only "web: " lines. All 58 pass.
- Chased. Harvested genera print no citation step; each record's `chased` is a none-reason that names the harvest's own family review (all nine family reviews ran, 2 to 333 hits). Accepted under the ruling. Unharvested Asteraceae and Poaceae genera name 10.1007/s44372-025-00446-3 from a labelled "<Family> photoreceptor review" web search; accepted under audits 86 and 87. The rest give the none-reason.
- Main. A script checked every search record (genus, trait) and evidence record (genus, trait) against docs/views/evidence/*.jsonl and docs/views/searched/*.jsonl on origin/main (753c0cd8). The three conflicts it found were all on main at the merge base (9ed39ed8), so the desk could see them.
- Searches. I ran about 35 WebSearches and fetched only URLs they returned. I opened no ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page. A springerlink.bibliotecabuap.elogim.com result and an academia.edu result were left alone. No paper text is committed.

## Evidence verdicts (8)

| Line | Record | Verdict |
|---|---|---|
| 1 | Galinsoga quadriradiata light (Jursik et al. 2003) | ok. PSE page opened. The quote is verbatim, and the abstract says non-dormant seeds were tested in light and dark at 5 to 30 C. Galinsoga ciliata filed under the accepted G. quadriradiata. |
| 2 | Galinsoga quadriradiata light (Yang et al. 2026) | ok. xb.ynau page opened. Authors, 41(1): 23-30 and DOI match, and the quote is verbatim. |
| 3 | Armeria helodes chemical (Vuerich et al. 2022) | ok. herbmedit PDF and bagav PDF opened. The quote is verbatim. The doses (1,000 ppm GA3; 0.2% and 2% KNO3; 24 h) match Methods. |
| 4 | Yucca reverchonii chemical (Troger et al. 2018) | ok. segraveslab PDF opened. The quote is verbatim, from the Results, on Y. reverchonii flowers. WFO accepts Y. reverchonii. Floral volatile emission counts under 10(a). |
| 5 | Ericameria nauseosa light (Khan et al. 1987) | ok. BYU page opened. The quote is verbatim. Chrysothamnus nauseosus is filed under Ericameria. |
| 6 | Larix olgensis chemical (Meng et al. 2018) | **error: synonym name.** The BJFU page opened, and the quote and doses (1, 5 or 10 mmol/L) match. But WFO (wfo-0000443271, opened) lists Larix olgensis as a synonym of the accepted Larix gmelinii var. olgensis, and POWO (77189504-1, opened) accepts L. gmelinii var. olgensis (A.Henry) Ostenf. & Syrach, whose basionym is A.Henry's L. olgensis. Under the ruling, a POWO synonym is an error. Refiled as Larix gmelinii, the value holds. |
| 7 | Larix gmelinii chemical (Men et al. 2013) | ok. PMC3765852 opened. Authors, BMC Genomics 14: 548, and the quote are verbatim, and 0.1 mM MeJA matches. |
| 8 | Cylindropuntia leptocaulis chemical (Rojas-Arechiga et al. 2011) | ok, with a cosmetic fault. The rngr.net PDF opened, and the quote and the 500, 1,000 and 1,500 ppm doses are verbatim. The source title is "Effect of Gibberellic Acid on Germination of Seeds of Five Species of Cacti From the Chihuahuan Desert, Northern Mexico", not "... of Cactaceae". |

Evidence errors: **1 of 8 (12.5%)**, line 6.

## Search record verdicts (35)

| Line | Record | Verdict |
|---|---|---|
| 2 | Galinsoga sense_chemical | ok. My GA3, nitrate and smoke search returned Peng et al. 2012 (CASB 28(1): 158-161, opened; temperature and humidity only) and the two light papers. No hormone, nitrate or smoke trial. Cosmetic fault: the `where` list holds a string split into single characters. |
| 5 | Anthyllis sense_chemical | ok. My search returned only smoke papers on other genera (Çatav et al. 2024; Keeley chaparral work). |
| 7 | Polypodium sense_light_nonvisual | ok. My search returned Ceratopteris and P. aureum (Phlebodium) papers, which the desk rightly excluded. biostor 218857 was blocked (permission unanswered), so it is unchecked. |
| 8 | Polypodium sense_chemical | **error: contradicts main.** origin/main oa-9:287 holds Polypodium cambricum sense_chemical (Hornych et al. 2021, antheridiogen and dark germination). Point 4: a trait with evidence on main gets no search record. |
| 9 | Polypodium diel | ok. No spore-release timing found. |
| 10 | Polypodium eye_type | ok. Eye_type is none for plants, and the screened works are rightly set aside. |
| 13 | Armeria eye_type | ok. |
| 14 | Maclura diel | ok. No flower-opening or scent timing came up. |
| 15 | Maclura sense_chemical | ok. My search returned Vitenko 2002 (AGRIS opened: sowing depth and germination duration only) and an apple GA3 paper (Latakia page opened; not Maclura). dergipark jist 511469 was blocked, so it is unchecked. |
| 16 | Maclura eye_type | ok. |
| 17 | Yucca eye_type | ok. |
| 19 | Hesperoyucca sense_chemical | ok. My search returned seed sellers and an unrelated smoke-water paper (MDPI Plants 8: 104, opened; no yucca). |
| 20 | Hesperoyucca diel | ok. My search returned flora pages only, with no opening hour for H. whipplei. |
| 21 | Hesperoyucca eye_type | ok. |
| 22 | Ericameria diel | ok. |
| 23 | Ericameria eye_type | ok. |
| 24 | Arum sense_light_nonvisual | ok. My search returned an Arabidopsis shade paper (PMC2803649, opened) and extension pages. Sowter 1949 (Biological Flora of A. maculatum, aroidsociety.org) was refused, so it is unchecked as a lead. |
| 26 | Corydalis sense_chemical | **error: contradicts main.** origin/main sweep-18:3 holds Corydalis cava sense_chemical (Olesen and Knudsen 1994, floral scent profiles), and emission counts under 10(a). |
| 30 | Veratrum sense_chemical | ok. My search returned Pacific Bulb Society notes, a Jelitto listing, Holloway 2011 (UAF opened; no Veratrum) and the USU chilling paper the harvest lists. No GA3 or smoke trial. |
| 31 | Veratrum eye_type | ok. |
| 32 | Cylindropuntia diel | ok, with a lead. My search returned Grant and Hurd 1979, "Pollination of the southwestern Opuntias", Pl Syst Evol 133: 15-28 (Springer page opened). The abstract says cholla flowers open by day and that one unnamed cholla has nocturnal flowers. No named species and no hour in the abstract. The full text may name species. |
| 33 | Cylindropuntia eye_type | ok. |
| 35 | Lycopodium diel | ok. |
| 36 | Lycopodium eye_type | ok. |
| 37 | Hordeum sense_light_nonvisual | **error: contradicts main.** origin/main oa-12:176 holds Hordeum vulgare sense_light_nonvisual (Tao et al. 2026, phyB mutants delay heading). |
| 41 | Hydrophyllum sense_chemical | ok. My search returned Holloway 2011 (no Hydrophyllum) and other genera. |
| 43 | Hydrophyllum eye_type | ok. |
| 46 | Claytosmunda diel | ok. |
| 48 | Claytosmunda eye_type | ok. |
| 51 | Amauropelta sense_light_nonvisual | ok. My search returned Thelypteris dentata (Christella) and Mexican Thelypteridaceae gametophyte morphology. No light trial on an Amauropelta species. |
| 53 | Umbellularia diel | ok. |
| 54 | Umbellularia sense_chemical | ok. The UW propagation protocol (opened) gives stratification only, with no GA3 or chemical data. |
| 55 | Umbellularia sense_light_nonvisual | ok. The same protocol gives only "shade-tolerant" from NRCS, with no measurement. |
| 56 | Umbellularia eye_type | ok. |
| 57 | Malosma diel | ok. My search returned pherobase and unrelated pages, with no timing. |

Search record errors: **3 of 35 (8.6%)**, lines 8, 26 and 37.

The script found no other main conflict among the 23 unjudged lines. Their queries match too.

## Counts and pool

- Search records: 3 of 35, 8.6%.
- Evidence: 1 of 8, 12.5%.
- Unit: 4 of 43, 9.3%.

Pooled with audits 83 to 90 (audit 90's figures: 48 in 1026 search records; 52 in 1090 with evidence):
- Search records: 51 in 1061, 4.8%.
- With evidence included: 56 in 1133, 4.9%.

**Verdict: fail.** Both the search records (8.6%) and the evidence (12.5%) are above 5%. The errors are mechanical (main conflicts and one synonym name), so dropping or refiling the lines below lets the rest of the unit stand.

**Error lines:**
- docs/views/searched/desk-d38.jsonl: lines 8, 26 and 37 (drop; main already holds those traits).
- docs/views/evidence/desk-d38.jsonl: line 6 (refile as Larix gmelinii, or as var. olgensis, or drop).

## Wanted lines (listed, not counted)

- Line 3 (James et al. 1993, Oecologia 93: 512-517, 10.1007/BF00328959): the authors, year, pages and DOI match the Jornada archive page (opened).
- Line 8 (Zhao et al. 2016, 10.11829/j.issn.1001-0629.2016-0362): the authors, year, pages and DOI match the cykx.lzu page (opened). That page itself prints "Volume 10", which the line copies.
- Lines 1, 2, 4, 5, 6, 7 and 9 were not opened by me, so they are unchecked. Line 4 (Khan et al. 1987) is the same paper as evidence line 5, and its authors match the BYU page.

## Leads

- Cylindropuntia diel: Grant and Hurd 1979 (Pl Syst Evol 133: 15-28), on cholla day-flowering, with species possibly in the full text.
- Arum: Sowter 1949, Biological Flora of Arum maculatum (unread).
- Ericameria sense_chemical: the Khan et al. 1987 GA3 and kinetin result (already wanted line 4).

## Blocked pages

- aroidsociety.org Sowter 1949 PDF: refused by the classifier, not retried.
- archive.org biostor-218857: permission unanswered, not retried.
- dergipark.org.tr jist 511469: permission unanswered, not retried.
