# audit-326: desk-d233, evidence lines 1, 3, 4 and 5 (line 2 held out)

Audited 31 October 2026 from the desk-d233 files present untracked in the worktree (docs/tracks/progress/desk-d233.md and docs/views/evidence/desk-d233.jsonl, 10 lines; neither committed here, neither edited). HEAD and origin/main 699baafa (desk-d232). `python3 -I tools/senses/check.py | grep d233`: "docs/views/evidence/desk-d233.jsonl: 10 records, 0 problems". Quote lengths (`len(q.split())`): line 1 11, line 3 30, line 4 31, line 5 33 words, all within 40. Lines 6 to 10 belong to audit 327 and are not judged here. Evidence records only; audits 323 to 325 are the format model, and the desk-audit.md evidence clause applies (40-word limit, no 125-character limit). Quotes returned as abutting pieces are judged under the six conditions in audit-324.md.

Sources opened (WebFetch): api.crossref.org/v1/works for the three DOIs (one pass each); www.mdpi.com/2075-4450/15/9/692 (two passes); www.mdpi.com/2075-4450/11/2/109 (three passes); journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0118575 (three passes); for names, gd.eppo.int/taxon/ANOLCN/datasheet and www.afromoths.net/species/19613. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 3 WebSearches and 13 WebFetch calls used.

## Line 2 (Tipula autumnalis): HOLD OUT: repeats main (desk-d232)

`git grep` on origin/main: docs/views/evidence/desk-d232.jsonl:3 is Tipula autumnalis sense_chemical, "nine EAG..." on 10.3390/insects16010024 (also desk-d232.md:9, audit-325.md line 3). Confirmed repeat; excluded from the error rate as instructed.

## Bibliographic and licence

- Line 1, Crook, Maynard, Furtado 2024. Page byline "Damon Crook, Emily Maynard and Mandy Furtado"; Crossref same order. Title verbatim (page in two abutting pieces, Crossref truncated by the tool): "Verification and Evaluation of Male-Produced Pheromone Components from the Citrus Long-Horned Beetle, Anoplophora chinensis (Forster) (Insecta: Coleoptera: Cerambycidae)", as recorded. Page "Insects 2024, 15(9), 692"; Crossref 15(9) 692, issued 2024-09-13, journal-article, relation empty, no update-to. Page: "This article is an open access article distributed under the terms and conditions of the" "Creative Commons Attribution (CC BY) license."; metadata CC BY 3.0 (tool summary); Crossref CC BY 4.0 vor, start 2024-09-13, delay 0. Met.
- Lines 3 and 4, Arif, Guarino, Colazza, Peri 2020. Byline "Mokhtar Abdulsattar Arif, Salvatore Guarino, Stefano Colazza and Ezio Peri", as recorded and in Crossref. Title verbatim on page and Crossref, as recorded. Page "Insects 2020, 11(2), 109"; Crossref 11(2) 109, issued 2020-02-09, relation empty, no update-to. Page metadata CC BY 3.0 (tool summary, no licence sentence returned); Crossref CC BY 4.0 vor, start 2020-02-09, delay 0. Accepted under the CC BY 3.0 page vs CC BY 4.0 Crossref pairing. Met.
- Line 5, Bouwer, Slippers, Degefu, Wingfield, Lawson, Rohwer 2015. Byline and Crossref order as recorded. Title verbatim, as recorded. Page citation "PLoS ONE 10(3): e0118575."; Crossref PLOS ONE 10(3) e0118575, issued 2015-03-31, relation empty, no update-to. Page: "This is an open access article distributed under the terms of the" " Creative Commons Attribution License"; Crossref CC BY 4.0 vor, start 2015-03-31. Met.

source.access "open" right on all four. Bibliographic faults 0; licence faults 0.

## Names

