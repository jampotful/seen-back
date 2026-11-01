# desk-d297: eye states and counts in cave and soil insects other than beetles, springtails and ants, 9 records

Branch research/desk-d297 from origin/main. About 35 WebSearches (4 extended) plus fetches; every fetched article URL came from a WebSearch first. `python3 -I tools/senses/check.py | grep 'd297\.'`: 9 records, 0 problems. Crossref read by DOI for Animals 13(20) 3199, ZooKeys 135, Subterranean Biology 19 and 37, ZooKeys 1232 (list query) and DEZ 63 (list query); Subterranean Biology 51 by list query. All CC BY (3.0 for ZooKeys 135, 4.0 elsewhere), vor; author order matches the pages. Grep of main docs/ and desk/audit branch evidence and progress by species: no repeats (hits for "cordiformis" and "appendiculata" are a crab and a Lobelia). New traits: eye_bridge_width_facets (Camptochaeta); ommatidia_count already used on main.

Filed (docs/views/evidence/desk-d297.jsonl), all Insecta:
1. Cixius theseus (Cixiidae), "Compound eyes and ocelli absent.", Head; holotype male, paratype female, nymphs.
2. Cixius palmirandus, Habitus sentence, compound eyes absent; holotype male only.
3. Nocticola appendiculata (Nocticolidae), "eyes reduced", surface species found under rocks; holotype male, paratypes 3 males 1 female.
4. Nocticola cordiformis, "Eyes well developed" contrast record; same paper.
5. Iuiuia caeca (Kinnaridae), compound eyes absent, DEZ 63(2); holotype male, paratypes 7 males 2 females; lateral ocelli vestigial noted.
6. Valenciolenda fadaforesta (Kinnaridae), "Compound eyes and ocelli absent."; holotype and paratypes of both sexes, nymphs separate.
7. Spelaeometra hypogea (Hydrometridae), "composed of just seven ommatidia"; per-eye reading not stated outright.
8. Nocticola gonzalezi, "Eyes reduced to 3-4 distinct facets." nymph stage only (d291 had set it aside as nymphs; stage is stated in the record).
9. Camptochaeta prolixa (Sciaridae), eye bridge 1-2 facets wide (male); Abstract and Discussion say the bridge is reduced in some specimens.

Dropped:
- Sentence only returned in pieces or longer than the tool returns: Tachycixius gomerobscurus and Meenoplus skotinophilus Head and Habitus (SB 51), Spelaeodelphax nexus (SB 55, 127-character Head sentence), Nocticola baiguensis (eye clause inside a semicolon list, only the clause came back), Zorotypus komatsui (ZooKeys 1178, apterous male Head sentence of 37 words returned in part).
- Clauses, not sentences: Gryllotalpa xinjiangica (ZooKeys, eyes in a clause list), Eurhaphidophora (eyes black, not a state of interest).
- No eye sentence in the paper: Spinanycta alabamensis (SB 49), Pacificampa (Campodeidae, SB), Turkmenocampa, Cylindrogaster cavernicola (ZooKeys 713: "Eyes prominent, slightly shorter than post-ocular length", no state or count; also set aside by d293).
- Blocked: europeanjournaloftaxonomy.eu downloads (PROVENANCE_REQUIRED) for the New cave japygids and Tachycines papers; subtbiol issue PDF 823980 (client error).
- Wrong page returned: subtbiol article_preview id 175661 returned the Spinanycta paper and zoom/fig/15 gave the Spelaeodelphax title only; filed nothing from either.
- Not in angle: Geopselaphus bullonorum (beetle), Ptomaphaginus troglodytes (beetle), Tritomurus veles (springtail), Raveniola yangren (spider).
- Closed or third-party: Zootaxa/mapress items (Ferricixius, Hainan Cixiidae, Rhaphidophoridae), Plazi, zenodo, PMC, ResearchGate, ICMBio repository copies.
- Searches for Dermaptera, Psocodea, Plecoptera/Trichoptera, Hymenoptera cave parasitoids, mole crickets, Hawaiian Oliarus, Protura/Archaeognatha and cave Diptera (other than Camptochaeta) returned closed journals, Plazi or items without eye sentences; nothing filed.
