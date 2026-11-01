# audit-409: desk-d311, file lines 1 to 7 (of 50)

Audited 1 November 2026 from the desk-d311 files present untracked in the worktree (docs/tracks/progress/desk-d311.md and docs/views/evidence/desk-d311.jsonl; neither committed here, neither edited). Branch research/audit-409 from origin/main (095e055d8). Six other auditors take lines 8 to 50. `python3 -I tools/senses/check.py | grep d311`: "docs/views/evidence/desk-d311.jsonl: 50 records, 0 problems". Quote lengths (`len(q.split())`) for lines 1 to 7: 13, 18, 18, 23, 16, 4, 9, all within 40.

Sources opened (WebFetch, every URL from a WebSearch result): zookeys.pensoft.net/article_preview.php?id=76077 (one pass), peerj.com/articles/17783 (two passes) and peerj.com/articles/17783.pdf (one pass), peerj.com/articles/9934 (two passes), zookeys.pensoft.net/article_preview.php?id=78233 (one pass), www.mdpi.com/2075-4450/13/2/119 (two passes). Crossref single-DOI lookups (api.crossref.org/v1/works/) for 10.3897/zookeys.1108.76077, 10.7717/peerj.9934, 10.3897/zookeys.1083.78233 and 10.3390/insects13020119, each read on the first call; 10.7717/peerj.17783 failed (client error) twice and was not worked around: its bibliography and licence were judged from the PeerJ PDF's printed byline, citation line and licence line. PMC, DOAJ, Plazi, bionames, ouci, optimap, reviewer.ly, ebusca.uv.mx, library catalogues and repository copies were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 7 WebSearches.

## Bibliographic and licence

- Line 1 (Fiorentino, Tocora, Ramirez 2022). Byline, citation line "Fiorentino G, Tocora MC, Ramirez S (2022) ... ZooKeys 1108: 1-9" and Crossref agree in order; title identical; no issue; issued 2022-06-23. Page "Creative Commons Attribution License (CC BY 4.0)"; Crossref CC BY 4.0 vor. Accepted.
- Lines 2, 3 (Asenjo, Valois, Zampaulo, Molina, Oliveira, Oliveira, Vasconcelos 2024). Crossref unreadable (above). PDF byline "Angélico Asenjo, Marcely Valois, Robson de Almeida Zampaulo, Michele Molina, Renato R.M. Oliveira, Guilherme Oliveira and Santelmo Vasconcelos"; "How to cite" line "Asenjo A, Valois M, Zampaulo RA, Molina M, Oliveira RRM, Oliveira G, Vasconcelos S. 2024. ... PeerJ 12:e17783"; "Published 12 August 2024"; "Distributed under Creative Commons CC-BY 4.0". Authors, year, volume and article number right; title matches the page. The note's "Crossref CC BY 4.0 (content version unspecified)" could not be confirmed here, but the publisher's own free copy carries the CC BY 4.0 statement, which is enough. Accepted.
- Lines 4, 5 (Reyes-Puig, Wake, Kotharambath, Streicher, Koch, Cisneros-Heredia, Yánez-Muñoz, Ron 2020). The HTML returned no byline (copyright line "Reyes-Puig et al."); Crossref order as filed, as the note says. Title identical; "PeerJ 8:e9934"; issued 2020-10-02. Page "Creative Commons Attribution License"; Crossref CC BY 4.0 unspecified. Accepted.
- Line 6 (Chen, Hu, Pei, Yang, Yong, Xu, Qu, Onditi, Zhang 2022). Byline, citation line and Crossref agree; "ZooKeys 1083: 129-146"; issued 2022-01-25. Page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.
- Line 7 (Zhang, Yin 2022). Byline "Wen-Xuan Zhang and Zi-Wei Yin"; "Insects 2022, 13(2), 119"; Crossref volume 13, issue 2, 119, issued 2022-01-24. Page metadata CC BY 3.0, footer CC BY 4.0 (tool summary); Crossref CC BY 4.0 vor. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

- Metopiellus guanano, Syrbatus obsidian, S. superciliata, Batrisceniola nanlingensis: the pages print no Insecta/Coleoptera headings. Coleoptera, Staphylinidae (Pselaphinae) come from the titles; Syrbatus pages also print "Family Staphylinidae (Latreille, 1802)" and "Subfamily Pselaphinae". Family Staphylinidae, order Coleoptera, class blank: right.
- Oedipina: the page prints Plethodontidae only; "Caudata", "Urodela" absent and "Amphibia" only inside the citation "AmphibiaWeb, 2020" (tool check). Order and class blank: right.
- Chodsigoa dabieshanensis: Soricidae, Eulipotyphla, Mammalia from the title; right.
- All seven are described as new in their papers; no synonymy issue.