- Anoplophora chinensis: EPPO preferred name "Anoplophora chinensis (Forster)", Coleoptera: Cerambycidae; A. malasiaca listed as a synonym (still used in Japan). Paper prints the accepted name. Met.
- Bagrada hilaris: paper "Bagrada hilaris (Burmeister)"; Plazi treatment titles "Bagrada (Bagrada) hilaris (Burmeister, 1835)" (search result titles, pages not opened); Pentatomidae, Hemiptera. Met, accepted status not read from a checklist page (Unchecked).
- Coryphodema tristis: Afromoths "Coryphodema tristis (Drury, 1782)", accepted, Cossidae (Cossinae); synonym Coryphodema capensis Felder, 1874. Met.

Name faults 0.

## Duplicates

git grep on origin/main (699baafa) across the whole docs/ tree (evidence, audit, audit/corrected, audit/ALL, sheets, searched, gaps, wanted, codex-findings, progress) for "Anoplophora", "Anoplophora chinensis", "citrus long-horned", "heptyloxy", "insects15090692", "15090692", "Crook", "Bagrada", "painted bug", "octenyl", "insects11020109", "11020109", "Pantelleria", "Coryphodema", "Cossidae", "goat moth", "pone.0118575", "0118575", "Bouwer".

- Line 1: Anoplophora on main is A. glabripennis only (oa-1 opsin rows, desk-d192, desk-d204 EAG); A. chinensis and 15090692 appear only in desk-d231.md:12 (held lead). Crook hits are other papers (oa-8, desk-d228, audit-320). Not a repeat.
- Lines 3 and 4: no Bagrada, octenyl, 11020109 or Pantelleria hit anywhere on main. Not a repeat; the two lines are separate results (female and male sentences, each its own quote), not a pooled or duplicated row.
- Line 5: no Coryphodema, 0118575 or Bouwer hit. Cossidae on main: Culama sp. and Givira mucida opsin rows (oa-1), Cossus cossus gap cells, Prionoxystus in audit-72. Not a repeat.

Duplicate faults 0.

## Per-record findings

### Line 1, Anoplophora chinensis, sense_chemical, both sexes respond to all three compounds

Results 3.1, verbatim and returned whole: "All three compounds elicited antennal responses from both females and males." MATCH, 11 words. Before: "Aerations of male extracts yielded 4-(n-heptyloxy)butan-1-ol, 4-(n-heptyloxy)butanal, and nonanal." and "Aeration extracts from females produced nonanal but did not yield either the alcohol or the aldehyde (Figure 1)." After: "When standards of the three products were used, antennal responses from both male and female beetles" "were more distinct (e.g., Figure 2)." Value says no more. Methods: "The insects originated from Italian and Chinese sources."; "All adult virgin A. chinensis (between 3 and 4 weeks old) used in laboratory studies were reared at the" "Forest Pest Methods Laboratory (FPML) Insect Containment Facility"; "Individual virgin adults (between 2 and 3 weeks old) were placed in 120 mL glass canning jars"; "Empty glass jars were aerated and used as controls."; "A total of 12 male, 12 female, and 12 control aerations were collected."; "Antennae were prepared by cutting a single antenna at the base of the head of an adult beetle". Number of EAD runs not stated (tool summary, two passes); whether control aerations were analysed is not reported (tool summary). Fig 2 caption: GC-EAD "by A. chinensis (female) in response to chemical standards". Y-tube: females "significantly more attracted to the three-component blend" (16 of 20, p < 0.05); "Neither any two-component blend nor the alcohol, aldehyde, or nonanal alone was significantly more attractive" than control; males not significantly attracted to any blend over control, no dose effect; alcohol alone 14 of 20, p = 0.07364 (tool summary of the male results).

