# audit-276: desk-d192 (10 evidence records, no search records, no wanted lines)

Audited 31 October 2026 from the desk-d192 files present untracked in the worktree (docs/tracks/progress/desk-d192.md and 10 evidence lines in docs/views/evidence/desk-d192.jsonl; neither committed here, neither edited). `tools/senses/check.py` on the evidence file: 10 records, 0 problems. Quote lengths (`len(q.split())`), lines 1 to 10: 18, 18, 18, 16, 38, 40, 14, 16, 31, 32; all within 40 (line 6 exactly at the limit). No searched or wanted file, so all ten records were judged. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md (grade and `partial`), BRIEF quote rules, the publisher-copy licence rule and the name rule, in the form of audits 270 to 275. Duplicates checked with git grep on origin/main (929c438f) under docs/views/evidence, docs/views/audit (corrected, ALL.jsonl and the unit audit files), docs/views/searched and docs/views/wanted for Asiophrida, xanthospilota, Exolontha, "Anoplophora glabripennis", Endebius, "Octopus vulgaris", Maselli, "Sensorial Hierarchy", 88.9, the first authors (Liang Z, Shang X, Jiang X, Zhang T-H) and all five DOIs. 9 WebSearch and 19 WebFetch calls used.

Sources opened: api.crossref.org/works/10.3390/INSECTS15070532, /10.3390/AGRONOMY12020481, /10.3390/INSECTS14050465, /10.3390/BIOMIMETICS10080513 and /10.3390/ANI10030457 (all answered in uppercase); the five record URLs on www.mdpi.com (Asiophrida twice); en.wikipedia.org/wiki/Exolontha, worldspecies.org/ntaxa/2380693 (a GBIF backbone mirror), gbif.org/species/1076250 (Endebius), gbif.org/species/1819693 and www.eol.org/pages/332762/names (both returned by searches for Asiophrida xanthospilota; both turned out to be other taxa), all from WebSearch results. Refused or blocked, not retried and not worked around: api.gbif.org/v1/species/match for Endebius florensis, Exolontha castanea and Asiophrida xanthospilota (permission not answered); www.biolib.cz/en/taxon/id792217 (robot security check); publication.plazi.org Endebius page (redirect stub only). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries, so quotes were checked by MATCH/MISMATCH with longer sentences returned in chunks of at most 12 words; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification.

## Bibliographic and licence

All five Crossref records agree with the records on author order, title, journal, volume, issue, article number and year; none has an update-to or a relation.
- Liang et al. 2024 (lines 1, 2): Zu-Long Liang, Tian-Hao Zhang, Jacob Muinde, Wei-Li Fan, Ze-Qun Dong, Feng-Ming Wu, Zheng-Zhong Huang, Si-Qin Ge; Insects 15(7): 532; issued 2024-07-13; licence CC BY 4.0 (vor).
- Shang et al. 2022 (lines 3, 4): Xian-Kun Shang, Xue-Hong Pan, Wei Liu, Ji-Li Wei, Cheng-Hua Huang, François-Régis Goebel, Amin Nikpay; Agronomy 12(2): 481; issued 2022-02-15; CC BY 4.0.
- Jiang et al. 2023 (lines 5, 6): Xianglan Jiang, Xiaoxia Hai, Yongguo Bi, Feng Zhao, Zhigang Wang, Fei Lyu; Insects 14(5): 465; issued 2023-05-15; CC BY 4.0.
- Zhang et al. 2025 (lines 7, 8): Tian-Hao Zhang, Zheng-Zhong Huang, Lei Jiang, Shen-Zhen Lv, Wen-Tao Zhu, Chao-Fan Zhang, Yi-Shi Shi, Si-Qin Ge; Biomimetics 10(8): 513; issued 2025-08-06; CC BY 4.0.
- Maselli et al. 2020 (lines 9, 10): Valeria Maselli, Al-Sayed Al-Soudy, Maria Buglione, Massimo Aria, Gianluca Polese, Anna Di Cosmo; Animals 10(3): 457; issued 2020-03-10; CC BY 4.0.

