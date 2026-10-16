# Precision audit 19, 16 October 2026

Scope: every record of harvest-7 (4), harvest-8 (2), harvest-9 (2), harvest-10 (1) and harvest-11 (3), 12 in all, no sampling. All are plants, eleven `sense_light_nonvisual` and one `diel`; eleven at `m`, one at `g`; all logged `partial: true` from page summaries. Also checked: the wanted lines of harvest-8, harvest-9 and harvest-10 (one each; harvest-11 has no wanted file).

Method as in audits 13 to 18: each source opened with WebFetch (WebSearch only to locate a paper or its repository record) and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces. Metadata checked against the opened page, the Crossref record or a repository record. Where the full text opened and the relevant section was read, `partial` was set to false and the verdict is `correct`. Corrections are in `docs/views/recheck/recheck-19.jsonl` in the recheck-5 schema. No evidence file, no wanted file and not `docs/views/audit/ALL.jsonl` was edited.

## Table

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| harvest-7:1 | Impatiens walleriana / sense_light_nonvisual | m | correct | Full text open (ASHS PDF). Quote verbatim, Results "Seedling height", 19 words. Flower-bud finding verbatim in Results. DOI confirmed on Crossref. `partial` to false. "R160" read as red-only from the record; the treatment code was not separately checked |
| harvest-7:2 | Quercus variabilis / sense_light_nonvisual | m | requote | Quote verbatim but carries no result; requoted to the 16-word ground-diameter sentence. Far-red sentence confirmed. Full text is on the MDPI page; only the abstract was checked, `partial` stays true |
| harvest-7:3 | Verbascum phlomoides / sense_light_nonvisual | m | correct | Full text open (MDPI). Quote verbatim. Authors restored with diacritics. The paper contradicts itself on PPFD (Methods: blue 173, red 299; abstract and Results: blue highest, red lower); note records it. `partial` to false |
| harvest-7:4 | Euphorbia pulcherrima / sense_light_nonvisual | m | correct | Full text open (ASHS HTML). Quote verbatim; 18% confirmed in Results. Authors were missing: Mata DA, Botto JF (CONICET repository). `partial` to false |
| harvest-8:1 | Medicago truncatula / sense_light_nonvisual | m | confirm | Full text open (MDPI). Sentence verbatim in the Discussion, 20 words. Discussion speaks of "an important role of phyA inputting light information into the clock to induce photoperiodic flowering" |
| harvest-8:2 | Medicago truncatula / diel | m | correct | Quote cut mid-sentence with no marked cut (whole is 44 words); requoted to the 39-word Results sentence with the periods (23.82 h mutant, 26.65 h wild type). Value gains the periods; method is leaf movement. `partial` to false |
| harvest-9:1 | Viola ×wittrockiana / sense_light_nonvisual | m | confirm | Abstract on the ASHS page: second sentence, verbatim. Runkle & Heins, JASHS 128(4):479-485, July 2003, DOI confirmed on Crossref. The 2001 paper's abstract lists V. ×wittrockiana among five species and says the FRd filter "delayed flower initiation", which supports the note's guess at the primary source |
| harvest-9:2 | Salvia hispanica / sense_light_nonvisual | m | unverifiable | Publisher PDF (api.fspublishers.org) blocked at the permission step; OpenAlex rate-limited. Crossref confirms title, the seven authors and 22(5), and gives the year as 2025; IJAB volume 22 is the 2019 volume, so the year needs a look when the page opens |
| harvest-10:1 | Verbascum phlomoides / sense_light_nonvisual | m | correct | Quote verbatim, 13 words. Conditions said red had lower PPFD, from the abstract; Methods gives red 299, blue 173. Conditions and note corrected. `partial` to false |
| harvest-11:1 | Medicago truncatula / sense_light_nonvisual | m | correct | Full text open (MDPI). Abstract sentence verbatim, 23 words. Method said cotyledon movement; Methods say "vertical leaf motion". Periods confirmed and added. `partial` to false |
| harvest-11:2 | Fragaria vesca / sense_light_nonvisual | m | confirm | OUP page: abstract sentence verbatim, one sentence; P8 "greatly increased plant height and reduced anthocyanin content". Authors, 10(12), uhad232 confirmed. Introduction to most of Methods visible on the page |
| harvest-11:3 | Populus tremula × P. tremuloides / sense_light_nonvisual | g | correct | Springer abstract (paywalled). Quote verbatim; the whole sentence is 41 words and continues after "shortening", so the cut is now stated as certain. Author list dropped the ninth (last) author, Eriksson ME; all nine given with diacritics |

**Rate: 8 errors in 11 verifiable records, 73%** (1 unverifiable). By verdict: 1 requote, 7 correct, 0 retract; 3 confirm.

## Wanted lines

| file | paper | check |
|---|---|---|
| harvest-8 | Molina-Contreras et al. 2019, Plant Cell 31(11):2649-2663, 10.1105/tpc.19.00275 | Authors (14, in order), year, volume, pages match the Universitat Jaume I repository record; the DOI resolves to academic.oup.com/plcell/.../31/11/2649. Matches. A PMC copy exists (PMC6881134; captcha here), so `get` could point there |
| harvest-9 | Baumhardt et al. 2014, Brain Behav Evol, 10.1159/000357750 | The DOI resolves to Karger bbe 83(3):181 with the title slug matching; the Karger page itself was blocked, so the author list is unconfirmed. The line lacks volume and pages (83(3):181-). Search shows a copy on the senior author's Purdue lab site, not opened here |
| harvest-10 | Castronuovo et al. 2016, Int J Plant Biol 7(1):6281, 10.4081/pb.2016.6281 | Authors, title, volume, article number and date (25 July 2016) match the Crossref record |

## Checks

- **Partial flag.** Six records were logged `partial` from page summaries although their sources are open in full; reading the relevant sections settled them (harvest-7:1, 7:3, 7:4, 8:2, 10:1, 11:1).
- **Metadata.** Two author lists were wrong: harvest-7:4 had none, harvest-11:3 lost its last author. harvest-7:3 had stripped diacritics.
- **Source contradiction.** The mullein paper (harvest-7:3, harvest-10:1) states PPFD both ways. Any row built on "red had lower light" should wait for the owner's reading.
- **Quotes.** One unmarked mid-sentence cut (harvest-8:2), one cut whose `where` hedged (harvest-11:3), one quote with no result in it (harvest-7:2).
- **Values.** Every value that opened stood; harvest-8:2 and harvest-11:1 gain measured periods.

## Rows written

`recheck-19.jsonl`: 8 rows: harvest-7:1, 7:3, 7:4, 8:2, 10:1, 11:1, 11:3 (`correct`); harvest-7:2 (`requote`).

## Blocked pages

- Permission step not answered: api.fspublishers.org PDF for 10.17957/ijab/15.1142; karger.com (Article/FullText/357750 and the bbe article-abstract page).
- Rate limited (HTTP 429): api.openalex.org; api.crossref.org for 10.1105/tpc.19.00275 and 10.1159/000357750 (two other Crossref records opened).
- pmc.ncbi.nlm.nih.gov/articles/PMC6881134 captcha; digital.csic.es and ddd.uab.cat bot walls.
- journals.ashs.org HTML for HortScience 50(4) failed; the PDF route opened.