**Error (control design misstated; behavioural nulls omitted).** (a) The conditions say "no solvent or blank control" and the note calls "no control" a design gap of the paper's. The paper collected 12 control (empty-jar) aerations alongside 12 male and 12 female; what it does not report is whether those controls were analysed. Since nonanal, one of the three EAD-active compounds, was found in both sexes' headspace, the unreported control analysis is the relevant gap, and the record states the wrong one. (b) The behavioural results are excluded by a sentence ("not summarised here"), but they carry nulls under the rules: males were attracted to no blend or dose, and females to none of the single compounds or binary blends. Audit 325 (Tipula, line 3) counted behavioural nulls omitted from an EAD record. Uncounted: aeration beetles 2 to 3 weeks old, laboratory beetles 3 to 4 weeks old. Fixable.

### Line 3, Bagrada hilaris, sense_chemical, females significant from 0.2 ug

Results 3.1, verbatim in two abutting pieces in one response: "In particular, females’ antennae exhibited a significant electroantennographic response at 0.2 µg (p < 0.05; ANOVA" "followed by LSD test), and similar responses were observed at 2 and 20 µg." Same join as the desk's two passes; first piece does not end a sentence; curly apostrophe as recorded; note marks the pieces. MATCH under audit-324's conditions, 30 words. Value says no more ("lowest dose tested 0.02 ug" is from the Methods dose list). Methods: "A colony of B. hilaris was established and restocked regularly with individuals collected from caper (Capparis " "spinosa L.) fields on the island of Pantelleria (Trapani, Italy)."; "Adults and nymphs (4th and 5th stages) were used separately in experiments."; "Tested doses of (E)-2-octenyl acetate were 0.02, 0.2, 2, 20, and 200 µg; acetone was used as a control."; "to generate a 1.5-s stimulus at 1-min intervals"; "EAG amplitudes were adjusted to a control stimulus (acetone)."; n 7 females, 7 males, 6 nymphs, square-root transform, one-way ANOVA with Fisher's LSD, rearing 30 ± 2 °C, 70 ± 10% RH, 16L:8D (tool summary). Two passes found no statement of presentation order and none of whether each antenna received all doses; adult age and mating status not stated. Olfactometer: "females were attracted by (E)-2-octenyl acetate rather than air (χ2 = 10.52, df = 1, p < 0.001, n = 46)"; with seedlings "(χ2 = 5.22, df = 1, p = 0.02, n = 62)".

**Error (unsupported design statement).** The conditions say the doses were "tested in ascending order". The paper lists the doses in ascending order but, in two passes over Methods 2.2, states no presentation order. The record turns a list into a protocol; the replacement says the order is not stated. If the desk can point to a printed sentence giving the order, this reverts to MATCH. Uncounted addition: the female olfactometer results. Fixable.

### Line 4, Bagrada hilaris, sense_chemical, males significant only at 2 ug

Results 3.1, verbatim in two abutting pieces in one response: "In males, the only significant response occurred at 2 µg (p < 0.05; ANOVA followed by LSD test); however, it was not" "significantly different from 0.2, 20, and 200 µg doses." Same join as the desk's. MATCH under audit-324's conditions, 31 words. Value says no more. Distinct from line 3: a separate sentence, sex and result; same design text. Olfactometer: "while males and nymphs were not attracted (χ2 = 0.71, df = 1, p = NS, n = 36; χ2 = 0.64, df = 1, p = NS, n = 56, respectively)"; "Males were not attracted to (E)-2-octenyl acetate (χ2 = 0.96, df = 1, p = 0.3, n = 66)". Abstract: "Olfactometer behavioral responses showed that females and nymphs were attracted to (E)-2-octenyl acetate," "while males showed no attraction." Field: 10 mg traps "catching both females and nymphs"; "In the traps baited with 5 mg of (E)-2-octenyl acetate, only B. hilaris nymphs were caught (mean 0.2 ± 0.1)."; "No captures were observed in the traps baited with 2 mg of (E)-2-octenyl acetate and in the control traps."

**Error (unsupported design statement; male behavioural nulls omitted).** (a) "tested in ascending order" as on line 3. (b) The record logs a weak male antennal result and omits that males showed no attraction in either olfactometer experiment and were not reported among field captures, the null results the Abstract itself states for males. Fixable. Uncounted, from the paper and not this record: the nymph Experiment 2 statistic "(χ2 = 7.22, df = 1, p = 0.07, n = 61)" is called significant; χ2 = 7.22 at 1 df gives about p = 0.007 (my own calculation), so p = 0.07 is probably a misprint.

