# desk-d301: eye states in small worms, rotifers and tardigrades (meiofauna angle), 7 records

Branch research/desk-d301 from origin/main. About 35 WebSearches (3 extended) plus fetches; every fetched article URL came from a WebSearch first. `python3 -I tools/senses/check.py | grep 'd301\.'`: 7 records, 0 problems. Crossref read for all seven DOIs (author order matches the pages; CC BY 4.0 vor for ZooKeys and PLoS ONE; EJT 398 is CC BY 3.0 with content-version unspecified and the PDF prints "Creative Commons Attribution 3.0 License"). No new trait (eye_type, eyes_count).

Repeat check after filing: grepped the whole docs/ tree on this branch and git grep across every origin/research/desk-* and audit-* branch (docs/) for each species name and DOI; result in the closing line below.

Filed (docs/views/evidence/desk-d301.jsonl):
1. Pectinereis strickrotti (Nereididae), "Eyes and lens absent (Figs 4D and 5A).", PLoS ONE 19(3) e0297961; holotype and three paratypes (epitokous males, one incomplete female).
2. Cephalodella binoculata (Rotifera), two distinct red eyespots in front of the head, ZooKeys 1141; holotype female, two female paratypes; Abstract and Differential diagnosis agree.
3. Milnesium minutum (Tardigrada), holotype description "eye spots present", ZooKeys 580; Specific diagnosis agrees.
4. Milnesium sandrae, same paper, holotype description "eye spots present".
5. Microstomum laurae (Macrostomorpha), paired red eyespots about 43 um, EJT 398; vegetative holotype plus one additional specimen.
6. Microstomum edmondi, "Pigmented eyes absent." (pigmented only, stated in the value), EJT 398; holotype male plus 12 additional specimens.
7. Macrostomum littorale, two round eyes (count only), ZooKeys 1099; Diagnosis says "two almost round eyes"; text read ended in the Remarks of this species.

Dropped:
- Already on main or branches: Nereis tricirrata (d284), Tetranemertes bifrost (d294 / audit 385 line), Milnesium berladnicorum (d293 dropped: sentence begins mid-sentence), Placobdelloides sirikanchanae (leech, done in earlier units).
- Sentence over 40 words or returned in pieces: Spio pigmentata and Rhynchospio aciliata (ZooKeys 1070, 1100; prostomium sentences about 69 words), Phylo heterochaetus (ZooKeys 1068; the prostomium sentence reached in two quotes, the paper spells "eyepots"), Nipponnemertes incainca (ZooKeys 693; eyespot sentence long and arrived as a fragment), Temnocephala ivandarioi (ZooKeys 918; eyespot clause is part of a list, not a whole sentence).
- Text not reached: Tetrastemma album, persona, shohoense (ZooKeys 1146; XML ends before species treatments), other Tetranemertes species (preview truncated), Helobdella spp. (ZooKeys 1261; XML ends in Methods), Milnesium matheusi (ZooKeys 884; fetched text ends in Table 4, Differential diagnosis not reached, so contrasting wording could not be checked), Minibiotus formosus (excerpt ends before the description), Dugesia (ZooKeys 1233; Tricladida, text ends before descriptions), Perinereis, Sigambra, Lumbrineriopsis, Terebellidae items (no fetchable Pensoft text in results).
- No eye statements in the article: gastrotrich papers ZooKeys 190, 223, 289; rotifer papers ZooKeys 315, 787.
- Refused or unreadable: Nature (Scientific Reports Cercaria duplicata, Syllidae), PMC, Springer (trematode cercarial papers), Plazi redirect pages (also a third-party copy), ResearchGate.
- Trematode miracidia/cercaria, monogenean larvae, acoels, kinorhynchs, sipunculan/echiuran larvae: searches returned Zootaxa, Springer, ScienceDirect, BioOne or PMC pages only; nothing filed.

Retrieval note: Pensoft article ids equal the last number of the DOI; search results for "download xml" returned fetchable XML. WebFetch paraphrases and splits long sentences, so only sentences returned whole in a quote were used; the figure references were confirmed by a second precise fetch (Cephalodella, Macrostomum).

Repeat check result: no hit for any of the seven species or DOIs in docs/ on this branch or on any of the 795 origin/research/desk-* and audit-* branches.
