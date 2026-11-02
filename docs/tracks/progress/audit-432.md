# audit-432: desk-d320 lines 9 and 10 (Myctophidae, Table 3 eye diameter)

Scope: 1-based lines 9 and 10 of docs/views/evidence/desk-d320.jsonl only (lines 1 to 8 audited separately). Line 9 is Ceratoscopelus maderensis, line 10 is Centrobranchus andreae. Searches used: 4 WebSearch; WebFetch on pages returned by those searches plus one Crossref list query.

Source opened: pmc.ncbi.nlm.nih.gov/articles/PMC3589346 (returned by WebSearch; it served the article, no reCAPTCHA). Page citation: de Busserolles F, Fitzpatrick JL, Paxton JR, Marshall NJ, Collin SP. Eye-Size Variability in Deep-Sea Lanternfishes (Myctophidae): An Ecological and Phylogenetic Study. PLoS One. 2013 Mar 5;8(3):e58519. doi:10.1371/journal.pone.0058519. Licence on the copy read: "This is an open-access article distributed under the terms of the Creative Commons Attribution License". Crossref list query (prefix 10.1371, pub date 2013-03-05): same DOI, same five authors in the same order, PLoS ONE 8(3) e58519, issued 2013-03-05, licence http://creativecommons.org/licenses/by/4.0/ content-version unspecified. Accepted under the "unspecified + page-printed CC Attribution License" ruling; no conflicting tag.

Page facts checked: Table 3 sits in Results, subsection "Morphometric measurements"; caption "Range of standard length, eye diameter and lens diameter for each of the 61 species of Myctophidae analysed in this study." (no units in caption; mm from Methods "measured with digital calipers to 0.1 mm" and Results "eye and lens diameter range from 1.5 mm to 11.1 mm"). Footnote: "A = adult, J = juvenile"; "?" undefined. Methods: "rostro-caudal eye diameter (measured in situ)"; most specimens measured fresh on board before fixation; cruises 7, 8, 9 (collaborator samples) measured after fixation, fixatives 5% buffered formalin and Karnovsky's; no fresh/fixed correction. Table 1: cruise 1 Coral Sea, 11/2009, RMT/plankton net/neuston net, night, 4% PFA, Karnovsky; cruise 8 Balearic Islands, Western Mediterranean Sea, 07/2010, double-warp modified commercial mid-water trawl/IKMT, day and night, Karnovsky. Comparison rows quoted in conditions match the page (M. lychnobium 4, 4.8–11.1; N. idostigma 8, 1.5–3.9). Neither species is named in Results or Discussion prose; the only related text is the genus-level remark that Gonichthyini (Loweina, Gonichthys, Centrobranchus) "appear to have smaller eyes", a relative-eye-size statement that does not contradict a single absolute value.

Names: Ceratoscopelus maderensis (Lowe, 1839) has its own FishBase species summary under Myctophidae, Myctophiformes; Centrobranchus andreae Lütken, 1892 is listed under that name on OBIS (WoRMS 272653), Myctophidae, Myctophiformes. No synonym found for either.

Repeats: git grep of origin/main docs/ (evidence, audit incl. corrected and ALL, sheets, searched, notes, progress) for "Ceratoscopelus", "Centrobranchus", "pone.0058519" and "Busserolles": no hit for either species or the DOI under any trait. Busserolles hits are other papers (Stieb et al. 2019, Caves et al. 2021, Cechetto et al. 2020, and the 2014 photoreceptor paper in audit-338/desk-d243 for Bolinichthys longipes, a different DOI and species). oa-5 line 1067 is an order-level review row, not these species.

## Verdicts

- Line 9 (Ceratoscopelus maderensis, 5.1 mm): OK. Quote is the whole Table 3 row (9 words) and matches the page; value, n = 1, SL 52, lens 2.1, stage A, cruise 8, fixation after Karnovsky's, method and units are all as printed; authors, order, title, journal, volume, issue, year and DOI match page and Crossref.
- Line 10 (Centrobranchus andreae, 2.2 mm): OK. Whole Table 3 row (9 words) matches; n = 1, SL 31.5, lens 0.8, stage "?" (undefined), cruise 1 measured fresh (cruise 1 is outside the 7 to 9 post-fixation set), fixatives 4% PFA/Karnovsky per Table 1; source fields match.

Errors: 0.

## Replacement

None required.

## Optional fixes (not errors)

- Line 9, conditions: "mid-water trawl, day and night)" -> "double-warp modified commercial mid-water trawl/IKMT, day and night; Table 1 lists Karnovsky's fixative for cruise 8)". The record's "(Karnovsky's fixative or 5% buffered formalin)" is the Methods sentence for cruises 7 to 9 as a group; Table 1 gives only Karnovsky's for cruise 8.
- Line 10, note: could add that the Results' only Centrobranchus mention is the genus-level relative-eye-size remark (Gonichthyini "appear to have smaller eyes"), so readers do not take the paper as silent on the genus.
