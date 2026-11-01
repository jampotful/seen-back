# audit-322: desk-d229, evidence lines 9 to 12

Audited 31 October 2026 from the desk-d229 files present untracked in the worktree (docs/tracks/progress/desk-d229.md and docs/views/evidence/desk-d229.jsonl, 12 lines; neither committed here, neither edited). HEAD and origin/main 412c2eb8 (desk-d228). Lines 1 to 8 are judged elsewhere or dropped by the desk (7 and 8 repeat d228) and were not read for this audit. `python3 -I tools/senses/check.py | grep d229`: "docs/views/evidence/desk-d229.jsonl: 12 records, 0 problems". Quote lengths (`len(q.split())`): lines 9 to 11 share one quote of 24 words; line 12 is 12 words; all within 40. Evidence records only; audits 318 to 320 are the format model.

Sources opened (WebFetch): journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0116173 (four passes); journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0087211 (two passes); api.crossref.org/v1/works for 10.1371/journal.pone.0116173 and 10.1371/journal.pone.0087211; irma.nps.gov/NPSpecies/Species/Profile/147929 (lake trout name); en.wikipedia.org/wiki/Deepwater_sculpin (sculpin spelling and family). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 2 WebSearches and 10 WebFetch calls used.

## Bibliographic and licence

- Lines 9 to 11, Harrington, Hrabik, Mensinger 2015. Page byline "Kelly A. Harrington", "Thomas R. Hrabik", "Allen F. Mensinger", the recorded order and Crossref's. Title verbatim on Crossref and in the page citation: "Visual Sensitivity of Deepwater Fishes in Lake Superior". Page citation "PLoS ONE 10(2): e0116173."; Crossref PLOS ONE 10(2) e0116173, issued 2015-02-03. Page licence: "This is an open access article distributed under the terms of the Creative Commons Attribution License,"; Crossref CC BY 4.0 vor from 2015-02-03, delay 0, relation empty, no update-to. Met.
- Line 12, Lakes-Harlan, deVries, Stölting, Stumpner 2014. Page byline "Reinhard Lakes-Harlan, Thomas deVries, Heiko Stölting, Andreas Stumpner", the recorded order and Crossref's. Title on Crossref: "Useless Hearing in Male Emblemasoma auditrix (Diptera, Sarcophagidae) – A Case of Intralocus Sexual Conflict during Evolution of a Complex Sense Organ?", as recorded. PLoS ONE 9(1) e87211, issued 2014-01-28. Page prints the Creative Commons Attribution License sentence; Crossref CC BY 4.0 vor from 2014-01-28, relation empty, no update-to. Met.

Bibliographic faults 0; licence faults 0. source.access "open" right on all four.

## Names

- Coregonus kiyi: printed "(Coregonus kiyi)" in Abstract sentence 2. Salmonidae, Salmoniformes as on main's salmonid rows (e.g. canon-3.jsonl:705). Met.
- Salvelinus namaycush (siscowet). Printed "siscowet (Salvelinus namaycush siscowet)" in Abstract sentence 2. Ruling on the no-subspecies rule: the trinomial is not a recognised subspecies. NPSpecies (irma.nps.gov profile 147929) gives Salvelinus namaycush (Walbaum in Artedi, 1792) at species rank, lists "Salvelinus namaycush siscowet" under synonyms, and states "Originally reported as subspecies Salvelinus namaycush siscowet by Hubbs and Lagler (1949)." and "Subspecies designations are not recognized by Robbins et al. (1991)." The siscowet is a lake trout morphotype (lean/siscowet/humper ecotypes of one species; USGS and Wisconsin search-result titles on "sympatric morphotypes of lake trout", snippets only). All fish measured were of the one morph, so the record is neither pooled nor a breed or subspecies row. ACCEPTED at species rank, provided the morph stays named (eye field and note, as filed) so the value is not read as tested on lean lake trout. The note should say the trinomial is a synonym, not a recognised subspecies (replacement below, uncounted). Owner question 2 in desk-d229.md is answered by this ruling.
- Myoxocephalus thompsonii: the paper prints "Myoxocephalus thompsoni" (Abstract, Methods; tool summary that the Introduction prints "Moxocephalus thompsonii"). GBIF species/2333811 (search result title) and Wikipedia both give Myoxocephalus thompsonii (Girard, 1851). The record's spelling is right. Family and order: GBIF backbone (the project's taxonomy, docs/CONTRACTS.md:44) Cottidae, Scorpaeniformes, as filed; Wikipedia's taxobox gives Psychrolutidae, Perciformes (a newer classification). Met under the backbone rule; the alternative is noted (uncounted).
- Emblemasoma auditrix: Sarcophagidae and Diptera as printed in the title. Met.

