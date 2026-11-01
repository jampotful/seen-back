# audit-246: desk-d161 (8 evidence records, no search records, no wanted lines)

Audited 30 October 2026 from the desk-d161 files present untracked in the worktree (progress note and 8 evidence lines; neither is committed here, neither was edited). `tools/senses/check.py` on the evidence file: 8 records, 0 problems. The unit wrote no searched or wanted file, so there is nothing for `screen_candidates.py --check` and no sample to draw; all 8 records were judged. Quote lengths (whitespace words as check.py counts, `len(q.split())`), lines 1 to 8: 32, 26, 39, 24, 18, 37, 36, 39, all within 40. Evidence judged under oa-audit.md, "Scientific context and counting (29 October 2026)", the oa-read.md quote rule and the licence rule, in the form of audits 241 to 245. 4 WebSearch and 18 WebFetch calls used (5 of the fetches refused, redirected or unanswered).

Sources opened: api.crossref.org/works for all three DOIs (uppercase form; the first eel fetch was rate-limited and the retry succeeded); pmc.ncbi.nlm.nih.gov/articles/PMC4414586 (Tian et al., two fetches); www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0059212 (Durif et al., the PLOS journal page, two fetches); pmc.ncbi.nlm.nih.gov/articles/PMC4433231 (Landler et al.); gbif.org/species/7261805; treatment.plazi.org (a redirect page only, nothing read); reptile-database.reptarium.cz/Chelydra/serpentina. Not reached: doi.org/10.1371/journal.pone.0059212 and pmc.ncbi.nlm.nih.gov/articles/PMC3598651 (permission requests not answered in time; not retried); api.gbif.org species match for Nyctalus plancyi and Chelydra serpentina (permission not answered; curl gave a proxy 403; not retried). The Mammal Diversity Database was not opened. Library-catalogue mirrors returned by searches (openaccess.library.uitm.edu.my, vufind.lboro.ac.uk, ebusca.uv.mx) were not opened. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. WebFetch returns model summaries, so each quote was checked by submitting it for a MATCH/MISMATCH answer; points marked "(tool summary)" were not returned verbatim.

## Duplicates

Searched origin/main (e73186bb) docs/views (evidence, audit, audit/corrected, audit/ALL.jsonl, gaps) for the three DOIs (by article number), the three species, the genera, and the first authors Tian, Durif and Landler.
- Nyctalus: only N. noctula and N. leisleri in gaps/try-species.json; no evidence or audit record for any Nyctalus species.
- Anguilla anguilla: only cff_hz records (methods:222, canon-3:685, oa-3:216, oa-6:185 and 687, recheck-22-fixed:1, with their audit and corrected copies). Different papers and trait; no sense_magnetic record, no contradiction.
- Chelydra serpentina: only gaps cells and queue rows (inferred visual traits) and a mention in drafts/herps-met.md; no evidence record.
- None of the three DOIs is on main. "Landler" matches only desk-d144 lines 7 and 8 (Bufo bufo, Landler and Gollmann 2011, Frontiers in Zoology), another paper and species.
No repeat by species and paper under any trait.

## Citation and licence (Crossref reached)

