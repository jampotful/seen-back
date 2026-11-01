# desk-d220 progress

Scope: animal sensory-trait records from open full text (MDPI CC BY). Records are in docs/views/evidence/desk-d220.jsonl; check.py reports 0 problems for the unit. Species and DOI were checked against origin/main (evidence, audit/corrected, audit/ALL, sheets, progress notes) before each paper was opened. About 33 WebSearches and 45 WebFetch pages.

## Records (4)
- Trialeurodes vaporariorum (greenhouse whitefly), Insects 11(2): 94, behaviour_vision: green LED (525 nm) traps more attractive than yellow or UV LED traps (Abstract sentence). The Results sentence that adding UV did not change the green LED catch, the rotated (not randomised) block layout and the unstated adult/nymph count are in conditions.
- Trichogramma japonicum, Insects 17(8): 798, sense_chemical: citral at 0.001 ug/uL and linalool at 0.1 ug/uL named as attractive in a four-arm olfactometer (10 s stay criterion; no p values in text; other concentrations not reported).
- Orius maxidentex, Biology 15(8): 658, sense_chemical: 10 ug/uL beta-bisabolene the most attractive single Celosia volatile in a Y-tube; the EAG null for methyl salicylate and the Y-tube nulls are in conditions.
- Papilio polytes, Insects 17(5): 452, sense_chemical: females attracted to linalool, citronellol and citronellal at 1 x 10^6 ng in a Y-tube (laboratory colony, 25 males and 25 females per combination).

## Held out
- Trogonophis wiegmanni (PeerJ 9: e10780, CC BY): tongue-flick results sentences are 127 to 139 characters; the page-summary tool cuts quotes at 125 characters, so no whole sentence carries a value.
- Oligota pygmaea and Parastethorus histrio (Insects 17(10): 1048): first fetch returned the O. pygmaea live-prey sentence as under 125 characters, second fetch said it is longer; not confirmed whole.
- Xylocoris flavipes volatiles / Tribolium castaneum and Oryzaephilus surinamensis (Insects 16(1): 31): the 200 ug/mL repellency sentence covers both prey species (Figure 4A,B,D,E), so a single-species record would be pooled.
- Liolaemus tenuis and L. lemniscatus (Diversity 15: 831), Scolia hirta sensilla (Insects 17(2): 160, sensilla types are structure, not a sense_chemical response), Eretmocerus eremicus (Insects 17(3): 329, only an unnumbered abstract null), Dociostaurus maroccanus EAG (Insects 17(2): 176, sentences carry no values), Thrips hawaiiensis (Insects 11(7): 408), Amo and Saavedra birds (Biology 10: 1010, pooled tit species, Discussion sentence only), African mole-rat bone conduction (a review), Agalychnis callidryas light-cued hatching (PeerJ 6018, key sentences over 125 characters).
- Blocked: frontiersin.org (fevo.2021.583837, fnint.2020.561524, fevo.2021.631762) and journals.biologists.com (jeb251478) returned PROVENANCE_REQUIRED after earlier Frontiers pages had opened; not retried.
- Already on main by species or DOI: Ischnura heterosticta, Arctocephalus forsteri, Danio/Notemigonus vision, Asiophrida, Endebius, Encarsia, Zeugodacus, Spodoptera frugiperda, Diaphorina, sea turtle colour preference, schizothoracine phototaxis, Ixodes/Amblyomma thermal.

## Advice
Main is saturated for open Insects, Animals and Frontiers 2020 to 2025 papers; 2026 MDPI papers (Insects 17, Biology 15) were the one vein not yet on main. The page-summary tool returns whole sentences only when they are 125 characters or fewer, so papers with short Results sentences (olfactometer papers listing concentrations) are the ones that can be filed.

## Owner questions
- Families for Orius (Anthocoridae) and Papilio (Papilionidae) are from general knowledge because GBIF refused and the pages do not print families; Trichogrammatidae and Aleyrodidae are printed by the papers or already on main.
- Three of the four papers show CC BY 3.0 in page metadata and CC BY 4.0 in Crossref; say if a version mismatch should hold a record.

## Desk disposition after audit 306

Audit 306 judged 3 of the 4 records: 2 in error (66.7% of those judged), both fixable. Line 1 (Trialeurodes vaporariorum behaviour_vision, Insects 11: 94) was unchecked because the MDPI, PMC and PubMed pages were all refused to the auditor (its quote matches the Crossref abstract); the desk held it out of the merge rather than file a record no auditor read in full. It stays a held lead: retry if a Results page opens (the Abstract adds that the green LED trap caught more than twice the whiteflies of the yellow sticky card alone under summer shading, sunny or cloudy). Line 2 (Trichogramma japonicum): 10 ug/uL linalool was repellent at the 30 and 60 s stay thresholds, and the text does give other concentrations; corrected. Line 3 (Orius maxidentex): the head-to-head chi-square tests behind "most attractive" added (p = 0.028, 0.001, 0.003), family printed in the Abstract (Anthocoridae); corrected. Line 4 (Papilio polytes) stood, with the optional wording fixes applied. Three records merged. Pooled audits 172 to 306: 324 of 725 (44.7%).

Owner questions: Aleyrodidae is not on main and was not confirmed on a page; Papilionidae (Papilio polytes) and Trichogrammatidae are on main; CC BY 3.0 page metadata against CC BY 4.0 on Crossref accepted as a version difference.
