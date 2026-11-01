# audit-419: desk-d313, evidence lines 9 to 16

Audited 1 November 2026 from the desk-d313 files present untracked in the worktree (docs/tracks/progress/desk-d313.md and docs/views/evidence/desk-d313.jsonl, 16 lines; neither committed here, neither edited). This audit covers file lines 9 to 16 only (Phyllium cayabyabi x2, P. crapulatum, Xenos yangi, Urothrips lancangensis, Baenothrips cuneatus, Coniopteryx tenuisetosa, Oroperipatus tiputini); lines 1 to 8 go to another auditor. HEAD equals origin/main (f1569e4f4). `python3 -I tools/senses/check.py | grep d313`: "docs/views/evidence/desk-d313.jsonl: 16 records, 0 problems". Quote lengths (`len(q.split())`) for lines 9 to 16: 22, 15, 15, 20, 11, 21, 3, 8, all within 40.

Sources opened (WebFetch, every page URL from a WebSearch result): zookeys.pensoft.net/article_preview.php?id=162609 (two passes), zookeys.pensoft.net/article_preview.php?id=76484, zookeys.pensoft.net/article/14616/download/xml/ (two passes), zookeys.pensoft.net/article/10706/download/xml/, zookeys.pensoft.net/article/57451/download/xml/ and article_preview.php?id=57451, zse.pensoft.net/article/117952/download/xml/ (two passes). Crossref single-DOI lookups (api.crossref.org/v1/works/<doi>): read for 10.3897/zookeys.1256.162609, zookeys.1085.76484 (second try), zookeys.636.10706, zookeys.1015.57451 and zse.100.117952; zookeys.694.14616 was rate-limited on both tries and not read (its citation comes from the article XML). No PROVENANCE_REQUIRED refusal was met in this audit. PMC, DOAJ, Plazi, Zenodo, BHL, library catalogues (uv.mx, ufrj.br, cas.cz, uitm.edu.my), the Siena repository PDF, zobodat and reviewer.ly were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 7 WebSearches.

## Bibliographic and licence

- Lines 9 to 11 (Cumming, Foley, Hennemann, Le Tirant, Daawia, Warikar, Yando, Suhartawan, Henze, Büscher, Bank 2025). Page byline and Crossref identical in order, including the single name "Daawia". Title identical. ZooKeys 1256: 317-370, no issue; Crossref issued 23 Oct 2025. Licence: page prints CC BY 4.0 (tool summary of the licence sentence); Crossref CC BY 4.0, vor. Accepted. The record notes say Crossref could not be read; it was readable here and agrees (optional note fix below).
- Line 12 (Dong, Liu, Mao, He, Li 2022). Byline, citation line "Citation: Dong Z, Liu X, Mao C, He J, Li X (2022)" ... "ZooKeys 1085: 11-27." and Crossref agree; title identical (Crossref carries a leading BOM). Page "Creative Commons Attribution License (CC BY 4.0),"; Crossref CC BY 4.0 vor. Accepted.
- Line 13 (Zhao, Tong 2017). Article XML: Chao Zhao; Xiaoli Tong; title identical; 694, fpage 1, lpage 10, 2017; CC BY 4.0 sentence (tool summary). Crossref unreadable (rate-limited twice). Accepted on the page licence.
- Line 14 (Zhao, Tong 2016). XML and Crossref agree: title identical, 636: 67-75, 2016; page "Creative Commons Attribution License (CC BY 4.0),"; Crossref CC BY 4.0 vor. Accepted.
- Line 15 (Zhao, Badano, Liu 2021). XML and Crossref agree: 1015: 129-144, 2021; page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.
- Line 16 (Montalvo-Salazar, Bejarano, Valarezo, Cisneros-Heredia 2024). XML and Crossref agree: Zoosystematics and Evolution 100(3): 779-789, 2024; page CC BY 4.0 sentence; Crossref CC BY 4.0 vor. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

