# audit-416: desk-d312, evidence lines 1 to 7 (Tachycines, ZooKeys 1109)

Audited 1 November 2026 from the desk-d312 files present untracked in the worktree (docs/tracks/progress/desk-d312.md and docs/views/evidence/desk-d312.jsonl, 12 lines; lines 8 to 12 go to another auditor; neither file committed here, neither edited). Branch research/audit-416 from origin/main. `python3 -I tools/senses/check.py | grep d312`: "docs/views/evidence/desk-d312.jsonl: 12 records, 0 problems". Quote lengths (`len(q.split())`), lines 1 to 7: 10, 15, 25, 8, 8, 18, 12, all within 40.

Sources opened (WebFetch, every URL from a WebSearch result): zookeys.pensoft.net/article/73937/download/xml/ (five passes) and zookeys.pensoft.net/article_preview.php?id=73937 (three passes); en.wikipedia.org/wiki/Tachycines and hopperwiki.org/index.php/Gymnaeta for names. The Crossref single-DOI lookup api.crossref.org/v1/works/10.3897/zookeys.1109.73937 was refused (PROVENANCE_REQUIRED, "Do not retry"); not retried or worked around, so the bibliographic check below rests on the publisher's citation line and licence sentence. PMC, plazi, DOAJ, agris, zoobank and BHL results were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of about 125 characters; points marked "(tool summary)" were not returned verbatim. 3 WebSearches.

## Bibliographic and licence

All seven lines: page citation "Zhou X, Yang W (2022) ZooKeys 1109: 115–140. https://doi.org/10.3897/zookeys.1109.73937"; byline Xulin Zhou, Weicheng Yang in that order; title "Ten new species of genus Tachycines (Orthoptera, Rhaphidophoridae, Aemodogryllinae) from karst caves in Guizhou, China", identical to the record; no issue printed; year 2022 printed. Page licence: "Creative Commons Attribution License (CC BY 4.0)" on the publisher's own free full text (accepted; Crossref licence not readable here, the unit's note reports CC BY 4.0 vor). Journal field uses a hyphen for the printed en dash in "115–140"; formatting only, not counted. Bibliographic faults 0; licence faults 0; access "open" right.

## Names and higher taxa

- Names: hopperwiki's Gymnaeta page (which defers to Orthoptera Species File) lists all seven, zhongi, lahaidensis, shibenzhangi, ziyunensis, jialiangensis, shanduensis and jinniui, under Tachycines (Gymnaeta), none as a synonym (tool summary; no authority or status printed). Orthoptera Species File itself was not in any result. Wikipedia's list (OSF as of 26 Sept 2021) predates the paper and omits them, as expected. Accepted.
- Order and family: each treatment prints a Taxon classification block "Animalia / Orthoptera / Rhaphidophoridae" (XML named-content kingdom, order, family); the title also prints both. Right.
- Class: the Taxon classification block has no class, and "Insecta" occurs only in the article-categories subject list ("Hexapoda", "Insecta", "Invertebrata"), not in the title, abstract, keywords or body. Leaving class blank follows "as printed". Not counted; optional fill below if the owner reads the subject list as printed.

## Repeats

`git grep -l -i` on origin/main over the whole docs/ tree (evidence, audit/corrected, audit/ALL, sheets, searched, tracks) for Tachycines, each of the seven epithets, "1109.73937" and "zookeys.1109". Hits: Tachycines only for T. trapezialis (desk-d285 evidence, Zhou & Yang 2020, eye_type) and in queue/progress notes; "zhongi" only inside Pengzhongiella (desk-d311); "ziyunensis" only as Triplophysa ziyunensis and Strigamia ziyunensis (desk-d295, d299). DOI: no hits. No repeat on main. Unmerged branches: see the end of this section.

Unmerged branches: all 311 origin/research/desk-d* branches other than desk-d312 grepped over docs/ with one `git grep -l -i -E` for the seven epithets and "zookeys.1109"; the only hits were the main-inherited desk-d295, desk-d299 and desk-d311 files named above (other genera). No repeat.

