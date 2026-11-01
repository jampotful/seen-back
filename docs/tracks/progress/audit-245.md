# audit-245: desk-d160 (12 evidence records, no search records, no wanted lines)

Audited 30 October 2026 from the desk-d160 files present untracked in the worktree (progress note and 12 evidence lines; neither is committed here, neither was edited). `tools/senses/check.py` on the evidence file: 12 records, 0 problems. The unit wrote no searched or wanted file, so there is nothing for `screen_candidates.py --check` and no sample to draw; all 12 records were judged. Quote lengths (whitespace words as check.py counts, `len(q.split())`), lines 1 to 12: 22, 27, 16, 26, 35, 24, 32, 25, 25, 34, 37, 20, all within 40. Evidence judged under oa-audit.md, "Scientific context and counting (29 October 2026)", the oa-read.md quote rule and the licence rule, in the form of audits 241 to 244. 7 WebSearch and 15 WebFetch calls used.

Sources opened: pmc.ncbi.nlm.nih.gov/articles/PMC5844528 (Vetter et al., three fetches); faculty.lsu.edu/maruskalab/.../31_burtoni_uses_acoustic_communication... .pdf (Maruska et al., the authors' lab copy of the PLOS article); frontiersin.org/articles/10.3389/fmars.2023.1135310/full (Zhu et al.); www.peerj.com/articles/14230 (two fetches); doaj.org article pages for the PeerJ, PLOS (Vetter) and Frontiers papers; researcharchive.calacademy.org Catalog of Fishes pages (spid=38518, genid=2567); bie.ala.org.au for Astatotilapia burtoni and Hypophthalmichthys molitrix; gbif.org/species/2362486; aquaticrepublic.com/hypophthalmichthys_nobilis. Not reached: api.crossref.org/works for all four DOIs (permission request not answered in time; not retried, so Crossref was not used for any check here); pmc.ncbi.nlm.nih.gov/articles/PMC3356291 (reCAPTCHA browser check; not worked around); the fws.gov silver carp risk-screening PDF (permission not answered; not retried). Library-catalogue mirrors returned by searches (libmast.utm.my, openaccess.library.uitm.edu.my, ebusca.uv.mx, buscaintegrada.ufrj.br) were not opened. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. WebFetch returns model summaries, so each quote was checked by submitting it for a MATCH/MISMATCH answer; points marked "(tool summary)" were not returned verbatim.

## Duplicates

Searched origin/main (2bc38ce9) docs/views (evidence, audit, audit/corrected, audit/ALL.jsonl) for the four DOIs, the five species names, the genus Hypophthalmichthys, and the synonyms Aristichthys and Haplochromis burtoni.
- Epinephelus awoara, Hypophthalmichthys (any species), Astatotilapia burtoni, Trichopsis vittata: nothing on main under any trait. None of the four DOIs is on main.
- Cyprinus carpio: only oa-7:728 to 731 (lambda_max_nm, Microspectrophotometry, all `retract` in ALL.jsonl) and the same four in recheck files. Different paper and trait; no sense_hearing record, no contradiction.
- 10.1371/journal.pone.0057588 is on main as desk-d143 lines 1 and 2 (Pseudetroplus maculatus, Steatocranus tinanti). The progress note holds it out correctly; it does not involve A. burtoni.
No repeat by species and paper under any trait.

## Citation and licence

Crossref was unreachable for this audit too, so author order and citation were checked on DOAJ and publisher or PMC pages.
- Zhu et al. 2023: Frontiers page and DOAJ: Xiangyu Zhu, Xinhai Zhang, Mingru Chen, Xiaomei Xu (order as recorded); title as recorded; Front. Mar. Sci. 10:1135310. Frontiers page states CC BY. The notes' "Crossref lists CC BY 4.0" was not checkable here (uncounted).
- Vetter et al. 2018: PMC and DOAJ: Brooke J. Vetter, Marybeth K. Brey, Allen F. Mensinger (order as recorded); PLoS ONE 13(3): e0192561, 9 March 2018; title as recorded; PMC copy states CC0 public domain dedication. `access` "open" stands.
- Maruska et al. 2012: authors' lab PDF of the article: Karen P. Maruska, Uyhun S. Ung, Russell D. Fernald (order as recorded); PLoS ONE 7(5): e37612, 18 May 2012; title as recorded (split at the colon); Creative Commons Attribution License. `access` "open" stands.
- Maiditsch and Ladich 2022: DOAJ: Isabelle Pia Maiditsch, Friedrich Ladich; PeerJ 10: e14230; title as recorded; PeerJ page states CC BY. Initials (from DOAJ, not Crossref): replace `"authors": "Maiditsch, Ladich"` with `"authors": "Maiditsch IP, Ladich F"` on lines 11 and 12, and in both notes replace "Crossref could not be reached; initials of the two authors are not printed on the page and are not given here." with "Crossref could not be reached; initials from the DOAJ record (Isabelle Pia Maiditsch, Friedrich Ladich)." Metadata, uncounted.

## Names and families

- Astatotilapia burtoni: Catalog of Fishes (spid=38518) "Valid as Astatotilapia burtoni (Günther 1894)", original Chromis burtoni, Cichlidae, Pseudocrenilabrinae; ALA "Accepted" (AFD) with Haplochromis burtoni and Chromis burtoni as synonyms. Accepted; the desk's unconfirmed status is now confirmed.
- Hypophthalmichthys molitrix: ALA "Accepted" (Cypriniformes, Cyprinidae). Catalog of Fishes genus page (genid=2567): "Valid as Hypophthalmichthys Bleeker 1860", Xenocyprididae, type species Leuciscus molitrix. Not a synonym.
- Hypophthalmichthys nobilis: GBIF backbone primary entry (Cypriniformes, Cyprinidae) with Aristichthys nobilis and Leuciscus nobilis under "Synonyms"; no page opened prints the word "accepted"; no source names it a synonym. Not an error; status word still unconfirmed.
- Cyprinus carpio: ACCEPTED EXACT, 4286975 in docs/views/gaps/gbif-names.tsv on main.
- Epinephelus awoara, Trichopsis vittata: not independently checked (desk's mybis.gov.my "Accepted" stands as the desk's source).
- Families: Cyprinidae for Hypophthalmichthys follows GBIF and the five Cyprinidae records on main (all Cypriniformes); Catalog of Fishes places the genus in Xenocyprididae, which the notes already say. Cichlidae order: lines 8 to 10 give Perciformes, but every Cichlidae record on main (desk-d143 and others, 4 records) gives Cichliformes; replace `"order": "Perciformes"` with `"order": "Cichliformes"` on lines 8 to 10 for consistency (uncounted). Osphronemidae under Perciformes (lines 11, 12) not checked against Catalog of Fishes (uncounted, unverified).

## Checks per paper

Zhu et al. 2023 (lines 1 to 3). All three quotes MATCH, each a whole sentence. Values match: 92, 90, 94 dB at 100, 200, 300 Hz; best 200 Hz, 90 dB re 1 µPa; 12 frequencies 100 Hz to 2 kHz; 10 fish; 22 °C holding; recording temperature not stated; n per frequency not stated; particle motion not measured (hydrophone near the inner ear for sound pressure). Uncounted fault, identical on all three lines: `conditions` says "Per-frequency n and anaesthesia are not stated", but the Methods report MS-222 (printed as "MS-2-2-2", concentration given as 20 g/L in one place and 20 mg/L in another) and gallamine triethiodide injected at the dorsal-fin base as a muscle relaxant (tool summary). Left uncounted because all three records already file the values as physiological ABR thresholds, not behavioural hearing, and no value depends on the drug; but the statement is false and should be fixed before merge: replace "Per-frequency n and anaesthesia are not stated." with "Fish were anaesthetised with MS-222 (concentration printed as both 20 g/L and 20 mg/L) and given gallamine triethiodide as a muscle relaxant; per-frequency n is not stated." Also harmless: the capture site is Gulangyu Island, Xiamen (Methods); the abstract's "Taiwan Strait" covers it. Line 3's note says thresholds above 300 Hz appear only in Figure 5; the text also says they exceed 100 dB, with a 13 dB step from 300 to 400 Hz (harmless).

Vetter et al. 2018 (lines 4 to 7). Quotes: line 4 MATCH (whole Results sentence); line 5 MATCH (whole final Abstract sentence); line 6 MATCH (whole Results sentence); line 7 MATCH, starts a Methods sentence, the marked cut drops "therefore, subsequent fish were only tested using frequencies from 100 Hz to 5 kHz." Values match Table 1 and the text: silver 80.6 ± 3.3 (Results; 3.29 in Abstract), bighead 90.5 ± 5.75 (Abstract; 5.8 in Results and Table 1), common carp 400 Hz 96.0 ± 9.2. n 5, 5, 3; 19-22 °C; MS-222 0.005%, pancuronium 0.001%; 350 L tank; 50 ms bursts, 500 repetitions, 3 dB steps all confirmed. Two context facts the records omit or misstate:
1. "The common carp were only tested at 100, 200, 400, 600, 800, 1000, 2000, 4000, and 5000 Hz" (Methods; matches Table 1). The shared `conditions` say the stimulus set was 100 Hz to 9 kHz with most fish tested 100 Hz to 5 kHz, which is wrong for common carp.
2. Stimulus levels at 6 to 9 kHz were 140 to 149 dB re 1 µPa SPLrms; the paper says levels above 150 dB were not possible "given the constraints of tank size and speaker output", and that further work "could examine sensitivity to frequencies > 5 kHz at sound pressure levels above 150 dB re 1 μPa SPLrms in both carp species" (tool summary).

Line 6 (scientific-meaning: applicability and comparison). The record files "lowest threshold at 400 Hz" for common carp under conditions that imply the same 100 Hz to 5 kHz set as the other species. Common carp were not tested at 300 or 500 Hz, so the 400 Hz minimum is the best of nine sparse frequencies and cannot be read against the 500 Hz minimum of silver and bighead carp, which a reader of three side-by-side records would do. The note compounds this: "Silver carp thresholds were significantly lower than those of common carp at seven frequencies between 500 Hz and 3 kHz", but of 500, 600, 700, 900, 1000, 1500 and 3000 Hz common carp were tested only at 600 and 1000 Hz; the paper's sentence pools bighead and common carp. Counted.

Line 7 (scientific-meaning: a null bounded by stimulus level). The genus record files "no responses to frequencies > 7 kHz to 9 kHz" and says the upper hearing limit is bounded by the 9 kHz top of the stimulus set, without saying the 6 to 9 kHz tones reached only 149 dB re 1 µPa and the speaker could not exceed 150 dB, which the authors name as the reason higher-frequency hearing is untested. The null is a level-limited null; read without that, it states an upper frequency limit the paper does not claim. Counted. Grade g and genus rank are right: the sentence pools "the first three silver and bighead carp" and the tool summary confirms it does not say three of each or three in all. The species-rank lines 4 and 5 are legitimately separate: they rest on per-species means (n = 5 each, Table 1) at 500 Hz, not on the pooled first tests, and neither claims an upper limit, so the genus record does not double-count them.

Lines 4 and 5: the conditions misstatement concerns only the common carp and the level ceiling bears only on the high-frequency null, so the 500 Hz minima stand; uncounted, but the shared `conditions` must be replaced on all four lines so the paper's limiting context is carried identically. Line 4's note repeats the paper's pooled sentence correctly; the added clause below is optional. Line 4's acceleration unit "1 m/s2" is the paper's "1 ms-2" (harmless).

Maruska et al. 2012 (lines 8 to 10). Lines 8 and 9 MATCH, whole sentences. Line 10 starts a sentence; the marked cut replaces the statistics parenthetical "(between-subject factor, F(1,14)= 7.22, p= 0.018; 600 Hz, p= 0.019; 700 Hz, p =0.001; 800 Hz, p =0.044)" and its following comma; "p>0.05" prints as "p.0.05" in the PDF text layer (extraction loss, not wording). Values match. Methods confirmed: four groups of 8; 28 °C housing; ice-cold water and 0.1% benzocaine then pancuronium; tank 30 cm diameter, 36.5 cm high, fish 14 cm above the speaker; 20 ms pulses, 2000 repetitions, 5 dB steps; the 11 frequencies as recorded; maximum level not given. Female result in line 10's note (gravid about 5-15 dB lower at 100-600 Hz, no difference at 700 Hz and above) confirmed. Uncounted: the authors say particle motion was not characterised and that sound-pressure referencing serves audiogram shape and relative differences only (tool summary); the records' "Sound-pressure thresholds (dB re 1 µPa)" carries the reference but not that limit. Optional addition to the shared `conditions` after "Sound-pressure thresholds (dB re 1 µPa)": "; particle motion was not characterised, and the authors use sound-pressure thresholds for audiogram shape and relative group differences."

Maiditsch and Ladich 2022 (lines 11 and 12). Line 11 MATCH; the marked cut drops the trailing "(Tables 1, 2, Fig. 2)." Line 12 MATCH, whole abstract sentence. Values match Table 1 (85.5 and 108.7 dB; shifts 11.7, 11.9, 12.0, 18.4, 13.2, 15.6 dB). Ten adult females (ovary), SL 38.8-47.3 mm, 25 ± 1 °C, six frequencies, white noise 110 dB re 1 µPa RMS, lab ambient 91 dB, n 10 quiet and 7-10 in noise all confirmed. Noted, not counted: the paper reports an overall noise effect and a noise × frequency interaction, not per-frequency tests, and some Table 1 differences do not equal the difference of the listed means (unequal n); the record follows the abstract sentence and does not overstate it.

## Per record

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Epinephelus awoara, 100-300 Hz | ok | (conditions, uncounted) | Quote MATCH; values right; "anaesthesia not stated" is false (fix required, see above) |
| 2 | Epinephelus awoara, best 200 Hz, 90 dB | ok | (conditions, uncounted) | Abstract sentence MATCH; same conditions fix |
| 3 | Epinephelus awoara, curve to 2000 Hz top | ok | (conditions, uncounted) | Quote MATCH; top of set stated; same conditions fix |
| 4 | Hypophthalmichthys molitrix, 500 Hz, 80.6 dB | ok | (conditions, uncounted) | Quote MATCH; Table 1 value; shared conditions wrong for common carp only |
| 5 | Hypophthalmichthys nobilis, 500 Hz, 90.5 dB | ok | (conditions, uncounted) | Abstract MATCH; per-species n = 5, separate from pooled first tests |
| 6 | Cyprinus carpio, 400 Hz, 96.0 dB | error, fixable | conditions, value, note | Common carp tested at only nine frequencies (no 300 or 500 Hz); note attributes seven-frequency comparisons to common carp it was not tested at (scientific-meaning: applicability) |
| 7 | Hypophthalmichthys (genus), no AEP > 7 kHz | error, fixable | conditions, value, note | Null at 6-9 kHz only up to 149 dB, speaker ceiling 150 dB, authors call for higher-level tests; record bounds the limit by frequency only (scientific-meaning: null limited by stimulus level) |
| 8 | Astatotilapia burtoni, best 200-300 Hz | ok | (order, uncounted) | Quote MATCH; all-group mean stated |
| 9 | Astatotilapia burtoni, 15-25 dB difference | ok | (order, uncounted) | Quote MATCH; 2000 Hz top of set stated |
| 10 | Astatotilapia burtoni, social status null | ok | (order, uncounted) | Cut marked, sentence start; null and female results right |
| 11 | Trichopsis vittata, best 1.5 kHz | ok | (authors, uncounted) | Quote MATCH, trailing citation cut marked; 4 kHz top stated |
| 12 | Trichopsis vittata, 12-18 dB masking | ok | (authors, uncounted) | Abstract MATCH; noise level and n stated |

Evidence errors: 2 of 12 (16.7%). Scientific-meaning faults 2 (lines 6, 7); quote-form faults 0. Licence faults: none. Name faults: none (no synonym). Duplicates: none. Units: Hz, kHz and dB re 1 µPa used correctly throughout; no kHz/Hz garbling.

## Replacement text (exact)

Lines 4 to 7, `conditions` (required on 6 and 7, and on 4 and 5 so the paper's context is carried identically): replace "tone bursts of 50 ms, 500 repetitions, 100 Hz to 9 kHz in the stimulus set, levels lowered in 3 dB steps;" with "tone bursts of 50 ms, 500 repetitions, levels lowered in 3 dB steps; silver and bighead carp were tested from 100 Hz to 9 kHz until the first three fish, then only from 100 Hz to 5 kHz; common carp were tested only at 100, 200, 400, 600, 800, 1000, 2000, 4000 and 5000 Hz;" and replace "Most fish were tested only from 100 Hz to 5 kHz." with "Stimuli at 6-9 kHz reached 140-149 dB re 1 µPa SPLrms; the tank and speaker could not exceed 150 dB."

Line 6, `value`: "lowest threshold at 400 Hz, 96.0 ± 9.2 dB re 1 µPa SPLrms, among nine tested frequencies (300 and 500 Hz not tested)".

Line 6, `note`: replace "Silver carp thresholds were significantly lower than those of common carp at seven frequencies between 500 Hz and 3 kHz." with "The paper reports silver carp thresholds significantly lower than those of bighead and common carp at 500, 600, 700, 900, 1000, 1500 and 3000 Hz; common carp were tested at only 600 and 1000 Hz of these and not at 500 Hz, so their 400 Hz minimum cannot be compared with the 500 Hz minimum of the other two species."

Line 6, `where`: "Results, common carp; Methods (common carp frequency set)".

Line 7, `value`: "no AEP above 7 kHz up to 9 kHz and inconsistent AEP from 5 to 7 kHz in the first three fish, at stimulus levels up to 149 dB re 1 µPa SPLrms (150 dB was the equipment limit); later fish tested only to 5 kHz".

Line 7, `note`: replace "so the upper hearing limit is bounded by the 9 kHz top of the stimulus set (and, for most fish, by 5 kHz)." with "so the upper hearing limit is bounded by the 9 kHz top of the stimulus set (for most fish by 5 kHz) and by the 149 dB maximum stimulus level at 6-9 kHz; the authors suggest testing frequencies above 5 kHz at levels above 150 dB re 1 µPa SPLrms in both species, so the null is not an upper hearing limit."

Line 7, `where`: "Methods, stimulus frequencies; Discussion (stimulus-level limit above 5 kHz)".

Line 4, `note` (optional, uncounted): after "...1500 and 3000 Hz;" add " common carp were tested at only 600 and 1000 Hz of these;".

Lines 1 to 3, `conditions` (uncounted, fix before merge): see Zhu et al. above.

Lines 8 to 10, `order` (uncounted): "Cichliformes".

Lines 11 and 12, `authors` and note (uncounted): see Citation and licence.

## Faults noted, not counted

- Lines 1 to 3: "anaesthesia are not stated" is false (MS-222 and gallamine).
- Lines 1 to 3: "Crossref lists CC BY 4.0" not checkable here (Crossref unreachable); the Frontiers page states CC BY.
- Lines 4 and 5: shared conditions misstate the common carp frequency set (fixed by the required replacement).
- Lines 8 to 10: order Perciformes against Cichliformes on every Cichlidae record on main; particle motion not characterised (authors' statement) not carried.
- Lines 11 and 12: author initials missing (IP, F from DOAJ).
- Lines 11 and 12: order Perciformes for Osphronemidae not checked.
- Progress note: A. burtoni and H. molitrix status now confirmed (Catalog of Fishes valid; ALA Accepted); H. nobilis still lacks a printed "accepted" but is not a synonym anywhere opened.

Search records: none in the unit (0 of 0). Wanted lines: none. Held-out leads in the progress note were not searched.

Pooled with audits 172 to 244: 146 of 344 evidence records (42.4%; audits 172 to 244 144 of 332 as audit 244 gives it, audit 245 2 of 12).

Verdict: lines 1 to 5 and 8 to 12 can be merged as they stand once the uncounted fixes the desk accepts are applied (the Zhu anaesthesia sentence and the shared Vetter conditions should be fixed; order and initials are optional). Lines 6 and 7 can be merged only with the replacement text above; a flagged scientific-meaning fault must be corrected before acceptance. Error line numbers: 6, 7.

No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page opened; no paper text committed beyond single sentences and short phrases quoted for verification. The desk-d160 copies stay untracked and unedited. This report is model output and carries no authority.
