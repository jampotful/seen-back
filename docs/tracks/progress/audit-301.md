# audit-301: desk-d216, evidence lines 1 to 7 (all 7 records)

Audited 31 October 2026 from the desk-d216 files present untracked in the worktree (docs/tracks/progress/desk-d216.md and docs/views/evidence/desk-d216.jsonl, 7 lines; neither committed here, neither edited). HEAD 63678788 equals origin/main and holds desk-d215. `tools/senses/check.py` on the evidence file: 7 records, 0 problems. Quote lengths (`len(q.split())`), lines 1 to 7: 30, 30, 27, 15, 15, 14, 18, all within 40. The unit has evidence records only (no search records), so every record was judged and there is no sample. Rules applied: the shared brief's grade, name and duplicate rules, audit-300 as the format model, and the caller's per-record method; the brief's search-record and plant-screening parts are superseded for this unit.

Duplicates: git grep on origin/main across docs and src (evidence, audit/corrected, audit/ALL.jsonl, searched, sheets, gaps, codex-findings, progress notes) for "Scylla", "paramamosain", "mud crab", "11248", "Kawamura", "Trabala", "vishnou", "20124", "Lasiocampid", "Hippophae", "Ateles", "spider monkey", "0080621", "Sarrafchi", "Laska", "Platydoras", "armatulus", "Raphael", "Doradidae", "0026479", "Cyprinella", "venusta", "blacktail", "0137290", "Crovo", "Megalechis", "thoracata", "Callichthy", "0121219", "Hadjiaghai", "Ladich", every trait included.

Sources opened (WebFetch): peerj.com/articles/11248 (three passes); peerj.com/articles/20124 (two passes); journals.plos.org article pages for e0080621 (two passes), e0026479 (two passes), e0137290 (one pass with an unencoded DOI returned a different article, PLoS ONE 11(3): e0152048, and was discarded; two passes with the encoded DOI), e0121219 (two passes); api.crossref.org/works for all six DOIs (curl to Crossref is refused by the egress proxy here, so read through WebFetch; one rate-limited fetch repeated). Names: sealifebase.se species 83566, fishbase.net.br summaries 47627 and 2912, mammaldiversity.org taxon 1000770, insecta.pro taxonomy 18984, en.wikipedia.org Trabala_vishnou and Megalechis, each returned by my WebSearch. api.gbif.org species/match refused (PROVENANCE_REQUIRED, not retried); gbif.org/species/5863635 failed at the site; a tb.plazi.org page returned only a redirect placeholder. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries with verbatim pieces of about 120 characters, so quotes were checked as MATCH/MISMATCH from piecewise verbatim returns; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 7 WebSearch and about 25 WebFetch calls used.

## Bibliographic and licence

- Lines 1 and 2, Kawamura et al. 2021, Crossref: Gunzo Kawamura, Chi Keong Loke, Leong Seng Lim, Annita Seok Kian Yong, Saleem Mustafa, in the recorded order; title verbatim; PeerJ 9 e11248, no issue, issued 2021-04-21; licence CC BY 4.0 (unspecified version); relation has-review only; no update-to. Page: "Creative Commons Attribution License", PeerJ 9:e11248, 2021. Met.
- Line 3, Liu et al. 2025, Crossref: Yonghua Liu, Kexu An, Shuo Tang, Jiangshuai Feng, Xiongfei Yan; title "Electroantennogram and Olfactory behavioral responses of Trabala vishnou gigantina (Lepidoptera: Lasiocampidae) to herbivore induced Hippophae rhamnoides leaf volatiles", as recorded and as on the page; PeerJ 13 e20124, issued 2025-10-01; CC BY 4.0; relation empty. Page: Creative Commons Attribution License. Met. Uncounted: the note says Crossref gives the title "with the closing phrase on herbivore-induced sea buckthorn leaf volatiles"; Crossref prints "to herbivore induced Hippophae rhamnoides leaf volatiles", the same as the page and the record. Replacement below.
- Line 4, Sarrafchi et al. 2013, Crossref: Amir Sarrafchi, Anna M. E. Odhammer, Laura Teresa Hernandez Salazar, Matthias Laska; title verbatim; PLoS ONE 8(11) e80621, issued 2013-11-20; CC BY 4.0; relation empty. Page: Creative Commons Attribution License. Met.
- Line 5, Papes and Ladich 2011, Crossref: Sandra Papes, Friedrich Ladich; title verbatim; PLoS ONE 6(10) e26479, issued 2011-10-17; CC BY 4.0. Page: Creative Commons Attribution License, published October 17, 2011. Met.
- Line 6, Crovo et al. 2015, Crossref: Jenna A. Crovo, Mary T. Mendonça, Daniel E. Holt, Carol E. Johnston; title verbatim; PLOS ONE 10(9) e0137290, issued 2015-09-23; CC BY 4.0 (vor); relation empty. My two passes of the page also returned no licence or citation line (title, authors and abstract only, tool summary), as the note says. PLOS ONE page with a Crossref vor CC BY 4.0 licence and no conflicting tag: met, as the note records it.
- Line 7, Hadjiaghai and Ladich 2015, Crossref: Oliwia Hadjiaghai, Friedrich Ladich; title verbatim; PLOS ONE 10(3) e0121219, issued 2015-03-16; CC BY 4.0 (vor). Page: Creative Commons Attribution License (CC BY 4.0). Met.

