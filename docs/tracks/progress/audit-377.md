# audit-377: desk-d288, evidence lines 1 to 6

Audited 1 November 2026 from the desk-d288 files present untracked in the worktree (docs/tracks/progress/desk-d288.md and docs/views/evidence/desk-d288.jsonl, 6 lines; neither committed here, neither edited). Worktree HEAD and origin/main faedc72f (Merge desk d287 (7 records) after audit 376). `python3 -I tools/senses/check.py | grep 'd288\.'`: "docs/views/evidence/desk-d288.jsonl: 6 records, 0 problems". Quote lengths (`len(q.split())`): 7, 9, 22, 25, 29, 39, all within 40 (the desk note's list "5, 9, 22, 25, 29, 39" is off for line 1, which is 7 words; a progress-note slip, not a record fault). Non-ASCII in quotes: line 5 "Tömösváry" and line 6 en dash "Five–six", both as printed. Line numbers are the file's (1-based).

Sources opened (WebFetch): mdpi.com/2075-4450/13/7/650/htm; www.mdpi.com/2673-6500/4/1/11 (two passes); zookeys.pensoft.net/article_preview.php?id=47295 (two passes), ?id=19980 (two passes), ?id=4285; api.crossref.org/v1/works/ for all five DOIs (10.3390/insects13070650, 10.3390/taxonomy4010011, 10.3897/zookeys.980.47295, zookeys.741.19980, zookeys.459.8169; two first attempts rate-limited, both answered on retry). All page URLs were returned by a WebSearch first. PMC, Plazi, GBIF, DOAJ, BHL, repository and catalogue hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 6 WebSearches.

## Bibliographic and licence

- Line 1 (de Souza, Medeiros, Ferreira, Souza-Silva, Bellini 2022). Crossref: Paolla Gabryelle Cavalcante de Souza, Gleyce da Silva Medeiros, Rodrigo Lopes Ferreira, Marconi Souza-Silva, Bruno Cavalcante Bellini; title identical; Insects 13(7): 650; issued 2022-07-19; CC BY 4.0 vor. Page byline same order; page metadata CC BY 3.0 (tool summary). CC BY 3.0 page vs CC BY 4.0 Crossref is accepted by rule. Accepted.
- Line 2 (Soto-Adames, Daly, Wynne 2024). Crossref: Felipe Soto-Adames, Kathryn M. Daly, J. Judson Wynne; title opening verbatim "Synopsis of Neotropical Trogolaphysa Mills, 1938 (Collembola: Paronellidae) with Reduced Eye Number," (rest over the tool limit, consistent with the record); Taxonomy 4(1): 199-236; issued 2024-03-05; CC BY 4.0 vor. Page links CC BY 3.0. Accepted.
- Line 3 and 4 (Chang, Pei, Zhu, Ma 2020). Page byline verbatim "Xiaodong Chang‡, Sujian Pei‡, Chunying Zhu‡, Huiqin Ma§‡"; printed citation "ZooKeys 980: 43-55"; title identical on page and Crossref; issued 2020-10-28; CC BY 4.0 vor; page licence sentence CC BY 4.0. Accepted.
- Line 5 (Pei, Lu, Liu, Hou, Ma 2018). Page and Crossref: Sujian Pei, Yanmin Lu, Haipeng Liu, Xiaojie Hou, Huiqin Ma; ZooKeys 741: 203-217; issued 2018-03-07; CC BY 4.0 vor; page sentence verbatim "open access article distributed under the terms of the Creative Commons Attribution License". Proceedings of the 17th International Congress of Myriapodology, a peer-reviewed ZooKeys issue. Accepted.
- Line 6 (Ma, Pei, Hou, Zhu 2014). Page byline verbatim "Huiqin Ma‡, Sujian Pei‡, Xiaojie Hou‡, Tiegang Zhu‡"; ZooKeys 459: 1-10; issued 2014-12-01; CC BY 4.0 vor; licence sentence verbatim "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),". Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout; printed years match Crossref issued years; no ZooKeys issue number printed or in Crossref.

## Names and higher taxa

No checklist was reachable (ChiloBase and Collembola checklist pages not in search results). All six species are described as new in the cited papers, so the names rest on the original descriptions.

- Troglobentosminthurus luridus: classification printed Order Symphypleona, Suborder Appendiciphora, Superfamily Sminthuroidea, Family Sminthuridae, Subfamily Sminthurinae (tool summary). Family and order as filed. Met.
- Trogolaphysa reneaui: page prints "Hexapoda: Collembola" and Paronellidae, no order heading (tool summary). Empty order allowed (audits 370, 372, 376); Collembola rightly not filed as order. Met.
- Lines 3 to 6: Lithobiidae, Lithobiomorpha, as in each title. Subgenus kept in parentheses in the taxon, the form main uses for L. (Ezembius) varioporus and ternidentatus. Met.

Name faults 0.

## Duplicates

git grep on origin/main (faedc72f) across the whole docs/ tree (evidence, audit/ALL, audit/corrected, sheets, searched/, gaps, codex-findings, progress notes) for Troglobentosminthurus, luridus, Trogolaphysa, reneaui, Sinuispineus, sinuispineus, minuticornis, tetraspinus, Monotarsobius, zhangi and the five DOIs: only unrelated matches ("luridus" is Siganus luridus in desk-d244, audit-339, try-species and sweep-12; "zhangi" is Zhangixalus and Rhacophorus rows in oa-2, frog gaps and sweep-55). No Trogolaphysa, Paronellidae or Sminthuridae row on main evidence. All 758 remote desk-* and audit-* branches: no hit in any branch's docs/views/evidence for the species, subgenera or DOIs; the 57 branches desk-d26x to d29x and audit-35x to 39x also checked in docs/tracks/progress, hits only in research/audit-377 itself.

Duplicates 0.

## Trait keys and rulings

All six are eyes_count with "eyes per side" (springtails) or "ocelli per side" (centipedes); the quotes print "on each side" or "n + n", so per-side units are right and no total is claimed. Every quote sits under the single new species' own Description or Diagnosis heading, so a sentence not naming the species is attributable.

## Per-record findings

### Line 1, Troglobentosminthurus luridus, 5 per side

Diagnosis verbatim "Eyes 5 + 5, reduced in size." **Quote MATCH**, 7 words. Head description verbatim "Eyes 5 + 5, reduced in size, apparently with an extra vestigial lens on each eyepatch." (in the note). Holotype female on slide ISLA 79664, Água Clara cave system, Serra do Ramalho, Carinhanha, Bahia, 11 October 2017; paratypes three males and one female, one male collected 16 October 2017 (tool summary). Mixed sexes. Uncounted: conditions print "Agua Clara" without the accent and say "the paper gives no variation in eye number" while the head description's vestigial lens is a possible sixth; the note carries it, so the conditions can point to it.

**Line 1 MATCH.**

### Line 2, Trogolaphysa reneaui, 1 + 1 (sometimes seemingly eyeless)

Head description verbatim, consecutive: "Antennal segments 3–4 lost in all specimens during slide making process." "Eyes 1 + 1 (Figure 5C), sometimes seemingly eyeless." "Extra ocular structure not seen." **Quote MATCH**, 9 words, figure reference reproduced. Table 2 row verbatim "| T. reneaui n. sp. | 0–1 |" agrees. Holotype verbatim "Holotype female, microscope slide mounted, accession # FSCA00051050."; paratypes two adult females, one adult male, one immature female from Crocodile Cave 2 (tool summary). Mixed sexes; no specimen-level eye counts printed. Variation kept in value.

**Line 2 MATCH.**

### Line 3, Lithobius (Sinuispineus) sinuispineus, 9 per side

Description verbatim in two consecutive pieces: "Nine, oval to rounded ocelli on each side, from small to large, arranged in three irregular rows;" + " posterior two ocelli comparatively large." **Quote MATCH**, 22 words, no figure reference inside. Diagnosis verbatim "ocelli usually nine on each side, in three irregular rows" (in the note). Description is general, sex paragraphs labelled only for genital characters, so the count is not sex-specific. Type material: holotype male and paratypes 1 female and 1 male (LS01-1), Huanggangshan, 15 August 2010; additional material 2 males (LS01-2), Yulinting, 8 August 2010 (tool summary). Uncounted: conditions say "no variation" although the Diagnosis's "usually" implies some; the note shows it; and the additional material is omitted.

**Line 3 MATCH.**

### Line 4, Lithobius (Sinuispineus) minuticornis, 8 to 10 per side

Description verbatim: "Eight to ten (commonly nine) oval to rounded ocelli on each side, from small to large, in three irregular rows;" + " posterior two ocelli comparatively large." **Quote MATCH**, 25 words. Diagnosis "ocelli 8–10 on each side, arranged in three irregular rows". Holotype male LS02-1, Zhenlei Mountain Forest Park, 27 August 2017; paratypes 65 females and 50 males. Conditions right.

**Line 4 MATCH.**

### Line 5, Lithobius (Ezembius) tetraspinus, 8 to 10 per side

Description verbatim: "Eight to ten oval to rounded ocelli on each side (Fig. 2), arranged in three irregular rows;" + "posterior two ocelli large; ocelli adjacent to the Tömösváry organ slightly small." **Quote MATCH**, 29 words. Diagnosis "8–10 ocelli on each side, arranged in 3 irregular rows, posterior two ocelli comparatively large". Remarks verbatim "The new species with 2+2 coxosternal teeth, 9–10 ocelli on each side of head," (about L. tetraspinus itself, compared with L. (E.) sibiricus), so the note's statement of the 9-10 discrepancy is right. Holotype verbatim opening "♂, body length 11.7 mm"; Balikun County, Hami City, Xinjiang, 968 m, 25 July 2006; paratypes 8 females and 1 male. Conditions right.

**Line 5 MATCH.**

### Line 6, Lithobius (Monotarsobius) zhangi, 5 to 6 per side

Description verbatim in three consecutive pieces: "Five–six oval to rounded ocelli on each side (Figure 3) in two irregular rows;" + "the terminal ocellus comparatively large; other ocelli about equal in size apart the ocelli adjoining to the ventral;" + "all ocelli domed, translucent, usually darkly pigmented." Preceding sentence ends "straight or slightly bulging."; following begins "Tömösváry’s organ situated". **Quote MATCH**, 39 words, whole sentence. Diagnosis and Key couplet 4 give 5–6. Type material: holotype female, Nanshan Park, Yantai City, Shandong, 5 July 2005, leg. Huiqin Ma; paratypes "Two females, with the same data as the holotype" (tool summary).

**Error (sample composition).** All three specimens are female, so the 5-6 range rests on females only; the conditions name only the holotype and say "no breakdown by sex is given", which hides that no male was examined. The rule counts single-sex material presented without saying so as an error. Fixable in conditions (below); the value itself is the quote's.

**Line 6 FIXABLE ERROR.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Troglobentosminthurus luridus, 5 per side | MATCH | none | Diagnosis quote MATCH (7); both sexes; vestigial-lens clause in note |
| 2 | Trogolaphysa reneaui, 1 + 1 (sometimes eyeless) | MATCH | none | quote MATCH (9), variation kept; Table 2 "0–1" agrees; empty order allowed |
| 3 | L. (S.) sinuispineus, 9 per side | MATCH | none | quote MATCH (22); Diagnosis "usually nine" in note |
| 4 | L. (S.) minuticornis, 8-10 per side | MATCH | none | quote MATCH (25); 65 F, 50 M paratypes |
| 5 | L. (E.) tetraspinus, 8-10 per side | MATCH | none | quote MATCH (29); Remarks 9-10 discrepancy stated |
| 6 | L. (M.) zhangi, 5-6 per side | FIXABLE ERROR | conditions | quote MATCH (39); all type material female, not stated |

Errors 1 of 6 audited records (16.7%), over the 5% bar. The one error is fixable and the audit covered the whole unit, so no record is held out. By kind: quotes 0; value exceeding quote 0; sample composition 1 (line 6); bibliographic 0; licence 0; names 0; filing convention 0; duplicates 0. Verdict: merge all six lines after applying the line 6 replacement; with it applied the unit stands at 0 open errors. The uncounted fixes may be applied at merge.

Unchecked: no checklist entry for any species; the springtail classification, the zhangi paratype sexes and the sinuispineus additional material rest on tool summaries; figures not viewed.

## Replacement

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 6 (counted):
- `conditions`: "Holotype female, Nanshan Park, Yantai City, Shandong Province, China; the count is a range for the species and no breakdown by sex is given" -> "Holotype female, Nanshan Park, Yantai City, Shandong Province, China, 5 July 2005; paratypes two females with the same data; all type material is female, so the range rests on females only and no male was examined"

Line 1 (uncounted):
- `conditions`: "Agua Clara" -> "Água Clara"
- `conditions`: "the paper gives no variation in eye number" -> "the paper gives no variation in eye number, though the Head description adds a possible extra vestigial lens on each eyepatch (see note)"

Line 3 (uncounted):
- `conditions`: "the description gives one count for the species and no variation, and the sex the count belongs to is not stated" -> "additional material 2 males (LS01-2), Yulinting, 8 August 2010; the Description gives one count and the Diagnosis says 'usually nine', so some variation is implied but not given; the count is not tied to a sex"
