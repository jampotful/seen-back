# audit-365: desk-d272, evidence lines 1 to 4

Audited 1 November 2026 from the desk-d272 files present untracked in the worktree (docs/tracks/progress/desk-d272.md and docs/views/evidence/desk-d272.jsonl, 4 lines; neither committed here, neither edited; the evidence file is byte-identical to origin/research/desk-d272). Worktree HEAD and origin/main b1829aa2 (d271 merged after audit 364). `python3 -I tools/senses/check.py | grep 'd272\.'`: "docs/views/evidence/desk-d272.jsonl: 4 records, 0 problems". Quote lengths (`len(q.split())`): 9, 9, 7, 17, all within 40. Non-ASCII in quotes: "±" (U+00B1) in lines 1 to 3, "μ" (U+03BC, Greek mu, as the page's table prints it) in line 3; line 4 has "um" in ASCII, as printed (the page prints "um" in that sentence and "μm" in its tables). Format model audit 358; desk-audit.md evidence clause (40-word limit, no 125-character limit); abutting pieces under audit-324.md (not needed: every quote here came back in one piece), cuts under audit-331.md (no quote is cut); ommatidia_count convention per audits 362 and 364.

Sources opened (WebFetch): www.frontiersin.org/articles/10.3389/fphys.2024.1343702/full (four passes, URL from my WebSearch); api.crossref.org/works?filter=doi:10.3389/fphys.2024.1343702 (list query, answered); www.afromoths.net/species/19403 (name). PMC, the DOAJ, UTM, CAS and OUCI catalogue copies, the epub and the public-pages text copy were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 2 WebSearches.

## Bibliographic and licence

Crossref (filter=doi list query): Xiaofan Yang, Hongfan Ran, Yueli Jiang, Ziyun Lu, Guoshu Wei, Jiancheng Li, in that order; title identical to the records, "(Busck 1916)" without comma as in the records; Frontiers in Physiology, volume 15, article-number 1343702, no issue; issued and published 2024-02-02; licence https://creativecommons.org/licenses/by/4.0/, content-version vor, delay 0, start 2024-02-02; no relation. The page (tool summary) gives the same authors, "Frontiers in Physiology, volume 15 (2024), article 1343702", published 02 February 2024, and no licence or copyright sentence in the article text (only a "Copyright statement" navigation link). Accepted under the rule "publisher page with no licence sentence + Crossref CC licence for version of record (vor) on that DOI"; the licence rests on a permitted list query, as the note says (the /works/<doi> form was not tried here). source.access "open" right; url opens. Bibliographic faults 0; licence faults 0.

## Names

docs/views/gaps/gbif-names.tsv line 2023: "Grapholita molesta	EXACT	ACCEPTED	Grapholita molesta	Grapholita	1736574". Afromoths (named checklist, tool summary): Grapholita molesta, Busck, 1916, valid, Tortricidae: Olethreutinae, original combination "Laspeyresia molesta, n. sp." (verbatim). Title prints "(Lepidoptera: Tortricidae)". Taxon, family and order right. Name faults 0.

## Duplicates

git grep on origin/main (b1829aa2) across the whole docs/ tree (including docs/views/audit/corrected, audit/ALL.jsonl, sheets, searched/, recheck/) for "Grapholita molesta" and "1343702": the only evidence row from this paper is sweep-56.jsonl line 10 (interommatidial_deg 4.3). Other hits are Grapholita dimorpha opsin rows (oa-1), the Martín-Gabarrella et al. 2025 Cydia pomonella row (sweep-40, recheck), which mentions "~ 15 µm in GM" inside a Cydia record, and search records that chased or screened this paper. No ommatidia_count, facet_diameter_um or rhabdom_um row for the species or the DOI. Branch-only additions over all 159 origin/research/desk-d2* and audit-3* branches: only research/desk-d272 itself and desk-d267.md (a JEB tortricid ERG paper, a different work). Duplicates 0.

Consistency with sweep-56 (main): that row quotes Section 3.2, "determined from the diameter of the corneal lens (15.8 μm) and the eye radius of 211.6 μm", and its method says "corneal lens diameter (15.8 um)". Line 3 files 15.2 µm for the facet diameter from Table 1 and Section 3.1. Both figures are printed by the paper for the same structure; neither row says so. Line 3's share of this is counted below; sweep-56's (uncounted, a main row) should gain the same cross-reference when main rows are next touched.

## Trait keys

- ommatidia_count: not in check.py TRAITS; admitted because both notes say "new trait". In use on main (oa-2, oa-3, oa-5, oa-6, oa-14, recheck, audit/corrected/methods.jsonl, desk-d270, desk-d271). Sexes as separate records with both values in conditions, the merged d270/d271 convention (audits 363, 364). Units "facets per compound eye": audits 362 and 364 offered main's commonest "ommatidia/eye", uncounted; offered again.
- facet_diameter_um: not in TRAITS; note says "new trait"; main units "µm" in all rows (audit 362); line 3 matches.
- rhabdom_um: in TRAITS on main and in the worktree (check.py line 15); line 4's note rightly omits "new trait". Main uses the key for both lengths and widths (99 rows; units "µm" 75, "µm (length)" 1, "µm (length, diameter)" 1, blank 22); line 4's quote says "total length" but its units and conditions do not; "µm (length)" offered, uncounted.

Trait-key faults 0.

## Per-record findings

### Lines 1 and 2, ommatidia_count, male 1072 and female 1029

Table 1 as rendered (column header "Structural compositions | Morphological data | N | Unit | Measurements"): "| | facet number in males | 5 | - | 1072 ± 37 |" and "| | facet number in females | 5 | - | 1029 ± 15 |"; the group cell is empty in these rows (merged "Compound eyes" cell; tool summary placed them under Compound eyes). Joining the cells with single spaces gives the quotes exactly: "facet number in males 5 - 1072 ± 37", "facet number in females 5 - 1029 ± 15". Whole rows, one table, "±" as printed, unit cell "-" kept. **Quotes MATCH** (9 words each). Each value is the mean of its row and says no more.

Verified, verbatim: Section 3.1 "Each compound eye of male and female individuals consists of approximately 1072 and 1029 facets, respectively (p = 0.077),"; Section 2.4 "To study numbers and sizes of the facets, the eyes of adult G. molesta (5 males and 5 females) were removed from the heads" | "and covered with a thin layer of colourless nail polish to produce cornea replicas"; replicas flattened on a slide, coverslipped, sealed with wax and "photographed under an Olympus BX63 light microscope"; Section 2.5 "The independent samples t-test was used to examine the difference between both sexes."; origin "laboratory strain ... wild-caught larvae ... peach orchard in Shunping County, Hebei Province, China, in August 2020", 26 C, 15L:9D, three-day-old adults (tool summary). The "±" statistic is not defined anywhere (tool, asked directly); the records say so.

Fault (design misdescribed). The records say "moths were light-exposed at one of four intensities ... for 2 h before decapitation at 20:00 (Section 2.2); the sex-by-intensity allocation of the 5 specimens is not stated". The exposure sentence is in Section 2.1 and is tied to the adaptation experiments: "For different light intensity adaptational experiments, specimens were exposed to four different light intensities" | "for 2 h prior to decapitation at 20:00 (when the moths are mostly active)."; Section 2.2 is TEM: "Five specimens of four light intensity adaptational states (10000, 100, 1, and 0.01 mW/m2)" | "of each sex were used for TEM." Section 2.4 (facet counts) and the SEM section describe no light treatment (tool summary, asked directly). So the paper does not say the five plus five facet-count moths were light-treated; the records assert it and cite the wrong section. Whether they came from the treated heads is unknown. The boring reading is that this changes nothing, since a 2 h light exposure cannot change facet number (my own construction, no source); it still tells a reader the counts carry a treatment the paper does not give them. Counted, because the records misstate the design and the launch prompt asks this exact question; if the owner rules a harmless misattribution uncounted, lines 1 and 2 become MATCH. Uncounted: method "facet counts from the removed eyes" leaves out that the counts were made on cornea replicas; "text reports the sex difference as not significant" is a paraphrase (the text prints only "(p = 0.077)", t-test per Section 2.5).

**Lines 1 and 2 error (light treatment attributed to facet-count specimens; section misattributed).** Fixable.

### Line 3, facet_diameter_um 15.2

Table 1 as rendered: "| Ommatidia | facet diameter | 60 | μm | 15.2 ± 0.3 |". The quote "facet diameter 60 μm 15.2 ± 0.3" is the row without its group cell, which here is "Ommatidia", not "Compound eyes" as the note says. "μ" is U+03BC on the page and in the quote. **Quote MATCH** (7 words). Value is the row's mean; Section 3.1 confirms it is a mean and gives the definition: "with a mean diameter of 15.2 μm (i.e., the corner to corner distance of facet"; Section 2.5: "SEM micrographs were used to determine the dorso-ventral and antero-posterior lengths of the eye," | "the diameters of the facet (i.e., the corner to corner distance of the hexagonal corneal surface) and ocelli." Sexes pooled; no sex test for facet size is reported (tool summary); the number of SEM individuals is not given (record right).

Faults:
- Omitted contrary value: Section 3.2 gives the corneal lens as 15.8 μm ("determined from the diameter of the corneal lens (15.8 μm) and the eye radius of 211.6 μm."), the figure main's sweep-56 row uses. The paper prints two diameters for the facet lens and does not reconcile them; the record gives only one.
- Design misdescribed, as in lines 1 and 2: "moths light-exposed at one of four intensities before fixation (Section 2.2)" for SEM specimens whose light history the paper does not state.
- Uncounted: the method should name SEM micrographs; ± not stated as SD or SE; note's group-cell name wrong.

**Line 3 error (conflicting 15.8 μm text value omitted; light treatment misattributed).** Fixable.

### Line 4, rhabdom_um 62.3

Section 3.2.3, verbatim in one piece: "Each ommatidium contains eight retinula cells to form a rhabdom, measuring about 62.3 um in total length." The sentence before ends Section 3.2.2 ("... where mitochondria are abundant in the cytoplasm of these cells."), the one after begins "In all ommatidia, seven retinula cells (R1-R7, called regular retinula cells) participate in the formation". Whole, begins and ends where printed, "um" as printed. **Quote MATCH** (17 words). The value is total rhabdom length, which says no more than "about 62.3 um in total length". Table 1: "| Rhabdom | length | 12 | μm | 62.3 ± 2.2 |"; distal and proximal diameters 1.8 ± 0.3 and 5.2 ± 0.5 µm, N = 10 (tool summary). Section 2.5: "Longitudinal sections for TEM were used to measure the ommatidial lengths, rhabdom lengths, radii of curvature of eye,". Distal rod, verbatim: "form a centrally-fused distal rhabdom rod" | "with a length of 31.4 μm and a diameter of 1.8 μm (measured in the most distal end)."

Faults (omitted nulls and a significant result; sample composition misstated):
- "sex not stated" understates what the paper gives: TEM used five of each sex at each of four states (Section 2.2, above; 40 specimens), and Section 3.2 says "Based on the electron microscopic observations from the central region of the eye," "no significant differences were detected between the eyes of male and female moths." The sex of the N = 12 is still not given.
- "the paper reports no per-state rhabdom length" is true, but the record drops the authors' null, Section 4.2: "Other feathers such as the size of rhabdom are not obvious different during different light intensity adaptations." (sic), and the significant positional change, Section 3.3: "The shape of crystalline tract and the position of the distal rhabdom are significant different" | "among different light intensity adaptation."; "In bright-light-adapted eyes the retinula cell bodies pull away from the cone,". So the length is reported as stable across states (by eye, no test given) while the rhabdom's position shifts.
- Uncounted: the note's "Table 1 row quoted without its merged 'Compound eyes' group cell ..." sentence does not apply to a sentence quote; "fused rhabdom" in eye is the paper's term only for the distal rod.

**Line 4 error (sex and light-state nulls and the significant distal-rhabdom shift omitted; TEM sex composition misstated).** Fixable.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Grapholita molesta, ommatidia_count 1072 (male) | error, fixable | conditions; method, units (uncounted) | row MATCH (9); light treatment attributed to facet-count moths, wrong section |
| 2 | Grapholita molesta, ommatidia_count 1029 (female) | error, fixable | as line 1 | as line 1 |
| 3 | Grapholita molesta, facet_diameter_um 15.2 | error, fixable | conditions; method, note (uncounted) | row MATCH (7); Section 3.2's 15.8 μm omitted; light treatment misattributed |
| 4 | Grapholita molesta, rhabdom_um 62.3 | error, fixable | conditions; units, note (uncounted) | sentence MATCH (17), total length; sex null, light-state null and distal-rhabdom shift omitted; TEM sexes misstated |

Errors 4 of 4 audited records (100%), above the 5% bar; none held out. By kind: design misdescribed 3 (lines 1 to 3; the weakest call, see line 1); omitted contrary value 1 (line 3); omitted null/significant results 1 (line 4); quotes 0; bibliographic 0; licence 0; names 0; duplicates 0 against main and all 159 desk-d2*/audit-3* branches; trait keys 0. If the owner treats the light-treatment misattribution as uncounted, the rate is 2 of 4 (50%), still a fail.

Unchecked: the exact printed Table 1 layout beyond the tool's rendering (cell spacing is the fetch's; the joins match single-space joins of the rendered cells); the number of SEM specimens; whether the facet-count replicas came from the light-treated heads (the paper does not say); whether Table 1's N = 12 for rhabdom length counts ommatidia or individuals; the PDF's printed year line (2024 rests on the page summary and Crossref, which agree).

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). For an empty new string the old string is deleted.

