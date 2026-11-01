# desk-d316: eye states of fungus gnats, gall midges, a keroplatid and cave-cricket relatives, 12 records

Branch research/desk-d316 from origin/main. About 40 WebSearches and WebFetch only on URLs returned by searches (MDPI pages, Pensoft article XML and preview pages, Crossref single-DOI lookups). `python3 -I tools/senses/check.py` for desk-d316: 12 records, 0 problems. Traits: eye_bridge_width_facets (key introduced by desk-d297; note says "new trait" as check.py requires) and eye_type.

Crossref answered for 10.3390/insects13010019, 10.3390/insects16090883, 10.3897/zookeys.1231.143063, 10.3897/zookeys.1275.181827 (CC BY 4.0, vor, authors and volumes match). The Insects pages print only a metadata CC BY 3.0 link, so those records rest on the CC BY 3.0 page / CC BY 4.0 Crossref ruling.

Repeat check: species and DOI grepped over origin/main docs/ and, in one pass over all unmerged desk and audit branches (evidence, progress, searched), for Catocha, Planetella, Asioditomyia, Proceroplatus, Diestramima, the two Rhaphidophoridae epithets, the four DOIs, Davimacrocera and Docosia: no hit.

Filed (docs/views/evidence/desk-d316.jsonl):
1-3. Catocha jingfui, C. manmiaoe, C. shengfengi (Cecidomyiidae): "Eye bridge complete, 3–4 facets wide, similar medially and laterally." (Insects 13(1): 19). Each has its own male holotype; the sentence is identical in the three. C. manmiaoe's vertex is broken on the described specimen.
4. Planetella taiwanensis: "Eye bridge lacking." (holotype male only).
5. Asioditomyia bruneicola (Ditomyiidae): compound eye semiglobular, not emarginated around antennal base.
6-7. Proceroplatus dapanshanus and P. biemarginatus (Keroplatidae, Insects 16(9): 883): compound eye outline and surface sentences.
8-10. Diestramima ligula, D. longzhouensis, D. napoensis (Rhaphidophoridae, ZooKeys 1231: 119-132): identical male eye-and-ocelli sentence.
11-12. Rhaphidophora jiaozishanensis and Diestramima (Baculitettix) phytophylacis (ZooKeys 1275: 299-309): "Eyes reniform ... (Fig.)" male sentences; forest litter, not caves.

Dropped candidates:
- On main: Cixius palmirandus and C. theseus (desk-d297, Subterranean Biology 51: 61-101); Domene lizeyui (desk-d281); the four-beetle micro-CT paper (Life 12(5): 741) is on main under interommatidial_deg for the same species and DOI (ommatidia counts 1380, 440, 92 not filed to avoid a same-DOI repeat). Eye-morphology papers for Scythris, Histia, Lymantria xylina, Cacopsylla, Asiophrida, Eucryptorrhynchus, Tomicus, Dineutus, Titanus, Ceratosolen and Empoasca are all on main.
- On main as a dropped clause: Spelaeobates coriniensis (Subterranean Biology 46: 21-46): "with no eyes" is a clause of a 46-word head sentence; not filed (desk-d311 dropped it too).
- Genus-level only: Davimacrocera davidi and D. taiwanensis (eye text only in the genus description, Insects 15(12): 1018); Quasitagalis afonsoi (genus description; species Comments give eye-size ratios of the sexes in clauses); Dongodytes, Five new trechine genera and Coarazuphium-type cave carabid papers (eyeless in genus characteristics only or text not reached); Zorotypus komatsui (d310, d312).
- No eye state in the text: Sergentomyia pradeepii, Pericoma unipennata, Trichophoromyia ruifreitasi (abstract only), Simulium khelangense (no eye sentence), Synorthocladius federicoi ("Eyes bare" inside a semicolon list), Allacta spp. (interocular space only), Tetrigidae of Costa Rica (eye position only), Atkinsoniella spp. (colour), Neotropiconyttus (clauses in long sentences), Asiodiplosis largifica ("Eye facets round.", general adult description, not filed).
- Sentence about ocelli only: Docosia (Insects 12(12): 1069, species name not read), Bolitophila nikolae, Diadocidia pseudospinusola.
- Blocked or not reached: subtbiol.pensoft.net article XML for Oromia orahan (52583), Baezia (61733) and Coarazuphium (73185) returned PROVENANCE_REQUIRED and were not retried; the page versions show abstracts only. Trichoptera, Plecoptera and Lepidoptera new-species searches gave no usable eye sentence.

Weak spots for the auditor:
- All sentences are telegraphic (no finite verb); Planetella ("Eye bridge lacking.") is three words and carries no measurement.
- Insects pages: licence rests on page metadata CC BY 3.0 plus Crossref CC BY 4.0 (vor); no licence sentence in the fetched text.
- Catocha sentence is identical in three species; Diestramima sentence identical in three; each has its own holotype.
- Planetella holotype locality: the tool returned "Nantou/Taitung (as printed)" for the same Tianlong trail record; the conditions say it was not resolved.
- Asioditomyia: the page text read ended inside the Description; female status not seen.
- Rhaphidophora/Diestramima (ZooKeys 1275): no citation line in the XML; author initials assembled from the Crossref author list; year 2026 from the Crossref issue date.
- Diestramima ligula/longzhouensis/napoensis sentence was read as two fragments joined (to "antennal sockets," and the remainder) on two passes.
- Class blank everywhere (no page prints a class); order Diptera comes from the titles for the MDPI papers.
- Proceroplatus: the ocellus sentences (three versus two ocelli) are in conditions only.

Questions: none.
