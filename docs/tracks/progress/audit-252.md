# audit-252: desk-d167 (8 evidence records, no search records, no wanted lines)

Audited 30 October 2026 from the desk-d167 files present untracked in the worktree (progress note and 8 evidence lines; neither is committed here, neither was edited). `tools/senses/check.py` on the evidence file: 8 records, 0 problems. The unit wrote no searched or wanted file, so there is nothing for `screen_candidates.py --check` and no sample to draw; all 8 records were judged. Quote lengths (`len(q.split())`), lines 1 to 8: 26, 31, 31, 31, 30, 31, 30, 30, all within 40. Evidence judged under oa-audit.md, "Scientific context and counting (29 October 2026)", the oa-read.md and BRIEF quote rules and the licence rule, in the form of audits 249 to 251. 8 WebSearch and 16 WebFetch calls used.

Sources opened: api.crossref.org/works/10.1242/JEB.243420, /works/10.1242/BIO.058796, /works/10.1098/RSPB.2024.2511; for Egri the /works/ path failed twice with a client error (as in audit 249) and the record was read at api.crossref.org/v1/works/10.1038/S41598-025-14294-4; the Chaib record URL (ncbi.nlm.nih.gov/pmc/articles/PMC8473842/); cob.silverchair.com/jeb/article-pdf/doi/10.1242/jeb.243420/2123798/jeb243420.pdf and cob.silverchair.com/bio/article-pdf/doi/10.1242/bio.058796/2100562/bio058796.pdf (publisher PDFs returned by my WebSearches); rcastoragev2.blob.core.windows.net/.../rspb.2024.2511.pdf (Royal Society publisher PDF returned by my WebSearch; two passes); nature.com/articles/s41598-025-14294-4 (record URL; two passes); Eschmeyer's Catalog of Fishes researcharchive.calacademy.org fishcatget.asp?spid=32633; fishbase.org/summary/3231. Not reached: doi.org/10.1242/jeb.243420 (Caves record URL; permission not answered), pmc.ncbi.nlm.nih.gov/articles/PMC12092137/ (Roberts; permission not answered), PMC12340130 (Egri; redirect, not followed). None retried. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries, so each quote was checked by a MATCH/MISMATCH question; points marked "(tool summary)" were not returned verbatim.

## Duplicates

Searched origin/main (c6c502bb) docs/views (evidence, audit, audit/corrected, audit/ALL.jsonl and the rest) for Xiphophorus, swordtail, Melopsittacus undulatus, Ischnura elegans, Electrogena and the four DOI suffixes.
- **Xiphophorus hellerii: main holds this paper.** docs/views/audit/corrected/fish-shark.jsonl line 154 (audit/ALL.jsonl line 894, audit/fish-shark.jsonl id fish-shark:154): Xiphophorus hellerii, acuity_cpd, value 3, anatomical RGC density, Caves EM, de Busserolles F, Kelley LA 2021, 10.1242/jeb.243420, quote "anatomical acuity was estimated to be approximately 3 cycles per degree (cpd) in both sexes", grade g, verdict flagged_unchecked (first-pass flag: grade should be m). Its `method` and `note` already carry the behavioural 0.8 and 3.0 cpd and the 1-2 / 2-3 cpd figures as text. desk-d167 line 1 repeats that record (same species, paper, trait, value, method) and its note's "Not on main (grep by species and DOI)" is false. Lines 2 and 3 file the optomotor means as their own values, which main holds only as text inside line 154; not counted as repeats, but their "Not on main" notes are also false. The grep the desk describes would have found the DOI in audit/corrected and audit/ALL.
- Melopsittacus undulatus: acuity_cpd lines on main from Caves et al. 2024 (6.9, 14.3), canon-5, oa-9 (6.9) and oa-5 297 to 299 (retracted Potier citations of Lind and Kelber 2011). No line from 10.1242/bio.058796. No repeat.
- **Ischnura elegans: main holds lambda_max_nm values** 370, 440, 540, 600 (and receptor_classes 4) from van der Kooi et al. 2021 Annu Rev Entomol Table 1 (audit/corrected/insect.jsonl 125 to 129; audit/corrected/methods.jsonl 650 to 653; verdicts unverifiable or correct for grade), plus a polarization line (oa-5 960, retracted). Lines 5 to 7 come from another paper and another method (expressed opsins, not compiled photoreceptor maxima) and 531 to 548 nm does not contradict the compiled 540 nm, so no repeat or contradiction. Their note "Not on main for this species (main holds I. heterosticta only)" is false; uncounted, must be fixed.
- Electrogena lateralis: desk-d164 lines 5 to 8 (same paper): lambda_max 536, 366, 353 and male dorsal cff 148.7 Hz. Female cff not on main. No repeat.

## Citation and licence

