# audit-410: desk-d311, file lines 8 to 14

Audited 1 November 2026 from the desk-d311 files present untracked in the worktree (docs/tracks/progress/desk-d311.md and docs/views/evidence/desk-d311.jsonl, 50 lines; neither committed here, neither edited). This audit covers file lines 8 to 14 only; six other auditors take the rest. Worktree /tmp/aud410, branch research/audit-410 from origin/main. `python3 -I tools/senses/check.py | grep d311`: "docs/views/evidence/desk-d311.jsonl: 50 records, 0 problems". Quote lengths (`len(q.split())`), lines 8 to 14: 9, 10, 9, 9, 9, 7, 8, all within 40.

Sources opened (WebFetch, every URL from a WebSearch result): www.mdpi.com/2075-4450/13/2/119; zookeys.pensoft.net/article_preview.php?id=81076 and zookeys.pensoft.net/article/81076/download/xml/; zookeys.pensoft.net/article_preview.php?id=110478; zookeys.pensoft.net/article_preview.php?id=3588 and zookeys.pensoft.net/article/3588/download/xml/; zookeys.pensoft.net/article_preview.php?id=97346. Crossref single-DOI lookups (api.crossref.org/v1/works/) for the five DOIs, each read on the first call. PMC, DOAJ, Plazi, Zenodo, BHL, GBIF, library catalogues (cas.cz, nu.edu.sa, uv.mx, utm.my, jioinstitute) and reviewer.ly results were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 5 WebSearches.

## Bibliographic and licence

- Line 8 (Zhang W-X, Yin Z-W 2022). Byline "Wen-Xuan Zhang and Zi-Wei Yin", Crossref identical in order; title identical; page "Insects 2022, 13(2), 119"; Crossref issued 2022-01-24, vol 13 issue 2 article 119. Page prints the MDPI "Creative Commons Attribution (CC BY) license" sentence; Crossref CC BY 4.0 vor. Accepted.
- Line 9 (Feng T, Yin Z-W 2022). Byline Ting Feng, Zi-Wei Yin; Crossref identical; title identical; "ZooKeys 1095: 75-81"; issued 2022-04-13; no issue. Page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.
- Lines 10 to 12 (Zhang Y-Q, Yin Z-W 2023). Byline Yong-Qin Zhang, Zi-Wei Yin; Crossref identical; title identical; "ZooKeys 1179: 231-241"; issued 2023-09-12. Page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.
- Line 13 (Yin Z-W, Li L-Z 2013). Byline Zi-Wei Yin, Li-Zhen Li; Crossref identical; title identical ("gen. et sp. n., a remarkable myrmecophile (Staphylinidae, Pselaphinae, Batrisitae) from the Gaoligong Mountains"); "ZooKeys 326: 17–26"; issued 2013-08-22. Page "Creative Commons Attribution License 3.0 (CC-BY)"; Crossref CC BY 3.0 vor. Accepted.
- Line 14 (Choi Y-J, Park S-J, Lee S-G, Park J-S 2023). Byline and Crossref identical in order; title identical including "Löbl"; "ZooKeys 1182: 165–181"; issued 2023-10-13. Page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout. Journal fields use hyphens where the pages print en dashes in page ranges (326, 1182); the desk's existing records do the same, not counted.

## Names and higher taxa

- Physomerinus clavipes, Trisiniotus taoismus, Pseudophanias furcilobus, P. leigong, P. mulun, Bryaxis grandinodus: Coleoptera and Staphylinidae printed in each title; the Trisiniotus XML also carries Order Coleoptera, Family Staphylinidae; the Bryaxis page's classification block starts at Pselaphinae. Order and family right; class blank right (Insecta not printed). All are names described as new in the paper read, no later synonymy seen.
- Pengzhongiella daicongchaoi: **order left blank although the page prints it.** The note says the order was "not read as printed", but the keywords line prints "Coleoptera, Batrisini, taxonomy, new genus, new species, myrmecophily" (preview page and XML), and the XML subject group gives "Staphylinidae". A blank field the page prints is an error under the launch brief. Fixable.

## Repeats

