# audit-339: desk-d244, evidence lines 1 to 3

Audited 31 October 2026 from the desk-d244 files present untracked in the worktree (docs/tracks/progress/desk-d244.md and docs/views/evidence/desk-d244.jsonl, 3 lines; neither committed here, neither edited). HEAD and origin/main 82bfd1ad (desk-d243). `python3 -I tools/senses/check.py | grep 'd244\.'`: "docs/views/evidence/desk-d244.jsonl: 3 records, 0 problems". Quote lengths (`len(q.split())`): 12, 10 and 20 words, all within 40; the only non-ASCII character in the quotes is "±" (line 2). Evidence records only; audits 337 and 338 are the format model, and the desk-audit.md evidence clause applies (40-word limit, no 125-character limit). Quotes returned in abutting pieces are judged under the six conditions in audit-324.md; cuts under audit-331.md.

Sources opened (WebFetch): api.crossref.org/v1/works/10.3390/ani12070801 and /10.3389/fvets.2024.1417278 (one pass each); www.mdpi.com/2076-2615/12/7/801 (five passes); www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2024.1417278/full (three passes); www.mammaldiversity.org/taxon/1005937 (returned by WebSearch); api.obis.org/v3/taxon/Siganus%20luridus. WoRMS and GBIF not opened (refused per rules). No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 1 WebSearch and 11 WebFetch calls used.

## Bibliographic and licence

