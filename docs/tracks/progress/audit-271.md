# audit-271: desk-d187 (7 evidence records, no search records, no wanted lines)

Audited 31 October 2026 from the desk-d187 files present untracked in the worktree (docs/tracks/progress/desk-d187.md and 7 evidence lines in docs/views/evidence/desk-d187.jsonl; neither committed here, neither edited). `tools/senses/check.py` on the evidence file: 7 records, 0 problems. Quote lengths (`len(q.split())`), lines 1 to 7: 25, 36, 38, 14, 36, 24, 27; all within 40. No searched or wanted file, so all seven records were judged. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md (grade and `partial`), BRIEF quote rules, the publisher-copy and repository-licence rule and the name rule, in the form of audits 268 to 270. Duplicates checked with git grep on origin/main (b883e09e) under docs/views/evidence, docs/views/audit/corrected, docs/views/audit/ALL.jsonl, docs/views/searched and docs/views/wanted for "Astyanax mexicanus", "Trachemys scripta", Halichoerus, Ruser, Alytes, Caorsi and the four DOIs. 0 WebSearch and 13 WebFetch calls used.

Sources opened: api.crossref.org/works/ 10.7717/PEERJ.8148, 10.1007/S00359-019-01372-Y, 10.1242/BIO.062059, 10.1038/S41598-019-55639-0; peerj.com/articles/8148 (record URL, three passes, title confirmed each time); link.springer.com/article/10.1007/s00359-019-01372-y (record URL, one pass, title confirmed); pmc.ncbi.nlm.nih.gov/articles/PMC6863946/ (the desk's second copy, one pass, citation confirmed); pmc.ncbi.nlm.nih.gov/articles/PMC12403521/ (record URL, two passes, title confirmed); nature.com/articles/s41598-019-55639-0 (record URL, two passes, title confirmed). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened; nothing was refused. WebFetch returns model summaries, so quotes were checked by MATCH/MISMATCH against returned fragments; points marked "(tool summary)" were not returned verbatim.

## Bibliographic and licence (Crossref, fresh)

- Simon: Noah Simon, Suguru Fujita, Megan Porter, Masato Yoshizawa; title as recorded; PeerJ 7, e8148; issued 2019-12-17; CC BY 4.0, content-version unspecified, from 2019-12-17; relation empty; no update-to. As recorded. Page: "This is an open access article distributed under the terms of the Creative Commons Attribution License". Accepted.
- Wang: Tongliang Wang, Handong Li, Jianguo Cui, Xiaofei Zhai, Haitao Shi, Jichao Wang; title as recorded; J Comp Physiol A 205, issue 6, 847-854; online 2019-10-25, print 2019-12; CC BY 4.0 tdm and vor from 2019-10-25; relation empty; no update-to. As recorded. The Springer page text returned no licence sentence ("Open access", "2019 The Author(s)" only); the PMC copy states "This article is distributed under the terms of the Creative Commons Attribution 4.0 International License". The publisher's own free full text is accepted in any case, and the repository copy carries its own open licence statement. Accepted.
- Ruser: Andreas Ruser, Kirstin Anderson Hansen, Magnus Wahlberg, Tobias Schaffeld, Ursula Siebert; title as recorded; Biology Open 14, issue 8, bio062059; issued 2025-08-15, online 2025-08-19; CC BY 4.0 vor from 2025-08-19 (delay 4); relation empty; no update-to. As recorded. PMC copy states CC BY 4.0 ("permits unrestricted use, distribution and reproduction in any medium provided that the original work is properly attributed"). Accepted.
- Caorsi: Valentina Caorsi, Vinicius Guerra, Raíssa Furtado, Diego Llusia, Lívia Roese Miron, Márcio Borges-Martins, Camila Both, Peter M. Narins, Sebastiaan W. F. Meenderink, Rafael Márquez; title as recorded; Scientific Reports 9, issue 1, article 19456; issued 2019-12-19; CC BY 4.0 tdm and vor from 2019-12-19; relation empty; no update-to. As recorded (the journal string omits issue 1; harmless). The nature.com page text returned no licence sentence ("Open access", "2019 The Author(s)"); accepted on Crossref vor CC BY with the publisher's own free copy.

Bibliographic faults 0; licence faults 0.

## Names

- Astyanax mexicanus: Catalog of Fishes spid 3965, valid, Acestrorhamphidae (audit 269, not re-fetched). The record names the Pachon cave morph in `eye` and `conditions`, as the cavefish rows on main do. Not pooled.
- Trachemys scripta elegans: EXACT, ACCEPTED in docs/views/gaps/gbif-names.tsv (6157026; parent Trachemys scripta 2443002; Pseudemys scripta elegans listed as its synonym). The paper prints "Trachemys scripta elegans" in title, abstract and Discussion. Filing at rank subspecies is right and matches the eight hearing rows already on main under the same name. Accepted.
- Halichoerus grypus: valid per MDD (audit 249; not re-fetched here). Accepted.
- Alytes obstetricans: EXACT, ACCEPTED in gbif-names.tsv (2426612). The paper tested only this species (tool summary). Accepted.

Name faults 0; cultivar or pooled 0.

## Duplicates

- Simon 2019 on main: desk-d185 lines 4 to 6 (surface fish more active in light with or without pineal; cavefish burst suggested non-pineal; no cavefish burst at light-to-dark). Line 1 here is the cavefish light/dark activity sentence, a different sentence and result. It is the row audit 269 recommended (owner question 3 there). Not a repeat.
- Trachemys scripta elegans hearing on main: [300, 500] best sensitivity (no DOI, another source) and four Wang 2022 temperature rows (10.3389/fevo.2022.856660). The DOI 10.1007/s00359-019-01372-y is not on main. Not a repeat.
- Halichoerus grypus on main: three rows from Ruser et al. 2014 PLoS ONE (10.1371/journal.pone.0090824). 10.1242/bio.062059 is not on main. Not a repeat.
- Alytes obstetricans on main: oil_droplets, diel, pupil_shape, eye_diameter_mm; no sense_vibration row; Caorsi and the DOI absent. Not a repeat.

Duplicates 0.

## Per-paper findings

### Simon et al. 2019 (line 1)

Quote MATCH (Results, "Diurnal activity pattern is maintained after removal of the pineal"), returned in two pieces of one sentence; whole sentence; the value says no more than the quote. The next sentence MATCH for the paired day-night statistics: "(between day and night: N = 18, t17 = 3.9, P < 0.01; and N = 15, t14 = 3.8, P < 0.01 after Bonferroni correction," with Tables S7 and S8. The desk's placement of the P values in `conditions` rather than the quote is correct, and they do not change the value.

Two faults in `conditions`.
(a) Wrong source fact. `conditions` says "The next sentence of the same paragraph gives the diurnal activity shift as P = 0.005 in control and P = 0.008". The next sentence is the N/t/Bonferroni sentence. The P = 0.005 and 0.008 sentence, "As reported, a diurnal activity shift was observed in control cavefish (P = 0.005), and importantly, in pinealectomized cavefish as well (P = 0.008).", sits in the section's final paragraph, about eight sentences later (tool count), and restates the comparison ("As reported"). The record also reads as if two tests were run; they are one comparison reported twice.
(b) Design omitted, causal interpretation. Methods: "White LED strips were placed in the recording chamber above the fish and maintained on a 13:11 h light:dark timer"; one 24 h recording per fish from about ZT-2, analysed in the middle four hours of day and night ("ZT6-10 and ZT19-23"). So "light" and "dark" are the day and night phases of an entrained cycle in the same fish. There is no constant-dark or constant-light condition and no test separating a direct light response (masking) from a circadian rhythm (tool summary; the Discussion raises masking only from prior work and says the light-ON burst "could also be regulated by circadian rhythm without light input"). The record's `method` ("locomotor activity under light and dark") and `conditions` (light 30 to 100 lux, no photoperiod) do not say this, though the main d185 rows carry "13:11 L:D". Filed under sense_light_nonvisual, the row reads as a direct light response of eye-degenerate fish; the design cannot show that. The arena caveat main carries (small 3.48 cm wells "may make fish nervous") is also missing (uncounted on its own).

Counted once (scientific context and wrong fact, fixable).

### Wang et al. 2019 (lines 2 and 3)

Quotes MATCH on Springer and PMC: line 2 (Results, Fig. 3a) and line 3 (Discussion), each returned in two pieces of one sentence; whole sentences; values within the quotes. Methods (tool summary with verbatim fragments): tone bursts "from 0.2 to 1.5 kHz in 100 Hz increments"; 10 males and 10 females, 5 years old; "0.5% pelltobarbitalum natricum" intramuscular; held at "28–32 °C", test temperature not stated; body mass "female: 1681.60 ± 195.31 g, male: 1069.7 ± 151.06 g"; free-field calibration at the jaw tip, dB SPL with no stated reference; females "generally approximately 3 dB lower"; tympanum diameter "no significant difference between the sexes ... (p = 0.08)". Results (MATCH on both copies): "the waveforms were not obvious at or above 1.1 kHz". The threshold ANOVA reports df = 8, which implies nine frequencies, against ten from 0.2 to 1.1 kHz (tool summary; owner question 2).

Line 2 (sex difference 0.2 to 1.1 kHz). Counted (scientific context, fixable). The reported significance at 1.1 kHz sits at the frequency where the authors say waveforms were not obvious; the record carries the 1.1 kHz end of the range with no such qualification. `conditions` also states "the dimorphism is not explained by tympanum size" as established; the test was p = 0.08 with n = 10 per sex, females 57% heavier, and the abstract's own wording is "does not appear to be related". Both limit the claimed effect's extent and its causal reading.

Line 3 (hearing range 0.2 to 0.9 kHz, best 0.6 kHz). Counted (scientific context, fixable). `conditions` says "the Results tested up to at least 1.1 kHz ... so the upper bound is the authors' summary, not the highest frequency with a response". The paper tested to 1.5 kHz and says waveforms were not obvious at or above 1.1 kHz, so the record's reading, that responses extend past 0.9 kHz, is the record's own inference and runs against the Results. Also omitted: the test temperature is not stated, and main's Wang 2022 rows show this species' bandwidth moving from 0.2-0.5 kHz at 10 °C to 0.2-1.5 kHz at 40 °C, so the range applies only at an unstated temperature (the record says only "held at 28-32 degrees C before testing").

### Ruser et al. 2025 (lines 4 and 5)

Quotes MATCH (Abstract), whole sentences. Table 1 (tool summary): 4 kHz Hg_1 42.9, Hg_2 43.8 dB re 1 µPa, so "43-44" is one value per seal and both seals peak at 4 kHz; dB reference stated by the paper as re 1 µPa. Both seals male, born 2014 and 2017, tested 2018 to 2021. Methods: "the interval from threshold to ambient noise level was close to or smaller than the critical ratio at some frequencies"; the authors call the results "unusually low" and ask for confirmation; ambient PSD at 4 kHz 38.4 ± 5.4 dB re 1 µPa²/Hz.

Line 4. Confirm. Conditions match (n = 2, pool, critical-ratio caveat, 6.0 to 13.3 dB inter-seal difference below 4 kHz).

Line 5. Confirm. Value equals the quote; `conditions` carries n = 2, the corroboration caveat and the inter-seal spread. Not stated (uncounted): the Discussion singles out Hg_1 ("particularly in individuals with hearing thresholds such as Hg_1"), and whether Hg_2 also falls below the PCW curve can be read only from Fig. 1; the PCW audiogram is built from 14 phocids of seven species, none of them grey seals (tool summary). The record's inter-seal spread already conveys that the low-frequency result is driven by one animal's lower thresholds, and possible masking by ambient noise would raise thresholds, so it does not undercut the direction; left uncounted, fix below.

### Caorsi et al. 2019 (lines 6 and 7)

Quotes MATCH: line 6 (Abstract) whole sentence; line 7 (Results) opening MATCH and the cut at "respectively …" marked; the full sentence runs to about 46 words, so the cut is needed and keeps subject and values; the cut clause (8 calls per min, synthetic stimuli) is in `conditions`.

Admissibility. BRIEF's sense_vibration is "substrate or web vibration: organs, frequency range, threshold", a string with figures; main files behavioural responses to substrate vibration under it (Apis, Monochamus, Pagurus). A call-rate change to buried-transducer playback is admissible as behavioural evidence of substrate-vibration sensing, with the sound confound stated. Method (tool summary): Clark Synthesis tactile transducer buried 5 to 10 cm, 4 to 6 m from the male; peak-normalised stimuli faded in over 2 min; a 1 s wind-turbine test stimulus used to set distance for equal amplitude; treatment order randomised per animal; no-stimulus treatment and 2 min silent intervals as controls, no sham transducer; "a geophone and a microphone were placed at a distance of 20–30 cm from the focal animal", but no airborne level from the transducer is reported and no sentence addresses airborne sound. Nulls: call duration p = 0.99, dominant frequency p = 0.68; pre/post baselines no difference; air temperature no effect on call rate (p = 0.16). Power threshold: "n = 15, likelihood-ratio test: x2 = 25.46, df = 3, p < 0.005"; "higher for traffic than wind farm" (MATCH). Line 7's conditions match all of these.

Line 6. Counted (quote-form: value beyond quote, fixable). The quote says "both seismic sources" and "other parameters remained stable"; the value names traffic and wind turbine vibration and "call duration and dominant frequency". Both facts are true and in `conditions`, but the value says more than its quote, the fault audit 269 counted on its line 2. The sound confound is stated correctly.

Line 7. Confirm. Uncounted: `conditions` could say a microphone was placed beside the geophone but no airborne level is reported, and give n = 15 for the threshold test.

Missed measurement (uncounted for evidence, as in audits 269 and 270): the behavioural power thresholds in dB re 1 (µm/s)² per stimulus type (Table 3) are the paper's threshold figures for BRIEF's sense_vibration, and the desk did not read Table 3. Owner question 3.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Astyanax mexicanus Pachon, more active in light than dark with or without pineal | correct | method, conditions | Quote MATCH; light/dark are day/night of a 13:11 cycle in one recording, no DD or masking test; P-value sentence misplaced as "next sentence" |
| 2 | Trachemys scripta elegans, female ABR thresholds lower 0.2-1.1 kHz except 0.9 | correct | value, conditions | Quote MATCH; waveforms "not obvious at or above 1.1 kHz" omitted; tympanum p = 0.08 stated as excluding a cause |
| 3 | Trachemys scripta elegans, range [200, 900] Hz, best 0.6 kHz | correct | conditions | Quote MATCH; record's reading of responses beyond 0.9 kHz runs against Results; test temperature unstated and range is temperature-dependent |
| 4 | Halichoerus grypus, best 4 kHz, 43-44 dB re 1 µPa | confirm | none | Quote MATCH; one value per seal (42.9, 43.8); caveats present |
| 5 | Halichoerus grypus, low-frequency thresholds below standard phocid audiogram | confirm | (conditions; uncounted) | Quote MATCH; Hg_1 emphasis and PCW composition could be added |
| 6 | Alytes obstetricans, call rate fell under both seismic sources, other parameters stable | correct | value | Quote MATCH; value names sources and parameters the quote does not |
| 7 | Alytes obstetricans, mean call-rate fall 15 and 17.5 calls/min | confirm | (conditions; uncounted) | Quote MATCH, cut marked and needed; conditions verified |

Evidence errors: 4 of 7 (57.1%): scientific-context faults 3 (lines 1, 2, 3; line 1 also carries a wrong source-location fact, counted once); quote-form faults 1 (line 6); duplicates 0; licence 0; bibliographic 0; name 0; pooled or cultivar 0. Unfixable records: none.

Pooled with audits 172 to 270: 213 of 529 evidence records (40.3%; audit 270's 209 of 522 plus 4 of 7 here; any audit running concurrently is not included). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Counted (line 1):
- `method`: "behavioural: locomotor activity in the day (light) and night (dark) phases of a 13:11 h light:dark cycle, one 24 h recording per fish analysed at ZT6-10 and ZT19-23; pinealectomy compared with sham controls"
- `conditions`: replace "The next sentence of the same paragraph gives the diurnal activity shift as P = 0.005 in control and P = 0.008 in pinealectomized cavefish." with "The section's final paragraph restates the same comparison as P = 0.005 (control) and P = 0.008 (pinealectomized) ('As reported, a diurnal activity shift was observed ...'). Light and dark are the day and night of an entrained 13:11 L:D cycle in the same fish, with no constant-dark or constant-light condition, so a direct light response (masking) is not separated from a circadian rhythm; the Discussion says the light-ON burst could also be regulated by circadian rhythm without light input. White LED; 1.2 to 1.5 cm SL; individual wells 3.48 cm across, which the Discussion says may make fish nervous and induce unexpected responses."

Counted (line 2):
- `value`: "female ABR thresholds were significantly lower than male thresholds from 0.2 to 1.1 kHz, except at 0.9 kHz (p = 0.053); the authors note waveforms were not obvious at or above 1.1 kHz"
- `conditions`: replace "the abstract reports no sex difference in tympanum diameter, so the dimorphism is not explained by tympanum size" with "tympanum diameter did not differ significantly between the sexes (p = 0.08, n = 10 per sex), and the authors say the difference 'does not appear' related to tympanum size; females were also about 57% heavier, so a body-size effect is not excluded"; append "; tone bursts 0.2 to 1.5 kHz in 100 Hz steps; dB SPL with no stated reference, free-field calibration at the jaw tip".

Counted (line 3, `conditions`): replace "The Discussion states the range as 0.2-0.9 kHz, while the Results tested up to at least 1.1 kHz and report significant sex differences to 1.1 kHz, so the upper bound is the authors' summary, not the highest frequency with a response." with "Tone bursts 0.2 to 1.5 kHz were tested; the Results say waveforms were not obvious at or above 1.1 kHz, and the Discussion gives the range as 0.2 to 0.9 kHz. Test temperature is not stated (animals held at 28-32 degrees C before testing); in this subspecies the ABR bandwidth depends on temperature (Wang et al. 2022, on main: 0.2-0.5 kHz at 10 degrees C to 0.2-1.5 kHz at 40 degrees C), so the range applies at an unstated temperature."

Counted (line 6, `value`): "males cut their call rate in response to both seismic sources; other call parameters stayed stable" (`conditions` already names the sources as traffic and wind-turbine substrate vibration and the parameters as call duration and dominant frequency; add "both seismic sources = recorded and synthetic traffic and wind-turbine vibration" there if the owner wants the value self-contained without exceeding the quote).

Uncounted:
- Line 5 `conditions`: append "; the Discussion singles out Hg_1 ('particularly in individuals with hearing thresholds such as Hg_1'), and whether Hg_2 also falls below the standard curve is shown only in Fig. 1; the standard phocid (PCW) audiogram is built from 14 phocids of seven species, none of them grey seals".
- Line 6 and 7 `conditions`: replace "no statement that airborne sound from the transducer was excluded" / "no airborne-sound control found in the passages read" with "a microphone was placed beside the geophone 20-30 cm from the male, but no airborne level from the transducer is reported and the paper does not address airborne sound; no sham transducer; treatment order randomised per male"; line 7 append "; threshold test n = 15".
- Line 1 `note`: append "Audit 269 recommended this row (its owner question 3)."

## Owner questions

1. Simon 2019: the tool summary reports that the only non-significant day/night result in the paper is for pinealectomized surface fish (P > 0.05). If that holds, main's desk-d185 line 4 ("surface fish are more active in light than in dark, with or without the pineal organ") omits a null that limits it. Unverified here (tool summary, not returned verbatim); worth a targeted recheck of main.
2. Wang 2019: the threshold ANOVA reports df = 8 (nine frequencies) while the sex comparison spans ten frequencies from 0.2 to 1.1 kHz. Should a note flag the inconsistency, or leave it as the paper prints it?
3. Caorsi 2019: Table 3 gives the behavioural power thresholds in dB re 1 (µm/s)² per stimulus type, the threshold figures BRIEF's sense_vibration asks for. File them as rows once Table 3 is read on the publisher copy?

Progress note: accurate on sources, licences, names and the not-a-repeat reasoning; it repeats the misplaced "next sentence" claim for the Simon P values and does not mention the 13:11 day/night design, the "not obvious at or above 1.1 kHz" Results sentence or Table 3.

Verdict: 4 errors in 7 (57.1%), above the 5% bar; pooled 40.3%. Error lines: 1, 2, 3, 6. No unfixable records; lines 1, 2, 3 and 6 can merge with the counted text, and lines 4, 5 and 7 as they stand or with the uncounted fixes.
