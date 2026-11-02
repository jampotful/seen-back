# audit-408: desk-d310, all 5 evidence lines

Audited 1 November 2026 from the desk-d310 files present untracked in the worktree (docs/tracks/progress/desk-d310.md and docs/views/evidence/desk-d310.jsonl, 5 lines; neither committed here, neither edited). HEAD equals origin/main (7b928a5a3). `python3 -I tools/senses/check.py | grep d310`: "docs/views/evidence/desk-d310.jsonl: 5 records, 0 problems". Quote lengths (`len(q.split())`): 18, 10, 35, 19, 31, all within 40.

Sources opened (WebFetch, every URL from a WebSearch result): www.mdpi.com/2075-4450/11/2/120 (two passes), journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0076015 (four passes), www.mdpi.com/2075-4450/13/3/249/html (two passes). Crossref single-DOI lookups api.crossref.org/v1/works/ for the three DOIs, each read on the first call, and for the PLOS correction notice 10.1371/annotation/b18fcad6-597e-4ba9-86bc-f21030ed3a1b. The PLOS correction page itself (journals.plos.org annotation URL, from a search result) was rate-limited twice and not read; a Crossref list query for it failed (client error) and was not retried. PMC, DOAJ, library catalogue records (utm.my, uitm.edu.my, uv.mx, ufrj.br), repository copies (JCU, ANU, Wrocław digilab, kau.edu.sa) and reviewer.ly were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 5 WebSearches.

## Bibliographic and licence

- Line 1 (Dvořáček, Sehadová, Weyda, Tomčala, Hejníková, Kodrík 2020). Byline and Crossref identical in order. Title as printed (Crossref splits it at the colon; the record joins it with ": " as printed). Citation line "Insects 2020, 11(2), 120"; Crossref 11, issue 2, issued 2020-02-12. Licence: page metadata CC BY 3.0; Crossref CC BY 4.0 vor. Accepted. The note's "page body prints no licence sentence" is slightly off: the body carries MDPI's generic "For articles published under an open access Creative Common CC BY license, ..." (printed "Common"), with no version. Not counted; optional fix below.
- Lines 2 to 4 (Narendra, Alkaladi, Raderschall, Robson, Ribi 2013). Byline and Crossref identical in order; title identical; "PLoS ONE 8(10): e76015"; issued 2013-10-14. Page prints "This is an open-access article distributed under the terms of the Creative Commons Attribution License,"; Crossref CC BY 4.0 unspecified. Accepted. The page carries a correction notice dated 12 Nov 2013; Crossref confirms 10.1371/annotation/b18fcad6-597e-4ba9-86bc-f21030ed3a1b is a publisher "correction" with update-to 10.1371/journal.pone.0076015 and no abstract. What the correction changed could not be read (see above). The unit does not mention it. Not counted, because I cannot show that it touches the filed values; the merger should read the correction before filing lines 2 to 4, and an optional note is given below.
- Line 5 (Kilian, Kadej, Cooter, Harvey 2022). Byline and Crossref identical in order; title identical with the em dash; "Insects 2022, 13(3), 249"; issued 2022-02-28. Page metadata CC BY 3.0, Crossref CC BY 4.0 vor. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

- Titanus giganteus: Coleoptera, Cerambycidae from the page as the note says. Right.
- Polyrhachis sokolova: the page prints Formicidae, Hymenoptera and Formicinae only in reference titles (refs 28, 35, 36, 41; tool summary); not in the title, Abstract, headings or Methods, and PLOS ONE has no Taxon classification line. Filling family and order from a printed reference title is acceptable here because the note discloses it, the placement is uncontroversial, and main already files this species under Formicidae, Hymenoptera (canon-4); class blank is right. Not counted.
- Leiodes cinnamomea: order and family from the title "(Coleoptera: Leiodidae: Leiodinae)"; no class printed. Right.

## Repeats

`git grep -il` on origin/main (7b928a5a3) over the whole docs/ tree for "Titanus", insects11020120, "Polyrhachis sokolova", sokolova, pone.0076015, "Leiodes cinnamomea", cinnamomea, insects13030249, Leiodes. Hits: "Titanus" only as Scaphoideus titanus, Dorcus/Serrognathus titanus (other species); "cinnamomea" only as Osmunda cinnamomea and Coltricia cinnamomea; Leiodes only in gaps/queue/taxonomy/searched files (no evidence). Polyrhachis sokolova is on main once: canon-4 acuity_cpd 0.08 from the Feller et al. 2021 compilation (10.1016/j.asd.2020.101002), a different trait and DOI, so lines 2 to 4 do not repeat it. Unmerged origin/research/desk-d* branches other than d310 (all of them, d1 to d309) grepped in one `git grep -il -E` over docs/ for the three species and three DOIs, excluding canon-4 and gaps copies inherited from main: completed, no hits.

