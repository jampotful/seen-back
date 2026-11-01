# audit-355: desk-d259, evidence lines 1 to 8

Audited 1 November 2026 from the desk-d259 files present untracked in the worktree (docs/tracks/progress/desk-d259.md and docs/views/evidence/desk-d259.jsonl, 8 lines; neither committed here, neither edited). Worktree HEAD and origin/main 21e89e16 (desk-d258 after audit 354). `python3 -I tools/senses/check.py | grep 'd259\.'`: "docs/views/evidence/desk-d259.jsonl: 8 records, 0 problems". Quote lengths (`len(q.split())`): 36, 23, 20, 29, 40, 27, 27, 27, all within 40. Non-ASCII "β" and "χ" (line 1), "χ" (line 5) checked against the page. Format model audits 353 and 354; desk-audit.md evidence clause (40-word limit, no 125-character limit); abutting pieces judged under the six conditions of audit-324.md, cuts under audit-331.md (no line here uses a cut).

Sources opened (WebFetch): api.crossref.org/v1/works/ for all five DOIs (10.1371/journal.pone.0041841, 10.3390/agriculture16121275, 10.3390/jzbg6040056, 10.3390/insects16121207, 10.3390/insects9040166; all answered, none robots_disallowed); journals.plos.org pone.0041841 (two passes; the first gave a summary only, the second returned the quote and two further sentences verbatim); mdpi.com 2077-0472/16/12/1275 (three passes), 2673-5636/6/4/56 (three), 2075-4450/16/12/1207 (two), 2075-4450/9/4/166 (one). Names: api.obis.org/v3/taxon/Rivomarginella%20morrisoni (path form answered; the `taxon?scientificname=` form in the launch prompt failed with client_error and was not worked around further); antwiki.org/wiki/Lasius_niger (answered on this retry); biodiversity.org.au/afd/taxa/APHALARIDAE/names (Australian Faunal Directory); gd.eppo.int/taxon/OXYAHY/distribution/US. Burckhardt, Ouvrard and Percy 2021 (European Journal of Taxonomy 736: 137-182) landing page opened; its PDF on europeanjournaloftaxonomy.eu returned "PROVENANCE_REQUIRED ... Do not retry." and was not retried; plazi treatment pages returned redirect notices only. WoRMS not opened (refused per rules). No curl, mirror, PMC, repository copy, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 6 WebSearches.

## Bibliographic and licence

- Line 1 (Verheggen et al. 2012). Crossref: François J. Verheggen, Lise Diez, Ludovic Sablon, Christophe Fischer, Stefan Bartram, Eric Haubruge, Claire Detrain, as recorded; title identical; PLoS ONE 7(8) e41841; issued 2012-08-01; CC BY 4.0 content-version unspecified; relation empty. Page: Creative Commons Attribution License sentence (tool summary). Accepted (unspecified + page-printed sentence). Faults 0.
- Line 2 (Sarker et al. 2026). Crossref: Souvic Sarker, Ahmed M. Saveer, Pradeep Paudel, Aijun Zhang; title identical; Agriculture 16(12) 1275; issued 2026-06-09; CC BY 4.0 vor. Page metadata CC BY 3.0, no body licence sentence. Accepted (CC BY 3.0 page vs CC BY 4.0 Crossref). Faults 0.
- Lines 3, 4 (Subpayakom et al. 2025). Crossref: Navapong Subpayakom, Pongrat Dumrongrojwattana, Supattra Poeaim; title identical (two pieces); Journal of Zoological and Botanical Gardens 6(4) 56; issued 2025-11-13; CC BY 4.0 vor. Page: "This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution"; footer CC BY 4.0, metadata CC BY 3.0. Accepted. Faults 0.
- Line 5 (Luo et al. 2025). Crossref: ten authors in the recorded order (Yingning Luo ... Liping Ban); title identical (two pieces); Insects 16(12) 1207; issued 2025-11-27; CC BY 4.0 vor. Page metadata CC BY 3.0. Accepted. Faults 0.
- Lines 6 to 8 (Farnier, Davies, Steinbauer 2018). Crossref: as recorded; title identical; Insects 9(4) 166; issued 2018-11-17; CC BY 4.0 vor. Page metadata CC BY 3.0, no body sentence. Accepted. Faults 0.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names

