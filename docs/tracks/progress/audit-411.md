# audit-411: desk-d311, evidence file lines 15 to 21

Audited 1 November 2026 from the desk-d311 files present untracked in the worktree (docs/tracks/progress/desk-d311.md and docs/views/evidence/desk-d311.jsonl, 50 lines; neither committed here, neither edited). Six other auditors take lines 1-7, 8-14, 22-28, 29-35, 36-42 and 43-50. `python3 -I tools/senses/check.py | grep d311`: "docs/views/evidence/desk-d311.jsonl: 50 records, 0 problems". Quote lengths (`len(q.split())`) for lines 15 to 21: 12, 5, 5, 5, 7, 7, 15, all within 40.

Sources opened (WebFetch, every URL from a WebSearch result): zookeys.pensoft.net/article_preview.php?id=97346 (two passes), zookeys.pensoft.net/article/35465/download/xml/ (publisher's own XML, one pass), zookeys.pensoft.net/article_preview.php?id=3430 (two passes), zookeys.pensoft.net/article_preview.php?id=3442 (one pass). Crossref single-DOI lookups api.crossref.org/v1/works/ for 10.3897/zookeys.1182.97346, 10.3897/zookeys.859.35465, 10.3897/zookeys.346.6233 and 10.3897/zookeys.251.4099, each read on the first call. PMC, GBIF, Plazi, BHL, DOAJ, library catalogue records (cas.cz, uitm.edu.my, utm.my, uv.mx) and species-id.net were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 4 WebSearches.

## Bibliographic and licence

- Lines 15 to 18 (Yeon-Jae Choi, Sun-Jae Park, Seung-Gyu Lee, Jong-Seok Park 2023). Byline and Crossref identical in order; title identical; "ZooKeys 1182: 165–181"; Crossref volume 1182, no issue, pages 165-181, issued 2023-10-13. Page prints the CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted. The page has no Order/Family line; it prints a classification block from Subfamily Pselaphinae down (Supertribe Goniaceritae, Tribe Bythinini, Genus Bryaxis) (tool summary), so the notes' "The page prints no classification block" is slightly off; order and family from the title are right. Optional fix, not counted.
- Line 19 (Qing-Hao Zhao, Wang Xu, Zi-Wei Yin 2019). Byline and Crossref identical; title identical; ZooKeys 859: 63–68; Crossref issued 2019-07-02, no issue. Page prints "Creative Commons Attribution License (CC BY 4.0)"; Crossref CC BY 4.0 vor. Classification Coleoptera (Order), Staphylinidae (Family), Pselaphinae as the note says. Accepted.
- Line 20 (Zi-Wei Yin, Li-Zhen Li 2013). Byline and Crossref identical; title identical; "ZooKeys 346: 23–27"; Crossref issued 2013-11-01, no issue. Page prints "Creative Commons Attribution License 3.0 (CC-BY)"; Crossref CC BY 3.0 vor. Order Coleoptera, Family Staphylinidae, Subfamily Pselaphinae printed. Accepted.
- Line 21 (Zi-Wei Yin, Li-Zhen Li 2012). Byline and Crossref identical; page title "Notes on Michael Schülke’s pselaphine collections from China. – Tyrini. I. genera Labomimus Sharp, Linan Hlaváč and Pselaphodes Westwood (Coleoptera, Staphylinidae, Pselaphinae)"; the record has a straight apostrophe, typographic only, as the note says. "ZooKeys 251: 83–118"; Crossref issued 2012-12-18; CC BY 3.0 page and Crossref vor. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout; class blank right (no class printed on any of the four pages).

## Repeats

`git grep -il` on origin/main over the whole docs/ tree (evidence, audit/corrected, audit/ALL, sheets, searched, tracks, gaps) for "Bryaxis uljinensis", "Bryaxis fabaiformis", "Bryaxis girinensis", "Bryaxis nemorosus", uljinensis, fabaiformis, girinensis, nemorosus, qiniangmontis, "Tangius indicus", Tangius, "Labomimus cognatus", and the four DOIs: no hit except 10.3897/zookeys.251.4099 once, in desk-d302 line 2 (Linan tendothorax, a different species from the same paper). "Labomimus" on main appears only as "Labomimus Sharp"; "cognatus" only as Anaxyrus and Sphex. Unmerged origin/research/desk-d29* to d31* branches (24 refs, excluding d311): every docs/ file each changes against main searched for the species and DOIs; only desk-d302's own copy of the Linan tendothorax line. No repeats.

## Per line

### Line 15, Bryaxis uljinensis, 32-34 facets

Description: "Eyes large, longer than twice that of tempora, composed of 32–34 facets." Previous sentence "Vertex convex; longitudinal carina present; vertexal foveae small."; next begins "Maxillary palpi moderately developed; ...". **Quote MATCH**, whole sentence, 12 words. No sex label on the Description (it opens "Body reddish brown, ... length 1.25–1.31 mm", so it spans more than one specimen); Sexual dimorphism: "Female eyes slightly longer than tempora, composed of 15 facets; antennal pedicels simple; protibial spines and metatibial spines absent." So the Description is the male by contrast, and the note's inference holds here. Type material 4 males, 3 females: holotype male Onjeong-myeon, Uljin-gun, 8 Jun 2019; paratypes 2 males (Gujeol-ri, 24 Apr 2020, "sifting leaf & soil litter") and 1 male, 3 females ("sifting ant colony, leaf & soil litter"). Conditions right (the two leaf-litter males are not described but the count of 6 is right). Remarks do not mention eyes.

**Line 15 MATCH.**

### Line 16, Bryaxis fabaiformis, 31-32 facets

Description: "Eyes large with 31–32 facets." Before: "Vertex weakly convex; longitudinal carina distinct; vertexal foveae enlarged."; after "Maxillary palpi moderately developed; ...". **Quote MATCH**, 5 words. Sexual dimorphism: "Female eyes slightly shorter than tempora, comprising 9 facets; antennal pedicels without modification; metatibial spines absent." Male inference holds. Type material 3 males, 1 female, Gujeol-ri, 24 Apr 2020: right. Remarks "having a rounded tempora as long as the eyes (Fig. 6E)" (a comparison; consistent with "Eyes large"); optional addition below.

**Line 16 MATCH.**

### Line 17, Bryaxis girinensis, 34 facets

Description: "Eyes large with 34 facets." **Quote MATCH**, 5 words. Single male holotype (Bangdong-ri, Girin-myeon, Inje-gun, 23 Jun 2009); Sexual dimorphism "Unknown." Value, eye and conditions right: the count rests on the one male.

Fault (one record error, fixable): the **note misstates the page**. It says the eye sentence "is read as the male because the holotype is a male and a separate 'Sexual dimorphism' paragraph gives the female eyes", but here that paragraph reads only "Unknown." (as the record's own conditions say). The basis for "male" is the single male specimen.

**Line 17 FIXABLE.**

### Line 18, Bryaxis nemorosus, 9 facets

Description: "Eyes reduced with 9 facets." **Quote MATCH**, 5 words. Type series 4 males, 1 female (holotype Mt. Doksil, Gageo island, 13 Jul 2021; paratypes 1 male 13 Jul 2021, 2 males 8 Jul 2020, 1 female 7 Jul 2020): conditions right. Diagnosis "Elongated head with small eyes situated on mid-length of head (Fig. 8E, arrow)." carried (the conditions drop the figure reference without a cut mark; optional fix).

Fault (one record error, fixable): **sex not stated as the page states it.** The `eye` field files the count as male "by the layout of the Description", and the note says a 'Sexual dimorphism' paragraph gives the female eyes. For this species the paragraph reads only "Female metatibial spines absent." (verbatim). The Description carries no sex label, and the only difference the page names between the sexes is the metatibial spines, so the page does not restrict the 9-facet count to males; the layout inference the unit used for lines 15 and 16 has no footing here. Remarks ("angular tempora much longer than the eyes (Fig. 9F)") and Discussion ("small eyes", "reduced eye sizes") are consistent with the value and may be added (optional).

**Line 18 FIXABLE.**

### Line 19, Linan qiniangmontis, female about 18 facets

Female paragraph: "Similar to male in general morphology, with slightly shorter antennae and smaller eyes; ..." then "Eyes each composed of approximately 18 facets." **Quote MATCH**, whole sentence, 7 words. Male: "Head longer than wide, length from clypeal anterior margin to head base 0.52–0.54 mm, width across eyes 0.48–0.49 mm; eyes small, each composed of ca. 23 facets." (the conditions call it a clause in a longer sentence: right). Holotype male Mt. Qiniang, Shenzhen, 23.III.2019; paratypes 1 male, 3 females, same label data: right. Diagnosis and Comparative notes do not mention eyes: right. Value "approximately" preserved; per eye ("each") right.

**Line 19 MATCH.**

### Line 20, Tangius indicus, male about 35 facets

Male description: "Each eye composed of about 35 facets." Before: "Antennomeres II–X (Fig. 2A) each subcylindrical, apical antennomeres nearly oval, enlarged."; after "Pronotum about as long as wide, PL 0.62–0.63 mm, ...". **Quote MATCH**, 7 words. Type material: holotype "INDIA, Meghalaya, Khasi Hills, 28.X, Mawphlang, 1800 m, Besuchet-Löbl, 78"; paratypes 4 males, 3 females same data and 1 female "INDIA: Darjeeling, distr., 13 km N. Ghoom, 1500 m, 15.X.1978, I. Löbl, Bes. nr. 15, litter"; stated totals 6 males, 3 females against an itemised 5 and 4: conditions right. "West Bengal" is not printed (geographically right; optional). Diagnosis and Comparative notes have no eye text: right.

Not counted: the conditions say "the Female description does not address the eyes". It opens "Identical to male except antennomeres shorter, and mesotibiae lacking distal concavity and preapical tooth.." (printed double stop), which by implication extends the eye count to females. The value stays restricted to the male as quoted, so this under-states rather than over-states; optional fix below.

**Line 20 MATCH.**

### Line 21, Labomimus cognatus, male about 40 facets

Male description, after "Length 3.18–3.41.": "Head longer than wide, HL 0.71–0.78, HW 0.65–0.71; eyes each composed of about 40 facets." **Quote MATCH**, whole sentence including the head dimensions, 15 words. Female: "Eyes each composed of about 27 facets." carried. Diagnosis and Comparative notes have no eye text.

Fault (one record error, fixable): **paratype data misstated.** Conditions put all 5 paratypes at "Gaoligong Shan localities, Aug. 2009". The page lists paratype 1 as a male with the holotype's data (Xiaoheishan N.R., 35 km SE Tengchong, 2110 m, 30 May 2007, SNUC); the other four (1 male, 3 females) are from the Gaoligong Shan W pass, 32-35 km SE Tengchong, 1600-2100 m, 25-28 Aug 2009 (M. Schülke, D.W. Wrase). Totals (3 males, 3 females) right.

**Line 21 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 15 | Bryaxis uljinensis, 32-34 facets | MATCH | | female 15 facets in Sexual dimorphism, so male inference holds |
| 16 | Bryaxis fabaiformis, 31-32 facets | MATCH | | female 9 facets in Sexual dimorphism |
| 17 | Bryaxis girinensis, 34 facets | FIXABLE | note | note says the Sexual dimorphism paragraph gives female eyes; page prints "Unknown." |
| 18 | Bryaxis nemorosus, 9 facets | FIXABLE | eye, note | filed as male, but the Sexual dimorphism paragraph names only female metatibial spines; page does not restrict the count to males |
| 19 | Linan qiniangmontis, female about 18 facets | MATCH | | whole Female sentence; male ca. 23 carried |
| 20 | Tangius indicus, male about 35 facets | MATCH | | type-count mismatch recorded; optional female-identity fix |
| 21 | Labomimus cognatus, male about 40 facets | FIXABLE | conditions | one male paratype has the holotype's 2007 data, not Aug. 2009 |

Errors: 3 of 7 records (42.9%); 3 fixable (lines 17, 18, 21), 0 held out, 0 unfixable; no line to drop. Repeats: none. Bibliography and licences: no faults. Telegraphic sentences: every quote is a whole printed sentence, none cut from a longer one; "about"/"approximately"/ranges preserved in values. Verdict for lines 15 to 21 of desk-d311: **ACCEPT AFTER REPLACEMENT** (lines 15, 16, 19, 20 as filed; lines 17, 18, 21 with the replacements below, or dropped if they are not applied).

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 17:
- `note`: "a separate 'Sexual dimorphism' paragraph gives the female eyes, which is an inference from the layout." -> "the species is known only from that male (the 'Sexual dimorphism' paragraph reads 'Unknown.'), so the count is the male holotype's."

Line 18:
- `eye`: "eyes, male (by the layout of the Description; see note)" -> "eyes (species Description, no sex label; type series 4 males, 1 female; the page does not restrict the count to one sex)"
- `note`: "a separate 'Sexual dimorphism' paragraph gives the female eyes, which is an inference from the layout." -> "for this species the 'Sexual dimorphism' paragraph reads only 'Female metatibial spines absent.', so the page names no eye difference between the sexes and the count is not filed as male-only."
- `conditions`: "The 'Sexual dimorphism' paragraph does not mention female eyes." -> "The 'Sexual dimorphism' paragraph reads only 'Female metatibial spines absent.', so the page names no sex difference in the eyes. The Remarks give 'angular tempora much longer than the eyes (Fig. 9F)' and the Discussion speaks of 'small eyes' and 'reduced eye sizes'."

Line 21:
- `conditions`: "5 paratypes (2 males, 3 females; Gaoligong Shan localities, Aug. 2009)" -> "5 paratypes (1 male with the holotype's data, 30 May 2007; 1 male and 3 females from the Gaoligong Shan W pass, 32-35 km SE Tengchong, 1600-2100 m, 25-28 Aug. 2009)"

Optional, not counted:
- Lines 15 and 16 `note`: "The page prints no classification block;" -> "The page prints no Order or Family line (its classification block starts at Subfamily Pselaphinae);"
- Line 16 `conditions`: append " The Remarks compare it as 'having a rounded tempora as long as the eyes (Fig. 6E)'."
- Line 18 `conditions`: "'Elongated head with small eyes situated on mid-length of head'" -> "'Elongated head with small eyes situated on mid-length of head (Fig. 8E, arrow)'"
- Line 20 `conditions`: "the Female description does not address the eyes." -> "the Female description opens 'Identical to male except antennomeres shorter, and mesotibiae lacking distal concavity and preapical tooth..' and does not mention the eyes separately."
- Line 20 `conditions`: "1 female from Darjeeling district, West Bengal" -> "1 female from Darjeeling district, 13 km N Ghoom"
