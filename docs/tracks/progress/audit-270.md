# audit-270: desk-d186 (7 evidence records, no search records, no wanted lines)

Audited 31 October 2026 from the desk-d186 files present untracked in the worktree (docs/tracks/progress/desk-d186.md and 7 evidence lines in docs/views/evidence/desk-d186.jsonl; neither committed here, neither edited). `tools/senses/check.py` on the evidence file: 7 records, 0 problems. Quote lengths (`len(q.split())`), lines 1 to 7: 38, 34, 31, 29, 29, 27, 9; all within 40. No searched or wanted file, so all seven records were judged. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md (grade and `partial`), BRIEF quote rules, the publisher-copy and repository-licence rule and the name rule, in the form of audits 267 to 269. Duplicates checked with git grep on origin/main (d56a62dd) under docs/views/evidence, docs/views/audit/corrected, docs/views/audit/ALL.jsonl, docs/views/searched and docs/views/wanted for Xenopus, Heliophobius, "Ctenomys talarum", "Salamandra salamandra", Spalax, Malewski, Hoover and the three DOIs. 1 WebSearch and 11 WebFetch calls used.

Sources opened: api.crossref.org/works/ 10.3389/FPHY.2022.995860, 10.7717/PEERJ.5819, 10.3390/D16060312; frontiersin.org/articles/10.3389/fphy.2022.995860/full (record URL, three passes, title confirmed each time); peerj.com/articles/5819 (record URL, one pass, title confirmed); mdpi.com/1424-2818/16/6/312 (record URL, three passes, title confirmed each time); biolib.cz taxon 302672 (returned by my WebSearch). A plazi.org result returned only a redirect notice. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened; nothing was refused. WebFetch returns model summaries, so quotes were checked by MATCH/MISMATCH; points marked "(tool summary)" were not returned verbatim.

## Bibliographic and licence (Crossref, fresh)

- Ren: Jie Ren, Weichuan Mo, Haitao Zhang, Rongqiao He, Xiumei Wang, Tao Jiang, Ying Liu; title as recorded; Frontiers in Physics 10, article 995860, no issue; online and issued 2022-09-30; licence creativecommons.org/licenses/by/4.0, vor, from 2022-09-30, delay 0; relation empty; no update-to. As recorded. The page text returned no licence line; accepted on Crossref vor CC BY with the publisher's own free copy, as audit 269 accepted Frontiers.
- Malewski: Sandra Malewski, Sabine Begall, Cristian E. Schleich, C. Daniel Antenucci, Hynek Burda; title as recorded; PeerJ 6, e5819; issued 2018-10-31; CC BY 4.0, content-version unspecified, from 2018-10-31; relation has-review only; no update-to. As recorded. Page: "This is an open access article distributed under the terms of the Creative Commons Attribution License". Accepted.
- Hoover: Hayes Hoover, Raoul Manenti, Andrea Melotto; title as recorded; Diversity 16, issue 6, page 312; online and issued 2024-05-22; Crossref licence creativecommons.org/licenses/by/4.0, vor, from 2024-05-22, delay 0; relation empty; no update-to. As recorded. Crossref reports CC BY 4.0, not 3.0. The exact copy read, the MDPI article page, carries no licence sentence in its body (an "Open Access" icon only); its page metadata gives dc.rights creativecommons.org/licenses/by/3.0/. The desk's progress note states both correctly (Crossref 4.0, page metadata 3.0). Judged on its merits, CC BY 3.0 is an open Attribution licence permitting reuse with credit, so it meets the licence rule, and the copy is the publisher's own free full text in any case. Accepted. Uncounted: the 3.0/4.0 mismatch is MDPI's metadata, not the desk's; a note line could record it.

Bibliographic faults 0; licence faults 0.

## Names

- Xenopus laevis: EXACT, ACCEPTED in docs/views/gaps/gbif-names.tsv (5217334). The Methods print only "Xenopus tadpoles (stage 48)"; the Introduction names "The African clawed frog (Xenopus laevis)" as the commonly used model, and the embryo protocol is a standard laevis in vitro fertilisation. The records say where the binomial comes from. Accepted; owner question 3.
- Heliophobius argenteocinereus (2437220) and Ctenomys talarum (2439621): EXACT, ACCEPTED in gbif-names.tsv; the paper prints both binomials in Table 1 ("Silvery mole-rat (Heliophobius argenteocinereus)", "Talas tuco-tuco (Ctenomys talarum)").
- Salamandra salamandra: EXACT, ACCEPTED (2431776). No subspecies is named anywhere on the page (Lombardy Prealps larvae). Cave and stream larvae are one species; pooling them at species rank is not a cultivar or hybrid pool, and the paper found no origin effect.
- Spalax galili (for the dropped null): BioLib taxon 302672 lists "Spalax galili Nevo, E. Ivanitskaya & A. Beiles, 2001" at species rank, citing Mammal Species of the World (3rd ed.). The desk's "no reachable name authority" was a retrieval gap, not an absence.

