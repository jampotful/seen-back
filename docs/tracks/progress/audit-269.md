# audit-269: desk-d185 (9 evidence records, no search records, no wanted lines)

Audited 31 October 2026 from the desk-d185 files present untracked in the worktree (docs/tracks/progress/desk-d185.md and 9 evidence lines in docs/views/evidence/desk-d185.jsonl; neither committed here, neither edited). `tools/senses/check.py` on the evidence file: 9 records, 0 problems. Quote lengths (`len(q.split())`), lines 1 to 9: 15, 15, 19, 20, 18, 23, 12, 20, 12; all within 40. No searched or wanted file, so all nine records were judged. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md (grade and `partial`), BRIEF quote rules, the publisher-copy and repository-licence rule and the name rule, in the form of audits 266 to 268. Duplicates checked with git grep on origin/main (aed57a0c) under docs/views/evidence, docs/views/audit/corrected, docs/views/audit/ALL.jsonl, docs/views/searched and docs/views/wanted for Rhynchohyalus, Opisthoproctus, Winteria, Opisthoproctidae, barreleye, spookfish, Astyanax, "Rattus norvegicus", airflow, supra-orbital, Mugnaini, Yoshizawa, "Wagner H-J", "Simon N" and the three DOIs. 5 WebSearch and 14 WebFetch calls used.

Sources opened: api.crossref.org/works/ 10.3389/FEVO.2022.1044565, 10.7717/PEERJ.8148, 10.1371/JOURNAL.PBIO.3002168; frontiersin.org/articles/10.3389/fevo.2022.1044565 (record URL, four passes, title confirmed each time); peerj.com/articles/8148 (record URL, two passes, title confirmed); edoc.hu-berlin.de item page b44730ef-3c1a-40ca-8e5d-dfcb274c4646/full and the record's bitstream PDF (two passes, title confirmed); Catalog of Fishes spid 10841, 10891 and 3965 and fishbase.mnhn.fr FamilySummary ID=85 (all returned by my WebSearches or named in the record). A search result on springerlink.bibliotecabuap.elogim.com (a library proxy) was not opened. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened; nothing was refused. WebFetch returns model summaries, so quotes were checked by MATCH/MISMATCH; points marked "(tool summary)" were not returned verbatim.

## Bibliographic and licence (Crossref, fresh)

- Wagner: Hans-Joachim Wagner, Martin J. Genner, Julian C. Partridge, Wen-Sung Chung, N. Justin Marshall, Bruce H. Robison, Ronald H. Douglas; title as recorded; Frontiers in Ecology and Evolution 10, article 1044565, no issue; online, published and issued 2022-12-01; licence creativecommons.org/licenses/by/4.0, vor, from 2022-12-01, delay 0; relation empty; no update-to. As recorded. The page fetched shows "Open access statement" and "Copyright statement" links without their text; accepted on Crossref vor CC BY with the publisher's own free copy.
- Simon: Noah Simon, Suguru Fujita, Megan Porter, Masato Yoshizawa; title as recorded (Crossref italicises "opsin"); PeerJ 7, e8148; issued 2019-12-17; CC BY 4.0, content-version unspecified, from 2019-12-17; relation empty; no update-to. As recorded. Page: open access under the Creative Commons Attribution License (tool summary). Accepted.
- Mugnaini: Matias Mugnaini, Dhruv Mehrotra, Federico Davoine, Varun Sharma, Ana Rita Mendes, Ben Gerhardt, Miguel Concha-Miranda, Michael Brecht, Ann M. Clemens; title as recorded; PLOS Biology 21, issue 7, e3002168; online 2023-07-06; CC BY 4.0 vor from 2023-07-06; relation has-preprint 10.1101/2022.08.18.504295; no update-to. As recorded.

Repository copy (Mugnaini, lines 7 to 9). The exact copy read is the Humboldt-Universitaet edoc bitstream `journal.pbio.3002168.pdf`. The item page that serves it states dc.rights "(CC BY 4.0) Attribution 4.0 International", dc.rights.uri creativecommons.org/licenses/by/4.0/, dc.type.version "publishedVersion", repository DOI 10.18452/33695. The PDF's first page prints "This is an open access article distributed under the terms of the Creative Commons Attribution License," with the citation PLoS Biol 21(7): e3002168. The copy carries an open licence statement on itself and on its item page, so it meets the repository rule. Accepted. Uncounted: the record could cite the item page or repository DOI in `note` so the licence statement can be found without downloading the PDF.

