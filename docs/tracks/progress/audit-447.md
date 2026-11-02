# audit-447: desk-d332, evidence lines 7 to 12

Audited 1 November 2026 from the desk-d332 files present untracked in the worktree (docs/views/evidence/desk-d332.jsonl, 12 lines; docs/tracks/progress/desk-d332.md); neither committed here, neither edited. This audit covers file lines 7 to 12 only (Diploexochus, 2 records; Mongoloniscus, 4 records). HEAD 96bf60b19 (desk d331 merge). `tools/senses/check.py` and `--require-evidence-kind` on the file: 12 records, 0 problems.

Sources opened (WebFetch): api.crossref.org/works list queries (filter=prefix:10.3897 with date range and query) for both DOIs; zookeys.pensoft.net/article_preview.php?id=133267 (two passes); zookeys.pensoft.net/article_preview.php?id=113560 (one pass); zoobank.org nomenclatural act for Diploexochus cacique. No PMC, mirror, repository copy, proxy, ResearchGate or academia.edu page opened. The desk's XML URL for 133267 was not opened (not in a search result); the article page served the same text. WebFetch returns pieces of about 125 characters; sentences below marked whole were returned whole. 5 WebSearch, 6 WebFetch.

Duplicates: grep of the whole docs/ tree for "Diploexochus", "Mongoloniscus", "133267", "113560". The only hit outside desk-d332 is desk-d289.md line 15 (declined, no row). No Mongoloniscus or ZooKeys 1202 hit anywhere. Duplicates 0.

Trait key: ommatidia_count is on main (126 rows across desk-d270 to d306 and others), including two-number list values for ranges (Ceratosolen gravelyi [228, 263], Carebara colobopsis [5, 6]). Keys 0 faults.

## Lines 7 and 8, Diploexochus troglobius (4) and D. cacique ([20, 21]), ZooKeys 1223

Bibliographic: Crossref gives Ricardo Borja-Arrieta, Carlos Mario López-Orozco, Yesenia M. Carpio-Díaz, Miguel Gutierrez-Estrada, Ivanklin Soares Campos-Filho, Gabriel R. Navas-S., Maria Elina Bichuette in that order; title "From surface to caves: new species of Diploexochus Brandt, 1833 (Oniscidea, Armadillidae) from Colombia, with the description of the first troglobitic species" as one string, so the desk's join of the page's two pieces is right; ZooKeys 1223, pages 263-288, no issue; issued 2025-01-13; licence CC BY 4.0, vor. The page prints the same authors, "ZooKeys 1223: 263-288" and "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0)," Bibliographic and licence met.

Quotes: Description of each species, returned whole: "Cephalon (Fig. 9D–F) with prominent frontal shield, distinctly protruding above vertex; eyes with four ommatidia." (troglobius) and "Cephalon (Fig. 5D–F) with frontal shield prominent, distinctly protruding above vertex; eyes with 20–21 ommatidia." (cacique). Each follows a sentence ending "(Fig. 9C)." / "(Fig. 5C)." and is followed by a sentence beginning "Pereonites 1–7". MATCH. On the d289 question: d289 declined the eye statement taken alone, which is a clause after a semicolon. Here the quote is the whole printed sentence, capital "Cephalon" to the full stop, from one section, with no cut. It meets the quote rule; the value says no more than "four" / "20–21". Natural history (troglobius), verbatim: "This species is considered troglobitic due to the reduction of body pigments and reduction in the number of ommatidia." Habitat verbatim: "in the aphotic zone of the Roca Madre Cave, beneath limestone rocks"; cacique "collected on tree bark around the Luis Pablo Ojeda Cave (Bañaderos cave),".

Other ommatidia sentences in the paper: D. brevispinis (redescribed) "eyes of 16 ommatidia."; the key "Eyes with 20 or more ommatidia" / "Eyes with 16 or fewer ommatidia." None contrary.