### Line 5, Coryphodema tristis, sense_chemical, male EAD 1.9 mV to the gland peak

Results, "Gas chromatography electro-antennographic detection.", verbatim in two abutting pieces in one response: "GC-EAD investigation of the gland extracts revealed a large (1.9 ± 0.4 mV, N = 9, ± SE) EAD response of the male antenna" " to the only peak above the FID detection limit." Same join as the desk's single pass. MATCH under audit-324's conditions, 33 words. Value says no more. Next sentence: "The response was in most cases well above the noise level of the EAD detector and occurred at 9.11 minutes" " after optimization of the chromatographic parameters." Fig 1 legend: "Bottom is the response to the blank." "(EAD response at 9.11 min: 1884 ± 435 μV, mean ± SE, N = 9)". Insects: "Infested Eucalyptus nitens logs were collected from a plantation near Lothair, South Africa"; insectary 20 to 25 °C, 12 h photo-/scotophase; "A total of 62 glands were removed from virgin female moths when calling behavior was observed."; "Twelve glands were extracted in n-hexane and acetone respectively and 38 glands were extracted in dichloromethane."; "The antennae from virgin male moths (between 2 and 3 days old) were removed with a surgical blade". Solvent for the N = 9 recordings and number of antennae not stated (tool summary). Retention index "calculated as 1797" "matched with the retention index of the standards for Z and E9-14:OAc"; GCxGC ratio "1.13 ± 1.31: 98.87 ± 1.31 (14:OAc: Z9-14:OAc, mean ± SD, N = 33)". Dose-response: "Live males and females (n = 5)"; "In general males showed larger responses to Z9-14:OAc, Z7-14:OAc, E9-14:OAc and Z9-14:Ald when compared to females."; "Females were more sensitive only for 14-Ac."; "Male and female antennae did not show a differential sensitivity for Z11-14:OH and Z9-14:OH."; "There were five zero values at lower concentrations for Z9-14:Ald, Z9-14:OH and Z11-14:OH." Field: "No moths were caught in blank treatments."; males caught in significant numbers only with combinations (Abstract, tool summary).

**Error (contrary sex result omitted).** The note summarises the dose-response sex comparison as males larger to four compounds and no difference for two, and leaves out the printed contrary result that females were more sensitive to 14:OAc (printed "14-Ac"), the compound that is the minor gland component; the five zero values that limited the dose:sex test are also omitted. Everything else in conditions is borne out (12 and 12 is "respectively", so 12 each). Fixable.

## Trait key and grading

All four sense_chemical (antennal electrophysiology to pheromone compounds or extracts). Grade `m` right on all four. Trait or grade faults 0.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Anoplophora chinensis, both sexes respond to three compounds | error, fixable | conditions, note | Quote MATCH; 12 empty-jar control aerations exist (record says no control), their analysis unreported; behavioural nulls (males attracted to nothing; females not to single compounds or pairs) omitted |
| 2 | Tipula autumnalis | HOLD OUT: repeats main (desk-d232) | | desk-d232.jsonl:3, same DOI and trait; excluded from rate |
| 3 | Bagrada hilaris, females significant from 0.2 ug | error, fixable | conditions | Quote MATCH (two abutting pieces); "tested in ascending order" not printed |
| 4 | Bagrada hilaris, males significant only at 2 ug | error, fixable | conditions | Quote MATCH (two abutting pieces); "ascending order" not printed; male olfactometer nulls (n = 36, 66) and field results omitted |
| 5 | Coryphodema tristis, male EAD 1.9 mV, N = 9 | error, fixable | note | Quote MATCH (two abutting pieces); females more sensitive to 14:OAc omitted from the sex comparison |