Bibliographic faults 0; licence faults 0.

## Names

- Opisthoproctus soleatus: Catalog of Fishes spid 10841, "Current status: Valid as Opisthoproctus soleatus Vaillant 1888. Opisthoproctidae." FishBase family list: accepted.
- Rhynchohyalus natalensis: FishBase family list: accepted (Hyalorhynchus natalensis, Ophthalmopelton macropus and the misspelling Rhynchoyalus listed as synonyms); Catalog of Fishes spid 10891 (Ophthalmopelton macropus) reads "Synonym of Rhynchohyalus natalensis (Gilchrist & von Bonde 1924)". FishBase also lists a second species, Rhynchohyalus parbevs Prokofiev & Kukuev, 2020; the paper's specimen was caught "as part of previous work" in the South Tasman Sea. I did not find R. parbevs's range (one search returned nothing relevant), so whether the identification predates and survives that description is unchecked (owner question 2). Not counted.
- Winteria telescopa: FishBase family list: accepted (Wintera telescopa and Winteria telescopus synonyms).
- Astyanax mexicanus: Catalog of Fishes spid 3965, "Valid as Astyanax mexicanus (De Filippi 1853)", Acestrorhamphidae. As recorded. Morphs are kept apart: line 4 is the surface morph and lines 5 and 6 the Pachon cave population (Cueva de El Pachon, confirmed), each named in `value`, `eye` and `conditions`, the form main accepted for desk-d162 lines 1 to 4. Not pooled.
- Rattus norvegicus: EXACT, ACCEPTED in docs/views/gaps/gbif-names.tsv (2439261). The paper never prints a binomial (tool summary: "the Latin binomial does not appear"); it names the animals "rats" and, in the cortical localisation, Neuropixels and behaviour Methods, "Long-Evans rats". The behaviour test that lines 7 to 9 rest on is the one naming Long-Evans, so the species is a direct reading of a standard laboratory strain of R. norvegicus, as audit 255 accepted for Long-Evans rats. Every note says the species is read from the strain. A laboratory strain is not a cultivar or a hybrid pool. Accepted.

Name faults 0; cultivar or pooled 0.

## Duplicates

None of the three DOIs, first authors, the three opisthoproctid genera or "supra-orbital" is on main. Astyanax mexicanus on main: desk-d162 lines 1 to 4 (sense_airflow, lateral-line afferent rates, eLife 77387), another paper and trait. Rattus norvegicus on main: vision rows and one sense_touch row (whisking rate, a modelling paper); no sense_airflow row and nothing from Mugnaini 2023. Duplicates 0.

## Per-paper findings

### Wagner et al. 2022 (lines 1 to 3)

