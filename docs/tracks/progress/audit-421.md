# audit-421: desk-d315, evidence lines 1 to 8

Audited 1 November 2026 from the desk-d315 files present untracked in the worktree (docs/tracks/progress/desk-d315.md and docs/views/evidence/desk-d315.jsonl; neither committed here, neither edited). Lines 9 to 24 go to two other auditors. Branch research/audit-421 from origin/main (2bb4cdea5). `python3 -I tools/senses/check.py | grep d315`: "docs/views/evidence/desk-d315.jsonl: 24 records, 0 problems". Quote lengths (`len(q.split())`) for lines 1 to 8: 8, 15, 22, 22, 6, 4, 7, 22, all within 40.

Sources opened (WebFetch, every page URL from a WebSearch result): zookeys.pensoft.net/article/9771/download/xml/ (two passes), zookeys.pensoft.net/article/7628/download/xml/, zookeys.pensoft.net/article_preview.php?id=136907, zookeys.pensoft.net/article_preview.php?id=27193 (two passes), zookeys.pensoft.net/article_preview.php?id=94545&skip_redirect=1 (four passes), mdpi.com/2075-4450/14/7/614 (three passes), dermaptera.speciesfile.org/otus/948156/overview. Crossref single-DOI lookups api.crossref.org/v1/works/ for all six DOIs (10.3897/zookeys.626.9771 rate-limited on the first call, read on the retry). PMC, DOAJ, plazi, library catalogue records (utm.my, uitm.edu.my, uv.mx, ufrj.br, kab.ac.ug), omicsdi, core.ac.uk, reviewer.ly and GBIF were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns pieces of at most about 125 characters; the MDPI page refused to return the Ekpagloderma sentence verbatim and was then asked to compare it against the filed string, which it confirmed character for character (tool comparison, not a verbatim return). 6 WebSearches.

## Bibliographic and licence

- Line 1 (Feng, Notton, Xu 2016). XML contributor order Jun Feng, David Notton, Zai-fu Xu; Crossref order Xu, Feng, Notton; record follows the byline. The XML citation line prints "Feng J, Notton D, Xu X-f (2016)" (a printed slip against the byline "Zai-fu Xu"); "Xu Z-f" is right and the note discloses it. Title verbatim; ZooKeys 626: 57-65, no issue; Crossref issued 2016-10-20. XML prints "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),"; Crossref CC BY 4.0 vor. Accepted.
- Line 2 (Hou, Xu 2016). Citation line "Hou Z, Xu Z-f (2016) ... ZooKeys 574: 97–104."; byline Zi Hou, Zai-fu Xu; Crossref Xu, Hou (byline wins, record right). Title verbatim with "Förster, 1856". CC BY 4.0 sentence printed; Crossref CC BY 4.0 vor. Accepted.
- Line 3 (Li, Liu, Chen, Wei, Yue, Qiu 2025). Byline and Crossref identical in order ("De-yi Qiu" lower-case y, as filed). ZooKeys 1232: 267-284, issued 2025-03-19. CC BY 4.0 sentence printed; Crossref vor CC BY 4.0. Accepted.
- Line 4 (Kamimura, Ferreira 2018). Byline and Crossref identical. Title verbatim. ZooKeys 790: 87-100, issued 2018-10-15. CC BY 4.0 sentence printed; Crossref vor. Accepted.
- Lines 5 to 7 (Rodrigues, Crumière, Toubiana, Khila, Moreira 2022). Byline and Crossref identical in order. Title verbatim. ZooKeys 1126: 155-199, issued 2022-11-01. CC BY 4.0 sentence printed (on the preview page); Crossref vor. Accepted.
- Line 8 (Yin, Shih, Engel, Ren 2023). Byline and Crossref identical. Title verbatim (the page title carries a dagger footnote mark, not part of the title). Citation "Insects 2023, 14(7), 614"; Crossref 14, issue 7, issued 2023-07-07. No licence sentence in the visible text; page metadata CC BY 3.0; Crossref CC BY 4.0 vor: accepted under the CC BY 3.0 page / CC BY 4.0 Crossref ruling.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