Bibliographic faults counted 0 (1 uncounted note fix, line 3); licence faults 0.

## Names

None of the six names is in docs/views/gaps/gbif-names.tsv (checked). GBIF API refused here.
- Scylla paramamosain (lines 1, 2): SeaLifeBase species page "Scylla paramamosain Estampador, 1949", Portunidae, Decapoda, under its own name. Accepted (aggregator page; no explicit status line).
- Trabala vishnou (line 3): the paper names "Trabala vishnou gigantina Yang, 1978" and never uses the word subspecies. insecta.pro (genus Trabala Walker, 1855) lists "T. v. gigantina, T. v. singhala" under Trabala vishnou (Lefebvre, 1827); Wikipedia lists four subspecies including gigantina Yang, 1978. So gigantina is a subspecies of T. vishnou, and filing at species rank under Trabala vishnou is valid at that rank. Main is mixed (Gallus gallus domesticus and Coturnix coturnix japonica at rank species; Trachemys scripta elegans and Canis lupus familiaris at rank subspecies), so species rank with the subspecies stated in conditions is within main's practice. Not counted; owner question 2.
- Ateles geoffroyi (line 4): Mammal Diversity Database taxon 1000770, Ateles geoffroyi Kuhl, 1820, Atelidae, Primates, valid species. Accepted.
- Platydoras armatulus (line 5): FishBase summary 47627, Platydoras armatulus (Valenciennes, 1840), Doradidae (Doradinae), Siluriformes. Accepted.
- Cyprinella venusta (line 6): FishBase summary 2912, Cyprinella venusta Girard, 1856, Leuciscidae (Pogonichthyinae), Cypriniformes; family as recorded. Accepted. Main files Cyprinella lutrensis in the gaps under whatever family the backbone gives; not checked further.
- Megalechis thoracata (line 7): Wikipedia's Megalechis page gives M. thoracata (Valenciennes, 1840) as valid, but says a 2005 synonymy moved the name: the species formerly called M. thoracata is now M. picta, and M. thoracata now applies to the former M. personata. The paper is from 2015 and uses M. thoracata; whether its aquarium-trade fish were identified under the post-2005 usage is not stated in what I read. Not counted; owner question 3.

Name faults 0.

## Duplicates

- Lines 1, 2: no Scylla row on main; "paramamosain" appears only in desk-d197.md:15 in another paper's context. Not a repeat.
- Line 3: no Trabala, vishnou or 20124 anywhere on main. Hippophae on main is the plant (desk-d40:3 GA3 germination row; sweep-32:12 and desk-d40 search records), none citing this paper. Lasiocampidae rows are Tolype and Artace opsin and diel rows. Not a repeat.
- Line 4: Ateles on main is Ateles paniscus ocular_media_t50_nm (corrected/methods:1028) and genus Ateles lambda_max_nm (oa-2:3504, :3505); no A. geoffroyi row, no 0080621, no Sarrafchi. "Laska" hits are plant search records (an unrelated author string match). Not a repeat.
- Lines 5 to 7: Platydoras, Cyprinella venusta and Megalechis occur on main only in desk-d160.md:16 (and Platydoras in desk-d212.md:16) as unopened leads; Doradidae rows on main are Amblydoras affinis and Megalodoras uranoscopus (desk-d184); Cyprinella rows are C. lutrensis visual_chromophore. Not repeats.

