# audit-310: desk-d223, evidence lines 1 to 7

Audited 31 October 2026 from the desk-d223 files present untracked in the worktree (docs/tracks/progress/desk-d223.md and docs/views/evidence/desk-d223.jsonl, 14 lines; neither committed here, neither edited). HEAD 003964c1 (desk-d222). This audit judges lines 1 to 7 only; audit 311 judges lines 8 to 14. `tools/senses/check.py` on the evidence file: 14 records, 0 problems. Quote lengths (`len(q.split())`) for lines 1 to 7: 29, 16, 7, 12, 23, 20, 18, all within 40. The unit has evidence records only, so the brief's search-record and plant-screening parts do not apply; audits 308 and 309 are the format model.

Sources opened (WebFetch): journals.plos.org article pages for e0146677 (two passes), e0053120 (three passes), e0036207, e0189228 (two passes), e0245165 (two passes), plosntds e0012787; api.crossref.org/works for the six DOIs; reptile-database.reptarium.cz/Gekko/subpalmatus, gbif.org/species/7858460 and gbif.org/species/5981223 (all returned by my WebSearch). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 3 WebSearch and 17 WebFetch calls used.

## Bibliographic and licence

- Line 1, Chen et al. 2016, Crossref: Jingfeng Chen, Teppei Jono, Jianguo Cui, Xizi Yue, Yezhong Tang, in the recorded order; title verbatim; PLOS ONE 11(1), e0146677, issued 2016-01-11; licence CC BY 4.0, content-version vor; relation empty. Page: "Chen J, Jono T, Cui J, Yue X, Tang Y (2016)" and "distributed under the terms of the Creative Commons Attribution License". Met.
- Lines 2 and 3, Otálora-Luna et al. 2013, Crossref: Fernando Otálora-Luna, Stephen L. Lapointe, Joseph C. Dickens; title verbatim; PLoS ONE 8(1), e53120, issued 2013-01-16; CC BY 4.0, content-version unspecified; relation empty. Page: "Otálora-Luna F, Lapointe SL, Dickens JC (2013)" and "This is an open-access article distributed under the terms of the Creative Commons Attribution License". Met.
- Line 4, Pacheco-Tucuch et al. 2012, Crossref: Freddy Santiago Pacheco-Tucuch, Maria Jesus Ramirez-Sierra, Sébastien Gourbière, Eric Dumonteil; title verbatim; PLoS ONE 7(4), e36207, issued 2012-04-27; CC BY 4.0, unspecified; relation empty. Page citation and Creative Commons Attribution License statement as above. Met.
- Line 5, Paris et al. 2017, Crossref: Thomson M. Paris, Sandra A. Allan, Bradley J. Udell, Philip A. Stansly; title verbatim; PLOS ONE 12(12), e0189228, issued 2017-12-13; CC0 1.0, vor. Page: "made available under the Creative Commons CC0 public domain dedication" (tool summary of a long sentence). Met.
- Line 6, Park and Lee 2021, Crossref: Young-gyun Park, Joon-Ho Lee; title verbatim; PLOS ONE 16(1), e0245165, issued 2021-01-07; CC BY 4.0, vor. Page licence statement as above. Met.
- Line 7, Bezerra-Santos et al. 2024, Crossref: nine authors in the recorded order (Marcos Antonio Bezerra-Santos ... Petr Volf, Domenico Otranto); title verbatim; PLOS Neglected Tropical Diseases 18(12), e0012787, issued 2024-12-30; CC BY 4.0, vor. Crossref relation carries a "new_version" entry pointing to the same DOI; the page shows "Version 2" beside "Version 1 Uncorrected Proof" and no correction notice (tool summary), so the record reads the current version. Page licence statement as above. Met.

Licence ruling asked by the unit: a Crossref licence with content-version "unspecified" plus a Creative Commons Attribution License statement printed on the publisher's own article page (the version of record, the exact copy read) is acceptable. The page statement on the copy read is sufficient by itself under the audits 307/308 rule; Crossref "unspecified" agrees and does not undercut it. Ruled acceptable for lines 2, 3 and 4. Lines 1, 6 and 7 have both page statement and Crossref vor; line 5 has CC0 on both.

Bibliographic faults 0; licence faults 0. source.access "open" right on all seven.

## Names

