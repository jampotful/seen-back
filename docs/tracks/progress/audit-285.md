# audit-285: desk-d201 (1 evidence record, no search records, no wanted lines)

Audited 31 October 2026 from the desk-d201 files present untracked in the worktree (docs/tracks/progress/desk-d201.md and 1 evidence line in docs/views/evidence/desk-d201.jsonl; neither committed here, neither edited). HEAD 3c8c4ef2 equals origin/main. `tools/senses/check.py` on the evidence file: 1 record, 0 problems. Quote length (`len(q.split())`): 26, within 40. No searched or wanted file, so the one record was judged whole. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md and BRIEF (whole sentence, 40 words, grade, `partial`), desk-audit.md (no 125-character limit), the BRIEF trait table (`sense_chemical`, `sense_thermal` under "other senses"), the publisher-copy licence rule and the name rule, in the form of audits 270 to 284. Duplicates checked with git grep on origin/main across docs/views (evidence, audit including corrected/ and ALL.jsonl, searched, wanted, gaps, sheets) and views/ for the binomial, the DOI suffix, the title words "Induction Coil", the strings Bloomquist and Richoux, and "DEET". 0 WebSearch and 5 WebFetch calls used.

Sources opened: api.crossref.org/works/10.3389/FEVO.2019.00247 (uppercase answered); the record URL frontiersin.org/articles/10.3389/fevo.2019.00247/pdf (three passes). api.gbif.org/v1/species/1651891 returned PROVENANCE_REQUIRED (permission not answered) and was not retried. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries, so the quote was checked as MATCH/MISMATCH; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification.

## Bibliographic and licence

