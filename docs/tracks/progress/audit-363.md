# audit-363: desk-d270, evidence lines 5 to 9

Audited 1 November 2026 from the desk-d270 files present untracked in the worktree (docs/tracks/progress/desk-d270.md and docs/views/evidence/desk-d270.jsonl, 9 lines; neither committed here, neither edited). Lines 1 to 4 (Arge similis) go to another auditor. Worktree HEAD and origin/main 6d94bb12 (merge of d267 after audit 360). `python3 -I tools/senses/check.py | grep 'd270\.'`: "docs/views/evidence/desk-d270.jsonl: 9 records, 0 problems". Quote lengths (`len(q.split())`): 17, 20, 30, 30, 27, all within 40. Non-ASCII in quotes: "–" (U+2013) in line 5; "±" (U+00B1) and "µ" (U+00B5) in lines 7 and 8; "Δ", "ϕ" (U+03D5), "°" and "–" in line 9. Format model audit-358.md; desk-audit.md evidence clause (40-word limit, no 125-character limit); abutting pieces judged under the six conditions of audit-324.md, cuts under audit-331.md.

Sources opened (WebFetch): api.crossref.org/v1/works/ for 10.3390/insects16070682 and 10.3390/insects16080771 (one pass each, both answered, neither robots_disallowed); www.mdpi.com/2075-4450/16/7/682/html (two passes); www.mdpi.com/2075-4450/16/8/771 (three passes). Names: species.biodiversitydata.se/species/6208391 and /6208400, lepiforum.org LepiWiki page, eol.org/pages/371626; publication.plazi.org and treatment.plazi.org (redirect placeholders only), mapress.com zootaxa.5165.4.7 and bonn.leibniz-lib.de node 19167 (no Histia content). GBIF, Catalogue of Life, PMC (PMC12386418) and the Wikipedia mirrors were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 5 WebSearches.

## Bibliographic and licence

- Line 5 (Xie et al. 2025). Crossref: Hua Xie, Yan Shi, Shouxian Zhang, Yonghui Zhu, Subo Shao, Yuan Zhang, Pei Yang, Zongbo Li, in that order; title identical to the record; Insects volume 16, issue 7, article 682; issued 2025-06-30; licence CC BY 4.0, content-version vor, delay 0; relation empty, no update-to. Page: "Insects 2025, 16(7), 682" (tool summary of the rendered citation); no licence sentence in the body; page metadata rights CC BY 3.0 (the accepted CC BY 3.0 page vs CC BY 4.0 Crossref case). Accepted. Faults 0.
- Lines 6 to 9 (Chen, Li and Huo 2025). Crossref: Qing-Xiao Chen, Ya-Fei Li, Yun-Zhu Huo; title identical; Insects 16, issue 8, article 771; issued 2025-07-27; CC BY 4.0 vor, delay 0; relation empty, no update-to. Page prints "Insects 2025, 16(8), 771; https://doi.org/10.3390/insects16080771"; no CC sentence in the body (tool summary: an MDPI reuse statement and metadata rights CC BY 3.0). Accepted. Faults 0.

source.access "open" right in all five. Bibliographic faults 0; licence faults 0.

## Names

- Ceratosolen gravelyi: docs/views/gaps/gbif-names.tsv:1015 "Ceratosolen gravelyi EXACT ACCEPTED ... 1359208". A search returned several papers using the name for the pollinator of Ficus semicordata in Agaonidae (titles only). Family and order as printed in the paper title. Met. Authority and synonymy in the Universal Chalcidoidea Database not checked (no UCD or Taxapad page in the results).
- Histia flabellicornis: absent from gbif-names.tsv. desk-d187.md:12 held this paper for want of a name authority; audit-300 then accepted the name on insecta.pro for desk-d215 line 2, which is now on main. This audit adds: LepiWiki (Lepiforum) "Histia flabellicornis (Fabricius, 1775)" in Zygaenidae, Chalcosiinae, Chalcosiini, with subspecies atrovirens, azurea and obsoleta linked; EOL "Histia flabellicornis Fabricius 1775", Zygaenidae, Lepidoptera, no taxonomy source named; the Swedish ALA portal (species.biodiversitydata.se), whose classification is the GBIF backbone, lists "Histia flabellicornis obsoleta" and "Histia flabellicornis tahanica" (synonym "Histia tahanica") as accepted names, both under the species node Histia flabellicornis in Zygaenidae; no name source is printed on those pages (tool summary). No direct GBIF or Catalogue of Life page was reachable (GBIF refused by rule; no CoL page in the results). Four independent aggregators agree, none lists the name as a synonym, and main already carries the name. Met for the record, uncounted, with the gbif-names.tsv addition still owed by the owner (desk-d215 owner question).

