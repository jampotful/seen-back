# desk-d312: eye states of cave crickets, a cave planthopper, an ant-inquiline histerid, a root mealybug and two aphids, 12 records

Branch research/desk-d312 from origin/main. About 45 WebSearches; WebFetch only on URLs returned by searches (Pensoft article XML and article_preview pages). `python3 -I tools/senses/check.py | grep d312`: 12 records, 0 problems. Traits: eye_type and ommatidia_count (keys already on main; notes say so where check.py needs it).

Repeat check: every species and DOI grepped over origin/main docs/ and over evidence and progress files of unmerged desk/audit branches (files not on main) before filing; no hits for the 12 species.

Filed (docs/views/evidence/desk-d312.jsonl):
1-7. Tachycines (Gymnaeta) zhongi, lahaidensis, shibenzhangi, ziyunensis, jialiangensis, shanduensis (male Description head sentences) and jinniui (female), cave crickets, ZooKeys 1109: 115-140. Eye states run from developed to extremely degenerated; shibenzhangi's sentence says some individuals are blind; ziyunensis conditions carry the Diagnosis contrast with shibenzhangi; jinniui carries the Diagnosis wording ("slightly reduced eyes") against the Description ("ommateum black and well developed"). T. buyii and T. portae (identical to shanduensis) and T. pinglangus (long semicolon sentence) not filed.
8. Spelaeodelphax nexus, compound eyes and ocelli absent, Subterranean Biology 55: 1-25 (desk-d297 set this sentence aside because it came in pieces; here a 26-word sentence read in two passes that agree with the tool's word count).
9. Paramyrmetes foveipennis (Histeridae), eyes flattened but visible from above, male lectotype, ZooKeys 675: 57-73.
10. Ishigakicoccus shimadai (Rhizoecidae), "Eye spot absent.", adult females, ZooKeys 616: 115-124.
11-12. Neonipponaphis pustulosis (3-faceted eyes, apterae) ZooKeys 236: 81-89; Aleurodaphis sinojackiae (3 facets, apterae) ZooKeys 135: 41-56.

Dropped candidates:
- On main: Ptomaphaginus troglodytes, Geopselaphus bullonorum, Valenciolenda fadaforesta, Wanoblemus/Shenoblemus/Jujiroa (ZooKeys 923), Tachycines trapezialis, Nocticola gonzalezi (nymph ommatidia on main; adult eye sentences not filed to avoid a same-species repeat).
- No eye sentence in the paper: Ascodipteron sanmingensis (BDJ 9), Ascodipteron euryale (ZooKeys 1273), Anillinus spp. (ZooKeys 1209, Anillini are all eyeless and the descriptions do not say so), Termitotrox venus/cupido, Ericaphis voegtlini, Indomasonaphis polygoni, Aphis luzuriagae/gaultheriae, Megaselia shadeae.
- Sentence longer than the tool returns or only in clauses: Apterygothrips flavescens (37-word head sentence), Zorotypus komatsui and Z. vinsoni (ZooKeys 1178), Jujiroa inexpectata (clause in a long semicolon sentence), Platycnemis phasmovolans larva (clauses only), Gosik 2019 weevil larvae (stemmata fragments), Chalcophora japonica chinensis larva (subspecies).
- Licence: Phyllium samarense and other Phylliidae (ZooKeys 1173, page prints CC0 Public Domain Dedication, not a CC BY tag; clean eye sentences with verbs for female and male, worth a ruling).
- Genus-level only: Neotermitosocius/Coptotermocola "Eyes large and produced anterolaterally.", Coframalaxius (genus description).
- Closed or unreachable: Ptiliidae compound-eye scaling (Doklady / Arthropod Struct Dev), Trichogramma ommatidium (Elsevier), plazi treatment pages (redirect placeholders only), Zootaxa.

Angle result: Anillini, Leptodirini, Curculionidae, Phoridae, bat flies, Chironomidae and Odonata larvae gave no usable species-level eye sentence from open sources; the yield came from Orthoptera, Hemiptera and Coleoptera papers in Pensoft journals read through article XML.

Weak spots for the auditor:
- Crossref was blocked (PROVENANCE_REQUIRED) from the Paramyrmetes lookup on, so records 9 to 12 carry the publisher's citation line and page licence statement and say so; ZooKeys 1109 and Subterranean Biology 55 were checked on Crossref (CC BY 4.0 vor).
- Spelaeodelphax: the quote was rebuilt from two tool passes (first 120 characters, then the remainder); the last author is printed "Lopes Ferreira R" in the page citation line but Crossref gives Rodrigo L. Ferreira.
- Tachycines records do not give the paratype localities for shibenzhangi and jinniui; class is blank because only title and XML metadata name Orthoptera and Rhaphidophoridae.
- ZooKeys 135 page names the Creative Commons Attribution License without a version (link is CC BY 3.0).
- Aphid "3 facets" is filed as ommatidia_count 3 with per-eye not stated.

Questions: does CC0 (Phylliidae paper, ZooKeys 1173) count as an accepted open licence for a repository copy?

## Desk disposition after audits 416-417
Audit 416 (lines 1-7, Tachycines, ZooKeys 1109): 2 fixable errors (lines 3, 7), fixed with the auditor's text; the optional line-4 fix applied; the optional class fill ("Insecta") not applied, class stays blank because the page does not print it as a taxonomy line. Audit 417 (lines 8-12): 1 fixable error (line 8, paratype count), fixed; optional fixes to lines 9 and 11 applied. 3 errors in 12 (25%), none held out or dropped. Crossref refused the auditors' lookups (PROVENANCE_REQUIRED, not worked around), so for the records checked there the bibliography rests on the publisher citation line and the page-printed CC licence with no Crossref cross-check; this is an owner question if the licence rule requires a Crossref tag. The Phylliidae paper (ZooKeys 1173, CC0 on page) was held out by the unit and is passed to unit d313.
