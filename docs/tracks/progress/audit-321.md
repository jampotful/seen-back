# audit-321: desk-d229, evidence lines 1 to 6

Audited 31 October 2026 from the desk-d229 files present untracked in the worktree (docs/tracks/progress/desk-d229.md and docs/views/evidence/desk-d229.jsonl, 12 lines; neither committed here, neither edited). HEAD and origin/main 412c2eb8 (desk-d228). Lines 7 and 8 repeat d228 on main and are dropped by the desk, so they are not audited here; audit 322 judges lines 9 to 12. `python3 -I tools/senses/check.py | grep d229`: "docs/views/evidence/desk-d229.jsonl: 12 records, 0 problems". Quote lengths (`len(q.split())`): lines 1 to 5, 33 each (one shared sentence); line 6, 29. Evidence records only, so the brief's search-record parts do not apply; audits 318 to 320 are the format model.

Sources opened (WebFetch): journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0103953 (two passes after three rate-limited attempts); journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0135888 (one pass after one rate-limited attempt); api.crossref.org/v1/works for 10.1371/journal.pone.0103953 and 10.1371/journal.pone.0135888; Eschmeyer's Catalog of Fishes (researcharchive.calacademy.org) spid 44175 and spid 48436; fishbase.se/summary/24117; obis.org/taxon/398460. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened; PMC and the repository PDF copies the search returned were not opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 3 WebSearches and 12 WebFetch calls used.

## Bibliographic and licence

- Lines 1 to 5, Wang et al. 2014. Page byline "Feng-Yu Wang, Wen-Chun Fu, I-Li Wang, Hong Young Yan, Tzi-Yuan Wang", as recorded and in Crossref order. Title verbatim on the page citation and Crossref: "The Giant Mottled Eel, Anguilla marmorata, Uses Blue-Shifted Rod Photoreceptors during Upstream Migration". Page citation "PLoS ONE 9(8): e103953."; Crossref PLoS ONE 9(8) e103953, issued 2014-08-07. Page licence: "This is an open-access article distributed under the terms of the Creative Commons Attribution License,"; Crossref CC BY 4.0, content-version unspecified, delay 0, relation empty, no update-to. Accepted under the "unspecified plus page-printed CC Attribution" rule. Met.
- Line 6, Sakata et al. 2015. Page byline "Rie Sakata, Ryo Kabutomori, Keiko Okano, Hiromasa Mitsui, Akihiro Takemura," "Tetsuya Miwa, Hiroyuki Yamamoto, Toshiyuki Okano", as recorded and in Crossref order. Title verbatim on Crossref. Crossref PLOS ONE 10(8) e0135888, issued 2015-08-14; the page citation line was returned only to the title, so the printed "PLoS ONE 10(8): e0135888" form is unchecked (Crossref agrees on volume, issue and number). Page licence "This is an open access article distributed under the terms of the Creative Commons Attribution License"; Crossref CC BY 4.0 vor, relation empty, no update-to. Met.

Bibliographic faults 0; licence faults 0.

## Names

- Anguilla marmorata: Catalog of Fishes spid 48436, verbatim: "Current status: Synonym of Anguilla marmorata Quoy & Gaimard 1824. Anguillidae." (Anguilla labrosa), so A. marmorata is the valid name, family Anguillidae. Order Anguilliformes as main's ten Anguilla anguilla rows. Met. (The species' own spid page was not opened; acceptance rests on a synonym pointing to it.)
- Careproctus rhodomelas: Catalog of Fishes spid 44175, verbatim: "Current status: Valid as Careproctus rhodomelas Gilbert & Burke 1912. Liparidae." Family met. **Order wrong for the desk's naming.** The record gives Scorpaeniformes from the paper's Fig 1A caption ("(A) Order Scorpaeniformes, Liparidae, snailfish."). FishBase prints "Perciformes/Cottoidei (Sculpins) > Liparidae (Snailfishes)"; OBIS (WoRMS backbone) for the congener Careproctus comus prints "Animalia > Chordata > Teleostei > Perciformes > Liparidae > Careproctus"; main files every Sebastidae row (desk-d194 lines 5 to 7, desk-d204 line 1) under Perciformes, accepted by audit 278 on OBIS. A paper's 2015 caption is not the naming authority. Counted as a names fault; fixable. The same question applies to this unit's Myoxocephalus thompsonii (Cottidae/Scorpaeniformes from GBIF), which audit 322 judges; an owner ruling would settle both.

