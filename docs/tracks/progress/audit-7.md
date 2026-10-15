# Precision audit 7, 15 October 2026

Two parts. (a) A random sample of 20 records from sweep-49 to sweep-57, each opened at its source and checked for value, grade and a verbatim quote, plus four canon-7 records (Futahashi 2015, Emerling 2017) that do not count toward the rate, and a re-search of three genera that sweep-57 searched with a single combined query. (b) Corrections for the known defects of the Codex round (oa-6 and oa-3): the Ficedula flycatcher values, neuron-level recordings filed as `cff_hz`, and taxon strings that are common names or garbled.

Method as in audit 6 (see `audit-6.md`): each source opened with WebFetch, asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces of at most about 125 characters, with split points recorded in `where`; corrected quotes are 40 words or fewer. Verdicts: `confirm`, `requote`, `correct`, `retract`, `unverifiable`. Typographic differences count as `confirm`. Corrections are in `docs/views/recheck/recheck-7.jsonl` in the recheck-5 schema; no evidence file and not `docs/views/audit/ALL.jsonl` was edited.

## Part (a): random sample of sweep-49 to sweep-57

All nine files have records (2 to 12 each, 47 in all). Two were drawn from each file and two more from the remainder (Python `random`, seed 20261015). The four canon-7 extras were drawn with the same generator after the sweep sample: two of the twelve Futahashi rows and two of the six Emerling rows.

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| sweep-49:1 | Gonatodes / fovea | g | correct | the page's sentence carries the markers for refs 22 and 23 (Underwood 1954; Röll 2001) after "temporal fovea", which the quote drops; the note said no citation was shown. Secondary citation, now `partial: true`; quote cut to the unpunctuated opening |
| sweep-49:2 | Gonatodes / pupil_shape | g | confirm | sentence verbatim under Stage 42; the record's `rank` reads "family" for a genus taxon string (the statement is family-level), left for the desk |
| sweep-50:4 | Sirex noctilio / lambda_max_nm | m | confirm | sentence verbatim in the DOAJ abstract |
| sweep-50:6 | Lama and Vicugna / tapetum | g | confirm | verbatim, but in the Figure 3 caption; the fundus section says "characterised by a lack of a tapetum lucidum" |
| sweep-51:1 | Mergus merganser / binocular_deg | m | confirm | Table 1 row verbatim; 28° under Goosander |
| sweep-51:3 | Gehyra mutilata / receptor_classes | g | confirm | sentence verbatim in Results; the authors the record lacked are Pinto, Nielsen and Gamble, filled in by a metadata-only row not counted as an error |
| sweep-52:1 | Ischnura heterosticta / lambda_max_nm | m | confirm | sentence verbatim (three pieces, same split points) |
| sweep-52:2 | Ischnura heterosticta / lambda_max_nm | m | confirm | as sweep-52:1 |
| sweep-53:9 | Lampyris noctiluca / acceptance_deg | m | confirm | verbatim in Discussion, Nocturnal colour vision and detection of bioluminescence |
| sweep-53:7 | Ardeotis kori / binocular_deg | m | confirm | verbatim on the ResearchGate figure page; the page's "Â" is the mis-encoded multiplication sign, as the record says |
| sweep-54:2 | Amphibolurus muricatus / fovea | m | confirm | clause verbatim in the thesis abstract; repository date still blank |
| sweep-54:1 | Amphibolurus muricatus / acuity_cpd | m | confirm | verbatim in 2.3 Image Analysis (the citation is a link in the markup; rendered text matches) |
| sweep-55:2 | Sirex noctilio / lambda_max_nm | m | confirm | verbatim in the repository abstract |
| sweep-55:4 | Sirex noctilio / receptor_classes | m | confirm | verbatim in the repository abstract |
| sweep-56:11 | Paysandisia archon / interommatidial_deg | m | confirm | sentence verbatim in the abstract |
| sweep-56:1 | Taeniopygia guttata / binocular_deg | m | confirm | clause verbatim in the Summary, ends at the semicolon |
| sweep-57:1 | Pygoscelis papua / acuity_cpd | m | confirm | unpunctuated verbatim piece of the 3.1.9 Retina sentence |
| sweep-57:3 | Lacertidae / lambda_max_nm | g | confirm | verbatim in Discussion, Relevance of UV vision in lacertids |
| sweep-50:2 | Charaxes jasius / lambda_max_nm | m | confirm | sentence verbatim in the English abstract; the 620 nm sentence confirmed |
| sweep-56:5 | Rhinocheilus lecontei / pupil_shape | m | confirm | clause verbatim; Brennan, 2023 confirmed |
| canon-7:4 (extra) | Anax parthenope / opsin_gene_count | m | confirm | verbatim, Diversity and Evolutionary Dynamics of Opsin Genes in the Odonata |
| canon-7:12 (extra) | Ladona fulva / opsin_gene_count | m | confirm | verbatim but for an en dash in "BR001237–BR001256" |
| canon-7:38 (extra) | Chelonia mydas / opsin_genes_intact | g | confirm | verbatim fragment, Turtle Visual Opsins |
| canon-7:40 (extra) | Aves / opsin_genes_intact | g | confirm | verbatim fragment, Gene Inactivation and the Loss of the Parietal ("Third") Eye |

