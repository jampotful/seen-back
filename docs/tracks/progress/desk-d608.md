# desk-d608 progress

Angle: salamanders, caecilians, Neotropical frogs and lizards in open-access Pensoft journals with an ED label and per-specimen mm values (OLD-ANGLE paragraph ignored). Log docs/views/evidence/desk-d608.jsonl, trait eye_diameter_mm, evidence_kind anatomical_measurement. 4 records. check.py plain and --require-evidence-kind: 0 problems for this file. About 41 WebSearches.

## Filed (all holotype only; no paratype ED value is printed per specimen in these papers)
- ZooKeys 1158: 27-48 (10.3897/zookeys.1158.99077) Bolitoglossa muisca, holotype IAvH-Am-17413, EYD 3.18 mm (first and eye clauses of the long holotype sentence, cut with [...]); Methods only label "eye diameter (EYD)".
- ZooKeys 1180: 257-293 (10.3897/zookeys.1180.107333) Pristimantis donnelsoni, holotype DHMECN 14701, Eye Diameter 1.9 (opening 39 words of the holotype paragraph; desk-d602 had left it as over 40 words). P. kayi holotype block not reached.
- ZooKeys 1081: 1-34 (10.3897/zookeys.1081.63009) Pristimantis gretathunbergae, holotype MHCH 3082, ED 4.6; Methods define "Eye Diameter as length of exposed eye".
- ZooKeys 185: 55-71 (10.3897/zookeys.185.1146, CC BY 3.0) Bolitoglossa chinanteca, holotype IBH 24708, ED 1.8; Methods define "diameter of eye opening (ED)".
Each species has an Amphibian Species of the World page opened from a search result (none prints the word "valid").

## Not filed and why
- Hypselotriton huanggangensis (ZooKeys 1208: 331-346, holotype ED 3.63 in Table 2, ED defined in Methods): the ASW page reached in search failed with robots_disallowed; not worked around. Lead if an ASW page opens.
- Dendropsophus cannatellai (Evol. Syst. 9(1): 7-31, 10.3897/evolsyst.9.135431): holotype "eye diameter 3.34 mm" in a defined-ED paper, but no ASW species page appeared in three searches. Lead.
- Already on main: Noblella madreselva (d576), Caecilia pulchraserrana (d308), Hyloscirtus tolkieni (d576), Hypselotriton oolong, Pristimantis danae group (d594), Chimerella (d601), Centrolene kutuku (d584).
- No eye measurement or only mean +/- SD: Pholidobolus (ZooKeys 954), Alopoglossus viridiceps (ZooKeys 410), Enyalioides feiruzae (Evol. Syst. 5), Anolis ZooKeys 794, Phyllodactylus cleofasensis (Table 3 means), Tylototriton asperrimus complex (eye length, ranges), Osteocephalus vasquezi (already dead), Hypselotriton/Pristimantis gladiator Table 2 ranges.
- Page reader returned metadata only for /article/N/ pages (Telmatobius ventriflavum ZooKeys 480, Pristimantis amaguanae ZooKeys 993 no ED definition, P. petersioides, Huicundomantis XML cut before the description).

## Process notes
- A scratch file in the shared scratchpad (b2.jsonl, 8 desk-d437 Araneus lines) was appended to by mistake and moved; the 8 lines briefly entered this branch (commit ac05765) and were removed in the following commit; the file was restored in the scratchpad from the copy. A b1.jsonl in the scratchpad may have been deleted by my rm (unknown whether it existed).
- One WebFetch used an edited ASW URL for Pristimantis kayi (a typing slip); it was refused (PROVENANCE_REQUIRED) and not retried.
- Page text came through the WebFetch reader; quotes and neighbouring text are tool-returned fragments joined. Licence sentences came split or paraphrased in their closing clause. Crossref not used.