Duplicates 0. Contradictions 0.

## Per-record findings

### Line 1, Scylla paramamosain, sense_chemical, Kawamura et al. 2021

Abstract, verbatim in pieces: "The dactyls of swimming legs and the antennules were chemosensitive, but not mechanosensitive" / "and vice versa for the antennae." / "However, the mouthparts, claws, and walking legs were chemo- and mechanosensitive." MATCH, two whole consecutive sentences from one section (accepted form, audits 244 and 256), 30 words; value says no more. Grade m right. Trait key: a living crab's cardiac and feeding response to a dissolved food stimulus is a living chemical response; sense_chemical fits (the owner's "no extracts" reading concerns a plant as the sensor, not the stimulus offered to an animal).

Methods, verbatim: "A total of 20 female and male specimens of adult mud crab, S. paramamosain," / "(9–11 cm in carapace width, 80–100 g in body weight)"; "Fifty-four stable ECGs were obtained from three test crabs: constant interbeat intervals (IBIs) of 0.5 −0.8 s" / "and constant amplitude of 0.3 −0.4 mV."; "A total of 63 video recordings were analyzed, which were played back to examine the feeding behaviour on a computer screen." (after the sentence on observing other appendages "During the stimulation at each appendage"); behavioural assay "and a total of 30 video recordings were analyzed."

**Error (sample misstated).** The conditions say "54 stable recordings from 63 attempts". The 63 are video recordings of the appendage-stimulation trials analysed for feeding behaviour, not ECG attempts; the paper gives no number of ECG attempts. The 20 crabs bought are also not stated (only the three used for ECG).

**Error (design detail omitted, same field).** The value says the antennae are not chemosensitive. Methods: "To prevent the diffusion of the sugarcane juice from the antennule to the antennae, the antennules were cauterised" / "after applying the sugarcane juice."; Results: "The crab with the antennules showed the heartbeat response, while those with the cauterised antennules showed no response" / "to the stimulation by the sugarcane juice application given to the antennae." So juice on the antennae did move the heart while the antennules were intact; the negative result for the antennae rests on crabs with cauterised antennules. The conditions do not say so. Fixable; replacement below.

Line 1: 2 faults, 1 record in error.

### Line 2, Scylla paramamosain, sense_touch, Kawamura et al. 2021

Same quote, MATCH, 30 words. Trait key sense_touch fits (micropipette touch). Value: "antennae mechanosensitive (and not chemosensitive)" restates "vice versa for the antennae", which the Results confirm ("the antennae were touch-sensitive (Table 2), but not chemosensitive (Table 1)"); swimming-leg dactyls "no response was observed by mechanical touch stimulation (Fig. 2B)"; antennule flagella no touch response (tool summary). Value says no more than the quote. Results: "statistically significant responses (P < 0.05) were observed for the walking legs, claws, antennae" / " and mouthparts of three specimens." Table 2 gives each of three crabs (tool summary).

**Error (sample misstated).** Same "54 stable recordings from 63 attempts" as line 1. Fixable.

Uncounted: conditions could add the per-crab result of Table 2 (all three crabs).

Line 2: 1 fault.

### Line 3, Trabala vishnou, sense_chemical, Liu et al. 2025

Table 3, verbatim: female row "0.33 ± 0.16d | 0.78 ± 0.23c | 1.55 ± 0.46b | 2.45 ± 0.54a | 2.53 ± 0.38a"; male "0.21 ± 0.09c | 0.48 ± 0.13b | 0.95 ± 0.24b | 1.86 ± 0.48a | 2.24 ± 0.53a"; headers "Compounds", "Sex", "Relative EAG response (μ g/μ L)", no caption. MATCH, whole row, 27 words. Units from Methods (mV): as recorded. Grade m: one named (sub)species measured; right. Trait key: an insect's antennal response to plant volatiles; fits.

Results, verbatim: "At a concentration of 50 µg/µL, the relative EAG responses of imagoes were all significantly higher" / "than those at a concentration of 10 µg/µL (P < 0.05), with hexyl 2-methyl butyrate having the highest relative values." / "When the volatile concentration increased to 100 µg/µL, the relative values of all EAG responses were maximized," / "except for those of hexyl 2-methyl butyrate and Leaf acetate, which showed no significant difference" / "from the values at a concentration of 50 µg/µL (P > 0.05)." Methods: "was calculated using the Duncan multiple comparisons method."

