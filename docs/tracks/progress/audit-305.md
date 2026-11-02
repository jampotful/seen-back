# audit-305: desk-d219, evidence lines 1 to 5

Audited 31 October 2026 from the desk-d219 files present untracked in the worktree (docs/tracks/progress/desk-d219.md and docs/views/evidence/desk-d219.jsonl, 5 lines; neither committed here, neither edited). HEAD 0e7b871a (desk-d218). `tools/senses/check.py` on the evidence file: 5 records, 0 problems. Quote lengths (`len(q.split())`), lines 1 to 5: 12, 16, 16, 16, 16, all within 40. The unit has evidence records only, so the brief's search-record and plant-screening parts do not apply; audits 302 to 304 are the format model.

Duplicates: git grep on origin/main across docs (evidence, audit/corrected, audit/ALL.jsonl, searched, wanted, sheets, gaps, codex-findings, progress notes) for "Odocoileus virginianus" (all traits), "wsb.438", "Lymantria xylina", "Lymantria" with behaviour_vision/phototaxis/lamp, "insects16040338", "Culex tarsalis", "Culex quinquefasciatus", "tarsalis", "quinquefasciatus", "insects13010092", "Reinhold". Lab-strain handling: grep for "laboratory strain", "lab strain", "laboratory colony", "lab colony".

Sources opened (WebFetch): api.crossref.org/works for all three DOIs; www.mdpi.com/2075-4450/16/4/338 (three passes); www.mdpi.com/2075-4450/13/1/92 (two passes); doaj.org/article/053546f0404145ccbbd1146d3e29c72d and en.wikipedia.org/wiki/Lymantria_xylina, both returned by my WebSearch. Refused (PROVENANCE_REQUIRED, not retried): doi.org/10.1002/wsb.438, api.gbif.org species match for Lymantria xylina and Culex tarsalis. No library catalogue, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened (the search returned two university library catalogue records of the DOAJ entry; left alone). WebFetch returns model summaries with verbatim pieces of about 120 characters, so quotes were checked as MATCH/MISMATCH from piecewise verbatim returns; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 2 WebSearch and 9 WebFetch calls used.

## Bibliographic and licence

