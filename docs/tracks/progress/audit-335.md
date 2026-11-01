# audit-335: desk-d241, evidence lines 1 to 5

Audited 31 October 2026 from the desk-d241 files present untracked in the worktree (docs/tracks/progress/desk-d241.md and docs/views/evidence/desk-d241.jsonl, 9 lines; neither committed here, neither edited). Lines 6 to 9 are audit 336's. HEAD and origin/main 1d7f41c5 (desk-d240). `python3 -I tools/senses/check.py | grep 'd241\.'`: "docs/views/evidence/desk-d241.jsonl: 9 records, 0 problems". Quote lengths (`len(q.split())`): 28, 19, 16, 35 and 17 words, all within 40. Evidence records only; audits 333 and 334 are the format model and the desk-audit.md evidence clause applies (40-word limit, no 125-character limit). Abutting pieces judged under the six conditions in audit-324.md; no cut quotes in these lines.

Sources opened (WebFetch): api.crossref.org/v1/works/ for 10.1038/srep33805, 10.1038/s41598-020-60383-x, 10.1038/srep14323 and 10.1371/journal.pone.0115291 (the last with the slash encoded; the unencoded request failed with a client error); journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0115291 (two passes, one earlier attempt rate-limited); www.nature.com/articles/srep33805 (three passes); www.nature.com/articles/s41598-020-60383-x (one pass); www.nature.com/articles/srep14323 (two passes). GBIF, WoRMS and OBIS not opened (refused per rules, or not needed). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 0 WebSearches and 11 WebFetch calls used.

## Bibliographic and licence

- Line 1. Crossref: José Augusto Pereira Carneiro Muniz, Luana Modesto de Athaide, Bruno Duarte Gomes, Barbara L. Finlay, Luiz Carlos de Lima Silveira; title as recorded; PLoS ONE 9(12), e115291; issued 2014-12-29; relation empty, no update-to. Page byline same five names in the same order. Licence: page "This is an open-access article distributed under the terms of the" "Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction"; Crossref CC BY 4.0, unspecified. Accepted (Crossref "unspecified" plus page-printed CC Attribution License). Faults 0.
- Lines 2, 3. Crossref: Susanne Schwarze, Friederike Steenken, Nadine Thiele, Dmitry Kobylkov, Nele Lefeldt, David Dreyer, Nils-Lasse Schneider, Henrik Mouritsen; "Migratory blackcaps can use their magnetic compass at 5 degrees inclination, but are completely random at 0 degrees inclination"; Scientific Reports 6 (issue 1 in Crossref, not printed on the page), 33805; issued 2016-09-26; relation empty, no update-to. Licence: page shows "Open access" and "2016 The Author(s)" with no Creative Commons sentence (tool summary); Crossref CC BY 4.0 for content-version vor. Accepted under the "no licence sentence + Crossref CC vor" rule. Faults 0.
- Line 4. Crossref: Julia Bojarinova, Kirill Kavokin, Alexander Pakhomov, Roman Cherbunin, Anna Anashina, Maria Erokhina, Maria Ershova, Nikita Chernetsov; title as recorded; Scientific Reports 10, 3473; issued 2020-02-26; relation empty, no update-to. Licence: page "This article is licensed under a Creative Commons Attribution 4.0 International License,"; Crossref CC BY 4.0 vor. Accepted. Faults 0.
- Line 5. Crossref: Bianca Alert, Andreas Michalik, Nadine Thiele, Michael Bottesch, Henrik Mouritsen; "Re-calibration of the magnetic compass in hand-raised European robins (Erithacus rubecula)"; Scientific Reports 5, 14323; issued 2015-09-21; relation empty, no update-to. Licence: page "2015 The Author(s)" and "You have full access to this open access article", no CC sentence; Crossref CC BY 4.0 vor. Accepted. Faults 0.

source.access "open" right for all five; years as printed. Bibliographic faults 0; licence faults 0.

## Names

