# audit-413: desk-d311, file lines 29 to 35

Audited 1 November 2026 from the desk-d311 files present untracked in the worktree (docs/tracks/progress/desk-d311.md and docs/views/evidence/desk-d311.jsonl; neither committed here, neither edited). Six other auditors take lines 1-28 and 36-50. `python3 -I tools/senses/check.py | grep d311`: "docs/views/evidence/desk-d311.jsonl: 50 records, 0 problems". Quote lengths (`len(q.split())`) for lines 29 to 35: 15, 15, 15, 16, 9, 16, 15, all within 40.

Sources opened (WebFetch, every URL from a WebSearch result): zookeys.pensoft.net/article/3442/download/xml/ (three passes; the tool's text of it stops after the P. erlangshanus treatment, 81431 characters), zookeys.pensoft.net/article_preview.php?id=3442 (three passes), zookeys.pensoft.net/article/126696/download/xml/ (one pass), zookeys.pensoft.net/article_preview.php?id=3726 (three passes). Crossref single-DOI lookups api.crossref.org/v1/works/ for 10.3897/zookeys.251.4099, 10.3897/zookeys.1206.126696 and 10.3897/zookeys.275.4571, each read on the first call. Not opened: Plazi, species-id.net, DOAJ, BHL, the PMC blob copy, library catalogue records (uv.mx, ufrj.br, bvsalud); no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns pieces of about 125 characters; points marked "(tool summary)" were not returned verbatim. 3 WebSearches.

## Bibliographic and licence

- Lines 29 to 32 (Yin, Li 2012, ZooKeys 251: 83-118). Crossref: Zi-Wei Yin; Li-Zhen Li; title identical to the record (Crossref "Schülke's" with a straight apostrophe, page a curly one; typography only); volume 251, no issue, pages 83-118, issued 2012-12-18; licence CC BY 3.0 vor. Page prints "This is an open access article distributed under the terms of the Creative Commons Attribution License 3.0 (CC-BY),". Accepted.
- Line 33 (Feng, Yin 2024, ZooKeys 1206: 231-239). Crossref: Ting Feng; Zi-Wei Yin; title identical; volume 1206, pages 231-239, issued 2024-07-08; CC BY 4.0 vor; page prints the CC BY 4.0 sentence. Page "Taxon classification: Animalia; Coleoptera; Staphylinidae" (no class). Accepted.
- Lines 34 and 35 (Yin, Hlaváč, Li 2013, ZooKeys 275: 23-65). Page byline "Zi-Wei Yin, Peter Hlaváč, Li-Zhen Li" (Crossref "Hlavac" without the accent; the record keeps the printed accent); title identical; volume 275, pages 23-65, issued 2013-03-04; CC BY 3.0 vor and page CC BY 3.0 sentence. No Taxon classification line and no class printed (tool summary); order/family from the title. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout. Class blank is right for all seven (no page prints a class).

## Names and repeats

All seven are species described as new in the paper read; no later synonymy seen. `git grep -il` on origin/main over the whole docs/ tree for each species name, each epithet, and the three DOIs (full and short forms): no species hit (the only "venustus" hit is Ancylomenes venustus in canon-4, a shrimp). Two DOIs are on main in desk-d302: Linan tendothorax (10.3897/zookeys.251.4099) and Dayao emeiensis (10.3897/zookeys.275.4571), other species, as the unit's notes say; ZooKeys 1206 is not on main. Unmerged origin/research/desk-d* and audit-* branches (excluding d311 and gaps copies) grepped for the seven epithets and the 1206 DOI: see the final paragraph of this section.

Unmerged-branch pass: running at this commit; result added below when complete.

## Per line

All quotes were returned verbatim with the en dashes as stored; every record's value "about N facets in each eye of the male" (or "approximately 55 ommatidia") keeps the printed "about"/"approximately" and says per eye as the sentence does ("eyes each composed of"). Each quote is a whole printed sentence opening at "Head", directly after "Length ..." (or "Male (Fig. ...). Length ...") and followed by "Antennal clubs as in Fig. ..." or "Pronotum (Fig. 5B) ..."; it is not a fragment cut from a longer sentence. Telegraphic Description sentences accepted on the audit-395/403 precedent. No Diagnosis or Comparative notes sentence in these treatments mentions eyes (tool summary).

### Line 29, Pselaphodes erlangshanus, about 30 facets per eye (male)

Quote MATCH: "Head longer than wide, HL 0.74–0.78, HW 0.65–0.68; eyes each composed of about 30 facets." Preceded by "Male (Fig. 11B). Length 3.29–3.78." Type material "(2 ♂♂)"; paratype "1 ♂, same label data as holotype, except 'det. Brachat 4.01' (cSch)."; "Female. Unknown." All right.

Fault: **holotype collecting data misstated.** The conditions say "W of Erlangshan pass ... 22 Jun., sifted from coniferous-forest litter". The label prints "CHINA: W-Sichuan 1999 / Ganzi Tibet. Aut. Pref., Luding Co. / W Erlanshan-pass, 2600 m / 7 km SSE Luding, 29°51'N, / 102°15'E, Laub+Nadelstreu, Pilze / 22. VI., leg. M. Schülke": leaf and needle litter and fungi, not coniferous-forest litter; no sifting is printed; the year 1999 is omitted. One error, fixable.

**Line 29 FIXABLE.**

### Line 30, Pselaphodes flexus, about 25 facets per eye (male)

Quote MATCH: "Head longer than wide, HL 0.66, HW 0.60; eyes each composed of about 25 facets." Preceded by "Length 2.87."; one male in the type series "(1 ♂, 7 ♀♀)", so the single HL/HW values are the holotype's (the conditions' hedge is harmless).