**Error (null result omitted and contradicted).** For this very compound the response at 100 µg/µL did not differ from 50 µg/µL (2.45a and 2.53a; P > 0.05). The conditions instead say "the top response (100 ug/uL) is the highest tested, not a saturation point", which runs against the paper's own test, and say the letters' "test not read" when the Methods name Duncan's test. Fixable; replacement below.

Uncounted: Results "with females consistently showed stronger responses than males" against Discussion "The responses of female and male T. vishnou gigantina imagoes to the same H. rhamnoides volatiles were basically the same." could be added; the note's Crossref title remark (above).

Line 3: 1 fault.

### Line 4, Ateles geoffroyi, sense_chemical, Sarrafchi et al. 2013

Results, verbatim: "In all cases, threshold values correspond to gas phase concentrations ≤1 ppb (parts per billion)." MATCH, whole sentence, 15 words. "All four animals significantly distinguished dilutions as low as 1:107 2-propylthietane, 1:3•108 2,2-dimethylthietane," / "1:107 3-mercapto-3-methylbutan-1-ol, 1:107 3-mercapto-3-methylbutyl formate, 1:107 3-methyl-1-butanethiol," / "and 1:3•106 methyl-2-phenylethyl sulfide from the solvent" (exponents flattened by the tool): the conditions' 1:3x10^6 to 1:3x10^8 is right. Four females aged 6 to 14, 30 trials per step, binomial criterion (tool summary): as recorded. Grade m right.

Discussion, verbatim: "The only known mammalian predators of the spider monkey, a comparatively large-bodied New World primate, are the jaguar" / "(Panthera onca) and the cougar (Puma concolor)" / "two felines whose urine, faeces and anal gland secretions have not yet been analyzed" / "for the presence of the odorants used in the present study." and "Thus, it seems unlikely that spider monkeys are regularly exposed to any of the six predator odorants tested here" / ", at least in the context of predator avoidance." Sources of the odorants (Methods, tool summary): mustelids (stoat, ferret), cat and bobcat urine, skunk anal gland, red fox urine.

**Error (source misstated).** The conditions say the "predator odorants are those of the monkeys' possible carnivore predators per the paper's framing (not checked)". The paper says the opposite: the odorants come from mustelids, small felids, skunk and fox, the monkeys' only known predators have not been analysed for them, and the monkeys are unlikely to meet them as predator cues. Fixable.

Uncounted: "With the exception of 2,2-dimethylthietane and 3-mercapto-3-methylbutan-1-ol, individual animals even reached" / "threshold values as low as 10 ppt (parts per trillion) with all odorants tested."; individual thresholds spread by factors of 10 to 1,000 by odorant and no significant difference in sensitivity between the six odorants (tool summary). Worth adding.

Line 4: 1 fault.

### Line 5, Platydoras armatulus, sense_hearing, Papes and Ladich 2011

Results, verbatim: "Best hearing occurred at 0.5 and 1 kHz at both temperatures." My fetch did not return the trailing "(Tab. 3, Fig. 5)" that the record's quote carries (the desk reports it from a second fetch); MATCH on the words returned, the figure reference unconfirmed, 15 words as recorded. Value says no more. Next sentences, verbatim: "A two-factorial ANOVA revealed that the auditory sensitivity differed between temperatures (F2,126 = 13.46, p<0.001)" / "and that there was a significant interaction between temperature and frequency (F10,126 = 2.15, p≤0.05)."; "A Bonferroni Post-hoc test showed a significant difference between the 30°C and both 22°C audiograms" / "(22°C versus 30°C: p≤0.001; 30°C versus 22°C repeated: p≤0.001; 22°C versus 22°C repeated: p≤0.001)." Methods: "Hearing thresholds were determined at frequencies of 0.1, 0.2, 0.5, 1, 2 and 4 kHz, presented in random order." N = 8, sizes and order 22, 30, 22 °C: as recorded.

**Error (design confound omitted, order).** The conditions give the order 22, 30, 22 °C and "hearing sensitivity was higher at 30 C", but not that the first and repeated 22 °C audiograms also differed (p ≤ 0.001), so the temperature effect is not separated from order or time in captivity. Fixable.

Uncounted: "frequency range tested not read" can be replaced by the tested frequencies above.

