# audit-336: desk-d241, evidence lines 6 to 9

Audited 31 October 2026 from the desk-d241 files present untracked in the worktree (docs/tracks/progress/desk-d241.md and docs/views/evidence/desk-d241.jsonl, 9 lines; neither committed here, neither edited). Lines 1 to 5 are audit 335's. HEAD and origin/main 1d7f41c5 (desk-d240). `python3 -I tools/senses/check.py | grep 'd241\.'`: "docs/views/evidence/desk-d241.jsonl: 9 records, 0 problems". Quote length (`len(q.split())`) 34 words in all four lines, within 40; four U+2212 minus signs and the "•" in "cd/m2•s" present in each quote. Evidence records only; audits 333 and 334 are the format model, and the desk-audit.md evidence clause applies (40-word limit, no 125-character limit). Quotes returned in abutting pieces are judged under the six conditions in audit-324.md; cuts under audit-331.md.

Sources opened (WebFetch): api.crossref.org/v1/works/10.1038/srep11531 (one pass after one rate-limit refusal); www.nature.com/articles/srep11531 (five passes); mammaldiversity.org/taxon/1004654, /1004826, /1004379 and www.mammaldiversity.org/taxon/1004542 (one pass each, all returned by WebSearch). GBIF, WoRMS and OBIS not opened (GBIF and WoRMS refused per rules; OBIS holds marine records and was not needed for four terrestrial bats). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 3 WebSearches and 10 WebFetch calls used.

## Bibliographic and licence