- Caves et al. 2021: Crossref: Eleanor M. Caves, Fanny de Busserolles, Laura A. Kelley (as recorded); title verbatim (prints "Xiphophorus helleri"); J Exp Biol 224, issue 24, article jeb243420, print 2021-12-15, online 2021-12-17; licence http://creativecommons.org/licenses/by/4.0 (vor). Publisher PDF: "© 2021. Published by The Company of Biologists Ltd"; "This is an Open Access article distributed under the terms of the Creative Commons Attribution License". As recorded.
- Chaib et al. 2021: Crossref: Sandra Chaib, Juliane Gaviraghi Mussoi, Olle Lind, Almut Kelber (as recorded); Biology Open 10, issue 9, article bio058796, online 2021-09-03; licence http://creativecommons.org/licenses/by/4.0 (vor, from 2021-09-03). **Copy at the record URL (PMC8473842):** the page as returned shows no copyright, licence or Creative Commons statement (tool summary), as the desk says. The publisher's PDF at cob.silverchair.com (watermarked "Biology Open • Accepted manuscript") states "© 2021. Published by The Company of Biologists Ltd." and "This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0), which permits unrestricted use, distribution and reproduction in any medium provided that the original work is properly attributed." The work is CC BY 4.0, so `access` "open" stands; but the record points to a copy on which no licence was read. Uncounted; set `url` to https://doi.org/10.1242/bio.058796 and say in `note` where the licence was read.
- Roberts et al. 2025: Crossref: Natalie S. Roberts, Erik I. Svensson, Marjorie A. Liénard (as recorded); Proc R Soc B 292, issue 2047, article 20242511, online 2025-05-21; licence http://creativecommons.org/licenses/by/4.0/ (vor and tdm); preprint 10.1101/2023.07.31.551331. Publisher PDF: © 2025 The Authors, Creative Commons Attribution licence http://creativecommons.org/licenses/by/4.0/ (tool summary). As recorded.
- Egri et al. 2025: Crossref (v1 path): Ádám Egri, Mihály Jásdi, György Kriska; Scientific Reports 15, issue 1, article 29465, 2025-08-12; licence https://creativecommons.org/licenses/by/4.0 (vor, tdm). Nature page: "This article is licensed under a Creative Commons Attribution 4.0 International License". As recorded.

## Names

- Xiphophorus hellerii (lines 1 to 3). Eschmeyer's Catalog of Fishes (spid 32633, entry for X. brevis Regan 1907): "Current status: Synonym of Xiphophorus hellerii Heckel 1848", the entry citing Rosen and Bailey 1963 for the spelling "helleri". FishBase summary 3231 heads "Xiphophorus hellerii Heckel, 1848", Poeciliidae, Cyprinodontiformes. The paper prints "Xiphophorus helleri" with "Heckel 1848". The record's spelling is the accepted one; the note's FishBase statement is right and could add the Catalog of Fishes.
- Melopsittacus undulatus (line 4): as on main; Psittaculidae as main files it. As recorded.
- Ischnura elegans (lines 5 to 7): Plazi treatment "Ischnura elegans (Vander Linden, 1820)" returned by my WebSearch, as the note cites. As recorded.
- Electrogena lateralis (line 8): as on main (desk-d164, audited in 249). As recorded.

## Checks per paper

Caves et al. 2021 (lines 1 to 3).
- Quotes: line 1 MATCH, whole Abstract sentence (before it, the sentence on RGC topography; after it, the line 2/3 sentence). Lines 2 and 3 MATCH, the next whole Abstract sentence. Values contained.
- Methods confirmed (publisher PDF, tool summary): optomotor 28 fish tested (13 M, 15 F), two females excluded for responding to the control and one as an outlier, final 13 M and 12 F; drum 35 cm (inner tank 30 cm); square-wave black-and-white gratings, 1 rotation per minute, grey control; full-spectrum arc lamp (6500 K) diffused through PTFE; luminance not given as a number. Whole-mounts 3 M, 3 F; Table 1: 3.1, 3.0, 3.0 (M), 2.8, 2.9, 2.9 (F); means 3.0 ± 0.06 and 2.9 ± 0.06. Conditioned grating-against-grey task: 4 M and 4 F, criterion 73%; males passed at 1 cpd (3 of 4) and all failed at 2 cpd; females all passed at 2 and all failed at 3 cpd.
- Context, uncounted: the Discussion offers as one possibility that the sex difference arises from "behavioural or attentional differences between males and females during experimental assays" and says the optomotor assay "inherently may confound" detail resolution with motion response; some individuals' optomotor acuity exceeded the anatomical estimate (tool summary). Lines 2 and 3 already state that the male value lies below an anatomical limit equal in both sexes and is not explained by eye size, so a reader is not led to an optical cause; left uncounted, but the authors' own wording should be added (below). The paper locates peak RGC density inconsistently (centro-temporal in the Abstract, elsewhere centro-ventral and dorso-temporal; tool summary); the quote is the Abstract's and stands.
- Grade m right on all three (one named species measured).