Faults (one record error, fixable): (a) **collecting data misstated.** The label prints "(creek / valley, secondary mixed forest) / 13.VIII.2003 Wrase [01]"; no sifting is printed. The paratypes are "3 ♀♀, same label data as holotype, except 'Labomimus sp. 7 ...'" and "4 ♀♀, same label data, except '13.VIII.2003, M. Schülke,". (b) **contrasting wording omitted.** Despite seven female paratypes, the treatment prints "Female. Unknown." directly after "Aedeagus length 0.60, with asymmetric median lobe (Figs 14I–K)."; the conditions say only "the female eye count is not given".

**Line 30 FIXABLE.**

### Line 31, Pselaphodes tibialis, about 40 facets per eye (male)

Quote MATCH: "Head longer than wide, HL 0.58–0.59, HW 0.54–0.55; eyes each composed of about 40 facets." Type material "(2 ♂♂)", holotype "Diancang Shan 45 / km NW Dali, 2730 m, ... creek valley, pines, ferns, / sifted, 29.V.2007, M. Schülke"; "Paratype: 1 ♂, same label data as holotype (cSch)."; "Female. Unknown." Conditions right.

**Line 31 MATCH.**

### Line 32, Pselaphodes venustus, about 30 facets per eye (male)

Quote MATCH: "Head slightly longer than wide, HL 0.65, HW 0.60; eyes each composed of about 30 facets." Preceded by "Length 3.07." Type material "(1 ♂, 1 ♀)", "Jizu Shan, summit plateau, / 37 km NE Dali 3150 m, (mixed / forest, sifted from litter, moss)", "5.IX.2009 DW Wrase [28]"; "Paratype: 1 ♀, same label data, except 'leg. M. Schülke [CH09-28]'". Female paragraph "Eyes each composed of about 30 facets." carried in conditions. Right.

**Line 32 MATCH.**

### Line 33, Pselaphodes wanchaoshanus, approximately 55 ommatidia per eye (male holotype)

Quote MATCH: "Eyes greatly prominent, each composed of approximately 55 ommatidia." in the Description (which begins "Male. Body (Fig. 1A) length 3.16 mm;"), a whole telegraphic sentence after "... lacking median carina." and before "Maxillary palpus (Fig. 1C) four-segmented, ...". Type material "(1 specimen). Holotype: China: ♂, ... Xingshan County, Wanchaoshan N. R., ... 1700 m, 19.viii.2023, Guo-Hao Wei leg.,"; "Female. Unknown."; P. nomurai additional material 2 ♂♂, same data. The word "ommatidia" occurs only in this sentence; "facets" nowhere (tool summary). Diagnosis has no eye statement. Conditions right.

**Line 33 MATCH.**

### Line 34, Labomimus fimbriatus, about 30 facets per eye (male)

Quote MATCH: "Head slightly longer than wide, HL 0.70–0.72, HW 0.60–0.65; eyes each composed of about 30 facets." Preceded by "Length 3.52–3.77."; female "Eyes each composed of about 30 facets." carried.