Order and family as printed: Phasmatodea, Phylliidae (ZooKeys 1256 title and classification); Strepsiptera, Xenidae (title; the preview pass reported no Taxon classification block, the record note says the XML prints one; not counted either way, both print the same names); Thysanoptera, Phlaeothripidae (classification, lines 13, 14); Neuroptera, Coniopterygidae (line 15); Euonychophora, Peripatidae (line 16). No page prints a class; class blank is right. Phyllium cayabyabi and P. crapulatum both have Phasmida Species File entries (search results); the other four are described in the cited papers and no later synonymy turned up.

## Repeats

`git grep -il -F` on origin/main (f1569e4f4) over the whole docs/ tree for cayabyabi, crapulatum, "Xenos yangi", lancangensis, "Baenothrips cuneatus", tenuisetosa, tiputini, each full DOI and each Pensoft article number (162609, 76484, 14616, 10706, 57451, 117952). Hits: "tiputini" only in desk-d293.md and desk-d304.md skip lists ("Oroperipatus tiputini: no eye count"), not a filed record; the bare numbers 14616 and 57451 only as record counts / a decimal in unrelated rows. No repeat on main. Unmerged branches: grep of the 728 origin/research/desk-d* and audit-* branches still running at this commit; see the final version.

## Per line

### Line 9, Phyllium cayabyabi, female compound eyes ~¼ of lateral margins

Female Head: "Compound eyes slightly protruding from the head capsule, not bulbous, taking up ~ ¼ of the head capsule lateral margins (Fig. 6A)." **Quote MATCH**, whole sentence with a participle, 22 words; figure reference confirmed. Next sentence "Ocelli absent." confirmed. Type material: holotype ♀ "Indonesia • North Kalimantan, Malinau Regency, Tanjung Lapang Village, August 2020, Coll RC #20-135 [IMQC]."; paratypes (1♂) Coll RC #20-137, ♀ nymph #20-136 [Coll RC], (2♀♀) [IMQC], eggs #20-138, #20-139 [Coll RC] and (1 egg) Coll TB, same locality and date (tool summary for the list structure). Conditions agree. No Diagnosis eye wording (tool summary). Value says no more than the quote.

**Line 9 MATCH.**

### Line 10, Phyllium cayabyabi, male compound eyes ~2/5, bulbous

Male Head: "Compound eyes large and bulbous, occupying ~2/5 of the head capsule lateral margins (Fig. 7A)." **Quote MATCH**, 15 words. Ocelli sentence "There are three distinct ocelli raised above the capsule and located between the compound eyes" confirmed. Exactly one male in the type series, paratype "(1♂) Coll RC #20-137"; holotype female. Conditions say so.

**Line 10 MATCH.**

### Line 11, Phyllium crapulatum, male compound eyes ~2/5, bulbous

Male Head: "Compound eyes large and bulbous, occupying ~2/5 of the head capsule lateral margins (Fig. 11D)." **Quote MATCH**, 15 words; next sentence on three well-developed ocelli confirmed. Holotype ♂ only: "Indonesia • West Kalimantan, Mount Bawang, 00 53.5'N, 109 22.2'E, Elv. 245 Meters, May, 2023. Tissue sample: SLT069 [IMQC]."; no paratypes; "Female, egg, and freshly hatched nymph unknown." Conditions agree, except that "about 245 m" adds a hedge the page does not print (optional fix, not counted).

**Line 11 MATCH.**

### Line 12, Xenos yangi, about 84 ommatidia per eye

Male Head, read in two pieces: "Compound eye raspberries-like, each composed of about 84 ommatidia, ommatidiaprominent and separated by" / "chitinous bridges covered with micortrichia (Fig. 3A)." Previous sentence "Head transverse, 1.44 mm in width."; next begins "Antenna four-segmented (Fig. 2B), ...". **Quote MATCH**, whole printed sentence, printed typos kept, 20 words. "each composed of about 84" is per eye, as `units` says; "about" carried. No other ommatidia count in the paper (tool summary). Type material: holotype male KIZ0130767, Xiangda Township, Longling County, 1666 m, "20.XII.2019, local villagers leg.", 75% ethanol; paratypes "four males (KIZ0130768–KIZ0130771), three neotenic females (KIZ0130772–KIZ0130774), same data as holotype". Conditions agree. They leave out the "Other material examined" (one further neotenic female, and one neotenic female and one male partly used for DNA extraction); optional fix, not counted, since the description does not say which males it rests on.