Quotes MATCH: line 1 under Results "Rhynchohyalus natalensis" (the paragraph's last sentence); line 2 under "Opisthoproctus soleatus"; line 3 under "Winteria telescopa". None names its species; each sits under its species subheading and `where` names it. Whole sentences.

Specimens (Table 1, tool summary): one individual of each; R. natalensis SL 183 mm, 800 to 1000 m, South Tasman Sea, histology and MRI, "fixed in 70% ethanol and formalin", captured "as part of previous work"; O. soleatus SL 42 mm, 500 to 700 m, North Atlantic, histology; W. telescopa SL 42 mm, 600 to 800 m, Indian Ocean, histology and MRI. The general fixation is "Most eyes were fixed immediately following capture in 4% paraformaldehyde and 2.5% glutaraldehyde"; no species-specific fixative for O. soleatus or W. telescopa. The records' conditions match. Methods name shrinkage: measurements "are subject to artifacts caused by, for example, tissue shrinkage" (fragment).

Line 1 (R. natalensis, 20% of 33,125 axons). Value right; Table 2 gives 6,750 diverticular axons of 33,125 (20.4%). The `method` says "axon count ... in histological sections", but the axons were "estimated by counting the number of axons in ultrathin electron microscopic sections" "from areas distributed at random across the surface of the structures" "covering at least 20% of their total area", with totals "estimated by assuming the same density throughout the entire structure" (Methods, fragments). The 33,125 is an extrapolated estimate. This does not change the 20% share's direction or scale; uncounted fix to `method`. Trait: eye_role is "what one eye or eye pair is for"; an axon share is anatomy rather than a role. Main has accepted anatomical eye_role rows (Marpissa muscosa "no second-order neuropil; axons project to the arcuate body"), and the note says it is not a measure of what the animal sees. Uncounted; owner question 1.

Line 2 (O. soleatus). Counted (quote-form and scientific context, fixable). (a) The value's "tubular main eye" is not in the quote; the quote says only that the diverticulum is continuous with the main eye via a small ventral opening. The paper says elsewhere the eyes are "similar to those of other mesopelagic fish with tubular eyes" (fragment), so the fact is true, but the value says more than its quote. (b) Filed under eye_type, the record gives no type for the diverticulum. The Discussion groups "the small lateral diverticula" of M. grimaldi, O. soleatus and W. telescopa as most likely serving "a simple light-detecting function" (fragments), and says that in O. soleatus and W. telescopa the reflective crystals "are not abundant and are irregularly arranged, so any role in image formation is unlikely" (fragment). For an app that might draw a second image from a diverticulum (as for Dolichopteryx), that changes applicability; the record's note does not say it. Counted once.

Line 3 (W. telescopa, about 900 um, 15% of ocular length). Value right; the sentence does not say whether the diameter came from histology or MRI (the preceding sentence says the diverticulum shows externally as a scleral outfolding). The same Discussion sentences apply, but the value is a dimension and claims no function, and the note already flags possible shrinkage, so the omission is left uncounted; fix below adds it. `method` "histology and MRI" should say the measurement method is not stated (uncounted).

### Simon et al. 2019 (lines 4 to 6)

Quotes MATCH, all in Results "Diurnal activity pattern is maintained after removal of the pineal"; line 6's sentence came back in two pieces of one sentence, rejoined; whole sentences.

Context (tool summary): behaviour fish 6 to 16 weeks, 1.2 to 1.5 cm SL (pinealectomised juveniles about 16 weeks); light 30 to 100 lux white LED, 13:11 L:D; tracking under 850 nm infrared. N = 18 control and 15 pinealectomised per morph come from the statistics in the Results, not the Methods (lines 4 and 5 say "Methods"; uncounted wording fix). Surface fish "showed a large burst in swimming following both the light OFF and ON" (Fig. 6A). Cavefish: "However, there was a small light-dependent burst in response to the transition from dark to light" "with no observed differences in response between control and pinealectomized cavefish" (Fig. 6B), and no statistical test is reported for any burst. The only cavefish P values are for the day-night activity shift: control P = 0.005, pinealectomised P = 0.008. Discussion caveat: "the relatively small size of the arenas for juvenile fish" which "may make fish nervous and induce unexpected responses" (fragments); and "it is likely that exo-rod and pineal are not involved in the light-induced shift in basal activity of cavefish" (fragment).

Line 4 (surface fish more active in light, with or without pineal). Value matches; the note's confound (eyes intact) is right. Confirm; uncounted: N source wording, arena caveat.

Line 5 (cavefish burst, suggested non-pineal). Value matches and carries "suggested". The note conveys that the burst is small and dark-to-light only. Not conveyed: the burst was not statistically tested. The value already marks the inference as the authors' suggestion and the note scopes the burst, so the omission does not change the direction or the causal reading the record gives; uncounted, fix below.

Line 6 (null: no cavefish burst at light-to-dark). Value matches; conditions scope it to the light-to-dark transition and the note gives the dark-to-light exception. Confirm.

Missed measurement (uncounted for evidence; recommended new row). The paper's main cavefish behaviour result is not logged: "In cavefish, as in surface fish, pinealectomized and control fish also showed higher activity in the light and lower activity in the dark (Fig. 6B)." (tool returned it as one sentence; run quotecheck.py on a legal text before filing), with P = 0.005 (control) and P = 0.008 (pinealectomised). Line 4's note says to read it "together with the cavefish records", but none of them carries this result, which is the one that separates a non-pineal, non-ocular light response in eye-degenerate fish. Owner question 3.

### Mugnaini et al. 2023 (lines 7 to 9)

Quotes MATCH: line 7 Abstract; lines 8 and 9 Results, "Wind-whisker trimming and supra-orbital whisker blockade interfere with airflow turning responses". Whole sentences.

Context (tool summary): stimuli were hand-flaps (about 0.3 m/s) and cardboard-flaps (about 0.5 m/s); "rats turned significantly more often towards hand-flaps than away from them (Fig 6B; p < 0.001, χ2 Test; "Turn to" (31 trials) versus "Turn away" (7 trials))"; no chance level or no-airflow control is reported. Tests in a darkened room, box lit by an infrared LED. Trimming: wind-whisker-trimmed rats turned towards the stimulus 20% of the time against 29% (p = 0.02, Fig 7D; 7 per group, Mann-Whitney). Lidocaine: subcutaneous at the supra-orbital follicles, dose not stated, crossover with Ringer 24 h apart, "The average turns towards the cardboard-flap stimulus were less frequent (18%) for lidocaine treatment than for Ringer treatment (23%, p = 0.039)" (Wilcoxon, N = 8); this is the sentence immediately before line 9's quote. The authors call the turning "at least partially, if not entirely, tactile reactions" and say they "carefully avoided noises" from the stimuli; no control for odour or temperature is described. The 5 rats for passive whisker movement were "deeply anesthetized with ketamine" (Results; Methods do not name the agent).

Line 7 (turn towards airflow in darkness). Value matches the Abstract. Confirm; uncounted: add stimulus speeds and the 31 to 7 count to `conditions`.

Line 8 (7 of 8 decreased after lidocaine). Counted (scientific context, magnitude, fixable). "7 of 8 decreased" reports consistency only. The same paragraph gives the size: mean turning towards the stimulus fell from 23% (Ringer) to 18% (lidocaine), p = 0.039, so the block reduced turning by about five percentage points from an already low rate and did not abolish it. Without this the record reads as a strong whisker-dependence; the note's "One of eight did not decrease" does not convey the scale. This is the oa-audit example of a small absolute outcome behind a consistent relative change.

Line 9 (supra-orbital whiskers alone contribute significantly). Value is the authors' conclusion and the note says so; it gives the trimming result (20% against 29%, p = 0.02, 7 per group), which conveys a partial reduction, not abolition. The conclusion's "alone" rests on the lidocaine block (18% against 23%), which the note omits, and `conditions` says the anaesthetic is not named, where the Results name ketamine. The limitation (reduced, not abolished) is already conveyed by the trimming figures, so uncounted; fixes below.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Rhynchohyalus natalensis, diverticulum 20% of 33,125 axons | confirm | (method, note; uncounted) | Quote MATCH under species heading; axon totals are EM-sample extrapolations, share unchanged |
| 2 | Opisthoproctus soleatus, tubular eye, diverticulum via ventral opening | correct | value, note | Value adds "tubular" absent from the quote; omits Discussion: small diverticulum, simple light detector, image formation unlikely |
| 3 | Winteria telescopa, diverticulum about 900 um, 15% ocular length | confirm | (method, note; uncounted) | Quote MATCH; dimension claims no function; measurement method not stated in the sentence |
| 4 | Astyanax mexicanus surface morph, more active in light with or without pineal | confirm | (conditions; uncounted) | Quote MATCH; eyes-intact confound stated; N comes from Results statistics |
| 5 | Astyanax mexicanus Pachon, burst suggested non-pineal | confirm | (note; uncounted) | Quote MATCH; "suggested", small and dark-to-light only stated; burst untested could be added |
| 6 | Astyanax mexicanus Pachon, no burst at light-to-dark | confirm | none | Quote MATCH (two pieces rejoined); scoped to the transition; dark-to-light exception in note |
| 7 | Rattus norvegicus (Long-Evans), turns to airflow in darkness | confirm | (conditions; uncounted) | Quote MATCH Abstract; species from strain, as audit 255; stimulus speeds can be added |
| 8 | Rattus norvegicus, 7 of 8 decreased after lidocaine | correct | value, note | Quote MATCH; omits that mean turning fell only from 23% to 18% (p = 0.039), reduced not abolished |
| 9 | Rattus norvegicus, supra-orbital whiskers alone contribute significantly | confirm | (conditions, note; uncounted) | Quote MATCH; partial reduction conveyed by trimming figures; lidocaine figures and ketamine can be added |

Evidence errors: 2 of 9 (22.2%): scientific-context faults 2 (lines 2, 8; line 2 also carries a quote-form fault, counted once); duplicates 0; licence 0; bibliographic 0; name 0; pooled or cultivar 0. Unfixable records: none. Both error lines are fixable with the counted text below.

Pooled with audits 172 to 268: 205 of 515 evidence records (39.8%; audit 268's 203 of 506 plus 2 of 9 here; any audit running concurrently is not included). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Counted (line 2):
- `value`: "diverticulum continuous with the main eye via a small ventral opening"
- `note`: append "The main eye is tubular (Results, O. soleatus: eyes 'similar to those of other mesopelagic fish with tubular eyes'), not stated in the quoted sentence. Discussion: the small lateral diverticula of M. grimaldi, O. soleatus and W. telescopa most likely serve a simple light-detecting function, and in O. soleatus and W. telescopa the reflective crystals are sparse and irregular, 'so any role in image formation is unlikely'. Not an image-forming second eye."

Counted (line 8):
- `value`: "7 of 8 rats decreased airflow turning after lidocaine in the supra-orbital follicles compared with Ringer solution; mean turns towards the stimulus 18% (lidocaine) against 23% (Ringer), p = 0.039, reduced but not abolished"
- `note`: replace "One of eight did not decrease." with "One of eight did not decrease. Same paragraph: 'The average turns towards the cardboard-flap stimulus were less frequent (18%) for lidocaine treatment than for Ringer treatment (23%, p = 0.039)' (Wilcoxon signed-rank, N = 8, Fig 7F); crossover design, solutions 24 h apart; lidocaine dose not stated."

Uncounted:
- Line 1 `method`: "anatomical: axons estimated by counting in ultrathin electron microscopic sections from random areas covering at least 20% of the optic nerve and the diverticular fascicle, totals extrapolated assuming uniform density".
- Line 3 `method`: "histology and MRI of one specimen (the sentence does not say which gave the diameter)"; `note`: append "Discussion: a small lateral diverticulum, structurally very similar to O. soleatus's, most likely serving a simple light-detecting function; image formation unlikely."
- Lines 4 and 5 `conditions`: replace "Methods give N" / "Methods N" with "Results statistics give N"; append "; juveniles 1.2 to 1.5 cm SL, light 30 to 100 lux white LED on 13:11 L:D, tracking under 850 nm infrared; the Discussion notes the small arenas may make fish nervous and induce unexpected responses".
- Line 5 `note`: append "No statistical test is reported for the burst; the Discussion says only that the pineal is 'likely' not involved, while the Abstract states it as regulated by a non-pineal extraocular organ."
- Line 7 `conditions`: replace "airflow speed for the turning test not read here" with "hand-flap airflow about 0.3 m/s and cardboard-flap about 0.5 m/s; turned towards hand-flaps in 31 trials against away in 7 (p < 0.001, chi-square); dark room, infrared LED for filming; stimulus noise avoided, odour and temperature not controlled".
- Line 9 `conditions`: replace "agent not named in Methods" with "ketamine (Results; not named in Methods)"; `note`: append "The 'alone' conclusion follows the supra-orbital lidocaine block: mean turns 18% against 23% for Ringer (p = 0.039, N = 8)."
- Lines 7 to 9 `note`: add "Licence also on the edoc item page (dc.rights CC BY 4.0, publishedVersion, repository DOI 10.18452/33695)."
- Recommended new row (Simon 2019, sense_light_nonvisual, Astyanax mexicanus Pachon): quote "In cavefish, as in surface fish, pinealectomized and control fish also showed higher activity in the light and lower activity in the dark (Fig. 6B)."; value "Pachon cave morph: higher activity in light than dark in both control and pinealectomized fish (P = 0.005 and 0.008)"; quotecheck on a legal text before filing.

## Owner questions

1. Line 1 files an axon share under eye_role. Keep it there, as main keeps anatomical eye_role rows, or move it to a trait for retinal or neural allocation?
2. Rhynchohyalus: FishBase lists R. parbevs (2020) beside R. natalensis. Should the South Tasman Sea specimen's identification be checked against R. parbevs's range?
3. Simon 2019: add the cavefish light/dark activity result (with P values) as its own row? It is the paper's main non-ocular finding and none of the three records carries it.

Progress note: accurate on sources, licences and names; its "Species-and-paper pairs not on main" holds.

Verdict: 2 errors in 9 (22.2%), above the 5% bar; pooled 39.8%. Error lines: 2, 8. No unfixable records; lines 2 and 8 can merge with the counted text, and the other seven with the uncounted fixes.