Name faults 0; cultivar or pooled 0.

## Duplicates

None of the three DOIs or first authors is on main. Xenopus laevis on main: vision, thermal and non-visual-light rows from other papers; no sense_magnetic row. Heliophobius argenteocinereus on main: oa-10 vision rows (10.1371/journal.pone.0011810). Ctenomys talarum on main: lambda_max, receptor_classes, field-of-view rows. Salamandra salamandra on main: colour_vision, behaviour_vision (prey-dummy strikes, 10.1007/bf00656390; dim-light snapping, 10.1007/bf00195393), depth_cue and others; none from Hoover 2024 and none on cave/stream or rearing. Duplicates 0.

## Per-paper findings

### Ren et al. 2022 (lines 1 to 3)

Quotes: line 1 MATCH and line 2 MATCH (Results 3.2); line 3 opening words MATCH (Results 3.3), the remainder confirmed by the tool as the 34% and 55% figures with p = 0.0015 and p = 0.0001 and a tail about the reduction exceeding the locomotion parameters, so the " …" cut keeps subject and values. Whole sentences.

Set-up (tool summary with verbatim fragments): "NdFeB permanent magnets" in the two central wells of a 12-well plate, sham "tin-foil-wrapped nickel coins of the same size and appearance"; blank and sham fields 0.042 and 0.043 mT; "The temperature was constant at around 25°C" (no per-arena measurement described). Because the magnets are permanent, coil heating and induced currents do not arise; vibration, blinding and randomisation are not mentioned. Statistics: Wilcoxon matched-pairs signed-rank for Figures 3 and 4; "n is the total number of tadpoles from seven experiments, twelve tadpoles per experiment" (about 84), so the tadpole is the unit, not the experiment.

Design fault the records omit. Methods: "For the second experiment, the same batch of tadpoles was tested under the sham and magnetic conditions sequentially"; Results 3.2: "each tadpole was tested under the "sham" and "magnet" conditions sequentially". No interval and no counterbalancing are reported, so every record's magnet-versus-sham fall is also a second-test-versus-first-test fall; habituation, fatigue or time in the arena are not excluded.

Contrary result the records omit. Results 3.1 (Fig. 2, separate tadpoles for sham and magnet, six experiments of eighteen): magnet distance "showed a decreasing trend during the tests compared to those in the dark adaptation (−21%, p = 0.2184)"; "the magnet-induced changes in swimming distance were not statistically significant"; dark adaptation −13% and dark pulse −15% not significant (tool summary); "The sham treatment showed the same negative effect on swimming distance". The one significant result there is recovery after magnet removal. So the only between-groups test of the effect was null, and the significant effects come from the order-confounded paired design.

The records' conditions say the response is to a strong field and gradient and not a compass, which is right, but neither the sequential design nor the Fig. 2 null is in any field. Both change the causal interpretation and limit the claimed effect (oa-audit: "a null result or exception that limits a claimed effect"). Counted on lines 1, 2 and 3 (scientific context, fixable). Uncounted: the tool reports that the Results call Fig. 3D the 30 s dark pulse while the legend labels that panel the light condition (owner question 2); the desk's dropping of the direction-preference sentence is acceptable, since it does not limit these values.

### Malewski et al. 2018 (lines 4 and 5)

Quote MATCH (Results). Whole sentence naming both species, each record logging only its own. Table 1 n (31 and 19) and localities match the records. Methods: "a digital compass rose", "normalizing the data relative to the direction of true magnetic North", "Only straight tunnels that were at least as long as 5% of the polygon's circumference".