**Line 12 MATCH.**

### Line 13, Urothrips lancangensis, about 10 dorsal facets, none ventral

Female aptera Head: "Eyes with approximately 10 facets dorsally, but absent ventrally; ocelli absent." **Quote MATCH**, whole sentence, 11 words; next sentence "Antennae arising ventrally, ..." Holotype "Female aptera, CHINA, Yunnan province, Pu'er City, Lancang County, Nuozhadu Nature Reserve" ... "5.xi.2016 (Chao Zhao)."; paratypes 6 females and 3 males with the holotype; "females and males all apterous" (tool summary). No Diagnosis; Remarks compare with U. tarai on head shape, sculpture, setae and fore-femur colour (tool summary). Agrees with conditions.

Fault: **contrasting wording misstated.** Conditions say "A male aptera is described with measurements only (no eye wording)." The male paragraph opens "Color and structure similar to apterous female, but body smaller." It has no eye wording, but it is not measurements only, and its first sentence extends the female structure to males in general terms. One record error, fixable.

**Line 13 FIXABLE.**

### Line 14, Baenothrips cuneatus, about 8 dorsal and 6 ventral facets

Female macroptera Head, four pieces: "Eyes with approximately eight facets dorsally and six ventrally," / "of which three dorso-lateral facets are distinctly larger than the others;" / "three ocelli present, anterior ocellus placed between inner cephalic setae," / "posterior ocelli behind outer pair of cephalic setae and placed close to eyes." The whole sentence is 43 words; the quote keeps the eye clause through "others;" and marks the trailing cut "…". The cut removes only the ocelli clause and drops no qualifier of the eye clause. **Quote MATCH** (21 words). Holotype "Female macroptera, CHINA, Guangdong province, Gaozhou County, Yuntan Town, Mt. Sanguanshan (21°55’10”N, 111°8’40”E)," "in leaf litter of Acacia auriculiformis (Fabaceae), 15.xii.2014, Chao Zhao (in SCAU)."; paratypes "8 females 1 male, taken with holotype; 3 females 7 males, same locality and habitat as holotype, 5.ix.2015" and further Hunan, Guangdong, Guangxi, Yunnan, Hainan material. Females all macropterous, males all apterous; male description has no eye wording (tool summary). Conditions agree (the 3 females 7 males of 5.ix.2015 fall under "further specimens"; acceptable).

**Line 14 MATCH.**

### Line 15, Coniopteryx tenuisetosa, "Compound eyes large."

Description under "Male: Head (Fig. 7a, b).": "Brown." / "Frons without projections." / "Compound eyes large." / "Antennae brown, 28-segmented, 1.2–1.5 mm in length." "Compound eyes large." is a whole printed sentence between full stops in the Description, not a heading, caption or a piece cut from a longer sentence. As a telegraphic whole Description sentence it falls within what the desk has accepted. **Quote MATCH**, 3 words. The value "compound eyes large (male)" says no more than the quote. Holotype "1 male, China: Tibet (Province): Linzhi (City)," 8.vi.2019, "leg. Yaru Zhao", CAU; paratypes "39 males and 54 females, same data as holotype"; no female description; no eye wording in Diagnosis or Remarks (tool summary). Conditions agree.

**Line 15 MATCH.**

### Line 16, Oroperipatus tiputini, eyes lateral behind antennal bases, slightly wrinkled

Description, Head: "Slightly wrinkled eyes laterally behind base of antennae." **Quote MATCH**, whole sentence, 8 words; next sentence begins "Ocular and frontal arches with large primary papillae and intraocular arch formed by smaller primary papillae". The Description names no sex (tool summary); Diagnosis "four supraocular papillae"; no eye variation in Remarks (tool summary). Value matches the quote.