- Gekko subpalmatus: Reptile Database prints "Gekko subpalmatus (GÜNTHER, 1864)", "Gekkonidae, Gekkota, Sauria, Squamata". Main's Gekko rows (G. gecko, G. japonicus, gbif-names.tsv) are Gekkonidae. Accepted, family right.
- Diaprepes abbreviatus: GBIF 7858460 (Curculio abbreviatus) places the name under Diaprepes abbreviatus, Curculionidae, Coleoptera. Accepted, family right; main has 36 Curculionidae rows and no Diaprepes.
- Triatoma dimidiata: GBIF species 8444055 "Triatoma dimidiata (Latreille, 1811)" returned by WebSearch; main's Triatoma rows (T. infestans, T. rubida) are Reduviidae. Accepted.
- Diaphorina citri: main gbif-names.tsv "Diaphorina citri EXACT ACCEPTED", and main's desk-d200 rows use Liviidae. Accepted, family right.
- Nesidiocoris tenuis: Plazi treatment "Nesidiocoris tenuis (Reuter, 1895)" returned by WebSearch (original combination Cyrtopeltis tenuis); Miridae as in the paper's title. Accepted.
- Phlebotomus perniciosus: GBIF 5981223 family Psychodidae, order Diptera; main's Lutzomyia longipalpis row (audit/corrected/methods.jsonl:706) is also Psychodidae. Accepted.

Name faults 0.

## Duplicates

git grep on origin/main across the whole docs/ tree (evidence, audit/corrected, audit/ALL.jsonl, searched, sheets, gaps, codex-findings, progress notes, desk-queue) for "Gekko", "subpalmatus", "pone.0146677", "Diaprepes", "pone.0053120", "Otálora|Otalora", "Triatoma", "pone.0036207", "Diaphorina", "pone.0189228", "Nesidiocoris", "pone.0245165", "Phlebotomus", "perniciosus", "pntd.0012787".

