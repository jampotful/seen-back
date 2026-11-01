# desk-d304: eye states and counts of polychaetes, sea spiders, tardigrades and a mole in CC BY papers, 22 records

Branch research/desk-d304 from origin/main. About 55 WebSearches, WebFetch only on URLs returned by searches (Pensoft article_preview and download/xml pages; Crossref single-DOI lookups through WebFetch, because curl to api.crossref.org is refused by the proxy). `python3 -I tools/senses/check.py | grep 'd304\.'`: 22 records, 0 problems.

Angle result: the assigned classes (cirrate octopods, heteropods, nudibranchs, chitons, tunicates, brittle stars, box jellyfish, hydromedusae, caecilians, moles, birds) gave almost nothing open and sentence-level; main already holds Octopus, chiton, Acanthaster, Linckia, Tripedalia, Copula, kiwi and oilbird records. The yield came from Annelida (no Polychaeta class on main), Pycnogonida and Tardigrada, which the brief did not name.

Filed (docs/views/evidence/desk-d304.jsonl):
1. Euroscaptor darwini (Talpidae), eye_type vestigial, not externally visible; holotype male, ZooKeys 1255.
2-4. Namanereis canariarum, N. llanetensis (Subterranean Biology 36), N. christopheri (Subterranean Biology 23): eyes absent; whole prostomium sentences rebuilt from consecutive chunks (37, 39 and 18 words). Desk d294 had dropped all three as unreachable whole.
5-7. Apistobranchus jasoni, Prosphaerosyllis modinouae (eyes_count 4; the page prints "pairsof"), ZooKeys 938; Spio pigmentata (eyes_count 4, ZooKeys 1070).
8-11. Eurycyde-paper pycnogonids not yet filed: Nymphopsis duodorsospinosa (4 eyes), Nymphon lituus (4 eyes), Callipallene californiensis ("apparently eyeless"), ZooKeys 530 (Eurycyde bamberi is d285's); Austropallene halanychi (4 eyes, ZooKeys 1185).
12-14. Macrobiotus annewintersae and M. rybaki (eyes present, ZSE 97(1)); Bryodelphax kristenseni (eyespots absent or not visible after mounting, ZooKeys 703).
15-22. Syllidae of Venezuela (ZooKeys 117): Exogone (Exogone) dispar and lourei, Sphaerosyllis piriferopsis and taylori, Syllis amica, gracilis, pseudoarmillaris, vittata; each "two pairs" of eyes. Records of known species, not new ones.

Weak spots for the auditor:
- Spio pigmentata uses a marked cut inside a 70-word sentence (start of sentence kept, middle and end cut). Desk d301 dropped this sentence as over 40 words; the cut is allowed by the quote rule but is the line most likely to be questioned.
- The Namanereis, Apistobranchus and Prosphaerosyllis sentences were assembled from 2 to 4 consecutive tool chunks; word counts were done by hand and check.py passes. Prosphaerosyllis keeps the printed typo "pairsof"; Apistobranchus keeps "notobserved".
- Orders left blank where the paper prints none (polychaetes, Spio, Macrobiotus); an earlier draft of the Namanereis lines carried Phyllodocida from a different paper and was blanked.
- ZooKeys 530: the page byline lists de León-Espinosa first, Crossref lists de León-González first; the byline is followed, as d285 did.
- ZooKeys 117: page prints the family as "Sillydae"; Crossref spells the first author Linero-Arana. The paper's specimen counts in conditions are my sums of the listed lots.
- Lot counts are by lot entries, not individuals per sex; no sexes are given for those polychaetes.

Dropped candidates:
- On main or other branches: Nereis tricirrata (d284), Leitoscoloplos olei (d294), Eurycyde bamberi (d285), Macrobiotus and Bryodelphax absent from all branches.
- Licence or access: Tripedalia maipoensis (Zoological Studies 62, DOI not found at Crossref, no licence on the page); Garm et al. scale-worm eyes (J Exp Biol 224(14), Crossref licence is the Company of Biologists user licence, not CC); Grimpoteuthis feitiana and Luteuthis shuishi (Zootaxa and Zoological Studies, not open); Gegeneophis madhavai (Zootaxa 644, no DOI).
- No eye sentence or no species-level sentence: Ichthyophis griseivermis (Vertebrate Zoology 75; the Diagnosis and Description were beyond the part of the page returned, only a Table 1 eye length of 0.7 mm reached), Olindias deigo (no ocelli text), Rhombophryne longicrus and Synapturanus danta (eye clauses only), Tritomurus veles and Geopselaphus bullonorum (Collembola and beetles, other units' angle; clause-level), Gunton et al. ZooKeys 1020 (new taxa are unnamed "sp. nov. 1" entries), Lee and Kim ZooKeys 1287 (three vent scale worms, "Eyes absent" sits under genus Descriptions), Oroperipatus tiputini (ZSE 100, "Slightly wrinkled eyes laterally behind base of antennae": no count or state; also dropped by d293).
- Erhaia dijiang (snail, taken by another unit), Spio and Rhynchospio: only Spio pigmentata filed.

Questions: Should a state like "apparently eyeless" (Callipallene californiensis) be filed as eye_type none or kept in the authors' words? It is filed in their words.
