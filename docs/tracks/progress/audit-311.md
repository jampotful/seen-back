# audit-311: desk-d223, evidence lines 8 to 14

Audited 31 October 2026 from the desk-d223 files present untracked in the worktree (docs/tracks/progress/desk-d223.md and docs/views/evidence/desk-d223.jsonl, 14 lines; neither committed here, neither edited). HEAD 003964c1 (desk-d222). Audit 310 judges lines 1 to 7; this report judges lines 8 to 14 only. `tools/senses/check.py` on the evidence file: 14 records, 0 problems. Quote lengths (`len(q.split())`) for lines 8 to 14: 30, 17, 19, 9, 16, 18, 20, all within 40. The unit has evidence records only, so the brief's search-record and plant-screening parts do not apply; audits 308 and 309 are the format model.

Sources opened (WebFetch): api.crossref.org/works for the five DOIs; journals.plos.org for 10.1371/journal.pone.0052551 (opened on the second attempt; the first returned an unrelated tsetse article and was discarded) and for 10.1371/journal.pone.0206526 (opened after several rate-limit refusals; no licence sentence and no Table 1 rows returned); the PMC copies PMC6211686 (Gnorimus, two passes) and PMC3642193 (Anopheles), both returned by my WebSearch; the University of Chicago repository PDF of the version of record for 10.1371/journal.pone.0025002 (two passes); eprints.soton.ac.uk/467735 (record page only, no full text); doaj.org/article/2e7c3d78829b4847974c59e1faa59be8 (eel abstract). journals.plos.org returned rate-limit errors on every attempt for 10.1371/journal.pone.0062995, 10.1371/journal.pone.0270573 and 10.1371/journal.pone.0025002; pmc.ncbi.nlm.nih.gov/articles/PMC3541397 returned a reCAPTCHA interstitial and PMC9246130 a permission timeout; neither was worked around. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened; a blob-storage PDF mirror returned by search was left alone. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences, table cells and fragments quoted for verification. 6 WebSearches used.

## Bibliographic and licence

- Lines 8, 9, Harvey et al. 2018, Crossref: 13 authors Deborah J. Harvey to Michael A. Birkett in the recorded order; title verbatim (also on the PLOS page); PLOS ONE 13(11), e0206526, issued 2018-11-01; licence CC BY 4.0, content-version vor; relation empty. Met. Licence: neither the PLOS page nor the PMC copy returned a licence sentence to me; the basis is the publisher's own page plus the Crossref CC BY 4.0 licence for the version of record (audits 307/308 rule). Acceptable, as the unit asked.
- Lines 10, 11, Spitzen et al. 2013, Crossref: ten authors Jeroen Spitzen to Willem Takken in the recorded order; title verbatim; PLoS ONE 8(5), e62995, issued 2013-05-02; CC BY 4.0, content-version unspecified; relation empty. Met. Licence: the PMC copy states the article is open access under a Creative Commons Attribution License (tool summary); the PLOS page did not open.
- Line 12, Kempster, Hart, Collin 2013, Crossref: authors in order; title verbatim; PLoS ONE 8(1), e52551, issued 2013-01-09; CC BY 4.0 unspecified. PLOS page, verbatim: "This is an open-access article distributed under the terms of the Creative Commons Attribution License"; citation "Kempster RM, Hart NS, Collin SP (2013) Survival of the Stillest: Predator Avoidance in Shark Embryos." Met.
- Line 13, Miller, Sharkh, Kemp 2022, Crossref: authors in order; title verbatim (colon-separated subtitle); PLOS ONE 17(6), e0270573, issued 2022-06-30; CC BY 4.0, content-version vor. Met. Licence: Crossref vor licence; the Southampton repository record prints "Available under License Creative Commons Attribution" for the version of record. The PLOS page did not open for me.
- Line 14, Coffin, Watters, Mateo 2011, Crossref: authors in order; title verbatim; PLoS ONE 6(9), e25002, issued 2011-09-21; CC BY 4.0 unspecified; relation has-review only. The version-of-record PDF read prints, verbatim, "This is an open-access article distributed under the terms of the Creative Commons Attribution License". Met.

