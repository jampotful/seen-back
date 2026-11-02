# desk-d319: eye states of a box jellyfish, giant clams, Mantophasmatodea and two hydromedusae, 8 records

Branch research/desk-d319 from origin/main. About 52 WebSearches; WebFetch only on URLs returned by searches (Pensoft article XML at /article/ID/download/xml/ for IDs seen in results, the MDPI page, Crossref single-DOI lookups one at a time, several refused with RATE_LIMIT_EXCEEDED and retried singly). `python3 -I tools/senses/check.py | grep desk-d319`: 8 records, 0 problems. Traits: eye_type (6), eyes_count (1), eye_diameter_mm (1; key on main, note says "new trait" as check.py requires).

Repeat check: a text index of origin/main docs/ plus the evidence, progress and searched files of the unmerged desk and audit branches (built once, 1 Nov 2026); every species and DOI grepped before filing, no hit.

Filed (docs/views/evidence/desk-d319.jsonl):
1. Meteorona kishinouyei (Cubozoa, Chirodropida), six eyes per rhopalium (ZooKeys 503).
2-3. Tridacna maxima (eyes_count 221) and T. squamosa (eye diameter 0.490 mm), hatchery-bred giant clams (Biology 15(4): 363); the two Results sentences are different, each filed for one species only.
4. Kuboesphasma compactum, male, compound eyes prominent, ocelli absent (ZooKeys 746).
5-6. Striatophasma naukluftense and Pachyphasma brandbergense, male Head sentences (ZooKeys 166).
7-8. Melicertissa antrichardsoni (black ocellus at base of each tentacle and cordylus, paratypes) and Paralovenia yongalensis ("No ocelli observed.", holotype) (ZooKeys 783).

Dropped candidates:
- Licence unknown: Tripedalia maipoensis (Zoological Studies 62-17; page showed only a copyright notice, PDF not readable).
- Review or no eye data: octopus eye review (Front. Physiol. 10: 1637; review values from cited work), Currea et al. Commun Biol 6: 246 (method paper, pooled), Psaltoda moerens and Grapholita molesta (on main).
- No eye text: Acanthodasys paurocactus (ZooKeys 190), Echinoderes komatsui/hwiizaa (ZooKeys 382), Olindias deigo (ZooKeys 900), Nausithoe werneri (ZooKeys 984, legend label only), Parasapyga spp. (ZooKeys 369, eye-patch colour only), Tyloceridius stictocephalus (ratios), Andixius spp. (ZooKeys 1141, eye colour only).
- Already dropped or covered: Bethylus colligatus (ratio sentence), Dryinus georgianus, Nesoproxius kishimotoi, Geopselaphus bullonorum (Pselaphinae covered), Shenoblemus/Wanoblemus/Jujiroa (d317), Zorotypus komatsui (on main), Kumarembia hurleyi (amber, clauses only).
- Not reachable: Plazi treatment pages return only a redirect notice; Psocodea (Myopsocus, Lichenomima) and Odonata, Tetrigidae, Endecous (cave crickets) papers were not traced to an open Pensoft article.
- Minutophasma richtersveldense: head text cut in the page text returned, so not filed.

Weak spots for the auditor:
- Meteorona: holotype and paratype sexes disagree between Material examined and Table 3 (stated in conditions); the sentence ends with figure references kept inside the quote.
- Tridacna: the page author list is cut by an ellipsis, so the Crossref list (11 authors) is used; page footer CC BY 4.0 versus metadata CC BY 3.0; the T. maxima Results sentence start was not checked against its predecessor. Pallial eyes are pinhole eyes without a lens (in conditions).
- Kuboesphasma: Citation line prints 2017, front matter and Crossref 2018; 2018 filed. Class blank.
- Mantophasmatodea: no formal classification block in the ZooKeys 166 text; class/order/family from the title and article categories. "interoccular" is the printed spelling.
- Melicertissa: the ocellus sentence is in Colour and describes the paratypes; Paralovenia quote is three words (a null observation on one specimen).
- All quotes are telegraphic (no finite verb) except Melicertissa and the Tridacna sentences.

Questions: none.

## Desk disposition after audit 430

Audit 430 read all 8 lines and found 2 fixable errors in 8 (line 2 quote omitted the printed "Specifically," and a note about main; line 4 printed year 2017 and a conditions error). All were corrected with the auditor's replacement text, plus three optional note fixes. All 8 merged. WoRMS and the speciesfile catalogue could not be opened, so group-authority name checks for jellyfish, clams, hydromedusae and Mantophasmatodea are unconfirmed (owner question).