Chaib et al. 2021 (line 4).
- Quote MATCH (Abstract, whole sentence; superscript formatting aside). Value 4.68 contained.
- Confirmed (tool summary): 7 birds (3 F, 4 M), 5 learned; black circular target about 0.23 cd/m2 on about 140 cd/m2 grey (over 99% contrast); 1.69 deg/s semi-random motion; Y-maze, monitor behind stimulus windows; 1-up/2-down staircase (about 70.7% correct); mean 0.107 ± 0.007 deg (4.68 ± 0.32 cpd), best bird 0.091, worst 0.124 deg; stationary-target threshold from the earlier study 0.098 ± 0.008 deg (5.1 cpd), moving versus stationary not significant (χ2 = 0.74, d.f. = 1, P = 0.39).
- Uncounted: the note compares with main's 14.3 cpd, but the authors themselves put budgerigar grating resolution at 7.7 to 10 cpd from earlier studies (tool summary); add it so the comparison is the paper's. URL and licence as above.
- Grade m right.

Roberts et al. 2025 (lines 5 to 7).
- Quotes: the sentence begins "The LWS opsin types display maximal sensitivity between 530 and 550 nm with the following λmax: LWA2 = 548 nm," and ends "LWE1 = 533 nm (figure 2C–H, electronic supplementary material, figure S1, dataset S1)." (both MATCH), with LWF1 = 531 nm second; one sentence of 43 words (49 counting "="). Each quote keeps the opening and the closing and marks cuts with " … ", which oa-read.md allows; values contained.
- Confirmed (tool summary): HEK293T, 11-cis-retinal, template fit with 1000 bootstrap iterations; Figure 2 n (aliquots with active rhodopsin): LWA2 2, LWF1 2, LWE1 6 (also SWb1 6, SWb2 4, LWF2 5, LWF3 6, LWF4 1); controls Apis mellifera SWS and SWb2 K335E; the paper reports no ERG or in vivo spectral measurement on I. elegans, and its models use I. heterosticta ERG plus I. elegans LWF1 and LWF2 λmax. The cDNA source is in the supplement, as the note says.
- Uncounted: the authors state that several LWS opsins may be co-expressed in one photoreceptor and that the retinal distribution of LWS opsins is unknown (tool summary); add to the note, since a single expressed-pigment peak need not be any photoreceptor's peak. The "Not on main" clause is false (Duplicates).
- Grade m right (expressed I. elegans opsins measured in this paper).

Egri et al. 2025 (line 8).
- Quote MATCH (Results; preceded by "The FFF measured in female eyes with UV and green stimulation did not differ significantly according to the Wilcoxon Rank Sum test (W = 22, p-value = 0.5887).").
- Confirmed: 6 female, 9 male ventral and 9 male dorsal preparations; intact animals waxed to plexiglas, tungsten electrode in the right eye, reference in the abdomen; dark adaptation at least 40 min; LEDs 520 nm (2.0e15) and 372 nm (1.2e15 photons cm-2 s-1); 5 to 150 Hz log-spaced; larvae from Domini creek, reared to emergence; the 40-70% light-adapted caveat.
- **Counted (scientific meaning, statistical claim the source does not make).** The note says female FFF is "significantly lower than the male dorsal region". The Abstract says "Temporal resolution of female eyes was similar to that of the ventral eye region of males." and "Flicker fusion frequency of the male dorsal eye region was significantly higher than that of the ventral region."; the paper's tests are female UV versus green and male dorsal versus ventral; no test of female against male dorsal FFF was found (tool summary, asked twice). Nor is a female versus male-ventral test reported; "similar" is the Abstract's word. The record turns an untested comparison into a significance finding; that misstates the strength of evidence for a sex difference, which is the paper's central question. Fix below.
- Grade m right.