Names faults 1 (line 6).

## Duplicates

git grep on origin/main (412c2eb8) across the whole docs tree (evidence, audit/corrected, audit/ALL, searched, sheets, gaps, batches, codex-findings, progress notes, compile notes) for "Anguilla", "marmorata", "0103953", "giant mottled", "Anguillidae", "Careproctus", "rhodomelas", "0135888", "Liparid", "snailfish", "Sakata". Hits: Anguilla only A. anguilla (cff_hz and sense_magnetic rows, audits 22, 246, 311); "marmorata" only other genera (Scaphiophryne, Kalanchoe, Ptenothrix, Actinemys); Sakata 2015 snailfish only as unread leads in desk-d184, d185, d187 and d188 progress notes (PLOS served other articles), never filed. No record repeats main. Duplicate faults 0.

Within the unit: lines 1 to 5 log five values from one sentence. Each is a separate stage-and-cell-type mean (rod: glass, cultured yellow, wild yellow; cone: cultured yellow, wild yellow), and the Results print the three rod means separately with their own SDs. Lines 2 and 3 share the value 489 but come from different fish groups (4 cultured, 2 wild), so they are separate measurements, not one value logged twice. None duplicates another. On the desk's owner question 3, the lines need not be merged; keeping them separate is consistent with the paper's per-stage reporting.

## Per-record findings