Name faults 0.

## Duplicates

git grep on origin/main (6d94bb12) across the whole docs/ tree (including docs/views/audit/corrected, audit/ALL.jsonl, sheets, searched/, recheck/) for "Histia", "flabellicornis", "insects16080771", "Ceratosolen" and "insects16070682":

- Histia, interommatidial_deg 4.08: **on main**. docs/views/evidence/desk-d215.jsonl:2 is Histia flabellicornis, interommatidial_deg, value 4.08, units degrees, same DOI, quoted from the Abstract ("The calculated interommatidial angles (Δϕ = 4.08°) and the eye parameter P (P = 1.74) suggest ..."), audited "stands" in audit-300. desk-d249.md:15 also lists insects16080771 as already on main. d270 line 9 repeats it from the Discussion. The desk note checked main for Ceratosolen (sweep-66) but not for Histia.
- Histia ommatidia_count and facet_diameter_um: no record on main under any trait key. The facet values 24.45 ± 0.30 (females, n = 8) and 24.43 ± 0.35 µm (males, n = 8) are cited inside the `conditions` of desk-d215.jsonl:2 as context for the angle; "over 2000 ommatidia" appears only in desk-d187.md:12 (a held lead). I do not count these as repeats (a different trait, not filed as a value), but see owner question 2.
- Ceratosolen gravelyi on main: sweep-66 lines 5 to 7 (interommatidial_deg 9.3, acceptance_deg 10.0, f_number 1.1; conditions empty) and recheck-quotes-3-fixed.jsonl:171 (the corrected 9.3 row). No ommatidia_count row and no 228 or 263 anywhere for this species. Line 5 is new.
- Branches: of the origin/research/desk-d2* and audit-3* branches, only research/desk-d215 (the merged unit) and research/desk-d270 (this unit) add Histia or Ceratosolen evidence lines; the rest differ only in desk-queue.md and wanted-merged.csv. No audit-3*.md hold-out names either species except audit-300 (above).

Duplicates 1 (line 9).

## Trait keys

ommatidia_count and facet_diameter_um are absent from TRAITS in tools/senses/check.py (line 11 on) and pass because the notes say "new trait"; both keys are in use on main (ommatidia_count about 62 rows, mostly int with units "ommatidia/eye", "count" or "ommatidia"; facet_diameter_um about 70 rows, units "µm"). interommatidial_deg is in TRAITS. Units strings differ from the commonest main forms but are clear; uncounted.

"over 2000" as a value: main has no list or range for ommatidia_count but carries a string lower bound elsewhere ("over 40" for Alpheus heterochaelis cff_hz, verdict stands; "at least 3" for Bombus acceptance_deg) and the string "about 5000" for Parnassius glacialis ommatidia_count (oa-14). On main's convention the string is acceptable; it says exactly what the page says. Uncounted. The [228, 263] list for a range is also used on main for other traits (desk-d154 and others).

## Per-record findings

### Line 5, Ceratosolen gravelyi, ommatidia_count [228, 263]