- Tian et al. 2015: Crossref: Lan-Xiang Tian, Yong-Xin Pan, Walter Metzner, Jin-Shuo Zhang, Bing-Fang Zhang (order and initials as recorded, "Tian LX, Pan YX, Metzner W, Zhang JS, Zhang BF"); title "Bats Respond to Very Weak Magnetic Fields" verbatim; PLOS ONE 10(4): e0123205, published 2015-04-29; licence http://creativecommons.org/licenses/by/4.0/. The PMC page prints the Creative Commons Attribution License statement. `access` "open" stands.
- Durif et al. 2013: Crossref: Caroline M. F. Durif, Howard I. Browman, John B. Phillips, Anne Berit Skiftesvik, L. Asbjørn Vøllestad, Hans H. Stockhausen (order and initials as recorded); title verbatim; PLoS ONE 8(3): e59212, 2013-03-15; licence CC BY 4.0. The PLOS journal page prints "distributed under the terms of the Creative Commons Attribution License". `access` "open" stands.
- Landler et al. 2015: Crossref: Lukas Landler, Michael S. Painter, Paul W. Youmans, William A. Hopkins, John B. Phillips (order and initials as recorded); title verbatim; PLOS ONE 10(5): e0124728, 2015-05-15; licence CC BY 4.0. The PMC page (PMC4433231) does print "This is an open-access article distributed under the terms of the Creative Commons Attribution License" (tool summary, in segments), so the desk's statement that the PMC page carried no licence line is wrong for the copy I opened. The PLOS journal page itself (journals.plos.org) was not returned by any search and was not opened; the CC BY statement rests on Crossref and PMC. `access` "open" stands. Uncounted metadata fix on lines 7 and 8: replace `"url": "https://vtechworks.lib.vt.edu/handle/10919/75069"` with `"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4433231"`, and in both notes replace "Licence: PLOS ONE article read on the PMC page; the explicit CC BY 4.0 statement was found on the Virginia Tech repository record of the article (url), the PMC page text carried no licence line." with "Licence: PLOS ONE article read on the PMC page, which states the Creative Commons Attribution License; Crossref gives CC BY 4.0."
- Progress note: "Crossref was unreachable" holds for the desk; all three DOIs, author orders and volume/issue/article numbers are now confirmed on Crossref.

## Names

- Nyctalus plancyi: GBIF 7261805 (GBIF Backbone, citing MSW3 and HMW vol. 9) lists it at species rank in Vespertilionidae, Chiroptera, with no synonym and no subspecies listed; "velutinus" appears only inside an English vernacular entry. No page opened prints the word "accepted"; no source names it a synonym. MDD not opened. Not an error; status word still unconfirmed (as the desk said).
- Anguilla anguilla: ACCEPTED EXACT, 5212973 in docs/views/gaps/gbif-names.tsv on main. Catalog of Fishes not opened.
- Chelydra serpentina: Reptile Database "Chelydra serpentina (LINNAEUS, 1758)", Chelydridae, Testudines, subspecies field blank, the former subspecies serpentina and osceola in its synonymy; the page notes that most former subspecies are now considered valid species without naming them here; that the Virginia turtles of Landler et al. belong to C. serpentina in the current sense is my inference, not checked on a range page. Accepted; no synonym problem.
- Families and orders on all lines agree with these sources.

## Checks per paper

Tian et al. 2015 (lines 1 to 3). Quotes: line 1 MATCH (whole Abstract sentence); line 2 MATCH (whole Results sentence); line 3 MATCH, sentence start, the marked cut drops "which did not allow us to determine preferred roosting angle." Table 1 confirmed: GMF 394, 25 degrees, r 0.53; 1/3rd 451, 21, 0.50; 1/4th 433, 25, 0.62; 1/5th 466, 27, 0.47; reversed GMF 454, 162, 0.52; reversed 1/5th 462, 158, 0.56; all p<0.001. Field strengths 51, 17, 13, 10 μT and reversed 51 and 10 μT; one group of six males throughout ("we used a group of six individuals (all males) in all conditions tested"); 30 cm basket, 1.5 m tri-axial Helmholtz coils, 72 sectors, 30 min logging, March to October 2013, local field 51 μT, all confirmed. The authors describe the roosting response as a polarity compass (tool summary), which the polarity reversals at 51 and 10 μT bear out; the records' "magnetic direction sense" is compatible.

