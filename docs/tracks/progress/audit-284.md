# audit-284: desk-d200 (6 evidence records, no search records, no wanted lines)

Audited 31 October 2026 from the desk-d200 files present untracked in the worktree (docs/tracks/progress/desk-d200.md and 6 evidence lines in docs/views/evidence/desk-d200.jsonl; neither committed here, neither edited). HEAD 5f043b24 equals origin/main. `tools/senses/check.py` on the evidence file: 6 records, 0 problems. Quote lengths (`len(q.split())`): 17, 19, 15, 20, 20, 21, all within 40. No searched or wanted file, so all six records were judged whole. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md and BRIEF (whole sentence, 40 words, grade, `partial`), desk-audit.md (no 125-character limit), the BRIEF trait table (`polarization`: "polarization sensitivity, where in the eye, what for"; `sense_thermal`, `sense_magnetic` under "other senses"; `behaviour_vision`: "a behaviour that shows what is seen (... colour choice)"), the publisher-copy licence rule and the name rule, in the form of audits 270 to 283. Duplicates checked with git grep on origin/main across docs/views (evidence, audit including corrected/ and ALL.jsonl, searched, wanted, gaps) and views/ for the four binomials, the three DOI suffixes and the first-author strings. 1 WebSearch and 10 WebFetch calls used.

Sources opened: api.crossref.org/works/10.3390/INSECTS8030088, /10.3390/INSECTS13020130, /10.3390/ANI10030489 (uppercase answered each time); the record URLs www.mdpi.com/2075-4450/8/3/88 (three passes), www.mdpi.com/2075-4450/13/2/130 (two passes), www.mdpi.com/2076-2615/10/3/489 (two passes); biodiversity.org.au/afd/taxa/Pogona_vitticeps (from my WebSearch). reptile-database.reptarium.cz returned PROVENANCE_REQUIRED (permission not answered) and was not retried. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries, so quotes were checked as MATCH/MISMATCH; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification.

## Bibliographic and licence

- Paris et al. 2017, fresh Crossref: Thomson Paris, Sandra Allan, Bradley Udell, Philip Stansly, in the recorded order; title as recorded; Insects 8, issue 3, page 88; issued and online 2017-08-19; CC BY 4.0 (vor, from 2017-08-19); relation empty; no update-to. Page: "Open Access" marker, meta dc.rights CC BY 3.0, no copyright line returned (tool summary). Licence rests on Crossref vor on the publisher's own copy, as the note says; prior audits (270, 273, 277, 278) did not count the 4.0/3.0 split. Met.
- Otálora-Luna et al. 2022, fresh Crossref: Fernando Otálora-Luna, Joseph C. Dickens, Jory Brinkerhoff, Andrew Y. Li, in the recorded order; title as recorded, "Ambylomma" as printed (harmless, reassessment 158-159); Insects 13, issue 2, page 130; issued 2022-01-26; CC BY 4.0 (vor, delay 0); relation empty; no update-to. Page: "Open Access" badge, meta dc.rights CC BY 3.0, no copyright line in the body (tool summary). Met, as for Paris.
- Nishimura 2020, fresh Crossref: Tsutomu Nishimura, sole author; title as recorded; Animals 10, issue 3, 489; issued 2020-03-15; CC BY 4.0 (vor); relation empty; no update-to. Page footer: "© 2020 by the author. Licensee MDPI, Basel, Switzerland." and "This article is an open access article distributed under the terms and conditions of the Creative Commons" (fragment), linked to CC BY 4.0; meta dc.rights CC BY 3.0. Met.

Bibliographic faults 0; licence faults 0.

## Names

- Diaphorina citri: gbif-names.tsv "Diaphorina citri EXACT ACCEPTED ... 2013312". Accepted.
- Amblyomma americanum: gbif-names.tsv "EXACT ACCEPTED ... 2184301". Accepted.
- Ixodes scapularis: gbif-names.tsv "EXACT ACCEPTED ... 2182727". Accepted.
- Pogona vitticeps: no gbif-names.tsv row. Main's data/everyday/log.txt logs "Pogona vitticeps -> 2465641 Pogona vitticeps (SPECIES, ACCEPTED)"; the Australian Faunal Directory (opened) lists "Species Pogona vitticeps (Ahl, 1926)", original combination Amphibolurus vitticeps Ahl 1926, under Pogona. The Reptile Database page the note cites was blocked for me (not retried), so its "VALID" stays unverified here. Accepted; not counted.

