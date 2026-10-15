# Precision audit 11, 15 October 2026

Two parts. (a) A random sample of 20 evidence records from sweep-76 to sweep-79, each opened at its source and checked for value, grade, partial flag and a verbatim quote, and the batch recheck that the error rate calls for. (b) Records named by the desk outside the sample: the Amnirana and Papurana entries of sweep-78, the Ctenomys records of sweep-78 and the Spalax and Paratrigona records of sweep-79.

Method as in audits 6 to 10: each source opened with WebFetch and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces of at most about 125 characters, with split points in `where`; corrected quotes are 40 words or fewer. Verdicts: `confirm`, `requote`, `correct`, `retract`, `unverifiable`. Typographic differences count as `confirm`; a change to the partial flag or the grade counts as `correct`. Corrections are in `docs/views/recheck/recheck-11.jsonl` in the recheck-5 schema. No evidence file and not `docs/views/audit/ALL.jsonl` was edited.

## Part (a): random sample of sweep-76 to sweep-79

sweep-77 has no evidence file. The other three hold 22 records (sweep-76: 4, sweep-78: 10, sweep-79: 8). Two were drawn from each file and 14 more from the remainder (Python `random`, seed 20261015). Not drawn: sweep-78:3 and 78:4, both Ctenomys records the desk named, so they were checked in part (b) and are not counted.

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| sweep-76:2 | Sphaerodactylus parkeri / fovea | m | confirm | first clause verbatim (Oxford Academic page); cited to Underwood (1951) on the page; already `partial: true` |
| sweep-76:1 | Dalmatolacerta oxycephala / lambda_max_nm | g | confirm | abstract sentence verbatim in two pieces, as the record splits it; Table 4 (p. 2904) row reads F at site 86, S at site 90, JQ917102 |
| sweep-78:8 | Ctenomys magellanicus / receptor_classes | m | correct | quote verbatim (CONICET abstract); abstract-only record without `partial: true`, now partial |
| sweep-78:10 | Ctenomys talarum / binocular_deg | m | confirm | "The region of maximum binocular overlap covered 60°" with a linked "(Fig. 1b)"; the paragraph is the C. talarum one (S. cyanus: 50°). Metadata row: the method is the ophthalmoscope reflex technique, two animals per species |
| sweep-79:1 | Chrysolophus / binocular_deg | m | correct | quote verbatim (author's PDF); a value pooled over two species ("when both species were combined") is a group value, held to `g` as audit 8 ruled |
| sweep-79:7 | Anilios bicolor / receptor_classes | m | confirm | verbatim (LSTM repository PDF, hyphen at "ge-netic"); "both species" are the two Anilios, named in the Fig. 2 caption; A. bicolor came from an eye transcriptome, A. bituberculatus from genome-wide data |
| sweep-76:4 | Sphaerodactylus parkeri / pupil_shape | m | requote | the quote drops the parenthesis "(as well as other more recently nocturnal geckos, such as S. roosevelti)" without a mark; the sentence restored (37 words) |
| sweep-76:3 | Sphaerodactylus macrolepis / fovea | m | correct | phrase verbatim (it continues "; Figure 2D–I)"), but the paper photographed S. macrolepis embryos for eye shape only and shows no fovea; its only histology is of Aristelliger lar. The label rests on earlier literature: now `partial: true`, method corrected |
| sweep-78:9 | Ctenomys talarum / fov_h_deg | m | confirm | verbatim in two pieces; metadata row for the method and the author list (the Nature page prints its own ellipsis) |
| sweep-78:2 | Ctenomys talarum / lambda_max_nm 510 | m | correct | as 78:8; the note's "both species together" is not in the abstract, note corrected |
| sweep-78:7 | Ctenomys magellanicus / lambda_max_nm 450 | m | correct | as 78:2 |
| sweep-78:5 | Ctenomys magellanicus / lambda_max_nm 370 | m | correct | as 78:2 |
| sweep-79:2 | Lerista / receptor_classes | g | confirm | verbatim (bioRxiv PDF, Conclusions); "39 Lerista and 20 Ctenotus species from gene capture" and "no stop codons or frameshift mutations" also verbatim; L. bougainvillii absent from the text, as the conditions say |
| sweep-79:5 | Spalax ehrenbergi / lambda_max_nm | m | confirm | verbatim (Haifa CRIS abstract): "... all functional characteristics of a rod visual pigment (λmax) = 497 ± 2 nm; ..."; baculovirus expression |
| sweep-79:4 | Spalax ehrenbergi / receptor_classes | m | confirm | verbatim, sentence ends "that have rendered the gene nonfunctional."; the abstract itself says "we demonstrate that Spalax is a LWS monochromat", by immunocytochemistry and molecular approaches |
| sweep-79:3 | Paratrigona / receptor_classes | m | correct | quote verbatim (USP repository); a genus record from one member printed "Paratrigona sumuda", a name matching no species, so held to `g`. Authors from the page's generated citation added |
| sweep-78:6 | Ctenomys magellanicus / lambda_max_nm 510 | m | correct | as 78:2 |
| sweep-79:6 | Anilios bituberculatus / receptor_classes | m | confirm | as 79:7 |
| sweep-79:8 | Chinchilla lanigera / receptor_classes | m | confirm | verbatim (HUJI CRIS abstract); "immunohistochemistry (IHC) was conducted to detect the presence of short and medium/long wavelength cone photoreceptors"; already `partial: true` |
| sweep-78:1 | Ctenomys talarum / lambda_max_nm 370 | m | correct | as 78:2 |

**Rate: 10 errors in 20 verifiable records, 50%** (0 unverifiable). Quotes are clean in 19 of 20; one was trimmed inside a sentence without a mark. The errors are three kinds:

- Six Schleich et al. 2010 records filed from the abstract without `partial: true`. Every abstract-only sweep record from sweep-8 to sweep-79 carries the flag, and `gaps.py` uses it to tell an abstract from a full text; sweep-78 is the only exception.
- Two group values graded `m`: Chrysolophus (two species pooled) and Paratrigona (a genus record from a misprinted member).
- Two Griffing et al. 2026 records: one requote, and one value (S. macrolepis foveated) that the paper asserts without data of its own.

**Batch recheck.** The rate is above 5%, so the whole of each file the errors came from was to be rechecked. Between the sample and part (b), all 22 records in sweep-76, 78 and 79 were opened, so the batch recheck is complete. It adds two errors outside the count (sweep-78:3 and 78:4, the same missing flag).

## Part (b): records named by the desk

**Ctenomys, Schleich et al. 2010 (sweep-78:1 to 78:8).** Values confirmed: the abstract (CONICET record, DOI 10.1002/cne.22440 under `dc.relation.alternativeid`) gives the three templates at 370, 510 and 450 nm and the L and S opsin split (a 6–16% S minority). Species: both C. talarum and C. magellanicus are named, and the S opsin sentence opens "In both species". The ERG sentence reads only "Photopic spectral electroretinograms were recorded." with no species, so the records' assignment of the ERG values to both species is how the abstract reads and nothing more. The full text was not reached: CONICET lists no file, the Wiley PDF link from Semantic Scholar failed, and Europe PMC answered 429. Vega-Zuniga et al. 2017, which shares an author, cites the paper only for cone proportions ("10–14% for C. talarum", "10–30% for Ctenomys magallanicus") and never mentions an ERG. All eight rows now carry `partial: true`, and the lambda notes say the ERG species is unconfirmed. Not retracted.

**Ctenomys, Vega-Zuniga et al. 2017 (sweep-78:9, 78:10).** Full text on nature.com. Species and values confirmed: the C. talarum paragraph gives the 170° monocular field (−25° to 145°) and the 60° maximum binocular overlap, dorso-rostral between 30° and 60° elevation; the 40° dorso-caudal figure and the −30° vertex are in the same paragraph. Two animals per species were measured and one is shown. Metadata rows (not counted) fill in the method and the authors.

**Spalax (sweep-79:4, 79:5)** and **Paratrigona (sweep-79:3)**: see the table; the Spalax pair stands, Paratrigona is regraded to `g`.

**Amnirana and Papurana.** sweep-78 holds no evidence record for either genus. The desk's description fits the two searched-log lines (`docs/views/searched/sweep-78.jsonl` lines 11 and 27), which chased the bioRxiv preprint 10.1101/2021.08.15.456426 and found nothing. The preprint was opened: neither "Amnirana" nor "Papurana" occurs, nor galamensis, nicobariensis or daemeli. "Hylarana albolabris" appears once, in the Figure 1 caption, and species data are deferred to "the supplementary data files". The sweep agent's statement is confirmed. No value rests on the preprint, so there is nothing to confirm, regrade or retract, and no row was written. The Amnirana pupil cell in `gaps/` points at oa-2:2040, which cites the NHM dataset (10.5519/4q5uvvpa) and was outside this audit.

## Rows written

`recheck-11.jsonl`: 14 rows.

- Counted: 76:3 (`correct`), 76:4 (`requote`), 78:1, 78:2, 78:5 to 78:8 (`correct`, partial flag and note), 79:1 and 79:3 (`correct`, grade to `g`).
- Not counted: 78:3 and 78:4 (same flag defect, outside the sample); 78:9 and 78:10 (method and authors, metadata only).

## Blocked pages

- Europe PMC REST answered 429 for the Schleich et al. search; not retried.
- The Wiley `pdfdirect` link for Schleich et al. 2010 returned a fetch error; the CONICET record has no file.
- The shell has no route to any publisher host, so every page was read through WebFetch.

## Patterns (this run)

1. A new sweep agent dropped the abstract flag. sweep-78 is the first sweep since sweep-8 to file abstract-only records without `partial: true`; the addlog check could require the flag whenever `access` is "abstract".
2. Pooled and genus-level values keep arriving as `m`. When a record's `taxon` is a genus, the grade is `g` unless the desk rules otherwise.
3. Papers that classify a species in passing (a "foveated gecko") get logged as if they measured it. The test is whether the paper's own methods touch the trait in that species.
