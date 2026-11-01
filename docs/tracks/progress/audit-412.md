# audit-412: desk-d311, file lines 22 to 28

Audited 1 November 2026 from the desk-d311 files present untracked in the worktree (docs/tracks/progress/desk-d311.md and docs/views/evidence/desk-d311.jsonl, 50 lines; neither committed here, neither edited). This audit covers file lines 22 to 28 only; six other auditors take the rest. HEAD equals origin/main (095e055d8). `python3 -I tools/senses/check.py | grep d311`: "docs/views/evidence/desk-d311.jsonl: 50 records, 0 problems". Quote lengths (`len(q.split())`): 16, 16, 15, 15, 15, 15, 15, all within 40.

All seven lines come from one paper, Yin and Li 2012, ZooKeys 251 (10.3897/zookeys.251.4099), read once and every line judged from it. Sources opened: Crossref single-DOI lookup api.crossref.org/v1/works/10.3897/zookeys.251.4099 (first call); zookeys.pensoft.net/article_preview.php?id=3442 (from a WebSearch result; five passes). No PMC, repository, species-id.net or library copy opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 1 WebSearch.

## Bibliographic and licence

Page byline "Zi-Wei Yin 1,†, Li-Zhen Li 1,‡"; Crossref Zi-Wei Yin, Li-Zhen Li, same order. Citation line "ZooKeys 251: 83–118, doi: 10.3897/zookeys.251.4099"; Crossref volume 251, no issue, page 83-118, issued 2012-12-18; printed year 2012. Licence: page prints "This is an open access article distributed under the terms of the" / "Creative Commons Attribution License 3.0 (CC-BY), ..."; Crossref CC BY 3.0 vor; relation empty, no update. Accepted. source.access "open" right.

Title: page prints "Notes on Michael Schülke’s pselaphine collections from China." / "– Tyrini. I. genera Labomimus Sharp, Linan Hlaváč and Pselaphodes Westwood" / "(Coleoptera,  Staphylinidae,  Pselaphinae)". The record matches in words, dash and punctuation; it has a straight apostrophe where the page and main's own copy of this title (desk-d302 line 2, accepted in audit 394) have the curly "Schülke’s", and single spaces where the body prints doubles inside the parenthesis. Typographic only (audit 5 and 314 precedent), not counted; optional fix below.

Higher taxa: the page prints Coleoptera, Staphylinidae, Pselaphinae in the title and "Staphylinidae; Pselaphinae; ..." in the keywords; it has no taxon-classification line and the word "Insecta" does not appear (tool summary). Order Coleoptera and family Staphylinidae right; class blank right. All seven names are described as new in this paper ("sp. n."), so the paper is the authority for them.

## Repeats

`git grep` on origin/main (095e055d8) over the whole docs/ tree (evidence, audit/corrected, audit/ALL, sheets, searched, tracks) for the seven binomials, zookeys.251.4099 and article/3442: one hit, docs/views/evidence/desk-d302.jsonl line 2, which is Linan tendothorax (female, about 16 facets) from the same DOI; none of the seven species occurs anywhere on main. Every unmerged origin/research/desk-d* branch other than d311 grepped over the docs/ files it changes against main for the same patterns: only desk-d302 (the same Linan tendothorax record, since merged). No repeat.

## Per line

All male sentences read in the Description, each directly after "Male (Fig. X). Length ...", so each quote starts at a sentence start and ends at the full stop; the head dimensions are part of the printed sentence (semicolon clause). The sentences are telegraphic Description sentences (no finite verb), accepted under audit-395/403 precedent; none is a bare heading or a fragment cut from a longer sentence. "about" is preserved in every value, and "each" makes every count per eye, which the values say ("in each eye"). No Diagnosis, Comparative notes, Distribution or Discussion text mentions eyes or facets for these species or genera, the paper has no key or genus-level eye statement, and it does not say how many specimens were counted (tool summary for absences); each note says so.

### Line 22, Labomimus dabashanus, about 25 facets per eye (male)

"Male (Fig. 1B). Length 2.85–2.96." then "Head slightly longer than wide, HL 0.63–0.66, HW 0.60–0.62; eyes each composed of about 25 facets." **Quote MATCH**. Female: "Eyes each composed of about 20 facets." as in conditions. Holotype "CHINA: W-Hubei (Daba Shan) / pass E of Mt. Da Shengnongjia, / 12 km NW Muyuping, ..." "22.VII.2001"; paratypes "2 ♂♂, 3 ♀♀, same label data as holotype", "1 ♂" from "S-Shaanxi (Qinling Shan) / pass on rd. Zhouzhi-Foping" "4.VII.2001", "2 ♀♀" from W-Hubei NE Muyuping (17.VII 2001): 4 males and 5 females with holotype. Conditions right.

**Line 22 MATCH.**

### Line 23, Labomimus mirus, about 45 facets per eye (male)