- Lines 1 and 2. Crossref: Wojciech Paszta, Karolina Goździewska-Harłajczuk, Joanna Klećkowska-Nawrot (3, the record's order and the page byline); title "Morphology and Histology of the Orbital Region and Eye of the Asiatic Black Bear (Ursus thibetanus)—Similarities and Differences within the Caniformia Suborder" (as the record); Animals volume 12, issue 7, article 801; issued and published online 2022-03-22; journal-article; relation empty, no update-to. Page citation Animals 2022, 12(7), 801 (tool summary). DOI verified. Licence: page metadata links CC BY 3.0, no licence sentence returned (tool summary); Crossref CC BY 4.0, content-version vor, start 2022-03-22, delay 0. Accepted pairing (CC BY 3.0 page vs CC BY 4.0 Crossref). Faults 0. The desk note says Crossref spells the second author "Gożdziewska"; this audit's Crossref pass returned "Goździewska" (the tool may normalise diacritics; uncounted, see Unchecked).
- Line 3. Crossref: Amira Derbalah, Samir A. A. El-Gendy, Hanan H. Abd-Elhafeez, Soha Soliman, Ahmed A. El-Mansi, Manal Seif, Ahmed M. Rashwan, Mamdouh B. Eldesoqui, Catrin Sian Rutland, Valentina Kubale, Mohamed A. M. Alsafy (11, the record's order; the page byline returned the same 11 names in two pieces, with a "+2 more" display control); title "Light and scanning electron microscopy of the eye of Siganus luridus (Rüppell, 1828)", identical; Frontiers in Veterinary Science volume 11, article 1417278, no issue; issued 2024-09-20; journal-article; relation empty, no update-to. Page: "Front. Vet. Sci., 20 September 2024", "Volume 11 - 2024". Licence: no licence sentence returned from the page; Crossref CC BY 4.0, vor, start 2024-09-20. Accepted ("publisher page with no licence sentence + Crossref CC licence for vor"). Faults 0.

source.access "open" right for all three. Bibliographic faults 0; licence faults 0.

## Names

- Ursus thibetanus (lines 1, 2). Mammal Diversity Database: "Ursus thibetanus", "G. Cuvier, 1823", Asian Black Bear, Ursidae, Carnivora, living, wild; Selenarctos thibetanus Pocock, 1932 listed as a synonym (Selenarctos as subgenus). The paper calls it Asiatic black bear throughout. Main has no Selenarctos row; main's Ursus rows (canon-3 genus row, mammal-groups U. americanus, oa-1 U. maritimus) carry Ursidae, Carnivora. Not in gbif-names.tsv. Met. Origin: "The research material was taken from one male of Asiatic black bear [53] (aged 27 years, 4 months, and 10 days)" "coming from Wroclaw Zoological Garden (Poland) (2018)". The paper says nothing read here about the bear's earlier history (bile farm, rescue or zoo-born); a tool summary in one pass asserted it was neither, but no sentence was returned to support that, so the record's "captive ... from Wroclaw Zoological Garden" is the most that can be said, and it says no more. Met.
- Siganus luridus (line 3). OBIS: "Siganus luridus", "(Rüppell, 1829)", "accepted", Siganidae, order "Acanthuriformes", class Teleostei, taxonID 127044. The paper's title gives the authority year as 1828. Main files every Siganidae row under Perciformes (desk-d193 S. guttatus, intake-5 S. doliatus, try-species.json S. luridus and S. doliatus); the record follows main. Name met; the order is main's convention, against OBIS's current Acanthuriformes (uncounted; an owner question, since one main convention covers all Siganus rows). Lessepsian status not stated in the text read; the abstract says only that it "lives" "in the Mediterranean Sea".

Name faults 0.

## Duplicates

git grep on origin/main (82bfd1ad) across the whole docs/ tree (evidence, audit incl. audit/corrected and audit/ALL, sheets, searched, sources, wanted, gaps, batches, codex-findings, progress) for "thibetanus", "Selenarctos", "black bear", "Ursus", "ani12070801", "12070801", "Paszta", "Siganus", "luridus", "Siganidae", "rabbitfish", "spinefoot", "1417278", "fvets.2024".

- Bear: "thibetanus" hits only Helleborus thibetanus (a plant); "black bear" only American Black Bear naming lists; Ursus rows are U. americanus (receptor_classes, fovea), U. maritimus (orbit_convergence_deg), and genus rows (canon-3 receptor_classes; oa-2 lambda_max_nm categories). "Paszta" hits only the Lycaon pictus paper (mammals-met, sweep-63, recheck-26) and the dog compile. DOI absent.
- Rabbitfish: Siganus guttatus (desk-d193, sense_hearing) and S. doliatus (intake-5, filter_pigments) only; S. luridus only in try-species.json. DOI absent.

Not repeats. Line 2 does not repeat line 1 (axial length against tapetum, two traits). Duplicate faults 0.

## Trait keys and value form

- `tapetum` is in check.py's TRAITS (the launch prompt's statement that the list lacks it is wrong for this key; only `eye_axial_length_mm` is absent). Main holds descriptive strings under it (Lycaon "cellular tapetum lucidum, semicircular, milky, 14-17 cell layers"; desk-d243 Orycteropus). The record's note carries no "new trait" and needs none.
- Diseased-eye finding under `tapetum` (launch question). Main's closest precedent is mammal-groups:167, Choloepus didactylus (Klećkowska-Nawrot et al. 2023, same research group), whose "degenerative choroidal tapetum lucidum cellulosum was found microscopically" is filed under `eye_type` with a round pupil. That row bundles two findings in one value; `tapetum` is the specific key and the right one for a tapetum finding, and the precedent does not argue for moving the bear row. The finding is partly anatomy and partly possible pathology: a choroidal tapetum lucidum cellulosum is present (macroscopically a faint dark-brown crescent; histologically 2-3 layers of cells), and its cells show degenerative features whose cause the authors cannot fix (age, inflammation spreading from the jaw lesion for which the bear was euthanised, or a family trait). That belongs under `tapetum` provided the record says the degeneration may be individual (see line 1 error). Holding out is not required.
- `eye_axial_length_mm`: 286 rows on main evidence (oa-1 275, oa-6 6, oa-7 3, desk-d243 1, recheck-codex-b-fixed 1), all mm. The note's "New trait for this species: eye_axial_length_mm is a key already on main (absent from the checker list)" passes check.py and is accurate.
- Grade `m` right for all three: one named species each, measured by the authors.

## Quote ruling

- Line 1. Abstract, returned whole: "Degenerative choroidal tapetum lucidum similar to ranch mink (Mustelidae) has been found." Sentence before: "There were palisades of Vogt in the corneal limbus epithelium similar to the Canidae."; after: "The pupil was big and round in shape." Both ends verified. MATCH, 12 words.
- Line 2. Results 3.1, returned whole: "The axial eye diameter was 16.7 ± 0.4 mm, approximately." Next: "The maximum transverse eye diameter was 17.127 ± 0.09 mm, and the minimum transverse eye diameter was 18.143 ± 0.08 mm, approximately." (the contradiction the record states is confirmed verbatim). "±" checked against the page. MATCH, 10 words.
- Line 3. Abstract sentence 9 of 10, returned in two abutting pieces in each of three passes, split at "herbivore" / "and herbivores" on two passes and at "typically" / "lack" on the third, the joined text identical: "The tapetum lucidum was observed, which is interesting since Siganus luridus is herbivore and herbivores typically lack a tapetum lucidum." Sentence before (sentence 8) ends "in the choroidal gland.", as the note says; sentence after begins "These observations shed new light". Audit-324 conditions 1 to 6 met (condition 4: the note says "read in two abutting pieces", not the exact "verbatim in two pieces"; accepted as in audits 337 and 338). MATCH, 20 words.

Quote faults 0. HOLD OUT: none; every quote's ends are verified verbatim on the page.

## Per-record findings

### Line 1, Ursus thibetanus, tapetum: degenerative choroidal tapetum lucidum

Design confirmed: one male, "aged 27 years, 4 months, and 10 days", Wroclaw Zoological Garden (2018); "The test samples were obtained post-mortem after the animal was euthanized at the Wroclaw Zoological Garden" "due to unhealed wounds associated with a non-wolf defect in the maxillary alveolar arch."; eyeballs "(n = 2)". Results verbatim: "Macroscopic examinations revealed the presence of a very faintly marked tapetum lucidum which resembled a crescent moon" "with a dark brown color, being slightly opalescent."; "The length of tapetum lucidum was 8.063 ± 0.05 mm"; "the choroidal tapetum lucidum cellulosum, which is composed of loosely packed degenerative cells with a diameter" "between 18.81 ± 10.4 µm and 40.007 ± 9.1 µm arranged in 2–3 layers". The record carries these.

**Error (authors' uncertainty about the cause of the value's key qualifier omitted).** Discussion, verbatim in four abutting pieces: "In the case of our test bear, we suppose that the cause of the degenerative changes in the wallpaper cells may be related" "to the age of the individual, but these changes may also have resulted from an inflammatory process" "within the maxillary sagittal arch, but perhaps it is a feature of the Ursidae family; therefore, precise determination of" "it requires further research in the Ursidae." The value's "degenerative" is the authors' observation in one aged animal whose euthanasia followed a jaw lesion they name as a possible cause; a reader of the record takes "degenerative" as the species' tapetum type. The record gives the age and the jaw wound but never links them to the degeneration, and does not say the authors leave open whether it is individual pathology or an ursid trait. Also verbatim: in the ranch mink "degeneration features of wallpaper cells" are reported and "Ollivier et al., 2004 [111], report that the cause of this wallpaper degeneration is unknown" "but could be related to dietary insufficiencies in specific animals, or perhaps the genetics of inbreeding." So the mink comparison in the quote is to a degeneration of unknown cause. Fixable. Uncounted: the brown bear's tapetum is reported (Kirbas Dogan et al. 2020) as "yellow-green color and" "triangular shape", a congeneric contrast; "non-healing jaw wound" is a fair paraphrase of "unhealed wounds associated with a non-wolf defect in the maxillary alveolar arch"; name source can cite MDD.

### Line 2, Ursus thibetanus, eye_axial_length_mm 16.7

Methods verbatim: "Immediately after the death of the animal, the eyeballs with selected additional organs of the eye were subjected" "to preparation, morphometry, and then the collected samples were placed in 4% buffered formaldehyde for at least 72 h" "and then rinsed in running water for 24 h." So morphometry preceded fixation, as recorded; no shrinkage question arises. Caliper: "using a digital caliper (Stainless Hardened, Farnell, Poland)"; six random measurements per structure, mean and SD (tool summary). "Axial eye diameter" is the anteroposterior dimension and is what main's `eye_axial_length_mm` holds; 16.7 is the printed mean, a measured value. The transverse contradiction (minimum 18.143 above maximum 17.127) is stated in conditions with the right inference (the printed morphometry may contain an error). The paper lists "eyeballs (n = 2)" and does not say whether the six measurements were on one eye or both; the conditions say n = 2 is listed, but the note's "six caliper repeats on one animal's eyeball" reads as one eye (uncounted wording fix below). **MATCH.**

### Line 3, Siganus luridus, tapetum present

Design verbatim: "Ten mature, healthy Siganus luridus fish were collected from the Mediterranean Sea (Damietta Governorate)."; "The freshly collected eyes were used to examine the structures under a light microscope."; "The eye samples were fixed in 10% neutral buffered formalin solution." No sentence on capture method, market purchase, sex, killing method or time to examination (tool summary of a full-text check); ethics approval ALEXU-IACUC 02/13/2022/11/13/175 under Directive 2010/63/EU. Identification verbatim, Results 3.1: "The eyes from the Siganus luridus showed a uniform appearance when a flashing light was not shone on it," "however it appeared shiny (eye-shine) when a flashing light was applied" "indicating the presence of the tapetum lucidum (luminous layer), a reflective cell layer behind the retina."; 3.4: "The choroid was divided into four layers: the suprachoroidal layer, the tapetal layer," and "The tapetum lucidum layer consisted of dense choroidal tissue infiltrated with numerous melanocytes and blood vessels". No sentence describes reflective cells, guanine crystals or iridocytes seen in histology or SEM (tool summary); the identification rests on eye-shine and the layer label. Discussion verbatim: "This layer was also observed in the choroid of Siganus javus." and "Fish living in shallow waters generally have less developed tapetum lucidum compared to their deep-water counterparts." The record's method gives both bases and its conditions say presence only, with the n, length and unstated provenance right. **MATCH.** Uncounted: say that no reflective cell type is described histologically; the congener S. javus report sits against the authors' "herbivores typically lack" framing; the note's name source can now cite OBIS.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Ursus thibetanus, degenerative choroidal tapetum lucidum | error, fixable | conditions | authors' open cause of the degeneration (age, inflammation from the jaw lesion, or an Ursidae trait) omitted; mink comparison is to a degeneration of unknown cause |
| 2 | Ursus thibetanus, axial eye diameter 16.7 mm | MATCH | note (uncounted) | measured before fixation, contradiction stated; one-eye-or-both not stated by the paper |
| 3 | Siganus luridus, tapetum lucidum present | MATCH | method, note (uncounted) | quote whole in reproduced abutting pieces; eye-shine plus layer label, no reflective cells described; name accepted (OBIS) |

Errors 1 of 3 records (33%), above the 5% bar: scientific-context 1; quote form 0; bibliographic 0; licence 0; names 0; duplicates 0; trait key 0; grading 0. HOLD OUT: none.

Answers to the launch questions: (1) Ursus thibetanus is the accepted name (MDD), captive zoo animal of unstated prior origin; one 27-year-old male, n = 2 eyes; "degenerative" is the authors' histological description of 2-3 layers of tapetal cells, whose cause they leave open between age, inflammation and a family trait; it belongs under `tapetum` (main's only similar finding, the sloth, sits under `eye_type` bundled with pupil shape, which is not a reason to move it) once the record carries that uncertainty. (2) "Axial eye diameter" is the axial length; 16.7 is a measured mean taken before fixation; whether one or both eyes is not stated; the transverse contradiction is adequately stated. (3) Siganus luridus is accepted (OBIS, Siganidae); wild status is "collected from the Mediterranean Sea" only; n = 10; tapetum identified by eye-shine and named in histology without reflective cells described. (4) `tapetum` is in check.py's TRAITS; only `eye_axial_length_mm` is absent.