Abstract, verbatim in one piece: "The oval apposition eyes contain 228–263 ommatidia, which are asymmetrically distributed between the left and right eyes." MATCH, whole sentence, 17 words, en dash as printed. The Simple Summary ("Their oval-shaped eyes have 228–263 tiny eye units (ommatidia).") and Section 3.1 ("they contain 228–263 ommatidia with facet diameters (corner-to-corner distance) ranging from 9.3 to 13.5 µm", a piece) agree. Value says no more than the quote; units and the adult-female eye follow the title.

What the range spans: Section 3.1, verbatim in pieces: "Notably, ommatidial counts exhibit bilateral asymmetry within individuals (e.g., left eyes: 248, 247, 228;" / " right eyes: 262, 263, 256, respectively)," / "and SEM analysis indicated that this stems from variation in spatial constraints during ommatidial differentiation" / ".". The six example counts span exactly 228 to 263, so the range is the extreme of six eyes, apparently three left and three right eyes of three females ("within individuals ... respectively"); "e.g." leaves open whether more eyes were counted, and no n and no test of the asymmetry are given (tool summary). Methods: "Following ultrasonic cleaning, 20 selected female specimens underwent sequential dehydration" (a piece) for SEM. The record's conditions say only "the range spans individual eyes ... no n in the abstract sentence", which omits that the Results print the per-eye counts behind the range, that they are examples from within individuals with left eyes lower than right in each, that the count's n is not stated though 20 females were prepared for SEM, and that no asymmetry test is reported. Sample-composition omission: **1 counted**.

Wild vs lab: "We collected newly matured stage D figs of F. semicordata" / "from Xishuangbanna Tropical Botanical Garden, Menglun, China"; "Figs were enclosed in nylon mesh bags to permit natural wasp emergence."; "Newly emerged individuals were anesthetized at −20 °C for 20 min." The record's "adult females emerged from wild-collected ... figs" is right; "date not stated" was not contradicted in my passes but I did not see the whole collection sentence (unchecked). Grade m right.

Line 5: 1 counted, fixable.

### Line 6, Histia flabellicornis, ommatidia_count "over 2000"

Section 3.1, verbatim in pieces in one response: "Each compound eye comprises over 2000 ommatidia, predominantly hexagonal in shape" / "with occasional quadrangular and pentagonal ones observed."; a separate pass asked for the tail with references returned "sional quadrangular and pentagonal ones observed (Figure 1B).". So the record's sentence, with "(Figure 1B)." at the end, is as printed; the comma after "shape" is in the record and in the first piece. MATCH, whole sentence, 20 words, contains the value. The Abstract also says "over 2000 ommatidia" with no sex (tool summary). Section 2.4: "A total of 40 adult specimens (20 females and 20 males) were used for morphological and anatomical analyses." and no n for the count (tool summary), as the conditions say. The preceding sentence gives eye diameter 0.91 mm in both sexes (n = 3 each) "with no significant sexual dimorphism", which needs no place in this record. Collection: campus of Henan University of Science and Technology, May 2023, adults collected there (field-collected, so wild; the page does not say "wild-caught", tool summary). Grade m right.

Line 6: MATCH, 0 counted.

### Lines 7 and 8, Histia flabellicornis, facet_diameter_um 24.45 (females) and 24.43 (males)

Section 3.1, verbatim in two abutting pieces in one response: "The diameter of the ommatidial facet is 24.45 ± 0.30 µm in females (n = 8) and 24.43 ± 0.35 µm in males (n = 8)," / "with no significant difference."; the tail pass returned "± 0.35 µm in males (n = 8), with no significant difference." with no figure or table reference. Audit-324 conditions met (one response, in order, no gap, the tail confirmed in a second pass, joined sentence 30 words). MATCH for both lines. Each value carries only its own sex and number; the sex comparison and both n are in the conditions.

Statistics, Section 2.4 (tool summary with pieces): "Mean values and standard errors were calculated using SPSS Statistics 20.0."; sex differences by "a two-tailed independent samples t-test" for n ≥ 6 and Mann–Whitney U for n < 6; "Statistical significance was set at p < 0.05." So ± is SE, as the records say, but the SE label comes from Section 2.4, not from "the sentence"; and the comparison was a t-test. Uncounted wording fix below. Whether µ on the page is U+00B5 or U+03BC cannot be told through the tool (the Ceratosolen page shows both); unchecked.