- Line 1, Cohen et al. 2014, Crossref: Bradley S. Cohen, David A. Osborn, George R. Gallagher, Robert J. Warren, Karl V. Miller, in the recorded order; title verbatim; Wildlife Society Bulletin 38(3): 480-485, issued 2014-05-16 (print September 2014). Crossref licence: Wiley terms and conditions only (onlinelibrary.wiley.com/termsAndConditions#vor), no open licence. DOAJ record: "Vol. 38, no. 3, pp. 480–485", "No licence statement" (tool summary). Licence rule: a publisher or index abstract of a closed article may be filed with source.access "abstract" and "partial": true, which the record does; no full text was used. Met as an abstract record. Bibliographic: as recorded.
- Lines 2 and 3, Zhang et al. 2025, Crossref: Jifeng Zhang, Baode Wang, Rong Wang, Xiancheng Peng, Junnan Li, Changchun Xu, Yonghong Cui, Mengxia Liu, Feiping Zhang, in the recorded order; title verbatim; Insects 16, issue 4, article 338, issued 2025-03-24; CC BY 4.0 (vor); relation empty, no update-to. Page: "Insects 2025, 16(4), 338"; metadata licence CC BY 3.0, no printed licence line (tool summary). Licence met (version difference, both CC BY). **Bibliographic fault, both lines:** `journal` "Insects 16: 338" omits the printed issue (16(4)); counted as in audit 194, under the caller's "exactly as printed" rule.
- Lines 4 and 5, Reinhold et al. 2022, Crossref: Joanna M. Reinhold, Karthikeyan Chandrasegaran, Helen Oker, José E. Crespo, Clément Vinauger, Chloé Lahondère, in the recorded order; title verbatim; Insects 13(1) 92, issued 2022-01-14; CC BY 4.0 (vor); relation empty, no update-to. Page: "Insects 2022, 13(1), 92", metadata CC BY 3.0. Met; as recorded.

Bibliographic faults 2 (lines 2, 3); licence faults 0. source.access right on all five.

## Names

- Odocoileus virginianus, Culex quinquefasciatus: EXACT ACCEPTED in docs/views/gaps/gbif-names.tsv.
- Lymantria xylina: gbif-names.tsv gives "EXACT DOUBTFUL". Wikipedia taxobox, verbatim: "Lymantria xylina C. Swinhoe, 1903", "Erebidae", synonym "Liparis xylina". Main already files the name (recheck-2-fixed.jsonl:8). Accepted; uncounted remark that GBIF flags it doubtful.
- Culex tarsalis: not in gbif-names.tsv; GBIF refused. Accepted as printed (Culex tarsalis Coquillett, standard vector name, no conflicting usage on main).
- Laboratory strains (lines 4, 5): the YOLO (BEI NR-43026) and JHB (BEI NR-43025) strains are laboratory colonies of the wild species, verbatim "Cx. quinquefasciatus (JHB strain, BEI Resources (NR-43025))" and "Cx. tarsalis (YOLO strain, BEI Resources (NR-43026))". A strain is not a cultivar or a domestic breed. Main accepts laboratory strains and colonies at species rank: Long-Evans rats as Rattus norvegicus (desk-d170.jsonl:3; audits 255 and 269), laboratory moth colonies (desk-d171.jsonl:6, desk-d189.jsonl:4), oa-14.jsonl:58. Acceptable.

Name faults 0.

## Duplicates

- Line 1: **repeat.** origin/main docs/views/audit/corrected/squirrel-deer-rabbit.jsonl:100 is the same paper (10.1002/wsb.438, same authors, access "abstract"), grade m, under colour_vision, value "more sensitive to short wavelengths than long; some sensitivity to ultraviolet", quote containing this record's sentence verbatim ("... Our findings also suggest the deer have some sensitivity to ultraviolet light."), method "behavioural: forced-choice detection", note "seven deer". docs/views/audit/ALL.jsonl:4552 (squirrel-deer-rabbit:101) gives it verdict "stands". This record files the same sentence as a narrower finding under another trait key. The unit's note says the abstract's short-wavelength sentence was "not filed"; it is on main.
- Lines 2 and 3: no Lymantria xylina behaviour_vision row and no insects16040338 on main. Main's only L. xylina evidence is interommatidial_deg from Jiang et al. 2025, Insects 16: 1122 (sweep-11.jsonl:15, recheck-2-fixed.jsonl:8, ALL.jsonl:4644). That row is sourced; the record's note calls it "an unsourced interommatidial row" (uncounted, replacement below). Not a repeat.
- Lines 4 and 5: no Culex tarsalis or Culex quinquefasciatus sense_* row on main (Cx. quinquefasciatus has only canon-4.jsonl:49, acuity_cpd from Feller et al. 2021). The same paper is on main as desk-d195.jsonl:6 (Culex territans, sense_chemical, null), whose `conditions` carry "Cx. quinquefasciatus and Cx. tarsalis landed on the warm target under CO2 in the same assay (Table 1)" and whose `note` carries "landed on the warm target at about 4 to 12%". That main row carries that the two species respond under CO2, but not that the response depends on CO2 (falls without it) and not the dose result. Partial overlap with a main row's note; I judge it not a counted repeat, because the record's value (dependence on CO2) is not in the main row. It does mean the record's "text read gives no landing percentages" is answered on main already.

Duplicates 1 (line 1). Contradictions 0.

## Per-record findings

### Line 1, Odocoileus virginianus, behaviour_vision, Cohen et al. 2014

DOAJ abstract, verbatim: "Our findings also suggest the deer have some sensitivity to ultraviolet light." Preceded by "We confirm that these cone photoreceptors contribute to deer behavior, and that deer have a greater..." (truncated by the tool). MATCH, whole sentence, 12 words. Crossref abstract summary: seven deer, lit against unlit LEDs at different wavelengths and intensities (tool summary).

**Error (repeat of main).** Same paper, same sentence, same grade and access as corrected/squirrel-deer-rabbit.jsonl:100 (verdict "stands"). Unfixable as a new row, drop. If the owner wants the 7-deer design and logistic-threshold method on main, that goes as a `conditions`/`method` fix to the main row.

Uncounted: the value drops the sentence's "suggest" (the note carries it); a re-file would read "some sensitivity to ultraviolet light suggested (no UV threshold reported in the abstract)". Grade m right. Licence rule met as an abstract (see above).

Line 1: 1 fault.

### Line 2, Lymantria xylina, behaviour_vision, lamp catch

Abstract: "The insecticidal lamp with a peak wavelength of 363 nm was most effective for male trapping." MATCH (the tool confirmed the exact sentence; preceded by "The results showed that all lamps attracted both males and females, but females were..."), whole sentence, 16 words. Results 3.1.1: 2911 adults at peak emergence (4 to 6 June 2019), 2902 males and 9 females; "The L360 lamp exhibited the highest capture rates for male moths"; at most three females at any lamp (L370); L360 took 31.0% of male captures at peak and 39.5% in the late peak; "(F = 2.593, df = 4, p = 0.101)" at peak, F = 5.367, df = 4, p = 0.007 in the late peak (tool summary for the late-peak figures). Methods 2.3.1, verbatim: "Adults of L. xylina were trapped during the late peak (26–28 June and 3–5 July 2018)."; lamps placed randomly each day, 2 m high, about 50 m apart, 19:00 to 04:00 (tool summary). Introduction peaks 363, 365, 368, 378 and 439 nm against labels L360 to L405; Table 1 is an image (tool summary).

**Error (null result omitted).** At peak emergence, where 2902 of the males were caught and which the record's catch totals describe, the lamps did not differ significantly (p = 0.101); the "most effective" result is significant only in the 2018 late-peak trapping (p = 0.007). The conditions give neither. Fixable.

**Error (bibliographic).** Issue 4 omitted. Fixable.

Uncounted: the note's "unsourced interommatidial row" is wrong (main row cites Jiang et al. 2025). Grade m right. Trait key behaviour_vision fits (owner's moth-lamp reading).