Name faults 0.

## Duplicates

- Diaphorina citri on main: oa-4:700 (behaviour_vision, grade g, an Introduction sentence of Huang et al. 2024, Animals 14: 1543, on opsin knockdown). Different paper and finding; not a repeat, no contradiction.
- Amblyomma americanum on main: ground-invertebrates (corrected 150, 151, 160, 161, 163): eye_type, rhabdom_um, sense_infrared twice (Carr and Salgado 2019, 10.1371/journal.pone.0221659, heat plate at 37 to 40 °C detected from 1 m), sense_chemical (Holscher et al. 1980). No Otálora-Luna row. Not a repeat; Carr and Salgado agree with line 4 in direction. Uncounted: the note's "main has no thermal record for either tick" overlooks the Carr and Salgado sense_infrared rows, which are heat detection by this species (the Otálora-Luna Discussion cites the same plate study in the sentence before the quote).
- Ixodes scapularis on main: ground-invertebrates corrected 165 and views/tick.json (sense_chemical, Josek et al. 2020). No thermal row. Not a repeat.
- Pogona vitticeps on main: gaps cells and queue rows only (no evidence). Not a repeat.
- DOI suffixes insects8030088, insects13020130, ani10030489 and the strings Paris TM, Otálora/Otalora (only an unrelated Rhabdomys row), Nishimura (unrelated rows): absent as these papers.

Duplicates 0.

## Per-paper findings

### Paris et al. 2017, Diaphorina citri (lines 1 to 3)

Design (tool summary with verbatim fragments): 1 min horizontal walking assay; each experiment run "until at least 35 adult psyllids" were tested (Table 1 N = 35; no separate per-treatment count in text); bandpass-filtered transmitted light, neutral density filters between source and bandpass; direction against 50% by χ², distance by Kruskal-Wallis or ANOVA, t-tests for pairs. Wavelength: distance "significantly greater than darkness" for 350 to 430 nm; 500, 550, 580 and 620 nm "were not different from complete darkness", "Psyllids only walked an average of 0.10 cm towards the 500–620 nm targets"; H = 96.03, df 9, p < 0.001. Intensity: "Although light intensity increased with wavelength", "greatest responses were associated with the lowest light levels", and "This result indicated that positive phototaxis was in response to wavelength rather than intensity"; dimming white and 365 nm light to 10% and 1% reduced walking (Results speed, Discussion distance). Polarization: unpolarized stimulus balanced with 0.4 OD ND; 405 nm t = −2.63, df 70, p = 0.01; 500 nm t = −0.36, df 43, p = 0.72; vertical and horizontal pooled for lack of difference (Figure 4 caption); means only in Figure 4. Colour morph (p = 0.94) and sex (p = 0.30) no effect; age no effect at 405 nm, day-old psyllids walked farther at 500 nm (t = 2.02, df 92, p = 0.05).

Line 1. Counted (scientific context, causal interpretation; fixable). Quote MATCH (Abstract only, as the note says). The value and quote are right. The note lists as "Limits the authors state" that "intensity was not matched across wavelengths and wavelength and intensity are not fully separated", while the paper reports that intensity rose with wavelength, that the brighter long-wavelength targets drew no response above darkness, that dimming reduced the response, and concludes "positive phototaxis was in response to wavelength rather than intensity". The covariance runs against an intensity explanation, so describing it as an unresolved confound attributed to the authors reverses the causal reading the design supports (oa-audit.md: crossed factors described as confounded). The darkness comparison (UV/blue above darkness, 500 to 620 nm not) belongs in `conditions`.

Line 2. Confirm. Quote MATCH (Abstract; the Discussion paraphrases it). Value within the quote; method states the 0.4 OD compensation and the note says the matching rests on it. The df 70 inference is labelled as such. Uncounted: add t = −2.63, df 70, p = 0.01 and that vertical and horizontal were pooled.

