# desk-d308: eye states of an owl, a caecilian, an ant, a mayfly and a dobsonfly, 5 records

Branch research/desk-d308 from origin/main. About 52 WebSearches; WebFetch only on URLs returned by searches (Pensoft article_preview pages, the Kafkas veterinary journal PDF) and Crossref single-DOI lookups through WebFetch for all five DOIs (api.crossref.org/works/ form). `python3 -I tools/senses/check.py docs/views/evidence/desk-d308.jsonl`: 5 records, 0 problems.

Repeat check: every species and DOI grepped over origin/main docs/ and over the docs files that differ from main on every origin/research/desk-* branch before filing.

Filed (docs/views/evidence/desk-d308.jsonl):
1. Bubo bubo, new trait eye_axial_length_mm, 30.9 to 31.35 mm (Discussion sentence, range); 12 eyes of 6 adult owls, Kafkas Univ Vet Fak Derg 30(1), CC BY-NC 4.0. Family not printed on the page, left blank; order and class from reference titles, said in the note.
2. Caecilia pulchraserrana, eye_type, eyes not covered by bone (ZooKeys 884). Another unit dropped this sentence as arriving in pieces; here the two pieces join at a space.
3. Ooceraea hainingensis, eye_type none in the worker caste, "Compound eyes and ocelli absent." (ZooKeys 1205); the one dealate queen has eyes and ocelli (in conditions).
4. Cincticostella jianchuan, male imago compound eyes contiguous, upper brown and lower black (ZooKeys 1205).
5. Corydalus ralphi, three yellow ocelli each ringed brown (ZooKeys 1111).

Dropped candidates:
- Ooceraea joshii and O. decamera, Strongylocentrotus purpuratus pluteus (Valero-Gracia 2016), Camponotus consobrinus, Grapholita molesta, Scolia hirta: already on main or in earlier desk notes.
- Talpa occidentalis (BMC Biol 2008, small eyes with closed eyelids covered by skin): only the PMC and repository copies were reachable, no publisher page; the figure legend says "absence of eyelids" against the Results wording.
- Eurycea rathbuni (PeerJ 11840): held earlier by d280 (donated dead captive stock).
- Dasyprocta prymnolopha axial length (Acta Sci Vet 117025): the sentence is a 55-word list, no licence name on the page.
- Amphimedon queenslandica pigment ring (Front Mar Sci 2017): abstract and results sentences too long for the tool, only paraphrases returned.
- Guiana and Clymene dolphin eyes (An Acad Bras Cienc 2022): ranges not tied to a named dimension, no licence on the page, authors not printed.
- How Do Whales See? (IntechOpen chapter, fin and sei whale eye 13 cm): species not named in the sentence.
- Larus michahellis axial length (KVFD 2025): values only in tables.
- Drosophila mauritiana, D. simulans, D. melanogaster ommatidia counts (BMC Evol Biol 2014): strain-level data, per-species n in a supplement.
- Stoneflies in Baltic amber (EJT 3107): amber insects were covered earlier.
- Dibamus tropcentr and Ichthyophis griseivermis: journal and licence of the Dibamus page not identified; the Ichthyophis eye sentences were not reachable in the part of the page returned.
- Colletes perplexus and C. quadratus (ZooKeys 1268): no eye sentence.

Angle result: the Lepidoptera, Trichoptera, Plecoptera, Odonata, bee, wasp, echinoderm, cnidarian, sponge, mammal and bird searches gave mostly closed or already-filed papers; mammal and bird eye sizes in CC BY papers were rare. The yield came from Pensoft descriptions with short whole eye sentences and one veterinary journal.

Questions: whether eye_axial_length_mm should stand as a new trait key or be filed under eye_diameter_mm; whether blank family is acceptable for Bubo bubo when the paper prints no family.

## Desk disposition after audit 404
Audit 404: 1 fixable error in 5 (line 1); replacement text applied; all 5 records merged. eye_axial_length_mm is already a key on main (Olsson 2021 Bubo bubo is a different paper).