Fault: **paratype localities and dates misstated.** The conditions put all 12 paratypes in "Nujiang Lisu Autonomous Prefecture, 2007 and 2009". The type material is "(7 ♂♂, 6 ♀♀)"; holotype "Pianma Town, Gaoligongshan Mt. / ... 3000 m, / (mixed leaf litter, sifted) / 2012.vi.24, Liang Tang leg."; the first paratype lot is "1 ♂, same label data as holotype (SNUC)", i.e. Pianma, 2012. The other lots (2 ♂, 3 ♀♀ 7.VI.2007; 1 ♀ and 1 ♀ 9.VI.2007; 1 ♂ 3.IX.2009; 1 ♂, 1 ♀ 2.IX.2009; 1 ♂ 9.VI.2007) are Gaoligong Shan, Nujiang Lisu Aut. Pref. The total 6 males and 6 females is right. One error, fixable.

**Line 34 FIXABLE.**

### Line 35, Labomimus jizuensis, about 40 facets per eye (male)

Quote MATCH: "Head longer than wide, HL 0.76–0.80, HW 0.63–0.65; eyes each composed of about 40 facets." Preceded by "Male (Fig. 4A). Length 3.54–3.64." Type material "(3 ♂♂). Holotype: ♂, labeled 'CHINA: Yunnan / above Dali, 2700-2900 m / 14.IV.1999 / leg. W. SCHAWALLER'"; "Paratypes: 2 ♂♂, ... Jizu ShaN, path to cable car, 37 km NE Dali / 2450 m, ... 5.IX.2009 D.W. Wrase"; "Female. Unknown." Conditions right (optional: add 2450 m).

**Line 35 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 29 | Pselaphodes erlangshanus, about 30 facets | FIXABLE | conditions | label prints leaf and needle litter and fungi (no sifting, not coniferous litter); year 1999 omitted |
| 30 | Pselaphodes flexus, about 25 facets | FIXABLE | conditions | "sifted" not printed; page prints "Female. Unknown." despite 7 female paratypes, not reported |
| 31 | Pselaphodes tibialis, about 40 facets | MATCH | | |
| 32 | Pselaphodes venustus, about 30 facets | MATCH | | |
| 33 | Pselaphodes wanchaoshanus, approximately 55 ommatidia | MATCH | | |
| 34 | Labomimus fimbriatus, about 30 facets | FIXABLE | conditions | one male paratype is from the holotype locality (Pianma, 2012), not Nujiang 2007/2009 only |
| 35 | Labomimus jizuensis, about 40 facets | MATCH | | |

Errors: 3 of 7 records (43%); 3 fixable (lines 29, 30, 34), 0 held out, 0 unfixable; no line to drop. Quotes, values, bibliography, licences and higher taxa all right; every fault is in collecting-data conditions. Verdict for lines 29 to 35 of desk-d311: **ACCEPT AFTER REPLACEMENT** (lines 31, 32, 33, 35 as filed; lines 29, 30, 34 with the replacements below, or dropped if not applied). The pooled verdict for desk-d311 rests with the merger across the seven audits of this unit.

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 29:
- `conditions`: "W of Erlangshan pass, Luding County, Sichuan, China, 2600 m, 22 Jun., sifted from coniferous-forest litter" -> "label 'W Erlanshan-pass, 2600 m / 7 km SSE Luding', Luding County, Ganzi, Sichuan, China, 22 Jun. 1999, leaf and needle litter and fungi ('Laub+Nadelstreu, Pilze'; collecting method not printed)"

Line 30:
- `conditions`: "sifted in a secondary mixed forest) and 7 female paratypes from the same locality and date; the female eye count is not given." -> "creek valley, secondary mixed forest; collecting method not printed) and 7 female paratypes from the same locality and date (3 with the holotype's label data, 4 labelled 'M. Schülke'). Despite the female paratypes, the treatment prints 'Female. Unknown.' and gives no female eye count."

Line 34:
- `conditions`: "12 paratypes (6 males, 6 females; Nujiang Lisu Autonomous Prefecture, 2007 and 2009)" -> "12 paratypes (6 males, 6 females): 1 male with the holotype's label data (Pianma, 3000 m, mixed leaf litter sifted, 24 Jun. 2012) and 5 males and 6 females from Gaoligong Shan, Nujiang Lisu Aut. Pref., 2007 and 2009"

Optional, not counted:
- Line 35 `conditions`: "2 male paratypes (Jizu Shan, 5 Sep. 2009)" -> "2 male paratypes (Jizu Shan, path to cable car, 2450 m, 5 Sep. 2009)"