- Calogalesus sinicus, Monelata truncata: taxon classification blocks print Animalia, Hymenoptera, Diapriidae; no class. Right.
- Nocticola baiguensis: title prints "(Blattodea, Corydioidea, Nocticolidae)", headings "Family Nocticolidae"; no class printed, so blank is right (desk-d297 filed Insecta for the two sister species from this page; not this unit's fault).
- Mesodiplatys falcifer: classification block "Order DERMAPTERA", "Family DIPLATYIDAE"; Insecta from the title "(Insecta, Dermaptera)". Right.
- Rhagovelia depressa, R. tantilloides, Steinovelia vittata: title prints Insecta, Hemiptera; Veliidae from the treatment headings. Right. All three are new in this paper (authority "Rodrigues, Khila & Moreira"); no later synonymy found.
- Ekpagloderma gracilentum: Results heading Family Semenoviolidae; Introduction says Bellodermatidae (disclosed). Dermaptera Species File lists it as valid, Semenoviolidae, Aglyptodermatinae, under Dermaptera and Insecta. The page prints no class heading ("Order Dermaptera de Geer, 1773" opens the systematics); blank is right.

## Repeats

`git grep -n -i -E` on origin/main (2bb4cdea5) over the whole docs/ tree for Calogalesus, "Monelata truncata", "Nocticola baiguensis", baiguensis, "Mesodiplatys falcifer", "Rhagovelia depressa", "Rhagovelia tantilloides", tantilloides, Steinovelia, Ekpagloderma and the six DOIs. Hits: desk-d297.jsonl lines 3 and 4 (Nocticola appendiculata and N. cordiformis, same DOI, different species, eye_type), desk-d297.md line 17 (N. baiguensis listed as a dropped candidate, no value filed) and audit-388.md (a grep list naming the sister species). None repeats a line here. Unmerged origin/research/desk-d* branches other than d315: see the closing paragraph of this section.

Unmerged branches: the 314 origin/research/desk-d* branches other than d315 that are not merged into origin/main, grepping with the same pattern only the docs/ files each branch changes against origin/main (a full-tree loop over every branch first returned only copies of desk-d297.jsonl, desk-d297.md and audit-388.md inherited from main). Hits: origin/research/desk-d297 (desk-d297.md and desk-d297.jsonl, the same Nocticola sister-species records and dropped-candidate note that are on main). No other branch carries any of the eight species or six DOIs.

## Per line

### Line 1, Calogalesus sinicus, eyes oval, slightly bulging, sparse hairs

Female description (heading "Female (Figs 1–4)." followed by "Holotype."), Head: "Eyes oval, slightly bulging laterally, with sparse hairs." Before: "Clypeus highly convex."; after: "Malar sulcus distinct." **Quote MATCH**, whole telegraphic sentence, 8 words. Value says no more than the quote. Holotype "Holotype, ♀: CHINA: Yunnan, Zhaotong, Huanghua town (N27°59', E103°33'), 10.VIII.2012, Shi-wen Yang leg."; paratypes 16 ♀♀ and 37 ♂♂, "10.VIII–26.X.2012"; Materials and methods "13 female and 34 male paratypes": all as in conditions. Male: "Other characteristics as for females." Key: "mandible distinctly shorter than eye height (1.0:2.0)" (conditions describe it correctly). One inaccuracy, not counted: the conditions call 'Eye 1.5 times as long as wide, 2.5 times as long as malar space.' "the next sentence"; it is five sentences later in the same Head paragraph (after the Antenna sentence). Optional fix below.

**Line 1 MATCH.**

### Line 2, Monelata truncata, eye oval, 1.5 x as long as wide

"Holotype. Female (Figs 1–3)." Head: "Eye oval, 1.5 times as long as wide, 1.5 times as long as malar space." then "Posterior orbit of eye not sinuate." **Quote MATCH**, 15 words. Holotype "Holotype: ♀, CHINA: Yunnan, Zhaotong, Yongshan, Huanghua, 2012.VIII–X, Shi-wen Yang (SCAU)."; paratypes "22 ♀♀ 35 ♂♂", same data. Male "Eye 1.4 times as long as wide, 2.3 times as long as malar space." carried. Diagnosis and Remarks have no eye wording (read). Right.

**Line 2 MATCH.**

### Line 3, Nocticola baiguensis, eyes reduced to a few ommatidia

Male description: "Head: vertex of head exposed; eyes reduced to a few ommatidia narrowly grouped near antennal sockets (Fig. 3F);" / "ocelli absent (Fig. 3F)." **Quote MATCH**, 22 words, whole sentence with its label (desk-d297 precedent). Diagnosis "It can be distinguished by its eyes reduced to a few ommatidia narrowly grouped near antennal sockets (Fig. 3D), while in N. baumi, N. bolivari, and N. cockingi eyes are absent." carried. Holotype "1 ♂; ... Wangjia Village, Baigu Cave; ... 1 November 2023, Hao-fei Fan leg; ZSCTC-LI0001."; paratypes 9 ♂, 8 ♀, 6 nymphs (14 March 2024), 1 ♂ Guilin National Forest Park (18 March 2024), 1 ♂ and 1 ♀ Baiyun Temple (28 March 2024): as in conditions. Female "Apterous (Fig. 4C, D)." with no eye sentence: right.

**Line 3 MATCH.**

### Line 4, Mesodiplatys falcifer, eyes conspicuously prominent, EL/POL 2.5

"Eyes conspicuously prominent, eye length 2.5 times the post-ocular length" / "(EL/POL, measured along anterior-posterior axis as shown in Figure 1; Table 2)." **Quote MATCH**, 22 words. Holotype ♂ only, Lapa dos Peixes II, Carinhanha, Bahia, "15.x.2017", "Ferreira R.L. leg.", ISLA 46682; "Female. Unknown."; "Three nymphs, possibly Mesodiplatys falcifer sp. n., were also found near the holotype collection site."; "located around 700 m from the entrance". Diagnosis "notably large eyes", Remarks "eyes notably longer than POL (Table 2)" and M. insularis "only 1.6 times the POL", key couplet 6: all carried. The Remarks' "single paratype female of this species" belongs to M. insularis (Figs 15–20), not to this species; the conditions are right to say no paratypes.

**Line 4 MATCH.**

### Line 5, Rhagovelia depressa, eyes not distinctly large, touching pronotum

"Head compact." then "Eyes not distinctly large, touching pronotum." **Quote MATCH**, 6 words. Holotype "apterous ♂ holotype; Réserve Naturelle Nationale des Nouragues, Camp Pararé and surroundings; 4.0386, –52.6728; 17–18 Oct. 2016; A.J.J. Crumière, A. Khila, F.F.F. Moreira, W. Toubiana leg.; CEIOC 82144"; "42 apterous ♂ paratypes, 32 apterous ♀ paratypes; same, except CEIOC 82145.": as in conditions. Female: no eye sentence, measurement "EYE 0.27–0.30".

Fault: **eye wording elsewhere denied.** The conditions say "The Comments (diagnostic features 1-13) do not mention eyes." The Comments open "Rhagovelia depressa Rodrigues, Khila & Moreira, sp. nov. belongs to the angustipes complex based on the pronotum of the apterous form shorter than the dorsal length of the eye, with the posterior margin concave.", and the male thorax reads "Pronotum shorter than dorsal eye length, with posterior margin slightly concave." Both relate eye length to the pronotum, which bears on how "not distinctly large" should be read. One record error, fixable.

**Line 5 FIXABLE.**

### Line 6, Rhagovelia tantilloides, eyes large, touching pronotum

"Head compact. Eyes large, touching pronotum." **Quote MATCH**, 4 words. Value right.

Faults (one record error, fixable): (a) **holotype data not read and replaced by inference.** The page prints the holotype entry with bracketed data: "French Guiana • apterous ♂ holotype; [unspecified locality]; [Oct. 2016];" / "[A.J.J. Crumière, A. Khila, F.F.F. Moreira, W. Toubiana leg.]; CEIOC 82141" (asked twice; the second pass confirmed the square brackets are printed, not tool placeholders). The conditions instead say the data were not read and that "the other types of the series were collected 17-18 Oct. 2016 in the Nouragues reserve", which the page does not say: the first paratype entry is "2 apterous ♂ paratypes, 3 apterous ♀ paratypes; same, except CEIOC 82143", so those share the holotype's unspecified locality, and only the second entry (2 ♀, near Cayenne, 21 Oct. 2016, CEIOC 82142) has a locality. (b) **eye wording elsewhere denied.** "The Comments do not mention eyes." is wrong: "Rhagovelia tantilloides Rodrigues, Khila & Moreira, sp. nov. is part of the angustipes complex based on the pronotum of the apterous form shorter than the dorsal eye length with the posterior margin slightly concave."; the male thorax also has "Pronotum shorter than dorsal eye length, with posterior margin slightly concave." Female measurement "EYE 0.30–0.32" with no eye sentence; Comments note "the absence of macropterous individuals".

**Line 6 FIXABLE.**

### Line 7, Steinovelia vittata, eye shining dark red, without ocular setae

Before: "Remaining portion of antennomere II brown, covered by short curved brown setae only."; "Eye shining, dark red, without ocular setae." **Quote MATCH**, 7 words. Holotype "macropterous ♂ holotype; Réserve Naturelle Nationale des Nouragues, Camp Inselberg; 4.0892, –52.6772; 16 Oct. 2016," ... "CEIOC 82140."; no paratypes. "Posterior margin of eye distant from pronotum by ~ 22% of dorsal eye length." and Comments "2) ocular setae absent (Fig. 19A, C);" carried. eye_type fit: colour plus the absence of ocular setae (a surface structure of the eye) is a morphological eye state; accepted, though the colour half alone would not be. The male Head also has "Antenniferous tubercles swollen, almost half as wide as eye (~ 43%)" (optional).

**Line 7 MATCH.**

### Line 8, Ekpagloderma gracilentum (fossil), compound eyes large and prominent

Description, Head: the filed sentence "Compound eyes large and prominent, located near posterior margin of head, compound eye length 0.41 mm, interocular distance 0.55 mm; ocelli absent." was confirmed by the tool as exact, one full stop (tool comparison; the opening "Compound eyes large and prominent, located near posterior margin of head," was returned verbatim). 22 words. It describes the fossil's own eye, not a comparison. Holotype "Holotype. A completely preserved female, CNU-DER-NN2023001C/P, deposited in the College of Life Sciences, Capital Normal University, Beijing, China."; "Adult female, preserved in both dorsal and ventral aspects."; "Jiulongshan Formation (Middle Jurassic)"; Daohugou Village, Wuhua Township, Ningcheng County, Inner Mongolia. Genus Diagnosis "Compound eyes large and situated at posterior temples; ocelli absent (as in Aglyptodermatinae)." carried. Formation and age stated; eye_type fits.

Fault: **specimen state not as printed.** The conditions say the holotype is "(part and counterpart; preservation type not stated in the text)". The holotype entry does not say part and counterpart (the phrase is printed for the paratype of Applanatiforceps angustus, "CNU-DER-NN2023003C/P (part and counterpart; Figure 5)"), and the preservation the page does state ("preserved in both dorsal and ventral aspects") is omitted. One record error, fixable. Neither "compression" nor "impression" is printed, so "preservation type not stated" may stay.

**Line 8 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Calogalesus sinicus, eyes oval, bulging, sparse hairs | MATCH | | whole sentence; "next sentence" misplacement optional |
| 2 | Monelata truncata, eye oval, 1.5 x | MATCH | | as printed; male ratios carried |
| 3 | Nocticola baiguensis, eyes reduced to a few ommatidia | MATCH | | whole labelled Head sentence; types right |
| 4 | Mesodiplatys falcifer, eyes conspicuously prominent | MATCH | | holotype only; insularis contrast carried |
| 5 | Rhagovelia depressa, eyes not distinctly large | FIXABLE | conditions | Comments and thorax relate pronotum to eye length; conditions say Comments do not mention eyes |
| 6 | Rhagovelia tantilloides, eyes large | FIXABLE | conditions, note | printed bracketed holotype data not given, Nouragues inference unsupported; Comments eye wording denied |
| 7 | Steinovelia vittata, eye dark red, no ocular setae | MATCH | | as printed; setae absence makes it an eye-structure state |
| 8 | Ekpagloderma gracilentum, compound eyes large, prominent | FIXABLE | conditions | "part and counterpart" printed only for another species; "preserved in both dorsal and ventral aspects" omitted |

Errors: 3 of 8 records (37.5%); 3 fixable (lines 5, 6, 8), 0 held out, 0 unfixable; no line to drop. Repeats: none. Bibliography, licences and higher taxa right. Verdict for lines 1 to 8 of desk-d315: **ACCEPT AFTER REPLACEMENT** (lines 1 to 4 and 7 as filed; lines 5, 6 and 8 with the replacements below, or dropped if they are not applied). Pool with the audits of lines 9 to 16 and 17 to 24 for the unit verdict.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 5:
- `conditions`: "The Comments (diagnostic features 1-13) do not mention eyes." -> "The Comments place the species in the angustipes complex 'based on the pronotum of the apterous form shorter than the dorsal length of the eye, with the posterior margin concave', and the male thorax reads 'Pronotum shorter than dorsal eye length, with posterior margin slightly concave.' The apterous female measurement table gives 'EYE 0.27–0.30'."

Line 6:
- `conditions`: "(the tool returned the holotype locality and date line only as placeholders, so locality and date were not read from the page; the other types of the series were collected 17-18 Oct. 2016 in the Nouragues reserve and 21 Oct. 2016 near Cayenne)" -> "(the page prints the holotype data in square brackets: '[unspecified locality]; [Oct. 2016]; [A.J.J. Crumière, A. Khila, F.F.F. Moreira, W. Toubiana leg.]'; the first paratype entry is 'same, except CEIOC 82143', so those five share the holotype's unspecified locality)"
- `conditions`: "The Comments do not mention eyes." -> "The Comments place the species in the angustipes complex 'based on the pronotum of the apterous form shorter than the dorsal eye length with the posterior margin slightly concave', and the male thorax reads 'Pronotum shorter than dorsal eye length, with posterior margin slightly concave.' The apterous female measurement table gives 'EYE 0.30–0.32'; the Comments note 'the absence of macropterous individuals'."
- `note`: "Weak spot: holotype locality and date not read. " -> "Holotype locality and date are printed in square brackets as unspecified (audit-421). "

Line 8:
- `conditions`: "(part and counterpart; preservation type not stated in the text), a completely preserved female," -> "(the holotype entry does not say part and counterpart; neither compression nor impression is printed), a completely preserved female ('Adult female, preserved in both dorsal and ventral aspects.'),"

Optional, not counted:
- Line 1 `conditions`: "The next sentence of the female Head reads 'Eye 1.5 times as long as wide, 2.5 times as long as malar space.'" -> "Later in the female Head paragraph (after the Antenna sentence): 'Eye 1.5 times as long as wide, 2.5 times as long as malar space.'"
