# desk-d504: eye state of one Thai scorpion (1 record)

Branch research/desk-d504 from origin/main. Angle override followed: no eye_diameter_mm search; existing eye-state keys (eye_type, eyes_count, ommatidia_count) for species not on main, from open-licence taxonomic papers, cave and subterranean fauna first. About 45 WebSearches; WebFetch only on URLs returned by searches. Crossref list queries were refused (PROVENANCE_REQUIRED) and not retried.

Trait key precedent read before filing: eye_type has 396 untyped lines on main, including Euscorpiops lii (desk-d305, ZooKeys 968) and Euscorpiops krachan (desk-d335, ZooKeys 1193), the same kind of sentence. check.py does not require evidence_kind for eye_type; `python3 -I tools/senses/check.py` gives 1 record, 0 problems for this file, and no line of desk-d504 appears under --require-evidence-kind.

Filed (docs/views/evidence/desk-d504.jsonl):
1. Euscorpiops doiphukha, eye_type, ZooKeys 1241: 171-184 (2025), Morphology sentence "Median eyes anterior to the middle of carapace; three pairs of lateral eyes, the third pair only slightly smaller than the first two." Page prints the CC BY 4.0 sentence. Authority: The Scorpion Files Scorpiopidae page lists E. doiphukha (Ythier, Kosulic, Nawanetiwong & Lourenco, 2025). Filed at genus rank as main does for E. krachan and E. lii. Desk d365 had seen this paper and filed nothing.

Dropped (all grepped on main by species and DOI; on main unless stated):
- On main: Erhaia dijiang, Girardia multidiverticulata, Gammarus tumaf, Iuiuia caeca, Valenciolenda fadaforesta, Troglocoelotes sinanensis, Cylindroiulus villumi, Hyleoglomeris rukouqu/xuxiakei, Glyphiulus maocun, Iandumoema smeagol, Triplophysa xiuwenensis, Sinocyclocheilus wanlanensis, Euscorpiops lii and krachan, Sarax timorensis, Geopselaphus bullonorum, Ptomaphaginus troglodytes, Nereis tricirrata, Acherontiella nezamdoosti and palaciosi, Microstomum laurae.
- No eye sentence in the paper: Cimmeritodes parvus / Wanoblemus wui (ZooKeys 625), Pacificampa spp. (Subterranean Biology 27), Quapawjapyx osage / Holjapyx nimiipuu (EJT 1043), Eukoenenia serrana (Subterranean Biology 57), Scolopendrellopsis glabrus and Symphylella spp. (Symphyla, ZooKeys 789, 845, 1003), Geophilus hadesi (ZooKeys 510), Ithyleucon sorbei (ZooKeys 235), Sinocyclocheilus xingrenensis (ZSE 101).
- No licence sentence on the page: Niphargus hasansarii (Ege J Fish Aquat Sci 43(2), "eyes absent", copyright line only); Triplophysa xiuwenensis blog page.
- No count or state in a quotable sentence: Nipponnemertes incainca (eyespot sentence long, no count; also dropped by d294 and d301); Eupera troglobia (statements are about the group, not the species).
- Closed, restricted or not reachable: Hyalella troglofugia (Zootaxa), Triplophysa nayongensis and Scorpiops bahunetra (Wiley / Elsevier, no open page reached), Sinocyclocheilus changlensis (PMC refused), Scorpiops kovariki, deshpandei, matthewi and Chaerilus herta (Euscorpius, no licence sentence expected), Hylomus yuani / Eutrichodesmus jianjia / Trichopeltis liangfengdong (Subterranean Biology 30; treatments not in the XML windows the fetch returned).
- Caridina tashanica (Subterranean Biology 55) is on main under d290.

Weak spots for the auditor:
- The eye sentence arrived from the fetch tool in two pieces ("...three pairs of lateral eyes," then "the third pair only slightly smaller than the first two."); both passes agree and the preceding and following sentences were returned separately, so it is read as one sentence.
- Crossref not checked (refused); licence rests on the page-printed sentence. Volume 1241, no issue printed.
- The median eyes are named without a count; the value says so.
- Authority page is The Scorpion Files (no WoRMS/GBIF, which the fetch tool refuses).

Angle result: the cave and soil invertebrate eye-state pool reachable through Pensoft XML is close to exhausted: of about 40 candidate species, one was both new to main and quotable.