Lines 7 and 8: MATCH, 0 counted.

### Line 9, Histia flabellicornis, interommatidial_deg 4.08

Discussion, verbatim in two abutting pieces: "In H. flabellicornis, the interommatidial angle (Δϕ = 4.08°) is larger than that of most flying insects (1–3°) [30]," / " indicating a lower capacity for fine spatial resolution." MATCH, whole sentence, 27 words. Calculated by the authors (Section 2.4 "Δϕ = D/R", D the facet diameter and R the local radius of curvature, tool summary), printed in the paper and carried by the quote, so the calculated value itself is fileable, and the record says it is calculated. The Results print no angle (Table 1 not returned), sex and eye count for the angle are not stated, as the record says.

But the same species, trait, value and DOI are on main as desk-d215.jsonl:2 (audit-300, "stands"). A record repeating main is an error and cannot be fixed by editing. **1 counted; HOLD OUT.**

## Verdict

| Line | Record | Verdict | Counted | Note |
|---|---|---|---|---|
| 5 | Ceratosolen gravelyi ommatidia_count [228, 263] | error, fixable | 1 | conditions omit the six per-eye example counts behind the range, within-individual left/right pattern, unstated n (20 females prepared), no test |
| 6 | Histia flabellicornis ommatidia_count "over 2000" | MATCH | 0 | "over 2000" acceptable on main's string convention |
| 7 | Histia facet_diameter_um 24.45 F | MATCH | 0 | SE label is from Section 2.4 (uncounted wording) |
| 8 | Histia facet_diameter_um 24.43 M | MATCH | 0 | as line 7 |
| 9 | Histia interommatidial_deg 4.08 | duplicate of main | 1 | desk-d215.jsonl:2; HOLD OUT |

Errors 2 of 5 audited records (40%), above the 5% bar. Line 5 fixable with the replacement text below; line 9 held out; lines 6 to 8 stand. Verdict for lines 5 to 9: not accepted as filed; accept lines 5 (as corrected), 6, 7 and 8 and drop line 9.

Owner questions:
1. Add Histia flabellicornis (Zygaenidae) to gbif-names.tsv, as desk-d215 already asked; this audit's name evidence is aggregator-level (LepiWiki, EOL, GBIF-backbone-derived ALA pages), consistent and synonym-free, but no direct GBIF or CoL page.
2. Do facet values already printed in a main row's `conditions` (desk-d215:2 gives 24.45 and 24.43 with n) make a later facet_diameter_um record a repeat? I read the rule's "under any trait" as covering filed values, not context in conditions, and did not count lines 7 and 8.
3. The desk's own owner question on per-sex records from one sentence: lines 7 and 8 follow the practice of keeping sexes separate with both values in conditions, which is consistent and loses nothing.

Unchecked: Universal Chalcidoidea Database / Taxapad authority for Ceratosolen gravelyi; the full Ceratosolen collection sentence (date); Table 1 of the Histia paper; µ code points on the page.

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 5, counted:
- `conditions`: "no n in the abstract sentence" -> "Section 3.1 reports bilateral asymmetry within individuals and gives the counts as examples (e.g., left eyes 248, 247, 228; right eyes 262, 263, 256, respectively), so the range is the extreme of these six eyes, apparently three females with the right eye higher in each; no n is given for the counts (20 females were prepared for SEM, Methods) and no statistical test of the asymmetry is reported"

Lines 7 and 8, each, uncounted:
- `conditions`: "mean ± SE as stated in the sentence for both sexes" -> "mean ± SE (Section 2.4: means and standard errors; sexes compared by two-tailed independent-samples t-test for n ≥ 6, p < 0.05) for both sexes"

Line 9: HOLD OUT (repeats desk-d215.jsonl:2 on main: Histia flabellicornis, interommatidial_deg 4.08, same DOI). No replacement; delete the line.