`git grep -il` on origin/main over the whole docs/ tree for "Physomerinus clavipes", clavipes, insects13020119, Trisiniotus, taoismus, 1095.81076, Pseudophanias, furcilobus, leigong, mulun, 1179.110478, Pengzhongiella, daicongchaoi, 326.5933, "Bryaxis grandinodus", grandinodus, 1182.97346. Hits: "clavipes" only as Cucujus clavipes, Nephila clavipes and Leptopilina clavipes (other species); "leigong" only as Formosatettix leigongshanensis (desk-d307 progress, a different species). No other hit. Unmerged origin/research/desk-d* branches other than d311 grepped over docs/views/evidence, audit and sheets for the five species and five DOIs (result below).

All 310 origin/research/desk-d* branches other than d311 grepped in one `git grep -il -E` per branch over docs/views/evidence, docs/views/audit and docs/views/sheets for the five species and five DOIs: completed, no hits.

## Per line

### Line 8, Physomerinus clavipes, approximately 35 ommatidia per eye (male)

Male Description: "Compound eyes prominent, each composed of approximately 35 ommatidia." Preceded by the venter sentence ("... extending from opening anteriorly to mouthpart.") and followed by "Antenna elongate, length 0.97 mm, lacking distinct club; ...". **Quote MATCH**, whole telegraphic sentence, 9 words; "approximately" kept in the value; per eye kept. Type material: male holotype, "China: Guangxi, Guilin, Huaping N. R., ... 780 m, 18.VIII.2020, streamside, Qiu Lu leg."; paratype "1 ♀, same locality as holotype". Female: "each compound eye composed of approximately 30 ommatidia." inside a longer sentence, as conditions say. Conditions say "The Diagnosis does not mention eyes"; the male Diagnosis does name the eyes positionally ("with thin mediobasal carina extending from head base to anteriorly beyond level of posterior margin of eyes,"), with no eye state or count (optional wording fix, not counted).

**Line 8 MATCH.**

### Line 9, Trisiniotus taoismus, approximately 35 large ommatidia per eye (male)

Male Description: "Eyes greatly prominent, each composed of approximately 35 large ommatidia." Preceded by the gular fovea sentence and followed by "Antenna moderately elongate, length 0.94–0.97 mm, simple, ...". **Quote MATCH**, 10 words; "approximately" and "large" kept. Type material "(15 exx.)": holotype ♂ Mao Shan, Jurong City, Jiangsu, 140 m, 24.viii.2020, "leaf litter, sifted"; paratypes "6 ♂♂, 3 ♀♀, same data as that of holotype"; "1 ♂♂, 2 ♀♀" Yaji-shan 23.viii.2020; "2 ♀♀" nr. Wawu-shan 22.viii.2020. Conditions match (14 paratypes). Female "each compound eye composed of approximately 30 ommatidia" carried. Diagnosis and Comparative notes do not mention eyes. Methods "head width was measured across the eyes" only.

**Line 9 MATCH.**

### Line 10, Pseudophanias furcilobus, approximately 30 ommatidia per eye (male)

Description heading "Male." Eye sentence: "Eyes moderately prominent, each composed of approximately 30 ommatidia." Preceded by "... setose C-shaped sulci broad, clearly visible in dorsal view." and followed by "Maxillary palpi symmetric, ...". **Quote MATCH**, 9 words. Holotype ♂ Maolan N. R., Libo County, Guizhou, 850–890 m, 20.vii.2015; paratypes 1 ♀ same data, 1 ♂ and 1 ♀ Mulun N. R., Hechi City, Guangxi, 26.vii.2015. Female "each eye composed of about 30 ommatidia" inside the female paragraph's opening sentence. No Discussion; the key (males) has no eye couplet; Diagnosis silent on eyes. Conditions right.

**Line 10 MATCH.**

### Line 11, Pseudophanias leigong, approximately 18 ommatidia per eye (male holotype)

"Eyes weakly prominent, each composed of approximately 18 ommatidia." under "Male."; holotype only "(1 ex.)", female "Unknown." **Quote MATCH**, 9 words. Locality on the page "Leigong Mt, Xiannütang., ... 1550 m, 3.v.2021"; conditions spell it "Xiannutang" (diaeresis dropped; optional fix, not counted). Other-species counts in conditions agree with lines 10 and 12.

**Line 11 MATCH.**

### Line 12, Pseudophanias mulun, approximately 16 ommatidia per eye (male holotype)

"Eyes weakly prominent, each composed of approximately 16 ommatidia." under "Male."; holotype only "(1 ex.)", "Mulun N. R., ... 460 m, 27.vii.2015", female "Unknown." **Quote MATCH**, 9 words. Conditions right.

**Line 12 MATCH.**

### Line 13, Pengzhongiella daicongchaoi, about 32 facets per eye (female)

