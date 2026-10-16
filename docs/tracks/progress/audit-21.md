# Precision audit 21, 16 October 2026

Scope: 20 records from 17 evidence files that no earlier audit table, recheck file or retract row had touched, then 17 follow-up records from the files where errors turned up. Main draw: canon-9 (3), canon-3 (1), intake-4 (1), intake-7 (1), sweep-21 (1), sweep-27 (1), sweep-29 (1), sweep-38 (1), sweep-43 (1), sweep-48 (1), sweep-52 (1), sweep-55 (1), sweep-59 (1), sweep-62 (1), sweep-63 (2), sweep-66 (1), sweep-74 (1). Taxa: insects 6, fish 3, birds 3, mammals 3, plants 3, reptiles 2. Seventeen at `m` and three at `g` before the audit.

Method as in audits 13 to 20: each source opened with WebFetch (WebSearch only to locate an open copy) and asked first whether the exact quote string appears, then for the page's own sentence or row. Metadata checked against the opened page, or against Crossref where the page showed less. A change to the partial flag, the grade, the method or a bibliographic field counts as `correct`. Following audit 14, a fragment that carries the value passes; a space before "deg." where the logged quote has none is treated as a rendering difference. Corrections are in `docs/views/recheck/recheck-21.jsonl` in the recheck-5 schema. No evidence file, no wanted file and not `docs/views/audit/ALL.jsonl` was edited.

## Table

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| canon-9:2 | Orthetrum albistylum / opsin_gene_count 10 LW | g | correct | PMC4371951: abstract quote verbatim. Results: O. albistylum RNA-seq "yielded the same set of 20 opsin genes". Measured in the species, as audit 20 found for canon-9:1. Grade to `m` |
| canon-9:3 | Ladona fulva / opsin_gene_count 5 SW | g | correct | Same page. The L. fulva draft genome (APVN01000000) "identified the same set of 20 opsin genes" and "confirmed no other opsin genes in the genome". Grade to `m` |
| canon-9:4 | Ladona fulva / opsin_gene_count 10 LW | g | correct | As canon-9:3. Grade to `m` |
| canon-3:690 | Carassius auratus / cff_hz 67.2 | m | correct | TARA accepted manuscript, Table 1, p. 3. The logged quote is a piped rebuild of the row; printed "Carassius auratus 67.2e,o,7 10.833 0.0001328 0.0171 H". Superscripts give ERG and optimum methodology (source 7, Hanyu & Ali 1963), so the method field's "not stated in the table" is wrong. Requoted; method corrected. 86(4):685-696 on Crossref |
| sweep-66:6 | Ceratosolen gravelyi / acceptance_deg 10.0 | m | confirm | MDPI: verbatim in 3.3; eight authors and 16(7):682 confirmed |
| sweep-52:4 | Empoasca onukii / acuity_cpd 0.28 | m | confirm | MDPI: abstract sentence verbatim; acuity is the reciprocal of the dorsal Δϕ (3.57°) measured on 3D digital microscopy. Seven authors and 14(4):370 confirmed |
| sweep-63:3 | Lycaon pictus / tapetum | m | confirm | DOAJ record of the abstract: quote verbatim. The sentence continues "arranged in a bricklike structure", so the `where` claim that it was returned whole is loose. Three authors with diacritics, 16(4): e0249368 confirmed |
| sweep-63:8 | Rhabdomys pumilio / receptor_classes 2 | m | correct | PLOS full text: abstract sentence verbatim; 13(8): e0202106 confirmed. Authors had lost their diacritics (Lukáts, Bláhová, Němec); restored, with "van der Merwe" as printed |
| sweep-62:3 | Oxybelis fulgidus / receptor_classes | m | correct | UNESP PDF, Table 3: all five pieces of the row found verbatim; 6.4, 1.4, 0.1, 92.3% confirmed; two retinas of one animal; LWS by subtraction. The record had no DOI; the PDF prints 10.1002/cne.70092, added |
| sweep-74:3 | Helicops angulatus / lambda_max_nm 495 (rod) | m | confirm | OUP page: "In H. angulatus, we found rods with maximum absorbance at 495 ± 2 nm (n = 11)"; one wild-caught individual. Journal field lacks pages (5225-5240) |
| sweep-21:5 | Manduca sexta / interommatidial_deg 1.24 | m | correct | Sponberg lab PDF. The quote was a verbatim clause without the value; requoted to the Table 1 row ("1.24+-0.81"). The empty DOI is now the printed bioRxiv DOI 10.64898/2026.04.28.721382. Δφ has no stated unit; note says so |
| sweep-55:1 | Anous stolidus / binocular_deg 15 | m | confirm | Springer, open (CC BY): item (2) verbatim in two pieces; ophthalmoscopic reflex technique. Page shows "Lucas, E.A., Martin, G.R., Rocamora, G. et al." and contribution initials for four people, matching the four names logged |
| sweep-38:2 | Picris willkommii / sense_light_nonvisual | m | confirm | MDPI: verbatim in 2.2.2, with the preceding and following clauses as the `where` gives them. 11(15):1981 confirmed |
| intake-7:17 | Sphyrna lewini / binocular_deg 34 | m | confirm | JEB article page (full text free): abstract prints "(34 deg.)"; the fragment carries the value. Table 1: 34.4 ± 2.6 morphological, 31.7 ± 3.7 physiological (± s.e.m.). `access: closed` understates; the journal field lacks the issue (24) |
| intake-4:24 | Acanthochromis polyacanthus / cff_hz 89.0 | m | confirm | JEB page: "control group (89.0±1.6 Hz)" verbatim in Results; fERG at 29 ± 1 °C, clove oil and pithing. Page shows a subscriber notice, so `access: closed` stands |
| sweep-48:6 | Puffinus pacificus / spectral_range_nm | m | confirm | JEB abstract page: last sentence verbatim; VS 406, SWS 450, MWS 503, LWS 566 and rod 502 nm confirmed. Full text paywalled; `partial: true` right |
| sweep-59:2 | Thomomys bottae / lambda_max_nm 367 | m | confirm | Springer abstract: both pieces verbatim; ERG. Journal field lacks the issue (2) |
| sweep-27:2 | Albizia julibrissin / sense_light_nonvisual | m | confirm | Springer abstract: "When given prior to a dark period, red light facilitates and far-red light inhibits pinnule closure in the dark." Blue-light reopening confirmed. Planta 77:135-141 |
| sweep-29:5 | Cuculus poliocephalus / oil_droplets | m | confirm | Kobe repository PDF: Results sentence verbatim; Table I names the Little Cuckoo C. poliocephalus. 41(4):127-139, 1995 |
| sweep-43:3 | Cucurbita foetidissima / sense_chemical | m | confirm | Springer (CC BY): verbatim in Results, "Identification of EAG-active Compounds". The authors field stops at "et al."; the contributions list six people (AS, SR, KKB-D, NBM, AJM, MML-U), but the page gave no full names, so the list was not completed |