- None of the six DOIs is on main. No row for Gekko subpalmatus, Diaprepes, Triatoma dimidiata or Phlebotomus on main under any trait. "Otálora" hits on main are other authors (Bano-Otalora, desk-d200 tick rows), not this paper.
- Diaphorina citri on main: desk-d200.jsonl:1 to 3 (Insects 8(3): 88, behaviour_vision UV/blue phototaxis and two polarization rows) and oa-4.jsonl:700 (a Vespinae paper's introduction, grade g). Different source and different finding (UV added to green or yellow broadband targets); line 5's note says so. Not a repeat and no contradiction.
- Nesidiocoris tenuis on main only in searched/sweep-46.jsonl (opsin genes, no LED behaviour) and sweep-101.jsonl. Not a repeat.
- Lines 2 and 3 share a source but log different results (odour attraction lost under green light; red preferred over green in still air). Not duplicates of each other.

Duplicates 0; contradictions 0.

## Per-record findings

### Line 1, Gekko subpalmatus, sense_hearing, ABR thresholds about 40 dB SPL at 1.0 to 3.5 kHz

Results sentence is 143 characters. The fetch returned its first part verbatim, "ABR thresholds were lower from 1.0 to 3.5 kHz (~40 dB SPL) than at both higher (4 kHz, ~45 dB SPL) and", and on a second pass its last 100 characters verbatim, "Hz (~40 dB SPL) than at both higher (4 kHz, ~45 dB SPL) and lower frequencies (0.8 kHz, ~46 dB SPL)." The two overlap, so the reassembly is complete and carries no trailing figure reference (the Fig 4 reference sits on the preceding F-test sentence, "(F12, 132 = 91.091, p < 0.001; Fig 4)."). MATCH, whole sentence, 29 words. The value says no more than the quote. Grade m right. Other carried items verified: 12 geckos (seven males, five females); "Thresholds increased significantly above 4.0 kHz ..." and the ~0.4 kHz, ~42 dB SPL band; 5 dB steps from 70 to 30 dB SPL; noise floor not reported (tool summary: none found).

**Error (origin, temperature and threshold criterion omitted).** (a) The geckos were "collected in urban areas" of Chengdu, Sichuan, and held in captivity at least two weeks before testing (tool summary); the record does not say they were wild-caught adults kept captive. (b) The page prints "ambient temperature was controlled at 27 ± 1 oC with an electrical heater"; temperature affects ectotherm ABR thresholds and latencies and is absent. (c) The threshold criterion, verbatim "Thresholds were defined as the lowest stimulus level at which a repeatable response could be recognized.", is a visual criterion with 5 dB resolution and is not carried. Fixable. Uncounted: the record says the values are "read from the Fig 4 curve"; the Results text prints the approximate values itself, so "as printed (approximate, ~) in the Results" is truer; the paper states "there are no sex differences in the ABR thresholds and latencies" and pooled the sexes (no test given); 400 sweeps averaged at 4/s.

Line 1: 1 record in error.

### Line 2, Diaprepes abbreviatus, behaviour_vision, odour attraction disappeared under green light

Abstract, verbatim: "However, the attractiveness of citrus + conspecific odors disappeared in the presence of a green light." Returned whole, 105 characters. MATCH, 16 words; value adds "(570 nm peak)", which Methods print ("Peak wavelengths tested occurred at 351 (ultraviolet), 472 (blue), 570 (green), 585 (yellow) and 660 nm (red)"). Grade m right.

**Error (light geometry and the direction of the response omitted; intensity and temperature omitted).** (a) In this series the green LEDs were placed at right angles to the odour stream (Fig 4 caption, verbatim "Green LEDs were perpendicular to the air stream and blue LEDs were parallel to the air stream") and the weevils "walked a greater distance crosswind (90° and 270° relative to the airflow) toward the green LEDs" (Wilcoxon signed rank, P<0.001, tool summary for the statistic). "Disappeared" therefore means the walk was redirected toward a competing light, not that odour response was abolished; the record's method says only "against a green LED" and never says the weevils walked toward it. (b) Because of (a), the conditions sentence that green light "elicited less attraction than darkness or dim green light", which comes from the still-air colour series (group 1), misleads when attached to this record: in the odour series the green light was what the weevils walked to. (c) Each standard LED emitted "approximately 1.55×10¹⁷ photons m⁻² s⁻¹" and tests ran "in a dark room at 25±0.5°C and 40±10% RH"; neither is carried, and the page does not state that intensity was matched across colours beyond that single approximate value. (d) Each odour test was compared with the same insect's preceding 2-min air-only control period; not stated. Fixable.

Line 2: 1 record in error.

### Line 3, Diaprepes abbreviatus, behaviour_vision, red preferred over green

Results, verbatim: "However, weevils preferred red over green (*P*<0.001)." No trailing figure reference (checked). MATCH, whole sentence, 7 words. The record correctly says no test is named in that sentence; the paragraph's tests are Wilcoxon paired tests. Red versus dark (P = 0.477), green versus dark (dark preferred, P<0.01) and dim versus bright green (P<0.001) are carried and verified. Grade m right.

**Error (light intensity, temperature and the rest of the colour series omitted).** (a) Standard LEDs emitted approximately 1.55×10¹⁷ photons m⁻² s⁻¹ each, intensity "regulated with a stimulator device" and measured with a spectrometer, bandwidths 50 to 90 nm; the record gives only the dim green flux, so a reader cannot tell that red and green were nominally equal in photon flux, nor that the page does not otherwise state intensity matching. (b) "in a dark room at 25±0.5°C and 40±10% RH", still air, LEDs the only visible light; temperature absent. (c) The same paragraph reports green preferred over blue (P<0.001) and over UV (P<0.001) and no preference between green and yellow (P = 0.693); without these the red-over-green result reads as a general long-wavelength preference, whereas the series shows green beating shorter wavelengths, red and darkness beating bright green, and dim green beating bright green, which points to avoidance of bright green rather than attraction to red. (d) The Methods give the colour-choice recording as "recorded for 3 min" while the test period is stated as two minutes (tool summary); the record's "two-minute tests" should note the conflict. Fixable.

Line 3: 1 record in error.

### Line 4, Triatoma dimidiata, behaviour_vision, attraction decreased with increasing wavelength

Abstract, verbatim: "Attraction was also dependent on light color and decreased with increasing wavelength." MATCH, whole sentence, 12 words. Carried items verified: wavelengths white (∼400 to 750 nm), blue 430, green 500, yellow 590, red 630 (Results 625); 5 to 30 individuals per experiment; starved 10 to 25 days; "Room temperature was kept at 24±2°C."; light position switched each experiment; no-light controls; no sex difference; nymph white-light P = 0.21; "Thus, yellow light was barely attractive while red light was not attractive at all."; green not reported in the text. Grade m right.

**Error (field versus laboratory origin and the scoring omitted).** (a) The page prints "Field-collected and first-laboratory generation insects were kept under natural photoperiod"; the record does not say the bugs were a mix of field-collected and first laboratory generation insects. (b) The attraction index is (T−C)/(T+C+O), with insects staying outside both tunnels (O) in the denominator, tested by χ2 against no-light controls (tool summary of a formula and a long sentence); not carried, so "attraction" in the value has no stated measure. (c) The record says "intensity held constant per the Discussion"; Methods report no LED intensity and no measurement (tool summary), so it should say intensity was neither reported nor measured in Methods and is described as constant only in the Discussion. Fixable.

Line 4: 1 record in error.

### Line 5, Diaphorina citri, behaviour_vision, UV enhanced attraction to green or yellow targets

Abstract sentence of 140 characters; fetch returned first 100 verbatim "The addition of ultra-violet light (< 400 nm) enhanced attraction of D. citri to transparent visual" and last 100 verbatim "0 nm) enhanced attraction of D. citri to transparent visual targets made of green or yellow filters." Overlap complete. MATCH, whole sentence, 23 words. Next sentence verbatim "However, attraction to blue targets was unaffected by UV light." (carried). Carried items verified: 37.9 ± 0.60 psyllids per test, 14 replicates, 15 min dark adaptation, sexes pooled, positional bias test t = -0.66, df = 26, P = 0.52; UV blocker "reduced overall light intensity by 19%, with a 9% reduction between 400 and 700 nm"; yellow versus green with UV blocked t = -0.89, P = 0.38. Grade m right.

**Error (the design behind "enhanced" omitted; colony and lamp omitted).** (a) No trial offered the same colour with and without UV. The record's method ("each with and without a UV-blocking filter") implies such pairs. The enhancement is inferred across pairs: green plus UV beat yellow with UV blocked (t = 12.16, df = 26, P < 0.0001), yellow beat green when both had UV (t = -4.00, df = 26, P < 0.0001), the two were equal when UV was blocked from both, and yellow with UV blocked lost to dimmer neutral-density yellow (t = 10.89 and t = 24.39). The text gives yellow with UV as about 1.5 times more attractive than yellow without UV by comparison across figures (tool summary). (b) Insects came from a laboratory colony on Murraya paniculata in a greenhouse at 29 ± 3 °C, of mixed ages; the light was a 400 W metal halide lamp giving "ca. 2000 lux" (tool summary); assay temperature is not reported. None of this is carried. Fixable.

Line 5: 1 record in error.

### Line 6, Nesidiocoris tenuis, behaviour_vision, highest attraction at 385 nm (73.5%)

Results, verbatim: "The attraction rate of N. tenuis was the highest at 385 nm wavelength (73.5%), followed by 365 nm wavelength (62.6%)." Returned whole, 117 characters. MATCH, 20 words. Carried items verified: commercial adults (Osang Kinsect System), about 30 per replicate, five replicates, one hour at 25 °C; sex, age and starvation not reported; intensity not reported, arm switching not reported; attraction rate divided by number released with central-chamber non-responders; "Attraction rates of N. tenuis to control LED light were >50% at wavelengths of 495, 525, and 595 nm."; Methods 590 versus 595 nm discrepancy; ANOVA F values. Units fit. Grade m right (B. tabaci kept out).

PASS. Uncounted: room lighting is not stated (arms were capped against outside light, tool summary); the Discussion reports that Uehara et al. found preferences "in the 385 to 405 nm wavelengths" with a multiple-choice design "while we use a single choice test against control design", which could be added as context; the Discussion, not only the Results, gives 595 nm.

### Line 7, Phlebotomus perniciosus, sense_chemical, attraction index 0.53 nonanal to -0.47 p-cymene

Abstract, verbatim: "The attraction indexes varied from 0.53 for nonanal (i.e., most attractive) to -0.47 to p-cymene (i.e., most repellent)." Returned whole, 120 characters. MATCH, 18 words, wording kept. Carried items verified: females 6 to 12 days, sugar-starved 24 to 48 h, 30 choosing females per compound, non-choosers excluded, apparatus rotated 180°, Yates-corrected χ² nonanal 8.53, myrcene 4.80, p-cymene 6.53, unresponsive 14.3% to 40.0%, ultra-pure air control arm. Grade m right.

**Error (null results and origin omitted).** (a) Eleven of the 14 compounds tested in the Y-tube (acetic acid, nonanoic acid, 2-propanol, 2-butanol, pentanal, hexanal, trans-2-nonenal, decanal, verbenone, 2-ethyl-1-hexanol, acetonitrile) gave no significant choice despite EAG activity, and pentanal increased time in the treated arm (p = 0.0030) without a significant choice (tool summary). The record gives only the range ends and the three significant compounds, so a reader cannot tell most EAG-active compounds were behaviourally null. (b) Flies were reared in the laboratory at the University of Bari (colony and generations not named), tested under a 35 W red light 60 cm above the olfactometer, with 2.5 μL of a 100 μg/μL mineral-oil stock per trial and no reported temperature (tool summary); none is carried. Fixable.

Line 7: 1 record in error.

## Trait key

- Lines 2, 3, 4, 5, 6, behaviour_vision: fit (walking or flight orientation of whole living insects to lights). Line 2 is a light-by-odour interaction; behaviour_vision fits because the measured change is orientation toward the light; sense_chemical would also be defensible but is not required.
- Line 1, sense_hearing: fits (ABR thresholds of one named species).
- Line 7, sense_chemical: fits (living females' Y-tube responses to single host volatiles).

Trait key faults 0.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Gekko subpalmatus, sense_hearing, ABR ~40 dB SPL 1.0-3.5 kHz | error, fixable | conditions | Quote MATCH (reassembly verified, 29 words); wild-collected captive origin, 27 °C recording temperature and visual repeatable-response threshold criterion omitted |
| 2 | Diaprepes abbreviatus, behaviour_vision, odour attraction lost under green | error, fixable | method, conditions | Quote MATCH; omits that green LEDs were perpendicular to the air stream and weevils walked crosswind toward them; Discussion sentence misapplied; intensity and 25 °C omitted |
| 3 | Diaprepes abbreviatus, behaviour_vision, red over green | error, fixable | conditions | Quote MATCH; standard LED photon flux, 25 °C and the green-over-blue/UV and green-equals-yellow results omitted; 2 vs 3 min conflict |
| 4 | Triatoma dimidiata, behaviour_vision, attraction falls with wavelength | error, fixable | conditions | Quote MATCH; field-collected plus first-lab-generation origin and the attraction-index scoring omitted; intensity overstated as held constant |
| 5 | Diaphorina citri, behaviour_vision, UV enhances green/yellow | error, fixable | method, conditions | Quote MATCH (reassembly verified); no same-colour UV versus UV-blocked pairing, enhancement inferred across pairs; lab colony, lamp and missing assay temperature omitted |
| 6 | Nesidiocoris tenuis, behaviour_vision, 385 nm 73.5% | pass | | Quote MATCH; design gaps (intensity, sex, side switching) already stated |
| 7 | Phlebotomus perniciosus, sense_chemical, AI 0.53 to -0.47 | error, fixable | conditions | Quote MATCH; 11 of 14 compounds behaviourally null and lab origin, red light, dose omitted |

6 of 7 records in error (85.7%): scientific-context 6 (lines 1, 2, 3, 4, 5, 7); quote-form 0; value beyond quote 0; duplicates 0; bibliographic 0; names 0; licence 0; trait key 0; grading 0.

Pooled with audits 172 to 309: 342 of 746 evidence records (45.8%; 336 of 739 before this audit, 6 of 7 here). Audit 311's lines 8 to 14 are not included. No search records.

## Replacement text

Line 1:
- `conditions`: replace "12 geckos (7 males, 5 females) were used for the hearing tests (Methods, paraphrased from page summary);" with "12 geckos (7 males, 5 females) were used for the hearing tests, collected in urban areas of Chengdu, Sichuan and held captive at least two weeks before testing; sexes pooled after the authors found no sex difference (no test given) (Methods, paraphrased from page summary); recording temperature 27 ± 1 C; threshold criterion 'the lowest stimulus level at which a repeatable response could be recognized', a visual criterion at 5 dB resolution;".
- `conditions` (uncounted): replace "thresholds are read from the Fig 4 curve as approximate values (~)" with "thresholds are as printed (approximate, ~) in the Results text and shown in Fig 4".

Line 2:
- `method`: replace "olfactory series with citrus host odour plus conspecifics against a green LED" with "multimodal series: citrus host odour plus conspecifics carried in an air stream over the weevil from 0 degrees, with green LEDs perpendicular to the air stream; each insect's 2-min test period compared with its preceding 2-min air-only control period".
- `conditions`: replace "the Discussion says green light elicited less attraction than darkness or dim green light, so the loss of odour attraction was tested against a light that is itself less attractive than darkness (paraphrase of a Discussion sentence of 125 characters or fewer)" with "under odour plus green light the weevils walked a greater distance crosswind (90 and 270 degrees to the airflow) toward the green LEDs (Wilcoxon signed rank, P<0.001), so the odour response was redirected toward a competing light rather than abolished; standard LEDs emitted approximately 1.55e17 photons m-2 s-1 each and the page does not otherwise state that intensity was matched across colours; tests in a dark room at 25 +/- 0.5 C and 40 +/- 10% RH".

Line 3:
- `conditions`: append "; standard LEDs emitted approximately 1.55e17 photons m-2 s-1 each (regulated with a stimulator, measured with a spectrometer, bandwidths 50 to 90 nm), so red and green were nominally equal in photon flux; tests in still air in a dark room at 25 +/- 0.5 C, LEDs the only visible light; the same paragraph reports green preferred over blue (P<0.001) and over UV (P<0.001) and no preference between green and yellow (P = 0.693), so red-over-green, with red equal to darkness and darkness and dim green preferred to bright green, points to avoidance of bright green rather than attraction to red; Methods give the colour-choice recording as 3 min while the test period is stated as two minutes".

Line 4:
- `conditions`: replace "adult males and females and fifth-stage nymphs," with "adult males and females and fifth-stage nymphs, field-collected and first laboratory generation insects,".
- `conditions`: replace "intensity held constant per the Discussion" with "Methods report no LED intensity or measurement and only the Discussion describes a constant intensity; attraction was scored as an index (T - C)/(T + C + O), with insects staying outside both tunnels (O) in the denominator, and tested by chi-square against no-light controls".

Line 5:
- `method`: replace "two-choice bioassay of attraction to light transmitted through clear, yellow, green and blue filters, each with and without a UV-blocking filter;" with "two-choice bioassays pairing targets of clear, yellow, green and blue filters with or without a UV-blocking filter, under a 400 W metal halide lamp (about 2000 lux); no trial paired the same colour with and without UV;".
- `conditions`: append "; the UV enhancement is inferred across pairs: green plus UV beat yellow with UV blocked (t = 12.16, df = 26, P < 0.0001), yellow beat green when both had UV (t = -4.00, df = 26, P < 0.0001), the two were equal when UV was blocked from both, and yellow with UV blocked lost to dimmer neutral-density yellow (t = 10.89 and 24.39); laboratory colony on Murraya paniculata (greenhouse 29 +/- 3 C), mixed ages; assay temperature not reported".

Line 6: none required. Optional (uncounted): append to `conditions` "; room lighting not stated (arms capped against outside light); the Discussion notes Uehara et al. found preferences in the 385 to 405 nm range with a multiple-choice design, against this paper's single choice test against a control".

Line 7:
- `conditions`: append "; 11 of the 14 compounds tested in the Y-tube (acetic acid, nonanoic acid, 2-propanol, 2-butanol, pentanal, hexanal, trans-2-nonenal, decanal, verbenone, 2-ethyl-1-hexanol, acetonitrile) gave no significant choice despite EAG activity, and pentanal increased time in the treated arm (p = 0.0030) without a significant choice; flies were laboratory-reared at the University of Bari (colony and generations not named), tested under a 35 W red light 60 cm above the olfactometer with 2.5 uL of a 100 ug/uL mineral-oil stock per trial; temperature not reported".

## Owner questions (the unit's, answered for lines 1 to 7)

1. Crossref licence content-version "unspecified" with a page-printed "Creative Commons Attribution License": acceptable, ruled per record above (lines 2, 3, 4 accepted; lines 1, 6, 7 carry vor as well; line 5 CC0 on both). The page statement on the version of record read is the basis; Crossref agrees.
2. Gnorimus nobilis, Anopheles strain and Chiloscyllium threshold questions concern lines 8 to 14 and are left to audit 311.

## Progress note

Accurate on citations, licences, names and duplicates, and the Diaphorina note correctly separates this DOI from main's Insects 8(3): 88 rows. The Records list does not carry the faults above: the Diaprepes odour record is listed as attraction "lost" without the perpendicular green LEDs the weevils walked toward, the Diaphorina record as UV "added" although no same-colour UV pairing was run, and the Phlebotomus record without the eleven null compounds.

Verdict: 6 of 7 judged records in error (85.7%), above the 5% bar. Error lines: 1, 2, 3, 4, 5 and 7, all fixable with the replacement text above. Line 6 passes. Pooled 342 of 746 (45.8%).

This report is model output and carries no authority.