"Male (Fig. 1C). Length 3.41–3.75." then "Head slightly longer than wide, HL 0.71–0.72, HW 0.65–0.68; eyes each composed of about 45 facets." **Quote MATCH**. Female "Eyes each composed of about 35 facets." Holotype "Diancang Shan, 3 km / W Dali old town" "1.IX.2003 Wrase"; paratypes 1 ♂ same data (30.VIII.2003), "4 ♂♂" Diancang Shan 45 km NW Dali 29.V.2007, "1 ♀" 27.V.2007: 6 males, 1 female, all Diancang Shan. Conditions right.

**Line 23 MATCH.**

### Line 24, Labomimus paratorus, about 40 facets per eye (male)

"Male (Fig. 1D). Length 3.55–3.87." then "Head longer than wide, HL 0.74–0.76, HW 0.66–0.69; eyes each composed of about 40 facets." **Quote MATCH**. "Female. Unknown." Holotype "Qin Ling Shan / ... Mountain W / pass at Autoroute km 70, 47 km / 2500-2600 m, sifted / 26.-27.08.1995"; paratypes 1 ♂ same data and 1 ♂ "45 km SSE Xi'an" "25.VII.2001". Conditions right.

**Line 24 MATCH.**

### Line 25, Labomimus sarculus, about 25 facets per eye (male)

"Male (Fig. 6A). Length 2.89–3.02." then "Head longer than wide, HL 0.70–0.71, HW 0.66–0.69; eyes each composed of about 25 facets." **Quote MATCH**. "Female. Unknown." Holotype "Gao- / ligong Shan, 32 km SE Tengchong" "26.VIII. / 2009"; paratype "1 ♂, same label data as holotype (cSch)". Conditions right.

**Line 25 MATCH.**

### Line 26, Labomimus schuelkei, about 20 facets per eye (male)

"Male (Fig. 6B). Length 3.92." then "Head longer than wide, HL 0.89, HW 0.78; eyes each composed of about 20 facets." **Quote MATCH**. "Female. Unknown." Holotype only ("(1 ♂)"; tool summary), "Hua Shan Mt. N Valley, 1200- / 1400 m, 118 km E Xi’an" "18.-20.08.1995". Single specimen and single values (HL 0.89) consistent with holotype-only. Conditions right.

**Line 26 MATCH.**

### Line 27, Labomimus vespertilio, about 30 facets per eye (male)

"Male (Fig. 6C). Length 3.34–3.52." then "Head longer than wide, HL 0.70–0.75, HW 0.63–0.65; eyes each composed of about 30 facets." **Quote MATCH**. Female "Eyes each composed of about 25 facets." Holotype "mount. range E Weishan, 12 km NE / Weishan" "15.IX. / 2009"; paratypes "1 ♂, 5 ♀♀, same label data as holotype". Conditions right.

**Line 27 MATCH.**

### Line 28, Pselaphodes distincticornis, about 40 facets per eye (male)

"Male (Fig. 11A). Length 2.74–2.88." then "Head longer than wide, HL 0.59–0.60, HW 0.58–0.59; eyes each composed of about 40 facets." **Quote MATCH**. Female "Eyes each composed of about 30 facets." Holotype "36 km N Dali, ruderal pasture wtih / pines and shrubs, ... 2158 m, litter sifted / under pines and shrubs, 24.VIII.2009"; paratypes "1 ♂, same label data as holotype" and "1 ♀, same label data sa holotype, except 'D.W. Wrase [04]'." The conditions' "same data" for the female passes over the different collector; not counted (optional fix).

**Line 28 MATCH.**

## Verdict

| line | taxon / value | verdict | reason |
|---|---|---|---|
| 22 | Labomimus dabashanus, about 25 per eye (male) | MATCH | whole Description sentence; 4 males, 5 females as printed; female 20 in conditions |
| 23 | Labomimus mirus, about 45 per eye (male) | MATCH | 6 males, 1 female; female 35 in conditions |
| 24 | Labomimus paratorus, about 40 per eye (male) | MATCH | holotype + 2 male paratypes; "Female. Unknown." |
| 25 | Labomimus sarculus, about 25 per eye (male) | MATCH | holotype + 1 male paratype; "Female. Unknown." |
| 26 | Labomimus schuelkei, about 20 per eye (male) | MATCH | holotype only; "Female. Unknown." |
| 27 | Labomimus vespertilio, about 30 per eye (male) | MATCH | 2 males, 5 females; female 25 in conditions |
| 28 | Pselaphodes distincticornis, about 40 per eye (male) | MATCH | 2 males, 1 female; female 30 in conditions |

Errors: 0 of 7 records (0%); 0 fixable, 0 held out, 0 unfixable; no line to drop. Repeats: none (the same DOI is on main only for Linan tendothorax). Verdict for lines 22 to 28 of desk-d311: **ACCEPT** as filed; pool with the six other audits of this unit.

## Replacement

No counted error, so no required replacement. Optional, not counted (each old string occurs once in the line named, checked with `str.count`):

- Lines 22 to 28, `source.title`: "Notes on Michael Schülke's pselaphine" -> "Notes on Michael Schülke’s pselaphine" (curly apostrophe as printed and as main's desk-d302 copy of this title has it).
- Line 28, `conditions`: "and 2 paratypes (1 male, 1 female, same data)." -> "and 2 paratypes (1 male, same data; 1 female, same data except collector D.W. Wrase)."