**Rate: 7 errors in 20 records, 35%** (none unverifiable). By verdict: 7 correct, 0 requote, 0 retract; 13 confirm.

### Follow-up draw (errors found, so more from the same files)

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| canon-3:684 | Ambystoma tigrinum / cff_hz 30 | m | correct | Printed "Ambystoma tigrinum 30e,s,1 10.7828 0.0001628 NA L"; piped quote rebuilt, ERG and suboptimum methodology stated by the table. Requoted; method corrected |
| canon-3:686 | Anolis cristatellus / cff_hz 70 | m | correct | Printed "Anolis cristatellus 70e,o,3 6.029 0.0008929 NA H". Same fault |
| canon-3:691 | Carcharhinus acronotus / cff_hz 18 | m | correct | Printed "…18e,o,8 14491.08 0.0011456* NA L". Same fault |
| canon-3:704 | Negaprion brevirostris / cff_hz 37 | m | correct | Printed "…37e,s,18 92987.044 0.0005362* NA L". Same fault |
| canon-3:705 | Oncorhynchus mykiss / cff_hz 27 | m | correct | Printed "…27b,s,19 4000.045 0.0004128 0.571 L"; behavioural. Same fault |
| canon-3:706 | Oryzias latipes / cff_hz 37.2 | m | correct | Printed "…37.2e,s,20 0.2120 0.0007228 0.0177 L". Same fault |
| canon-3:711 | Sphenodon punctatus / cff_hz 45.6 | m | correct | Printed "…45.6b,s,24 353.7550 0.0001728 NA L"; behavioural. Same fault |
| canon-3:712 | Sphyrna lewini / cff_hz 27.3 | m | correct | Printed "…27.3e,o,8 1893.08, 51 0.001065* 60.077 L". Same fault |
| canon-3:716 | Thunnus albacares / cff_hz 80 | m | correct | Printed "…80e,s,26 45349.053, 54 0.0015868* 6.2477 H". Same fault |
| intake-7:16 | Eusphyra blochii / binocular_deg 48 | m | correct | JEB: abstract "(48 deg.)"; Table 1 repeats 48.3 ± 2.7 under both methods because only dead wingheads were obtained. The method field said physiological retinal scan on anaesthetised animals; corrected to morphological |
| intake-7:18 | Sphyrna tiburo / binocular_deg 13 | m | confirm | Abstract "bonnethead sharks (13 deg.)"; Table 1 13.4 ± 0.7 physiological, 16.4 ± 0.5 morphological, as the note says |
| intake-7:19 | Negaprion brevirostris / binocular_deg 10 | m | confirm | Abstract "lemon (10 deg.) and blacknose (11 deg.) sharks"; Table 1 10.0 ± 1.5 and 11.8 ± 0.7 |
| intake-7:20 | Carcharhinus acronotus / binocular_deg 11 | m | confirm | Same sentence; Table 1 10.7 ± 1.3 and 13.6 ± 0.8 |
| sweep-63:6 | Rhabdomys pumilio / lambda_max_nm | m | confirm | City repository: abstract passage verbatim; nine authors, JEB 223(11): jeb215368 confirmed; CC BY published PDF linked |
| sweep-62:5 | Acanthodactylus erythrurus / lambda_max_nm (UVS) | g | confirm | JEB PDF: "the short-sensitive photoreceptor of lacertids is likely of the UVS type" (Discussion); Table 4 lists JQ917084; exceptions L. agilis and M. simoni as the note says |
| sweep-21:3 | Phleum pratense / sense_light_nonvisual | m | unverifiable | Frontiers page not reached (permission step not answered) |
| sweep-21:14 | Nymphaea nouchali / diel | m | unverifiable | BMC figure page not reached (permission step not answered). The record's authors field reads "authors not shown on the page read" and should be filled when the page opens |

