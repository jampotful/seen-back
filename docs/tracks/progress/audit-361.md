# audit-361: desk-d269, evidence lines 1 to 4

Audited 1 November 2026 from the desk-d269 files present untracked in the worktree (docs/tracks/progress/desk-d269.md and docs/views/evidence/desk-d269.jsonl, 4 lines; neither committed here, neither edited; the untracked jsonl is byte-identical to origin/research/desk-d269). Worktree HEAD and origin/main 6d94bb12 (merge of d267 after audit 360). `python3 -I tools/senses/check.py | grep 'd269\.'`: "docs/views/evidence/desk-d269.jsonl: 4 records, 0 problems". Quote lengths (`len(q.split())`): 10, 10, 10, 10. Non-ASCII in quotes: "±" (U+00B1) and "°" (U+00B0) in each, as printed. Format model audit-358.md; desk-audit.md evidence clause (40-word limit, no 125-character limit); abutting pieces under the six conditions of audit-324.md (not needed: every quote came back whole in one piece); cuts under audit-331.md (none).

Sources opened (WebFetch): www.mdpi.com/2075-1729/12/5/741 (four passes); api.crossref.org/works/10.3390/life12050741 (answered, not robots_disallowed); insecta.pro/taxonomy/1017724 (Pterostichus melas) and /814098 (genus Clinidium); baza.biomap.pl Clinidium canaliculatum page; en.wikipedia.org Clinidium canaliculatum (secondary, used only as a cross-check); aegaweb.com Toribio et al. 2020 PDF on Pterostichus melas; zin.ru Pterostichus page (no melas entry). biolib.cz returned a security check page and was not retried. PMC, the PMC PDF mirror, iris.unical.it, DOAJ, ouci.dntb.gov.ua, the brum.beds.ac.uk proxy copy, GBIF and reviewer.ly in the search results were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 5 WebSearches.

## Bibliographic and licence