- Yang et al. 2019, fresh Crossref: Liu Yang, Yuzhe Liu, Gary M. Richoux, Ulrich R. Bernier, Kenneth J. Linthicum, Jeffrey R. Bloomquist, in the recorded order; title "Induction Coil Heating Improves the Efficiency of Insect Olfactory Studies" as recorded; Frontiers in Ecology and Evolution 7, article number 247; issued and published online 2019-06-28 (the note's "issued 28 June 2019" agrees); licence CC BY 4.0 (vor, from 2019-06-28, delay 0); relation empty; no update-to. PDF: "Copyright © 2019 Yang, Liu, Richoux, Bernier, Linthicum and Bloomquist." and "This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY)." Licence on the exact copy read: met.

Bibliographic faults 0; licence faults 0.

## Names

- Aedes aegypti: docs/views/gaps/gbif-names.tsv "Aedes aegypti EXACT ACCEPTED Aedes aegypti Aedes 1651891". The GBIF API page for 1651891 was blocked for me (not retried), so the authority was not re-read live; the tsv row is the desk's standing name source. Accepted. Family Culicidae and order Diptera fit.

Name faults 0.

## Duplicates

- Aedes aegypti on main: lambda_max_nm (van der Kooi et al. 2021 review; audit/corrected insect 183, 184 and methods 703, 704; ALL 1565, 1566, 3166, 3167), acuity_cpd (canon-4:35), sense_thermal (desk-d144:2, 3, Corfas and Vosshall 2015), sense_infrared (desk-d156:1 to 3, Chandel et al. 2024), behaviour_vision (oa-13b:251, 252; oa-13c:41 to 43). No sense_chemical row for the species and no row from this paper under any trait.
- DOI suffix fevo.2019.00247, "Induction Coil", Bloomquist, Richoux: absent from origin/main. "DEET" on main: only the tick sheet (docs/views/sheets/tick.md and tick.audit.md, a tick thermotaxis study), unrelated.
- Main-row notes: the desk-d144 sense_thermal rows are mosquito thermotaxis to warmed targets, a different stimulus and paper; no contradiction with an EAG odour result.

Duplicates 0.

## Per-paper findings

### Yang et al. 2019, Aedes aegypti (line 1)

Design (tool summary with verbatim fragments). Orlando strain ("established in 1952"); "Non-blood fed 4–7 day old adult female antennae were used for the EAG tests"; "EAG recordings for each chemical were obtained from at least seven antennae, each removed from a different female"; humidified air at 0.6 L/min, 120 s between stimulations. Stimulus: "10 µL of liquid DEET or 1-octen-3-ol in 10 µL of acetone solution were applied to a filter paper strip"; the per-dose preparation of 1 mg and 0.1 mg is not stated separately (tool summary). Heating: "the pipette was fixed in the middle of the heating coil"; the 20-gauge carbon steel wire reached 135 ± 2.7 °C after 4 s at 10 V (tool summary); the sample's own temperature is not reported. Room temperature "ca. 25◦C" (Abstract). Antenna side: "The temperature change of the airstream delivered to the antenna was measured in separate studies", by "inserting the thermocouple into the outlet of the air flow pipette", rise "no more than about 1◦C". Correction: "EAG responses to volatiles were calculated as corrected EAG values by subtracting the matched blank response"; clean air and "evaporated acetone paper strip" as negative controls; no heated blank reported. Statistics: unpaired t-tests (GraphPad Prism 7.0), so heated and unheated groups are different antennae (inference from the test, not stated). Results: unheated 1 mg 0.34 (± 0.05) mV; no heated 1 mg mean printed; 0.1 mg 0.11 (± 0.03) mV unheated against 0.33 (± 0.05) mV heated, t = 3.87, df = 14, P = 0.002; heated 0.1 mg "virtually equal to the EAG response of 1 mg (0.34 ± 0.05 mV)" (F = 0.81, df = 2, 19, P = 0.46). Discussion: the equal responses were "clearly because the odorant receptor response was maximal at 1 mg for both compounds at room temperature"; no thermal-degradation test of DEET at 135 °C (the NMR check covered VUAA-1 only), with the general caution that "any heating paradigm must consider the thermal lability of the material under study."

Quote. MATCH: the second fetch returned "The EAG response to 1 mg DEET showed no significant change in amplitude with or without heat (t = 0.02, df = 12, P = 0.986)." whole, under Results, subsection "EAG Response in Coupled Induction Heating-Electroantennogram System", as `where` says. One sentence, one section, 26 words, no cuts needed. The value says no more than the quote except the heating temperature, which comes from Methods (see below). Quote-form 0.

Trait key. `sense_chemical` is right: the stimulus is an odorant at the antenna, and the heat is applied to the odour source to raise volatilisation. It does not belong under `sense_thermal`: the measured airstream at the antenna rose by no more than about 1 °C, so the antenna received no thermal stimulus the design varies; main's Aedes sense_thermal rows (desk-d144) are behavioural thermotaxis to warmed targets, a different thing. No owner reading covers animal sense_chemical with a heated source (the owner's readings in desk-screen.md point 10 concern plant sense_chemical); nothing in them moves this record.

Line 1. Counted (scientific context, causal interpretation; fixable). The filed result is a null: heat did not change the response to 1 mg DEET. The authors explain that null as a ceiling, the receptor response being "maximal at 1 mg ... at room temperature", which is why heating the tenfold smaller dose raised it to the same 0.34 mV. The record carries the 0.1 mg exception correctly in `conditions` (about 3-fold, 0.11 to 0.33 mV, P = 0.002, matching unheated 1 mg) and limits the null to 1 mg, but it never says the 1 mg response was already saturated. Read without that, the row is a heat-insensitivity null about DEET detection; read with it, the 1 mg null carries no information about heating at all, because the antenna had no headroom. That changes the causal interpretation of the only finding the row files (oa-audit.md: a null whose stated explanation limits it). The fix belongs in `value`, since it limits the result.

