# desk-d313: eye states of leaf insects (Phylliidae), a twisted-wing parasite, two thrips, a dustywing and a velvet worm, 16 records

Branch research/desk-d313 from origin/main. About 55 WebSearches and WebFetch only on URLs returned by searches (Pensoft article_preview pages and article XML). `python3 -I tools/senses/check.py | grep desk-d313`: 16 records, 0 problems. Traits: eye_type and ommatidia_count (keys already on main; the note says so where check.py needs it).

Crossref: every api.crossref.org lookup (three DOIs tried) returned PROVENANCE_REQUIRED and was not worked around; each record says so. Citation lines, volumes and page ranges come from the publisher's own article XML or page, licences from the licence sentence printed in the XML (CC0 for ZooKeys 1173, 1018, 1110 under the unit ruling; CC BY 4.0 or 3.0 for the rest). No Crossref licence tag was checked for any record.

Repeat check: every species grepped over origin/main docs/ and the evidence files of all unmerged desk/audit branches (taxon index built once, then single greps, plus DOI greps for ZooKeys 1173, 1018, 1015); no hit for the 16 species.

Filed (docs/views/evidence/desk-d313.jsonl):
1-5. ZooKeys 1173: Phyllium samarense (female, male), P. ortizi (female, male), P. iyadaon (male); compound-eye extent sentences, ocelli sentence in conditions.
6-7. ZooKeys 1018: Cryptophyllium animatum, C. bankoi (males; females unknown).
8. ZooKeys 1110: Vaabonbonphyllium rafidahae (male; female unknown).
9-11. ZooKeys 1256: Phyllium cayabyabi (female, male), P. crapulatum (male).
12. Xenos yangi (Strepsiptera), about 84 ommatidia, ZooKeys 1085 (printed typos kept in the quote).
13-14. Urothrips lancangensis (ZooKeys 694; about 10 facets dorsally, absent ventrally) and Baenothrips cuneatus (ZooKeys 636; about 8 dorsal and 6 ventral facets; quote cut with an ellipsis because the printed sentence is 43 words).
15. Coniopteryx tenuisetosa, "Compound eyes large." (ZooKeys 1015).
16. Oroperipatus tiputini (Onychophora), eyes lateral behind antennal bases, slightly wrinkled (Zoosystematics and Evolution 100(3)).

Dropped candidates:
- Already on main or earlier desks: Tripedalia maipoensis (desk-d294/d304, Zoological Studies, no licence), Mengenilla moldrzyki, Arge similis and Agasicles hygrophila (compound-eye papers), Spinanycta alabamensis (d311), Zorotypus komatsui/vinsoni (d310, d312).
- Sentence not whole or in unreliable pieces: Allochthonius bainiensis, A. pandus, A. xinqiaoensis ("no traces of eyes" is a clause in a semicolon list, ZooKeys 1139); Terrobittacus emeishanicus and T. laoshanicus (ocellar clauses only, ZooKeys 1148); Karnyothrips cyathomorphus (eye clause inside a long sentence, ZooKeys 346); Apterygothrips flavescens (37-word head sentence); Mystrothrips levis (head sentence over the tool's reach); Saussurembia borba and Archembia oruma (eye only as OR ratio in long sentences, ZooKeys 1088).
- Genus-level: Rakaphyllium generic characteristics (ZooKeys 1110), Compsothrips and Ethirothrips diagnoses (ZooKeys 345), Haplothripini papers without eye text (ZooKeys 1176).
- Text not reached: Phylliidae in ZooKeys 1173 beyond P. ortizi (Pulchriphyllium heracles, delislei, bhaskarai, anangu), eleven further Cryptophyllium species (ZooKeys 1018), P. hennemanni (female sentence not verified), P. boislardi, illusorium, morganae, ouelleti (ZooKeys 1256), Coniopteryx serrata (type data not reached).
- No eye text: Pacificampa (Subterranean Biology 27), Palaeoconis (amber, d-earlier scope), Chelicerca/Pararhagadochir Embioptera.
- Unreachable or not open: chiton, scallop, ark clam, cubozoan and echinoderm eye papers (Springer, Royal Society, closed or PMC copies); Plazi treatment pages (redirect placeholders); Zenodo PDFs (binary); Zootaxa.

Angle result: the hexapod orders in the brief gave only telegraphic or clause-level eye text in most open papers; the usable yield was the Phylliidae male/female sentences (full sentences with verbs or participles) and three Pensoft thrips, strepsipteran and neuropteran descriptions. Non-arthropod eye papers returned closed or unreadable copies.

Weak spots for the auditor:
- Crossref not checked (above); licence for 1173, 1018 and 1110 is CC0 as printed in the XML.
- Telegraphic sentences without a finite verb: Xenos yangi, Urothrips, Baenothrips, Coniopteryx ("Compound eyes large.", three words), Oroperipatus (no measurement, position and surface only). Phylliidae sentences use participles ("occupying", "taking up").
- Xenos yangi quote contains printed typos ("ommatidiaprominent", "micortrichia"); read in pieces on three passes.
- Phylliidae male descriptions in P. samarense, ortizi and cayabyabi rest on paratype males (the holotype is a female); said in conditions. Paratype localities for samarense are in a supplement that was not read.
- P. cayabyabi's other authors list: sp. nov. authorship is a subset of the paper's authors (the record lists the paper's byline as printed in the XML, including the single name "Daawia").
- Class blank in all records (no page prints a class); order and family from XML classification or title.
- Facet counts for thrips are dorsal/ventral counts and are filed under eye_type text, not ommatidia_count; Xenos yangi is the only ommatidia_count (84, "about", singular eye).

Questions: none.

## Desk disposition after audits 418-419
Audit 418 (lines 1-8, Phylliidae): 4 fixable errors (lines 3, 4 culture-reared paratypes omitted; lines 6, 7 title dash), fixed; optional fixes applied. Audit 419 (lines 9-16): 2 fixable errors (line 13 male paragraph wording; line 16 paratype dates and 'adult'), fixed; optional fixes applied. 6 errors in 16 (37.5%); none held out or dropped. CC0 on the page was cross-checked against Crossref (vor) for the Phylliidae DOIs and CC BY 4.0 for the others read; one DOI was rate-limited twice for the auditor and rests on the publisher XML. Open owner question: eye_type holds free-text sentences about eye proportions for the leaf insects; the auditors raised no error but the key's intended values should be confirmed.