- Lasius niger (line 1): not in gbif-names.tsv; AntWiki (retry answered): "Lasius niger (Linnaeus, 1758)", current name, Formicidae, Formicinae, Lasiini. Wild-collected queenless field colonies. Met; note provenance addition uncounted.
- Oxycarenus hyalinipennis (line 2): not in gbif-names.tsv. Main's docs/views/gaps/taxonomy-gbif.tsv:1317 reads "Oxycarenus	Oxycarenidae	Hemiptera	GBIF backbone species/match 2026-10-19 (usageKey 4407280, class Insecta)", and main's cells.jsonl and insect.md place Oxycarenus lavaterae in Oxycarenidae; the EPPO page's cited reference prints "(Hemiptera: Oxycarenidae)". The record's Lygaeidae is the paper's title usage, an older broad placement; filed as is, the row would sit in a different family from main's own taxonomy for the genus. **Fault 1** (family). Name otherwise met (EPPO preferred name "Oxycarenus hyalinipennis", authority Costa from the cited reference).
- Rivomarginella morrisoni (lines 3, 4): OBIS path form: "Rivomarginella morrisoni", authorship "Brandt, 1968", "accepted", family "Marginellidae", order "Neogastropoda", class Gastropoda, taxonID 473993. The desk's inferred order is right; the note should cite OBIS (uncounted). Owner question 1 answered: Neogastropoda confirmed. Snails wild-collected (four river basins, 26 to 29 March 2023; 25 per site, 100 in total, tool summary).
- Odontothrips loti (line 5): not in gbif-names.tsv; the paper prints "Odontothrips loti (Haliday, 1852)", Thysanoptera, Thripidae (tool summary). No independent checklist opened (unchecked). Laboratory colony founded in 2021 from field thrips, three generations on alfalfa. Met.
- Ctenarytaina eucalypti, C. bipartita (lines 6, 7): gbif-names.tsv:1287 and :1286 EXACT ACCEPTED. Anoeconeossa bundoorensis (line 8): gbif-names.tsv:286 maps the misspelling "Anoeconesossa bundoorensis" (SYNONYM) to accepted "Anoeconeossa bundoorensis", the record's spelling. Australian Faunal Directory, Family APHALARIDAE Löw, 1879, Subfamily Spondyliaspidinae: "Ctenarytaina eucalypti (Maskell, 1890)" and "Ctenarytaina bipartita Burckhardt, Farnier, Queiroz & Taylor, 2013" under Tribe Ctenarytainini White & Hodkinson, 1985; "Anoeconeossa bundoorensis Taylor & Burckhardt, 2013" under Tribe Spondyliaspidini Schwarz, 1898. Aphalaridae and Hemiptera met for all three (the launch's Psyllidae and Triozidae alternatives do not apply). Laboratory glasshouse colonies founded from insects collected at Bundoora and Fish Creek, Victoria. Authorities are uncounted note additions.

Name faults 1 (line 2).

## Duplicates

git grep on origin/main (21e89e16) across the whole docs/ tree (evidence, audit incl. audit/corrected and audit/ALL, sheets, searched, gaps, progress, desk-queue) for each DOI suffix (0041841, agriculture16121275, jzbg6040056, insects16121207, insects9040166), for Lasius niger, Oxycarenus, Rivomarginella, Odontothrips, Ctenarytaina, Anoeconeossa/Anoeconesossa, Verheggen and Farnier; then the branch-only additions (`git diff origin/main...<branch>`) of all 136 remote branches matching origin/research/desk-d2* or origin/research/audit-3*; then grep of docs/tracks/progress/audit-3*.md and desk-d2*.md.

- No DOI of this unit is on main or any other branch; the only branch hit is research/desk-d259 itself.
- Lasius niger: genus-level search record only (searched/sweep-57.jsonl:35, vision traits). Oxycarenus: gaps rows for O. lavaterae and sweep-105 (vision traits), no evidence row. Ctenarytaina eucalypti and C. bipartita: canon-4.jsonl:73, :74 (acuity_cpd 0.08 cpd from a compilation), a different trait and source. Anoeconeossa bundoorensis: desk-d199.jsonl:6 on main (behaviour_vision, grey targets, Farnier et al. 2014, fevo.2014.00067), a different paper and trait; line 8's text calls it "desk-d199", which is now on main (wording uncounted).
- No hold-out of these papers in audit-3*.md or earlier desk progress files.