**Part (a) rate: 1 error in 20 verifiable records, 5%** (0 unverifiable). The canon extras: 4 of 4 confirmed. The rate is not above 5%, so no batch recheck was started. The one error is a new shape: a quote that silently drops in-sentence citation markers, which hid that the claim is secondary.

### Re-search of three sweep-57 genera

Three of the 31 genera that sweep-57 searched with one combined query were drawn (seed 20261015) and searched again with two separate queries each.

| genus | queries | result |
|---|---|---|
| Pastor | `"Sturnus roseus" OR "Pastor roseus" retina OR "visual pigment" OR "oil droplets" OR "visual field"`; `rose-coloured starling eye visual acuity OR cone OR ultraviolet sensitivity study` | nothing for the genus holds; both queries return European starling work only (Hart et al. 1998 and others), and Sturnus vulgaris is already in the evidence under several units |
| Sparganothis | `"Sparganothis pilleriana" compound eye OR spectral sensitivity OR electroretinogram OR phototaxis`; `Sparganothis sulfureana OR "Sparganothis fruitworm" light trap wavelength OR vision OR eye` (and a family query on Tortricidae ERG) | nothing for the genus holds; the family query finds spectral work on Adoxophyes orana and Cydia pomonella, which is already in the evidence and gives none of the four searched traits |
| Agelasticus | `"Agelasticus" OR "Agelaius thilius" eye OR vision OR retina OR "visual field"`; `Agelaius phoeniceus red-winged blackbird visual field OR visual acuity OR cone photoreceptor OR "spectral sensitivity"` | nothing for the genus holds, but the log's "no measured relative" is wrong: the yellow-winged blackbird was until recently Agelaius thilius, and the red-winged blackbird has a measured visual field, acuity and cone set ("Vision in an abundant North American bird: the Red-winged Blackbird", The Auk 136(3): ukz039, 2019; a USDA copy at digitalcommons.unl.edu/icwdm_usdanwrc/2280). Agelaius phoeniceus is already in oa-2 and oa-3 |

Found note: no openable measurement for Pastor, Sparganothis or Agelasticus themselves. For Agelasticus, a measured former congener exists (Agelaius phoeniceus, above), so the sweep's `chased` field should read that a relative exists. The single-query sweeps look right on the genus-level answer and weak on the relative-chasing step.

## Part (b): Codex round (oa-6, oa-3)

### Ficedula flycatchers

Boström et al. 2016 (PLoS ONE 11(3): e0151099), opened at journals.plos.org, Results and Discussion: "The average CFFs of these species, 130.3 ± 0.94 Hz (±SD) in three blue tits, 128.1 ± 9.8 Hz in seven collared flycatchers and 138.2 ± 6.5 Hz in eight pied flycatchers, are clearly higher than those of humans ...". The Figure 2 legend gives a maximum of 141 Hz for collared and 146 Hz for pied flycatchers.

The primary paper therefore gives **collared flycatcher (F. albicollis) 128.1 and pied flycatcher (F. hypoleuca) 138.2**, the reverse of the assignment stated in the task brief. Potier et al. 2020 Table 3 (oa-3:31, oa-3:33) has it right. The Lafitte et al. 2022 S10 supplement swaps the means and their SDs (albicollis 138.2 ± 6.5, hypoleuca 128.1 ± 9.8) while keeping the maxima right. Four records copied the supplement's swap and are corrected to the primary values with the primary paper as source: oa-6:23, oa-6:24, oa-3:75, oa-3:76. The maxima records (oa-6:243, 244; oa-3:271, 272) are correct in value; their notes repeat the supplement's swapped SDs, a note-only defect left for the desk.