## Per line

### Line 1, Titanus giganteus, apposition compound eye ("It seems")

Discussion 4.2: "It seems that the Titanus compound eye is of the apposition type that is typical for diurnal insects." **Quote MATCH**, whole sentence, 18 words. Value carries the hedge; "apposition compound eye" is what the quote says. Results 3.2 "It looks that a clear zone separating the dioptric apparatus from the photoreceptive structures was not developed ... the eye thus resembled an apposition eye", "hundreds of mostly hexagonal ommatidia", regular central and irregular peripheral facets, "an undetermined number of retinula and pigment cells", "Titanus is known to fly at night, but its apposition ommatidium also suggests diurnal activity.", and "one individual is not sufficient for a deep ground-breaking study" all carried. Specimen: "a male Titanus giganteus collected 12 January, 2019 in French Guiana in Montagne de Kaw, Camp Patawa.", "The male was attracted to light (250 W) at 1.30 h after midnight.", "assayed within 10 days from the time of capture"; n = 1 (Introduction). SEM of the eye surface and "the cross section of the eye" right.

Fault: **specimen state misstated.** Conditions call it "One dead adult male". The page does not say the beetle was dead; section 2.1 is silent on it, and 2.2 says "The animal was decapitated using of surgical scissors under the deep carbon dioxide anesthesia," which is done to a live animal. The same sentence calls it "a 250 W light trap"; the page says only "attracted to light (250 W)". One record error, fixable.

**Line 1 FIXABLE.**

### Line 2, Polyrhachis sokolova, 596.2 facets per eye

Results: "Each compound eye has 596.2±51.7 (n = 5) facets (Fig. 2)." The quote "Each compound eye has 596.2±51.7 (n = 5) facets …" ends with "…" in place of the trailing "(Fig. 2)" only; nothing else follows "facets". This is a legitimate trailing cut marker for a figure reference under rules.md; no qualifier is dropped. **Quote MATCH**, 10 words. Per eye stated by the quote ("Each compound eye"), so no per-eye/both ambiguity. Methods "We determined facet numbers and facet diameters of five individuals."; workers "from two nests in the mangrove habitats of Pallarenda ... Townsville, QLD, Australia." (no date); "The ants are monomorphic and exhibit very little variation in body size (body length: 10.82±0.12 mm; head width: 1.86±0.10 mm; n = 5)." Discussion "(590)" contrast carried. The Abstract gives "596 ommatidia per eye" (consistent with the value).

**Line 2 MATCH.**

### Line 3, Polyrhachis sokolova, facet diameter 23.5 µm

Results: "They have an average facet diameter of 23.5±3.0 µm (mean ± s.d., n = 50, 5 animals), with the largest facets (33 µm) found in the posterior and ventral region of the eye (Fig. 2)." **Quote MATCH**, whole sentence with figure reference, 35 words. Same five workers as line 2 (Methods "facet numbers and facet diameters of five individuals"). Units right. The Abstract headlines "large lenses (33 µm in diameter)"; the conditions carry the 33 µm maximum.

**Line 3 MATCH.**

### Line 4, Polyrhachis sokolova, rhabdom length 79 to 135 µm

Results: "The length of the rhabdom varied from 79 µm (dorsal) to 135 µm (frontal) to 113 µm (ventral) region." **Quote MATCH**, 19 words; value range and units right; same caste (workers); no n in the sentence, as the conditions say.

Faults (one record error, fixable): (a) **method unsupported.** The `method` says the length came from "one-micron cross-sections of ommatidia". The Methods say "One-micron thick cross-sections of ommatidia from the frontal region of the eye and of the dorsal region of the eye were cut ..." but do not say how rhabdom length was measured; length is not readable from cross-sections, and the page shows "longitudinal sections and illustration of a single ommatidium" only in the Figure 4 caption (tool summary for the absence). (b) **adaptation state omitted.** The Histology Methods fixed eyes "under natural light conditions at 10 am (light-adapted) and at 10 pm (dark-adapted)", and the rhabdom changes with state ("The diameter of the distal rhabdom in the light-adapted eye was 5 µm", "In the dark-adapted eye the rhabdom diameter increased to 6 µm and the retinula cell pigments migrated away from the rhabdom."). The length sentence names no state; the conditions should say so.

**Line 4 FIXABLE.**

### Line 5, Leiodes cinnamomea, larval stemmata absent; adults have eyes