Duplicates 0.

## Trait keys and rulings

- sense_chemical for lines 1, 2, 3, 5, 6 to 8: acceptable (living-animal odour or water-borne cue choice tests).
- Line 4, behaviour_vision null (owner question 2). The snail has eyes ("paired elongate tentacles with basal eyes", Methods, verbatim), and the barrier ("a transparent barrier without perforations allowed visual access to the food", watertightness checked with coloured water, tool summary) does exclude chemical cues, so the stimulus is visual in kind. But it is not defined: the paper states no illumination, light level or time of day for this trial (the 300 lux figure belongs to the light/dark test, the light meter sentence to Section 2.4), the species is nocturnal ("showing peak emergence between 18:00 and 22:00 h."), and the bait's size, distance and contrast are not given. A null for a visual cue presented under unstated lighting cannot be read as a visual result; the rule that a null with a defined stimulus is acceptable is not met, and the paper cannot supply the missing condition. **HOLD OUT.**
- Grade m right for lines 1 to 3, 5 to 8.

## Per-record findings

### Line 1, Lasius niger, (E)-beta-farnesene two-choice

Results sentence verbatim in two abutting pieces in one response on pass 2 ("Ant scouts preferrentially orientated towards the branch leading to the EβF treated plant (67%)" | "rather than to the branch leading to the control non treated plant (33%) (n = 43, χ2 = 5.23, P = 0.02)."); pass 1's summary agrees on every figure; heading "Two-choice Bioassay". **Quote MATCH**, 36 words; value says no more ("pure" and "septum" are design, verified).

Verified, verbatim: "A rubber septum containing pure EβF was placed alternatively" "(with similar number of replicates being conducted on both sides) on one of the two plants" "and switched after each observed ant scout." Tool summary: queenless colonies of more than 500 workers collected in Brussels in April 2007, fed 1 M sucrose, dead arthropods and water, starvation not mentioned; three colonies pooled after a bias check; T-shaped aluminium arena with two branches leading to uninfested broad bean plants, airflow about 0.6 m/s; scouts tested singly; septum dose not stated; chi-square goodness of fit, paired t-tests, ANOVAs, Fisher's exact tests; four-arm 53.3 % against 25 % (χ2 = 9.63, P = 0.003, n = 30), 42.7 % of time (P = 0.033); nulls for neutral-area time (P = 0.978), walking speed (1.74 against 1.96 cm/s, P = 0.338) and hesitation (29 % against 10 %, Fisher P = 0.190).

Not carried: the next sentence, verbatim: "For each ant scout, the time spent on the branch leading to the EβF treated plant (mean = 8.28 sec, n = 43)" "was on average significantly higher than the time spent on the branch leading to the control plant" "(mean = 3.59 sec, n = 43) (Paired t-test, T-value = 2.97, P = 0.005)." The record carries the same test's three nulls but omits its significant residence-time result. The method's "two plant branches" misdescribes the arena (uncounted).

**Error (significant result from the same test omitted).** Fixable.

### Line 2, Oxycarenus hyalinipennis, four attractive compounds

Abstract sentence verbatim in two abutting pieces in one response ("Y-tube olfactometer assays revealed that only four individual compounds, 1-heptanal, 1-decene, 1-nonanal, and isopropyl" | "palmitate, elicited significant attraction from both males and females."). **Quote MATCH**, 23 words; value says no more. Section 3.2 agrees: males "Among males, four compounds showed significant attraction: 1-heptanal (Zc = 2.83; p = 0.005)," "1-decene (Zc = 4.42; p < 0.001), 1-nonanal (Zc = 2.22; p = 0.027), and isopropyl palmitate (Zc = 2.63; p = 0.009)."; females "1-heptanal (Zc = 2.65; p = 0.008)", "1-decene (Zc = 4.99; p < 0.001), 1-nonanal (Zc = 4.24; p < 0.001), and isopropyl palmitate (Zc = 3.21; p = 0.001)."; "females showed a significant repellent response to p-xylene (Zc = 2.00; p = 0.045)." All match the record.