Shared quote for lines 1 to 5, Abstract sentence 7, verbatim in two pieces: "The λmax of rod cells are 493, 489, and 489 nm in glass, yellow, and wild eels," "while those of cone cells are 508, and 517 nm in yellow, and wild eels, respectively." MATCH, 33 words, one whole sentence (split only by the tool's length cap). Each value is in the quote; no line's value says more than the quote.

Methods confirmed verbatim: "The glass-stage eels (denoted as 'Glass') were collected from the mouth of the Hsiukuluan River"; "four specimens were bought from an eel farm"; "(the eels were 3-years-old, and are denoted as 'Cultured yellow'),"; "two specimens were caught upstream of the Laomei Stream"; "The sample sizes for each stage were as follows: 9 for Glass, 4 for Cultured yellow, and 2 for Wild yellow."; "After overnight dark adaptation inside a darkroom"; "and then enucleated under a dim red light."; "single-beam, computer-controlled, microspectrophotometer stage"; "If the SD of the λmax was smaller than 7.5 nm, then the spectrum was considered valid and collected for analysis."; "Approximately 40 measurements were obtained from each specimen." Method is MSP of photoreceptors, as recorded; the Ocean Optics spectrophotometer was used only for in situ light, not pigments. No silver eels: "silver" appears once, in the Discussion, about the European eel. Life-stage labels right; the abstract's "yellow" maps to cultured yellow on the rod means (Results "489±6.1 nm for cultured yellow eels", wild "489±5.1nm").

Results confirmed verbatim: "The mean λmax values of rod cells were 493±4.7 nm for glass eels and 489±6.1 nm for cultured yellow eels."; "No significant difference in λmax was observed between cultured and wild yellow eels (489±5.1nm)."; "The λmax of glass eel was significantly different from those of other stages" "(Table 2)."; "Only a single cone cell was observed in cultured and wild yellow eels."; "The mean λmax values of single cone cells are all in the range of green light spectra (Table 1)."; "Student's t-test showed that the λmax values between cultured yellow eel and other stages" "are significantly different (Table 2)." (this sentence follows the cone sentences; its place in the cone paragraph is tool order). Table 1 caption: "The mean λmax of photoreceptor cells from A. marmorata at different developmental stages, as measured using MSP." Discussion: "Here, we report that A. marmorata possesses only one type of cone cell, which senses a limited range" (continuing "of the light spectrum, i.e., from 500 nm to 535 nm", tool summary). Table cells did not render.

Shared fault in conditions and note (all five lines): (a) "the Results ... give no cone values or cone sample size in the text, so the 508 and 517 nm cone figures appear only in the abstract" is contradicted by the Results, which refer the cone means to Table 1 (the MSP table of mean λmax by stage); the cone values are very likely in Table 1, which neither the desk nor I read. (b) "the Results say only a single cone class was observed and only in cultured and wild yellow eels" rewrites the sentence: "only" in "Only a single cone cell was observed in cultured and wild yellow eels." governs "a single cone cell", not the stages, and the record then says the opposite ("the text does not say whether cones were found in glass eels"). Whether "a single cone cell" means one morphological class (single cones, as the Discussion's "only one type of cone cell" suggests) or literally one cell per stage is a live fork the record should print verbatim, not resolve. (c) Omitted for the cone lines: the t-test sentence saying cultured yellow differs significantly from the other stages (Table 2, no p values in text), which is the paper's statement that 508 and 517 nm differ.

### Line 1, rod 493 nm, glass eel

Rod value, label, method, n = 9, SD 4.7 and the significant glass-versus-other difference all right. **Error (shared cone misstatement (a) and (b) in conditions and note).** The rod content is correct; the fault is the shared text, fixable mechanically.

### Line 2, rod 489 nm, cultured yellow eel

Rod value right (489 ± 6.1, n = 4). **Error (shared cone misstatement (a) and (b)).** Fixable.

### Line 3, rod 489 nm, wild yellow eel

Rod value right (489 ± 5.1, n = 2, no difference from cultured). **Error (shared cone misstatement (a) and (b)).** Fixable.

### Line 4, cone 508 nm, cultured yellow eel

**Error (cone provenance misstated; sentence misread; significant cone difference omitted).** (a), (b) and (c) above. The cone SD and cell count are not given (Table 1 unread), and the record should say so rather than say no such figures exist. Fixable.

### Line 5, cone 517 nm, wild yellow eel

**Error (as line 4).** With n = 2 wild yellow eels, the Table 1 cone count may be small; unread. Fixable.

### Line 6, Careproctus rhodomelas, 480 nm eyeball extract

Abstract sentence 3, verbatim in two pieces: "Proteins were solubilized from the C. rhodomelas eyeball and subjected to spectroscopic analysis, which revealed the presence of a pigment" "characterized by an absorption maximum (λmax) at 480 nm." MATCH, 29 words, whole sentence. Methods confirmed verbatim: "C. rhodomelas was collected from active hydrothermal vent field on the Hatoma Knoll" "(24°51’N; 123°50’E; depth 1480–1530 m) of the Okinawa Trough, Japan."; ROV "Hyper-Dolphin equipped with Deep Aquarium system"; "One eyeball was kept in RNAlater (Ambion) at -80°C for RNA extraction, and the other was frozen in the dark"; "All extraction and spectroscopic analysis experiments were performed under dim red light (>640 nm, ~120 μW/cm2)."; "A frozen C. rhodomelas eyeball was incubated in the dark at 4°C for 10 min"; "1% (v/v) CHAPS]."; "The homogenate was centrifuged at 50,000 g for 20 min"; "this extraction procedure was repeated three times" "to obtain a total of four extracts."; "kept at 28°C"; "hydroxylamine (NH2OH) was added to the extract to a final concentration of 100 mM"; bleaching "with orange" (yellow in the same sentence, tool summary). Results: "the absolute absorption spectrum showed the presence of component(s) with absorption around 410 nm and 480 nm"; "Difference absorption spectra showed a peak at 414 nm for the decayed compound(s) (tentatively termed P414"; "On the other hand, the absorption appearing around 480 nm may be accounted for by rhodopsin."; recombinant "showed the difference absorption peak at 480 nm" fitted "with the template spectrum calculated for A1-based Rh480". No fish count, date or statistics (tool summary). Method (extract spectrophotometry, not MSP), depth, habitat and the P414 component are all recorded rightly; grade m right (one named species measured).

**Error (order).** Scorpaeniformes should be Perciformes under the desk's naming (see Names). Uncounted: the extraction describes "A frozen C. rhodomelas eyeball" with the other eye kept for RNA, which implies one fish; the record could say so, and could name the cruise (NT08-15, R/V Natsushima; tool summary) since no date is printed. Fixable.

## Trait key and grading

All six lines lambda_max_nm: fits (MSP means for lines 1 to 5; extract absorption maximum for line 6, with the method stated). Grading m right for all six. Trait key faults 0; grading faults 0.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Anguilla marmorata, rod 493 nm glass | error, fixable | conditions, note | Quote MATCH (33 words); rod data right; shared text says cone values are abstract-only (Results cite Table 1) and misreads the single-cone sentence |
| 2 | A. marmorata, rod 489 nm cultured yellow | error, fixable | conditions, note | As line 1 |
| 3 | A. marmorata, rod 489 nm wild yellow | error, fixable | conditions, note | As line 1; not a duplicate of line 2 (different fish) |
| 4 | A. marmorata, cone 508 nm cultured yellow | error, fixable | conditions, note | As line 1, plus the significant cultured-yellow cone t-test omitted |
| 5 | A. marmorata, cone 517 nm wild yellow | error, fixable | conditions, note | As line 4 |
| 6 | Careproctus rhodomelas, 480 nm extract | error, fixable | order, note | Quote MATCH (29 words); order Perciformes (WoRMS/OBIS, FishBase, main's Sebastidae), not the caption's Scorpaeniformes |

Count: 6 of 6 records in error (100%): scientific-context 5 (lines 1 to 5, one shared fault, with the omitted cone test on lines 4 and 5); names 1 (line 6); quote form 0; duplicates 0; bibliographic 0; licence 0; trait key 0; grading 0. None held out. Lines 1 to 3 carry only the shared cone text; their rod content is correct.

Pooled with audits 172 to 320: 393 of 801 evidence records (49.1%), taking audit 319's 384 of 792, adding audit 320's 3 of 3 (387 of 795) and 6 of 6 here. Audit 322's lines 9 to 12 are not included.

## Unchecked

- Lines 1 to 5: Table 1 and Table 2 cells did not render, so the cone values, cone SDs and cell counts, the table's mapping of 508 to cultured and 517 to wild yellow, and the per-comparison p values are unread. The place of the "cultured yellow eel and other stages" t-test sentence in the cone paragraph rests on tool order. Whether "a single cone cell" means one class or one cell is unresolved.
- Line 6: printed citation line beyond the title; the exact count of fish (implied one); the A. marmorata species page on Catalog of Fishes (acceptance read through a synonym's page).
- Lines 7 and 8 (drop, repeat d228) and 9 to 12 (audit 322) not audited.

## Replacement text

Lines 1, 2, 3, 4 and 5 (same strings in each):
- `conditions`: "the Results say only a single cone class was observed and only in cultured and wild yellow eels, and give no cone values or cone sample size in the text, so the 508 and 517 nm cone figures appear only in the abstract; the text does not say whether cones were found in glass eels;" -> "the Results print 'Only a single cone cell was observed in cultured and wild yellow eels.' (whether this means one cone class or one cell is not stated; the Discussion says the eel 'possesses only one type of cone cell', sensing about 500 to 535 nm) and 'The mean λmax values of single cone cells are all in the range of green light spectra (Table 1).'; the cone means, SDs and cell counts are in Table 1, not read, so 508 and 517 nm are logged from the abstract; the text does not say whether cones were sought and absent in glass eels; the Results also state that the λmax values of cultured yellow eels differ significantly from the other stages by Student's t-test (Table 2, no p values in the text);"
- `note`: "The cone figures are abstract-only (see conditions)." -> "The cone figures are logged from the abstract; the Results refer the cone means to Table 1, which was not read (see conditions)."

Line 6:
- `order`: "Scorpaeniformes" -> "Perciformes".
- `note`: "Family and order are from the Fig 1A caption ('Order Scorpaeniformes, Liparidae, snailfish')." -> "Family Liparidae as in the Fig 1A caption and Eschmeyer's Catalog of Fishes ('Valid as Careproctus rhodomelas Gilbert & Burke 1912. Liparidae.'); order Perciformes as FishBase ('Perciformes/Cottoidei') and OBIS (WoRMS backbone) place Careproctus and as main files Sebastidae; the caption prints the older 'Order Scorpaeniformes' (audit 321)."
- `conditions` (uncounted): "number of fish and collection date not stated;" -> "number of fish and collection date not stated, the spectroscopy describing one frozen eyeball, the other eye kept for RNA, which implies a single fish;".

Verdict: 6 of 6 audited records in error (100%), above the 5% bar. All six fixable with the replacement text above; none held out. Pooled 393 of 801 (49.1%) before audit 322.