Name faults 0.

## Duplicates

git grep on origin/main (412c2eb8) across the whole docs tree (evidence, audit, audit/corrected, sheets, searched, gaps, compile, codex-findings, progress) for "Coregonus kiyi", "kiyi", "Salvelinus namaycush", "namaycush", "siscowet", "lake trout", "Myoxocephalus", "thompsoni", "deepwater sculpin", "0116173", "Harrington", "Emblemasoma", "auditrix", "0087211", "Lakes-Harlan", "Okanagana". Hits: Harrington only for an unrelated fern paper (audit-194, desk-d104/d107); Emblemasoma, auditrix and Lakes-Harlan only in desk-d173.md:9, a held lead for a different paper (Tron et al. 2016, J Insect Sci). Salvelinus on main only as S. fontinalis cff_hz (oa-3, oa-6). None of lines 9 to 12 repeats main. Duplicate faults 0.

## Per-record findings

### Lines 9 to 11, Coregonus kiyi, Salvelinus namaycush (siscowet), Myoxocephalus thompsonii, ERG peak 525 nm

Abstract sentence 4, verbatim in two pieces: "Spectral sensitivity curves revealed peak sensitivity at 525 nm for each species" "which closely corresponds to the prevalent downwelling light spectrum at depth." MATCH, 24 words, one whole sentence, no comma between the pieces, value says no more. Results confirm: "All three fishes exhibited maximum sensitivity at 525 nm with relatively broad sensitivity from 500 to 550 nm"; "Deepwater sculpin displayed broader sensitivity between 475 to 550 nm than the other two species,". Each species has its own curve (Fig 3, "Error bars = 1 SE."), so the three values are separately measured, though all three equal 525 nm and are sampled at 25 nm steps. "ERG peak" is a spectral sensitivity peak (b-wave criterion response), and the record labels it as such in units, eye, method and note: not a pigment lambda_max. Trait key: main files electrophysiological peaks under lambda_max_nm (canon-3 "E (table key)" rows), so the key fits with the label.

Methods confirmed verbatim: "Fish were collected at depths ranging from 100 to 117 m during 10 minute bottom trawls"; "on November 13, 2012 and June 26, 2013"; "collected via daytime bottom trawls in the Apostle Islands region of Lake Superior, east of Stockton Island."; "all kiyi were tested within 4 days of capture"; "Siscowet were tested within 3 weeks of capture and sculpin within 2 months of capture."; "All fishes were dark adapted for 30 minutes prior to testing."; "Buffered 0.002% MS-222, maintained at 4°C"; "immobilized by an intramuscular injection of pancuronium bromide"; "A 0.20 mm diameter silver-silver chloride recording electrode was inserted into the vitreous of the eye"; "100 W quartz tungsten-halogen lamp"; "Wavelengths from 400 to 700 nm at 25 nm intervals were used as the stimulus with the presentation order randomly determined."; "the b-wave amplitude of 5 μV was set as the criterion response at 400 nm"; "Neutral density filters (0.1 to 3.0)". No n, size or sex printed anywhere (tool summary: no "n =", "N =" or "individuals"), as the record says. No statistical test, as the record says. Depth discrepancy: the Abstract gives 45 m for the sculpin under full moon; the Results sentence ("under full moon conditions to depths of approximately 30 m," "while deepwater sculpin could detect downwelling irradiance to 63 m") gives 63 m; the record's note of the conflict is right.