Uncounted, suggested (each harmless to the direction of the finding, or unknown from the paper):
- `value` says "when the sample was heated to 135 C"; the paper reports the wire at 135 ± 2.7 °C, not the sample (`method` has this right). Reword.
- `conditions` "1 mg DEET applied in 10 uL acetone": the Methods wording ("10 µL of liquid DEET ... in 10 µL of acetone solution") does not state each dose's preparation; mark it as the Methods' general wording.
- Sample sizes: df = 12 implies 7 antennae per group at 1 mg; df = 14 implies 16 antennae over the two 0.1 mg groups; the three-group F has df 2, 19. Worth printing with the 0.34 ± 0.05 mV unheated 1 mg amplitude, which is printed in the same subsection (the value's "the amplitude itself is not in the quoted sentence" is true but the figure is available).
- Design confounds: no heated blank is reported, so the blank subtracted from heated samples may be an unheated one; the airstream at the antenna rose no more than about 1 °C (thermocouple at the pipette outlet), which answers the antenna-temperature question; DEET itself was not tested for thermal degradation at 135 °C. None reverses the 1 mg null (a heated-blank artefact or degradation would bias against equality, and equality was found), so they are left uncounted, but they belong in `conditions`.

Grade m right (one named species measured in the source); access open; `partial` false right (full text read). `eye` "antenna (electroantennogram)" fits. `method` fits.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Aedes aegypti, EAG to 1 mg DEET unchanged by heating (null) | correct | value, conditions | Quote MATCH; 0.1 mg exception carried; omits the authors' explanation that 1 mg was already at maximal response, so the null reads as heat-insensitivity rather than a ceiling |

Evidence errors: 1 of 1 (100%): scientific-context faults 1 (line 1); quote-form 0; name 0; duplicates 0; licence 0; bibliographic 0; abstract-access grading 0. Unfixable records: none.

Pooled with audits 172 to 284: 263 of 613 evidence records (42.9%; audit 284's 262 of 612, and 1 of 1 here). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Counted (line 1):
- `value`: "female antennal EAG response to 1 mg DEET did not change in amplitude when the delivery wire was heated to 135 C (t = 0.02, df = 12, P = 0.986); unheated 1 mg gave 0.34 +/- 0.05 mV, which the authors read as the maximal receptor response, so the null reflects a ceiling at this dose rather than no effect of heating (heated 0.1 mg rose about 3-fold to the same level)"
- `conditions`: replace "1 mg DEET applied in 10 uL acetone" with "stimulus applied to a filter paper strip (Methods: '10 µL of liquid DEET ... in 10 µL of acetone solution'; per-dose preparation not stated separately)"; replace "values corrected by subtracting the matched blank (acetone-treated paper strip, clean air)" with "values corrected by subtracting the matched blank (clean air and evaporated acetone paper strip as negative controls; no heated blank reported)"; append "7 antennae per group at 1 mg (df 12), 16 antennae over the two 0.1 mg groups (t = 3.87, df = 14); unpaired t-tests, so heated and unheated groups are different antennae; heated 0.1 mg against unheated 1 mg F = 0.81, df = 2, 19, P = 0.46; airstream at the antenna rose no more than about 1 C (thermocouple at the pipette outlet); DEET not tested for thermal degradation at 135 C (NMR check on VUAA-1 only)".
- `note`: append "The authors' Discussion attributes the equal responses to the odorant receptor response being maximal at 1 mg at room temperature (fetch summary with fragment)."

## Owner questions

1. A null filed at a dose the authors say already saturates the response: should such rows be filed at all under sense_chemical, or held as uninformative, with only the positive 0.1 mg heating result (if a whole sentence under 40 words can be read) filed instead?
2. For animal records where heat is applied to an odour source and the airstream at the antenna is measured as nearly unchanged (here no more than about 1 C), confirm that `sense_chemical` is the key and that no `sense_thermal` row is implied.

Progress note: accurate on the DOI, licence, authors, n and name, and it states the 0.1 mg result and the dose limit. It does not mention the authors' ceiling explanation. The held-out leads were not re-checked here (they are not filed records).

Verdict: 1 error in 1 (100%), above the 5% bar; pooled 42.9%. Error line: 1. No unfixable records; line 1 can merge with the counted text.

This report is model output and carries no authority.