**Follow-up rate: 10 errors in 15 verifiable records, 67%** (2 unverifiable). Nine of the ten are one fault repeated across the Healy et al. 2013 rows of canon-3.

**Combined: 17 errors in 35 verifiable records, 49%** (2 unverifiable).

## Checks

- **Quotes.** The canon-3 Healy rows were logged as pipe-separated rebuilds ("Species | CFF | Mg | qWg | n"), and the last cell is in fact the source superscript of the CFF value. Every Healy row checked (10 of 10) has this form, and canon-3:715, corrected in an earlier audit, has it too; the remaining Healy rows in canon-3 (685 to 689, 692 to 703, 707 to 710, 713, 714, 717) very likely share it and should be requoted as a batch. The logger's caution that reference numbers run into the mass and metabolic-rate cells holds (trailing 28 and 29 match reference-list entries) and is kept.
- **Method.** The same rows say the method is not in the table, but Table 1's notes define the superscripts (e electroretinogram, b behavioural; o optimum, s suboptimum methodology). intake-7:16 gave a physiological method for a species the paper measured only on dead animals.
- **Grade.** canon-9:2 to 9:4 raised to `m`, completing the change audit 20 made for canon-9:1.
- **Metadata.** Two missing DOIs added (sweep-62:3, sweep-21:5); one author list restored with diacritics (sweep-63:8). Not counted: journal strings that omit an issue or pages (sweep-74:3, sweep-59:2, intake-7:17), `access` set lower than the page allows (intake-7:17 to 7:20), and sweep-43:3, whose "et al." is honestly labelled but could not be completed from the page.
- **Partial flag.** No wrong flags found. sweep-21:5 stays `partial: true` because only the table and Methods were read.

## Rows written

`recheck-21.jsonl`: 17 rows, all `correct`: canon-9:2, 9:3, 9:4; sweep-63:8; sweep-62:3; sweep-21:5; canon-3:690, 684, 686, 691, 704, 705, 706, 711, 712, 716; intake-7:16.

## Blocked pages

Records whose pages could not be opened were dropped from the main draw before any check, and replaced.

- Permission step not answered: pmc.ncbi.nlm.nih.gov PMC6140104 (sweep-48:1) and PMC3745574 (sweep-39:3); discovery.ucl.ac.uk eprint 10104370 (sweep-51:2); nhm.openrepository.com item ec90bd73 (sweep-26:3); peerj.com/articles/14326 (sweep-44:3); cob.silverchair.com JEB 211/8/1203 PDF (sweep-66:4); www2.mdpi.com/1422-0067/2/4/156 (sweep-20:4); frontiersin.org 10.3389/fpls.2015.00465 (sweep-21:3); bmcplantbiol.biomedcentral.com s12870-018-1357-7 figure 1 (sweep-21:14).
- Rate limited (HTTP 429): zenodo.org file Behav_and_RGC_Data.csv (canon-5:194); api.crossref.org for 10.1007/s00114-024-01926-4 and 10.1007/s10886-025-01664-5.
- Robots disallowed: datadryad.org file stream 2840338 (canon-5:194).
- Fetch error: doi.org/10.1002/ece3.8595 (herps-met:1).
- journals.plos.org returned an unrelated article (Wynde & Port 2012) for article?id=10.1371/journal.pone.0249368 in both URL forms; the abstract was read on DOAJ instead.