Line 5: 1 fault.

### Line 6, Cyprinella venusta, sense_hearing, Crovo et al. 2015

Results, verbatim: "The pressure audiogram generated from control individuals showed that the auditory thresholds" / "of C. venusta were most sensitive at 300 and 400 Hz (ncontrol = 5)." / "The auditory thresholds were 85 dB at 300 Hz and 82 at 400 Hz." / "After 2 hours of traffic playback, auditory thresholds were elevated at 300 and 400 Hz (ntraffic = 5)." / "Auditory thresholds shifted upward significantly by 7 dB at 300 Hz (p = 0.020) and 9 dB at 400 Hz (p = 0.025)." / "Auditory sensitivity at all other test frequencies remained virtually unchanged between the two groups (Fig 3)." Quote MATCH, whole sentence, 14 words; value says no more (the dB unit stated as taken from context). Grade m right.

AEP Methods, verbatim: "Individuals were exposed to the same traffic recording looped for a period of 2 hours at 140 dB re 1 μPa (n = 5)."; "Individuals in the control treatment were exposed to a period of silence for 2 hours;"; "After each treatment, test fish were wrapped in gauze and restrained in a clay bed". The cortisol section: "Each fish received the control and noise treatment on separate days;". No AEP sentence says whether control and traffic fish were different individuals.

**Error (sample composition asserted beyond the source).** The conditions call the controls "a separate set of fish from the traffic-noise group". The paper does not say so, and its other experiment gave each fish both treatments. Fixable.

Uncounted: the shift sizes (7 and 9 dB) could be added; "body size only in S1 Table" should read that S1 Table lists weights and cortisol values per test fish and no length is given.

Line 6: 1 fault.

### Line 7, Megalechis thoracata, sense_hearing, Hadjiaghai and Ladich 2015

Results, verbatim: "Hearing curves of both sexes were U-shaped with best auditory sensitivities between 0.2 and 1 kHz (Fig. 12)." MATCH, whole sentence, 18 words; value says no more. Also verbatim: "Hearing abilities decreased rapidly above 1 kHz."; "Thresholds increased by 41 dB between 1 and 4 kHz in males and females."; "Overall, hearing thresholds did not differ between sexes (two-way ANOVA: F8, 89 = 1.2, n. s.)."; "Females had better hearing between 0.1 and 1 kHz (two-way ANOVA: F 1, 50 = 7.72, p < 0.01)" / "but not between 1 and 4 kHz (two-way ANOVA: F 1, 49 = 0.007, n.s.)."; "Thresholds obtained for males (N = 6) and females (N = 6) were compared by a two-way ANOVA". The sex difference and the null are both in the conditions. Grade m right.

Animals, verbatim: "Seventeen specimens of M. thoracata were used for the study: seven subadult males" / "nine subadult females (84–102 mm, 9.8–17.1 g) and one adult male (126 mm, 32.9 g)". Uncounted: the conditions give only "subadult males 93 to 104 mm total length"; the females' size and the one adult male (which may or may not be among the six males in the audiograms) belong in sample composition; "41 dB between 1 and 4 kHz" could be added.

Line 7: 0 counted.

## Trait key