## Per line

The page prints no identification key; the Discussion speaks of cave-adapted Gymnaeta in general ("the ommateum and conical tubercles of the vertex reduced"), not of these species (tool summary). Material is preserved "in 75% ethanol". Each female description of the six male-described species reads "Appearance is similar to the male" and does not mention eyes (lahaidensis, shanduensis, ziyunensis, jialiangensis read; zhongi tool summary; shibenzhangi tool summary).

### Line 1, Tachycines zhongi, eyes slightly reduced; ocelli absent

Male description: "Body medium and small-sized (Fig. 1D)." / "Eyes slightly reduced, ocelli absent; conical tubercles of vertex reduced." / "Legs elongate and slender; ...". **Quote MATCH**, 10 words. Material: holotype 1 male, Daxiao Dong, Xinchang township, Liuzhi Special District, 900 m, 28 July 2019; paratypes 5 males, 2 females, same site and date (tool summary). Diagnosis compares body size, vertex tubercles ("much more reduced"), sternal projections and hind tarsus; no eyes. Conditions right.

**Line 1 MATCH.**

### Line 2, Tachycines lahaidensis, eyes moderately reduced, about 1/2 normal

"Vertex conical tubercles inconspicuous, eyes moderately reduced, approx. 1/2 the size of the normal eye." **Quote MATCH**, 15 words. Material: "Holotype , 1♂, Lahaide Dong, Pinglang Town, Duyun City, 2015-VII-24" ... "paratypes, 6♂, 8♀, same data as the holotype." Diagnosis (versus T. shibenzhangi) on epiphallus and sternal projections; no eyes. Conditions right.

**Line 2 MATCH.**

### Line 3, Tachycines shibenzhangi, ommateum extremely degenerated; some blind

Read in two pieces: "Vertex conical tubercles absent, ommateum extremely degenerated," / "present by narrow stripes with several black facets (some individuals have no black facets and are completely blind)." **Quote MATCH**, 25 words, one sentence. Value paraphrases "present by" as "present as"; acceptable.

Fault: **material incomplete.** Material examined: "Holotype, 1♂, Xuehua Cave, Zhonghe Town, Sandu County, 2019-VII-28" ... "paratypes, 16♂, 15♀, same data as the holotype." The conditions give the counts but no locality or date, and say "The female description was not read for eyes"; it reads "Appearance is similar to the male" and does not mention eyes (tool summary). The species' own Diagnosis also states the eye state ("the conical tubercles of the vertex are absent, the ommateum are extremely degenerated,"), which the conditions do not carry. One record error, fixable.

**Line 3 FIXABLE.**

### Line 4, Tachycines ziyunensis, ommateum moderately reduced

"Vertex conical tubercles almost absent, ommateum moderately reduced." **Quote MATCH**, 8 words. Material: "Holotype 1♂, Sanjiaoshan cave, Ziyun County, 2019-X-2, collected by Xulin Zhou" ... "paratypes 15♂, 38♀, same data as holotype". Diagnosis pieces "it can easily be distinguished by the eyes moderately reduced," and "but the latter of eyes extremely reduce," as the conditions quote them. The conditions say the female description was not read; the preview page says it reads only "Appearance is similar to the male." (tool summary). Not counted; optional fix.

**Line 4 MATCH.**

### Line 5, Tachycines jialiangensis, ommateum moderately reduced

Male: "Male. Body medium in size." / "Vertex conical tubercles almost absent, ommateum moderately reduced." **Quote MATCH**, 8 words. Material: "Holotype 1♂, Lajilou Cave, Jialiang Town, Libo County, 2017-X-23", collectors Xulin Zhou, Dongshan Xu, Weicheng Yang, "paratypes, 4♂, 2♀, same data as holotype". Diagnosis versus T. ziyunensis on hind tarsus (keeled versus bristles) and hind-tibial spines, no eyes (tool summary). Female: "Appearance is similar to the male." Conditions right.

**Line 5 MATCH.**

### Line 6, Tachycines shanduensis, ommateum black and well developed