Licence on the copy read: each MDPI page carries a Creative Commons rights field, and the Exolontha, Endebius and Octopus pages returned MDPI's open-access statement ("For articles published under an open access Creative Common CC BY license," fragment, Octopus page). The tool returned no footer statement for the Asiophrida and Anoplophora pages; their page metadata gives creativecommons.org/licenses/by/3.0/ where Crossref gives 4.0 (the same 3.0 metadata field appears on all five pages, so it looks like a site-wide tag). Publisher's own CC BY copy; met. Uncounted: the progress note's "all CC BY" holds, but none of the records names the licence or version.

Bibliographic faults 0; licence faults 0.

## Names

- Octopus vulgaris (lines 9, 10): gbif-names.tsv "Octopus vulgaris EXACT ACCEPTED" (2289671). Accepted.
- Anoplophora glabripennis (lines 5, 6): gbif-names.tsv "Anoplophora glabripennis EXACT ACCEPTED" (7572133). Accepted.
- Exolontha castanea (lines 3, 4): not in gbif-names.tsv; GBIF's match API blocked. The GBIF backbone mirror at worldspecies.org lists "Animalia > Arthropoda > Insecta > Coleoptera > Scarabaeidae > Exolontha > Exolontha castanea" but shows no status or authority; Wikipedia's Exolontha page lists it as "Zhang, 1965" (the paper's "Chang" is the older romanisation of the same name). Present in the backbone; accepted status not shown on any page I could open. Uncounted: the record's family "Melolonthidae" is the paper's usage; the GBIF backbone mirror places the genus in Scarabaeidae, and no evidence row on main uses the family name Melolonthidae.
- Asiophrida xanthospilota (lines 1, 2): UNVERIFIED. Not in gbif-names.tsv; GBIF API blocked; the two pages searches returned as possible authority pages were other taxa (Mylantria xanthospila, Leptobrachium xanthospilum). A Semantic Scholar topic "Ophrida xanthospilota" shows the older combination exists (Asiophrida was split from Ophrida), so the name is a plausible current combination, not a checked one.
- Endebius florensis (lines 7, 8): UNVERIFIED. GBIF's genus page (1076250) shows "Endebius Lansberge, 1880" in Scarabaeidae ("as Dynastidae" in its references) but listed no species; BioLib behind a robot check. Name as printed in the paper.

Name faults 0 counted; 2 names unverified (4 records), 1 present but status not shown (2 records).

## Duplicates

- Octopus vulgaris on main: lambda_max_nm, receptor_classes, colour_vision, acuity_cpd, cff_hz, fovea, rhabdom_um, eye_movement, eye_type, polarization, several behaviour_vision pupil rows, diel, sense_touch, sense_light_nonvisual (Maselli et al. 2025, another paper) and docs/views/audit/corrected/sea-invertebrates.jsonl:119, sense_chemical, "food choice depends more on chemical than visual cues (88.9%)", from Maselli et al. 2020 (10.3390/ani10030457), Abstract, quote "Nevertheless, food choice resulted in being more dependent on chemical cues than visual ones (88.9%, Friedman test"; ALL.jsonl:3943 gives it "stands". **Line 10 repeats that row: same species, paper, trait, section and sentence.** Line 9 (T2 visual-only 50%, behaviour_vision) is a different finding from the same paper and is not on main.
- Anoplophora glabripennis on main: three opsin_sequences_recovered rows (Sharkey et al. 2017, retracted in ALL.jsonl), and two wanted lines on olfaction and oviposition. No phototaxis or trap row and no 10.3390/insects14050465. Not a repeat.
- Asiophrida, Exolontha, Endebius: no evidence row on main. The Liang et al. 2024 paper is named in screened lists of other genera's search records (harvest-36, harvest-43 and others) as another genus's paper, not filed. Not a repeat.

Duplicates 1 (line 10).

## Per-paper findings

### Liang et al. 2024, Asiophrida xanthospilota (lines 1, 2)

Line 1 quote MATCH (Abstract), whole sentence. Line 2 quote MATCH (Results 3.4, ERG Testing), whole sentence. Context: the next sentence in 3.4 reads "When comparing the response intensity of red and yellow light wavelengths" "between males and females, no significant difference was found." (two chunks). Results 3.4 also gives the sex-specific maxima: "Among females, the green-light stimulation elicits the highest signal intensity," and "In males, in contrast, blue-light stimulation elicits the highest signal intensity," (both verbatim), red lowest in both. Methods 2.5 give one stimulus level for all colours, "with an approximate illuminance of ca. 100 lux." (verbatim fragment), and no nm values for the ERG LEDs; the nm ranges (red 620-625, yellow 588-590, green 515-525, blue 460-465, UV 365-400) are given only for the phototaxis test in 2.6 (tool summary). Figure 8 caption "n = 9"; the text does not say whether that counts individuals (tool summary). The paper also reports a phototaxis test, "The phototropism experiments showed that both males and females exhibited positive phototaxis to all five lights," (Abstract, verbatim), blue strongest; the unit filed no record of it.

Line 1. Counted (scientific context, fixable). The value ranks colours by ERG amplitude ("strong to blue and green, weak to red") but the record gives no stimulus level. All colours were set to about 100 lux; illuminance weights radiance by the human photopic curve, so at equal lux a 460 nm stimulus carries many times the photons of a 520 nm one (my own construction from the photopic curve; the paper gives no radiometry) and a UV stimulus is barely defined in lux. That bears on the blue ranking directly (the weak red response survives it, since red also gets more photons than green at equal lux). The value also merges the sexes, whose maxima differ (green in females, blue in males). Both belong in `conditions`.

Line 2. Counted (value says more than the quote). The value adds "red and yellow responses did not differ between sexes", which the quoted sentence does not say; the note itself says that sentence was not quoted. The claim is true (verified above), so the fix is to keep the value to the quote and give the red/yellow sentence in the note with its location, or file it as its own record. Uncounted: the cross-sex comparison uses the same stimuli for both sexes, so the equal-lux issue does not affect this record; add the 100 lux level anyway.

Trait key (lines 1, 2): ERG amplitudes at five colours with no nm and no hue-discrimination test are filed as colour_vision. tools/senses/check.py accepts the key; main is mixed (ERG rows sit mostly under lambda_max_nm when nm are given, eleven under spectral_range_nm and four under colour_vision, e.g. Trybliographa rapae). Not counted; owner question 1.

### Shang et al. 2022, Exolontha castanea (lines 3, 4)

Line 3 quote MATCH (Abstract), whole sentence. Line 4 quote MISMATCH in form: the printed sentence continues "Females had positive phototaxis to 13 monochromatic light" "with wavelengths ranging from 365 to 630 nm," ", and the phototactic response rate decreases gradually" "with the increase in wavelength." (chunks as returned; 27 tokens in all), Results 3.1. Methods (verbatim): "The light intensity of the experiment was set as 50 lux" "for the phototactic reaction experiment of different spectra."; "Ten insects (females and males tested separately) were used in each group" "with six replicates."; "Insects once tested were not reused."; "The duration of each illumination lasted 20 min."; "insects were dark adapted for 2 h before the experiment." Female response rates ranged "from 30.00% to 88.33%" (fragment). Males in 3.1: "Males were sensitive to ultraviolet, violet, and blue light at 365–435 nm," "and the phototactic response rate was more than 70%." and, separately, "males had negative phototaxis at 365 nm, 380 nm, 475 nm," "500 nm, 520 nm, and 550 nm," with "the response rate of photophobic behavior was very low, less than 5%" (fragments); the Discussion says both sexes were positive at all 13 (tool summary). "Under the light intensity of 10 lux, 50 lux, and 100 lux at 360 nm," confirms the note's 360/365 nm misprint. Intensity test: females highest 93.33% at 100 lux (365 nm), males 93.33% and 91.67% at 100 and 300 lux (420 nm); "There was no significant difference among light intensities of G3." (verbatim).

Line 3. Confirm. Equal-lux confound, sexes tested separately, response rates and the 360 nm misprint are all in the record. Uncounted: add "insects not reused; 20 min exposure after 2 h dark adaptation".

Line 4. Counted (quote form and scientific context, fixable; counted once). Unmarked cut of a 27-token sentence that fits the limit whole. The dropped clause is a magnitude qualifier: positive phototaxis at all 13 wavelengths ran from 88.33% at 365 nm down to 30.00%, falling with wavelength, and the value "positive phototaxis at all 13 monochromatic lights" without it reads as a uniform response. `conditions` should carry the equal-lux caveat that line 3 carries.

### Jiang et al. 2023, Anoplophora glabripennis (lines 5, 6)

Line 5 quote MATCH (Results 3.3), whole sentence; line 6 quote MATCH (Results 3.4), whole sentence, "X2" and the inverted p range as printed. Methods (tool summary with quoted fragments): intensity "always maintained at 180 lx," except the 365, 420 and 435 nm LEDs, which reached only 24, 144 and 36 lx at the chamber centre; "The 10 adult females or males, as one replicate in each test." (fragment); results read "after an illumination time of 120 min." (fragment); five time slots, 9:00-11:00, 14:00-16:00, 19:00-21:00, 0:00-2:00 and 5:00-7:00; reuse of beetles not stated. Section 3.4 (verbatim chunks): "The behavioral responses of females were determined at different light intensities" "at 420 nm, 435 nm, 560 nm, and 595 nm, which were the wavelengths most preferred by females and males"; "Overall, 18 lx was the most attractive for females under short-wavelength illumination" "(420 nm and 435 nm), while 180 lx was the most attractive under long-wavelength illumination (560 nm and 595 nm),"; "but there was no significant difference between the different light intensities at a 120 min exposure time."; at 420 nm 36 lx drew fewer females at 15, 30, 45 and 90 min, and at 560 nm 90 and 180 lx drew more than 45, 360 and 720 lx at 15 and 30 min. The paper says "Fourteen monochromatic LED lamps" but lists 13 wavelengths, and mentions a 455 nm lamp in the results (tool summary).

Line 5. Counted (scientific context, fixable). `conditions` say "each test light held at 180 lx; night-time exposure", and the note says "Equal lx across wavelengths". Both are wrong on the paper: the two winning wavelengths, 420 and 435 nm, ran at 144 and 36 lx against 180 lx for most others, and tests ran in five slots across day and night. Lower illuminance at the two top wavelengths changes how the ranking reads (the winners were not favoured by brightness, at least in lux), so this is consequential, and the confound the note names is the wrong one.

Line 6. Counted (scientific context, fixable). The intensity experiment was run on females only ("The behavioral responses of females were determined at different light intensities"), and the null is the 120 min reading; the value and conditions name neither, so the null reads as a property of the species. The note already carries the "18 lx most attractive" summary; add the time-course effects at 420 and 560 nm, which show intensity does change catches at shorter exposures.

### Zhang et al. 2025, Endebius florensis (lines 7, 8)

Line 7 quote MATCH (Abstract), whole sentence; line 8 quote MATCH (Abstract), whole sentence. The tool reported that the page ended mid-sentence in Section 3.3, so later parts were not read. Results (verbatim chunks): blue, "both female and male individuals exhibited strong positive phototaxis" "under blue light." with "extremely significant differences (p < 0.001)"; yellow, "all individuals of both sexes tested under yellow light" "did not enter the NLA." and "suggesting a possible negative phototaxis towards yellow light."; green, "only 2 out of 5 males passed through the NLA."; "There are no significant differences in NLA residence time" "between male and female individuals under green, yellow, and red light." Behavioural stimuli "200 lux" at the start point, ERG "pre-adjusted to 100 lux" (fragments); LEDs blue 463-469, green 516-525, yellow 586-596, red 625-645 nm (verbatim list). ERG: "The ERG signals generated by females under blue and green light stimulation" "were significantly higher than those under red light (p < 0.05)."; for males "the ERG signals under blue, green, and yellow light stimulation" "all were significantly higher than those under red light."; "The ERG signals under yellow light stimulation exhibited a large variation range."; "there were no significant differences in ERG signals between males and females."; "A total of six individuals participated in the test" (all verbatim chunks).

Line 7. Counted (scientific context, fixable). The value states "negative phototaxis to yellow" as a finding; the Results ground it only in no beetle entering the near-light area and call it "a possible negative phototaxis". No entry under yellow is consistent with indifference as well as avoidance, which is the causal reading the value asserts. `conditions` should give the group sizes the text shows (5 males under green) and the 200 lux level for all colours.

Line 8. Counted (scientific context, fixable). "Sensitivity to blue, green, and yellow, with reduced response to red" holds as tested for males; for females only blue and green were significantly above red, and the yellow responses varied widely. The value carries the abstract's yellow claim with neither limit. Add the 100 lux equal-illuminance level and the stimulus nm to `conditions`.

### Maselli et al. 2020, Octopus vulgaris (lines 9, 10)

Line 9 quote MATCH (Discussion), whole sentence; line 10 quote MATCH (Abstract), whole sentence. Methods (verbatim chunks): "Specimens of O. vulgaris (n = 4, bodyweight 600 ± 50 g, mean ± SD)" "were collected from the Bay of Naples (Italy) between June 2018 and October 2018."; "Each octopus was exposed to 5 trial days for each task."; "We performed FP followed by T1 as first, then animals were tested with the tasks fromT2 toT5 randomly." The paper gives no number of jars per trial and no chance level (tool summary). T2 Results: "In T2 (only visual discrimination), the octopuses had a significant decrease in recognition" "of the jar that contained the preferred food." with no task-level statistic (tool summary). T5: "all octopuses showed no difference in choosing the jar." (fragment). The 88.9% is the pooled share of successful first-opening decisions "based on chemical cues," "were significantly higher than visual one (88.9% vs. 11.1% respectively, Wilcoxon matched-pairs test p < 0.05)" (chunks); the abstract names a Friedman test for the same figure.

Line 9. Counted (scientific context, fixable). The record leaves open what the Methods settle: the same four animals ran every task, five trial days each, with the food-preference test and T1 always first and T2 to T5 in random order, so order and experience effects are possible; and the paper prints no chance level, so "only 50%" cannot be read as at, above or below chance from the paper. The note's "not checked" flags a gap in the desk's reading rather than conveying the limitation, so it does not excuse the omission.

Line 10. Counted (duplicate, unfixable). Repeats main's audit/corrected/sea-invertebrates.jsonl:119 (stands in ALL.jsonl:3943): same species, paper, trait, abstract sentence and value. Drop. The fuller quote and the "88.9% vs. 11.1%" reading belong as a fix to the main row, not a second row; owner question 3.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Asiophrida xanthospilota, ERG strong blue/green, weak red | correct | conditions | Quote MATCH; ~100 lux for all colours (equal lux, not equal photons) and sex-specific maxima omitted from a colour ranking |
| 2 | Asiophrida xanthospilota, male ERG > female at green/blue/UV | correct | value, note | Quote MATCH; value adds the red/yellow null the quote does not hold |
| 3 | Exolontha castanea, most sensitive 365 nm (F), 420 nm (M) | confirm | (conditions; uncounted) | Quote MATCH; equal-lux confound and rates in record |
| 4 | Exolontha castanea, females positive at all 13 wavelengths | requote | quote, value, conditions | Unmarked cut of a 27-token sentence; dropped clause is the fall in response with wavelength (88% to 30%) |
| 5 | Anoplophora glabripennis, top trap rates at 420 and 435 nm | correct | conditions, note | Quote MATCH; 420 and 435 nm ran at 144 and 36 lx, not 180 lx; tests in five day and night slots |
| 6 | Anoplophora glabripennis, no intensity effect at 435 and 595 nm | correct | value, conditions | Quote MATCH; females only, 120 min reading; time-course effects at 420 and 560 nm |
| 7 | Endebius florensis, positive to blue, negative to yellow | correct | value, conditions | Quote MATCH; Results call yellow "a possible negative phototaxis" from no entries; 5 males per group seen |
| 8 | Endebius florensis, ERG to blue, green, yellow; reduced red | correct | value, conditions | Quote MATCH; females' yellow not above red, yellow widely variable; n = 6; 100 lux all colours |
| 9 | Octopus vulgaris, visual-only jar choice 50% (T2) | correct | conditions, note | Quote MATCH; same 4 animals in all tasks, FP and T1 first, no chance level printed |
| 10 | Octopus vulgaris, chemical over visual (88.9%) | retract | (whole record) | Repeat of main audit/corrected/sea-invertebrates.jsonl:119 |

Evidence errors: 9 of 10 (90%): scientific-context faults 7 (lines 1, 5, 6, 7, 8, 9; and line 4, counted once with its quote fault); quote-form or value-exceeds-quote 2 (lines 2, 4); duplicates 1 (line 10); name 0 (4 records on unverified names, 2 on a name whose status was not shown); licence 0; bibliographic 0; abstract-access grading 0. Unfixable records: line 10.

Pooled with audits 172 to 275: 236 of 568 evidence records (41.5%; audit 275's 227 of 558 plus 9 of 10 here; any audit running concurrently is not included). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Counted (line 1):
- `conditions`: "adults of both sexes; ERG n = 9 (Figure 8 caption; the text does not say whether n counts individuals); all five stimuli set to ca. 100 lux (equal illuminance, not equal photon flux; nm not given for the ERG LEDs). Females' highest response to green, males' to blue; red lowest in both (Results 3.4)."
- `note`: add "Equal-lux stimuli favour blue and UV in photon terms, so the blue ranking is confounded; the weak red response is not."

Counted (line 2):
- `value`: "male ERG responses to green, blue and UV stimulation significantly higher than female responses"
- `conditions`: "adults, ERG n = 9 (Figure 8 caption); stimuli ca. 100 lux each"
- `note`: replace the sentence on the companion sentence with "Results 3.4 goes on: 'When comparing the response intensity of red and yellow light wavelengths between males and females, no significant difference was found.' (relayed in two parts; could be its own record)."

Counted (line 4):
- `quote`: "Females had positive phototaxis to 13 monochromatic light with wavelengths ranging from 365 to 630 nm, and the phototactic response rate decreases gradually with the increase in wavelength." (27 tokens; the comma before "and" was returned at a chunk boundary, check it on the page)
- `value`: "females showed positive phototaxis at all 13 monochromatic lights tested, 365 to 630 nm, with response falling as wavelength increased (88.33% at 365 nm down to 30.00%)"
- `conditions`: "50 lux per spectrum (equal lux, not equal photon flux); 10 females per group, 6 replicates; insects not reused; 20 min exposure after 2 h dark adaptation"

Counted (line 5):
- `conditions`: "10 adults of one sex per replicate; LEDs at 180 lx except 365, 420 and 435 nm, which reached only 24, 144 and 36 lx at the chamber centre; trap rates read after 120 min; five time slots across day and night (9:00-11:00, 14:00-16:00, 19:00-21:00, 0:00-2:00, 5:00-7:00)"
- `note`: replace "Equal lx across wavelengths, not equal photon flux." with "Illuminance was not equal: the two top wavelengths ran dimmer (144 and 36 lx) than most others (180 lx). The paper says 14 LEDs but lists 13 wavelengths and mentions 455 nm in the results."

Counted (line 6):
- `value`: "in females, no significant difference in trapping rate between light intensities at 435 nm and at 595 nm (120 min reading)"
- `conditions`: "females only; intensity series at 420, 435, 560 and 595 nm (at 560 nm: 45, 90, 180, 360 and 720 lx); trap rate read after 120 min"
- `note`: add "Exceptions in the same section: at 420 nm, 36 lx drew fewer females than the other intensities at 15, 30, 45 and 90 min; at 560 nm, 90 and 180 lx drew more females than 45, 360 and 720 lx at 15 and 30 min."

Counted (line 7):
- `value`: "robust positive phototaxis to blue light (both sexes, p < 0.001); no beetle entered the near-light area under yellow, which the authors read as a possible negative phototaxis"
- `conditions`: "adult beetles; LEDs blue 463-469, green 516-525, yellow 586-596, red 625-645 nm, each set to 200 lux at the start point 25 cm from the source; group sizes not given in the text read except 5 males under green"

Counted (line 8):
- `value`: "electroretinogram responses to blue and green (both sexes) and to yellow (males) significantly above red; yellow responses highly variable; no male-female difference"
- `conditions`: "six individuals; stimuli blue 463-469, green 516-525, yellow 586-596, red 625-645 nm, each pre-adjusted to 100 lux (equal illuminance, not equal photon flux); each wavelength three times, 30 s apart"

Counted (line 9):
- `conditions`: "n = 4 octopuses (600 +/- 50 g), Bay of Naples, June to October 2018; the same four animals ran every task, five trial days per task; food-preference test and T1 always first, T2 to T5 in random order; task T2 excluded chemical cues"
- `note`: replace "Four animals (whether the same animals ran every task was not checked)." and "Chance level of the T2 design not checked." with "The paper gives no number of jars per trial and no chance level, so 50% cannot be placed against chance from the text; the Results call T2 'a significant decrease in recognition' without a task-level statistic. Fixed order of the first two tests and reuse of the four animals across tasks allow order effects."

Line 10: retract; do not merge. If the owner wants the main row improved, its quote can take the full abstract sentence and its note "88.9% vs. 11.1% of successful first-opening decisions, pooled over T1 to T5; Wilcoxon matched-pairs in the Results, Friedman in the Abstract; n = 4".

Uncounted:
- Line 3 `conditions`: add "insects not reused; 20 min exposure after 2 h dark adaptation".
- Lines 3, 4 `family`: "Scarabaeidae" (GBIF backbone mirror; main has no Melolonthidae rows), with "Melolonthidae as printed" in the note.
- Lines 1, 2, 7, 8: the notes' "accepted status not checked" stays true after this audit; keep it.

## Unverifiable

- Asiophrida xanthospilota (lines 1, 2) and Endebius florensis (lines 7, 8): no authority page reachable here gave the species' status (GBIF API permission not answered, BioLib robot check). Exolontha castanea (lines 3, 4) is in the GBIF backbone mirror and Wikipedia's genus list but without a status shown.
- Endebius paper: the tool reported the page ended mid-sentence in Section 3.3, so later results and any reuse or presentation-order statement for the behavioural assays were not seen.

## Owner questions

1. Lines 1, 2 and 8 file ERG amplitudes at a few broad colours, with no nm values and no hue-discrimination test, as colour_vision. Main is mixed (four ERG rows under colour_vision, eleven under spectral_range_nm). Should relative ERG response across colours go under spectral_range_nm (the span responded to), with colour_vision kept for discrimination evidence?
2. Lux-matched stimuli recur in this unit (lines 1, 3 to 8). Should records with lux-matched stimuli always say so in `conditions`, given that it reverses or inflates short-wavelength rankings, or only when the record ranks wavelengths?
3. Line 10 repeats main's sea-invertebrates:119, whose quote is cut mid-parenthesis without a mark ("(88.9%, Friedman test"). Should that main row be requoted from this unit's whole sentence by a fix file, rather than a second row filed?
4. The Asiophrida paper also reports positive phototaxis to all five lights with blue strongest (Abstract), and Shang et al. report male negative phototaxis at six wavelengths that the Discussion contradicts. Should the next unit file the Asiophrida phototaxis result (behaviour_vision) as a lead?

Progress note: accurate on sources, DOIs and licences, and its "joined from parts" quotes all MATCH as printed; its "Green turtle hatchlings ... already on main" and the other held-out items were not checked here. It is wrong that the Anoplophora lamps were held at equal lux, and it did not see that line 10 was already on main.

Verdict: 9 errors in 10 (90%), above the 5% bar; pooled 41.5%. Error lines: 1, 2, 4, 5, 6, 7, 8, 9, 10. Unfixable: line 10 (duplicate). Lines 1, 2, 4 to 9 can merge with the counted text; line 3 as it stands or with the uncounted fix.

This report is model output and carries no authority.
