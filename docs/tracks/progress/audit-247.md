# audit-247: desk-d162 (8 evidence records, no search records, no wanted lines)

Audited 30 October 2026 from the desk-d162 files present untracked in the worktree (progress note and 8 evidence lines; neither is committed here, neither was edited). `tools/senses/check.py` on the evidence file: 8 records, 0 problems. The unit wrote no searched or wanted file, so there is nothing for `screen_candidates.py --check` and no sample to draw; all 8 records were judged. Quote lengths (whitespace words as check.py counts, `len(q.split())`), lines 1 to 8: 40, 40, 39, 39, 32, 32, 34, 32, all within 40. Evidence judged under oa-audit.md, "Scientific context and counting (29 October 2026)", the oa-read.md quote rule and the licence rule, in the form of audits 241 to 246. 5 WebSearch and 15 WebFetch calls used.

Sources opened: api.crossref.org/works for all three DOIs (uppercase form); elifesciences.org/articles/77387.pdf (two passes), elifesciences.org/articles/77387/figures, elifesciences.org/articles/77387v1 (abstract and licence only); biorxiv.org preprint PDF 10.1101/2022.01.26.477913 (used only to confirm the df of the spontaneous comparison and the Methods shared with the published version); link.springer.com/article/10.1007/s00359-018-1287-8 (two passes, page text cut off in the reference list); pmc.ncbi.nlm.nih.gov/articles/PMC6208660 (Okanoya, licence and threshold criterion); frontiersinzoology.biomedcentral.com/counter/pdf/10.1186/1742-9994-6-22.pdf (two passes); Catalog of Fishes (researcharchive.calacademy.org, spid 3965 and 4184). Not reached: elifesciences.org/articles/77387 (JavaScript browser challenge) and pmc.ncbi.nlm.nih.gov/articles/PMC9246366 (reCAPTCHA page); neither was worked around or retried. Library-catalogue hits returned by searches (katalog.lib.cas.cz, ebusca.uv.mx, searchworks.jioinstitute.edu.in) were not opened. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. WebFetch returns model summaries, so each quote was checked by submitting it for a MATCH/MISMATCH answer; points marked "(tool summary)" were not returned verbatim.

## Duplicates