Ruling on the unit's question (Crossref content-version "unspecified" plus a page-printed "Creative Commons Attribution License"): acceptable, record by record, for lines 10, 11, 12 and 14. The statement printed on the copy read is the licence; Crossref's "unspecified" says only that the deposit did not tie the licence URL to a version, and it agrees on CC BY. For lines 10 and 11 the statement was read on PMC, which carries the publisher's text. Lines 8 and 9 (Gnorimus) rest on the Crossref vor rule and are acceptable under audits 307/308. Line 13 has a Crossref vor licence and needs no ruling.

Bibliographic faults 0; licence faults 0. source.access "open" right on all seven.

## Names

- Gnorimus nobilis: Plazi treatment "Gnorimus nobilis subsp. nobilis, (Linnaeus, 1758)" (returned by my WebSearch) uses the name as accepted. Main has no Gnorimus row; main files the related Cetoniinae (Cetonia, Protaetia, Oxythyrea, Trichius) under Scarabaeidae and never uses Cetoniidae. Scarabaeidae, Coleoptera right.
- Anopheles gambiae: main's docs/views/gaps/gbif-names.tsv:303 "Anopheles gambiae EXACT ACCEPTED". The paper names Anopheles gambiae sensu stricto in its title, so this is the species, not the complex; audit 263 ruled that An. coluzzii must be filed under its own name when a paper prints it. This paper's Methods give a Wageningen colony from Suakoko, Liberia (1987) with no M/S form or coluzzii statement (tool summary), so An. gambiae as printed is right. Culicidae, Diptera as main.
- Chiloscyllium punctatum: Hemiscylliidae, Orectolobiformes, as main's audit/corrected/fish-shark.jsonl:22 and audit/corrected/methods.jsonl:10. Right.
- Anguilla anguilla: Anguillidae, Anguilliformes, as main's 10 rows. Right.
- Spheniscus humboldti: Spheniscidae, Sphenisciformes, as main's 95 rows. Right.

Name faults 0.

## Duplicates

git grep on origin/main across the whole docs tree (evidence, audit/corrected, audit/ALL.jsonl, searched, sheets, gaps, wanted, codex-findings, progress notes) for "Gnorimus", "noble chafer", "Cetoniinae", "Anopheles gambiae", "Spitzen", "Chiloscyllium", "Kempster", "bamboo shark", "shark embryo", "Anguilla anguilla", "Sharkh", "glass eel", "elver", "Spheniscus", "humboldti", "penguin" with odour terms, "Coffin", and the five DOIs. None of the five DOIs is on main. Gnorimus has no row. Anopheles gambiae has one acuity_cpd row (evidence/canon-4.jsonl:42, Feller et al. 2021) and no sense_chemical or sense_thermal row; desk-d201 held out a different wind-tunnel paper (Front Behav Neurosci 15). Chiloscyllium punctatum rows are lambda_max_nm, acuity_cpd, cff_hz, fovea and colour_vision from other papers; the only Hemiscylliidae sense_electric row is Hemiscyllium ocellatum pore anatomy (audit/corrected/fish-shark.jsonl:47, 10.1371/journal.pone.0049857); the only Kempster row is an Elasmobranchii pore review (audit/corrected/fish-shark.jsonl:130, a different paper). Anguilla anguilla rows are cff_hz and sense_magnetic (10.1371/journal.pone.0059212). Spheniscus humboldti rows are vision traits and one sense_hearing. "Coffin" on main is a different author (Robert D. Coffin, Panicum). The two Gnorimus records are different measures (Y-tube behaviour, EAG) and the two Anopheles records different treatments (odour + heat; heat alone); neither pair duplicates itself. Duplicates 0; contradictions 0.

## Per-record findings

### Line 8, Gnorimus nobilis, sense_chemical, Y-tube sex difference

Quote checked in verbatim pieces. PMC: "In Y-tube olfactometer assays, males responded to the synthetic compound at doses of 1 μg and above"; PLOS page: "1 μg and above (Table 1), whereas females were repelled by the compound at all doses tested." It starts the sentence and the pieces overlap. MATCH, whole sentence, 30 words. The value says no more than the quote.

