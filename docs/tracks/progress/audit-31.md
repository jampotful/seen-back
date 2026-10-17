# Precision audit 31, 17 October 2026

Scope: the evidence records that this branch (Codex pull request #19 merged with main) adds in harvest-c1 (4), harvest-c2 (2), harvest-c3 (9), oa-1 (33), oa-2 (122) and oa-3 (32): 202 lines. The branch adds no `docs/views/searched/` files, so there are no harvest-c search records to check against the harvest queries. Sampling with Python `random.seed(31)`, drawn per file so that every unit is covered: first 20 records (harvest-c1 x1, c2 x1, c3 x3, oa-1 x4, oa-2 x7, oa-3 x4), then, because errors were found, 15 more (seed 3131, records not in the first draw: c1 x1, c3 x2, oa-1 x3, oa-2 x6, oa-3 x3).

Method as in audit 16. Sources came from WebSearch results and were then opened with WebFetch. No library login, proxy, shadow library or copy of unclear rights was used. The Lin 1993 PDF in the record is a copy on a personal library page at zin.ru; it was not opened.

Opened and read: Springer page for Wei et al. (Ecological Processes), ISHS page for Sønsteby et al., Bristol research page for Sumner-Rooney et al., CONICET repository record for Casalía et al., journal page for Zaimenko et al. (abstract). Blocked or unanswered: PubMed Central (bot challenge, so Healy, Hunt, Rockwell), u-gakugei repository (Nakanishi), Springer page for Maslova, UGent PDF (Christiaens), oceanrep.geomar.de PDF (Rockwell), Figshare (Casalía Table S1), agrobiodiversity.uniag.sk PDF, Europe PMC REST.

Typographic differences count as `confirm`. A missing `partial: true` on a compiled, table or review read counts as `correct` (audit 27 rule). Metadata faults (journal, url) are written as rows that are not counted. No evidence file, `src/`, `views/*.json` or `ALL.jsonl` was edited.

## Table, first 20

| # | id (file:line) | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 1 | harvest-c1:1 | Oxalis corymbosa / sense_light_nonvisual | m | unverifiable | repository page blocked. Journal field lacks volume, issue and pages |
| 2 | harvest-c2:2 | Stachys sieboldii / sense_light_nonvisual | g | unverifiable | Springer page blocked. `g` and `partial: true` are right for a pooled abstract. Journal lacks volume and pages |
| 3 | harvest-c3:2 | Euonymus japonicus / sense_light_nonvisual | m | correct | quote verbatim, a complete sentence, on the Springer page. The page prints "Yaxi Wei, Zhen Li, Jiaolong Zhang, …, Dan Hu", so the four-name author list leaves out at least one author. No journal (Ecological Processes 12(1): 38; metadata row, not counted) |
| 4 | harvest-c3:7 | Rhododendron simsii hybrids / sense_chemical | g | unverifiable | thesis PDF blocked |
| 5 | harvest-c3:9 | Ribes sativum / sense_light_nonvisual | m | requote | the quote stops after "24°C" and the page's sentence goes on to the 12°C result, so it is a cut sentence with no cut marked. Abstract-only `partial: true` right. Journal field empty (Acta Horticulturae 1388: 183-190) |
| 6 | oa-1:5160 | Nephroselmis pyriformis / lambda_max_nm 614 | m | unverifiable | PMC and the geomar PDF blocked; figure label. Journal field lacks the issue |
| 7 | oa-1:5166 | Ectocarpus siliculosus / lambda_max_nm 688 | m | unverifiable | same |
| 8 | oa-1:5165 | Dolichomastix tenuilepis / lambda_max_nm 726 | m | unverifiable | same |
| 9 | oa-1:5172 | Ophiocoma wendtii / behaviour_vision | m | confirm | quote verbatim in the abstract (Bristol page); `partial: true` right. Journal lacks 30(2): 319-327 and the url is a Europe PMC search call (metadata row, not counted) |
| 10 | oa-2:3406 | Asio flammeus / cff_hz 70 | g | correct | Healy Table 1 compilation, original not opened, no `partial`. Value not rechecked (PMC blocked) |
| 11 | oa-2:3411 | Caretta caretta / cff_hz 40 | g | correct | same |
| 12 | oa-2:3332 | Catarrhini / lambda_max_nm 563 | g | correct | Hunt review, no `partial`. The quote opens mid-sentence ("one of which encodes ...") with no cut marked; page not opened, so a requote is possible |
| 13 | oa-2:3333 | Alouatta / lambda_max_nm 558 | g | correct | Hunt Table 1, no `partial` |
| 14 | oa-2:3409 | Carassius auratus / cff_hz 67.2 | g | correct | Healy compilation, no `partial` |
| 15 | oa-2:3319 | Eutheria / oil_droplets absent | g | correct | Hunt review, no `partial` |
| 16 | oa-2:3399 | Serinus canaria / lambda_max_nm 442 | g | correct | Hunt review, no `partial` |
| 17 | oa-3:605 | Pheucticus aureoventris / sws1_opsin_type | i | unverifiable | Table S1 on Figshare blocked |
| 18 | oa-3:610 | Passerina cyanea / sws1_opsin_type | i | unverifiable | same |
| 19 | oa-3:616 | Rhopospina fruticeti / sws1_opsin_type | i | unverifiable | same |
| 20 | oa-3:630 | Malurus splendens melanotus / sws1_opsin_type | i | unverifiable | same. The quote begins at "Maluridae" and carries no species name, so it cannot show which row it is |

First 20: 10 verifiable, 9 errors (3 and 5 by content, 7 by missing `partial`); 10 unverifiable.

## Extension, 15 records

| # | id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 21 | harvest-c1:4 | Oxalis stricta / diel | m | correct | secondary report of Harshberger 1922 (original unopened) with no `partial`; quote with marked cuts is a spliced clause, not one sentence |
| 22 | harvest-c3:1 | Rhododendron catawbiense / sense_light_nonvisual | m | unverifiable | PDF blocked. The journal page's abstract agrees with the value (red highest flavonoids, blue strongest anthocyanin effect). The quote is a lower-case fragment about two species and speaks only to flavonoids. Journal field empty (Agrobiodiversity for Improving Nutrition, Health and Life Quality 10(1)) |
| 23 | harvest-c3:6 | Coccinella septempunctata / polarization | m | unverifiable | the url is a personal-library copy at zin.ru, not opened. Journal field empty |
| 24 | oa-1:5176 | Porcellio scaber / filter_pigments | m | unverifiable | Europe PMC blocked; journal lacks volume; url is a search call |
| 25 | oa-1:5164 | Dolichomastix tenuilepis / lambda_max_nm 598 | m | unverifiable | PMC blocked |
| 26 | oa-1:5158 | Tetraselmis astigmatica / lambda_max_nm 648 | m | unverifiable | same |
| 27 | oa-2:3426 | Pagophilus groenlandicus / cff_hz 32.7 | g | correct | Healy compilation, no `partial` |
| 28 | oa-2:3390 | Aves / filter_pigments | g | correct | Hunt review, no `partial` |
| 29 | oa-2:3326 | Ornithorhynchus anatinus / lambda_max_nm 550 | g | correct | same |
| 30 | oa-2:3417 | Gallus gallus domesticus / cff_hz 87 | g | correct | Healy compilation, no `partial` |
| 31 | oa-2:3433 | Tamias amoenus / cff_hz 100 | g | correct | same |
| 32 | oa-2:3330 | Isoodon obesulus / receptor_classes | g | correct | Hunt review, no `partial` |
| 33 | oa-3:628 | Mimus saturninus / sws1_opsin_type | i | unverifiable | Table S1 blocked |
| 34 | oa-3:608 | Cyanoloxia rothschildii / sws1_opsin_type | i | unverifiable | same |
| 35 | oa-3:611 | Thlypopsis sordida / sws1_opsin_type | i | unverifiable | same; the quote spells the taxon "sórdida" |

Extension: 7 verifiable, 7 errors (all missing `partial`); 8 unverifiable.

## Error rate

- Both draws: 17 verifiable, 16 errors, 94 per cent; 18 of 35 unverifiable.
- Without the 14 missing-`partial` faults: 2 errors in 17 verifiable, 12 per cent (harvest-c3:2 authors, harvest-c3:9 quote).
- Both figures exceed 5 per cent. The `partial` faults were judged from the record's own note ("Original paper not opened", "secondary", "review"); the values behind those 14 rows were not rechecked.

## Systematic faults

1. Compiled and review rows without `partial: true`. All 13 oa-2 Healy and Hunt rows sampled lack it, although each note says the original was not opened, and so does harvest-c1:4. The oa-2 pool has 122 new lines; a script keyed on "Secondary" or "Original paper not opened" in `note` would set the flag.
2. Journal field without volume, issue or pages, or empty: harvest-c1:1, c2:2, c3:1, c3:2, c3:6, c3:9, the Rockwell, Healy, Hunt and Sumner-Rooney rows. Four oa-1 and harvest-c3 urls point at Europe PMC search calls or personal-library copies, not at an article page.
3. Quotes that are cut or fragmentary: harvest-c3:9 (cut, no mark), harvest-c3:1 (lower-case fragment about two species), oa-2:3332 (opens mid-sentence), harvest-c1:4 (spliced clauses). Table rows and Table S1 lines are the pipeline's convention and are not counted.
4. Author list shortened to four names with a gap (harvest-c3:2).
5. Thin checking of figure labels and supplements: 14 of 18 unverifiable records are Rockwell figure labels, Casalía Table S1 lines and blocked PMC pages. A desk member with the PDFs should open Rockwell Figs. 2 and 3 and Casalía Table S1.

## Rows written

`docs/views/recheck/recheck-31.jsonl`: 17 rows, all `correct`. Counted: 14 `partial` rows (oa-2:3406, 3411, 3409, 3426, 3417, 3433, 3332, 3333, 3319, 3399, 3390, 3326, 3330 and harvest-c1:4). Not counted: metadata rows for harvest-c3:9 (journal), oa-1:5172 (journal, url) and harvest-c3:2 (journal). The requote of harvest-c3:9 and the author list of harvest-c3:2 have no counted row because the full sentence and full author list could not be read.

## Recommendation

Do not merge as it stands. Set `partial` on the compiled rows by script, fill the journal fields and requote harvest-c3:9, then merge; the unverifiable Rockwell and Casalía rows need a session with PMC and Figshare access.
