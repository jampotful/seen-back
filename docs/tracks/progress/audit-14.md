# Precision audit 14, 15 October 2026

Scope: every evidence record in sweep-90, sweep-91 and sweep-92. sweep-93 has no evidence file. The audit covers 8 records (sweep-90: 2, sweep-91: 2, sweep-92: 4). No sampling; all were opened.

Method as in audits 12 and 13: each source opened with WebFetch and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces of at most about 125 characters, with split points in `where`; corrected quotes are 40 words or fewer. Verdicts: `confirm`, `requote`, `correct`, `retract`, `unverifiable`. Typographic differences count as `confirm`; a change to the partial flag or the grade counts as `correct`. Corrections are in `docs/views/recheck/recheck-14.jsonl` in the recheck-5 schema. No evidence file, no wanted file and not `docs/views/audit/ALL.jsonl` was edited.

## Table

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| sweep-90:1 | Phodopus sungorus / receptor_classes | m | confirm | verbatim (Cambridge abstract), conclusion (2), split after "in the ultraviolet"; the clause continues "one with maximum sensitivity in the ultraviolet (c. 360 nm), the other with peak sensitivity closely similar to that of its rod". Metadata matches: Visual Neuroscience 16(1): 53-63, 10.1017/S0952523899161029. Purchase "temporarily unavailable", so the flag stands |
| sweep-90:2 | Phodopus sungorus / lambda_max_nm 360 | m | confirm | verbatim, same sentence; "c. 360 nm" logged as 360 with the qualifier kept in the quote. The second cone has no number in the abstract, as the note says |
| sweep-91:1 | Cervidae / receptor_classes 2 | g | correct | quote verbatim (MDPI, Section 2) but cut mid-sentence; it continues "and recognizing multiple forms of camouflage." A review statement resting on cited studies, so by the audit-5 ruling it carries `partial: true` with its sources named. Requoted to Section 3: "cervids possess S-cone, M-cone, and rod photoreceptors ... [47,48,59,68,92]" |
| sweep-91:2 | Cervidae / tapetum | g | correct | quote verbatim (Section 2), split after "allows the eye", but it describes light capture and cites [30,57,78]. The sentence that states the trait opens Section 2: "a reflective tapetum lucidum [57,69,77]". Flag set to `partial: true`, requoted |
| sweep-92:1 | Mesocricetus auratus / receptor_classes | m | confirm | verbatim, conclusion (3), one piece. Taxon pairing correct: the abstract gives two cone classes to Phodopus and one to Mesocricetus |
| sweep-92:2 | Mesocricetus auratus / lambda_max_nm 506 | m | confirm | as 92:1; "about 506 nm". The rod peak "about 498–500 nm" is stated for both species |
| sweep-92:3 | Mesocricetus auratus / receptor_classes | m | confirm | verbatim (vetdoc.vetmeduni.ac.at), split after "colocalizes"; the abstract adds "Only double-labeled cones were found." Metadata matches: Brain Research 929(1): 139-146, 10.1016/S0006-8993(02)02267-9. No full-text link |
| sweep-92:4 | Mesocricetus auratus / receptor_classes | m | confirm | verbatim (Northumbria portal), including the space in "blue- /UV-sensitive"; the authors' own result is green cone opsin by immunocytochemistry and RT-PCR, and the abstract calls the hamster "a green cone monochromat". The 501 nm ERG value belongs to unnamed "other investigators" and is rightly left out. Metadata matches: 770(1-2): 131-138 |

**Rate: 2 errors in 8 verifiable records, 25%** (0 unverifiable). Every quote is verbatim. Both errors are the same kind: a family-level review statement filed as a primary full-text record, with a quote that stops mid-sentence and does not state the logged value.

## Checks the desk asked for

- **Calderone and Jacobs 1999 taxon-to-value pairings.** Checked against the twelve abstract pieces on the Cambridge page. Conclusion (2) gives Phodopus sungorus two cone classes, one near 360 nm and one close to the rod peak; conclusion (3) gives Mesocricetus auratus one cone class near 506 nm and no second cone. Records 90:1, 90:2, 92:1 and 92:2 pair each value with the right species. Authors, year, volume, issue, pages and DOI match the page.
- **Abstract-only records carry `partial: true`.** Yes for all six abstract records (90:1, 90:2, 92:1 to 92:4); none of the three source pages offers the full text. The two Cervidae records were `partial: false` on an open review whose statements are secondary (corrected).
- **Records with `partial: true` whose full text is open.** None found. The Cambridge, vetdoc and Northumbria pages link only to the publisher.
- **Pooled or unnamed-species records are `g`.** The two family-level Cervidae records are `g`. Every other record names one species and is `m`.
- **Encyclopedia and database sources.** None.
- **Values quoted from another study.** The Cervidae values come from a review and now carry their reference numbers (91:1, 91:2). 92:4 correctly leaves out the 501 nm value that the abstract borrows from unnamed investigators. The page's reference list stops at [33], so references [47] to [92] are named by number only.
- **Converted or estimated values.** None. 90:2 logs "c. 360 nm" as 360 and 92:2 logs "about 506 nm" as 506, each with the qualifier in the quote.
- **Metadata.** All four sources match the opened page.