## Repeats

`git grep -il` on origin/main (095e055d8) over the whole docs/ tree for each species, each genus or epithet alone (Metopiellus, Syrbatus, Batrisceniola, dabieshanensis, villamizariorum, ecuatoriana) and each DOI (zookeys.1108.76077, peerj.17783, peerj.9934, zookeys.1083.78233, insects13020119): no hit except "ecuatoriana" as Phyllomedusa ecuatoriana in oa-2.jsonl (another species) and docs/views/gaps/gbif-names.tsv. Unmerged origin/research/ branches: see the last section.

## Per line

### Line 1, Metopiellus guanano, 12 ommatidia (holotype male)

Head paragraph of the holotype male: "Compound eyes small and slightly protruding laterally, composed of 12 ommatidia (Fig. 1F)." **Quote MATCH**, whole telegraphic sentence (preceded by the setae sentence, followed by the antennae sentence; tool summary for the neighbours), 13 words. Value keeps "per eye or both not stated". Type material: holotype male ICN 099808, Mitú-Monfort road km 16, Cucura, 10 Aug 2019, Winkler 48 h; paratype female ICN 099807, Villa Fatima, Pie de Cerro Tipiaca, 19 Mar 2020 (Winkler 40 h, not in conditions; trivial). Female description says head, pronotum and elytra match the male (tool summary), consistent with "refers back to the male". Diagnosis and Comments carry no eye text; key couplets "eyes absent", "eyes small or almost absent", "eyes small", "eyes almost absent" as conditions say.

**Line 1 MATCH.**

### Line 2, Syrbatus obsidian, 19 right and 20 left (holotype male)

Holotype description, Head: "Eyes composed of 19 (right side) and 20 (left side) ommatidia situated at posterior third of head length." **Quote MATCH**, whole sentence (preceded by "Anterior margin rounded and emarginated at middle, genal edge rounded and carinated."), 18 words. Sides kept apart, not totalled. "Type material (eight males, six females)."; holotype MPEG-01052553, cave FZ_0054, Catas Altas, 4 Sept 2019; 13 further specimens from FZ_0054, FZ_0053, FZ_0050, FZ_0049 (7 males, 6 females; three listed as molecular vouchers inside the type material; tool summary). Female description and Discussion carry no eye text; Discussion "the absence of evident troglomorphisms" and troglophile reading carried. S. moustache "Eyes composed of 13 ommatidia and situated at posterior third of head length." matches the conditions' contrast.

**Line 2 MATCH.**

### Line 3, Syrbatus superciliata, 10 right and 9 left (holotype male)

"Eyes composed of 10 (right side) and 9 (left side) ommatidia situated at posterior third of head length." **Quote MATCH**, whole sentence, 18 words. "Type material (one male, five females)."; holotype ISLA-110317, ABOB_0028, Nova Lima, 29 Apr 2019; five females from ABOB_0028 and ABOB_0015, two of them 1 Aug 2013 (tool summary). Diagnosis refers to S. moustache ("mustache" as printed there); no eye text in the female description.

**Line 3 MATCH.**

### Line 4, Oedipina villamizariorum, eyes moderate, dorsolateral (female holotype)

Description: "Eyes are moderate in size and dorsolaterally oriented; eyes extend beyond the lateral margins of the head (less evident in the preserved specimen)." Confirmed exact, semicolon included. **Quote MATCH**, 23 words; qualifier kept in value. Holotype DHMECN 14489, adult female, Quinshull, Chical, Carchi, 2 Aug 2017, 921 m; known from one specimen. Diagnosis "dorsolaterally oriented eyes that are moderate in size", O. maritima "(small laterally orientated)", O. berlini "with relatively large protruding eyes": carried. FHGO 9642 (Padre Santo, Esmeraldas, 130 m, 2000) is "similar to the holotype"; the authors think it is probably a third, undescribed species (tool summary). The conditions' "treated as O. aff. villamizariorum and is not described" is adequate; optional wording below.

**Line 4 MATCH.**

### Line 5, Oedipina ecuatoriana, eyes relatively small (male holotype)

