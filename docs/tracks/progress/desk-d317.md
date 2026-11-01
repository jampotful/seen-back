# desk-d317: eye states of beetles, a mite harvestman, two harvestmen, a bristletail and two minute wasps, 16 records

Branch research/desk-d317 from origin/main. About 52 WebSearches, WebFetch only on URLs returned by searches (Pensoft article XML at /article/ID/download/xml/ for IDs seen in results or in a Subterranean Biology Coleoptera browse page, MDPI pages) and Crossref single-DOI lookups. `python3 -I tools/senses/check.py | grep desk-d317`: 16 records, 0 problems. Traits: eye_type (14) and ommatidia_count (1, note says "new trait" as check.py requires); Metagovea, Euconnus etc. are eye_type text.

Crossref answered (one call at a time; parallel calls are rate-limited) for every DOI filed: 10.3897/zookeys.1231.142538, zookeys.103.1124, insects 10.3390/insects11110803, subtbiol.43.73185, subtbiol.41.75613, subtbiol.35.52583, subtbiol.38.61733, zookeys.477.8706, jhr.89.77931, zookeys.217.3136, zookeys.52.471, zookeys.806.27320. All vor with CC BY (3.0 or 4.0) matching the page sentence.

Repeat check: a text index of origin/main docs/ plus the evidence, progress and searched files of every unmerged desk and audit branch was built once; every species and DOI was grepped before filing. Drops from that grep: Iandumoema smeagol, Ptomaphaginus troglodytes, Neocarus proteus, Beronaphaenops paphlagonicus (all on main).

Filed (docs/views/evidence/desk-d317.jsonl):
1-2. Euconnus imparitus and E. magnoculus (Staphylinidae, Scydmaeninae), male holotypes, ZooKeys 1231 (d315/d316 had dropped the paper because only paraphrases returned; the two head sentences now came back in consistent pieces).
3. Parazuphium aguilerai (Carabidae), "No trace of eyes or ocular scars", single male holotype, endogean, Morocco (ZooKeys 103).
4. Pterostichus monolineatus (Carabidae), "Eyes weakly convex ...", Insects 11(11): 803.
5-6. Coarazuphium xikrin and C. kayapo (Carabidae), eyes reduced, depigmented, flattened, ommatidia not visible at 50x (Subterranean Biology 43; the d316 XML block did not recur).
7. Leonhardia solaki (Leiodidae), anophthalmous, both sexes (Subterranean Biology 41).
8. Oromia orahan (Curculionidae), eyeless male (Subterranean Biology 35).
9-11. Baezia aranfaybo, B. madai, B. tizziri (Curculionidae), identical male sentence "lacking eyes", each with its own male holotype (Subterranean Biology 38).
12. Metagovea ligiae (Opiliones, Neogoveidae), "Eyes and eye lenses absent." (ZooKeys 477).
13. Mymaromma menehune (Mymarommatidae), "Eye with about 35 ommatidia." female, ommatidia_count (JHR 89).
14. Trechus bouilloni (Carabidae), eyes reduced, flat, holotype, mesovoid shallow substratum (ZooKeys 217).
15. Trilasma ranchonuevo (Nemastomatidae), eyes relatively large, bulging, male holotype (ZooKeys 52).
16. Haslundiella iranica (Microcoryphia, Machilidae), compound eyes black, wider than long, seen in an adult female (ZooKeys 806; d288 had dropped the Diagnosis ratio sentence).

Dropped candidates:
- On main or earlier desks: Iandumoema smeagol, Ptomaphaginus troglodytes, Neocarus proteus, Beronaphaenops paphlagonicus (genus-level eye text), Nocticola gonzalezi (d315 note), Cylindroiulus villumi, Zorotypus komatsui and vinsoni, Spelaeobates coriniensis (46-word sentence), Jujiroa inexpectata, Shenoblemus and Wanoblemus (ZooKeys 923: clause or diagnosis only).
- Genus-level sentence only: Chrysoctonoides longisetosa (Mymaridae, ZooKeys 505): the female "about 12 ommatidia" and male "about 75 ommatidia" sentences sit in the Description of the new genus Chrysoctonoides, not the species treatment, and the genus Diagnosis says about 11 for the female, so no species-level record was filed. Dinapsis (Megalyridae) setose-eye text is group-level and cut.
- Clause or fragment only: Heterospilus belokobylskiji and H. vincenti ("ocelli present but small" clause), Tachycines zhongi/lahaidensis (Rhaphidophoridae covered; clause-level), Euplocania spp. (colour, ratios), Bamazomus shanghang and B. songi ("eye spots distinct." closes a long sentence), Rowlandius pedrosoi ("eyespot suboval; ..." clause), Psilogamasus spp. (no eye text), Cryptomaster behemoth (eye colour only), Websterinereis pettiboneae (polychaete, covered group), Stenohya spp. (sentences over the tool limit), Igatuia cavernicola, Grunagryllus spp. (MDPI Taxonomy, eye text in long sentences or semicolon lists).
- No eye text, or the species text was cut: Anillinus bexarensis and A. reddelli (ZooKeys/Subterranean Biology 44, CC0), Horologion (description not in the text returned), Appalachian Anillini, Bembidion (ZooKeys 1156), Austropurcellia, Eukoenenia serrana (Subterranean Biology 57), Barinas guanenta and Avima wayuunaiki (ocularium shape only, no eyes), Veraphis spp. (eyes only in ratios), Mirlatia, Aphanogmus, Erechthias, Gryon, Gryonoides, Diplolepis abei, Pambolus/Paroplitis (ratios), Bethylus colligatus (eye length measurement in a semicolon sentence, not whole), Glyptapanteles, Fidiobia, Olixon, Triatoma huehuetenanguensis, Biasticus, Claviplatys.
- Strain-level: Drosophila subgroup ommatidia counts (PLOS ONE 7: e37346) per strain; honeybee PLOS ONE paper already on main.
- Not reached: ticks (no new-species eye sentence in search results), Plecoptera/Trichoptera/Lepidoptera new-species papers (searches returned no usable eye sentence).

Weak spots for the auditor:
- All sentences are telegraphic or semicolon lists without a finite verb (accepted precedent). Euconnus (32 words) and Trechus bouilloni (24) carry more than the eye clause; Leonhardia's carries the head ratio and the occipital carina; Haslundiella's carries the sex remark and the l/w ratios; Baezia and Oromia sentences carry head shape.
- Parazuphium: the page title prints a colon "(Coleoptera: Carabidae)"; the XML text returned once showed a reordered title, so the Crossref/page title is used. Treatment block prints no order or family (taken from the title).
- Oromia: the summariser gave "all females except one" for the paratypes; the specimen lines read as five females from Reventon Oscuro plus one male from Acebinos, as filed.
- Pterostichus monolineatus: page footer CC BY 4.0 link, metadata CC BY 3.0, Crossref CC BY 4.0 vor; the sentence describes convexity and relative length only.
- Trilasma: page metadata pages 9-46 versus Crossref 9-45; title keeps the accent in "México".
- Leonhardia: page prints "Tonći Rađa", Crossref "Tonči"; page spelling used.
- Metagovea: Crossref lists Kury before Giupponi; the printed byline order is used. Species validity checked only against the paper (no Opiliones checklist page opened).
- Class is blank in all records (no page prints a class in the classification blocks read).

Questions: none.
