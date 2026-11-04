# desk-d601 progress

Angle: new-species descriptions 2019-2025 with ED (eye diameter) in millimetres for named specimens, reached through Pensoft article XML and article pages that appeared in my own WebSearch results (Evolutionary Systematics, Vertebrate Zoology, ZSE, Herpetozoa, ZooKeys, BDJ), plus ASW and Reptile Database pages. The OLD-ANGLE paragraph was ignored. About 41 WebSearches. Log: docs/views/evidence/desk-d601.jsonl, 4 records, check.py 0 problems (plain and --require-evidence-kind). No ear-length or tympanum trait exists on main, and fish tables print ED as % SL/HL, so no mammal or fish record was possible.

## Filed
- Chimerella mira (Evolutionary Systematics 7(2): 195-209, 10.3897/evolsyst.7.102950, CC BY 4.0): holotype MUSM 40278 ED 2.7 mm and paratype MUSM 40264 ED 2.4 mm (both adult males); ASW page opened. 2 records.
- Phalotris shawnella (ZSE 98(1): 77-85, 10.3897/zse.98.61064): holotype CZPLT-H-594 (adult male) 'Eye diameter 1.1 mm.' Filed as sensory_anatomy per the brief because the Methods print no definition of eye diameter; Reptile Database page opened. 1 record.
- Ansonia karen (Vertebrate Zoology 71: 763-779, 10.3897/vz.71.e73529): holotype ZMMU A-7605 ED 2.7 mm, whole Table 1 row (ED is the 9th value); ASW page opened. 1 record.

## Weak spots
- All text came through the WebFetch reader on Pensoft XML/previews: sentences arrive in ~120-character pieces joined in order; the Ansonia row was read in two fetches (cells 1-9, 10-25) plus a separate ED-column read that agreed. The Chimerella holotype line is 'Measurements (in mm).' followed by the list, quoted as two consecutive sentences.
- Chimerella heading path comes from the reader (Results > Bioacoustics > Type material); the taxon block is not a titled heading.
- Ansonia Table 1 caption prints no unit; mm comes from the Methods precision sentence.
- Crossref not used. Licence sentences read on the XML/preview copies.

## Not filed and why
- Already on main: Rhacophorus dulongensis (d512), Calamaria synergis (d455/d499), Quasipaa taoi (d594), Brachytarsophrys wui (d457/d574), Tylototriton gaowangjienensis (d598), Toxicocalamus longhagen (d298), Plagiopholis maculosa (d477), Rhinophis siruvaniensis (d487), Gracixalus truongi (d588), Zhangixalus thaoae, Stumpffia froschaueri (d576), Litoria kikori (d584; d600 also).
- Licence conflict: Pristimantis sira (CC0 on page vs attribution tag, held out by d307) and Dixonius fulbrighti (Evol. Syst. 7(2), same CC0/attribution mismatch).
- Methods define ED differently from the table label: Lepidophyma jasonjonesi (d585).
- Identity unresolved: Odorrana sangzhiensis (ASW page is Rana sangzhiensis Shen 1986, d591).
- Group means/ranges only, no specimen row: Pristimantis petersioides, Stolephorus (fish, % of length), Kerivoula bat paper (no new species), ZooKeys 67621/79229/24557 tables.
- XML truncated before the description (no value reachable): Leptobrachella verrucosa (Herpetozoa 35), Gracixalus weii, Leptobrachella yongshunensis and L. shimentaina, Xenophrys yingjiangensis, Brachytarsophrys guilinensis, Dendropsophus cannatellai, Pristimantis normawingae, Osteocephalus vasquezi, Zhangixalus thaoae.
- Not measured: Selvasaura candesi and S. evasa, Trachischium lalremsangai, Dasypeltis albigularis, Papuascincus, Pareas temporalis, Pseudoeurycea jaguar, Gekko hulk, Allobates albiventris (adults EL only), Calamaria/Cyrtodactylus santana (ED only as ratio).
- Dead routes: Zootaxa (Lygodactylus herilalai), JoTT (Raorchestes asakgrensis, d584), Trimeresurus liqibini (no Reptile Database page reached).