Lines 6 to 9 share one source. Crossref: He-Qun Liu, Jing-Kuan Wei, Bo Li, Ming-Shan Wang, Rui-Qi Wu, Joshua D. Rizak, Li Zhong, Lu Wang, Fu-Qiang Xu, Yong-Yi Shen, Xin-Tian Hu, Ya-Ping Zhang (twelve, in the record's order); title "Divergence of dim-light vision among bats (order: Chiroptera) as estimated by molecular and electrophysiological methods", identical to the record; Scientific Reports volume 5, Crossref issue 1, article-number 11531; issued and published online 2015-06-23; journal-article; relation empty, no update-to (update policy only). The page prints "Sci. Rep. 5, 11531; doi: 10.1038/srep11531 (2015)." and an abbreviated byline ("Liu, H.-Q. et al."; tool summary), so no issue is printed and "Scientific Reports 5: 11531" with year 2015 is right; author order rests on Crossref. Licence: the page tool returned no Creative Commons sentence; Crossref CC BY 4.0, content-version vor (and tdm), start 2015-06-23. Accepted under rules.md (publisher page with no licence sentence plus Crossref CC vor licence). source.access "open" right. Bibliographic faults 0; licence faults 0.

## Names

MDD taxon pages: Rhinolophus affinis Horsfield, 1823, Rhinolophidae, Chiroptera, "previously included R. andamanensis" (Andaman split; the paper's bats are not Andaman animals); Taphozous melanopogon Temminck, 1841, Emballonuridae, no splits; Cynopterus sphinx (Vahl, 1797), Pteropodidae, no split recognised; Rousettus leschenaultii (A. G. Desmarest, 1821), Pteropodidae, seminudus and shortridgei now synonyms only, "leschenaultia" flagged as an incorrect spelling. None of the four is in main's gbif-names.tsv (grep of the four genera: only Rhinolophus rouxi, Rousettus aegyptiacus, R. madagascariensis and Taphozous georgianus). The paper uses the same four binomials. Names, families and orders met. The note's sentence "family for the species named in the paper agrees with the paper's own text (Pteropodidae, Emballonuridae) or MDD (Rhinolophidae)" is garbled boilerplate repeated in all four lines; wording fix uncounted.

## Origin, design and rulings asked

- Wild-caught, verified: "sample bats of all of the studied species were captured in the wild"; "Animals were allowed to acclimate to the facility for 5-6 days prior to the experiment."; ethics approval SWYX-20111010001. Capture locality and date not stated (tool summary). Not domestic, not lab-bred. Acceptable.
- n per species, verified: "Two animals of C. sphinx (male, 26 g and 30 g in weight)" "and R. leschenaultii (male, 75 g and 88 g in weight)"; "Four animals each of T. melanopogon (22.5 g ± 2.60 g) and R. affinis (13.3 g ± 1.88 g)", sex not given for these two. The record's counts and sexes are right.
- Method, verified: active electrodes "over the bilateral visual cortex (V1)"; dark adaptation in "absolute darkness (less than 0.25 lx luminescence) for 20 minutes" under restraint; "two trains of 180 flash stimuli at a 100 ms duration"; "ISI of 1 to 3 s (0.3–1 Hz, random)"; "180 epochs were averaged"; display "suitably linearized by gamma correction." No photometer is named for the flashes; the only meter (AvaSpec-ULS2048LTEC) measured room background (tool summary). The record's "calculated versus measured not stated" is right.
- Threshold criterion (printed, record says "not read"): "The absolute visual threshold was defined as the lowest flash intensity that produced an N-P-N structure distinguishable from baseline;" "i.e., when the light intensity was lower than the absolute visual threshold, the bat could not see."
- Stimulus series (not in the record): "All bats were stimulated at 12 levels (−0.95, −1.49, −1.90, −2.45, −2.85, −3.71, −4.77, −6.20, −6.30, −6.37," "−6.43 and −6.51 log cd/m2•s) of photic intensity." Each of the four thresholds is one of these tested levels, so each value is the lowest tested level that gave a response, and the true threshold lies between it and the next lower level: R. affinis between −1.90 and −2.45; T. melanopogon between −3.71 and −4.77 (a step of more than one log unit); C. sphinx between −6.30 and −6.37; R. leschenaultii between −6.37 and −6.43. The 0.07 log-unit difference between the two pteropodids is one step of the series, on two animals each. Whether the species value is per animal, a mean or the lowest across animals is not stated, and no per-animal variation or statistic is given (tool summary). The Results give the range as "approximately −0.49 to −6.51", against −0.95 as the first Methods level (paper's own inconsistency; uncounted).
- Recording mode confounded with family: C. sphinx and R. leschenaultii "were repeatedly measured in chronic recordings."; T. melanopogon and R. affinis "were used for acute measurement experiments because they did not survive long after surgery." Anaesthesia ("sodium pentobarbital (3.4 mg/0.1 kg, i.p.)") is stated for surgery only; its state during recording is not stated, and the authors give no caveat on comparing acute and chronic recordings (tool summary). The two higher (less sensitive) thresholds therefore come only from acutely recorded animals in post-surgical decline, and the two lowest only from chronically implanted animals. The record names acute and chronic but not why, and not that the family ranking rests on that split. Design confound, counted.
- One sentence, four species (desk owner question 2): each value is confined to its own clause, the last two by "respectively", and the quote is whole. Audit 334 allowed one sentence for two species on the same terms; nothing in the quote rule changes at four. Allowed; one record per species with the same quote is the right form. Not pooled-species records: each line carries one binomial and one value.
- Trait key and units (desk owner question 3): `absolute_sensitivity` is on main (91 rows in docs/views/audit/ALL.jsonl; evidence rows in canon-2, desk-d195, desk-d207, desk-d234, intake-7, oa-2, oa-10 and others) with free-text units that already include ERG thresholds in uW cm-2 sr-1 and "log units" (intake-7, Androctonus australis), lx (oa-10), cd/m2 (canon-2, oa-2) and photoisomerizations/rod/s (oa-2). An f-VEP threshold in log cd/m2•s fits the same key. The note's "units are log values not cd/m2 as in main's canon-2 rows" understates main's spread; wording fix uncounted.
- Grade `m` right (four named species, measured by the authors). eye "" right.

## Duplicates

git grep on origin/main (1d7f41c5) across the whole docs/ tree (evidence, audit incl. audit/corrected and audit/ALL, sheets, searched, sources, wanted, gaps, progress, tracks) for "srep11531", "11531", the title words "dim-light vision among bats", "He-Qun Liu", and the four binomials. A git grep of all 729 remote branches not merged into main (audit branches excluded) over docs/views/evidence, docs/views/audit and docs/views/sheets for "srep11531", "Taphozous melanopogon" and "Rhinolophus affinis".

- srep11531: no hit on main (the "11531" hits are unrelated: a wanted-merged count column and an MDPI PDF version string). Only branch hit: origin/research/desk-d241 itself.
- Rhinolophus affinis, Taphozous melanopogon: no hit on main.
- Cynopterus sphinx, Rousettus leschenaultii: audit/corrected/mammal-groups.jsonl:76 and audit/ALL.jsonl:2315, a pooled three-pteropodid acuity_cpd row (another trait, another source); gaps/try-species.json. No absolute_sensitivity row; nothing in sheets, searched, sources or wanted. Not repeats.

Duplicate faults 0.

## Quote ruling

The tool returned the sentence on the first page pass in two abutting pieces in one response: "The absolute visual threshold intensity for each species was −1.90 (log cd/m2•s) for R. affinis, −3.71 (log cd/m2•s)" " for T. melanopogon and −6.30 and −6.37 (log cd/m2•s) for C. sphinx and R. leschenaultii, respectively." The join falls mid-sentence, with no ellipsis or dropped punctuation; the minus signs and "•" match the record; a later pass returned the opening clause again in the same form, and the Discussion-style summary "As predicted, the lowest absolute visual thresholds were found in Pteropodidae (−6.30 and −6.37, log cd/m2•s)," "followed by Emballonuridae (−3.71) and then insectivorous bats (−1.90)." agrees with every value. Conditions 1 to 6 of audit-324 met; the record's note says "said in pieces". Whole sentence, 34 words, verbatim. Values −1.9, −3.71, −6.3 and −6.37 say no more than the quote. MATCH in all four lines.

## Per-record findings

### Line 6, Rhinolophus affinis, −1.90 log cd/m2•s

Bibliography, licence, name, origin, n (4, sex not given), quote MATCH. **Error (stimulus series and threshold resolution omitted; threshold criterion omitted; acute-recording confound omitted).** The value is the lowest of 12 tested levels that evoked a distinguishable N-P-N response; the next lower level was −2.45, so the threshold lies between −1.90 and −2.45; the record gives neither the series nor the criterion, and gives "acute recordings" without the printed reason ("did not survive long after surgery") or that recording mode splits exactly along the families compared. Fixable.

### Line 7, Taphozous melanopogon, −3.71 log cd/m2•s

As line 6; n 4, sex not given. **Error (same three omissions).** The next lower tested level was −4.77, so this threshold is resolved only to within more than one log unit. Fixable.

### Line 8, Cynopterus sphinx, −6.30 log cd/m2•s

As line 6; n 2 males, chronic recordings. **Error (stimulus series and resolution omitted; criterion omitted; recording-mode confound omitted).** Next lower level −6.37; the difference from R. leschenaultii is one step of the series on two animals each, so the two pteropodid values are not shown to differ. Fixable.

### Line 9, Rousettus leschenaultii, −6.37 log cd/m2•s

As line 8; n 2 males, chronic. **Error (same three omissions).** Next lower level −6.43. Fixable.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 6 | Rhinolophus affinis, −1.90 | error | method, conditions | 12-level series and step resolution, N-P-N criterion, acute post-surgical recording confound omitted |
| 7 | Taphozous melanopogon, −3.71 | error | method, conditions | as line 6; next level −4.77 |
| 8 | Cynopterus sphinx, −6.30 | error | method, conditions | series and resolution, criterion, chronic-vs-acute confound omitted; pteropodid difference is one step |
| 9 | Rousettus leschenaultii, −6.37 | error | method, conditions | as line 8; next level −6.43 |

Errors 4 of 4 records (100%), above the 5% bar; all fixable with the text below; none held out. Bibliographic, licence, name, origin and duplicate checks pass; the quote is whole and verbatim; one sentence serving four species records is ruled acceptable, and these are not pooled-species records; the trait key fits main. Unchecked: the figures (VEP waveforms per intensity, which might show per-animal thresholds); the latency statistic "Mean ± SD, n = 12 (n = 5 in R. affinis)", which gives n = 5 for R. affinis against four animals (tool summary; not reconciled, likely trials); the molecular (rhodopsin) half of the paper; Supplementary Information; capture locality (not printed).

## Replacement text

Each old string occurs exactly once in its field in the line(s) named (checked with `str.count`).

All four lines (6, 7, 8, 9), counted:
- `method`: "100 ms flashes at 12 intensity levels on a gamma-linearised LCD display" -> "two trains of 180 flashes of 100 ms, ISI 1 to 3 s random, 180 epochs averaged per f-VEP, at 12 intensity levels (−0.95, −1.49, −1.90, −2.45, −2.85, −3.71, −4.77, −6.20, −6.30, −6.37, −6.43 and −6.51 log cd/m2•s) on a gamma-linearised LCD display; threshold defined as the lowest flash intensity that produced an N-P-N structure distinguishable from baseline, so each value is a tested level and the true threshold lies between it and the next lower level"
- `conditions`: "and the threshold criterion was not read." -> "and no photometer is named for the flashes (the only meter named measured room background)."
- `conditions`: "n is 2 to 4 per species, no statistics are given for the thresholds, and no variation around the single value per species was read." -> "n is 2 to 4 per species; whether each species value is per animal, a mean or the lowest across animals is not stated, and no per-animal variation or statistic is given. Recording mode follows the family split: the two pteropodids were recorded chronically and the insectivorous R. affinis and the emballonurid T. melanopogon acutely, because they did not survive long after surgery; the state of anaesthesia during recording is not stated and the authors give no caveat on comparing acute and chronic recordings, so the family ranking is confounded with recording mode."

Lines 6 and 7 only, counted:
- `conditions`: "acute recordings, 4 animals (details from a summarising page tool)." -> "acute recordings, 4 animals (sex not given), used acutely because they did not survive long after surgery."

Line 6 only, append to the field (counted): after the replacement above, the same `conditions` string "used acutely because they did not survive long after surgery." -> "used acutely because they did not survive long after surgery. The next lower tested level was −2.45, so the threshold lies between −1.90 and −2.45 log cd/m2•s."

Line 7 only (counted): "used acutely because they did not survive long after surgery." -> "used acutely because they did not survive long after surgery. The next lower tested level was −4.77, so the threshold is resolved only to between −3.71 and −4.77 log cd/m2•s, a step of more than one log unit."

Lines 8 and 9 only, counted:
- `conditions`: "chronic recordings, 2 male animals (details from a summarising page tool)." -> "chronic recordings, 2 male animals (C. sphinx 26 and 30 g; R. leschenaultii 75 and 88 g), measured repeatedly."

Line 8 only (counted), applied after the replacement above: "measured repeatedly." -> "measured repeatedly. The next lower tested level was −6.37, so the threshold lies between −6.30 and −6.37 log cd/m2•s, and the difference from R. leschenaultii (−6.37) is one step of the stimulus series on two animals each."

Line 9 only (counted), applied after the replacement above: "measured repeatedly." -> "measured repeatedly. The next lower tested level was −6.43, so the threshold lies between −6.37 and −6.43 log cd/m2•s, and the difference from C. sphinx (−6.30) is one step of the stimulus series on two animals each."

All four lines, `note` (uncounted):
- "Trait key absolute_sensitivity as on main; units are log values not cd/m2 as in main's canon-2 rows." -> "Trait key absolute_sensitivity as on main, whose rows already use free-text units including cd/m2, lx, log units and ERG thresholds in uW cm-2 sr-1; audit 336 ruled an f-VEP threshold in log cd/m2•s fits the key."
- "family for the species named in the paper agrees with the paper's own text (Pteropodidae, Emballonuridae) or MDD (Rhinolophidae)." -> "family and order as on the MDD taxon page; the paper's text names Pteropodidae and Emballonuridae and calls R. affinis an insectivorous bat."