Line 2: 2 faults.

### Line 3, Lymantria xylina, behaviour_vision, female phototaxis

Abstract: "Only 14.6% of non-ovipositing females showed phototactic behavior, and only 0.6% flew directly toward the lamp." MATCH (exact sentence confirmed; preceded by "Females, when laying eggs, did not exhibit phototactic behavior."), whole sentence, 16 words. Results 3.4: "Among 43 non-ovipositing female moths, 7 females exhibited displacement behavior close to the lamp" (Test 1, 16.3%, none flew directly, tool summary); "Only 1 of the 78 non-ovipositing female moths flew directly toward the lamp" and "9 females exhibited displacement behavior close to the lamp" (Test 2, 12.8%); Test 3, 30 egg-laying females, 0%; "Non-ovipositing female moths exhibited a low phototactic response rate, averaging 14.6%."; "Male moths exhibited much a higher phototactic response rate, averaging 57.7%," and "and 33.3% (45 males) flew directly toward the lamp." No statistical test compares the sexes (tool summary). Methods 2.3.4: "using an L360 insecticidal lamp (25 W) as the light source"; "Net cages containing L. xylina adults were placed 7.0 m from the light source."; "conducted in a dark room measuring 7.2 m × 6 m × 3 m"; lamp on 21:00 to 04:00.

**Error (sample and comparison omitted; stated as unavailable).** The conditions say the sentences read do not give how many females the 14.6% rests on or how the tests were pooled; Results 3.4 gives 7 of 43 and 10 of 78, and 14.6% is the average of the two tests' rates (16.3% and 12.8%; 0.6% matches the average of 0 of 43 and 1 of 78, i.e. one female, my arithmetic). The males tested alongside (57.7% responding, 33.3% flying directly) are the comparison that gives "only" its meaning and are left out. Fixable.

**Error (bibliographic).** Issue 4 omitted. Fixable.

Grade m right. Trait key behaviour_vision fits.

Line 3: 2 faults.

### Lines 4 and 5, Culex tarsalis and Culex quinquefasciatus, sense_thermal, Reinhold et al. 2022