**Error (scotopic, rod-mediated limit omitted; dark holding omitted), each of lines 9, 10 and 11.** The authors limit what the peak measures: "the information presented is limited to scotopic visual sensitivity" "most likely mediated by the rod photoreceptors." The record states 30 min dark adaptation but not that only scotopic (rod) sensitivity was measured and that no light-adapted or cone-mediated response was tested. For a lambda_max_nm row this bounds the value: 525 nm is the dark-adapted, probably rod, peak, not the species' photopic or cone peak. Also omitted: fish were held for days to two months in "refrigerated dark rooms" "illuminated indirectly by dim red light" at "between 3 and 6°C", which bears on the adaptation state beyond the 30 min. Uncounted additions: the sculpin "needed a minimum of 190 seconds" "between flashes to avoid transient “bleaching”."; the Discussion says fish "were trawled from 100 to 115 m during both day and night" (tool summary of context), against the Methods' "daytime bottom trawls"; the 25 nm step limits the peak's resolution. Fixable.

### Line 12, Emblemasoma auditrix, hearing threshold tuned to 5 kHz in both sexes

Abstract, verbatim: "In both sexes the physiological hearing threshold is tuned to 5 kHz." MATCH, 12 words, one whole sentence, the value says no more. Hearing is measured: "The hearing threshold was determined by suction electrode recordings from axons of auditory interneurons" ("in the neck connective."); stimuli "pure sine waves between 3 and 50 kHz and a duration of 50 ms with pauses of 250 ms". Results: "The male hearing organ is physiologically functional." "The hearing threshold has a minimum at about 5 kHz and is relatively insensitive in the ultrasonic range."; "the threshold curves of males and females are rather similar in respect to tuning and general sensitivity." Origin confirmed: "infected host cicadas (Okanagana rimosa)", "near Grayling or Pellston, Michigan, USA", "kept for up to six months at 4°C", males for behaviour "collected by sweeping the vegetation". Behaviour: "Altogether 17 flies were tested, up to three times in an experiment."; "Despite the more sensitive hearing at 5 kHz, the phonotactic score to 5 kHz models is significantly lower" "than to 9 kHz models (p = 0.0113, t = 3.27, df = 11, paired t-test)." No threshold value in dB SPL at 5 kHz is printed (tool summary), and no test between the sexes' curves. sense_hearing fits; grade m right.

**Error (female threshold not measured in this study).** Fig 2 caption: "Hearing thresholds (mean and s.e.m.) of female (green) and male (red) E. auditrix." "Hearing threshold for female adapted from [17]." Reference 17 is Lakes-Harlan R, Stölting H, Stumpner A (1999), "Convergent evolution of insect hearing organs from a preadaptive structure", Proc R Soc B 266: 1161-1167 (reference list, tool returned). The paper describes no new female recordings (tool summary). The record's method ("threshold curves compared between sexes") and conditions ("electrophysiology N = 3 females and N = 4 males") present both curves as this study's measurements; the female half of "both sexes" is a value carried from the 1999 paper. The new measurement here is the male threshold (N = 4). Uncounted: the phonotaxis 9 versus 5 kHz statistic (p = 0.0113, t = 3.27, df = 11, paired t-test) should replace "scored higher"; units "Hz" for a kHz value. Fixable.

## Trait key and grading

- Lines 9 to 11, lambda_max_nm: fits as an ERG spectral sensitivity peak, labelled as such (main precedent: canon-3 electrophysiology rows).
- Line 12, sense_hearing: fits (neural threshold curve to tones).

Trait key faults 0. Grading `m` right for all four.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 9 | Coregonus kiyi, ERG peak 525 nm | error, fixable | eye, conditions | Quote MATCH (24 words); authors' scotopic, rod-mediated limit and dark/red-light holding omitted |
| 10 | Salvelinus namaycush (siscowet), ERG peak 525 nm | error, fixable | eye, conditions, note | As line 9; siscowet ACCEPTED at species rank (trinomial is a synonym, not a recognised subspecies; one morph, not pooled) |
| 11 | Myoxocephalus thompsonii, ERG peak 525 nm | error, fixable | eye, conditions | As line 9; spelling thompsonii right (paper prints thompsoni); Cottidae/Scorpaeniformes per GBIF backbone |
| 12 | Emblemasoma auditrix, threshold tuned to 5 kHz both sexes | error, fixable | method, conditions | Quote MATCH (12 words); female curve adapted from Lakes-Harlan et al. 1999, not measured here |