### Neuron-level recordings filed as cff_hz

Found by grepping `cff_hz` records whose value, quote, method or note speaks of neurons, cells, units or tuning, then reading the review's comment cell and the primary study's title. Retracted, since a single cell's temporal resolution or tuning is not the animal's flicker fusion frequency (and several carry a wrong method, "ERG" or "EEG"):

- Macaca mulatta, LGN parvocellular and magnocellular cells (Spear et al. 1994): oa-6:222, oa-6:321, oa-3:250, oa-3:353
- Macaca mulatta, MT neuron temporal-frequency tuning, young and aged (Yuan et al. 2014): oa-6:239, oa-6:329, oa-3:267, oa-3:360
- Felis catus, retinal horizontal cells and "wide bandwidth units" (Lankheet et al. 1991): oa-6:160, oa-6:280, oa-3:191
- Eristalis, cSIFE neurons (de Haan et al. 2013): oa-6:76, oa-3:115
- Rhinella marina, one horizontal cell (Nowak and Green 1983): oa-6:306, oa-3:340 (the rod and ERG values from that study stand)

Seven of these were grade `m` in oa-6 (76 was already `g`); the oa-3 copies were `g`.

Flagged, not acted on: Felis catus "Physiological" records from Vantoi and Riva 1995 (oa-6:230, 326, 327, 328; oa-3:258, 357, 358, 359) measure optic-nerve-head blood flow driven by flicker, which is also not a perceptual CFF; and Macaca radiata (oa-6:220, oa-3:248) is a steady-state evoked potential in LFP and EEG (Salelkar and Ray 2020). Both deserve a desk decision.

### Taxon strings

Found by testing every taxon in oa-6 and oa-3 for a Latin genus or binomial form, then reading the distinct strings by eye (oa-3 has none). Sixteen distinct strings in oa-6, 41 records:

| string | records | action |
|---|---|---|
| bald eagle | oa-6:6 | correct to Haliaeetus leucocephalus |
| Euploea coreCramer, | oa-6:44 | correct to Euploea core |
| Diurnal birds | oa-6:605 to 614 | correct to Aves (class), conditions "diurnal birds" |
| Chicken and Japanese quail | oa-6:620 to 625 | correct to Gallus gallus; note names the quail, which has its own rows |
| human | oa-6:651 to 654 | correct to Homo sapiens |
| goldfish | oa-6:655 to 658 | correct to Carassius auratus |
| mouse | oa-6:659 | correct to Mus musculus (rank species, grade held at g) |
| Animals exposed to variable / high / low light levels | oa-6:337 to 339 | retract: exposure categories across all species |
| Type 1 birds | oa-6:537, 538 | retract: a visual-field type that cuts across orders; the Table 1 species rows carry the values |
| Mallard and Eurasian Woodcock | oa-6:539 | retract: redundant with oa-6:512 and 517 |
| Zebra finch, Canary, Starling and Budgerigar | oa-6:631 | retract: rounded group value; species rows exist |
| Humboldt Penguin, Manx Shearwater and Pigeon | oa-6:632 | retract: rounded group value; species rows exist |
| Raptors; Hawks and falcons | oa-6:1 to 5, 7 | retract: no taxon short of Telluraves covers falcons, hawks and eagles; re-log per species from Tucker 2000's Methods |

## Rows written

`recheck-7.jsonl`: 62 rows, 33 `correct` and 29 `retract`. Part (a): 2 rows (sweep-49:1, a counted error; sweep-51:3, metadata only). Part (b): 4 flycatcher corrections, 15 neuron retractions, 27 taxon corrections and 14 taxon retractions.

## Error rate

Part (a): **1 of 20, 5%** (0 unverifiable); canon extras 4 of 4 confirmed.

## Patterns (this run)

1. The newest sweeps hold at audit 6's 5%. The residual error has moved from the clause cut to a quieter omission: citation markers removed from inside a quoted sentence, which hides a secondary claim.
2. The Codex round's defects come from trusting a review supplement row by row. The flycatcher swap is the supplement's own error, and the neuron rows are rows the review itself filed under CFF; a primary-source spot check would have caught both.
3. The single-query sweeps answer the genus question correctly in all three re-searched cases but under-chase relatives (Agelasticus).