Verified, verbatim: "CSB used in this study were initially collected on 24 October 2021 from Lagunaria patersonia (primrose trees)" "located along Primrose Street in Irvine, Orange County, California."; "at 26 ± 1 °C, 75% RH, and a 16:8 h (L:D) photoperiod."; "a Y-shaped glass tube with an inner diameter of 5 mm, two arms each 6 cm long, and a main stem 7 cm long."; "at a constant flow rate of 100 mL min−1 per arm."; "A choice was recorded when the insect moved at least 5 cm into one of the olfactometer arms" "and remained there for a minimum of 30 s."; "Each insect was given up to 5 min to respond."; "Initially, each single compound was evaluated using unmated males and females, with 10–35 replicates" "(1 insect/replicate);" "further tests were conducted on mated males and females with 10–32 replicates."; "the positions of treatment and control were alternated to minimize positional bias."; Chi-square "calculated in Microsoft Excel following the formulas and procedures described by Zar [25]."; mated and unmated "combined since no significant differences (p > 0.05) were found between them."; "Twenty-four-hour starved mated and unmated males and females aged 8–12 days were used in the assays."; blend at 0.010 µg "females showing 70.8% attraction (Zc = 2.89; p = 0.004) and males 71.4% attraction (Zc = 2.27; p = 0.023)."; at 1.000 µg "neither sex showed significant attraction, with 37.5% of both males and females" (Zc = 1.00, p = 0.317, tool summary).

Not carried: "Insects that failed to make a choice within the observation period were categorized as non-responders" "and excluded from analysis." (the number excluded was not read); at 0.100 µg of the natural-ratio blend "males showed significant attraction (77.8%; Zc = 2.36; p = 0.018) compared to control." while "females did not show significant attraction (37.5%)", a significant result the record's "several single-sex nulls at other doses" hides; the abstract says removal of isopropyl palmitate "almost resulted in a complete loss" "of attraction." whereas Section 3.4 says it "eliminated attraction entirely." (the record follows the Results; the disagreement is not disclosed). Family as above.