Count: 4 of 4 records in error (100%): scientific-context 4 (three the same omission from one paper; one provenance); quote form 0; duplicates 0; bibliographic 0; names 0; licence 0; trait key 0; grading 0. HOLD OUT: none.

Pooled with audits 172 to 320: 391 of 799 evidence records (48.9%), taking audit 319's 384 of 792, adding audit 320's 3 of 3 (387 of 795) and 4 of 4 here. The other audit of desk-d229's lines 1 to 6 is not included.

## Unchecked

- Lines 9 to 11: Fig 3 curves (image, not rendered), so whether any species' curve is flat between 500 and 550 nm enough that 525 nm is a tie was not read; the "Moxocephalus thompsonii" Introduction spelling is a tool summary; morphotype status of the siscowet rests on NPSpecies plus search-result titles, not on Eschmeyer's Catalog or FishBase (not opened).
- Line 12: the female N = 3 is taken from the record and the tool's reading of the caption (whether N = 3 belongs to the 1999 data was not returned verbatim); the 1999 reference entry came as a tool rendering of the reference list.

## Replacement text

Lines 9, 10 and 11 (apply to each):
- `eye`: "whole-eye ERG" -> "whole-eye ERG, dark-adapted (scotopic, most likely rod-mediated per the authors)" (line 10: "whole-eye ERG, siscowet morph" -> "whole-eye ERG, siscowet morph, dark-adapted (scotopic, most likely rod-mediated per the authors)").
- `conditions`: "dark-adapted 30 min, anaesthetised" -> "held in refrigerated dark rooms lit indirectly by dim red light at 3-6 C, dark-adapted 30 min before testing; the authors state the data are limited to scotopic visual sensitivity most likely mediated by the rod photoreceptors, and no light-adapted (photopic or cone) response was tested; anaesthetised".
- `conditions`: "curves are group means with SE bars" -> "the deepwater sculpin needed at least 190 s between flashes to avoid transient bleaching; the peak is resolved only to the 25 nm stimulus step; curves are group means with SE bars".
- `conditions` (uncounted): "a separate depth-profile result not logged here" -> "a separate depth-profile result not logged here; the Discussion says fish were trawled during both day and night, against the Methods' daytime trawls".

Line 10 only:
- `note` (uncounted): "The fish measured were the siscowet form, printed 'Salvelinus namaycush siscowet'; logged at species level." -> "The fish measured were the siscowet morphotype, printed 'Salvelinus namaycush siscowet'; that trinomial is a synonym, not a recognised subspecies (NPSpecies: subspecies designations not recognized by Robbins et al. 1991), so the row is logged at species level with the morph named (audit 322 ruling); the value is not shown for lean lake trout."

Line 11 only:
- `note` (uncounted): "Family and order are from GBIF species/2333811, as the paper states neither." -> "Family and order are from GBIF species/2333811 (backbone), as the paper states neither; some recent classifications place the genus in Psychrolutidae, Perciformes."

Line 12:
- `method`: "threshold curves compared between sexes" -> "male threshold curve recorded in this study (N = 4) and compared with a female threshold curve adapted from earlier work (Lakes-Harlan, Stölting and Stumpner 1999, Proc R Soc B 266: 1161-1167, the paper's ref. 17)".
- `conditions`: "electrophysiology N = 3 females and N = 4 males (Fig 2 caption)" -> "electrophysiology N = 4 males in this study; the female curve (N = 3, Fig 2 caption) is adapted from the 1999 paper, not newly recorded, so the female half of 'both sexes' is carried from earlier data; no threshold in dB SPL at 5 kHz is printed".
- `conditions` (uncounted): "scored higher for a 9 kHz song model than a 5 kHz model even though 5 kHz is the best hearing frequency" -> "scored significantly higher for 9 kHz than 5 kHz song models (p = 0.0113, t = 3.27, df = 11, paired t-test) even though 5 kHz is the best hearing frequency".
- `units` (uncounted): "Hz" -> "kHz".
- `note` (uncounted): "Sample sizes are small (3 and 4 flies)." -> "Sample sizes are small (4 males recorded here; female curve of 3 flies from the 1999 paper)."

Verdict: 4 of 4 audited records in error (100%), above the 5% bar. All four fixable with the replacement text above; none held out. Siscowet ruling: acceptable at species rank. Pooled 391 of 799 (48.9%).