Line 3. Confirm, with a flagged context addition (uncounted). Quote MATCH (Abstract). Value says no more than the quote; the note limits the null to the assay. Flag: in the same paper's wavelength assay 500 nm light did not differ from darkness (0.10 cm), so a polarized-versus-unpolarized null at 500 nm may sit on a weak or floor response; the 500 nm means in the polarization test are only in Figure 4, which I could not read, and the day-old 500 nm effect (p = 0.05, df 92) shows some response in some 500 nm test. Under oa-audit.md I do not infer the Figure 4 levels, so I leave it uncounted and suggest the addition below; the authors read the null as polarization from host surfaces not being a factor (tool summary).

Grade m right for all three; access open, `partial` absent, right (page read). Traits: `behaviour_vision` fits wavelength choice; `polarization` fits a behavioural test of polarization sensitivity.

### Otálora-Luna et al. 2022, Amblyomma americanum and Ixodes scapularis (lines 4 and 5)

Design (tool summary with verbatim fragments). Servosphere: infrared LED flashlight, peak 850 nm (880 nm also cited), front 5 cm from the tick, reaching about 41 °C; 20 females of each species, no males or nymphs; both species "oriented locomotion toward the IR lamp (p < 0.001)". The Peltier was used only on the flying T. Flying T: "We tested 30 females, 30 males and 30 nymphs of each species on the flying T"; 32 °C Peltier against one at "ambient temperature (24 ± 1 °C)", rotated every 10 ticks; binomial test with normal approximation; A. americanum females z = 2.01, p < 0.050; males z = 1.64, p < 0.010; nymphs z = 3.83, p < 0.001; I. scapularis females z = 0.55, p = 0.292; males z = 0.00, p = 0.572; nymphs z = 0.55, p = 0.292; counts per arm only in Figure 4; ambient-against-ambient control for A. americanum nymphs only (p = 0.181, z = 0.91). Discussion: "The Peltier element used here emitted both long-wavelength IR (~9 μm) and convective heat at 32 °C." and, for I. scapularis, that not being attracted on the flying T "does not mean that it cannot physiologically detect heat or will not behaviorally respond to it under other circumstances."

Shared sentence. Quote MATCH, Section 4 Discussion. Both records may use it: it names A. americanum as attracted and I. scapularis as not, and each value says no more than its half (line 4 "nymphs and adults of both sexes ... attracted"; line 5 "not attracted"). Quote-form 0.

Line 4. Counted (scientific context, design misstated; fixable). The note says "The Abstract adds that only this species was attracted to the Peltier element while climbing upward in the servosphere (20 females per species, open-loop)". The Peltier was never on the servosphere; the servosphere tested an IR LED, both species oriented to it, and only females (20 per species) were tested there; "climbing upward" is the flying T. The note thus invents a second, independent Peltier result for this species and hides that the species-specific difference appears on the flying T only. Uncounted flag (owner question 1): the printed male statistic "p < 0.010 males, z = 1.64" is internally inconsistent (z = 1.64 is about p = 0.10 two-tailed), so "both sexes" rests for males on a figure that does not check; `conditions` should print the z and p values.

Line 5. Counted (scientific context, contrary result omitted; fixable). The record files a sense_thermal null for I. scapularis and keeps the authors' disclaimer, but omits that in the same paper I. scapularis females oriented toward the warm (about 41 °C) IR LED on the servosphere (p < 0.001). That positive response is a direct exception limiting the null's applicability (oa-audit.md), and the disclaimer alone does not convey that the paper shows a heat or IR response by this species. The z and p values are also absent.