Lines 1 and 2, each, counted:
- `conditions`: "; moths were light-exposed at one of four intensities (10000, 100, 1 or 0.01 mW/m2) for 2 h before decapitation at 20:00 (Section 2.2); the sex-by-intensity allocation of the 5 specimens is not stated" -> "; for its light-adaptation experiments the paper exposed specimens to one of four intensities (10000, 100, 1 or 0.01 mW/m2) for 2 h before decapitation at 20:00 (Section 2.1) and used five of each sex per intensity for TEM (Section 2.2); Section 2.4 does not say whether the facet-count moths were light-treated or from which group they came"

Lines 1 and 2, each, uncounted:
- `conditions`: "text reports the sex difference as not significant (p = 0.077)" -> "Section 3.1 prints p = 0.077 for the sex difference (independent samples t-test, Section 2.5)"
- `method`: "facet counts from the removed eyes (Section 2.4)" -> "facets counted on nail-polish cornea replicas of the removed eyes, photographed under a light microscope (Sections 2.4, 2.5)"
- `units`: "facets per compound eye" -> "ommatidia/eye"

Line 3, counted:
- `conditions`: "; moths light-exposed at one of four intensities before fixation (Section 2.2)" -> " (collected August 2020); the light history of the SEM specimens is not stated (the four-intensity exposure is described for the light-adaptation experiments and TEM, Sections 2.1, 2.2); sexes pooled and no sex test for facet size reported; Section 3.2 gives the corneal lens diameter as 15.8 µm (the figure used for the 4.3° interommatidial angle, main sweep-56), which the paper does not reconcile with the 15.2 µm of Section 3.1 and Table 1"

