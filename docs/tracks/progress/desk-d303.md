# desk-d303: eye wording in new species of stygobiont, anchialine and marine peracarid, leptostracan and caridean crustaceans, 8 records

Branch research/desk-d303 from origin/main. About 38 WebSearches (4 extended) plus fetches; every fetched article URL came from a WebSearch result. `python3 -I tools/senses/check.py | grep 'd303\.'`: 8 records, 0 problems. Crossref single-DOI lookups (api.crossref.org/v1/works or /works) read for all eight DOIs: author order matches the page byline, all CC BY 4.0 vor, page prints the CC BY 4.0 sentence. No new trait (eye_type throughout).

Repeat check after filing: grep of main docs/ (whole tree) by species and DOI, and git grep over origin/main and every origin/research/desk-* and audit-* branch (docs/views/evidence, docs/tracks, docs/views/audit) for jetama, Sarsinebalia agoensis, terazakii, Nebalia tagiri, spinidigitus, Macrobrachium guizhouense, Macrobrachium parvum, Mayaweckelia and the eight DOI strings: see the result line at the end of this note.

Filed (docs/views/evidence/desk-d303.jsonl):
1. Palaumysis jetama (Mysidae, Mysida), "Eye (Fig. 4A, B, F) large, cornea globular, well pigmented." male description; ZooKeys 1284; holotype adult male, allotype ovigerous female, paratypes both sexes; contrast record (well-eyed cave mysid).
2. Sarsinebalia agoensis (Nebaliidae, Leptostraca), Diagnosis "Compound eyes subrectangular, with three lobes on terminal margin."; ZooKeys 1097; adult females only.
3. Nebalia terazakii (Nebaliidae), "Compound eye without papilla (Fig. 1e), ommatidial part occupying 0.67 length of eyestalk."; ZooKeys 605; post-ovigerous female holotype, adult female paratypes and 32 unsexed juveniles; page byline "B.H.R. Othman" followed over Crossref's name fields.
4. Nebalia tagiri (Nebaliidae), "Compound eye (Fig. 2C): ommatidial part covering two-thirds of eye-stalk."; ZooKeys 897; eye described in the female holotype section only; family/order not printed as headings.
5. Apseudes spinidigitus (Apseudidae, Tanaidacea), "Eye lobe well separated, wide and short, without visual elements."; ZooKeys 1096; the Description is of paratype MBM032095, a non-ovigerous simultaneous hermaphrodite.
6. Macrobrachium guizhouense (Palaemonidae, Decapoda), "Eyes with cornea totally degenerated."; Zoosystematics and Evolution 101(4); holotype male, 28 male and 61 female paratypes.
7. Macrobrachium parvum, "Eyes with cornea strongly degenerated, only small area on tip pigmented."; same paper; Remarks and Discussion call it a stygophile with reduced but pigmented eyes (stated in the record).
8. Mayaweckelia troglomorpha (Hadziidae, Amphipoda), Diagnosis "Medium-sized, eyeless hadziid with conspicuous troglomorphic traits."; ZooKeys 735; the Description has no eye sentence; holotype male, allotype female, paratypes and two juveniles. The sentence is a nominal phrase; an auditor may judge it a fragment.

Dropped:
- Arrived in pieces or over the tool limit: Pseudocrangonyx wonkimi (ZooKeys 960, "eyes absent" ends a 17-word head sentence returned as two quotes), Pseudocrangonyx gudariensis (ZSE 92, same pattern, plus Remarks sentences continue), Phasmon typhlops (ZooKeys 1008; Diagnosis, Description and Remarks eye sentences all over the limit), Pseudomma kryotroglodytum (ZooKeys 1079; long sentences), Eocuma orbiculatum (ZooKeys 910; "ocular lobe ... with 3 lenses" ends a 75-word sentence).
- No eye sentence in the text read: Typhlocirolana longimera (SB 22), Hangangbathynella mihoensis (ZooKeys 1046), Siambathynella (SB 44), Allobathynella danyangensis (SB 44), Stenasellus tashanensis (SB 26), Niphargus hakani (SB 22), N. elburzensis and N. zagrosensis (ZSE 100), Niphargus carolinensis (Hydrobiology), Stygobromus (SB 48), Sinelobus kisui (ZSE 98), Bogidiella pingxiangensis (figure fragment only, d280/d299).
- XML ends before the descriptions: Bermudamysis caribbaea, Heteromysis troglophila, Palaumysis antillensis (ZooKeys 1283, 83,000-character text, descriptions not reached), Ischiomysis proincisa (ZSE 100; eye sentences describe stalk and cornea shape, not state), Phoxokalliapseudes shandongensis and Swireapseudes planafrontis (ZooKeys 1096, XML cut before their descriptions).
- Eye sentences not a state or count: Heteromysis cancelli, H. fosteri, H. octopodis (ZooKeys 685; eyestalk shape and scales).
- On main already: Graeconiscus gevi, Caridina zhaoi and other Caridina (many units).
- Licence or access: Procambarus adani (Revista Mexicana de Biodiversidad, CC BY-NC-ND), Tegano tashanensis (Brill), Bogidiella isajii and B. painushima, Hyalella troglofugia, Salmoneus karenae (Zootaxa), Pseudotanais isabelae and Zeuxo bimbache (Marine Biodiversity, restricted), Koonunga (PLoS ONE on PMC, PMC not used), Plazi and zenodo copies not used.
- Not crustacean: Erhaia dijiang (gastropod, SB 56).
- Searches for cave crayfish (Cambarus, Procambarus, Orconectes), Remipedia, Thermosbaenacea, Spelaeogriphacea, Mictacea, Cumacea, Syncarida, Sphaeromatidae, Cirolanidae, Monolistra and Alpheidae returned no open CC BY page with an eye sentence (biostor, archive.org, mapress/Zootaxa, Plazi, ResearchGate, caves.org journals); none opened beyond Pensoft, MDPI and Crossref.

Retrieval notes: Pensoft article_preview.php and download/xml pages both worked; WebFetch breaks any sentence over about 125 characters into quotes, so only short eye sentences could be filed whole. Crossref /v1/works returned a client error twice for 10.3897/zookeys.1096.79382 and worked at /works/.

Repeat check result: grep of origin/main and all origin/research/desk-* and audit-* branches (evidence, tracks, audit paths) for the eight species and DOI strings returned no hits; a whole-docs/ grep of main showed only unrelated substrings (Buteo galapagoensis, Katagiri in a reference).