- Line 1, sense_chemical: fits (living crab's cardiac and feeding responses to a dissolved food stimulus). The value also carries mechanosensitivity clauses from the same sentences; tolerable since they are in the quote and line 2 files touch separately.
- Line 2, sense_touch: fits.
- Line 3, sense_chemical (EAG to plant volatiles): fits.
- Line 4, sense_chemical (olfactory threshold): fits.
- Lines 5 to 7, sense_hearing (best frequency strings; one threshold pair): fit, as main's Doradidae sense_hearing rows (desk-d184).

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Scylla paramamosain, sense_chemical, appendage map | error, fixable | conditions | Quote MATCH (30 words); "54 stable recordings from 63 attempts" misreads 63 feeding videos; antennae's chemo-negative result rests on cauterised antennules, not stated |
| 2 | Scylla paramamosain, sense_touch, appendage map | error, fixable | conditions | Quote MATCH (30 words), trait fits; same 54/63 misstatement |
| 3 | Trabala vishnou (gigantina), sense_chemical, female EAG 2.53 at 100 ug/uL | error, fixable | conditions | Row MATCH (27 words); 100 vs 50 ug/uL not significant for this compound, yet conditions say "not a saturation point" and "test not read" (Duncan); species rank for the subspecies acceptable |
| 4 | Ateles geoffroyi, sense_chemical, thresholds ≤1 ppb | error, fixable | conditions | Quote MATCH (15 words); conditions say the odorants are the monkeys' predators' when the paper says their predators were never analysed and exposure is unlikely |
| 5 | Platydoras armatulus, sense_hearing, best 0.5 and 1 kHz | error, fixable | conditions | Quote MATCH (15 words); the two 22 °C audiograms differed (p ≤ 0.001), an order confound left out |
| 6 | Cyprinella venusta, sense_hearing, 85 dB at 300 Hz, 82 dB at 400 Hz | error, fixable | conditions | Quote MATCH (14 words); "a separate set of fish" is not in the paper |
| 7 | Megalechis thoracata, sense_hearing, best 0.2 to 1 kHz | stands (uncounted fixes) | conditions | Quote MATCH (18 words); sex difference and null recorded; female and adult-male sizes missing |

Faults per record: line 1: 2; line 2: 1; line 3: 1; line 4: 1; line 5: 1; line 6: 1; line 7: 0. 7 faults in 7 records; 6 of 7 records in error (85.7%): scientific-context 6 (lines 1 to 6); duplicates 0; quote-form 0; licence 0; bibliographic 0; name 0; trait key 0; grading 0.

Pooled with audits 172 to 300: 305 of 701 evidence records (43.5%; 299 of 694 before this audit, and 6 of 7 here). No search records.

## Replacement text

Line 1:
- `conditions`, replace "electrocardiography on three crabs (one male, two females) with 54 stable recordings from 63 attempts;" with "20 crabs bought; electrocardiography on three of them (one male, two females), 54 stable ECGs ('Fifty-four stable ECGs were obtained from three test crabs'); 63 video recordings of the appendage-stimulation trials were analysed for feeding behaviour (these are videos, not ECG attempts; ECG attempts are not counted in the paper);".
- `conditions`, after "tank water as control gave no cardiac or feeding response;" insert " the antennae's lack of chemosensitivity rests on crabs whose antennules were cauterised after juice application, to stop juice diffusing from antennules to antennae: with the antennules intact, juice on the antennae did give a heartbeat response ('The crab with the antennules showed the heartbeat response, while those with the cauterised antennules showed no response to the stimulation by the sugarcane juice application given to the antennae');".

Line 2:
- `conditions`, replace "electrocardiography on three crabs (one male, two females) with 54 stable recordings from 63 attempts;" with "20 crabs bought; electrocardiography on three of them (one male, two females), 54 stable ECGs; 63 video recordings of the appendage-stimulation trials were analysed for feeding behaviour (videos, not ECG attempts);".
- `conditions` (uncounted), append "; Table 2 gives each of the three crabs: walking legs, claws, antennae and mouthparts responded significantly (P < 0.05) in all three, the swimming-leg dactyls and both antennule flagella in none".

Line 3:
- `conditions`, replace "the letters after the means (a to d) are the paper's significance groups, test not read;" with "the letters after the means (a to d) are Duncan multiple-comparison groups between concentrations of the same compound;".
- `conditions`, replace "and the top response (100 ug/uL) is the highest tested, not a saturation point;" with "and 100 ug/uL is the highest tested; for hexyl 2-methyl butyrate the response at 100 ug/uL did not differ from that at 50 ug/uL (2.45 +/- 0.54, both group 'a'; Results: no significant difference from the values at 50 ug/uL, P > 0.05), so the response had levelled off by 50 ug/uL;".
- `note` (uncounted), replace "Title as it appears in the PeerJ search listing; Crossref returns the same title with the closing phrase on herbivore-induced sea buckthorn leaf volatiles." with "Title as on the PeerJ page and in Crossref (both end 'to herbivore induced Hippophae rhamnoides leaf volatiles')."
- `conditions` (uncounted), append "; the Results say females consistently responded more strongly than males, while the Discussion calls the sexes' responses basically the same".

Line 4:
- `conditions`, replace "predator odorants are those of the monkeys' possible carnivore predators per the paper's framing (not checked)" with "the odorants come from mustelids, small felids (cat, bobcat), skunk and red fox (Methods); the paper states that the spider monkey's only known mammalian predators, jaguar and cougar, have not been analysed for these odorants and that 'it seems unlikely that spider monkeys are regularly exposed to any of the six predator odorants tested here, at least in the context of predator avoidance'".
- `conditions` (uncounted), append "; with four of the six odorants (all but 2,2-dimethylthietane and 3-mercapto-3-methylbutan-1-ol) individual animals reached thresholds as low as 10 ppt; individual thresholds differed by factors of 10 to 1,000 depending on odorant, and sensitivity did not differ significantly between the six odorants".

Line 5:
- `conditions`, replace "in the order 22 C, 30 C, then 22 C again;" with "in the order 22 C, 30 C, then 22 C again; Bonferroni post-hoc tests found the 30 C audiogram different from both 22 C audiograms and the two 22 C audiograms different from each other (22 C versus 22 C repeated: p <= 0.001), so the temperature effect is not separated from order or time in captivity; two-way ANOVA temperature F2,126 = 13.46, p < 0.001, temperature x frequency F10,126 = 2.15, p <= 0.05;".
- `conditions` (uncounted), replace "frequency range tested not read;" with "tested at 0.1, 0.2, 0.5, 1, 2 and 4 kHz in random order;".

Line 6:
- `conditions`, replace "a separate set of fish from the traffic-noise group (n = 5)," with "compared with a traffic-noise group (n = 5; the AEP Methods do not say whether control and traffic fish were different individuals, and the paper's cortisol experiment gave each fish both treatments on separate days),".
- `conditions` (uncounted), replace "whose thresholds were elevated at 300 and 400 Hz after 2 hours of road-traffic playback;" with "whose thresholds were elevated by 7 dB at 300 Hz (p = 0.020) and 9 dB at 400 Hz (p = 0.025) after 2 hours of road-traffic playback at 140 dB re 1 uPa, other frequencies virtually unchanged;" and replace "body size only in S1 Table (not read);" with "no length given; S1 Table lists weights and cortisol values per test fish (not read);".

Line 7 (uncounted):
- `conditions`, replace "subadult males 93 to 104 mm total length;" with "Methods: seven subadult males 93 to 104 mm TL, nine subadult females 84 to 102 mm TL (9.8 to 17.1 g) and one adult male 126 mm (32.9 g); which six of each sex were in the audiograms is not stated; thresholds rose by 41 dB between 1 and 4 kHz;".

## Owner questions (the unit's, answered where I could)

1. Names absent from gbif-names.tsv: Scylla paramamosain Estampador, 1949, Portunidae, Decapoda (SeaLifeBase); Trabala vishnou (Lefebvre, 1827), Lasiocampidae (insecta.pro); Ateles geoffroyi Kuhl, 1820, Atelidae, Primates (Mammal Diversity Database); Platydoras armatulus (Valenciennes, 1840), Doradidae, Siluriformes (FishBase); Cyprinella venusta Girard, 1856, Leuciscidae, Cypriniformes (FishBase). GBIF API refused here, so none is GBIF-checked.
2. Trabala vishnou gigantina: a subspecies (insecta.pro, Wikipedia; the paper calls it Trabala vishnou gigantina Yang, 1978). Species rank with the subspecies in conditions is acceptable and matches main's Gallus and Coturnix rows; main also has rank "subspecies" rows (Trachemys scripta elegans, Canis lupus familiaris). The owner should pick one convention; until then line 3 can stay at species rank.
3. New: Megalechis thoracata changed meaning in 2005 (the former M. thoracata is now M. picta; M. thoracata now covers the former M. personata, per Wikipedia's Megalechis page). The 2015 paper postdates the change, but whether its fish were identified under the new usage is not stated in what I read. Owner to decide whether a name check beyond the printed name is wanted.
4. Scylla paramamosain, two traits from one pair of sentences: keep two records, one per trait, as main does for multi-trait sentences; each now carries its own design caveat (cauterised antennules belong to line 1).

## Progress note

Accurate on citations, licences and the duplicate checks for these six papers; held-out leads were not re-opened. Its Records summaries do not repeat the faults found in the conditions.

Verdict: 6 of 7 records in error (85.7%), 7 faults, above the 5% bar; pooled 305 of 701 (43.5%). Error lines: 1, 2, 3, 4, 5 and 6, all fixable with the replacement text above. Line 7 can merge, with the uncounted fixes.

This report is model output and carries no authority.