Fault: **specimen dates and stage misstated.** Conditions say "paratypes 5 adult males (2017 to 2023)". The male paratypes are dated 22 May 2018, 21 May 2019, 13 Apr. 2021, 8 Jun. 2022 and 30 Jun. 2023, so the range is 2018 to 2023; the 2017 date belongs to "1 ♀ and 1 juvenile, ... 7 Jun. 2017". The type list prints ♂ and ♀ against "juvenile" and does not print "adult". The holotype line is "Ecuador • ♀, province of Orellana, Tiputini Biodiversity Station; -0.637, -76.152; 220 m elevation;" "6 Jun. 2022; ..." One record error, fixable.

**Line 16 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 9 | Phyllium cayabyabi, female eyes ~¼ | MATCH | | whole sentence; type series as printed |
| 10 | Phyllium cayabyabi, male eyes ~2/5 | MATCH | | rests on the single paratype male, as stated |
| 11 | Phyllium crapulatum, male eyes ~2/5 | MATCH | | holotype male only; "about 245 m" optional fix |
| 12 | Xenos yangi, about 84 ommatidia per eye | MATCH | | printed typos kept; "each" = per eye |
| 13 | Urothrips lancangensis, ~10 dorsal facets | FIXABLE | conditions | male paragraph called "measurements only"; it says "Color and structure similar to apterous female" |
| 14 | Baenothrips cuneatus, ~8 dorsal, 6 ventral facets | MATCH | | 43-word sentence cut after the eye clause, marked "…" |
| 15 | Coniopteryx tenuisetosa, compound eyes large | MATCH | | whole three-word Description sentence |
| 16 | Oroperipatus tiputini, eye position and surface | FIXABLE | conditions | male paratype dates 2018 to 2023, not 2017; "adult" not printed |

Errors: 2 of 8 records (25%); 2 fixable (lines 13, 16), 0 held out, 0 unfixable; no line to drop. Repeats: none on main; unmerged branches as above. Verdict for lines 9 to 16 of desk-d313: **ACCEPT AFTER REPLACEMENT** (lines 9, 10, 11, 12, 14, 15 as filed; lines 13 and 16 with the replacements below, or dropped if they are not applied). Pooled with the other auditor's lines 1 to 8 when that audit lands.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 13:
- `conditions`: "A male aptera is described with measurements only (no eye wording)." -> "The male aptera paragraph opens 'Color and structure similar to apterous female, but body smaller.' and has no eye wording."

Line 16:
- `conditions`: "Holotype adult female (ZSFQ-i8249)" -> "Holotype female (♀; ZSFQ-i8249)"
- `conditions`: "paratypes 5 adult males (2017 to 2023), 2 adult females and 3 juveniles from the same station" -> "paratypes 5 males (22 May 2018 to 30 Jun. 2023), 2 females (7 Jun. 2017 and 25 May 2022) and 3 juveniles (30 Jul. 2001, 7 Jun. 2017, 6 Jun. 2022), all with the holotype's locality data (the type list prints ♂, ♀ and juvenile, not 'adult')"

Optional, not counted:
- Line 11 `conditions`: "about 245 m" -> "245 m ('Elv. 245 Meters')"
- Line 12 `conditions`: "in 75% ethanol." -> "in 75% ethanol. Other material examined: one further neotenic female (same locality and date), and one neotenic female and one male partly used for DNA extraction; the description does not say which males it rests on."
- Lines 9, 10, 11, 12, 14, 15, 16 `note`: "Crossref could not be read (api.crossref.org fetches refused twice with PROVENANCE_REQUIRED, not worked around), so the citation line and volume/pages come from the publisher's own article XML." -> "The unit could not read Crossref (PROVENANCE_REQUIRED); audit-419 read it on 1 Nov 2026: authors, title, volume, pages and year agree, licence CC BY 4.0 (vor)."