Searched origin/main (52f1bbf7) docs/views (evidence, audit, audit/corrected, audit/ALL.jsonl) for the four species, the three DOIs (by suffix), and the first authors Lunsford, Okanoya and Kostarakos.
- Astyanax: no record anywhere on main.
- Heterocephalus glaber: visual traits only (fovea, receptor_classes, acuity_cpd, eye_axial_length_mm; Kopania and Clark 2025, Hunt et al. 2009, Veilleux and Kirk 2014). No sense_hearing record.
- Meriones unguiculatus: visual and flicker traits only (fovea, lambda_max_nm, orbit_convergence_deg, acuity_cpd, eye_axial_length_mm, diel, cff_hz). No sense_hearing record.
- Teleogryllus oceanicus: one sense_hearing record exists, insect:424 (audit/insect.jsonl, audit/corrected/insect.jsonl, ALL.jsonl): Imaizumi and Pollack 1999, J Neurosci, auditory receptor fibre characteristic frequencies over a tested 2 to 40 kHz, value [2000, 40000]. Different paper and a different measure (receptor CF clusters against one interneuron's tuning); the AN1 best frequency of 4.4 to 5.1 kHz sits inside the lowest CF cluster that record names, so no contradiction. The progress note's statement that main holds "no ... Teleogryllus oceanicus hearing line" is wrong (uncounted).
- "Okanoya" matches only a raptor hearing-range record (Yamazaki et al. 2004) in audit/corrected/birds.jsonl; "1287-8" matches only 10.1099/00221287-82-2-209 (a fungus paper). None of the three DOIs is on main.
No repeat by species and paper under any trait.

## Citation and licence (Crossref reached)

- Lunsford et al. 2022: Crossref: Elias T Lunsford, Alexandra Paz, Alex C Keene, James C Liao (order and initials as recorded); title verbatim; eLife 11: e77387, published 2022-06-16; licence http://creativecommons.org/licenses/by/4.0/ (vor, am, tdm). The eLife figures page prints "This article is distributed under the terms of the Creative Commons Attribution License". `access` "open" stands.
- Okanoya et al. 2018: Crossref: Kazuo Okanoya, Shigeto Yosida, Catherine M. Barone, Daniel T. Applegate, Elizabeth F. Brittan-Powell, Robert J. Dooling, Thomas J. Park (order and initials as recorded); title verbatim; J Comp Physiol A 204(11): 905-914, online 2018-09-19, print November 2018; licence https://creativecommons.org/licenses/by/4.0 (vor, tdm). The Springer page text I received ended inside the reference list and named no licence; the PMC copy (PMC6208660) prints "This article is distributed under the terms of the Creative Commons Attribution 4.0 International License" with the CC BY 4.0 URL. `access` "open" stands.
- Kostarakos et al. 2009: Crossref: Konstantinos Kostarakos, Matthias R Hennig, Heiner Römer (order and initials as recorded; the record's "Romer H" drops the umlaut, harmless); title verbatim; Frontiers in Zoology 6(1): 22, 2009-09-28. Crossref lists no licence; the BMC PDF prints "This is an Open Access article distributed under the terms of the Creative Commons Attribution License". `access` "open" stands.

## Names

- Astyanax mexicanus: Catalog of Fishes spid 3965, "Valid as Astyanax mexicanus (De Filippi 1853)", Acestrorhamphidae (Acestrorhamphinae); family and order on lines 1 to 4 agree. The cave population in the paper is Pachón, as every record says. Not in docs/views/gaps/gbif-names.tsv; GBIF not opened.
- Heterocephalus glaber: ACCEPTED EXACT, usage key 5219654 in docs/views/gaps/gbif-names.tsv on main. MDD page not opened.
- Meriones unguiculatus: ACCEPTED EXACT, usage key 5219721 in gbif-names.tsv. MDD page not opened.
- Teleogryllus oceanicus: ACCEPTED EXACT, usage key 1723426 in gbif-names.tsv. Orthoptera Species File not opened.
No synonym problem.

## Checks per paper

Lunsford et al. 2022 (lines 1 to 4). Quotes: lines 1 and 2 MATCH; the marked cut inside the closing parenthesis drops "t = 15.97, df = 5,795;" and the sentence ends at "Figure 2C)." as quoted (eLife PDF). Lines 3 and 4 MATCH, whole sentence. 30 Hz values in the note confirmed ("n = 12; 119.6 ± 16.6 Hz" against "n = 10; 73.2 ± 6.9 Hz; p = 0.03, t = 2.38, df = 18"). Methods confirmed (tool summary): 4 to 7 dpf, 10% Hank's at 26 °C, recording temperature not stated, 0.1% α-bungarotoxin, probe about 50 µm anterior to the cupula, 5, 10, 20, 30 and 40 Hz, 1 s on and 4 s off, 60 sweeps, no numeric deflection amplitude. Posterior neuromast count p = 0.77 (U = 111.5); hair cells per neuromast p = 0.09 (n = 11 blind, n = 9 surface). Fig. 2C legend: "surface (blue; 12.4 Hz, n = 10 fish)", "Pachón (red; 18.6 Hz, n = 5 fish)", and that the rates "suggests that lateral line response thresholds in cavefish are lower"; the abstract says the elevated activity "identified a lower response threshold". The records' note (authors infer a lower threshold, none measured) is a fair reading.
- Sampling unit for evoked responses (uncounted, fix): the shared `conditions` say "Fish numbers: ... evoked responses n = 12 Pachon and n = 10 surface". Neither the Results nor the Fig. 2D/E legend says whether n = 12 and n = 10 are fish, neuromasts or afferent recordings, and an unpaired t-test on 12 and 10 fish would have df = 20, while the paper prints df = 18. The record states as fact a unit the paper does not give. Left uncounted because it changes neither the direction nor the size of the morph difference, nor its applicability; it should not stand as written.
- Cause of the difference: the Discussion says "The increased afferent activity in cavefish is a likely consequence of eye loss" and frames efferent loss as possibly induced by eye degeneration (tool summary). The records attribute no cause, and the note's efferent remark is confined to the fictive-swimming result, which the paper supports. No fault.
- Fig. 2C legend calls 12.4 and 18.6 Hz medians; the Results text gives them as mean ± SE. The records follow the text (harmless).

Okanoya et al. 2018 (lines 5 to 7). Quotes: lines 5 and 6 MATCH, whole sentence beginning "For example,"; line 7 MATCH, whole sentence. Confirmed: subcutaneous ketamine 35 to 50 mg/kg and xylazine 8 mg/kg; four mole-rats (breeding female, breeding male, two non-breeding adult females; 6.3, 3.4, 1 and 6 years) and two gerbils (2 to 8 months, sex not stated); body temperature "30 ± 0.5 °C (NMR) and 37 ± 0.5 °C (gerbils)"; meter 30 cm from the speaker, "fast A-weighted scale"; 5 ms tones at 0.25, 0.5, 1, 2, 4, 8 and 10 kHz; 5 dB steps over a 40 dB range with examples 70 to 110 and 30 to 70 dB; no single maximum level; "the ABR derived curves are elevated by about 15–25 dB for both naked mole-rats and gerbils"; mole-rat response amplitude "only about 25% that of the gerbil". No numerical threshold at 8 or 10 kHz in the text, and no numerical best frequency. The 0.25 kHz values (75 dB against 40 dB) and the 25 to 50 dB average offset are correct, and every record carries anaesthesia, the two body temperatures, n = 4 and n = 2, the tone range, the A-weighting and the ABR-to-behaviour offset. No counted fault.
- Threshold criterion (uncounted, fix): the paper defines threshold as "the lowest intensity at which a response could be detected visually on the trace, regardless of wave, or 2.5 dB below the lowest intensity that elicited a measurable response" (PMC6208660). The shared `conditions` keep only the first half. Harmless at the scale of a 35 dB species difference.
- Text values (uncounted, fix): the shared notes say "(all frequencies appear only in Fig. 3)" and line 7 says "the individual-frequency values are only in Fig. 3, not in the text". The text gives the 0.25 kHz averages the records quote and estimated 2 kHz thresholds ("22.5 dB" gerbil, "52.5 dB" naked mole-rat, the Fig. 2 examples, tool summary).
- Line 7 compiler note (uncounted, fix): "'best at low frequencies' is the authors' description in the abstract and Results". The ABR wording is in the Discussion ("The ABR-derived measure of auditory sensitivity confirmed that the naked mole-rats have best hearing for low frequencies"); the abstract says only "we confirmed hearing sensitivity using the auditory brainstem response", and its low-frequency wording refers to the behavioural audiogram.

Kostarakos et al. 2009 (line 8). Quote MATCH, whole sentence. Confirmed: tungsten hook electrodes on the connectives between prothoracic and suboesophageal ganglia; chlorethylene; 21 to 23 °C in a Faraday cage; 11 T. oceanicus (3 males, 8 females), own culture, one week after the final moult; 23 ms pulses, 16 ms pauses, four pulses per chirp; tuning at 3.5 to 6 kHz ("The tuning of AN1 was determined with ipsilateral stimulation at frequencies ranging from 3.5 to 6 kHz", with T. commodus at 3.0 to 6.0 kHz); 1 dB steps; at least one spike per syllable in at least three of five stimulations; no maximum level stated. Table 1: mean-curve best frequency 5.0 kHz, mean threshold 39.9 dB SPL, individual best frequency 4.8 ± 0.26 kHz (range 4.4 to 5.1), male calling-song carrier 4.8 ± 0.21 kHz. The text also gives "The average AN1-tuning for all 11 individuals is best at 4.85 kHz", which the note omits while citing the table's 5.0 kHz (uncounted; the value field uses only the range sentence, which is right). Value, units and the one-neuron limitation are right.

## Per record

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Astyanax mexicanus, Pachón spontaneous 18.6 Hz | ok | (conditions, uncounted) | Quote MATCH with marked cut; values, larval age, paralysis, unstated recording temperature and amplitude carried; "fish" for evoked n unsupported |
| 2 | Astyanax mexicanus, surface spontaneous 12.4 Hz | ok | (conditions, uncounted) | As line 1 |
| 3 | Astyanax mexicanus, Pachón evoked 101.3 Hz at 40 Hz | ok | (conditions, uncounted) | Quote MATCH; 30 Hz values in note confirmed; evoked n unit unsupported |
| 4 | Astyanax mexicanus, surface evoked 52.3 Hz at 40 Hz | ok | (conditions, uncounted) | As line 3 |
| 5 | Heterocephalus glaber, ABR about 75 dB at 0.25 kHz | ok | (conditions, note, uncounted) | Quote MATCH; ketamine/xylazine, 30 C, n = 4, 0.25 to 10 kHz, ABR offset carried; threshold criterion half-stated; "only in Fig. 3" overstated |
| 6 | Meriones unguiculatus, ABR about 40 dB at 0.25 kHz | ok | (conditions, note, uncounted) | As line 5; n = 2 and 37 C carried |
| 7 | Heterocephalus glaber, 25 to 50 dB above gerbil | ok | (conditions, note, uncounted) | Quote MATCH; relative value labelled as such; note misplaces "best at low frequencies" and says no frequency values are in the text |
| 8 | Teleogryllus oceanicus, AN1 tuning 4.5 to 5.1 kHz (9/11), 4.4 kHz (2) | ok | (authors, note, uncounted) | Quote MATCH; 3.5 to 6 kHz, n = 11, 21 to 23 C, one-neuron limitation carried; umlaut lost; text's 4.85 kHz average not mentioned |

Evidence errors: 0 of 8 (0.0%). Scientific-meaning faults counted 0; quote-form faults 0. Licence faults: none (all three CC BY on the copy read; `access` "open" stands on every line). Name faults: none. Duplicates: none. Units: Hz spike rates (spikes/s), dB as printed (A-weighted meter, reference not labelled SPL for tones) and kHz used correctly throughout.

## Replacement text (exact, all uncounted, recommended before merge)

Lines 1 to 4, `conditions`: replace "Fish numbers: spontaneous activity n = 5 Pachon and n = 10 surface (figure legend); evoked responses n = 12 Pachon and n = 10 surface (df = 18 at 40 Hz)." with "Fish numbers: spontaneous activity n = 5 Pachon and n = 10 surface fish (Fig. 2C legend); evoked responses n = 12 Pachon and n = 10 surface, unit not stated (fish, neuromasts or recordings), and the t-tests at 30 and 40 Hz report df = 18, which does not fit 22 independent fish."

Lines 5 to 7, `conditions`: replace "Threshold was the lowest level with a visible response on the trace." with "Threshold was the lowest level at which a response could be detected visually on the trace, regardless of wave, or 2.5 dB below the lowest level that elicited a measurable response."

Lines 5 to 7, `note`: replace "The text gives no numerical best frequency and does not report values at 8 and 10 kHz (all frequencies appear only in Fig. 3)." with "The text gives no numerical best frequency and does not report values at 8 and 10 kHz; besides the 0.25 kHz averages it gives example 2 kHz thresholds (gerbil 22.5 dB, naked mole-rat 52.5 dB), and the full curves are in Fig. 3."

Line 7, `note`: replace "the individual-frequency values are only in Fig. 3, not in the text. ABR waveform" with "the curves at each frequency are in Fig. 3. ABR waveform", and replace "Compiler note: 'best at low frequencies' is the authors' description in the abstract and Results, without a numerical best frequency." with "Compiler note: 'best hearing for low frequencies' is the authors' description of the ABR result in the Discussion, without a numerical best frequency; the abstract's low-frequency wording refers to the behavioural audiogram."

Line 8, `source.authors`: replace "Kostarakos K, Hennig MR, Romer H" with "Kostarakos K, Hennig MR, Römer H".

Line 8, `note` (optional): replace "Table 1 gives a mean-curve best frequency of 5.0 kHz" with "Table 1 gives a mean-curve best frequency of 5.0 kHz (the Results text gives 4.85 kHz for the average tuning of all 11 animals; individual best frequencies 4.8 +/- 0.26 kHz, range 4.4 to 5.1)".

## Faults noted, not counted

- Lines 1 to 4: evoked n stated as fish numbers without support; df = 18 does not fit 12 + 10 fish.
- Lines 5 to 7: threshold criterion half-stated; notes say no per-frequency values are in the text, but 0.25 and 2 kHz values are.
- Line 7: "best at low frequencies" placed in the abstract and Results; it is in the Discussion.
- Line 8: umlaut lost in Römer; text's 4.85 kHz average not mentioned.
- Progress note: main does hold a Teleogryllus oceanicus sense_hearing record (insect:424, Imaizumi and Pollack 1999), which this unit neither repeats nor contradicts.

Search records: none in the unit (0 of 0). Wanted lines: none. Held-out leads in the progress note were not searched.

Pooled with audits 172 to 246: 148 of 360 evidence records (41.1%; audits 172 to 246 148 of 352 as audit 246 gives it, audit 247 0 of 8).

Verdict: all 8 lines can be merged as they stand; the uncounted fixes above are recommended, the lines 1 to 4 `conditions` fix most of all, since it replaces an unsupported statement about sampling units. Error line numbers: none.

No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page opened; no paper text committed beyond single sentences and short phrases quoted for verification. The desk-d162 copies stay untracked and unedited. This report is model output and carries no authority.