Grade and trait. The measurement is burrow-axis orientation; magnetoreception is the authors' suggestion, not tested. Under oa-read, `g` covers "a value the paper predicts or presumes rather than measures", with the presumption named in `method`, and `method` says "magnetoreception inferred, not tested". BRIEF's sense_magnetic is a free string under "other senses", and main already files orientation-to-field rows there. Grade g and the key fit. The value says no more than the quote ("(second-order mean)" is the Results' own level, stated in the preceding sentence and the note).

Context. The Discussion names alternative cues ("landscape characteristics (e.g., dunes, vegetation, slopes, water currents)", "soil condition"); the records' "slope, soil, sun, drainage" is close; the sun is raised only in the Introduction (uncounted wording fix). Fukomys (NE/SW) is a pooled two-species result (F. anselli n = 7, F. mechowii n = 2) and the desk rightly did not file it at species rank.

Spalax galili null. "No prevailing magnetic direction of the studied burrows was found in the blind mole rat (S. galili) (Fig. 1D)." This is the paper's own measurement for a third species. It does not limit the silvery mole-rat or tuco-tuco findings, and both notes already state it as the paper's contrast, so lines 4 and 5 are not in error. As a unit it is a missed row: the desk's stated reason (no name authority reachable) does not hold, since MSW3 via BioLib lists S. galili at species rank. Following audit 269 (missed measurement uncounted for evidence, recommended row), not counted; recommended row below, with the paper's own caveat that "Basaltic soils are generally characterized by rather strong magnetic signatures". Owner question 1.

Lines 4 and 5: confirm.

### Hoover et al. 2024 (lines 6 and 7)

Quotes MATCH (Results), whole sentences: line 6 "After rearing, for the tests including a visual stimulus, there was a reduction in the average approach time by more than 170 s (Figure 3, Table 2)."; line 7 "No differences between cave and stream larvae were observed."

Context (tool summary with verbatim fragments). 52 larvae, stage 1, seven caves and six streams; 500 lux. Four test conditions: O+V+ a defrosted Chironomus larva with shaking tweezers (the shaking gives the visual cue); O+V− larva dropped by gravity; O−V+ the odourless uncoloured plastic-string decoy shaken; O−V− decoy dropped. Rearing: 55 days, each larva fed Chironomus with continuously shaken tweezers; "all larvae were assigned the same feeding treatment", so there is no rearing control. Discussion: "Although larval body lengths were longer in the second test period, thus enabling quicker movements generally, the test period alone did not result in significantly quicker approach times." Preceding sentence of line 6's quote: "Moreover, while the test period was not significant, its interactions with both visual and chemical stimuli were." Following: "For tests including a chemical stimulus, a reduction occurred after rearing, but was lower." Table 1 (tool summary): visual cue F = 271.76, p < 0.001; origin F = 0.03, p = 0.85; test period F = 0.52, p = 0.47. Number tested after rearing and mortality not reported.

Line 6. Counted (scientific context and value beyond quote, fixable, counted once). (a) `conditions` asserts "so the post-rearing change reflects experience, not an innate response". With every larva given the same treatment and no unreared or differently reared group, experience is confounded with 55 days of growth, age and laboratory time; the authors themselves note the larvae were longer at the second test. The record states as established a causal reading the design cannot separate. (b) `value` narrows "tests including a visual stimulus" to the "odourless plastic-string decoy", but the tests including a visual stimulus are O+V+ (shaken real larva) and O−V+ (shaken decoy); the quote does not say the fall was in the decoy test.

Line 7. Null, matches the quote and the Table 1 origin term (p = 0.85). The same `conditions` clause about experience is carried here, but it does not bear on the origin comparison; uncounted fix below.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Xenopus laevis, bright: distance −31%, speed −32%, duration unchanged | correct | value, conditions | Quote MATCH; omits sequential sham-then-magnet design (no counterbalancing) and the null between-groups test of Fig. 2 with sham showing the same decline (Results 3.1, Methods) |
| 2 | Xenopus laevis, dark pulse: distance −26%, duration −26%, speed −32% | correct | value, conditions | Same omissions as line 1; same paired design |
| 3 | Xenopus laevis, path adjustments −34% bright, −55% dark | correct | value, conditions | Quote opening MATCH, cut fair; same omissions (Fig. 4 uses the same sequential design) |
| 4 | Heliophobius argenteocinereus, burrow axes N–S | confirm | (conditions; uncounted) | Quote MATCH; grade g fits presumed magnetoreception; n 31; S. galili null in note |
| 5 | Ctenomys talarum, burrow axes NNW/SSE | confirm | (conditions; uncounted) | Quote MATCH; grade g; n 19 |
| 6 | Salamandra salamandra, approach time fell >170 s after rearing | correct | value, conditions | Quote MATCH; no rearing control and growth confound, so "reflects experience" overstates; value narrows "tests including a visual stimulus" to the decoy |
| 7 | Salamandra salamandra, no cave/stream difference | confirm | (conditions; uncounted) | Quote MATCH; origin F = 0.03, p = 0.85 |

Evidence errors: 4 of 7 (57.1%): scientific-context faults 4 (lines 1, 2, 3, 6; line 6 also carries a value-beyond-quote fault, counted once); duplicates 0; licence 0; bibliographic 0; name 0; pooled or cultivar 0; quote-form 0. Unfixable records: none. All four error lines are fixable with the counted text below.

Pooled with audits 172 to 269: 209 of 522 evidence records (40.0%; audit 269's 205 of 515 plus 4 of 7 here; any audit running concurrently is not included). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Counted (lines 1 to 3, `conditions`): append "; design: the records' Figure 3 and 4 data come from a paired test in which 'the same batch of tadpoles was tested under the sham and magnetic conditions sequentially' (Methods), sham first, with no interval or counterbalancing reported, so order, habituation and fatigue are not excluded; Wilcoxon matched-pairs, n = tadpoles (seven experiments of twelve), not experiments; in the separate-groups experiment (Results 3.1, Fig. 2, six experiments of eighteen) the magnet-induced changes in swimming distance were not statistically significant (−21%, p = 0.2184; dark adaptation −13%, dark pulse −15%) and the sham showed the same negative effect on swimming distance, though distance recovered when the magnet was removed; permanent NdFeB magnets, so no coil heating or induced current; temperature about 25 °C, not monitored per arena; vibration, blinding and randomisation not mentioned".

Counted (`value`):
- Line 1: "In bright light the magnet cut swimming distance by 31% and speed by 32%; active swimming duration did not change (paired test, sham always before magnet; the separate-groups test of Fig. 2 found no significant fall in distance)"
- Line 2: "During the 30 s dark pulse the magnet cut swimming distance by 26%, active duration by 26% and speed by 32% (paired test, sham always before magnet; the separate-groups test of Fig. 2 found no significant fall in distance)"
- Line 3: "Total number of path adjustments fell 34% in bright light and 55% in the dark under the magnet (paired test, sham always before magnet)"

Counted (line 6):
- `value`: "after 55 days of rearing, approach time in tests including a visual stimulus fell by more than 170 s"
- `conditions`: replace "visual-only condition used an uncoloured, odourless plastic-string decoy moved with shaking tweezers; larvae were reared individually for 55 days at a mean 18 C under natural photoperiods and fed while exposed to accompanying stimuli, so the post-rearing change reflects experience, not an innate response" with "tests including a visual stimulus were O+V+ (defrosted Chironomus larva on shaking tweezers) and O−V+ (uncoloured, odourless plastic-string decoy on shaking tweezers); larvae were reared individually for 55 days at a mean 18 C under natural photoperiods and fed Chironomus with shaken tweezers; all larvae received the same feeding treatment, with no rearing control, and were longer at the second test (Discussion), so experience is confounded with growth, age and laboratory time; the test period alone was not significant (F = 0.52, p = 0.47), its interactions with visual and chemical cues were; number tested after rearing not reported"
- `note`: append "Next sentence of the Results: 'For tests including a chemical stimulus, a reduction occurred after rearing, but was lower.'"

Uncounted:
- Lines 4 and 5 `conditions`: replace "(slope, soil, sun, drainage)" with "(the Discussion names landscape characteristics such as dunes, vegetation, slopes and water currents, and soil condition)"; append "; straight tunnels at least 5% of the burrow polygon's circumference".
- Line 7 `conditions`: the same replacement as line 6's conditions; `note`: append "Table 1: origin term F = 0.03, p = 0.85."
- Lines 6 and 7 `note`: append "Licence: Crossref CC BY 4.0 vor; the MDPI page metadata gives CC BY 3.0 (dc.rights)."
- Recommended new row (Malewski 2018, sense_magnetic, Spalax galili, grade g): quote "No prevailing magnetic direction of the studied burrows was found in the blind mole rat (S. galili) (Fig. 1D)."; value "no prevailing magnetic direction of burrow axes (null)"; conditions "Upper Galilee Mountains (Israel), n = 9 burrow systems (Table 1); the Discussion notes that 'Basaltic soils are generally characterized by rather strong magnetic signatures'"; name Spalax galili Nevo, Ivanitskaya & Beiles 2001 (MSW3 via BioLib). Check the quote on a legal text before filing.

## Owner questions

1. Malewski 2018: file the Spalax galili null as its own row (recommended above), or keep it in the two notes only? It is the paper's one magnetic null and S. galili is listed at species rank in MSW3.
2. Ren 2022: the tool reports that the Results call Fig. 3D the 30 s dark pulse while the legend labels it the light condition. Line 2 follows the Results text; should a note flag the paper's inconsistency?
3. Ren 2022 names Xenopus laevis only in the Introduction; the Methods say "Xenopus tadpoles". Accept the Introduction's binomial (as done here), or hold the rows at genus Xenopus?

Progress note: accurate on sources, licences (including the Crossref 4.0 and MDPI 3.0 distinction) and names; its reason for not filing S. galili (no name authority) does not hold; it does not mention the sequential design or the Fig. 2 null.

Verdict: 4 errors in 7 (57.1%), above the 5% bar; pooled 40.0%. Error lines: 1, 2, 3, 6. No unfixable records; lines 1, 2, 3 and 6 can merge with the counted text, and lines 4, 5 and 7 with the uncounted fixes.