- Alouatta caraya: gbif-names.tsv:174 EXACT ACCEPTED (usageKey 2436652); Atelidae, Primates as on main. Met.
- Sylvia atricapilla: gbif-names.tsv:4634 EXACT ACCEPTED; Sylviidae, Passeriformes as filed on main (audit/corrected/birds.jsonl:161,162). Met.
- Sylvia borin: not in gbif-names.tsv; main files it in docs/views/gaps/bird.md:809 and cells.jsonl as "Sylvia borin (Garden Warbler)", Sylviidae / Passeriformes. Name as used on main. Met (no external authority page opened; listed under unchecked).
- Erithacus rubecula: gbif-names.tsv:1775 EXACT ACCEPTED; Muscicapidae, Passeriformes as on main (corrected/birds.jsonl:160). Met.

## Duplicates

git grep on origin/main (1d7f41c5) across the whole docs/ tree (evidence, audit incl. audit/corrected and audit/ALL, sheets, searched, sources, wanted, gaps, progress, codex-findings) for the four DOIs (numeric parts), "Schwarze", "Bojarinova", "Muniz", "garden warbler" and the four species names; and a git grep of all 729 remote branches not merged into main (audit branches excluded) over docs/views/evidence, docs/views/audit and docs/views/sheets for the four DOIs.

