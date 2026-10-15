# Precision audit 15, 15 October 2026

Scope: every evidence record in sweep-96 and sweep-97. The audit covers 14 records (sweep-96: 8, sweep-97: 6) and the six wanted lines of the same sweeps. No sampling; all were opened.

Method as in audits 13 and 14: each source opened with WebFetch and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces of at most about 125 characters, with split points in `where`; corrected quotes are 40 words or fewer. Verdicts: `confirm`, `requote`, `correct`, `retract`, `unverifiable`. Typographic differences count as `confirm`; a change to the partial flag or the grade counts as `correct`. Corrections are in `docs/views/recheck/recheck-15.jsonl` in the recheck-5 schema. No evidence file, no wanted file and not `docs/views/audit/ALL.jsonl` was edited.

## Table

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| sweep-96:1 | Agelaius phoeniceus / binocular_deg 51.46 | m | confirm | verbatim in the open PDF (UNL Digital Commons), Results, "Visual Field Configuration". The sentence runs across the page break from p. 12 to p. 13 with the Figure 4 caption between, after "at the horizontal". 8 of 10 birds at rest, as filed. Location fixed in a row that is not counted |
| sweep-96:2 | Agelaius phoeniceus / fov_h_deg 316 | m | confirm | verbatim, one piece, p. 13 (filed as p. 12; location row, not counted) |
| sweep-96:3 | Agelaius phoeniceus / acuity_cpd 9.22 | m | confirm | verbatim, p. 13, "Retinal Ganglion Cell Density and Distribution". The authors' own anatomical estimate (Williams and Coletta 1987 equation) from one eye of each of five males. The `eye` field "both eyes, eyes at rest" was copied from the visual field records; fixed with the page in a row that is not counted |
| sweep-96:4 | Egregia menziesii / sense_light_nonvisual | m | confirm | verbatim, p. 26, Results, "Sporophyte production"; the sentence there refers to Egregia alone (p. 23 has the same words for Macrocystis and Nereocystis together). Egg timing: "Macrocystis and Egregia both produced eggs faster at 100 than at 20 μE·m−2·s−1 and 40 μE·m−2·s−1" (p. 21-22). Methods p. 13 say "four light treatments" but list three. The thesis names no family; the blank field stays |
| sweep-96:5 | Sideroxylon obtusifolium / sense_light_nonvisual | m | confirm | verbatim, Resultados e Discussão, with a line break inside. Table 1 at 30 °C: white 79 aA, dark 66 bA; 8 h light, four replicates of 25 seeds. The journal's article page prints DOI 10.25066/agrotec.v35i1.10254, which the record left blank (metadata row, not counted) |
| sweep-96:6 | Epacris tasmanica / sense_chemical | m | confirm | verbatim (CSIRO abstract), split after "The most effective treatment for"; the sentence continues "; however, germination with direct smoke was delayed by about two weeks". "A small fraction (5.3%) of non-dormant E. tasmanica seed could germinate in the absence of fire-related cues." Abstract only; metadata matches |
| sweep-96:7 | Malaclemys terrapin / receptor_classes 4 | m | confirm | verbatim on the Drexel record; the page does not say how the cones were identified, as the method field says. The open PDF was refused at the permission step, so the flag stands until someone reads it |
| sweep-96:8 | Malaclemys terrapin / spectral_range_nm | m | confirm | verbatim; the sentence reads "...modeled their sensitivity in the UV, blue, green and red portions of the electromagnetic spectrum (~355-640 nm)". "about 355-640" keeps the source's tilde |
| sweep-97:1 | Carex pensylvanica / sense_light_nonvisual | m | confirm | both sentences verbatim (experts.umn.edu); the abstract's own words are "an obligate short-day plant that does not require vernalization". No open full text; metadata matches |
| sweep-97:2 | Carex brevior / sense_light_nonvisual | m | correct | quote verbatim (USU abstract, Key Results), but the value gives red replacement and far-red reversal to "the other tested Carex". The abstract says red light replaced white "in all species" and far-red reversed it "in all species, except C. stipata", so C. brevior is included. Value corrected; flag kept, since the full text was refused |
| sweep-97:3 | Panicum virgatum / sense_light_nonvisual | m | requote | the quote stops mid-sentence before the result; the sentence continues "(decreasing or increasing daylength <12 h) with a less synchronized dormancy-breaking pattern than prairie cordgrass." Requoted to the whole sentence (23 words); the note now names the upland ecotype |
| sweep-97:4 | Thelypteris dentata / sense_light_nonvisual | m | confirm | verbatim (UNESP), split after "far-red"; "phytochrome control through the low fluence response" is in the abstract. The repository spells the second author "Takak, M." (the record says so) and gives no DOI, only Handle 11449/38123 and WOS:A1992KD93700014; access restricted, so the flag stands |
| sweep-97:5 | Cephalanthera sp. / sense_light_nonvisual | g | confirm | verbatim (Bayreuth eref), split after "the major"; the page names neither species, so genus level and `g` are right. The value matches "Low light levels result in strong myco-heterotrophy while higher irradiances successively drive the orchids towards autotrophy." |
| sweep-97:6 | Ciconia ciconia / binocular_deg | g | confirm | verbatim (Tethys), split after "binocular fields typical"; "in storks head movements of 55° are necessary". The quoted sentence covers all three species, so `g` stands; a stork-only width from the full text would be `m`. Authors match the page ("Martin, G.; Shaw, J.") |