**Error (contrary results in Table 1 and sample sizes omitted; "n not stated" is wrong).** Table 1 rows for 2P3H on the PMC copy (Pos / No. replicates / exact binomial p, as printed): 1 ng "2 / 17 / 0.0012" males, "0 / 12 / 0.0001" females; 10 ng "1 / 17 / 0.0001", "1 / 12 / 0.0032"; 100 ng "1 / 17 / 0.0003", "0 / 12 / 0.0001"; 1 μg "12 / 17 / 0.0717", "0 / 12 / 0.0001". Footnote b, verbatim: "No. replicates is the total number of beetles tested individually to each stimulus." So (a) 17 males and 12 females were tested per stimulus, while the record says the number is not stated and that Table 1 was not read; (b) at 1, 10 and 100 ng males chose the compound arm significantly less often than chance (2/17, 1/17, 1/17), the pattern the record calls repellence in females, and the text does not discuss it (tool summary: no Results or Discussion sentence calls the male ng responses avoidance); (c) at 1 μg the male response is 12/17, p = 0.0717, not significant, so "1 μg and above" is supported by the table only at 10 μg (13/17, p = 0.0245) and 100 μg (17/17, p = 0.0001) (these two rows tool summary). Also omitted: "no beetle was used more than once" (verbatim) and that the beetles were field-collected adults (Bystrzyca, Poland, and Worcestershire, UK; tool summary). Doses tested were 1, 10, 100 ng and 1, 10, 100 μg (tool summary). Fixable.

### Line 9, Gnorimus nobilis, sense_chemical, male EAG dose-dependent

PLOS page, verbatim and whole: "Synthetic 2-propyl (E)-3-hexenoate elicited EAG responses from male antennae in a dose-dependent manner (Fig 3, S2 Table)." MATCH, 17 words. n = 5 initial and n = 4 dose-response recordings and the hexane control match the Methods (tool summary). Grade m right.

**Error (stimulus doses omitted while marked unread).** The Methods print the dose series 0.01, 0.1, 1, 10, 100 and 1000 μg on filter paper in Pasteur pipettes, with responses normalised to hexane delivered before and after each set (tool summary; verbatim: "Antennal responses were normalized against a solvent (hexane)."). The record says "dose values are in Fig 3 and S2 Table, which were not read", omitting a stimulus range printed in the Methods. Which doses differed from hexane is shown only in Fig 3 (ANOVA then LSD, 4 replicates; tool summary), and the record should say so. Fixable.

### Line 10, Anopheles gambiae, sense_chemical, odour + heat longer flights and more landings

Abstract (PMC), verbatim and whole: "The combination of odor+heat resulted in longer flights with more landings on the source than to either cue alone." MATCH, 19 words. Counts (201 tested, 156 upwind, 145 tracks), 65 to 85% upwind (χ², P = 0.076), 46.5% landings against 0 to 7% (χ², P < 0.05), clean sock with heater off as control: all match (tool summary).

**Error (colony origin wrongly said unstated; treatment-order design omitted).** (a) The Methods give the colony: Wageningen University, derived from Suakoko, Liberia, in 1987 and reared on human blood since 1988 (tool summary); the record says "colony origin of the mosquitoes is not stated in the parts read". A laboratory colony about 25 years in culture is the lab-versus-wild point the brief requires. (b) Testing order was randomised between and within days, the treatment changed after every five mosquitoes and each mosquito used once (tool summary); not carried. (c) Wording within the same error: the value is a combined odour + heat effect; under sense_chemical it should say the landing increase needed heat with the odour (odour alone gave 0 to 7% landings and convoluted flights, which the conditions already carry). Fixable.

### Line 11, Anopheles gambiae, sense_thermal, heat alone short and direct

Abstract (PMC), verbatim and whole: "With heat alone, flights were similarly short and direct." MATCH, 9 words; "similarly" refers to the preceding verbatim sentence "With wind as the only stimulus (control), short and close to straight upwind flights were recorded.", which the record quotes. Table 1 (tool summary): track duration 15.2 s control and 18.8 s heat, upwind speed 22.7 and 24.7 cm/s, same letter "a", no significant difference. The null is scoped right and sense_thermal fits.

**Error (as line 10: colony origin wrongly said unstated, randomised order omitted).** Same fix as line 10. Uncounted: the air-temperature effect of the 34 °C source was measured only up to 20 cm downwind (tool summary), so a heat-alone null in a 160 cm tunnel says little about detection at close range.