Section 3.2, verbatim: "The heat-seeking responses of both Cx. tarsalis and Cx. quinquefasciatus were contingent on exposure to CO2" / "(Table 1; Supplementary Tables S1 and S2)." MATCH bar the trailing table reference, 16 words; preceded by "Therefore, the responses of Cx. territans were excluded from subsequent analysis." The paragraph continues, verbatim: "The response of both species towards Peltierwarm (30–50 °C) was significantly higher after exposure to CO2" / "at 30,000 ppm when compared to 2100 ppm (Table 1; Supplementary Tables S1 and S2)."; "Post exposure to CO2 at 30,000 ppm, the proportion of heat-seeking Cx. tarsalis and Cx. quinquefasciatus increased" / "significantly with the temperature of Peltierwarm and was the highest at 40 and 45 °C (Figure 6A; Table 1)."; "Between the two species, post exposure to CO2 at 30,000 ppm, the magnitude of heat-seeking response of Cx. tarsalis" / "towards Peltierwarm (30–50 °C) was significantly higher when compared to Cx. quinquefasciatus (Chisq: 15.22, p < 0.01;"; "Post exposure to 2100 ppm CO2, the heat-seeking responses of Cx. tarsalis and Cx. quinquefasciatus were not" / "significantly different between 30 and 40 °C (Figure 6A; Table 1)."; "However, the proportion of heat-seeking Cx. quinquefasciatus towards Peltierwarm set at 45 and 50 °C upon exposure" / "to 2100 ppm of CO2 was significantly more than Cx. tarsalis". Strains as under Names.

Two records from one sentence naming both species: right, as in audits 299 and 300, since each states its own species' half and the sentence makes the same claim of each.

**Error, each line (effect sizes and species contrast omitted).** The value "contingent on exposure to CO2" stands, but the record omits the paragraph's dose result (response significantly higher at 30,000 than 2100 ppm), the temperature peak (40 and 45 °C at 30,000 ppm), and the species contrast that runs in opposite directions by dose (Cx. tarsalis higher at 30,000 ppm, Chisq 15.22, p < 0.01; Cx. quinquefasciatus higher at 45 and 50 °C under 2100 ppm). For a record filed per species, the comparison with the other species is that species' effect size. No landing rate is given either, though main's Cx. territans row from the same paper already carries "about 4 to 12%". Fixable.

Uncounted: the quote omits the printed table reference "(Table 1; Supplementary Tables S1 and S2)" without a mark (audit 266 left a dropped reference marker uncounted; note it). Grade m right on each line. Trait: sense_thermal fits heat-seeking; main files the same assay's Cx. territans null under sense_chemical (owner question 3).

Line 4: 1 fault. Line 5: 1 fault.

## Trait key