**Rate: 2 errors in 14 verifiable records, 14%** (0 unverifiable). Every quote is verbatim. One error is a value that misreads the abstract's scope ("in all species"); the other is a quote cut before the words that carry the value.

## Checks the desk asked for

- **Abstract-only records carry `partial: true`.** Yes for all ten abstract records (96:6 to 96:8, 97:1 to 97:6). The three Red-winged Blackbird records and the two thesis and journal PDF records (96:4, 96:5) were read in full text and are `partial: false` by omission, correctly.
- **Records with `partial: true` whose full text is open.** Two candidates. The Dominy thesis PDF (96:7, 96:8) is marked "Open Access (License Unspecified)" on the Drexel record, but the PDF address was refused at the permission step, as it was at filing; the flag stays until it is read. The Kettenring et al. paper (97:2) may be open on the publisher's site; doi.org was refused, so that is unchecked. The other abstract sources show no open full text (CSIRO, UMN, SDSU, UNESP "Acesso restrito", Bayreuth, Tethys).
- **Pooled or unnamed-species records are `g`.** Cephalanthera sp. (97:5) and the three-species sentence of 97:6 are `g`. Every other record names one species and is `m`.
- **Encyclopedia and database sources.** None.
- **Values quoted from another study.** None. Every value is the source's own result.
- **Converted or estimated values.** None converted. The acuity of 96:3 is the authors' anatomical estimate, logged as they give it and labelled so in method and note.
- **Plant trait keys.** All seven plant and alga records use `sense_light_nonvisual` or `sense_chemical` for the source's own response: sporophyte output by light level (96:4), photoblastism (96:5), smoke-cued germination (96:6), photoperiodic flowering (97:1), light-dependent germination (97:2, 97:4), dormancy break under photoperiod (97:3) and light-driven carbon source (97:5). The value of 97:2 overstated what was specific to other species (corrected).
- **Metadata.** All sources match the opened pages. Blank DOIs: 96:5 now has one from the journal page; 97:4 has none to find (1992, no DOI on the repository record, which gives a Handle and a Web of Science ID instead). No authors field is blank.

## Wanted lines (not edited)

- **sweep-96, Baskin and Baskin 1992.** Confirmed on the University of Kentucky scholars page: Jerry M. Baskin, Carol C. Baskin; Plant Species Biology 7(2-3): 61-68; 10.1111/j.1442-1984.1992.tb00219.x. Its abstract says nothing about light or darkness, so the line's hope that the full text states a light requirement is untested.
- **sweep-96, Gilmour, Crowden and Koutoulis 2000.** Confirmed on the CSIRO page: Craig A. Gilmour, Ronald K. Crowden, Anthony Koutoulis; Aust. J. Bot. 48(5): 603-609; 10.1071/BT99029.
- **sweep-96, Dominy 2015.** Confirmed on the Drexel record: Abigail Elizabeth Dominy, PhD, 1 April 2015; 10.17918/etd-6335. The PDF is open but the fetch tool cannot take it.
- **sweep-97, Martin and Shaw 2010.** Confirmed on Tethys: "Martin, G.; Shaw, J."; Biol. Conserv. 143: 2695-2702; 10.1016/j.biocon.2010.07.014. No issue number on the page.
- **sweep-97, Flores et al. 2011.** Confirmed on CONICET (ri.conicet.gov.ar/handle/11336/13071): 15 authors in the line's order; Environ. Exp. Bot. 71(1): 79-88; 10.1016/j.envexpbot.2010.10.025. The record prints accents the line drops (Dávila, León, Ordóñez, Ramírez Bullón). It marks the item open access, though no file is attached. Neither Escobaria nor Pelecyphora appears on the page.
- **sweep-97, Hornych et al. 2021.** Authors, year, New Phytol. 229(1): 607-619 and 10.1111/nph.16836 confirmed on the Pherobase literature record E/12167. A search lists the paper in PubMed Central (PMC7754499), so `get: "journal via library"` likely understates its access; the PMC page returned a reCAPTCHA. The NSF PAR record gives volume and pages but leaves authors and DOI blank. Thelypteris is not mentioned on either page reached.

## Rows written

`recheck-15.jsonl`: 6 rows.

- Counted: 97:2 (`correct`, value and note), 97:3 (`requote`, quote, where and note).
- Not counted: 96:1 and 96:2 (`correct`, page location), 96:3 (`correct`, `eye` field and page location), 96:5 (`correct`, DOI filled from the journal's article page, note updated).

## Blocked pages

- The Drexel full-text PDF (researchdiscovery.drexel.edu/esploro/fulltext/...) was refused at the permission step.
- doi.org/10.1093/aob/mcl170 and the Europe PMC REST query for it were refused at the permission step.
- pmc.ncbi.nlm.nih.gov (PMC7754499) returned a reCAPTCHA page.

## Patterns (this run)

1. A summary value can misread the scope of an abstract sentence. 97:2 gave "in all species" results to the other species only, which an abstract-only record cannot afford, since the abstract is all the record has.
2. Fragment quotes recur (97:3, and 97:4 and 97:5 are phrases too). Audit 14's pattern 2 holds: a fragment that stops before the result fails, while one that carries the result can pass. Quoting the full sentence at filing settles it.
3. Fields copied from a neighbouring record (96:3's `eye` from the visual field rows) and page numbers given for a whole run of records drift from the source. Each record's `where` and `eye` should be set from its own sentence.
4. A journal's article landing page can carry a DOI the PDF does not print (96:5). One fetch of the landing page at filing fills the field.