Female description: "Female (Fig. 1B)." "Similar to male in general." "Measurements: BL 2.13–2.18 mm, ... AW 0.69–0.74 mm." then "Each eye composed of about 32 facets." then "Antennae simple." **Quote MATCH**: a standalone telegraphic sentence, 7 words, "about" kept, sex stated by the section heading. Male clause "eyes moderately developed, each composed of about 40 facets" sits inside the long semicolon head sentence beginning "Head (Fig. 2A) as long as wide.", as conditions say. Type material "(6 ♂♂, 35 ♀♀)": holotype ♂ plus "5 ♂♂, 35 ♀♀, same label data as holotype", Baihualing, S. Gaoligong Mt., W. Yunnan, 1550–1600 m, 20.iv.2013, "nest of Odontomachus monticola"; host section "collected from a colony of Odontomachus monticola" that "nested inside a rotten fallen tree". Conditions right.

Fault: **order blank though printed** (see Names). One record error, fixable.

**Line 13 FIXABLE.**

### Line 14, Bryaxis grandinodus, 23–26 facets

Description heading reads only "Description"; the sentence "Eyes as long as tempora, with 23–26 facets." sits between "Vertex slightly convex; longitudinal carina weak; vertexal foveae large." and "Maxillary palpi moderately developed; ...". **Quote MATCH**, 8 words, whole sentence. Sexual dimorphism: "Female eyes shorter than tempora, composed of 11 facets;" so the 23–26 sentence is the male (holotype ♂); the note discloses the inference from layout, which the page supports. Type material: holotype ♂ Dangsan-ri, Gyegok-myeon, Haenam-gun, Jeonnam, 18 May 2019; paratypes 2♂♂ 2♀♀ Sinsi island (4 Jul 2022), 2♂♂ Seonyu island (16 Jun 2021), 1♂ 3♀♀ Seonyu island (4 Jul 2022): type series 11, 6 ♂, 5 ♀. Conditions right. Diagnosis silent on eyes.

Fault: **value says more than the quote.** The value's "(eye size equal to the temples)" turns the printed length comparison ("as long as tempora") into a statement about eye size. One record error, fixable.

**Line 14 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 8 | Physomerinus clavipes, ~35 ommatidia per eye (male) | MATCH | | whole sentence; female 30 and type series right |
| 9 | Trisiniotus taoismus, ~35 large ommatidia per eye (male) | MATCH | | whole sentence; 15-specimen type series right |
| 10 | Pseudophanias furcilobus, ~30 per eye (male) | MATCH | | whole sentence under "Male."; female 30 right |
| 11 | Pseudophanias leigong, ~18 per eye (male holotype) | MATCH | | holotype only, female unknown |
| 12 | Pseudophanias mulun, ~16 per eye (male holotype) | MATCH | | holotype only, female unknown |
| 13 | Pengzhongiella daicongchaoi, ~32 facets per eye (female) | FIXABLE | order | "Coleoptera" printed in keywords, field left blank |
| 14 | Bryaxis grandinodus, 23–26 facets | FIXABLE | value | "eye size equal" for printed "as long as tempora" |

Errors: 2 of 7 records (28.6%); 2 fixable (lines 13, 14), 0 held out, 0 unfixable; no line to drop. Repeats: none. Verdict for desk-d311 lines 8 to 14: **ACCEPT AFTER REPLACEMENT** (lines 8 to 12 as filed; lines 13 and 14 with the replacements below, or dropped if they are not applied). The unit's pooled verdict rests with the seven audits together.

## Replacement

Each old string is copied from the desk file and occurs once in the line named.

Line 13:
- `order`: empty -> fill with "Coleoptera"
- `note`: "The page has no classification table; order and family come from the title (Staphylinidae, Pselaphinae, Batrisitae)  class left blank." -> "The page has no classification table; family from the title (Staphylinidae, Pselaphinae, Batrisitae) and order from the printed keywords ('Coleoptera, Batrisini, taxonomy, ...'); class left blank."

Line 14:
- `value`: "23-26 facets (eye size equal to the temples)" -> "23–26 facets (eyes as long as the tempora)"

Optional, not counted:
- Line 8 `conditions`: "The Diagnosis does not mention eyes." -> "The Diagnosis gives no eye state or count (it names the eyes only as a landmark for the mediobasal carina)."
- Line 11 `conditions`: "Xiannutang" -> "Xiannütang"