## Per record

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Xiphophorus hellerii, anatomical acuity 3 cpd | drop (duplicate) | whole record; note | Quote MATCH and value right, but main holds the same paper, species, trait, value and method (audit/corrected/fish-shark.jsonl 154, grade g, flagged for m); "Not on main" false |
| 2 | Xiphophorus hellerii, optomotor males 0.8 cpd | ok | (note, uncounted) | Quote MATCH; n 13 M, 12 F, drum, lamp right; "Not on main" false; add authors' behavioural/attentional and optomotor-confound caveats |
| 3 | Xiphophorus hellerii, optomotor females 3.0 cpd | ok | (note, uncounted) | As line 2 |
| 4 | Melopsittacus undulatus, 4.68 cpd moving-target equivalent | ok | (url, note, uncounted) | Quote MATCH; method and n right; record URL copy shows no licence, work is CC BY 4.0 (Crossref, publisher PDF); authors' grating comparison is 7.7 to 10 cpd |
| 5 | Ischnura elegans, LWA2 548 nm | ok | (note, uncounted) | Quote MATCH with allowed cuts; n 2 right; in vitro context right; "main holds I. heterosticta only" false (main holds I. elegans 370/440/540/600 from van der Kooi 2021) |
| 6 | Ischnura elegans, LWF1 531 nm | ok | (note, uncounted) | As line 5; n 2 right |
| 7 | Ischnura elegans, LWE1 533 nm | ok | (note, uncounted) | As line 5; n 6 right |
| 8 | Electrogena lateralis, female FFF 104.5 Hz | correct | note | Quote MATCH, value, n and apparatus right; note asserts female FFF "significantly lower than the male dorsal region", a test the paper does not report |

Evidence errors: 2 of 8 (25.0%), lines 1 (duplicate of main) and 8 (scientific meaning, note). Quote-form faults 0. Licence faults 0 counted (line 4 URL copy unlicensed on the page read; work CC BY 4.0). Bibliographic faults 0. Names 0 (Xiphophorus hellerii is the accepted spelling on Catalog of Fishes and FishBase).

Pooled with audits 172 to 251: 161 of 400 evidence records (40.3%; audits 172 to 251 159 of 392 as audit 251 gives it, audit 252 2 of 8). No search records in this unit, so nothing to pool with audits 83 to 90.

Verdict: the unit does not pass as filed; drop line 1 and correct line 8 before merging; lines 2 to 7 can merge with the uncounted note fixes below.

## Replacement text

Line 1 (counted): drop. If the anatomical value is wanted with this record's fuller `conditions`, the change belongs in main's fish-shark:154 through the audit path (grade g to m, as its first-pass flag says, and the full Abstract sentence as quote), not a second line.

Line 8 (counted), `note`: replace "Female FFF is similar to the male ventral eye region (the paper's abstract: temporal resolution of female eyes was similar to that of the ventral region of males) and significantly lower than the male dorsal region." with "Female FFF is similar to the male ventral eye region (104.1 ± 23.2 Hz; Abstract: 'Temporal resolution of female eyes was similar to that of the ventral eye region of males.') and numerically below the male dorsal region (148.7 ± 32.7 Hz); the paper tests male dorsal against ventral (significantly higher) and female UV against green (W = 22, p = 0.5887, no difference), but reports no test of female against male eye regions."

Lines 2 and 3, `note` (uncounted): replace "Not on main (grep by species and DOI)." with "Main holds this paper's anatomical value (audit/corrected/fish-shark.jsonl 154, value 3, with the optomotor means as text only)." and append "The authors raise as one possibility that the sex difference reflects 'behavioural or attentional differences between males and females during experimental assays', and note that the optomotor assay 'inherently may confound' detail resolution with motion response. Conditioned-task n = 4 males, 4 females (criterion 73%)." Line 1's note, if line 1 were kept, would need the same main-reference correction.

Line 4 (uncounted): set `url` to "https://doi.org/10.1242/bio.058796"; in `note` replace "Licence: Crossref lists CC BY 4.0 (vor); the PMC copy read shows no licence line in the text returned." with "Licence: Crossref lists CC BY 4.0 (vor); the publisher's accepted-manuscript PDF states the Creative Commons Attribution License (CC BY 4.0); the PMC page returned no licence line." and after "main already holds 14.3 cpd (behavioural grating) for this species" add "; the authors cite budgerigar grating resolution of 7.7 to 10 cpd from earlier studies".

Lines 5 to 7 (uncounted), `note`: replace "Not on main for this species (main holds I. heterosticta only)." with "Main holds compiled I. elegans photoreceptor maxima 370, 440, 540 and 600 nm from van der Kooi et al. 2021 (audit/corrected/insect.jsonl 125 to 128), another source and method; no expressed-opsin values." and append "The authors note that several LWS opsins may be co-expressed in one photoreceptor and that their retinal distribution is unknown, so an expressed-pigment peak need not equal any receptor's in vivo peak."

## Faults noted, not counted

- Lines 1 to 7: false "not on main" statements (Xiphophorus, Ischnura elegans); the desk's grep missed docs/views/audit/corrected and audit/ALL.jsonl.
- Line 4: record URL is a copy with no licence statement read on it.
- Lines 2 and 3: authors' non-sensory explanation and optomotor confound not carried.
- Lines 5 to 7: co-expression caveat not carried.
- Unchecked: the Caves record URL (doi.org) and the PMC copies of Roberts and Egri were not reached; the publisher PDFs and Nature page were used instead.