Line 3, uncounted:
- `conditions`: "mean 15.2 ± 0.3 over 60 facets (Table 1)" -> "mean 15.2 ± 0.3 over 60 facets (Table 1; ± not stated as SD or SE)"
- `method`: "facet diameter measured as corner to corner distance of a facet" -> "facet diameter measured on SEM micrographs as the corner to corner distance of the hexagonal corneal surface (Section 2.5)"
- `note`: "merged 'Compound eyes' group cell" -> "merged 'Ommatidia' group cell"

Line 4, counted:
- `conditions`: "sex not stated; specimens of four light-adaptation states (10000, 100, 1 or 0.01 mW/m2, 2 h) were sectioned, and the paper reports no per-state rhabdom length" -> "total rhabdom length (the centrally-fused distal rhabdom rod is 31.4 µm long and 1.8 µm wide at its distal end); sex of the 12 not stated, but TEM used five of each sex at each of four light-adaptation states (10000, 100, 1 or 0.01 mW/m2, 2 h; Section 2.2), and the paper gives no per-sex or per-state rhabdom length; it reports no significant differences between the eyes of males and females (Section 3.2) and says the size of the rhabdom was not obviously different between light-adaptation states (Section 4.2, no test given), while the position of the distal rhabdom differed significantly between states, the retinula cells pulling away from the cone in bright light (Section 3.3)"

Line 4, uncounted:
- `units`: "µm" -> "µm (length)"
- `note`: "Table 1 row quoted without its merged 'Compound eyes' group cell; the fetch rendered the table as text, so spacing between cells is the fetch's. " -> ""
