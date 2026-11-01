# desk-d309: eye states of marine and freshwater crustaceans, a clingfish, a sculpin, flies, a firefly, an ant, polyclads and slugs, 20 records

Branch research/desk-d309 from origin/main. About 50 WebSearches (many restricted with allowed_domains to zookeys.pensoft.net, europeanjournaloftaxonomy.eu, zse.pensoft.net and peerj.com); WebFetch only on URLs returned by searches, Pensoft article_preview.php pages (article id equals the DOI suffix for ZooKeys papers; not for older ZooKeys such as ZooKeys 404 and not for ZSE) and Crossref single-DOI lookups for every DOI filed. `python3 -I tools/senses/check.py | grep d309`: 20 records, 0 problems. Traits: eye_type, eyes_count, ommatidia_count (key already on main, note says so); no new key.

Repeat check: species and DOI grepped over origin/main docs/ and over the evidence files of every origin/research/desk-, audit- and sweep- branch (one dump to a scratch file) before each record; no hits for any filed species or DOI.

Filed (docs/views/evidence/desk-d309.jsonl):
1-2. Amphilochus anoculus (eyes absent, Remarks sentence) and A. hamatus (eyes not evident, ill-defined eye-patch), deep Atlantic amphipods, ZooKeys 731.
3. Pseudomma kryotroglodytum, red cornea-like eyeplate portions, Antarctic ice cave mysid, ZooKeys 1079.
4-5. Amblyops arianii (eye rudiments without visual elements) and Thalassomysis tattersalli (ommatidia without rhabdom forming a cornea; non-adult male), Antarctic deep-sea mysids, European Journal of Taxonomy 940.
6. Abyssomysis cornuta, eyes reduced to horn-like eyestalk rudiments on an eyeplate, Angola Basin, EJT 628.
7. Cottus cyclophthalmus, eye round and protruding (eye diameter 7.3 % SL in the same sentence, not filed as a key because the key is in mm), EJT 834.
8. Barryichthys hutchinsi, eye large and dorsolateral, ZooKeys 864.
9. Laspionchis boucheti, central papilla bears three dorsal eyes (eyes per papilla, not a body total; genus Diagnosis says usually four), ZooKeys 877.
10-12. Haematopota fenestralis, Chrysops brucei, Tabanus gratus, female eyes separated by the frons (males not studied), ZooKeys 769.
13. Oculogryphus chenghoiyanae, female compound eyes with 13 ommatidia (per eye or both not stated), ZooKeys 739.
14-15. Prostheceraeus vittatus and Euryleptodes galikias, polyclad eye arrangements, ZooKeys 404 (Pensoft article id 3776, DOI suffix 7122).
16-17. Asymmetrione tuxtlaensis, bopyrid isopod: female eyes at the ventral anterolateral head edges, male eyes conspicuous (two records, EJT 861).
18. Mesembrius arcuatus, male eyes holoptic, ZooKeys 1046.
19-20. Protanilla gengma, gyne compound eye with 12 ommatidia and male eyes large (REL 53 to 57), EJT 987.

Weak spots for the auditor:
- Telegraphic sentences with no finite verb: Amblyops arianii, Thalassomysis tattersalli, Abyssomysis cornuta, Barryichthys hutchinsi, Tabanus gratus ("Eyes separated by ..."), Mesembrius arcuatus, the polyclad pair, the male Asymmetrione and male Protanilla. Treated as whole sentences in the descriptive style of the papers (d307/d308 filed the same style). If the owner reads these as noun-phrase fragments, those records go.
- Higher taxa: classes left blank where the page prints none (most records). Orders/families filled from the title or text where the page names them (Laspionchis: Gastropoda and Pulmonata from the title; Tabanidae from an Introduction sentence; Oculogryphus and Mesembrius from the title); each note says so. Amphilochus and mysid records carry no class (Crustacea is not a class heading).
- Eye state versus eye shape and colour: Cottus (round, protruding), Barryichthys (large, dorsolateral), Tabanidae (separated; colour bands only in conditions) lean on the open question from d307 about whether such statements count as eye_type. The separated-eyes (dichoptic) and holoptic records are states in the usual sense.
- Counts: Oculogryphus (13) and Protanilla (12) do not say per eye or both; the values say so. Laspionchis is per papilla.
- Pages: European Journal of Taxonomy 628 and 861 have no page range in the record because the tool did not return one; 940, 834 and 987 ranges were read from the page.
- Authors: Quảng Ngô Xuân is written "Quảng N X" in the initials style (page prints full names); Chevaldonné and Álvarez keep their accents.
- Crossref licence: EJT papers show CC BY 4.0 with content-version "unspecified" (accepted with the page-printed CC BY sentence); Pensoft papers show vor.
- Quote assembly: every WebFetch piece joined here came back as consecutive pieces of one printed sentence or as one piece; the male Asymmetrione sentence and the Euryleptodes sentence were joined from two and three pieces at commas/spaces.

Dropped candidates:
- Already on main: Blepharicera gengdica, B. balangshana, B. kongsica (d296), Triplophysa anshuiensis and Oreonectes qinae (d295); Triplophysa wulongensis noted in d280/d295.
- Too thin or fragment: Haliella seisuimaruae ("Pigmented eyes absent."), Amphilochus anoculus Description ("Eyes absent."), Petalophthalmus cristatus ("No external corneal structures visible."), Abyssomysis cornuta ("Eyes without visual elements."), Guinean Tabanus guineensis ("Black eyes separated by black frons.").
- Contradiction: Atylotus nigromaculatus (Head says eyes with a thin black band, Note says the species has eyes with no band).
- Long sentences or unclear specimen counts: Sphyrapus caribensis and Kudinopasternakia siegi (eye-lobes without visual elements, ends long cephalothorax sentences), Triatoma mopan (eye/ocelli comparisons in long sentences), Mesembrius caffer (male slightly dichoptic; material is lists without totals), Onchidium melakense (ZooKeys 892; "Some of these papillae bear dorsal eyes" carries no count; central papilla clause inside a longer sentence), Laspionchis bourkei (description not in the text read), Dactylamblyops murrayi (not new, only partial sentence).
- Licence/bibliographic: Trichomycterus dali and Aspidoras albater (SciELO pages without authors, DOI or licence sentence; Crossref lists no licence for T. dali, same hold as d298); Paraphronima gracilis (Current Biology, Elsevier user licence, not CC); scallop eye-number papers (NSF PAR repository copies, BioOne).
- No body text on the page: Gangaichthys indonepalicus (ZooKeys 1289, only the Abstract on the page), Sueviota sp. (ZooKeys 1212), moray eel and Chaetostoma pleco (ZSE pages carry only metadata), Baltic amber isopod and DIVA-1 view pages (EJT view pages hold the abstract only; DIVA-1 was then read through its download PDF).
- Not reached: Hyperiidea, Euphausiacea, holothurian, ophiuroid, asteroid, scallop, Odonata, Trichoptera, Neuroptera and Culicidae papers with an open-licensed species-level eye sentence; searches returned Zootaxa, Plazi and repository pages or papers whose eye sentences continue past 40 words.

Questions:
1. Do eye-shape, eye-size and eye-colour statements (round and protruding, large and dorsolateral, black with bands) count as eye_type states? Records 7 and 8 depend on it.
2. Should telegraphic Diagnosis or Description sentences without a finite verb count as sentences for the quote rule?
3. Should an eye_diameter_pct_sl style key exist for fish (Cottus cyclophthalmus 7.3 % SL), or do such values stay in conditions?