Count: 4 of 4 audited records in error (100%): scientific-context 4; duplicates 0 (line 2 held out, not counted); quote form 0; bibliographic 0; names 0; licence 0; trait key 0; grading 0. HOLD OUT: line 2.

Pooled with audits 172 to 325: 409 of 818 evidence records (50.0%), taking audit 325's 405 of 814 and adding 4 of 4 here (audit 327's lines 6 to 10 not included).

## Unchecked

- Bagrada and Coryphodema licence metadata and the Bagrada byline punctuation are tool summary; MDPI licence for Bagrada read from metadata only.
- Bagrada presentation order: absence found in two passes of a summarising tool; Figure 1 and its caption not read.
- Anoplophora: whether control aerations were run by GC-MS or GC-EAD (the tool reports no statement); male Y-tube figures are tool summary.
- Bagrada hilaris accepted status not read from a checklist page.
- Coryphodema: whether "n = 5" is five per sex; Table 5 trap counts not read; dichloromethane-only GC-MS count (27) is tool summary.
- Dash, degree and µ characters in the three two-piece quotes not checked against raw page characters (audit-324 condition 6); the tool rendered them as recorded.

## Replacement text

Line 1:
- `conditions`: "no solvent or blank control and no EAD statistics are described; non-responding runs not reported." -> "12 male, 12 female and 12 control (empty-jar) aerations were collected, but no analysis of the control aerations is reported, and no GC-EAD blank or solvent run and no EAD statistics are described; non-responding runs not reported; aeration adults were 2 to 3 weeks old and laboratory-study adults 3 to 4 weeks old, EAD beetle age not stated."
- `conditions`: "Behavioural tests (Y-tube, chi-square) are separate and not summarised here." -> "In Y-tube tests females chose the three-component blend over control (16 of 20, p < 0.05) but no two-component blend and no single compound significantly; males were not significantly attracted to any blend or dose (alcohol alone 14 of 20, p = 0.07364)."
- `note`: "The design gaps (n not reported, no control) are the paper's, not omissions here." -> "The design gaps (number of EAD runs not reported, no GC-EAD blank described, control aerations collected but their analysis not reported) are the paper's (audit 326)."

Line 3:
- `conditions`: "tested in ascending order, 1.5 s puffs" -> "presentation order not stated, 1.5 s puffs"
- `conditions` (uncounted): "antennae of all stages reached saturation and responded less at 200 ug." -> "antennae of all stages reached saturation and responded less at 200 ug. In the olfactometer females were attracted to (E)-2-octenyl acetate against air (chi2 = 10.52, p < 0.001, n = 46) and with host seedlings (chi2 = 5.22, p = 0.02, n = 62)."

Line 4:
- `conditions`: "tested in ascending order, 1.5 s puffs" -> "presentation order not stated, 1.5 s puffs"
- `conditions`: "antennae of all stages reached saturation and responded less at 200 ug." -> "antennae of all stages reached saturation and responded less at 200 ug. Males were not attracted to (E)-2-octenyl acetate in the olfactometer, against air (chi2 = 0.71, p = NS, n = 36) or with host seedlings (chi2 = 0.96, p = 0.3, n = 66); field traps at 10 mg caught females and nymphs, at 5 mg only nymphs, and none at 2 mg or in controls."

Line 5:
- `note`: "males larger responses than females to four compounds, no differential sensitivity for Z11-14:OH and Z9-14:OH;" -> "males larger responses than females to Z9-14:OAc, Z7-14:OAc, E9-14:OAc and Z9-14:Ald, females more sensitive only for 14:OAc (printed '14-Ac'), no differential sensitivity for Z11-14:OH and Z9-14:OH; five zero values at lower concentrations (Z9-14:Ald, Z9-14:OH, Z11-14:OH) left a significant dose:sex interaction only for Z11-14:OH;"

Verdict: 4 of 4 audited records in error (100%), above the 5% bar; all fixable mechanically with the text above; line 2 held out as a repeat of main (desk-d232).
