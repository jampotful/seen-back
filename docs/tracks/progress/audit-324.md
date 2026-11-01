# audit-324: desk-d231, evidence line 1

Audited 31 October 2026 from the desk-d231 files present untracked in the worktree (docs/tracks/progress/desk-d231.md and docs/views/evidence/desk-d231.jsonl, 1 line; neither committed here, neither edited). HEAD and origin/main f891dae8 (desk-d230). `python3 -I tools/senses/check.py | grep d231`: "docs/views/evidence/desk-d231.jsonl: 1 records, 0 problems". Quote length (`len(q.split())`): 14 words, within 40. Evidence records only; audits 322 and 323 are the format model, and the desk-audit.md evidence clause applies (40-word limit, no 125-character limit).

Sources opened (WebFetch): www.mdpi.com/2075-4450/16/12/1233 (three passes); api.crossref.org/v1/works/10.3390/insects16121233; for the name, thbif.onep.go.th/taxons/detail/26523 and two plazi.org links that returned only redirect notices. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 1 WebSearch and 6 WebFetch calls used.

## Bibliographic and licence

Li, Cao, Cai, Chen 2025. Page byline Lun Li; Jiyu Cao; Zhiping Cai; Jing Chen (tool summary of the byline), the recorded order and Crossref's (Lun Li, Jiyu Cao, Zhiping Cai, Jing Chen). Title verbatim on page and Crossref: "Plant Volatile Organic Compounds Attractive to Monolepta signata (Olivier)". Page citation "Insects 2025, 16(12), 1233"; Crossref container Insects, volume 16, issue 12, page 1233, issued 2025-12-06, type journal-article, relation empty, no update-to. DOI 10.3390/insects16121233 verified. Licence: page metadata links CC BY 3.0 (tool summary; no licence sentence returned); Crossref CC BY 4.0, content-version vor, start 2025-12-06, delay 0. Accepted under the CC BY 3.0 page vs CC BY 4.0 Crossref pairing. source.access "open" right. Bibliographic faults 0; licence faults 0.

## Names

Paper prints "Monolepta signata (Olivier)" (title) and the order and family Coleoptera: Chrysomelidae as the desk records. Thai BIF: "Monolepta signata (Olivier, 1808)", Chrysomelidae, Coleoptera (status not stated). Plazi carries treatments titled "Monolepta signata (Olivier, 1808)" (search result titles; pages returned only redirects), and the search lists Zootaxa 2530 and a 2012 revision of Oriental Monolepta (Galerucinae) under which the name is used. No synonymy or transfer found. Met, with the accepted status not read from a checklist page (Unchecked).

## Duplicates

git grep on origin/main (f891dae8) across the whole docs/ tree (evidence, audit, audit/corrected, audit/ALL, sheets, searched, gaps, wanted, codex-findings, progress) for "Monolepta", "signata", "insects16121233", "16121233", "Lun Li", "Shihezi" and "Chrysomelidae.*sense_chemical". No Monolepta hit anywhere; "signata" hits only Sidymella rubrosignata, Scinax v-signatus, Hemiaspis signata, Stictia signata; "Lun Li" only an unrelated wanted row; Shihezi only an Apocynum search query; Chrysomelidae sense_chemical rows on main are Chrysomela populi (desk-d221:10 and 11). DOI absent. Not a repeat.

## Per-record finding

### Line 1, Monolepta signata, sense_chemical, EAG response of both sexes to all mixtures