Description: "Eyes are relatively small and dorsolaterally oriented; slightly extending beyond the lateral margins of the head." Confirmed exact. **Quote MATCH**, 16 words (the second clause lacks a subject as printed). Holotype BMNH 1901.3.29.115, male, "Paramba (Hacienda Parambas?, see Remarks section)", Imbabura, about 1,067 m, bought from W.F.H. Rosenberg: right. Diagnosis eye wording only in the O. berlini parenthetical: right.

Fault: **contrasting wording elsewhere omitted.** The Discussion says "The eyes of O. ecuatoriana are much more prominent than topotypic O. complex." (verbatim). A filed value of "relatively small" needs this relational statement beside it in the conditions; it is the only other eye statement on this species in the paper. One record error, fixable.

**Line 5 FIXABLE.**

### Line 6, Chodsigoa dabieshanensis, "Eyes are very small."

Description: "External ears are prominent, rounded, and covered with very short dark hairs." / "Eyes are very small." / "The dorsal surfaces of hands and hind feet ...". **Quote MATCH**, 4 words. Holotype "AHU2008FZL005, an adult female ... August 2020, at Foziling natural reserve (... 1187 m a.s.l.)"; paratypes "Ten specimens collected between May 2017 and August 2020 from the Dabie Mountains", sexes not stated; Figure 4 caption "(AHU2008FZL004; left)": all as conditions say. No other eye mention anywhere (tool check). Description basis not stated; Table 2 gives N = 11 for the species (tool summary), consistent with the conditions' hedge.

**Line 6 MATCH.**

### Line 7, Batrisceniola nanlingensis, about 30 ommatidia per eye (male)

Male Description: "Compound eyes prominent, each composed of approximately 30 ommatidia." Followed by "Antenna elongate, length 1.01–1.03 mm, lacking distinct club." **Quote MATCH**, 9 words; "approximately" kept in value; per eye ("each"), not a total. Holotype male, Pubuqun, 660–850 m, 3 May 2021; paratypes 15 males and 4 females from the holotype locality, Xiaohuangshan, Qinshui Valley, Guang-dong-di-yi-feng and Nanling N. R. Station (2008, 2020, 2021): right. Female: "each compound eye composed of approximately 25 ommatidia" inside a longer sentence: carried. Diagnosis no eye text: right.

Fault: **collecting method overstated.** Conditions say "all sifted leaf-litter samples". The holotype label reads "3.V.2021, sifting, Hu, Lin, Zhou and Li leg."; neither the Methods nor the type labels mention leaf litter, which the Discussion mentions only for Batrisini in general (tool summary). One record error, fixable.

**Line 7 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Metopiellus guanano, 12 ommatidia | MATCH | | whole sentence; per-eye ambiguity disclosed |
| 2 | Syrbatus obsidian, 19 R / 20 L | MATCH | | sides kept apart; holotype only |
| 3 | Syrbatus superciliata, 10 R / 9 L | MATCH | | sides kept apart; holotype only |
| 4 | Oedipina villamizariorum, eyes moderate | MATCH | | exact with semicolon; diagnosis contrasts carried |
| 5 | Oedipina ecuatoriana, eyes relatively small | FIXABLE | conditions | Discussion "much more prominent than topotypic O. complex" omitted |
| 6 | Chodsigoa dabieshanensis, eyes very small | MATCH | | only eye mention in the paper |
| 7 | Batrisceniola nanlingensis, about 30 per eye | FIXABLE | conditions | "leaf-litter" not printed; label says "sifting" only |

Errors: 2 of 7 records (28.6%); 2 fixable (lines 5, 7), 0 held out, 0 unfixable; no line to drop. Bibliographic and licence faults 0; repeats none. Verdict for lines 1 to 7: **ACCEPT AFTER REPLACEMENT** (lines 1 to 4 and 6 as filed; lines 5 and 7 with the replacements below, or dropped if not applied). Pooled verdict for desk-d311 rests with the merger across audits 409 to 415.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 5:
- `conditions`: "No statement on eye visibility in the preserved specimen is made for this species." -> "No statement on eye visibility in the preserved specimen is made for this species. The Discussion compares the eyes with another species: 'The eyes of O. ecuatoriana are much more prominent than topotypic O. complex.'"

Line 7:
- `conditions`: "2008 to 2021, all sifted leaf-litter samples." -> "2008 to 2021; the holotype label reads 'sifting' and no substrate is printed."

Optional, not counted:
- Line 4 `conditions`: "is treated as O. aff. villamizariorum and is not described." -> "is called similar to the holotype of O. villamizariorum; the authors think it probably a third, undescribed species, and it is not described."