"Vertex conical tubercles are well developed, bisected from the base; ommateum is black and well developed (Fig. 6A)." **Quote MATCH**, 18 words, figure reference kept. Material: "Holotype 1♂, Shuilong Cave, Sandu County, 2019-VII-22" ... "paratypes, 6♂, 8♀, same data as holotype." Diagnosis (versus T. solida, T. tongrenus) on epiphallus, hind-tibial spines and hind tarsus; no eyes. Female "Appearance is similar to male (Fig. 6B)," no eyes. Conditions right.

**Line 6 MATCH.**

### Line 7, Tachycines jinniui, ommateum black and well developed (female)

Female description: "Body medium sized." / "Vertex conical tubercles slightly reduced, apex obtuse, ommateum black and well developed." **Quote MATCH**, 12 words. "Male. Unknown." Diagnosis pieces "The new species is very similar to Tachycines (Gymnaeta) trapezialis Zhou & Yang, 2020" / "but differs from the latter by having slightly reduced eyes" / "and the conical tubercles of the vertex intermediately reduce,", as the conditions say.

Faults (one record error, fixable): (a) **value says more than the quote.** The value adds "the Diagnosis says the eyes are slightly reduced compared with T. trapezialis", which is not in the quoted sentence; the contrast belongs in the conditions, where it already is. (b) **material incomplete.** Material examined: "Holotype, 1♀, Jinniu Cave (Fig. 14), Libo County, 2017-X-23, collected by Xulin Zhou, Dongshan Xu, Weicheng Yang;" / "paratype, 1♀, same collection data as for holotype." The conditions give no locality or date.

**Line 7 FIXABLE.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | T. zhongi, eyes slightly reduced | MATCH | | |
| 2 | T. lahaidensis, eyes moderately reduced (1/2) | MATCH | | |
| 3 | T. shibenzhangi, ommateum extremely degenerated | FIXABLE | conditions | locality and date omitted; own Diagnosis eye wording and female description not carried |
| 4 | T. ziyunensis, ommateum moderately reduced | MATCH | | optional female note |
| 5 | T. jialiangensis, ommateum moderately reduced | MATCH | | |
| 6 | T. shanduensis, ommateum well developed | MATCH | | |
| 7 | T. jinniui, ommateum well developed (female) | FIXABLE | value, conditions | value carries Diagnosis wording beyond the quote; locality and date omitted |

Errors: 2 of 7 records (28.6%); 2 fixable (lines 3, 7), 0 held out, 0 unfixable; no line to drop. Repeats: none. Verdict for desk-d312 lines 1 to 7: **ACCEPT AFTER REPLACEMENT** (lines 1, 2, 4, 5, 6 as filed; lines 3 and 7 with the replacements below, or dropped if they are not applied).

## Replacement

Each old string is copied from the desk file and occurs once in the field of the line named (checked with `str.count`).

Line 3:
- `conditions`: "holotype 1 male and paratypes 16 males and 15 females (Type material heading)." -> "holotype 1 male and paratypes 16 males and 15 females, all from Xuehua Cave, Zhonghe Town, Sandu County, 28 July 2019. The species' own Diagnosis says 'the conical tubercles of the vertex are absent, the ommateum are extremely degenerated'."
- `conditions`: "The female description was not read for eyes." -> "The female description says only that the female is similar to the male and does not mention eyes."

Line 7:
- `value`: "ommateum black and well developed (Description, female); the Diagnosis says the eyes are slightly reduced compared with T. trapezialis" -> "ommateum black and well developed"
- `conditions`: "(holotype 1 female and paratype 1 female; no males)." -> "(holotype 1 female and paratype 1 female, both from Jinniu Cave, Libo County, 23 October 2017; 'Male. Unknown.')."

Optional, not counted:
- Line 4 `conditions`: "The female description was cut off in the text returned and was not read for eyes." -> "The female description says only that the female is similar to the male and does not mention eyes."
- Lines 1 to 7 `class`: fill with "Insecta" only if the owner counts the article's subject list ("Hexapoda", "Insecta") as printed; otherwise leave blank.