Two context facts the records misstate or omit:
1. "Hence, we began data collection on the 4th exposure day and continued for the subsequent 10 days" (Results, 1/5th conditions). At 10 μT the bats roosted at random for three days before any preference appeared, so the 10 μT orientation in Table 1 is the result of days 4 to 13 of exposure. The shared `conditions` say only "each field condition run for 10 consecutive days".
2. Neither "adult" nor any statement of age appears in the paper (MATCH query answered no); the bats were collected "at the end of September of 2012", six males with mean body length 8.6 cm and mass 31.5 g (tool summary). The shared `conditions` say "Captive adult males".

Line 1 (scientific-meaning: omitted null that limits the effect, applicability). The record files "roosts at magnetic north in a 10 μT field" with no word that the bats were disoriented for the first three days at that strength and that the preference was measured only from day 4. That is an explicit exception the paper reports in the same experiment, and it changes what "responds to 10 μT" means (after exposure of several days, not on first exposure). Line 3 carries it, but oa-audit.md asks for the limitation in the same record. Counted.

Line 2: at full 51 μT, where no acclimation phase is reported; value and note right. Uncounted: shared `conditions` ("adult").

Line 3: value, quote and note right; the note states that Table 1 describes the later days. Uncounted: shared `conditions` ("adult", and "10 consecutive days" contradicts the record's own value at 10 μT).

Durif et al. 2013 (lines 4 to 6). Quotes: line 4 MISMATCH in one character: the PLOS page prints "µ = 331°" where the record has "m= 331°" (a symbol-font loss in a PDF text layer, I infer; spacing differences ignored); line 5 MATCH, whole Abstract sentence (Results gives the same finding as an axis of 97 to 277 degrees); line 6 MATCH, whole Results sentence. Statistics confirmed: below 12 °C 331°, r 0.46, n 31, p 0.001; 12 to 17 °C unimodal r 0.25, n 22, p 0.25, axial 97 to 277°, r 0.40, n 22, p 0.027; geographic-north control p 0.56 and 0.83; 53 tests (14, 13, 14, 12), each eel tested once, April to October 2010 in daytime, complete darkness under IR, 1.40 m test tank, "most of these eels were at the yellow stage, but some individuals showed signs of silvering", no stage difference (p>0.5), outdoor holding tanks with shelter pipes, eels moved to the test facility at least two days before testing (tool summary). The temperature split is on training-tank temperature in the Results ("significantly correlated with water temperature in the training tanks"); the Discussion speaks of "testing tank temperatures (6–11°C)" and the test tank was 1 to 2 °C warmer, so the paper is inconsistent on which tank; the records follow the Results (harmless).

Line 4 (scientific-meaning: reference frame of the direction). The record's value says the eels oriented "relative to magnetic north: mean 331 degrees", and its note says 331 degrees "is in magnetic-bearing terms after rotating each exit direction by the field alignment". The paper recalculated exit directions "relative to the direction of the artificial magnetic north" and then "Bearings were also standardized according to the direction of their displacement away from the holding tank"; the two training tanks lay on opposite sides of the test building (displacement c. 360° for tank 1, c. 180° for tank 2). So 331° is a bearing relative to the displacement direction set at 360°, not a magnetic bearing; read as filed, half the eels (tank 2) are given the opposite meaning. Counted.

Line 5: the bimodal axis and the failed unimodal test are carried in the note with r and n; value right. Line 6: control carried correctly. Uncounted on lines 4 to 6 (shared `conditions`): "about 51 μT, ambient inclination" can be the paper's 50.3 to 51 μT and 73 degrees; tests below 6 °C gave no results ("eels showed no or very little movement at temperatures <6°C and those tests yielded no results"), which the "6 to 17 C" span does not say.

Landler et al. 2015 (lines 7 and 8). Quotes: line 7 MATCH with three marked cuts ("and subsequently tested in the four magnetic field alignments without RF"; "relative to the magnetic field with the mean vector bearing"; "Moore's modified Rayleigh test, Fig 1"); line 8 MATCH, one marked cut ("Moore's modified Rayleigh test"). Values confirmed: 353°, p<0.005, R* 1.388, n 18; 196°, p<0.01, R* 1.307, n 18. Other sequences: RF off→on R* 0.121 n.s.; RF on→off R* 0.674 n.s. (both n 18). Eggs from wild females in the South River and Middle River, Virginia, collected April to July 2011; hatchlings emerged August to September 2011; five months of hibernation; tested within a month of emergence in May 2012; six turtles per session; Faraday cage; full-spectrum light; 51.24 μT, 64.3°; 1.430 MHz at 30 to 52 nT; last 40 min scored on 36 frames; vertical-field control random (tool summary). The authors call the behaviour spontaneous magnetic alignment (untrained body alignment), not a navigational compass, and read the RF result as "consistent with the involvement of a radical pair mechanism" and as altering "rather than elimination of magnetic input altogether"; the records' `eye` ("spontaneous magnetic alignment, radical-pair test") and line 8's note say the same. Uncounted: "the same animals" in line 8's quote are the turtles first exposed with RF on, a different 18 from line 7's (six turtles a day over six days, three days starting with RF on; the total of 36 is inferred from the design, not stated); line 8's value already names the RF-on-first sequence, so the quote is not misread from the record alone. Optional note addition below.

## Per record

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Nyctalus plancyi, magnetic north at 10 μT | error, fixable | value, conditions, note | Quote MATCH; omits that the bats roosted at random for the first three days at 10 μT and that Table 1 covers days 4 to 13 (scientific-meaning: omitted exception limiting applicability) |
| 2 | Nyctalus plancyi, reversal at 51 μT | ok | (conditions, uncounted) | Quote MATCH; Table 1 values right; "adult" unsupported |
| 3 | Nyctalus plancyi, random first three days at 10 μT | ok | (conditions, uncounted) | Sentence start, trailing cut marked; "adult" and "10 consecutive days" in shared conditions to fix |
| 4 | Anguilla anguilla, 331° below 12 °C | error, fixable | value, note, (quote, uncounted) | 331° is relative to the displacement direction after standardization, not to magnetic north (scientific-meaning: reference frame); quote prints "m=" for "µ =" |
| 5 | Anguilla anguilla, bimodal at 12-17 °C | ok | (conditions, uncounted) | Abstract MATCH; axis, unimodal null, r and n in note |
| 6 | Anguilla anguilla, geographic control random | ok | (conditions, uncounted) | Results MATCH; control right |
| 7 | Chelydra serpentina, RF off→off 353° | ok | (url, note, uncounted) | Quote MATCH with marked cuts; disoriented sequences carried; licence note wrong about PMC |
| 8 | Chelydra serpentina, RF on→on 196° | ok | (url, note, uncounted) | Quote MATCH; "same animals" is the RF-on-first group; licence note as line 7 |

Evidence errors: 2 of 8 (25.0%). Scientific-meaning faults 2 (lines 1, 4); quote-form faults counted 0 (line 4's one-character symbol fault is uncounted, see below). Licence faults: none (all three CC BY; `access` "open" stands on every line). Name faults: none (no synonym; N. plancyi status word unconfirmed). Duplicates: none. Units: μT, degrees, r, R*, n, p and °C used correctly throughout.

## Replacement text (exact)

Line 1, `value`: "roosts at magnetic north (Table 1: mean 27 degrees, r 0.47) in a 10 μT field, one-fifth of the local 51 μT field, after roosting at random for the first three days at this strength; the preference was measured on days 4 to 13 of exposure; 10 μT was the lowest strength tested, nothing was tested below it".

Line 1, `note`: replace "The same paper also tested 17 μT and 13 μT (preference for magnetic north, p<0.001 each)." with "The same paper also tested 17 μT and 13 μT (preference for magnetic north, p<0.001 each). At 10 μT the bats roosted at random for the first three experimental days, and data collection began on the 4th exposure day (Results); with polarity reversed at 10 μT they roosted at 158 degrees (r 0.56), so the response follows field polarity, which the authors call a polarity compass."

Line 1, `where`: "Abstract; Results (1/5th field strength, data from the 4th exposure day)".

Lines 1 to 3, `conditions` (required on line 1, and on 2 and 3 so the paper's context is carried identically): replace "Captive adult males collected at a temple in Tianjin in September 2012," with "Captive males (age not stated; mean body length 8.6 cm, mass 31.5 g) collected at a temple in Tianjin at the end of September 2012," and replace "each field condition run for 10 consecutive days;" with "each field condition run for 10 consecutive days of recording, except that at 1/5th strength (10 μT, normal and reversed) the bats roosted at random for the first three days and recording ran from the 4th exposure day for the next 10 days;".

Line 4, `value`: "eels from training tanks below 12 C oriented in the direction of their displacement from the training tank: mean 331 degrees on bearings standardized so that the displacement direction is 360 degrees, r 0.46, n 31, p 0.001".

Line 4, `note`: replace "The orientation is relative to the magnetic field alignment, so the mean 331 degrees is in magnetic-bearing terms after rotating each exit direction by the field alignment." with "Exit directions were recalculated relative to the artificial magnetic north and then standardized to the direction of displacement away from the holding tank; the two training tanks lay on opposite sides of the test building (displacement c. 360 and c. 180 degrees), so 331 degrees is a bearing relative to the displacement direction, not to magnetic north."

Line 4, `quote` (uncounted, fix before merge): replace "(Fig. 4A; m= 331°, r= 0.46, n = 31, p = 0.001)." with "(Fig. 4A; µ = 331°, r = 0.46, n = 31, p = 0.001)." as the PLOS page prints it.

Lines 4 to 6, `conditions` (uncounted, recommended): replace "(about 51 μT, ambient inclination)" with "(50.3 to 51 μT, inclination 73 degrees)" and replace "water temperature in the training tank 6 to 17 C;" with "water temperature in the training tank 6 to 17 C (tests below 6 C yielded no results, the eels showing no or very little movement; the test tank was 1 to 2 C warmer than the training tank);".

Lines 7 and 8, `url` and licence note (uncounted): see Citation and licence.

Line 8, `note` (optional, uncounted): add "'The same animals' in the quote are the turtles first exposed with RF present, not those of the RF off → RF off record; six turtles were tested per day and n is 18 per initial-exposure group."

## Faults noted, not counted

- Lines 2 and 3: "adult" unsupported (no age stated); "10 consecutive days" misdescribes the 10 μT conditions (fixed by the required conditions replacement).
- Line 4: "m=" for "µ =" in the quote (one-character extraction loss, value unaffected).
- Lines 4 to 6: field inclination given as "ambient"; tests below 6 °C yielded no results; training-tank versus test-tank temperature inconsistency in the paper itself.
- Lines 7 and 8: licence note says the PMC page carries no licence line, but it does; url is a repository record where the PMC copy read is available.
- Progress note: Crossref now confirms all three citations; "Auditors may treat this paper as licence-uncertain" no longer applies (Crossref and PMC both give CC BY).

Search records: none in the unit (0 of 0). Wanted lines: none. Held-out leads in the progress note were not searched.

Pooled with audits 172 to 245: 148 of 352 evidence records (42.0%; audits 172 to 245 146 of 344 as audit 245 gives it, audit 246 2 of 8).

Verdict: lines 2, 3 and 5 to 8 can be merged as they stand once the uncounted fixes the desk accepts are applied (the shared Tian conditions and the line 4 quote character should be fixed; the eel conditions, turtle url and licence note are recommended). Lines 1 and 4 can be merged only with the replacement text above; a flagged scientific-meaning fault must be corrected before acceptance. Error line numbers: 1, 4.

No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page opened; no paper text committed beyond single sentences and short phrases quoted for verification. The desk-d161 copies stay untracked and unedited. This report is model output and carries no authority.