**Error (fixable, scientific meaning), both lines: specimen basis and size confound.**
- `eye` "compound eye, holotype male" and `method` "morphological description of the holotype" are not supported. The paper does not say the Description is of the holotype, and figure captions cite paratypes (for example "♀ paratype, CBUDC-CRU 396"). The type series has male and female paratypes for both species (troglobius holotype ♂ plus paratypes 1♂ and 1♂,1♀; cacique holotype ♂ plus 1♂,1♀ and 1♀; counts as returned by the tool). Labelling the value a single male's count narrows its applicability wrongly and invents a sex restriction.
- Line 7's conditions set the cave species against surface D. cacique (20-21) but omit that the comparison is not size-matched: "Maximum body length: male 2.7 mm, female 4.2 mm." (troglobius) against "Maximum body length: male 8 mm, female 9 mm." (cacique). In a comparison of ommatidia number between a cave and a surface species, a threefold body-length difference is a design confound for the authors' attribution to cave life. Line 8 carries the cacique size for the same reason.

Names: both names are from the 2025 original description; ZooBank registers "Diploexochus cacique López-Orozco, Carpio-Díaz & Campos-Filho, 2024" (the ZooBank year is printed 2024; the act's authority line is "in Borja-Arrieta, ... 2025") with no status shown; Plazi treatment titles give "Diploexochus troglobius López-Orozco, Borja-Arrieta & Campos-Filho, 2025". WoRMS is refused under the desk rules, so registry acceptance is unchecked; no synonymy found. Not counted.

Grade m right. Lines 7 and 8: 1 error each, fixable.

## Lines 9 to 12, Mongoloniscus crenatus ([15, 19]), M. polyacanthum (20), M. parvus ([14, 15]), M. orientalis (20), ZooKeys 1202

Bibliographic: Crossref gives Chao Jiang, Jing Zhong, Zhidong Wang, Weichun Li, Luqi Huang in that order; title "Taxonomic study on the genus Mongoloniscus Verhoeff, 1930 (Isopoda, Agnaridae) from China: morphological and phylogenetic analyses" (returned in two pieces split at the colon; matches the record); ZooKeys 1202, pages 229-253, no issue; issued 2024-05-23; CC BY 4.0, vor. The page prints the same authors and "ZooKeys 1202: 229-253", and the CC BY 4.0 licence statement (the tool summarised this pass; Crossref vor CC BY 4.0 on the DOI meets the rule either way). Met.

Quotes, each a whole sentence in its species' Description, between the Cephalon sentence and a sentence beginning "Antenna with fifth article of peduncle": "Eyes with 15–19 ommatidia." (crenatus), "Eyes with 20 ommatidia." (polyacanthum), "Eyes with 14 or 15 ommatidia." (parvus), "Eyes with 20 ommatidia." (orientalis). MATCH for all four; the record's `where` labels the section "Cephalon", which is the adjoining sentence, harmless. Other ommatidia sentences: M. koreanus Remarks "eyes with 20–24 ommatidia," and "In M. maculatus, its eyes have 15 or 16 ommatidia," (fragments, comparative, not contrary).

**Error (fixable, scientific meaning), all four lines: specimen basis.** `method` "morphological description of the holotype male" is not supported: the page does not say the Description is based on the holotype, and each species has male and female paratypes (the tool counted 43 ♂ and 72 ♀ paratypes for M. crenatus, 1 ♂ and 8 ♀ for M. polyacanthum, 7 ♂ and 6 ♀ for M. parvus, 8 ♂ and 15 ♀ for M. orientalis; tool counts, not verbatim). For M. crenatus a 15–19 range across more than a hundred type specimens is most plausibly a between-specimen range; filing it as the holotype male's count misstates what the value covers. The conditions' "does not say whether it is between eyes or between specimens" is right and is kept.

Names: from the 2024 original description, authority Jiang, Li & Huang, 2024 (Plazi treatment titles for M. parvus, M. crenatus, M. orientalis). WoRMS refused; acceptance unchecked; no synonymy found. Not counted.

Grade m right. Lines 9 to 12: 1 error each, fixable.

## Summary

| Line | Taxon | Verdict | Fields | Reason |
|---|---|---|---|---|
| 7 | Diploexochus troglobius | correct (fixable) | eye, method, conditions | Description not stated to be of the holotype; male and female paratypes; cave/surface comparison not size-matched (2.7 mm vs 8 mm males) |
| 8 | Diploexochus cacique | correct (fixable) | eye, method, conditions | same specimen-basis fault; size added for the comparison |
| 9 | Mongoloniscus crenatus | correct (fixable) | method, conditions | "description of the holotype male" unsupported; large mixed-sex type series |
| 10 | Mongoloniscus polyacanthum | correct (fixable) | method, conditions | same |
| 11 | Mongoloniscus parvus | correct (fixable) | method, conditions | same |
| 12 | Mongoloniscus orientalis | correct (fixable) | method, conditions | same |

Errors 6 of 6 records (100%), all fixable, all one kind (specimen basis misstated, with a size confound added on line 7); quotes 0 (all whole sentences, d289's clause objection does not apply to the whole printed sentence); bibliographic 0; licence 0; trait keys 0; duplicates 0; names unchecked in a registry (not counted); none held out. Verdict: merge lines 7 to 12 after the replacements below. Tested: the replacements, applied to a scratch copy, give 12 records and 0 problems under check.py, each old string occurring exactly once in its field.

## Replacement

Strings are decoded text; they contain no double quotes, and the file stores UTF-8 unescaped, so they appear identically in the raw lines.

### Line 7 (Diploexochus troglobius)

- `eye`: "compound eye, holotype male" -> "compound eye"
- `method`: "morphological description of the holotype" -> "species description (the paper does not say whether the Description is based on the holotype or on the whole type series; figure captions cite paratypes)"
- `conditions`: "Holotype male, Roca Madre Cave" -> "Type series of holotype male with male and female paratypes; holotype from Roca Madre Cave"
- `conditions`: "the surface-dwelling D. cacique of the same paper has 20-21." -> "the surface-dwelling D. cacique of the same paper has 20-21 and the redescribed D. brevispinis 16. The comparison is not size-matched: 'Maximum body length: male 2.7 mm, female 4.2 mm.' for D. troglobius against 'Maximum body length: male 8 mm, female 9 mm.' for D. cacique."

### Line 8 (Diploexochus cacique)

- `eye`: "compound eye, holotype male" -> "compound eye"
- `method`: "morphological description of the holotype" -> "species description (the paper does not say whether the Description is based on the holotype or on the whole type series; figure captions cite paratypes)"
- `conditions`: "Holotype male, Cerro Bañaderos, Hatonuevo, La Guajira, Colombia, collected on tree bark in tropical dry forest;" -> "Type series of holotype male with male and female paratypes; holotype from Cerro Bañaderos, Hatonuevo, La Guajira, Colombia; specimens collected on tree bark around the Luis Pablo Ojeda Cave (Bañaderos cave), in tropical dry forest; maximum body length male 8 mm, female 9 mm;"

### Lines 9 to 12 (Mongoloniscus)

On each line:
- `method`: "morphological description of the holotype male" -> "species description (the paper does not say whether the Description is based on the holotype or on the type series)"
- `conditions`: "Holotype male (ID); the range or alternative, where given, is as printed and the sentence does not say whether it is between eyes or between specimens." -> "Holotype male (ID) with male and female paratypes; the Description is not stated to be of the holotype, and the sentence does not say whether a range is between eyes or between specimens."

with ID = 20210417001 (line 9), 20210908003 (line 10), 20200913004 (line 11), 20230403006 (line 12).

## Optional fixes (not counted)

- Lines 7 and 8 `where`: "(sentence read through WebFetch of the article XML)" could read "(sentence read whole on the article page and XML; audit 447)".
- Lines 9 to 12 `where`: "Description, Cephalon" -> "Description (sentence after the Cephalon sentence)".
- Notes on lines 9 to 12 ask the auditor to confirm acceptance; WoRMS could not be opened (desk rules), so the note could say "registry acceptance unchecked (WoRMS refused; Plazi treatments under Jiang, Li & Huang, 2024)".