Crossref: Anita Giglio, Maria Luigia Vommaro, Raffaele Giuseppe Agostino, Lai Ka Lo, Sandro Donato, in that order (the record's "Giglio A, Vommaro ML, Agostino RG, Lo LK, Donato S" is right); container Life, volume 12, issue 5, article 741; published online and issued 2022-05-17; publisher MDPI AG; licence https://creativecommons.org/licenses/by/4.0/, content-version vor, start 2022-05-17, delay 0; relation empty; no update-to (the update-policy field is the Crossmark policy URL). Title begins "Exploring Compound Eyes in Adults of Four Coleopteran Species" (rest tool summary).

Page: author line as above; title "Exploring Compound Eyes in Adults of Four Coleopteran Species Using Synchrotron X-ray Phase-Contrast Microtomography" "(SR-PhC Micro-CT)", identical to the record; citation "Life 2022, 12(5), 741", so year 2022 and "Life 12(5): 741" are as printed. Licence: no licence sentence in the page body; page metadata (dc.rights) "https://creativecommons.org/licenses/by/3.0/". The licence rule accepts a publisher page with no licence sentence plus Crossref CC licence for the vor, and accepts CC BY 3.0 page against CC BY 4.0 Crossref (audit 344 applied the same pairing to another MDPI paper). No NC or ND tag anywhere. Accepted; source.access "open" right.

Bibliographic faults 0; licence faults 0. desk-d165 held this paper only under the older licence reading ("same hold as desk-d163 applied to a metadata-only link"); audit-250 audited d165's five filed records and does not mention this paper, so no audit ruled on it. The 31 October licence rule now admits it.

## Names

Main's docs/views/gaps/gbif-names.tsv: "Tenebrio molitor EXACT ACCEPTED" (usage key 1045843) and "Tribolium castaneum EXACT ACCEPTED" (4990338). No Pterostichus or Clinidium row.

- Pterostichus melas. insecta.pro: "Pterostichus (Feronidius) melas (Creutzer, 1799)", Carabidae, Pterostichinae, Pterostichini (tool summary of the path); the page lists no subspecies. Toribio et al. 2020 (aegaweb PDF), verbatim: "Pterostichus (Feronidius) melas (Creutzer, 1799)" and "P. (F.) melas italicus (Dejean, 1828), que se conoce del sur de Francia, norte de Italia, Serbia y Croacia". So italicus is a recognised subspecies and the species name is accepted; filing at species rank with the subspecies in note and conditions follows the species-rank rule. Met. Side note (uncounted): Toribio et al. give no southern Italian range for italicus, while the sample is from Calabria; the paper's subspecies determination is the authors', and nothing here contradicts it.
- Clinidium canaliculatum. Paper Abstract, verbatim: "namely the saproxylic Clinidium canaliculatum (Costa, 1839) (Rhysodidae),". baza.biomap.pl: "Clinidium canaliculatum (Costa, 1839)", "name status: valid name", family Rhysodidae (tool summary). insecta.pro genus page: "genus Clinidium Kirby, 1835", Coleoptera, Carabidae, Rhysodinae, Rhysodini, Clinidiina (tool summary). Wikipedia: "Clinidium canaliculatum is a species of ground beetle in the subfamily Rhysodinae." So the species name is accepted; the family differs by classification, not by error. The record's Rhysodidae is as printed and defensible. I recommend Carabidae for the family field (the GBIF-backed names table places the genus there, per the desk-d165 note, which I could not open GBIF to confirm), with Rhysodidae as printed in the note. Uncounted; the owner may prefer the printed family.
- Tenebrio molitor, Tribolium castaneum: Tenebrionidae as printed ("Tenebrio molitor (Linnaeus, 1758) and Tribolium castaneum (Herbest, 1797) (Tenebrionidae),", verbatim; "Herbest" is the paper's spelling). Coleoptera for all four. Met.

Lab stocks. Methods: "Tenebrio molitor specimens were obtained from a laboratory stock population" at the University of Calabria (rest tool summary; no origin for the stock is given); "Specimens of T. castaneum, belonging to the strain Croatia 1 (CRO1), were collected" from a wild population in Croatia and reared in the laboratory (rest tool summary). Lab stock is allowed at species rank (audit 332). Line 3's note does not say the stock's origin is unstated; line 4's says only "wild-collected stock". Fixes below, uncounted.

Name faults 0.

## Duplicates

git grep on origin/main (6d94bb12) across the whole docs/ tree (docs/views/audit/corrected, audit/ALL.jsonl, sheets, searched/, progress notes) for life12050741, Giglio, Clinidium and "Pterostichus melas": no evidence row. Hits are progress notes only: desk-d165 line 10 (the hold), desk-d245 line 14 (Pterostichus melas italicus ommatidia count held: "does not name the species or the specimen"), desk-d265 line 19 (paper skipped, "ommatidia counts only"). Tenebrio molitor interommatidial_deg on main: 6.5 from Land 1997 (corrected/insect.jsonl 251, corrected/methods.jsonl 69, both audit verdict "unverifiable", review-sourced) and Df 6.5 inside the canon-4 acuity_cpd row (Feller et al. 2021 compilation). These are a different source and value, not repeats of this DOI; a measured 6.89 from a primary paper adds to them. Tribolium castaneum: opsin rows only on main. All 152 remote branches matching origin/research/desk-d2* or origin/research/audit-3*: branch-only files mentioning these names or the DOI are desk-d245.md, desk-d265.md and desk-d269 itself; the Tenebrio interommatidial hits on audit-33 to audit-37 are the same Land 1997 rows.

Duplicates 0.

## Trait key and units

interommatidial_deg is in tools/senses/check.py TRAITS (line 13) and on main; main's units for it are "degrees" in 289 + 24 records (3 "deg", 1 "degree", 1 an unrelated density). The records' "degrees" match. Faults 0.

## What the number is

Methods 2.5, verbatim: "Morphometric measurements on 2D virtual slices were assessed with the open-source software ImageJ [66]" "on digitised images and processed as mean ± standard deviation."; "The ommatidial axis was taken as a line through the midpoint of the rhabdom and the corneal lens," "and the interommatidial angle was measured from line drawings by two continuous ommatidia on 2D virtual sections." So each value is a mean ± SD over N measured pairs of neighbouring ommatidia on virtual sections; N is never defined (verified: no sentence defines it), no eye side, eye region or section plane is given, and no statistical test or sex comparison is reported for any eye measure (tool summary of a search for one). Specimens, verbatim: "one male and one female for C. canaliculatum and P. m. italicus, and 2 males and 2 females for T. molitor and T. castaneum."; fixation "fixed in 2.5% glutaraldehyde and 1% paraformaldehyde in 0.1 M phosphate buffer", then graded ethanol (tool summary). The Results have no subsections; "3. Results" is one section. The records' method, conditions, N, SD, sexes and "the paper does not define N" are right. The angle is anatomical (axes of fixed tissue), not optical or behavioural, which the method field says.

Eye types, verbatim: "Comparing the 2D virtual sections of the compound eyes, two different structures can be distinguished."; Discussion: "the superposition eyes of P. melas and the apposition structure of both T. molitor and T. castaneum." C. canaliculatum is assigned to neither type. Tenebrionids: "They exhibit a characteristic bilobed shape, due to a protrusion of the strongly expanded gena in the anterior eye field." C. canaliculatum: "The cornea is smooth and the external facets of the corneal lens marking the position of the ommatidia are indistinguishable in both males and females." and a cluster of 70 ommatidia (tool summary with the verbatim phrase "the virtual cuticle removal from the head shows a cluster of 70 ommatidia"). None of these is a contrary or significant result; they are context the records could carry (uncounted).

## Per-record findings

All four quotes, each verbatim in one piece from one pass and confirmed character by character on a second ("°" directly after the SD digit, then one space before "(N"): "The interommatidial angle was 4.09 ± 0.66° (N = 13)."; "The interommatidial angle was 7.36 ± 1.25° (N = 8)."; "The interommatidial angle was 6.89 ± 1.02° (N = 14)."; "The interommatidial angle was 12.99 ± 1.2° (N = 9)." Each is a whole sentence, 10 words, from Results, contains the value and the value says no more. **Quote MATCH** on all four.

The common fault: none of the four sentences names its species, and every record gives the same `where`, "Results (interommatidial angle sentence)", in a Results section with no subsections and four identical sentence frames. The desk's own earlier holds of this paper turned on exactly this (desk-d165: "the angle sentences do not name the species"; desk-d245: "does not name the species or the specimen"). Audit 268 accepted unnamed-species sentences because `where` named the species subheading and the note said the sentence names no species; audit 299 accepted one because the paragraph's opening fixed the species. Here neither is in the record. I traced each sentence's neighbours (verbatim):
- Line 1: preceded by the P. melas italicus axon sentence (tool summary: axons connect to the optic lobe and cerebrum); the next paragraph opens "The volume renderings and virtual sections of the C. canaliculatum head". Attribution sound.
- Line 2: inside the paragraph that opens "The volume renderings and virtual sections of the C. canaliculatum head highlight an ocular elliptic flattened area"; the next paragraph opens "The compound eyes of both tenebrionid species are dorsoventral extended and cover a large part of the lateral head." Attribution sound.
- Line 3: in the shared tenebrionid paragraph, after "The axons converged towards the optic lobe (Figure 4D,E), which is divided in the lamina, medulla and lobula." and before "The facets in the eye of T. castaneum (Figure 5A) are 92 in both males and females." The T. molitor block is the one citing Figure 4, the T. castaneum block Figure 5. Attribution sound, but only from the neighbours.
- Line 4: after "The axons converged towards the optic lobe connected to the cerebrum (Figure 5D,E)." and "The lamina, medulla and lobula are also distinguishable."; the next paragraph compares the four species' 2D sections. Attribution sound.

So the values belong to the species filed, but a reader of the record cannot trace that from the quote or the location, and lines 3 and 4 share one paragraph. **Each line: error (species attribution untraceable: quote names no species, `where` does not locate the paragraph, note silent).** Fixable by `where` and `note`.

Uncounted on all four: the conditions should add that no eye region or section plane is stated and no tests are reported, and name the fixative; `eye` can carry the paper's eye type (superposition for P. melas; apposition, bilobed, for both tenebrionids; none stated for C. canaliculatum, whose facets are externally indistinguishable). Line 3's note "440 facets of 50 ± 3.2 µm (N = 7) in both sexes" checked, verbatim: "In T. molitor, the eyes consist of 440 regular facets, 50 ± 3.2 µm (N = 7) in diameter in both males and females;".

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Pterostichus melas (italicus), 4.09 deg | error, fixable | where, note | quote MATCH (10); quote names no species and where does not locate the paragraph |
| 2 | Clinidium canaliculatum, 7.36 deg | error, fixable | where, note | as line 1; family Rhysodidae as printed, Carabidae recommended (uncounted) |
| 3 | Tenebrio molitor (lab stock), 6.89 deg | error, fixable | where, note | as line 1, in a paragraph shared with T. castaneum; stock origin not stated (uncounted) |
| 4 | Tribolium castaneum (CRO1), 12.99 deg | error, fixable | where, note | as line 3 |

Errors 4 of 4 audited records (100%), above the 5% bar; none held out. By kind: provenance (species attribution untraceable) 4; quote form 0; bibliographic 0; licence 0 (no page sentence, page metadata CC BY 3.0, Crossref vor CC BY 4.0: accepted pairing); names 0; duplicates 0 against main, 152 desk-d2* and audit-3* branches and corrected/ALL; trait key and units 0; omitted significant or contrary results 0 (none reported in the paper); grading 0.

Unchecked: GBIF placement of Clinidium (GBIF not opened; the Carabidae recommendation rests on insecta.pro and the d165 note); the remainder of the Crossref title beyond the tool's summary (the page title was returned whole and matches); the P. melas italicus axon sentence before line 1 (tool summary, not verbatim); whether N counts pairs within one section or across sections and specimens; figure captions (only "frontal (dorsal view)" noted, tool summary); Supplementary Material, if any.

## Replacement text

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file). "field = new string" replaces the whole field.

Line 1, counted:
- `where` = "Results (Section 3, no subsections), P. melas italicus paragraph: the sentence follows the description of the axons reaching the optic lobe and cerebrum, and the next paragraph opens on the C. canaliculatum head"
- `note`: "Subspecies Pterostichus melas italicus as printed; logged at species." -> "Subspecies Pterostichus melas italicus as printed; logged at species (P. (Feronidius) melas (Creutzer, 1799); P. m. italicus (Dejean, 1828) is a recognised subspecies, Toribio et al. 2020). The quoted sentence names no species; attribution rests on the paragraph named in where (audit 361)."

Line 2, counted:
- `where` = "Results (Section 3, no subsections), C. canaliculatum paragraph, which opens 'The volume renderings and virtual sections of the C. canaliculatum head'; the next paragraph opens on both tenebrionid species"
- `note`: "Family Rhysodidae as printed in the abstract (the family is now often treated as a carabid subfamily; check gbif-names)." -> "The paper prints Rhysodidae; filed as Carabidae (subfamily Rhysodinae, tribe Rhysodini, subtribe Clinidiina on the insecta.pro genus page); baza.biomap.pl still lists the family Rhysodidae. The cornea is smooth and the external facets are indistinguishable in both sexes; the virtual cuticle removal shows a cluster of 70 ommatidia. The quoted sentence names no species; attribution rests on the paragraph named in where (audit 361)."
- `family` (uncounted, recommended): "Rhysodidae" -> "Carabidae"

Line 3, counted:
- `where` = "Results (Section 3, no subsections), tenebrionid paragraph, T. molitor part: the sentence follows 'The axons converged towards the optic lobe (Figure 4D,E)' and precedes 'The facets in the eye of T. castaneum (Figure 5A) are 92 in both males and females.'"
- `note`: "Laboratory stock colony, not wild-caught." -> "Laboratory stock colony at the University of Calabria, origin of the stock not stated; not wild-caught. The quoted sentence names no species and sits in a paragraph shared with T. castaneum; attribution rests on the neighbouring sentences named in where (audit 361)."

Line 4, counted:
- `where` = "Results (Section 3, no subsections), tenebrionid paragraph, T. castaneum part: the sentence follows 'The axons converged towards the optic lobe connected to the cerebrum (Figure 5D,E).' and 'The lamina, medulla and lobula are also distinguishable.'; the next paragraph compares the 2D sections of the four species"
- `note`: "Laboratory strain reared from wild-collected stock." -> "Laboratory strain Croatia 1 (CRO1), collected from a wild population in Croatia and reared in the laboratory. The quoted sentence names no species and sits in a paragraph shared with T. molitor; attribution rests on the neighbouring sentences named in where (audit 361)."

Lines 1 to 4, each, uncounted:
- `conditions`: "the paper does not say whether sexes were pooled or which eye was measured." -> "the paper does not say whether sexes were pooled, which eye was measured, or which eye region or section plane the angle comes from, and reports no statistical test or sex comparison for any eye measure. Specimens fixed in 2.5% glutaraldehyde and 1% paraformaldehyde before ethanol dehydration."

Line 1, uncounted:
- `eye`: "compound eye" -> "superposition compound eye (as the Discussion names it)"

Lines 3 and 4, each, uncounted:
- `eye`: "compound eye" -> "apposition compound eye, bilobed by the expanded gena in the anterior eye field"