- Line 1, behaviour_vision: would fit, but main files the same finding under colour_vision; the record falls as a repeat.
- Lines 2 and 3, behaviour_vision: fit (owner's moth-lamp reading).
- Lines 4 and 5, sense_thermal: fit; see owner question 3.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Odocoileus virginianus, behaviour_vision, some UV sensitivity | error, unfixable, drop | whole record | Quote MATCH (12 words); same paper and sentence already on main, corrected/squirrel-deer-rabbit.jsonl:100 (colour_vision, verdict stands) |
| 2 | Lymantria xylina, behaviour_vision, 363 nm lamp best for males | error, fixable | conditions, journal | Quote MATCH (16 words); no significant lamp difference at peak emergence (p = 0.101) omitted; issue 4 omitted |
| 3 | Lymantria xylina, behaviour_vision, 14.6% and 0.6% of females | error, fixable | conditions, journal | Quote MATCH (16 words); per-test n (7/43, 10/78; 0.6% is one female) called unavailable, male 57.7%/33.3% omitted; issue 4 omitted |
| 4 | Culex tarsalis, sense_thermal, heat-seeking contingent on CO2 | error, fixable | conditions | Quote MATCH (16 words); dose result, 40 to 45 °C peak and species contrast (Chisq 15.22) omitted |
| 5 | Culex quinquefasciatus, sense_thermal, heat-seeking contingent on CO2 | error, fixable | conditions | Quote MATCH (16 words); same omission, including its higher response at 45 and 50 °C under 2100 ppm |

Faults per record: line 1: 1; line 2: 2; line 3: 2; line 4: 1; line 5: 1. 7 faults in 5 records; 5 of 5 records in error (100%): duplicates 1 (line 1); scientific-context 4 (lines 2 to 5); bibliographic 2 (lines 2, 3); names 0; quote-form 0; licence 0; trait key 0; grading 0.

Pooled with audits 172 to 304: 322 of 722 evidence records (44.6%; 317 of 717 before this audit, 5 of 5 here). No search records.

## Replacement text

Line 1: unfixable as a new row, drop (repeat of corrected/squirrel-deer-rabbit.jsonl:100). Optional fix to that main row, `conditions`: "7 deer, light-adapted; automated forced-choice discrimination of lit from unlit monochromatic LEDs, intensity lowered to threshold, logistic function per deer; abstract only (no licence stated), wavelengths and intensities not given in the abstract".

Line 2:
- `source.journal`: replace "Insects 16: 338" with "Insects 16(4): 338".
- `conditions`: replace "the page text read does not map the L-labels to peak wavelengths other than 363 nm for the most effective lamp, and gives no replicate count;" with "at peak emergence (4-6 June 2019) the lamps did not differ significantly in male catch (F = 2.593, df = 4, p = 0.101; L360 took 31.0% of males), in the 2018 late-peak trapping they did (F = 5.367, df = 4, p = 0.007; L360 39.5%); the Discussion calls L360 the 363 nm lamp, the Introduction lists 363, 365, 368, 378 and 439 nm, and the label-to-peak mapping for the rest is in Table 1 (an image, not read); no replicate count beyond the trapping nights;".
- `note` (uncounted): replace "no earlier row on main for any trait except an unsourced interommatidial row, none with this DOI" with "main's only row for the species is interommatidial_deg from Jiang et al. 2025, Insects 16: 1122 (recheck-2-fixed.jsonl:8); none with this DOI".

Line 3:
- `source.journal`: replace "Insects 16: 338" with "Insects 16(4): 338".
- `conditions`: replace "the Results give 14.6% as an average response rate of non-ovipositing females; the sentences read do not say how many females the 14.6% rests on or how the tests were pooled; male rates are not quoted here" with "Results 3.4: Test 1, 7 of 43 non-ovipositing females (16.3%) moved toward the lamp and none flew directly to it; Test 2, 1 of 78 flew directly to the lamp and 9 more moved toward it (12.8%); 14.6% is given as an average of the tests, and 0.6% matches the average of 0 of 43 and 1 of 78, so it is one female; males in the same tests averaged 57.7% responding and 33.3% (45 males) flying directly to the lamp; no statistical test compares the sexes; 25 W L360 lamp, dark room 7.2 x 6 x 3 m, lamp on 21:00 to 04:00".

Lines 4 and 5:
- `conditions`: replace "the sentence read names both species together and the text read gives no landing percentages (Figure 6 and Tables 1 to 3 not read);" with "Results 3.2: both species responded significantly more after 30,000 than after 2100 ppm CO2, and at 30,000 ppm the proportion heat-seeking rose with target temperature to a peak at 40 and 45 °C; at 30,000 ppm Cx. tarsalis responded significantly more than Cx. quinquefasciatus (Chisq 15.22, p < 0.01), while after 2100 ppm the two did not differ at 30 to 40 °C and Cx. quinquefasciatus responded significantly more at 45 and 50 °C; landing proportions are in Table 1 (not read here; main's Cx. territans row from this paper gives about 4 to 12%);".
- `note` (uncounted): append "The printed sentence ends with '(Table 1; Supplementary Tables S1 and S2)', omitted from the quote."

## Owner questions (the unit's, answered where I could)

1. Lab-colony strains (Culex JHB and YOLO): acceptable at species rank. A laboratory strain is not a cultivar or domestic breed, and main already files Long-Evans rats as Rattus norvegicus (audits 255, 269) and laboratory moth colonies (desk-d171, desk-d189). Keep the strain and BEI number in `conditions`, as the records do.
2. Odocoileus abstract-only record with no open licence: the licence rule allows a publisher or index abstract of a closed article as source.access "abstract" with "partial": true, which the record meets (Crossref licence is Wiley's own terms; DOAJ shows no licence). The record still falls, as a repeat of corrected/squirrel-deer-rabbit.jsonl:100.
3. New: main files Reinhold et al.'s Cx. territans null from this same CO2-gated heat-seeking assay under sense_chemical (desk-d195.jsonl:6), and these records under sense_thermal. Should one assay sit under both keys (CO2 for the null, heat for the positive), or should the pair be aligned?

## Progress note

Accurate on citations, licences and the lab-strain question. Its duplicate index missed docs/views/audit/corrected, where the deer paper and sentence already sit (line 1), and its note on main's Lymantria row ("unsourced") is wrong. The Lymantria leads line (Table 1 maps the L-labels) is right. The Records list does not carry the faults above.

Verdict: 5 of 5 records in error (100%), 7 faults, above the 5% bar; pooled 322 of 722 (44.6%). Error lines: 1, 2, 3, 4 and 5. Lines 2 to 5 are fixable with the replacement text above; line 1 should be dropped.

This report is model output and carries no authority.