**Error (family against main's taxonomy; non-responder exclusion and a significant blend result omitted; abstract/Results disagreement undisclosed).** Fixable.

### Line 3, Rivomarginella morrisoni, bait side behind opaque perforated barrier

Results 3.5 ("Feeding Behavior and Chemosensory Response") sentence: passes 1 and 2 returned "The snails exhibited a strong preference for the bait-present side (98.06%) over the bait-absent side (1.94%)" (rest summarised as a chi-square at p < 0.05); pass 3, asked for the words from "(1.94%)" to the end, returned "(1.94%) (Chi-square, p < 0.05)." The two pieces overlap on "(1.94%)", so no gap is possible, but they come from separate requests and do not meet condition 1 of audit-324.md as the auditor's own join; the desk reports one two-piece response. **Quote MATCH** on text (20 words, whole sentence); value says no more ("behind an opaque perforated barrier" is design).

Verified, verbatim: "The tank was divided by an opaque barrier containing three perforations at its base," "allowing the diffusion of chemical cues and the passage of snails."; "All snails underwent a 3-day food deprivation period for acclimation". Tool summary: four river basins, 26 to 29 March 2023, 25 snails per site; 25 °C; 10 snails per tank, three tanks per treatment; about 400 mg food items; positions every 15 min for 3 h; "Each tank was considered an independent experimental unit to ensure statistical independence."; chi-square in SPSS 29; bait-side assignment not described for this test; reuse of snails across experiments not stated.

Wrong in the record: the method says the barrier let "only water-borne cues" pass, and the conditions say snails "might also have contacted bait, which the paper does not discuss". The paper states that the perforations allowed "the passage of snails", so the side counts include snails that had crossed to the bait; vision is excluded only before crossing. Not carried: lighting and time of day for this trial are not stated, for a species with "peak emergence between 18:00 and 22:00 h."; the total pool of 100 snails and the unstated reuse across experiments.

**Error (design misdescribed: snails could pass the barrier; lighting unstated).** Fixable.

### Line 4, Rivomarginella morrisoni, transparent barrier null

Results 3.6 ("Visual Food Detection Experiment") sentence: pass 2 returned "Snail distribution fluctuated throughout, and Chi-square analysis, based on time-aggregated data to avoid temporal" (rest summarised with the same figures); pass 3, asked for the rest after "to avoid temporal", returned " dependence, showed no significant preference for either side (bait-present: 51.39%, bait-absent: 48.61%; p > 0.05)." Separate requests (condition 1 of audit-324.md not met by the auditor's join; the desk reports three pieces in one response). **Quote MATCH** on text, 29 words. **HOLD OUT** under the ruling above (visual stimulus undefined: illumination not stated for this trial; unfixable from the paper).

### Line 5, Odontothrips loti, p-menth-8-en-2-one

Results 3.2 sentence verbatim in two abutting pieces ("The assay results showed that p-Menth-8-en-2-one significantly attracted both male (χ2 = 5.786, df = 1, p = 0.016)" | " and female (χ2 = 7.407, df = 1, p = 0.006) O. loti compared to the control (Figure 3, Table S6)."), first words also on pass 1. **Quote MATCH**, 40 words; value says no more.

Verified: "The other compounds elicited no significant responses by both male and female thrips." (verbatim); tool summary: 2021 collection at Shangzhuang Experimental Station, three generations on alfalfa at 25 ± 1 °C; 3 to 5 days old, starved 3 h; Y-tube arms 10 cm × 1 cm at 75°, 50 mL/min; 10 ng/μL in paraffin oil; 60 per sex per treatment in Methods, Figure 3 "sixty for each compound" for both sexes, Figure 4 eight (O. loti) and ten (F. occidentalis) EAG replicates; swaps after five thrips, ethanol cleaning after ten; dose results at 10 ng/μL χ2 = 9.281, p = 0.002 (females, 2.35 times) and χ2 = 6.564, p = 0.01 (males, 2.06 times); EAG df = 5, p = 0.598. The record carries all of these.

Not carried: "If the thrips did not enter either arm during the observation period, it was recorded as "no choice."" (verbatim); non-choosers were 0 to 15 % across the Y-tube assays (tool summary), and exclusion is stated only for the lure experiment ("Assays where no choice was made were excluded from subsequent analysis."), so their handling in this screening is unstated; the Results text gives no statistics for O. loti at concentrations other than 10 ng/μL (Figure 4 only, not read), and the one 1000 ng/μL null sentence ("At 1000 ng/μL, neither male nor female thrips showed any attraction to the compound (p = 1.000 > 0.05).") sits in the F. occidentalis paragraph; the abstract's "2.05–3.07 times" range mixes both thrips species (tool summary; uncounted).

**Error (non-choice handling and the rest of the dose series undisclosed).** Fixable.

### Lines 6 to 8, Ctenarytaina eucalypti, C. bipartita, Anoeconeossa bundoorensis, undamaged host odour nulls

Results 3.1 ("Behavioral Responses") sentence verbatim in two abutting pieces ("Surprisingly, none of the four species were attracted to their host odors; C. eucalypti (p = 0.76)," | " C. bipartita (p = 0.27), A. bundoorensis (p = 0.78)."); next sentence verbatim "Even more surprising was the behavior of G. brimblecombei which strongly avoided host plant odors (p < 0.001, Figure 2)." **Quote MATCH**, 27 words. Each species' p-value stands in its own clause, so one sentence supports the three lines (audits 334, 336); each value carries only its own p. "undamaged" is design (host branchlets of young leaves, abstract "HPVs from undamaged leaves"), "adults" from the abstract.

Positive results in the paper, verbatim abstract: "Although adult C. eucalypti were consistently repelled by HPVs from damaged host leaves, none of the species" "exhibited positive chemotaxis to HPVs from undamaged leaves."; the damaged-leaf pilot was a check that psyllids could respond (C. eucalypti avoided it, tool summary); G. brimblecombei avoidance. All carried. Design (tool summary): Y-tube 8 cm arms, 12 cm stem, 1.5 cm inner diameter; choice at 4 cm; non-choosers within 30 min excluded; branchlets in oven bags against an empty oven bag; C. eucalypti on E. globulus, C. bipartita on E. kitsoniana, A. bundoorensis and G. brimblecombei on E. camaldulensis; at least 50 insects per experiment; odour sources swapped every four insects; binomial tests against 50:50; responsiveness 77, 74, 70, 69 %. The record carries these except the per-species host mapping, the 30 min exclusion and the four-insect swap (uncounted additions; none is a confound). Per-species n is in Figure 2 (not read by desk or auditor).

**MATCH** for lines 6, 7 and 8. Uncounted additions: host per species, exclusion, swaps, authorities, AFD family source; line 8's "desk-d199" now on main.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Lasius niger, EbF two-choice | error, fixable | conditions; method, note (uncounted) | quote MATCH (36); significant residence-time result of the same test omitted |
| 2 | Oxycarenus hyalinipennis, four compounds | error, fixable | family, conditions, note | quote MATCH (23); family Oxycarenidae on main; non-responder exclusion, male 0.1 µg blend attraction and abstract/Results disagreement omitted |
| 3 | Rivomarginella morrisoni, bait side | error, fixable | method, conditions; note (uncounted) | quote MATCH (20); snails could pass the perforations, contrary to the method; lighting unstated |
| 4 | Rivomarginella morrisoni, visual null | HOLD OUT | none | quote MATCH (29); visual stimulus undefined (illumination unstated, nocturnal species) |
| 5 | Odontothrips loti, p-menth-8-en-2-one | error, fixable | conditions | quote MATCH (40); no-choice handling and remaining dose results undisclosed |
| 6 | Ctenarytaina eucalypti, null | MATCH | conditions, note (uncounted) | quote MATCH (27) |
| 7 | Ctenarytaina bipartita, null | MATCH | conditions, note (uncounted) | quote MATCH (27) |
| 8 | Anoeconeossa bundoorensis, null | MATCH | conditions, note (uncounted) | quote MATCH (27) |

Errors 4 of 7 audited records (57%), above the 5% bar, plus 1 held out: scientific-context 4 (lines 1, 2, 3, 5), of which omitted significant results 2 (lines 1, 2), omitted non-response handling 2 (lines 2, 5), design misdescribed 1 (line 3), undisclosed abstract/Results disagreement 1 (line 2), dose series 1 (line 5); names 1 (line 2, family); quote form 0; bibliographic 0; licence 0; duplicates 0 against main, all 136 desk-d2* and audit-3* branches and the audit-3* hold-outs; grading 0. HOLD OUT: line 4.

Answers to the desk-d259 owner questions.
1. Rivomarginella order: Neogastropoda confirmed by OBIS (accepted, Brandt, 1968, Marginellidae); MolluscaBase/WoRMS not opened.
2. Snail behaviour_vision null: not acceptable from this paper. The snail has eyes and the barrier isolates sight, but the trial's lighting is not stated for a nocturnal animal, so the visual stimulus is undefined.

## Unchecked

- Line 1: EβF loading on the septum (not stated); per-colony n; verbatim colony and statistics sentences (tool summary only); the four-arm F statistic and ± 6.2 %.
- Line 2: number of non-responders excluded; per-compound n.
- Lines 3, 4: a one-response join of either quote by the auditor (tails obtained on a separate pass); KMnO4 permeability check; bait-side assignment in the chemosensory test (stated as not described, tool summary); whether snails were reused.
- Line 5: Figure 4 dose results for O. loti; Table S6; an independent checklist for Odontothrips loti.
- Lines 6 to 8: Figure 2 per-species n; juvenile versus adult E. globulus foliage per experiment; Burckhardt et al. 2021 text (PDF blocked), family taken from the Australian Faunal Directory.

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). For blank fields the form is field = new string.

Line 1, counted:
- `conditions`: "Nulls in the two-choice test:" -> "Also significant in the two-choice test: each scout spent longer on the branch leading to the EbF plant than on the branch leading to the control plant (mean 8.28 v 3.59 s, n = 43, paired t-test, T = 2.97, P = 0.005). Nulls in the two-choice test:"
- `method` (uncounted): "scouts offered two plant branches, one plant carrying" -> "scouts walked a T-shaped arena whose two branches led to uninfested broad bean plants, one plant carrying"
- `note` (uncounted): "AntWiki permission was not answered." -> "AntWiki (audit 355): Lasius niger (Linnaeus, 1758), current name, Formicidae, Formicinae."

Line 2, counted:
- `family`: "Lygaeidae" -> "Oxycarenidae"
- `conditions`: "a choice needed at least 5 cm into an arm and 30 s residence." -> "a choice needed at least 5 cm into an arm and 30 s residence; insects that made no choice within 5 min were classed as non-responders and excluded from analysis (number excluded not read). Tested insects were 8 to 12 days old and starved 24 h, tested in the light phase."
- `conditions`: "several single-sex nulls at other doses." -> "at 0.1 ug the natural-ratio blend attracted males (77.8 %, Zc = 2.36, p = 0.018) but not females (37.5 %); other single-sex nulls at other doses. The abstract says removing isopropyl palmitate 'almost resulted in a complete loss of attraction', whereas Section 3.4 says it eliminated attraction entirely."
- `conditions` (uncounted): "Bugs field-collected in October 2021 in Irvine, California" -> "Bugs field-collected on 24 October 2021 from Lagunaria patersonia (primrose trees) in Irvine, California"
- `note`: "Family and order from the title; no synonym found in gbif-names.tsv." -> "The title prints Lygaeidae; family Oxycarenidae follows main's taxonomy-gbif.tsv (GBIF backbone: Oxycarenus, Oxycarenidae, Hemiptera) and the EPPO page's cited '(Hemiptera: Oxycarenidae)' (audit 355); no synonym found in gbif-names.tsv."

Line 3, counted:
- `method`: "so only water-borne cues passed" -> "which the paper says allowed the diffusion of chemical cues and the passage of snails, so snails could cross to the bait side; vision of the bait was excluded only before crossing"
- `conditions`: "barrier perforations were large enough that snails might also have contacted bait, which the paper does not discuss." -> "the Methods say the perforations allowed the passage of snails, so the bait-side counts include snails that had crossed and could contact the bait. Lighting and time of day for this test are not stated, for a species whose emergence peaks between 18:00 and 22:00 h. 100 snails were collected (25 per site); whether individuals were reused across experiments is not stated."
- `note` (uncounted): "order Neogastropoda is inferred from the paper's statement 'Like other neogastropods, members of the family Marginellidae' and no order is printed, so confirm against MolluscaBase (WoRMS refused)." -> "the paper prints no order; OBIS (audit 355): Rivomarginella morrisoni Brandt, 1968, accepted, Marginellidae, Neogastropoda, Gastropoda (WoRMS not opened)."

Line 4: HOLD OUT (behaviour_vision null with an undefined visual stimulus: the paper states no illumination or time of day for the transparent-barrier trial on a nocturnal snail, and no bait size, distance or contrast; not fixable from the paper).

Line 5, counted:
- `conditions`: "The other ten compounds elicited no significant response in either sex (same Results section)." -> "The other ten compounds elicited no significant response in either sex (same Results section). Thrips that entered neither arm within 5 min were recorded as 'no choice' (0 to 15 % across the Y-tube assays); exclusion from analysis is stated only for the lure experiment, so their handling in this screening is not stated."
- `conditions`: "(chi2 = 9.281, p = 0.002; chi2 = 6.564, p = 0.01)." -> "(chi2 = 9.281, p = 0.002; chi2 = 6.564, p = 0.01). The Results text gives no statistics for O. loti at the other concentrations (Figure 4, not read); the abstract's 2.05 to 3.07 times range covers both thrips species."

Lines 6, 7 and 8, uncounted (same string in each line):
- `conditions`: "non-parametric binomial test against 50:50." -> "non-parametric binomial test against 50:50. C. eucalypti was tested on E. globulus, C. bipartita on E. kitsoniana, A. bundoorensis and G. brimblecombei on E. camaldulensis; insects that did not choose within 30 min were excluded, and odour sources were swapped every four insects."
- `note`: "Family from the article's keywords (Aphalaridae); order Hemiptera from the paper." -> "Family from the article's keywords (Aphalaridae) and the Australian Faunal Directory (Aphalaridae, Spondyliaspidinae; Ctenarytaina eucalypti (Maskell, 1890) and C. bipartita Burckhardt, Farnier, Queiroz & Taylor, 2013 in Ctenarytainini; Anoeconeossa bundoorensis Taylor & Burckhardt, 2013 in Spondyliaspidini; audit 355); order Hemiptera from the paper."

Line 8, uncounted:
- `conditions`: "The same species has an unrelated behaviour_vision row on desk-d199 (grey targets)." -> "The same species has an unrelated behaviour_vision row on main (desk-d199, Farnier et al. 2014, grey targets)."

Verdict: 4 of 7 audited records in error (57%), above the 5% bar; lines 1, 2, 3 and 5 fixable with the replacement text above; line 4 held out; lines 6, 7 and 8 MATCH.