- pone.0115291: main only desk-d239.md:14 (held lead). Alouatta caraya on main: oa-1:3551 fovea (Kopania and Clark 2025, citing a Muniz et al. 2015 secondary), oa-1:3552 orbit convergence, oa-1:3698 to 3700 retinal-specialization rows, oa-1:4230 acuity_cpd 59.61 (Veilleux and Kirk 2014, from cone density), oa-1:4231 eye axial length. No ganglion-cell density row. Not a repeat. Trait key peak_ganglion_cell_density_mm2 is on main (oa-5, oa-11, recheck-codex-b-fixed; numeric values, cells/mm2).
- srep33805: no hit. Sylvia atricapilla sense_magnetic on main: birds:161 (10.1007/s00359-021-01537-8) and birds:162 (10.1073/pnas.2301153120), radio-frequency papers. Not a repeat.
- s41598-020-60383: no hit. Sylvia borin has no species-rank evidence row on main, only gap cells; main does hold a common-name row, oa-2:4075 "garden warbler" sense_magnetic (cryptochrome antibody staining, Solov'yov et al. 2010, 10.1016/j.bpj.2010.03.053, grade g), a different finding. Not a repeat; the record's note ("main holds only visual rows for Sylvia borin") is inaccurate (uncounted note fix below).
- srep14323: no hit. Erithacus rubecula sense_magnetic on main: corrected/birds.jsonl:159 (10.1371/journal.pone.0020091, cryptochrome 1a, pooled with Gallus), 160 (10.1371/journal.pone.0043271), oa-2:4073, 4074 (10.1016/j.bpj.2010.03.053). Not a repeat; the note omits pone.0020091 (uncounted).
- The only branch hit for any of the four DOIs is origin/research/desk-d241 itself.

Duplicate faults 0.

## Trait key and grading

sense_magnetic is on main for these birds. peak_ganglion_cell_density_mm2 is on main with numeric single values; line 1 files four directional means as a string. check.py passes it and the quote supports every number, so accepted; the desk may prefer the nasal maximum (44,963) as the numeric value with the other three in conditions, owner's call (uncounted). Grade `m` right for all five (one named species measured by the authors). eye "" right.

## Quote rulings

- Line 1. Printed: "Ganglion cell density reached maximum values in the foveal slope: 44,963±3,089, 42,191±2,063, 43,825±788," "and 40,673±2,669 cells/mm2 at 0.5 mm nasal, temporal, dorsal, and ventral to the fovea, respectively." Two abutting pieces in one response, first piece ends mid-sentence, join identical to the desk's two passes, plus-minus signs as printed, 28 words. MATCH under audit-324's conditions.
- Line 2. "At 5° inclination, the birds oriented as well as they did in the normal 67° inclined field in Oldenburg." returned unbroken on two passes. MATCH.
- Line 3. "In contrast, they were completely randomly oriented in the horizontal field, showing no sign of bimodality." returned unbroken. MATCH.
- Line 4. "Extraordinarily, when the device was on, they were not disoriented either: the birds showed migratory orientation" " appropriate for autumn migratory season (α = 189°, n = 14, r = 0.49, P = 0.03; Fig. 2D)." Two abutting pieces in one response, same join as the desk's; alpha and degree signs as printed. MATCH. The trailing "Fig. 2D" is kept, so no cut.
- Line 5. "In contrast, control birds that were deprived of any natural celestial cues throughout remained unable to orient." returned unbroken. MATCH.

## Per-record findings

### Line 1, Alouatta caraya, ganglion cell density at 0.5 mm

Design verified: "Five adults, male Alouatta caraya were obtained from the breeding colony of the Centro Nacional de Primatas" "– CENP (Ananindeua, Pará, Brazil)."; "The animals were bred and kept in the CENP facilities until the day the experiment started." (captive-bred; ages not printed); "Six retinas were studied from the five animals." (AC 01L to 04L, AC 05L and 05R); "Five retinas were counted over their entire extent." and the sixth only beyond 2 to 3 mm; N = 5 for the central 3 mm plots; 12 radial directions at 30 degrees; x100 oil objective; 0.25 mm steps in the first 3 mm; perfusion with 10% formaldehyde, formaldehyde vapour at 60 C for 2 to 3 h, Nissl stain; ganglion cells told from displaced amacrines by "the abundant amount of Nissl substance in their cytoplasm."; "The mean areal shrinkage in the four retinas that were measured before and after histology was 4.8±4.3% (range: 1 to 11%)."; "There was no consistent difference in the dorsal versus ventral ganglion cell density."; no cycles-per-degree estimate.

Abstract against Results: the abstract prints "Ganglion cell density peaked at 0.5 mm between the fovea and optic nerve head, reaching 40,700–45,200 cells/mm2." Ruling: the value follows the Results sentence, which gives the four directional means with SD for the N = 5 retinas and is the quoted sentence; the abstract range is a rounded summary whose upper figure (45,200) does not match any printed mean, and the record already states the difference. No change.

**Error (shrinkage rationale misstated).** The record says "no correction was applied to densities, so densities are for shrunken tissue." The paper gives the opposite reason: "As shrinkage occurred only along retinal borders and cuts performed to flat the retinas, no corrections" "were applied for cell density estimates obtained by cell counting." The authors hold that the counted central regions were not shrunk. Uncounted: the counting-field description stops at 1.5 mm (fields enlarge to 9,604 and 38,416 µm2 further out); the dorsal-ventral "no consistent difference" sentence can be added. Fixable.

### Line 2, Sylvia atricapilla, oriented at 5 degrees as at 67 degrees

Design verified (tool summary unless quoted): 26 wild-caught blackcaps, August 2013 and 2014, within 1 km of the University of Oldenburg, two per cage in a windowless room under local photoperiod; modified aluminium Emlen funnels (35 cm, walls 45 degrees, scratch paper); huts "covered with aluminum plates on the inside, which were grounded" "and therefore acted as Faraday cages"; "the total field intensity remained the same as in the control conditions." (67 deg fields 48,600 +/- 240 and +/- 250 nT; 5 and 0 deg values only in Table 1, not read); conditions given "in a semi-random pattern"; evaluators "did not know in which cardinal direction (N, S, E or W) the overlap point had been fixed."; papers under 30 scratches inactive (about 25%), observer disagreement leading to "random" (about 10%), bimodal excluded (about 0.3%); the same birds across conditions, "each bird only contributes one mean direction" in pooled data. Per-group Rayleigh results as in the record.

**Error (between-group tests omitted; design of the 5 vs 67 degree comparison omitted).** The value's "as well as" and the record's "turned accordingly" rest on Mardia-Watson-Wheeler tests the record does not carry: spring 2014 5°NMF vs 5°CMF "(W = 6.402, df = 2, p = 0.041)."; autumn 2014 5°NMF vs 5°CMF "(W = 12.348, df = 2, p < 0.002), but not between the 67°NMF and the 5°NMF condition" " (W = 0.574, df = 2, p > 0.607 (ns))."; spring 2015 67°NMF vs 67°CMF "(W = 19.965, df = 2, p < 0.001)." The 5 and 67 degree conditions were run in the same season only in autumn 2014 (spring 2014 had no 67 deg group, spring 2015 no 5 deg group), and no test of concentration (r) between 5 and 67 degrees is printed (tool summary), so "as well as" is the authors' wording resting on direction tests and similar r values. The method also omits the Emlen funnels. Fixable.

### Line 3, Sylvia atricapilla, random at 0 degrees

Quote and value verified; per-season 0 deg Rayleigh results, the pooled NMF null and the spring-2014 doubled-angle exception match the page. **MATCH.** Uncounted additions: the pooled 0°CMF null "0°CMF: group mean orientation = 4°, r = 0.08, p = 0.882 (ns), N = 20" (same direction as the logged null, so not counted), Emlen funnels in method, and the shared design points of line 2.

### Line 4, Sylvia borin, not disoriented with the oscillating-field device on

Verified: "We captured first-year garden warblers during autumn migration on the Courish Spit" " (Kaliningrad region, Russia; 55°09′N, 20°52′E)."; phase 1 "(α = 216°, n = 21, r = 0.38, P = 0.045)."; off device "just below the significance level" " (α = 164°, n = 11, r = 0.51, P = 0.056; Fig. 2C)." (the record states correctly that this group was not significantly oriented); "Out of 22 birds carrying the portable OMF device, 21 showed nocturnal migratory activity"; double-blind for device tests; "Inactive (fewer than 40 scratches) and disoriented birds were excluded from analysis."

**Error (repeated-measures design misstated; between-group tests and testing-to-criterion omitted).** (a) The record calls the coil group "the same species" and says the on and off groups "were different birds as far as the page summary shows (not confirmed)". The paper says "As we expected, the same birds, being subjected to homogeneous 5 nT OMF created by stationary coils, were disoriented" " (Fig. 2B; α = 106°, n = 12, r = 0.11, P = 0.86)."; "During the second phase, birds passed three types of tests."; and the coil test was run "either before it was put on" " or after it had been removed". The phase-2 conditions were the same birds, not independent groups. (b) Omitted: "The direction of activity shown by garden warblers with OMF devices switched on was statistically indistinguishable" " from the direction shown by the birds without devices (MWW test: W = 0.15, p = 0.93)." and "the birds with devices switched off (MWW test: W = 0.49, p = 0.78)." (c) Omitted: "Each bird was tested from one to four times until receiving the directional selectivity." With disoriented birds also excluded, testing ran to a criterion, which favours oriented group results. The value states the null as "not disoriented", which is the paper's reading of no OMF effect via the device; acceptable. Note fix (uncounted): main holds no species-rank Sylvia borin row, only gap cells, plus a common-name garden warbler sense_magnetic row (oa-2:4075). Fixable.

### Line 5, Erithacus rubecula, control robins unable to orient

Verified: nestlings "collected for hand-raising from their nests in the vicinity of Oldenburg" "at the ages between five and eleven days" in 2010 (13), 2011 (13) and 2013 (15); Emlen funnel cages; test field "a total intensity of 48,880 nT ± 520 nT (s.d.), a declination of 0° and an inclination of 67.5° ± 0.4° (s.d.)."; autumn baseline "(mean = 23°, r = 0.17, n = 41, P = 0.295)."; control "(Rayleigh test: mean = 294°, r = 0.08, n = 19, P = 0.895"; experimental P = 0.004 in Results and "(mean = 56° ± 40°, r = 0.43, n = 22, P = 0.017)" in the Fig. 2 legend (the record's statement of the discrepancy is right); assignment and blinding not described.

**Error (significant between-group result and the V test omitted; value adds to the quote).** (a) "The orientation of the control group (r = 0.08) was significantly more scattered" " than the orientation of the experimental group (r = 0.43, P = 0.002;" " 99% confidence limits calculated to be 0.11 < r < 0.75 by bootstrapping" (bootstrap from the oriented sample) is not carried; it is the paper's direct test of the control null against the experimental group. (b) The control V test toward the expected 33 deg spring direction, V = −0.012, P = 0.529 (tool summary), is not carried. (c) Experimental birds did not differ between seasons "(F = 1.307, df = 2, P = 0.294)." (uncounted addition). (d) The value's "in the geomagnetic field" is not in the quote; the test field is described in method. Fixable.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Alouatta caraya, 40,673 to 44,963 cells/mm2 | error | conditions | shrinkage rationale stated opposite to the paper |
| 2 | Sylvia atricapilla, oriented at 5 deg | error | conditions, method | MWW direction tests omitted; 5 vs 67 deg run together only in autumn 2014; Emlen funnels |
| 3 | Sylvia atricapilla, random at 0 deg | MATCH | conditions (uncounted) | pooled 0°CMF null can be added |
| 4 | Sylvia borin, oriented with OMF device on | error | conditions, note | same birds across phase-2 conditions misstated; MWW tests and test-to-criterion omitted |
| 5 | Erithacus rubecula, controls unable to orient | error | value, conditions | bootstrap P = 0.002 and V test omitted; value adds "in the geomagnetic field" |

Errors 4 of 5 records (80%), above the 5% bar; all fixable with the text below; none held out. Bibliographic, licence, name, duplicate and quote checks pass. Ruling asked: line 1's value follows the Results means (the quoted sentence), not the abstract's rounded 40,700–45,200 range. Unchecked: Schwarze et al. Table 1 (field intensities at 5 and 0 deg) and Fig. 2; Bojarinova et al. Supplementary Material (coil details, per-bird test history); the bird-by-condition breakdown in both blackcap and warbler papers; Alert et al. figure 2a panels; an external taxonomic authority page for Sylvia borin (none opened; name as on main). Desk owner questions: (1) a categorical null from an abstract sentence is acceptable as a sense_magnetic value when the statistics are in conditions, as main's birds:162 shows; (2) and (3) concern lines 6 to 9 (audit 336).

## Replacement text

Each old string occurs exactly once in its field (checked with `str.count`).

Line 1 (counted):
- `conditions`: "no correction was applied to densities, so densities are for shrunken tissue." -> "no correction was applied to densities because, the authors state, shrinkage occurred only along retinal borders and the relieving cuts, so the counted regions are taken as unshrunk. There was no consistent difference in dorsal versus ventral ganglion cell density (no statistical test printed)."
- `conditions` (uncounted): "counting fields 1,537 square micrometres to 1.5 mm." -> "counting fields 1,537 square micrometres within 1.5 mm of the fovea, 9,604 from 1.75 to 5 mm and 38,416 from 6 mm to the periphery."

Line 2 (counted):
- `conditions`: "(turned accordingly after the -120 deg rotation);" -> "(turned accordingly after the -120 deg rotation; Mardia-Watson-Wheeler 5 deg NMF vs CMF W = 6.402, df = 2, p = 0.041);"
- `conditions`: "spring 2015 67 deg NMF 38 deg, r = 0.66, N = 13, p < 0.01; 67 deg CMF 284 deg, r = 0.79, N = 13, p < 0.001." -> "spring 2015 67 deg NMF 38 deg, r = 0.66, N = 13, p < 0.01; 67 deg CMF 284 deg, r = 0.79, N = 13, p < 0.001 (NMF vs CMF W = 19.965, df = 2, p < 0.001). Autumn 2014 5 deg NMF vs CMF W = 12.348, df = 2, p < 0.002; 67 deg NMF vs 5 deg NMF not different (W = 0.574, df = 2, p > 0.607). The 5 and 67 deg fields were run in the same season only in autumn 2014 (spring 2014 had no 67 deg group, spring 2015 no 5 deg group), and no test of concentration (r) between 5 and 67 deg is printed, so 'as well as' is the authors' reading of similar direction and r. The same birds were tested across conditions (pooled analyses use one mean per bird); scratch papers with observer disagreement were treated as random (about 10%)."
- `method`: "orientation tests of caged night-migratory birds in Faraday-shielded huts" -> "Emlen funnel orientation tests (modified aluminium funnels, scratch paper) of caged night-migratory birds in grounded aluminium-lined huts acting as Faraday cages"

Line 3 (uncounted):
- `conditions`: "pooled 0 deg NMF over spring 2014-2015 mean 25 deg, r = 0.33, p = 0.140 (ns), N = 17." -> "pooled 0 deg NMF over spring 2014-2015 mean 25 deg, r = 0.33, p = 0.140 (ns), N = 17; pooled 0 deg CMF mean 4 deg, r = 0.08, p = 0.882 (ns), N = 20."
- `method`: "orientation tests of caged night-migratory birds in Faraday-shielded huts" -> "Emlen funnel orientation tests (modified aluminium funnels, scratch paper) of caged night-migratory birds in grounded aluminium-lined huts acting as Faraday cages"

Line 4 (counted):
- `conditions`: "Phase 1, no device, indoors: n = 21, r = 0.38, P = 0.045." -> "Phase 1, no device, indoors: mean 216 deg, n = 21, r = 0.38, P = 0.045. In phase 2 the birds passed three types of tests (device on, device off, stationary-coil OMF without device, the coil test before the device was fitted or after it was removed), so the phase-2 groups are largely the same birds. Device-on direction did not differ from the no-device birds (Mardia-Watson-Wheeler W = 0.15, p = 0.93) or the device-off birds (W = 0.49, p = 0.78). Each bird was tested one to four times until it showed directional selectivity."
- `conditions`: "Contrary result: the same species placed in a homogeneous 5 nT OMF from large stationary coils (no device, n = 12, r = 0.11, P = 0.86) showed clear disorientation." -> "Contrary result: the same birds placed in a homogeneous 5 nT OMF from stationary coils (no device, mean 106 deg, n = 12, r = 0.11, P = 0.86) were disoriented."
- `conditions`: "The two device groups (on and off) were different birds as far as the page summary shows (not confirmed)." -> "The per-bird breakdown across conditions is in the Supplementary Material, not read; testing to a criterion with disoriented birds excluded favours oriented group results."
- `note` (uncounted): "(main holds only visual rows for Sylvia borin)" -> "(main holds no species-rank Sylvia borin evidence row, only gap cells, and a common-name 'garden warbler' sense_magnetic row, oa-2:4075, on cryptochrome staining from Solov'yov et al. 2010, a different DOI and finding)"

Line 5 (counted):
- `value`: "remained unable to orient in the geomagnetic field" -> "remained unable to orient"
- `conditions`: "Control spring result (Results): Rayleigh mean 294 deg, r = 0.08, n = 19, P = 0.895 (disoriented)." -> "Control spring result (Results): Rayleigh mean 294 deg, r = 0.08, n = 19, P = 0.895 (disoriented); V test toward the expected 33 deg spring direction V = -0.012, P = 0.529. The control group's orientation was significantly more scattered than the experimental group's (r = 0.08 vs 0.43, P = 0.002; 99% confidence limits 0.11 < r < 0.75 by bootstrapping 19 values from the oriented sample). Experimental birds' mean directions did not differ between the three seasons (Watson-Williams F = 1.307, df = 2, P = 0.294)."
- `note` (uncounted): "(pone.0043271, the bpj paper)" -> "(pone.0043271, pone.0020091 pooled with Gallus, and the bpj paper)"
