# audit-319: desk-d228, evidence lines 1 to 5

Audited 31 October 2026 from the desk-d228 files present untracked in the worktree (docs/tracks/progress/desk-d228.md and docs/views/evidence/desk-d228.jsonl, 9 lines; neither committed here, neither edited). Lines 6 to 9 belong to audit 320. HEAD and origin/main f250eade (desk-d227). `python3 -I tools/senses/check.py | grep d228`: "docs/views/evidence/desk-d228.jsonl: 9 records, 0 problems". Quote lengths (`len(q.split())`) for lines 1 to 5: 20, 13, 13, 8, 21, all within 40. Evidence records only; audits 315 to 317 are the format model.

Sources opened (WebFetch): www.frontiersin.org /full pages for 10.3389/fphys.2023.1155129 (three passes) and 10.3389/ffgc.2025.1588866 (two); peerj.com/articles/8149/ (three) and peerj.com/articles/8149.pdf (two); journals.plos.org page for 10.1371/journal.pone.0082182 (three); api.crossref.org/v1/works for all four DOIs (two retries after rate limits). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 0 WebSearches and 15 WebFetch calls used.

## Bibliographic and licence

- Line 1, Biswas, Yuvaraj, Hansson, Löfstedt, Anderbrant, Andersson 2023, Crossref /v1: authors in the recorded order; title verbatim; Frontiers in Physiology 14, 1155129, issued 2023-03-20, no issue; CC BY 4.0 vor from 2023-03-20; relation empty, no update-to. Page: "Volume 14 - 2023", no licence sentence returned (menu label "Copyright statement" only). Accepted under the Crossref vor rule (publisher's own page). Met.
- Line 2, Shewale, Bláha, Synek, Schebeck, Andersson, Kandasamy, Jirošová 2025, Crossref /v1: authors in the recorded order; title returned in two halves, "Comparative analysis of olfactory sensory neurons in two Ips species" and "reveals conserved and species-specific olfactory adaptations", and the page prints the same words; joined, they match the recorded title (129 characters). Frontiers in Forests and Global Change 8, 1588866, issued 2025-06-04, no issue; CC BY 4.0 vor; relation empty. Page: no licence sentence. Accepted under the Crossref vor rule. Met. The note's "confirm the printed title if audited" is answered: confirmed.
- Lines 3 and 4, Watve, Prati, Taborsky 2019, PDF page 1: "Copyright 2019 Watve et al." and "Distributed under Creative Commons CC-BY 4.0"; authors and title as recorded; PeerJ 7, e8149. Crossref: CC BY 4.0, content-version unspecified, relations has-review only, no update-to. Accepted (licence printed on the copy read). Met.
- Line 5, Alderks, Sisneros 2013, Crossref /v1: authors and title verbatim; PLoS ONE 8(12), e82182, issued 2013-12-10; CC BY 3.0 vor; relation empty, no update-to. Page prints "This is an open-access article distributed under the terms of the Creative Commons Attribution License". Met.

Bibliographic faults 0; licence faults 0. source.access "open" right on all five. No retraction or update-to on any DOI.

## Names

Trypodendron lineatum and Ips acuminatus (Curculionidae, Coleoptera; Scolytinae), Neolamprologus pulcher (Cichlidae, Cichliformes), Porichthys notatus (Batrachoididae, Batrachoidiformes; order present in docs/views/world-orders.csv:346): names as printed in the papers, families and orders right. No authority was looked up for any of the four (not counted; see Unchecked). Name faults 0.

## Duplicates

git grep on origin/main across the whole docs tree for "Trypodendron", "Ips acuminatus", "Neolamprologus", "pulcher", "Porichthys", "midshipman", "Batrachoid", "Lepidiolamprologus", "lineatin", "isophorone", "Biswas", "Shewale", "Watve", "Alderks" and the four DOI suffixes. Trypodendron and Ips acuminatus appear only as held leads in desk-d221.md:16 and the licence ruling in audit-307.md:134, audit-308.md:118 and desk-d221.md:27/39; "isophorone" otherwise only in the Buddleja davidii rows (sweep-22); "pulcher" only in other taxa (Malurus pulcherrimus, Euphorbia pulcherrima); "Watve" only as a query word in sweep-9.jsonl:2 (Merops). No species or DOI of lines 1 to 5 is on main as a record. Duplicate faults 0.

## Per-record findings

### Line 1, Trypodendron lineatum, 37 of 90 strongly responding OSNs best to lineatin

Results 3.3, verbatim: "As many as 37 of the 90 strongly responding OSNs (A cells) responded best to lineatin (Table 1; Figure 2B)." MATCH, 20 words; value says no more. Confirmed: 57-compound panel at 10 µg (10 µL of 1 µg/µL), random order, paraffin oil blank per sensillum subtracted, "responding strongly (≥80 Hz) to one or several compounds at the 10 μg stimulus dose" (Table 1 caption), "any average response below 20 Hz was considered as no response.", "(187 sensilla were contacted, using 48 male and 64 female individuals)" against 170 in the Abstract, traps "baited with commercial lineatin dispensers", April to June 2020 and 2021, two southern Swedish forests, Table 1 22 female and 15 male class 1 neurons, no sex test, dose series 10 pg to 10 µg with "(±)-lineatin (OSN class 1; n = 8)" and racemic lineatin only.

**Error (non-responders and unclassified neurons omitted; strength of secondary responses misstated; authors' sex caveat omitted).** (a) "Neurons in the remaining 73 olfactory sensilla did not respond to any compound." and "a total of 90 (female: 46, male: 44) out of 119 responsive neurons could be classified": 73 of 170 sensilla were silent and 29 responsive neurons fall outside the 13 classes; the record gives neither, so the reader cannot place the 90 in the sample. (b) The record says the 28 lineatin neurons responded to other compounds "generally more weakly"; the page says "Although the average responses to the secondary compounds were weak" and "several individual OSNs responded by > 60 Hz, and sometimes even >80 Hz to a few of the secondary compounds", so some secondary responses reached the paper's own "strong" level. (c) The record lists classes found only in males or only in females without the authors' qualifier: "Because only few of these OSNs were found we cannot, however, classify them as sex specific." Fixable.

### Line 2, Ips acuminatus, IAc6 >80 Hz to α-isophorone (n = 6)

Results 3.2.2, verbatim: "The IAc6 class showed high specificity (>80 Hz) to α-isophorone (n = 6)." MATCH, 13 words, one whole sentence as printed and not reassembled (it is a Results sentence, not an Abstract one; the Abstract does not mention α-isophorone or IAc6). Value says no more. Confirmed: Rouchovany batch (late spring 2024, Pinus sylvestris branches, reared at CULS) and Schönberg am Kamp batch (spring 2024, reared at BOKU Vienna, sent to Lund); 82 sensilla of I. acuminatus.

**Error (preceding sentence misattributed to IAc6; dose-response n omitted; non-responders omitted).** (a) The record's conditions open with "the preceding Results sentence says IAc6 was the most abundant OSN class in this species and was found exclusively in females (n = 7)". The preceding sentences are about IAc5: "The IAc5 class responded strongly (>80 Hz) to (−)-verbenone (n = 7) and exhibited weaker secondary responses" ... "This was the most abundant OSN class in this species (Figure 4B) and was found exclusively in females (n = 7)." The paper does not state the sex of the IAc6 neurons. The record thus files a false sex and abundance claim for IAc6 and an n conflict that does not exist. (b) The next sentence, which the record carries only as "tool summary", was returned verbatim: "These A neurons did not respond to verbenone or any other compounds from the odor panel," + "dose–response tests revealed an exceptionally low response threshold at 10 pg, indicating high sensitivity (Figure 4E)."; the Figure 4 legend gives "IAc6 class: α-isophorone (n = 4)" for the dose series, against n = 6 in the text, and the record omits it; IAc6 lay "mainly in the sensory band B on the antennal club". (c) Of 82 contacted I. acuminatus sensilla, 69 responded to at least one compound, 12 to none and 3 were excluded for poor recording quality (tool summary); omitted. Fixable.

### Line 3, Neolamprologus pulcher, attack playback much like live predator

Abstract, verbatim: "However, playbacks mimicking an attacking predator induced responses much like a live predator." MATCH, 13 words; the preceding Abstract sentence opens "Regular playbacks of calmly swimming predators were less effective than live predators". Confirmed: N = 16, five presentations, randomised, at least 3 h apart, blind observer (SP), "predator-naïve adults (size range 40–45 mm) reared in the laboratory for 5 generations", predators "first generation offspring of wild caught fish", aggression GLMM χ² = 23.41, p = 0.0001, frontal vs live p = 0.13, lateral vs live p = 0.0008, attentiveness frontal vs live p = 0.02. Trait behaviour_vision fits (screen stimuli).

**Error (attack-versus-calm comparisons omitted; one comparison misdescribed; predator N omitted).** (a) The attack playback did not differ from the calm playback on any measure: Table 1 aggression "Lateral-Frontal −1.06 0.52 73 −2.05 0.25"; Table 2 attention "Lateral-Frontal 66.9 122 60 0.54 0.98"; Table 3 interaction zone "Lateral-Frontal −27.1 30.7 60 −0.88 0.90". The record names only the p = 0.98 row and says the text read "does not name" its measure (it is attentiveness, Table 2). So "much like a live predator" rests on a non-significant frontal-versus-live difference, while the attack playback is not shown to beat the calm one. (b) Omitted: time in interaction zone differed by presentation type (LMM F = 5.34, p = 0.0009; frontal vs live p = 0.46, lateral vs live p = 0.09) and time in safe zone did not (F = 1.29, p = 0.28) (tool summary for these statistics); attentiveness overall LMM F = 4.14, p = 0.004. (c) "Individual L. elongatus (N = 2)": two predator fish supplied all videos and live presentations of Experiment 1 ("the same individual L. elongatus also acted as live stimulus."); focal-fish sex is not reported; no sample-size justification. Fixable.

### Line 4, Neolamprologus pulcher, chemical cues no effect (null)

Abstract, verbatim: "Chemical cues did not affect predator directed behaviour." MATCH, 8 words (printed unhyphenated, as the quote has it). Distinct from line 3: Experiment 2 (N = 18, four cues on a calm playback) against Experiment 1 (N = 16, five visual stimuli). Confirmed: "a control cue of water collected from the focal’s own tank", aggression χ² = 2.08, p = 0.55, attentiveness F = 1.15, p = 0.33, safe zone F = 1.44, p = 0.24, interaction zone F = 0.36, p = 0.77, blind observer. The record's caveat that the assay was combined visual plus chemical is right.

**Error (single unstated stimulus amount and absent power justification omitted for a null; predator-odour source misdescribed).** (a) "The final volume of all cues was maintained at 120 mL (0.6% tank volume)." Each cue was given once at one concentration through a funnel at the start of the calm playback; skin extract from 11 juvenile N. pulcher was diluted 16-fold then 10-fold (tool summary). A null at one concentration with no odour-only arm needs the stimulus amount; the record gives none. (b) No power analysis or sample-size justification is given; the authors explain the null by "precedence of visual cues over chemical cues". (c) Predator odour came from "individual L. elongatus (N = 3)" held 48 h in 60 L tanks, fed daily and then unfed for 24 h before 500 mL was taken and frozen (tool summary for the 48 h and feeding schedule); the record's "tank water collected after 24 h without feeding" drops the three donors and the holding time. Fixable.

### Line 5, Porichthys notatus, lowest AEBR thresholds 140 to 150 dB re 1 µPa below 225 Hz

Abstract. The page prints "Lowest AEBR thresholds were 140–150 dB re 1 µPa or −33 to −23 dB re 1 g for frequencies below 225 Hz." (two passes; the preceding sentence prints "154 dB re1 µPa" without the space, the target sentence with it). The record's quote has "re1 µPa": **quote not verbatim**. Confirmed: response "only considered when the caudal fin moved greater than 50%" of total length, video at 30 frames/s, "All fish were randomly presented 100 ms pure tone stimuli", calibration script equalising sound pressure across frequencies, 154 to 136 dB in 3 dB steps, groups n = 19, 19, 12, 17, Tamales Bay and Seal Rock Beach, 15 ± 2 °C, no sham control, BEF Abstract/Results wording mismatch (the Results also report no difference in BEF distribution across size classes, p = 0.095, tool summary).

Hearing measured or inferred: measured as a behavioural threshold to calibrated tones, with sound pressure (Brüel & Kjær 8103) and particle acceleration (3-axis PCB 356A32 accelerometer at the fish position, 10 cm above the speaker, in a 30 cm Nalgene tank) both recorded. The sense_hearing filing stands, but the paper does not separate inner ear from lateral line: "The lateral line organ is likely involved in mediating the AEBR but not necessary to evoke the startle-like response." That conclusion rests on DASPEI staining of 35 larvae and three larvae without neuromasts that still responded, with no ablation (tool summary for the n = 3 and no-ablation points). Sexes and male types: the subjects are larvae and juveniles of unknown sex; the paper gives no nest count for the threshold fish and does not say whether nests were guarded by type I males (tool summary), which bears on parentage only, not on the trait.

**Error (quote not verbatim; lateral-line involvement and scoring gaps omitted; value adds "in larvae").** (a) "re1" for "re 1" in the quote. (b) Omitted: the authors' own statement that the lateral line likely mediates the response, the near-field geometry (fish 10 cm above the speaker in a 30 cm tank), unstated number of presentations per level and unstated scorer blinding, and group sizes totalling 67 against 62 in the onset experiment (Figure 4 cites 60 larvae and 2 juveniles; tool summary). (c) The value's "in larvae" is not in the quote and the threshold groups include juveniles (2.8 to 3.2 cm). Fixable.

## Trait key

- Lines 1 and 2, sense_chemical: fit (single-sensillum recordings of living beetles).
- Line 3, behaviour_vision: fits.
- Line 4, sense_chemical: fits as a filed null, with the design caveats.
- Line 5, sense_hearing: fits as a behavioural threshold with measured pressure and acceleration; the lateral-line caveat goes in conditions.

Trait key faults 0.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Trypodendron lineatum, 37 of 90 best to lineatin | error, fixable | conditions | Quote MATCH (20 words); 73 silent sensilla and 29 unclassified responsive neurons omitted; secondary responses up to >80 Hz misstated as weaker; authors' "cannot classify as sex specific" omitted |
| 2 | Ips acuminatus, IAc6 >80 Hz to α-isophorone | error, fixable | conditions | Quote MATCH (13 words, whole printed Results sentence); IAc5's "most abundant, females only (n = 7)" attributed to IAc6; dose-response n = 4 omitted; non-responders omitted |
| 3 | Neolamprologus pulcher, attack playback like live | error, fixable | conditions | Quote MATCH (13 words); attack vs calm playback non-significant on all measures (p = 0.25, 0.98, 0.90) omitted or misdescribed; zone results omitted; two predator individuals omitted |
| 4 | Neolamprologus pulcher, chemical cues null | error, fixable | conditions | Quote MATCH (8 words); single cue amount (120 mL, 0.6% tank volume) and dilutions omitted for a null; no power justification; three odour donors omitted |
| 5 | Porichthys notatus, AEBR 140 to 150 dB | error, fixable | quote, value, conditions | Quote has "re1" where the page prints "re 1"; lateral-line involvement and near-field setup omitted; value adds "in larvae" |

5 of 5 records in error (100%): scientific-context 5 (lines 1 to 5; line 2 also a misattributed result), quote form 1 (line 5, same record), value beyond quote 1 (line 5, same record), name 0, duplicates 0, bibliographic 0, licence 0, grading 0. HOLD OUT: none.

Pooled with audits 172 to 318: 384 of 792 evidence records (48.5%): audit 316's 370 of 778, plus audit 317's 5 of 5 and audit 318's 4 of 4 (379 of 787), plus 5 of 5 here. Audit 320's count for this unit's lines 6 to 9 is to be added to this figure.

Verdict: 5 of 5 records in error (100%), above the 5% bar. All fixable with the replacement text below; none held out.

## Replacement text

Line 1:
- `conditions`: replace "most in both sexes (classes 5, 8 and 11 only in males, class 7 only in females);" with "most in both sexes (classes 5, 8 and 11 only in males, class 7 only in females, but the authors write 'Because only few of these OSNs were found we cannot, however, classify them as sex specific.');".
- `conditions`: replace "the next Results sentence says 28 of the lineatin-responsive neurons also responded to other compounds, generally more weakly;" with "the next Results sentence says 'Most (28) of the lineatin-responsive OSNs displayed responses to additional compounds.'; average secondary responses were weak, but several individual OSNs responded above 60 Hz and sometimes above 80 Hz to a few secondary compounds; 'Neurons in the remaining 73 olfactory sensilla did not respond to any compound.', and 90 (46 female, 44 male) of 119 responsive neurons could be classified, so 29 responsive neurons lie outside the 13 classes;".

Line 2:
- `conditions`: replace "the preceding Results sentence says IAc6 was the most abundant OSN class in this species and was found exclusively in females (n = 7), so the n = 7 and n = 6 of the two sentences are not reconciled in the text;" with "the sex of the IAc6 neurons is not stated (the preceding sentence, 'most abundant' and 'found exclusively in females (n = 7)', is about class IAc5, which responded to (-)-verbenone);".
- `conditions`: replace "the tool summary says IAc6 neurons did not respond to verbenone or other panel compounds and had a threshold near 10 pg, which is not in the quote and is not carried in the value;" with "the next Results sentence says these A neurons did not respond to verbenone or any other panel compound and the dose-response threshold was 10 pg, with n = 4 in the Figure 4 legend against n = 6 in the text; IAc6 lay mainly in sensory band B of the antennal club; the threshold is not carried in the value;".
- `conditions`: replace "82 sensilla of I. acuminatus (85 of I. cembrae) were contacted" with "82 sensilla of I. acuminatus (85 of I. cembrae) were contacted, of which 69 responded to at least one compound, 12 to none and 3 were excluded for poor recording quality".

Line 3:
- `conditions`: replace "predators (Lepidiolamprologus elongatus, 80 to 140 mm) were first-generation offspring of wild-caught fish;" with "predators (Lepidiolamprologus elongatus, 80 to 140 mm) were first-generation offspring of wild-caught fish, and Experiment 1 used two predator individuals, the same fish filmed for the playbacks and presented live; focal-fish sex is not reported and no sample-size justification is given;".
- `conditions`: replace "the page also reports no difference between lateral and frontal playbacks at p = 0.98 (Table 2) for a measure the text read does not name;" with "the attack (frontal) playback did not differ from the calm (lateral) playback on any measure: aggressive displays p = 0.25 (Table 1), attentiveness p = 0.98 (Table 2), time in the interaction zone p = 0.90 (Table 3); time in the interaction zone differed by presentation type (LMM F = 5.34, p = 0.0009; frontal vs live p = 0.46, lateral vs live p = 0.09) and time in the safe zone did not (F = 1.29, p = 0.28); 'much like a live predator' rests on non-significant differences from the live predator, and the attack playback is not shown to exceed the calm one;".

Line 4:
- `conditions`: replace "predator odour was tank water collected after 24 h without feeding and frozen at -20 C, skin extract was prepared after Brown and Smith (1998);" with "predator odour was water from three predators each held 48 h in 60 L tanks, the last 24 h unfed, then frozen at -20 C; skin extract from 11 juvenile N. pulcher was prepared after Brown and Smith (1998) and diluted 16-fold and then 10-fold; every cue, the control included, was 120 mL (0.6% of tank volume) poured in once at the start of the calm-predator playback, a single concentration with no odour-only arm; focal-fish sex is not reported and no sample-size justification or power analysis is given; the authors attribute the null to 'precedence of visual cues over chemical cues';".

Line 5:
- `quote`: replace "140–150 dB re1 µPa or" with "140–150 dB re 1 µPa or".
- `value`: replace "at frequencies below 225 Hz in larvae" with "at frequencies below 225 Hz".
- `conditions`: replace "no sham (no-stimulus) control is described;" with "no sham (no-stimulus) control is described; fish sat 10 cm above the speaker in a 30 cm diameter tank, with particle acceleration measured by a 3-axis accelerometer at the fish position; the Abstract says 'The lateral line organ is likely involved in mediating the AEBR but not necessary to evoke the startle-like response.', a conclusion from neuromast staining and three larvae without neuromasts that still responded, with no lateral-line ablation, so the thresholds may combine inner-ear and lateral-line input; the number of presentations per level and scorer blinding are not stated; the four groups total 67 fish against 62 in the onset experiment, not reconciled in the paper; larval sex is unknown;".
- `note` (uncounted): replace "The page tool returned the Abstract sentence whole." with "The page prints 're 1 µPa' with a space in this sentence (the preceding Abstract sentence prints 're1')."

Values marked "(tool summary)" above and reused here (line 2's 69/12/3 sensilla; line 3's zone statistics; line 4's 48 h holding and dilutions; line 5's n = 3 neuromast-free larvae, no ablation, 67 against 62) should be confirmed against the page text when the desk applies them.

## Unchecked

- Name authorities for all four species (not looked up; unit-brief authority not consulted).
- Line 1: Figure 2B values; sensilla per sex for the 187 contacted.
- Line 2: the sex distribution of IAc6 neurons (not printed in the text read; Figure 4B not read).
- Line 3: Figure 2 values; the frame rate of the tablet screen (not reported, as the record says).
- Line 4: Brown and Smith (1998) preparation details (record's wording not checked against the page).
- Line 5: the MANOVA statistics and the 7.4 and 6.5 dB medium-versus-small differences in the record's conditions (not re-read); the Tamales/Tomales spelling.

## Owner questions (the unit's, answered)

- Reassembled quotes: line 2's quote is a short Results sentence read whole and is not reassembled; the progress note's mention of record 2 among long Abstract sentences is wrong for this record. Records 7 to 9 are audit 320's.
- Neolamprologus pulcher laboratory stock at species rank: accepted, as filed; colony origin (five laboratory generations; predators first-generation from wild-caught fish) is in conditions.

## Progress note

Accurate on citations, licences, quote wording (one spacing slip) and duplicates. The Records list carries the faults above: Ips IAc6 given IAc5's sex and abundance; Neolamprologus without the attack-versus-calm nulls; Trypodendron without its 73 silent sensilla; Porichthys without the lateral-line caveat.