Grade m right for both; access open, `partial` absent, right. Trait `sense_thermal` acceptable: the stimulus is 32 °C with IR and convective heat unseparated, which both notes state (main files Carr and Salgado's plate under `sense_infrared`; owner question 2).

### Nishimura 2020, Pogona vitticeps (line 6)

Design (tool summary with verbatim fragments): Experiment 3 used eight adults (four males, four females) from Experiment 2, crossover ("the control group in the first instance became the EMF group in the second instance" is stated for Experiment 1; the tables label Experiment 2 crossover), a 6 mm SC-40 filter (cut below 380 nm) taped to the dorsal head over the parietal eye; "the whole body of lizards was exposed to an EMF for 5 days for 11 h/day (08:00 to 19:00)" (Experiment 2, Experiment 3 identical), 3-day baseline; tail lifts from images taken every minute; observer blinding not stated; control not exposed, no sham described; EMF parameters (6 and 8 Hz, 2.6 µT, 10 V/m) given in Abstract and Introduction from the earlier study, not restated in Methods. Results: increase −0.5 ± 7.1 against 3.7 ± 9.4, ratio 0.9 ± 0.3 against 1.9 ± 0.6, n = 8, p = 0.02 each; Wilcoxon signed-rank named for the increase, no test named for the ratio. Experiments 1 and 2 (580 nm filter): combined n = 16, p = 0.67 and 0.41. Abstract after the quote: "Therefore, the lizards appeared to respond to light of certain wavelengths rather than the filters themselves."

Line 6. Counted (scientific context, exposure scale misstated; fixable). Quote MATCH (Abstract). Value within the quote; the note carries the 580 nm null with the right p values and the E/M caveat, so keeping the null in the note is harmless (it does not limit the 380 nm result; it is its contrast). But `conditions` gives "about half a day of exposure", while the exposure was 11 h a day for 5 days after a 3-day baseline; this misstates the practical scale of the stimulus by about fivefold. Uncounted: add the effect sizes (ratio 1.9 against 0.9), no blinding stated, and that the EMF parameters come from the earlier study.

Grade m right; access open, `partial` absent, right. Trait `sense_magnetic` acceptable as the paper's own framing, with the note's caveat that electric and magnetic parts were not separated (owner question 3). `eye` "parietal eye" fits.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Diaphorina citri, walked farther to UV/blue | correct | note, conditions | Quote MATCH; note calls intensity an unresolved, author-stated confound, but brighter long wavelengths drew nothing and the authors conclude wavelength not intensity |
| 2 | Diaphorina citri, polarized > unpolarized at 405 nm | confirm | (conditions, uncounted) | Quote MATCH; ND compensation stated; t, df, p worth adding |
| 3 | Diaphorina citri, no polarization effect at 500 nm | confirm | (conditions, uncounted) | Quote MATCH; 500 nm alone not above darkness in the wavelength assay, worth adding; Figure 4 levels unseen |
| 4 | Amblyomma americanum, attracted to 32 °C Peltier | correct | note, conditions | Quote MATCH; note puts the Peltier on the servosphere (it was an IR LED that both species oriented to); male z = 1.64 with p < 0.010 inconsistent |
| 5 | Ixodes scapularis, not attracted to 32 °C Peltier | correct | value, conditions, note | Quote MATCH; omits that I. scapularis females oriented to the warm IR LED (p < 0.001) in the same paper |
| 6 | Pogona vitticeps, responded to ELF EMF with 380 nm filter | correct | conditions | Quote MATCH; exposure was 11 h/day for 5 days, not "about half a day" |

Evidence errors: 4 of 6 (66.7%): scientific-context faults 4 (lines 1, 4, 5, 6); quote-form 0; name 0; duplicates 0; licence 0; bibliographic 0; abstract-access grading 0. Unfixable records: none.

Pooled with audits 172 to 283: 262 of 612 evidence records (42.8%; audit 283's 258 of 606, and 4 of 6 here). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Counted (line 1):
- `conditions`: "Each adult tested once for 1 min in a horizontal walking arena; each experiment run until at least 35 adults were tested (Table 1 N = 35); target light transmitted through narrow bandpass filters, attenuated by neutral density filters, no absolute intensities given; distance toward 350 to 430 nm greater than darkness, 500 to 620 nm not different from darkness (about 0.10 cm); Kruskal-Wallis H = 96.03, df 9, p < 0.001; intensity rose with wavelength, so the dimmer UV/blue targets drew the larger response; colour morph and sex no effect"
- `note`: replace "Limits the authors state or the page shows (fetch summary, not quoted): intensity rose with wavelength and the strongest responses came at the lowest light levels, so intensity was not matched across wavelengths and wavelength and intensity are not fully separated;" with "Intensity was not matched across wavelengths, but it rose with wavelength and the brighter long-wavelength targets drew no response above darkness, while dimming white and 365 nm light reduced walking; the authors conclude phototaxis 'was in response to wavelength rather than intensity'. Limits (fetch summary):"; keep the rest.

Counted (line 4):
- `conditions`: append "binomial tests: females z = 2.01, p < 0.050; males printed as z = 1.64, p < 0.010 (inconsistent as printed: z = 1.64 is about p = 0.10 two-tailed); nymphs z = 3.83, p < 0.001; ambient-against-ambient control on nymphs p = 0.181"
- `note`: replace "The Abstract adds that only this species was attracted to the Peltier element while climbing upward in the servosphere (20 females per species, open-loop)." with "The Abstract adds that only this species was attracted to the Peltier element while climbing upward on the flying T; on the servosphere (an infrared LED, front about 41 °C at 5 cm, 20 females per species) both species oriented toward the lamp (p < 0.001)."; replace "main has no thermal record for either tick" with "main's Amblyomma americanum sense_infrared rows (Carr and Salgado 2019, heated plate) are a different paper".

Counted (line 5):
- `value`: "not attracted to a 32 °C Peltier element in a flying T choice test (females, males and nymphs), although females oriented toward a warm infrared LED on the servosphere in the same study"
- `conditions`: append "binomial tests: females z = 0.55, p = 0.292; males z = 0.00, p = 0.572; nymphs z = 0.55, p = 0.292; on the servosphere 20 females oriented toward an infrared LED (850 nm, front about 41 °C, 5 cm away), p < 0.001"
- `note`: replace "main has no thermal record for either tick" with "main has no thermal record for this species".

Counted (line 6):
- `conditions`: replace "about half a day of exposure" with "whole-body exposure 11 h a day (08:00 to 19:00) for 5 days after a 3-day baseline; EMF parameters given in the Abstract and Introduction from the earlier study"; append "tail lifts counted from images taken every minute, blinding not stated; increase −0.5 ± 7.1 (control) against 3.7 ± 9.4 (EMF), ratio 0.9 ± 0.3 against 1.9 ± 0.6, n = 8, p = 0.02 each (Wilcoxon signed-rank named for the increase)".

Uncounted (line 2), suggested:
- `conditions`: append "405 nm polarized against unpolarized t = −2.63, df 70, p = 0.01; vertical and horizontal filters pooled for lack of difference (Figure 4)".

Uncounted (line 3), suggested:
- `conditions`: append "500 nm t = −0.36, df 43, p = 0.72; in the wavelength assay 500 nm light did not differ from darkness (about 0.10 cm), so the null may sit on a weak response; polarization-test means only in Figure 4".

## Owner questions

1. Otálora-Luna et al. print "p < 0.010 males, z = 1.64" (and z = 0.00 with p = 0.572 for I. scapularis males): should the desk file a sex-specific "attracted" claim that rests on an internally inconsistent statistic, or limit line 4's value to females and nymphs?
2. Tick heat from a Peltier (IR plus convective) is filed here as `sense_thermal`, while main files Carr and Salgado's heated plate for the same species as `sense_infrared`. Which key should heat-source attraction with radiation and convection unseparated take?
3. An extremely low frequency EMF with electric and magnetic parts unseparated (line 6): is `sense_magnetic` the right key, or should such records wait for a magnetic-only test?
4. Pogona vitticeps is absent from gbif-names.tsv (main's everyday log has GBIF 2465641 ACCEPTED): add it to taxonomy-extra.tsv?

Progress note: accurate on the DOIs, licences, n and names. It repeats the intensity framing ("Intensity not matched across wavelengths") without the paper's argument that the covariance runs the other way, and its tick line does not mention the servosphere LED result.

Verdict: 4 errors in 6 (66.7%), above the 5% bar; pooled 42.8%. Error lines: 1, 4, 5, 6. No unfixable records; lines 1, 4, 5 and 6 can merge with the counted text, lines 2 and 3 as filed (suggested additions optional).

This report is model output and carries no authority.