Section "3.1. Electroantennogram Responses of M. signata to Plant Volatile Mixture", verbatim and returned whole: "Both male and female antennae responded to all tested mixtures, with varying response amplitudes." MATCH, 14 words, one unbroken sentence; the tool confirmed it as a single sentence under that heading. Value says no more (the "plant-volatile" qualifier is the section heading's subject). Sentence before: "Notably, mixtures 4, 20, 22, 23, and 26 elicited consistently strong responses in both sexes" "and were, therefore, considered key candidates for further analysis". Female strongest 20, then 23 and 12; male 26, then 19 and 4 (tool summary).

Methods confirmed verbatim: "The test sequence was as follows: liquid paraffin, n-hexane, test volatile mixture, n-hexane and liquid paraffin."; "Each mixture was tested in numerical order, and the responses were recorded from six different antennae per treatment."; "To minimize variation, only active and undamaged adult M. signata were selected for testing."; "Before each test, the sex of the adult M. signata was identified and the individuals were starved for at least 4 h."; "All tests were conducted between 25 ± 1 °C from 10:00 to 20:00."; "Each volatile mixture was tested using six biological replicates, with one antenna per beetle."; formula "A = (B − C)/(D − C) × 100%," with control values averaged before and after each stimulus (tool summary). Section 2.3: "The nine VOCs used in this study were selected from the 14 volatiles previously identified in cotton leaves" "(Gossypium hirsutum) and corn leaves (Zea mays) by headspace collection and GC–MS analysis (unpublished data)." Abstract: "... 26 binary" "and ternary mixtures of 13 plant-derived volatile compounds extracted from cotton and corn leaves." So the note's 13 against 14 caveat is right (and the Methods say nine were used). Rearing 25 ± 1 °C, 50-70% RH, 16:8 h L:D (tool summary). Statistics: one-way ANOVA with LSD; captions cite Duncan's test (tool summary), as the record says.

Sex comparison, verbatim: "There were no significant differences in the EAG responses between males and females for most mixtures (p > 0.05)," "except for mixtures 1 (F = 2.547, df = 10, p = 0.014), 2 (F = 2.477, df = 10, p = 0.019), 3 (F = 0.017, df = 10, p = 0.021)," "5 (F = 5.711, df = 10, p = 0.023), 8 (F = 3.346, df = 10, p = 0.012), 10 (F = 0.162, df = 10, p = 0.003)," "11 (F = 0.208, df = 10, p = 0.015), 14 (F = 0.130, df = 10, p = 0.029), 15 (F = 1.193, df = 10, p = 0.035)," "19 (F = 0.001, df = 10, p = 0.003), 23 (F = 0.081, df = 10, p = 0.006), and 25 (F = 0.595, df = 10, p = 0.090)," "which showed significant sex-based differences". Discussion: "However, as field-collected adults of unknown age and mating status were used in this study," "these factors may have contributed to individual variations in antennal or behavioral responses".

**Error (stimulus-order confound, significant sex differences and sample-composition caveat omitted).** (a) Mixtures were "tested in numerical order", not randomised; the record gives no order, which is a control-order design confound the rules list. (b) The record says male and female responses "did not differ significantly for most mixtures" and names only mixture 25's p = 0.090. The paper lists 12 exceptions, 11 of them at p = 0.003 to 0.035 (mixtures 1, 2, 3, 5, 8, 10, 11, 14, 15, 19, 23), so 11 of 26 mixtures differed by sex, including key candidate 23. Under the omitted-significant-results rule this has to be in the record. (c) The authors' own caveat that adults were field-collected "of unknown age and mating status", which they say may have caused individual variation, is omitted; so are the 4 h starvation and the 25 C, 10:00 to 20:00 test window (minor; included in the replacement). Uncounted: the sex comparison is described as independent-samples t-tests but reports F values with df = 10 (presumably Levene's F alongside the t-test p; the t statistics are not printed); df = 10 fits six antennae per sex. The note's "summarising page tool ... confirmed unbroken" is borne out. Fixable.

## Trait key and grading

sense_chemical fits (antennal olfactory response to plant volatiles). Grade `m` right: one named species measured. No `partial`.

## Rule question: a sentence returned as two contiguous pieces

Question from desk-d231 owner question 1: when the page tool returns one sentence as two contiguous pieces with no gap, is a quote assembled from them acceptable?

How audits 318 to 323 handled it. Every one of them accepted such quotes and counted them MATCH, writing "verbatim in two pieces" (318 lines 6, 7 and 9, and three pieces for line 8; 320 lines 6 and 7; 321 the shared eel quote, "one whole sentence (split only by the tool's length cap)", and the Chaceon line; 322 the sculpin quote, "one whole sentence, no comma between the pieces"; 323 lines 2, 3 and 4, and its own replacement quote for Amalosia, 34 words, was built from two pieces). 319 accepted a 129-character title returned in two halves. 320 distinguished a sentence the tool returned whole from "reassembly from separate sentences", which it did not allow. None held a record out for being returned in pieces. The desk's hold of Dociostaurus maroccanus on that ground is stricter than audit practice.

The written rules. The quote rule (rules.md) asks for a whole sentence, never starting mid-sentence, with every cut marked; it says nothing about how the text reached the reader. BRIEF.md line 51 and oa-read.md say not to "evade a tool's restrictions by soliciting pieces" and not to use "pieces requested to bypass that cap"; both treat the cap as a retrieval constraint and point to a legal full-text source or a recorded retrieval gap.

Recommendation: accept, under conditions, and have the owner write it down. The prohibition targets circumvention (asking the tool for word-range fragments to rebuild text it declined to give), and the risk it guards is a silent gap or reordering at the join. A sentence the tool returns in sequence, from an ordinary request for the passage verbatim, in two pieces that abut with nothing missing, is the publisher's own open text cut by an output length limit; the sentence is whole and the rule's object (the printed sentence) is met. Conditions: (1) the pieces come in one response, in order, and the join shows no ellipsis, no "[...]" and no dropped punctuation; (2) the first piece does not end a sentence and the second does not begin one, unless the printed sentence is checked; (3) a second pass, or the auditor's independent pass, returns the same join; (4) the record's note says "verbatim in two pieces"; (5) the joined sentence passes the 40-word count and the rest of the quote rule; (6) dash, degree and minus characters are checked against the page because the tool may normalise them (audit 323's warning). Not acceptable: pieces from separate requests stitched together, pieces requested by word or character range after the tool refused the passage, or any join the auditor cannot reproduce. Honest caveat: the line between "asking for the passage verbatim" and "soliciting pieces" is thin, and this audit's own prompts asked for quotes "in pieces of up to 125 characters", as the earlier audits evidently did; if the owner reads BRIEF line 51 to bar that phrasing, every two-piece MATCH in audits 318 to 323 rests on the same footing and would need the same ruling, so the ruling should be made once and applied both ways.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Monolepta signata, sense_chemical, both sexes respond to all 26 mixtures | error, fixable | conditions | Quote MATCH (14 words, whole, unbroken); mixtures tested in numerical order (not randomised) omitted; 11 of 26 mixtures with significant sex differences (p = 0.003 to 0.035) reduced to "most did not differ"; authors' unknown age and mating status caveat omitted |

Count: 1 of 1 record in error (100%): scientific-context 1; duplicates 0; quote form 0; bibliographic 0; names 0; licence 0; trait key 0; grading 0. HOLD OUT: none.

Pooled with audits 172 to 323: 402 of 810 evidence records (49.6%), taking audit 323's 401 of 809 and adding 1 of 1 here.

## Unchecked

- Byline read from the tool's summary, not as printed characters (Crossref order agrees).
- Licence: the page's CC BY 3.0 is from page metadata via tool summary; no licence sentence returned.
- Name: accepted status not read from a checklist page (Catalogue of Life, GBIF or BioLib not opened; plazi pages redirected).
- Whether each mixture's response was tested against the liquid paraffin control (the record's "responded" rests on the authors' sentence; no per-mixture test against control was returned).
- Rearing RH and photoperiod, the formula's averaging of control readings, and the female and male rank orders are tool summary.
- Y-tube and field results not read (not logged by the record).

## Replacement text

Line 1:
- `conditions`: "Adults collected from cotton fields in Shihezi City, Xinjiang, China, and reared on fresh cotton leaves;" -> "Adults collected from cotton fields in Shihezi City, Xinjiang, China, and reared on fresh cotton leaves; field-collected adults of unknown age and mating status, which the authors say may have contributed to individual variation in antennal responses; only active, undamaged adults used, starved at least 4 h before testing; tests at 25 +/- 1 C between 10:00 and 20:00;"
- `conditions`: "six biological replicates per mixture, one antenna per beetle, no antenna reused;" -> "six biological replicates per mixture, one antenna per beetle, no antenna reused; mixtures were tested in numerical order (not randomised), each in the sequence liquid paraffin, n-hexane, mixture, n-hexane, liquid paraffin; relative response A = (B - C)/(D - C) x 100%;"
- `conditions`: "male and female responses did not differ significantly for most mixtures" -> "male and female responses did not differ significantly for most mixtures (p > 0.05), but differed significantly for mixtures 1, 2, 3, 5, 8, 10, 11, 14, 15, 19 and 23 (p = 0.003 to 0.035, df = 10; 11 of 26 mixtures, including key candidate 23), and the text also lists mixture 25 (p = 0.090) among the significant differences"
- `note` (uncounted): "Whole sentence read through a summarising page tool and confirmed unbroken under Results 3.1." -> "Whole sentence read through a summarising page tool and confirmed unbroken under Results 3.1 (audit 324). The sex comparison is described as independent-samples t-tests but prints F values with df = 10."

Verdict: 1 of 1 audited record in error (100%), above the 5% bar; fixable with the replacement text above; none held out. Rule question: recommend accepting a sentence the tool returns as two abutting pieces in one ordered response, under the six conditions above, as audits 318 to 323 did throughout; the owner should write the ruling into BRIEF so the desk and the audits apply one standard.