## Wanted lines (not edited)

- **sweep-93, Kott, Sumbera and Nemec 2010.** Confirmed on the DOAJ record: Ondrej Kott, Radim Sumbera, Pavel Nemec; PLoS ONE 5(7): e11810; 10.1371/journal.pone.0011810. The abstract names two species, "the silvery mole-rat Heliophobius argenteocinereus and the giant mole-rat Fukomys mechowii", and tests white, blue, green-yellow, ultraviolet and red light, so `for` could add Fukomys mechowii. The PLoS page itself served a different article (Davis and Keisler 2016, e0150598) under both the encoded and plain URLs, the same fault audit 13 met.
- **sweep-91, Hetling et al. 2005.** Authors, year, title, J Comp Physiol A 191: 317 and 10.1007/s00359-004-0584-6 match the reference list of McMullen et al. 2010 (PMC3086521), which spells the third author Comer. The Reed course page that the line cites for authors prints "Corner, Christoper M." and "funtion", so it is the weaker source. The Springer page was refused.
- **sweep-91, Peichl, Nemec and Burda 2004.** Authors, year, title, Eur J Neurosci 19 and start page 1545 match the ESTHER record (PubMed 15066151), whose abstract names Heterocephalus glaber and says "In all three species, the vast majority of the cones were strongly S-opsin-immunoreactive." The end page and DOI are not on that page; the Wiley page returned a fetch error.
- **sweep-91, Nemec et al. 2008.** The title is cut short. The Czech research register (STARFOS, RIV/00216208:11310/08:14084) gives "The visual system in subterranean African mole-rats (Rodentia, Bathyergidae): Retina, subcortical visual nuclei and primary visual cortex", Brain Res. Bull. 75(2-4), 2008, with 12 researchers whose names the page did not return. The DOI resolves to Elsevier PII S0361923007003309, which fits Brain Research Bulletin (ISSN 0361-9230), but the Elsevier page came back empty, so the pages and author list remain unchecked.
- **sweep-91, Schiviz et al. 2008.** Authors, year, title, J Comp Neurol 507: 1336-1350 and 10.1002/cne.21626 match reference [31] of the Newman and D'Angelo review; the Wiley page was not reached. The review sentence that names the northern pudu as lacking the dorsotemporal extension carries no citation; the [31] citation belongs to the southern pudu sentence before it. The review spells the species "Pudu mephitophiles".

## Rows written

`recheck-14.jsonl`: 2 rows, both counted. 91:1 and 91:2 (`correct`: partial flag, quote, `where`, note, and the method of 91:1).

## Blocked pages

- The MDPI page text ends partway through reference [33], so the primary sources behind [47] to [92] were not read; a curl to www.mdpi.com was refused by the egress proxy, and a Europe PMC query was rate-limited (HTTP 429) with an instruction not to retry.
- journals.plos.org served the wrong article for 10.1371/journal.pone.0011810.
- link.springer.com (10.1007/s00359-004-0584-6) and api.crossref.org were refused at the permission step; onlinelibrary.wiley.com returned a fetch error; pubmed.ncbi.nlm.nih.gov and linkinghub.elsevier.com returned empty pages.

## Patterns (this run)

1. A review can enter the log as `partial: false` because its full text is open. The flag answers whether the value was read in the study that measured it, and a review statement never is; the addlog check could ask for `partial: true` whenever `method` begins "review statement".
2. Quotes cut at a fixed length (here two 15-word clauses) can stop before the words that carry the value. Quoting the whole sentence, or the clause that names the trait, would have caught that 91:2's sentence was about light capture.
3. Wanted lines drawn from reference lists and course pages carry their typos and truncations (Hetling's "Corner", Nemec's short title). One fetch of a register or publisher record fixes them at filing.
4. The PLoS fetch fault recurs: journals.plos.org can return a different article for a given DOI. DOAJ gives the metadata reliably.