Discussion, read in three consecutive pieces: "Stemmata are absent but adults have eyes present, whereas, among Leiodinae," / "eyes are absent in both adults and larvae in inquilines such as S. meliponae" / "and Scotocryptodes germaini Portevin, 1907 [38,39,50]." Previous sentence ends "... Scotocryptus meliponae Girard, 1874 [38]."; next begins "Antennae are, proportionally to the size of the cranium, ...". **Quote MATCH**, one whole sentence from one section, 31 words as check.py counts. Scope: the sentence follows a comparison of this species' larval head with other Leiodinae larvae, so "Stemmata are absent" is about L. cinnamomea larvae; the genus and tribe get no stemmata statement ("for Leiodini, only L. cinnamomea has been described"). Results 3.2 ("Description of the Immature Stages of Leiodes cinnamomea"): Body paragraph "without stemmata" and Head "Stemmata absent." precede the Instar I/II/III sub-entries, so "instars I to III" is supported (tool summary). Material: England, Wiltshire, "ex. adults" from Tuber aestivum (23.11.2014, January and September 2015, leg. J. Cooter); Poland near Sękocin and Pińczów, from T. excavatum, 31.08 to 17.11.2015 (10 larvae, 2 adults); 20 larvae cultured; slides 2 + 2 + 1, SEM one per instar: as in conditions apart from the Polish field counts (optional fix). Light-response hypothesis carried; the Introduction also says "Both adults and larvae are photophobic." (optional).

**Line 5 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Titanus giganteus, apposition eye ("It seems") | FIXABLE | conditions | beetle called "dead", though decapitated under deep CO2 anaesthesia; "light trap" for "attracted to light" |
| 2 | Polyrhachis sokolova, 596.2 facets per eye | MATCH | | trailing "…" replaces "(Fig. 2)" only; per eye stated |
| 3 | Polyrhachis sokolova, facet diameter 23.5 µm | MATCH | | same five workers; 33 µm maximum carried |
| 4 | Polyrhachis sokolova, rhabdom length 79-135 µm | FIXABLE | method, conditions | length attributed to cross-sections the paper does not say; light/dark-adapted fixation and 5 vs 6 µm rhabdom diameter omitted |
| 5 | Leiodes cinnamomea, larval stemmata absent | MATCH | | one whole 31-word sentence; scoped to this species' larvae |

Errors: 2 of 5 records (40%); 2 fixable (lines 1, 4), 0 held out, 0 unfixable; no line to drop. Repeats: none. Higher taxa for Polyrhachis acceptable as disclosed. Open item, not counted: the 12 Nov 2013 PLOS correction to the Polyrhachis paper was not readable here; check it before filing lines 2 to 4, and drop them if it changes a filed value. Verdict for desk-d310: **ACCEPT AFTER REPLACEMENT** (lines 2, 3, 5 as filed; lines 1 and 4 with the replacements below, or dropped if they are not applied).

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 1:
- `conditions`: "One dead adult male (n = 1) from a 250 W light trap at Montagne de Kaw" -> "One adult male (n = 1; weight 37.5 g, length 155 mm) attracted to a 250 W light at 1.30 h after midnight at Montagne de Kaw"

Line 4:
- `method`: "one-micron cross-sections of ommatidia (Methods: histology of the frontal and dorsal regions of the eye)" -> "histology of the eye (Methods: one-micron cross-sections of the frontal and dorsal regions; Fig. 4 shows longitudinal sections); the paper does not say how rhabdom length was measured"
- `conditions`: "the Methods say sections were cut from the frontal and dorsal regions, and the ventral value is also printed here." -> "the Methods say sections were cut from the frontal and dorsal regions, and the ventral value is also printed here. Eyes were fixed light-adapted (10 am) and dark-adapted (10 pm), and the length sentence does not say which state it refers to; the rhabdom diameter changes with state ('The diameter of the distal rhabdom in the light-adapted eye was 5 µm'; 'In the dark-adapted eye the rhabdom diameter increased to 6 µm')."

Optional, not counted:
- Line 1 `note`: "page body prints no licence sentence (page metadata CC BY 3.0)" -> "page body prints only MDPI's generic 'Creative Common CC BY license' sentence, no version (page metadata CC BY 3.0)"
- Lines 2, 3 and 4 `note`: "Crossref CC BY 4.0 with content-version unspecified (accepted). " -> "Crossref CC BY 4.0 with content-version unspecified (accepted). A correction was published 12 Nov 2013 (10.1371/annotation/b18fcad6-597e-4ba9-86bc-f21030ed3a1b); its content was not read."
- Line 2 `conditions`: "The ants forage day and night; the Results have no subsections." -> "The Abstract gives '596 ommatidia per eye'. The ants forage day and night; the Results have no subsections."
- Line 5 `conditions`: "and T. excavatum near Sękocin and Pińczów, Poland (2015);" -> "and T. excavatum near Sękocin and Pińczów, Poland (31.08 to 17.11.2015; 10 field-collected larvae and 2 adults); the English material is listed as 'ex. adults';"
- Line 5 `conditions`: "offered as a hypothesis." -> "offered as a hypothesis; the Introduction says 'Both adults and larvae are photophobic.'"
