# audit-265: desk-d181 (9 evidence records) and desk-d180 line 5 (1 record)

Audited 30 October 2026 from the desk files present untracked in the worktree (docs/views/evidence/desk-d180.jsonl, desk-d181.jsonl and docs/tracks/progress/desk-d180.md, desk-d181.md; none committed here, none edited). Scope set by the caller: all nine desk-d181 lines and desk-d180 line 5 only. desk-d180 lines 1 to 4 (Nilaparvata lugens, PeerJ 12351) repeat desk-d178, which is on main, and are being dropped; they were not audited. `tools/senses/check.py`: desk-d180 5 records, 0 problems; desk-d181 9 records, 0 problems. Quote lengths (`len(q.split())`): d181 lines 1 to 9: 27, 24, 30, 25, 17, 33, 12, 18, 29; d180 line 5: 28. All within 40. No searched or wanted files, so there is nothing for `screen_candidates.py --check` and no sample to draw. All ten records were judged under oa-audit.md "Scientific context and counting (29 October 2026)", the BRIEF and oa-read.md quote rules, the licence rule (the publisher's own free full text is accepted; a repository copy needs an open licence statement on that copy) and the name rule, in the form of audits 262 to 264. 4 WebSearch and 21 WebFetch calls used (counting refused and redirected fetches).

Sources opened: api.crossref.org/works/ 10.7554/ELIFE.77628, 10.7717/PEERJ.18491, 10.1038/S41598-022-11998-9, 10.1038/S41598-022-19236-Y, 10.3389/FNBEH.2021.698516; elifesciences.org/articles/77628 (four passes); peerj.com/articles/18491/ (two passes); www.nature.com/articles/s41598-022-11998-9 (two passes); frontiersin.org fnbeh.2021.698516/pdf (two passes; returned by my WebSearch); dspace.library.uvic.ca item 4c45870f (UVic record of the halibut paper, metadata only); orthoptera.speciesfile.org/otus/843600; fishbase.se/summary/4768; researcharchive.calacademy.org Catalog of Fishes spid=23117; en.wikipedia.org/wiki/Hippoglossus.

Blocked and not retried: www.nature.com/articles/s41598-022-19236-y (the halibut Author Correction; permission not answered); pmc.ncbi.nlm.nih.gov/articles/PMC9448732 (the same correction on PMC, after a redirect; permission not answered); obis.org/taxon/127138 (permission not answered); frontiersin.org fnbeh.2021.698516/full (permission not answered; the PDF was read instead); gbif.org/species/5213980 (client error). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened; library-catalogue hits (libmast.utm.my, ebusca.uv.mx, openaccess.library.uitm.edu.my, pesquisa.bvsalud.org) were left alone. WebFetch returns model summaries, so quotes were checked by MATCH/MISMATCH and segment questions; points marked "(tool summary)" were not returned verbatim.

## Bibliographic (Crossref, fresh)

- Pulver: Christian A Pulver, Emine Celiker, Charlie Woodrow, Inga Geipel, Carl D Soulsbury, Darron A Cullen, Stephen M Rogers, Daniel Veitch, Fernando Montealegre-Z (order as recorded); eLife 11, e77628, no issue; issued 2022-09-28; CC BY 4.0 for vor, am and tdm; has-preprint 10.1101/2021.09.01.458595; no update-to. As recorded. Uncounted: `journal` could read "eLife 11: e77628".
- Ramos: Andreia Ramos, David Gonçalves, Raquel O. Vasconcelos; PeerJ 13, e18491; issued 2025-01-13; CC BY 4.0 (content version unspecified); relation empty. As recorded.
- Bolstad: Kennedy Bolstad, Iñigo Novales Flamarique; Scientific Reports 12, issue 1, article 8062; issued 2022-05-16; CC BY 4.0 (vor and tdm). Crossref also records `updated-by` an Author Correction, 10.1038/s41598-022-19236-y, published 2022-09-06. The records do not mention it. The nature.com article page says "An Author Correction to this article was published on 06 September 2022" and "This article has been updated", so the text the desk and I read is the updated version. What the correction changed could not be read (both copies refused). Uncounted bibliographic omission; note text below; owner question 2.
- Lanaia: Veralice Lanaia, Konstantin Tziridis, Holger Schulze; Front Behav Neurosci 15, article 698516; issued 2021-07-30; CC BY 4.0 (vor); relation empty. As recorded.

Bibliographic faults counted: 0.

## Licence

- eLife page: "This article is distributed under the terms of the Creative Commons Attribution License" (verbatim fragment). Publisher's own text with CC BY. Met.
- PeerJ page: "This is an open access article distributed under the terms of the Creative Commons Attribution License" (verbatim fragment). Met.
- nature.com page: labelled open access, "2022 The Author(s)", no licence line in the text returned (tool summary). This is the publisher's own free full text, and Crossref's vor licence is CC BY 4.0. Met under audits 223, 257 and 264. The UVic DSpace copy shows no licence statement on its record, so it could not carry the record and was not used.
- Frontiers PDF: "This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY)" (verbatim fragments). Met.

Licence faults: 0.

## Names

- Copiphora gorgonensis: Orthoptera Species File, Montealegre-Z. & Postles, 2010, one valid name and no invalid names; Tettigoniidae, Conocephalinae, Copiphorini. As filed.
- Betta splendens: FishBase, Betta splendens Regan, 1910, Anabantiformes, Osphronemidae (Macropodusinae). FishBase presents it as the main entry but the page does not say "accepted" in words (tool summary). Genus not in doubt. As filed.
- Hippoglossus hippoglossus: the desk's weak spot. OBIS (WoRMS) was refused to me as well. Catalog of Fishes (California Academy of Sciences), spid 23117, gives Hippoglossus vulgaris Fleming 1828 as "Synonym of Hippoglossus hippoglossus (Linnaeus 1758)", family Pleuronectidae, subfamily Hippoglossinae. That entry treats H. hippoglossus as the valid name, and Catalog of Fishes is the standard authority for fish names. Family Pleuronectidae confirmed. Order: Wikipedia's taxobox gives Carangiformes (the Betancur-R. arrangement), while the records give Pleuronectiformes (FishBase and WoRMS usage). That is a classification choice, outside the genus test; uncounted. Note text below.
- Meriones unguiculatus: the note relies on docs/views/gaps/gbif-names.tsv. Main already files this species under several traits (mammals-met, desk-d162, desk-d170, oa-1, oa-13c). Genus not in doubt. As filed.

Name faults: 0.

## Duplicates

`git grep` on origin/main (f55ee1c5) under docs/views/evidence, docs/views/audit/corrected and docs/views/audit (including ALL.jsonl) for "Copiphora", "gorgonensis", "Betta", "Hippoglossus", "Meriones", "Pulver", "Bolstad", "Lanaia", "Ramos A", "77628", "18491", "11998", "698516", "Osphronemidae" and "Pleuronectidae":
- Copiphora gorgonensis: one record on main, desk-d146 line 6, sense_hearing, Jonsson et al. 2016 (J R Soc Interface, 10.1098/rsif.2016.0560), tympanal best response 23.63 kHz. That is a different paper and a different measurement. No duplicate.
- Meriones unguiculatus: desk-d162 has a sense_hearing ABR record from Okanoya et al. 2018 (10.1007/s00359-018-1287-8), a different paper; the rest are vision traits. No duplicate.
- "77628" hits sweep-46 line 10 inside an unrelated string (Serenoa repens record). False hit.
- "Ramos A" hits sea-invertebrates (another author). Osphronemidae and Pleuronectidae hit other species (desk-d160, desk-d159). No Betta or Hippoglossus record on main.

Duplicates: 0.

## desk-d181 lines 1 to 4: Pulver et al. 2022, Copiphora gorgonensis

Quotes: lines 1 and 2 MATCH in the Abstract; line 3 MATCH in Results (3D printed model measurements), the sentence before it being "Overall, the greatest pressure gains were detected at 101.47 ± 3.43 kHz ..."; line 4 MATCH in Results (Behavioural audiograms). Each is a whole sentence. Quote-form faults 0.

Context read on the eLife page (tool summary unless quoted):
- The 20 to 30 dB gains come from 3D printed ears (scaled 1:~11.5) and numerical simulations. No pressure gain in dB was measured on live ears. Live tympanal vibrometry was limited to 60 kHz: "Frequencies above 60 kHz were not tested due to the acoustic limitations of the experimental setup" (verbatim). Live broadband tests gave tympanal velocity per pressure, with resonances near 108 to 111 kHz. The authors also say the print and numerical models lack a vibrating tympanum.
- Directional hearing at 23 kHz: laser Doppler vibrometry on 13 live ears at 23, 40 and 60 kHz, with and without pinnae. "We found a significant interaction between the presence of pinnae with angle of incidence ... and with frequency (Table 1)" (verbatim, F = 4.47, p = 0.012); "Post-hoc analysis showed that pinnae significantly delayed the time of arrival at 23 kHz from 0.56 ± 0.05 µs to 0.55 ± 0.05 µs" (verbatim; the numbers fall while the word says delayed); "Pinnae maintained mean Δ φ° at 80.9° for 23 kHz ... with the pinnae ablated, phase differences were smaller" (62.7° at 23 kHz; verbatim fragments); the Discussion says the pinnal contribution to tympanal displacement "depended on the incident angle of the sound source at frequencies ≤60 kHz" (verbatim). Simulations gave higher pressure at 23 kHz without pinnae (t = 3.45, p < 0.001) and no angle effect.
- Behaviour: "Behavioural audiograms of startle behaviour were obtained from nine tethered females walking on a treadmill" and "Audiograms were obtained with stimuli in the range 20–120 kHz" (verbatim). Startle thresholds "decline sharply for stimuli between 20 kHz and 35 kHz ... and remains essentially constant at higher frequencies" (verbatim fragments). The Discussion: "The average startle behavioural threshold in C. gorgonensis was 59.28 ± 1.80 dB SPL (Figure 5B)" (verbatim). Table 3 means run about 55 to 62 dB SPL from 40 to 85 kHz (tool summary), so the dip at 90 to 120 kHz is shallow.
- Neural audiograms (five animals, whole auditory nerve): best frequency 23 kHz; no numerical thresholds.
- 3D prints: "(n = 8; 4 prints from males and 4 prints from females, 2 ears each, ± pinnae)" (verbatim); Table 1 lists four ears for this model (tool summary), an inconsistency in the paper.

Line 1 (error, scientific context, fixable). The `conditions` say the gain was "measured on models and live ears". The paper measured no pressure gain on live ears, and its live recordings stopped at 60 kHz, while the gain is claimed above 60 kHz. The `method` adds "behavioural and neural audiograms from live specimens", which reads as if live data gave the gain. This misstates how the finding was obtained and so its applicability to a living ear (modelled cavities without a tympanum, scaled prints). Counted under the scientific-context rule (the quote is right; the method and conditions are not).

Line 2 (error, contrary result omitted, fixable). The record labels the finding a null for direction ("null for direction", "negative result for directional hearing"). The authors do conclude that the pinnae "do not assist in directional hearing for conspecific call frequencies", and the quote is theirs. But the same paper reports that at 23 kHz the pinnae significantly changed arrival time, that pinna effects interacted with angle of incidence (F = 4.47, p = 0.012), that phase differences between the two tympana were larger with pinnae (80.9° against 62.7°), and, in the Discussion, that the pinnal contribution to tympanal displacement depended on angle at 60 kHz and below. A reader of the record would take it as no measurable directional effect. The paper shows angle-dependent effects that the authors judged too small or of the wrong kind to aid direction finding. That limits the null and is an explicit result, so it counts under "a null result or exception that limits a claimed effect".

Line 3 (confirm). Ablated-pinnae values 9.69 and 9.83 dB in the quote; prints n = 8 as stated in the text. Uncounted: the note's "pinnal contribution about 17 to 20 dB" is the record's own subtraction (26.33 − 9.69 = 16.6; 30.04 − 9.83 = 20.2); write it as computed. Uncounted: mention that Table 1 lists four ears for this model.

Line 4 (confirm). Value matches the quote; conditions give nine tethered females and the startle criterion; "stayed about constant at higher frequencies" conveys the shallow dip. Uncounted: the Discussion calls the same 59.28 dB SPL "the average startle behavioural threshold" without a frequency range, and the Table 3 means for 90 to 120 kHz average about 58 dB SPL (tool summary), so the basis of the figure is not stated; add to note.

## desk-d181 lines 5 to 7: Ramos, Gonçalves and Vasconcelos 2025, Betta splendens

Quotes: line 5 MATCH (Abstract), line 6 MATCH (Results, Auditory sensitivity), line 7 MATCH (Abstract). Whole sentences. Quote-form faults 0.

Context (PeerJ page): fish lab-reared, 10th generation from Chiang Rai stock, 5 males and 6 females, 8 months, MS-222 400 mg/L (as recorded); "For each frequency, tones were initially presented at 140 dB re 1 µPa and then following 2.5 dB consecutive decrements" (verbatim); threshold = "the minimum level required to elicit an identifiable and reproducible AEP response in at least two averaged waveforms" (verbatim); calibration by hydrophone (Brüel & Kjær 8104), no particle-motion measurement, the 100 Hz tone delivered by a shaker-driven disc (tool summary). Directly after the line 6 sentence: "Since auditory responses at 4,000 and 6,000 Hz were not consistently present in all recordings, they were excluded from statistical analysis." (verbatim). Then frequency effect F(6,54) = 56.694, p < 0.001; sex F(1,9) = 10.123, p = 0.011; males lower at 400 Hz (p = 0.015) and 600 Hz (p = 0.009).

Line 5 (confirm). 100 to 400 Hz in the quote; lab-bred origin against the title's "wild" correctly flagged. Uncounted: add that particle motion was not measured (pressure thresholds only).

Line 6 (error, consequential qualification omitted, fixable). The value states a 4,000 Hz threshold of 137.8 ± 3.6 dB as the highest threshold. The next sentence of the Results says responses at 4,000 and 6,000 Hz were not consistently present in all recordings and were excluded from the statistics, and the stimulus series began at 140 dB re 1 µPa, so the 4,000 Hz figure sits at the top of the levels presented and rests on the fish that responded at all. The `conditions` say only that 6,000 Hz "was tested, no threshold is given in this sentence". That loses an explicit limitation on the magnitude and meaning of the 4,000 Hz value. Uncounted: the note takes the dB reference "from the paper's soundscape units"; the Methods state the stimulus levels in dB re 1 µPa, which is the better support.

Line 7 (confirm). Value is the quote; statistics in the note match. Uncounted: the sex × frequency interaction is not reported, and n is 5 against 6; the note's "Small n" covers it.

## desk-d181 lines 8 and 9: Bolstad and Novales Flamarique 2022, Hippoglossus hippoglossus

Quotes: line 8 "The rod visual pigment had λmax ± SD at 491 ± 7 nm (n = 25) (Fig. 8F)." MATCH, whole sentence, Results > Visual pigments, with "(Fig. 8F)." present on both of my passes; the desk's dropped segment was a summariser artefact. Line 9: the sentence came back in five consecutive segments: "The cone visual pigments consisted of two short wavelength (S) types with maximum wavelength" / "of absorbance (λmax) ± SD at 431 ± 7 nm (n = 8) (Fig. 8A) and 457 ± 6 nm (n = 7) (Fig. 8B)," / "three middle wavelength (M) types with λmax ± SD at 500 ± 5 nm (n = 23) (Fig. 8C)," / "514 ± 8 (n = 35) (Fig. 8D), and 527 ± 6 (n = 19) (Fig. 8E)," / "and one long wavelength (L) type peaking at 550 ± 11 nm (n = 4) (Fig. 8G)." The record's quote is the opening and the end joined with " … ", which the rule allows; the subject, value, unit and n are kept. Quote-form faults 0.

Context: measurements from outer segments of individual photoreceptors in four juvenile fish; template fitting was used only to decompose the S(431) hump; L(550) n = 4 is the smallest cone sample; no A1/A2 statement in the text returned; adaptation state not given in the Results (a figure caption calls the retina light adapted; tool summary). The Methods did not come through on my passes either, so the records' "Methods not reached" stands.

Line 8 (confirm). Line 9 (confirm). Uncounted additions: the Author Correction (above) and the order note.

## desk-d180 line 5: Lanaia, Tziridis and Schulze 2021, Meriones unguiculatus

Quote MATCH, Results ("The Hearing Threshold in the Control Group"), whole sentence. Methods as recorded: pure tones 1 to 8 kHz, 30 to 90 dB SPL in 5 dB steps, RMS 0 to 10 ms, automatic thresholds; 37 ten-week-old males, 18 controls; ketamine and medetomidine with atropine. Control thresholds 38.45 ± 13.45 dB SPL before and 32.94 ± 12.72 dB SPL 2 h after saline (Tukey p < 0.001); salicylate 39.51 ± 13.53 against control 32.94 at 2 h, F(1,132) = 9.92, p = 0.002, transitory after a week; all as the note gives them. No frequency main effect or 4 kHz post hoc test is reported, so "best frequency 4 kHz" is the authors' description of the mean curve. The authors write that "the hearing of the gerbil up to 20 kHz closely resembles the human audiogram" with best hearing around 4 kHz (citing Ryan 1976; verbatim fragment), which agrees with the record's 4 kHz and with its note that the tested range stops at 8 kHz. Confirm. Uncounted: add the anaesthetic to `conditions` and say in the note that no statistical test of the frequency effect is reported.

## Verdicts

| file:line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| d181:1 | Copiphora gorgonensis, pinna gain 20 to 30 dB above 60 kHz | correct | method, conditions | Quote MATCH; gain is from scaled prints and simulations, no live-ear gain, live tests stop at 60 kHz; record says "measured on models and live ears" (scientific context) |
| d181:2 | Copiphora gorgonensis, no directional assist at call frequency | correct | value, conditions, note | Quote MATCH; labelled a clean null but the paper reports significant pinna × angle effects on arrival time, larger phase differences with pinnae and angle-dependent displacement at ≤60 kHz (contrary results omitted) |
| d181:3 | Copiphora gorgonensis, ablated gain 9.69 / 9.83 dB | confirm | (note; uncounted) | Quote MATCH; subtraction should be marked as computed |
| d181:4 | Copiphora gorgonensis, startle threshold 59.28 dB SPL | confirm | (note; uncounted) | Quote MATCH; basis of the figure not stated in the paper |
| d181:5 | Betta splendens, best range 100 to 400 Hz | confirm | (note; uncounted) | Quote MATCH; lab-bred flagged; particle motion unmeasured |
| d181:6 | Betta splendens, lowest 100 Hz, highest 4,000 Hz | correct | conditions, note | Quote MATCH; omits that 4,000 and 6,000 Hz responses were inconsistent and excluded, with stimuli starting at 140 dB (consequential qualification) |
| d181:7 | Betta splendens, males lower at 400 and 600 Hz | confirm | none | Quote MATCH; statistics right |
| d181:8 | Hippoglossus hippoglossus, rod 491 nm | confirm | (note; uncounted) | Quote MATCH with "(Fig. 8F)."; name valid in Catalog of Fishes; Author Correction unmentioned |
| d181:9 | Hippoglossus hippoglossus, L cone 550 nm | confirm | (note; uncounted) | Quote MATCH with permitted ellipsis; as line 8 |
| d180:5 | Meriones unguiculatus, ABR best 4 kHz in 1 to 8 kHz | confirm | (conditions, note; uncounted) | Quote MATCH; all note figures verified |

Evidence errors: 3 of 10 (30.0%): scientific-context faults 3 (d181 lines 1, 2, 6); quote-form 0; bibliographic 0; licence 0; name 0; duplicates 0. All three are fixable with the text below. Unfixable records: none.

Pooled with audits 172 to 264: 195 of 481 evidence records (40.5%; 192 of 471 through audit 264, that is audit 263's 192 of 464 plus audit 264's 0 of 7, plus 3 of 10 here). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Counted fixes (required before merging):

- d181 line 1 `method`: "pressure gain measured on 3D-printed ear models (scaled about 1:11.5 from micro-CT geometry; 8 prints, ± pinnae) and numerical simulations; live ears were tested by laser Doppler vibrometry only up to 60 kHz". `conditions`: "pressure gain is a property of the pinnal cavities in printed and numerical models, which lack a vibrating tympanum; no pressure gain was measured on live ears, and live stimuli above 60 kHz could not be delivered; not a hearing threshold". Append to `note`: "Live broadband vibrometry (7 specimens) found tympanal resonances near 108 to 111 kHz; startle thresholds of nine females were nearly flat from about 40 to 120 kHz (Table 3), so the live behavioural gain at 90 to 120 kHz is small."
- d181 line 2 `value`: "the authors conclude the pinnae do not assist directional hearing at conspecific call frequencies (about 23 kHz) and act as ultrasound detectors; pinnae still changed tympanal arrival time and phase difference, with effects depending on angle of incidence". `conditions`: "laser Doppler vibrometry of 13 live ears at 23, 40 and 60 kHz across incidence angles, with and without pinnae, plus numerical simulations; the cue measured is the difference between the anterior and posterior tympana of one ear". Replace the note's "Contrary/null result: the pinnae give no directional benefit at the species' own call frequencies." with "Qualified null: the authors' conclusion rests on small effects at 23 kHz (arrival time 0.56 ± 0.05 to 0.55 ± 0.05 µs, reported as a significant delay), a significant pinnae × angle interaction (F = 4.47, p = 0.012, Table 1), larger phase differences with pinnae (80.9° against 62.7° ablated) and simulations giving higher pressure at 23 kHz without pinnae (t = 3.45, p < 0.001); the Discussion says the pinnal contribution to tympanal displacement depended on incident angle at 60 kHz and below."
- d181 line 6 `conditions`: "lab-bred fish, n = 11, anaesthetised; tones started at 140 dB re 1 µPa with 2.5 dB decrements; responses at 4,000 and 6,000 Hz were not consistently present in all recordings and were excluded from statistical analysis, so the 4,000 Hz value comes from the fish that responded, at the top of the levels presented". In `note`, replace "dB reference taken as re 1 µPa from the paper's soundscape units; not restated in this sentence." with "dB re 1 µPa: the Methods give stimulus levels in dB re 1 µPa (hydrophone calibration; particle motion not measured); the reference is not restated in this sentence."

Uncounted fixes:

- d181 lines 1 to 4 `source.journal`: "eLife 11: e77628".
- d181 line 3 `note`: "pinnal contribution about 17 to 20 dB" to "pinnal contribution about 17 to 20 dB (computed here: 26.33 − 9.69 and 30.04 − 9.83)"; append "The text gives n = 8 prints; Table 1 lists four ears for this model."
- d181 line 4 `note`: append "The paper does not say how 59.28 dB SPL was derived; the Table 3 means for 90 to 120 kHz average about 58 dB SPL."
- d181 line 5 `note`: append "Pressure thresholds only; particle motion was not measured."
- d181 lines 8 and 9 `note`: append "Crossref records an Author Correction (10.1038/s41598-022-19236-y, 6 September 2022); values read on the updated nature.com article; the correction's content was not reached. Name: Catalog of Fishes (spid 23117) lists Hippoglossus vulgaris Fleming 1828 as a synonym of H. hippoglossus (Linnaeus 1758), family Pleuronectidae (Hippoglossinae); some classifications place Pleuronectidae in Carangiformes." Replace "the WoRMS page itself did not load, so the family and order are not authority-checked here" with "the WoRMS and OBIS pages did not load".
- d181 line 8 `note`: replace "The rod sentence was read in full on one fetch and in part on the second (the Fig. 8F reference was dropped by the second summary)." with "The rod sentence, including '(Fig. 8F).', was confirmed on audit 265's two passes."
- d180 line 5 `conditions`: append "; anaesthetised with ketamine and medetomidine (with atropine)". `note`: append "No statistical test of the frequency effect is reported; the authors state that gerbil hearing up to 20 kHz resembles the human audiogram with best hearing around 4 kHz (citing Ryan 1976)."

## Owner questions

1. Copiphora line 2: whether a paper's own null conclusion should be filed when its data show significant but small effects of the same factor. I count the record as needing the qualification; the owner may prefer to drop it and keep lines 1, 3 and 4.
2. The halibut Author Correction (10.1038/s41598-022-19236-y) could not be read from either copy. The values were read on the updated article, so they should be the corrected ones; the owner may want the notice checked through the library.
3. Fish order: Pleuronectiformes (FishBase, WoRMS) against Carangiformes (Betancur-R., as on Wikipedia) for Pleuronectidae. The desk has used Pleuronectiformes (desk-d159); one convention should be fixed.

Progress notes: desk-d181.md is accurate on what was read and refused. Its claim that the rod quote's "(Fig. 8F)." was dropped by one fetch is now settled (present). desk-d180.md lines 1 to 4 concern the dropped Nilaparvata records and were not judged.

Verdict: 3 errors in 10 (30.0%), above the 5% bar; pooled 40.5%. Error lines: desk-d181 lines 1, 2 and 6, all fixable with the counted replacement text. desk-d181 lines 3, 4, 5, 7, 8, 9 and desk-d180 line 5 can merge with the uncounted fixes. No record is unfixable.