Owner question: OBIS places Siganidae in Acanthuriformes; main files all Siganidae under Perciformes. A main-wide decision, not a desk fault.

Pooled rate: not computed; no pooled evidence figure has been carried since audit 324 (402 of 810), and audits 325 to 338 are not tallied here.

## Unchecked

- Line 1: the Discussion's sentence beginning "Another factor could be improper light expos" was truncated in the tool's text on two passes; whether it bears on the tapetum is unknown. The bear's history before Wrocław Zoo (bile farm, rescue, zoo-born) not stated in text read. Crossref's exact spelling of the second author ("Gożdziewska" per desk, "Goździewska" per this audit's pass) not settled.
- Line 2: whether the six measurements were on one or both eyes (not stated); the page's licence (CC BY 3.0) is from metadata via tool summary.
- Line 3: Figure 1 and Figure 8 images not viewed; whether the fish were wild-caught or market-bought, and the Lessepsian origin of the population (not stated in text read).
- Pooled rate across audits 325 to 339.

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 1, counted:
- `conditions`: "those sentences are not quoted." -> "those sentences are not quoted. The authors do not settle the cause of the degeneration: they suppose it may be related to the bear's age, but say it may also have resulted from an inflammatory process within the maxillary arch (the lesion for which the bear was euthanised), or perhaps be a feature of the Ursidae, and that further research in the Ursidae is needed; so the degenerative state may belong to this aged individual rather than to the species. The ranch mink comparison is to a wallpaper-cell degeneration whose cause Ollivier et al. (2004) report as unknown (possibly dietary or inbreeding). In the brown bear the tapetum is reported (Kirbas Dogan et al. 2020) as yellow-green and triangular."

Line 1, uncounted:
- `note`: "WoRMS/OBIS not applicable." -> "WoRMS/OBIS not applicable; Mammal Diversity Database (audit 339): Ursus thibetanus G. Cuvier, 1823, Ursidae, Carnivora, with Selenarctos thibetanus a synonym (none on main)."

Line 2, uncounted:
- `note`: "on one animal's eyeball" -> "on one animal (the paper lists two eyeballs and does not say whether the six measurements were taken on one eye or both)"
- `note`: "WoRMS/OBIS not applicable." -> "WoRMS/OBIS not applicable; Mammal Diversity Database (audit 339): Ursus thibetanus G. Cuvier, 1823, Ursidae, Carnivora."

Line 3, uncounted:
- `conditions`: "The authors note it is unexpected because herbivores typically lack a tapetum." -> "The authors note it is unexpected because herbivores typically lack a tapetum, though they also cite the same layer in the congener Siganus javus. No reflective cell type (guanine crystals, iridocytes) is described in the histology or SEM; the identification rests on the eye-shine and on the authors' naming of a choroidal layer as tapetal."
- `note`: "(OBIS/WoRMS page could not be opened)" -> "(OBIS, audit 339: Siganus luridus (Rüppell, 1829), accepted, Siganidae, order Acanthuriformes, taxonID 127044; the order is filed as Perciformes to match main's other Siganidae rows)"

Verdict: 1 of 3 audited records in error (33%), above the 5% bar; fixable with the text above; none held out. Bibliography, licence (CC BY 4.0 vor on both papers), names, duplicates, trait keys and all three quotes pass.