### Line 12, Chiloscyllium punctatum, sense_electric, stage 34 response at 0.4 µV/cm

PLOS page, verbatim: "In contrast, stage 34 embryos would respond to electric field strengths as low as 0.4 µV/cm ([Fig. 3I])." (the brackets are the tool's link markup). The record's quote stops at "0.4 µV/cm" with no final full stop and no mark for the dropped figure reference. Following sentence, verbatim: "Embryos prior to stage 32 failed to show any response to electric field strengths between 0.4 µV/cm and 2.1 µV/cm.", as recorded.

**Error (quote cut not marked; design points omitted).** (a) Quote form: the trailing "(Fig. 3I)" and full stop are cut without a mark. (b) Field strength was calculated from an ideal-dipole equation from the applied current (100 to 500 µA), electrode separation (5 cm) and 12 cm embryo distance, not measured (tool summary); omitted, and it bears directly on an electric value. (c) The 0.4 is the lower edge of a 0.4 to 0.6 µV/cm band; the record calls it the lowest tested value but not a band edge. (d) Stage 34 mean freeze durations about 15.8 s, 38.4 s and 59.4 s at the three bands (Fig 3 caption), strongest response at 0.25 to 1.00 Hz with a 0.5 Hz peak, repeated exposure shortening responses (habituation within 30 to 40 min), 40 min between trials in pseudorandom order, eggs from captive-bred adults at Queensland aquaria, 24 to 25 °C, no sham trials and no stated blinding (all tool summary). The record carries the 11 embryos and no-control point but none of (b) to (d). Fixable.

### Line 13, Anguilla anguilla, sense_electric, low-field route preferred under 2 Hz

Abstract (DOAJ copy), verbatim and whole: "For the 1.22, 2.17 and 3.74 Vcm-1 and under 2 Hz, eel preferred to pass the LEF route." MATCH, 18 words. The next two abstract sentences match the record's conditions. The full text (journals.plos.org, PMC) would not open for me, so the Methods and Results details in the record (River Severn glass eel, size, 12 °C, the 10 Hz null sentence, χ² for frequency, 22.2% rejection, pilot of 38 eel) are unchecked.

**Error (field contrast omitted).** The abstract prints that the treatment route gave "High Electric Field (HEF) strength that was between 1.5-2 times stronger than" "the Low Electric Field (LEF) strength encountered in the alternative route". Both routes carried a field in treatments; the preference is for the weaker of two fields differing by a factor of 1.5 to 2, not for a field-free route. The record's method says the electrodes split the section "into a high-field and a low-field route" and the units give the mean high-field strength, but nowhere says the low-field route was also electrified or gives the ratio. Fixable.

### Line 14, Spheniscus humboldti, sense_chemical, more time with non-kin than kin odour

Results (version-of-record PDF), verbatim and whole: "Total time investigating and inside kennels was longer for non-kin odors than kin odors (t11 = 2.724, P = 0.02)." MATCH, 20 words. Following sentence, verbatim: "For all tests, no effects of sex or mating status (previously mated or not) were found." Familiar test direction, verbatim: "Penguins spent more time inside kennels with familiar odors than inside kennels with unfamiliar odors" (Z = 1.992, P = 0.046), as recorded. Observer blinding and same-sex donor pairs as recorded.

**Error (kin-test design misstated; test order and inside-time result omitted).** (a) Methods, verbatim: "odors from an unfamiliar kin (coefficient of relationship, r, = 0.125–0.5) and an unfamiliar non-kin". Both kin-test odours were unfamiliar, so the record's "the preference is for unfamiliar odour, which the authors read as novelty" misstates the comparison; the authors' reading, verbatim, is "Penguins may have perceived non-kin odors as novel because they did not match the birds’ recognition templates." (phenotype matching). (b) Verbatim: "all but one bird had the kin-nonkin test first", the tests about 77 days apart (tool summary): test order was not counterbalanced. (c) The kin test's time-inside result, verbatim "Penguins spent more time inside kennels containing non-kin odors than kin odors" (t11 = 3.434, P = 0.006), is not carried. Fixable.

## Trait key

- Lines 8, 9, sense_chemical: fit (behaviour of living beetles to a volatile pheromone; EAG of living antennae).
- Line 10, sense_chemical: fits once worded as an odour response that needed heat for landing (line 10 fix).
- Line 11, sense_thermal: fits (heated source, null against the wind-only control).
- Lines 12, 13, sense_electric: fit; line 13 is behavioural avoidance of a field contrast, not a sensory threshold, which the record says.
- Line 14, sense_chemical: fits (living birds' responses to conspecific preen-gland odour).

Trait key faults 0 counted.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 8 | Gnorimus nobilis, Y-tube sex difference | error, fixable | conditions (value optional) | Quote MATCH (30 words); Table 1 n (17 males, 12 females), significant male avoidance at 1 to 100 ng and non-significant 1 μg row omitted; "n not stated" wrong |
| 9 | Gnorimus nobilis, male EAG dose-dependent | error, fixable | method, conditions | Quote MATCH (17 words); Methods dose series 0.01 to 1000 μg omitted |
| 10 | Anopheles gambiae, odour + heat landings | error, fixable | conditions, value | Quote MATCH (19 words); colony origin (Suakoko, Liberia, 1987) printed but said unstated; randomised order omitted |
| 11 | Anopheles gambiae, heat alone null | error, fixable | conditions | Quote MATCH (9 words); same colony and order omissions |
| 12 | Chiloscyllium punctatum, 0.4 µV/cm stage 34 | error, fixable | quote, conditions | Trailing "(Fig. 3I)." cut unmarked; calculated (not measured) field, intensity bands, graded and habituating response omitted |
| 13 | Anguilla anguilla, low-field route at 2 Hz | error, fixable | method, conditions | Quote MATCH (18 words); both routes electrified, HEF 1.5 to 2 times LEF, omitted; full text unchecked |
| 14 | Spheniscus humboldti, non-kin odour preferred | error, fixable | conditions | Quote MATCH (20 words); both kin-test odours unfamiliar, record says preference is for unfamiliar odour; uncounterbalanced test order and t11 = 3.434 inside-time result omitted |

7 of 7 records in error (100.0%): scientific-context 7 (lines 8 to 14), one of which (line 12) also has a quote-form fault; value beyond quote 0; duplicates 0; bibliographic 0; names 0; licence 0; trait key 0; grading 0.

Pooled with audits 172 to 309: 343 of 746 evidence records (46.0%; 336 of 739 before this audit, 7 of 7 here). Audit 310's lines 1 to 7 are not included.

## Replacement text

Line 8:
- `conditions`: replace "the number of beetles tested, whether the arms were switched, and beetle age beyond 'adult' are not stated in the Methods read; results are in Table 1 (not read);" with "17 males and 12 females were tested individually to each stimulus (Table 1 footnote: 'No. replicates is the total number of beetles tested individually to each stimulus.'), no beetle used more than once, test beetles field-collected adults (Bystrzyca, Poland, and Worcestershire, UK); doses 1, 10, 100 ng and 1, 10, 100 ug; arm switching and beetle age are not stated; exact binomial tests against 0.5; in Table 1 males chose the compound arm 2/17 at 1 ng (p = 0.0012), 1/17 at 10 ng (p = 0.0001) and 1/17 at 100 ng (p = 0.0003), significantly below chance, which the text does not discuss, and 12/17 at 1 ug (p = 0.0717, not significant), so male attraction is significant only at 10 ug (13/17, p = 0.0245) and 100 ug (17/17, p = 0.0001); females chose it 0 to 2 of 12 times at every dose (all p < 0.05);".
- `value` (optional, to match the table): "males were attracted to synthetic 2-propyl (E)-3-hexenoate at 10 and 100 ug (authors: 1 ug and above) and chose against it at 1 to 100 ng, whereas females were repelled at all doses tested".

Line 9:
- `method`: "electroantennogram recordings from male antennae of live beetles, n = 5 for the initial recordings and n = 4 for a dose series of 0.01, 0.1, 1, 10, 100 and 1000 ug on filter paper in Pasteur pipettes, responses normalised to hexane delivered before and after each set".
- `conditions`: replace "dose values are in Fig 3 and S2 Table, which were not read" with "which doses differed from the hexane control (ANOVA then LSD, 4 replicates) is shown only in Fig 3 and S2 Table, which were not read".

Lines 10 and 11:
- `conditions`: replace "colony origin of the mosquitoes is not stated in the parts read;" with "laboratory colony at Wageningen University derived from Suakoko, Liberia, in 1987 and reared on human blood since 1988 (Methods, page summary), not wild mosquitoes; each mosquito tested once, testing order randomised between and within days with the treatment changed after every five mosquitoes (page summary);".
- Line 10 `value`: "odour + heat together gave longer flights with more landings on the source than either cue alone (landing needed heat with the odour)".
- Line 11 `conditions` (uncounted, optional): append "; the air-temperature effect of the 34 C source was measured only up to 20 cm downwind (page summary)".

Line 12:
- `quote`: "In contrast, stage 34 embryos would respond to electric field strengths as low as 0.4 µV/cm (Fig. 3I)." (or keep the current text and mark the cut after "0.4 µV/cm").
- `conditions`: append "; field strength was calculated from an ideal-dipole equation (100 to 500 uA, 5 cm electrode separation, embryo 12 cm away), not measured; intensities were bands, so 0.4 is the lower edge of the 0.4 to 0.6 uV/cm band; stage 34 freeze duration rose with intensity (about 15.8 s, 38.4 s and 59.4 s for the three bands, Fig 3 caption), responses were strongest at 0.25 to 1.00 Hz (peak 0.5 Hz), and repeated exposure shortened responses (habituation within 30 to 40 min); 40 min between trials in pseudorandom order; eggs from captive-bred adults at Queensland aquaria, 24 to 25 C; no blinding stated (page summary)".

Line 13:
- `method`: replace "splitting it into a high-field and a low-field route)" with "splitting it into a high-field (HEF) and a low-field (LEF) route; in treatments both routes carried a field, the HEF strength 1.5 to 2 times the LEF strength)".
- `conditions`: replace "this is a behavioural avoidance of a field," with "this is a preference for the weaker of two fields differing by a factor of 1.5 to 2 (Abstract), a behavioural avoidance,".

Line 14:
- `conditions`: replace "unfamiliar non-kin odour was the comparison in the kin test;" with "the kin test paired odours of an unfamiliar kin (r = 0.125 to 0.5) and an unfamiliar non-kin ('odors from an unfamiliar kin (coefficient of relationship, r, = 0.125–0.5) and an unfamiliar non-kin'), so familiarity was matched;".
- `conditions`: replace "the preference is for unfamiliar odour, which the authors read as novelty" with "time inside kennels was also longer for non-kin than kin odour (t11 = 3.434, P = 0.006); the authors read the non-kin preference as novelty through phenotype matching (non-kin odours did not match the birds' recognition templates); all but one bird took the kin test first, about 77 days before the familiarity test, so test order was not counterbalanced; no effects of sex or mating status were found".

## Owner questions (the unit's, answered where I could)

1. Gnorimus licence (no licence sentence on the copy read, Crossref CC BY 4.0 vor): acceptable under the audits 307/308 rule. The PLOS page I opened also returned no licence sentence.
2. Crossref content-version "unspecified" with a page-printed "Creative Commons Attribution License": acceptable for lines 10, 11, 12 and 14; the printed statement on the copy read governs and Crossref agrees on CC BY.
3. Anopheles colony: the Methods do state it (Wageningen colony from Suakoko, Liberia, 1987, on human blood since 1988). File as An. gambiae as printed (sensu stricto in the title) and carry the colony and its age as a lab-strain condition. No M/S form or coluzzii statement was seen.
4. Chiloscyllium 0.4 µV/cm: right to call it the lowest tested value; add that intensities were bands and field strength was calculated, not measured.

## Progress note

Accurate on citations, licences, names and duplicates for lines 8 to 14. The Records list repeats the faults above: Gnorimus "1 ug and above" without the non-significant 1 ug row and the male low-dose avoidance; Anopheles described with an unknown colony that the Methods name; Chiloscyllium without the calculated field; the eel result without the two-field design; the penguin kin test without matched unfamiliarity.

Verdict: 7 of 7 judged records (lines 8 to 14) in error (100.0%), above the 5% bar. Error lines: 8, 9, 10, 11, 12, 13 and 14, all fixable with the replacement text above. Pooled 343 of 746 (46.0%).

This report is model output and carries no authority.
