# desk-d614 progress

Angle: Pensoft salamander, caecilian, Neotropical frog and lizard papers (ZooKeys, ZSE, Herpetozoa, Evolutionary Systematics, Vertebrate Zoology) not searched by d598-d612; trait eye_diameter_mm, evidence_kind anatomical_measurement. About 40 WebSearches. 14 records in docs/views/evidence/desk-d614.jsonl; check.py plain and --require-evidence-kind: 0 problems. Main re-checked (git fetch, b68223015) immediately before filing: no species or DOI hit except the d602 progress-note lead for D. bilobatus.

## Filed
- ZooKeys 942: 77-104 (10.3897/zookeys.942.51864) Dendropsophus bilobatus: holotype INPA-H 41300, ED 2.5, Table 3 holotype row (d602 lead). Table 3 TL and FL disagree with the holotype sentence (noted in the record); ED agrees. Search: "Dendropsophus bilobatus sp. nov. green bilobate vocal sac southwestern Amazonia Ferrão ZooKeys 942 article preview" reached article_preview.php?id=51864. ASW page opened.
- Vertebrate Zoology 74: 1-21 (10.3897/vz.74.e103573) Brachycephalus herculeus: holotype MNRJ 42408, ED 1.5, holotype list with marked cut. Search: exact title plus "Folly Vertebrate Zoology 74". ASW page opened (found by search on the species name with holotype code). Methods give only the label 'eye diameter (ED (eye diameter))'.
- Herpetozoa 36: 225-232 (10.3897/herpetozoa.36.e106566) Hemiphyllodactylus hongkongensis: 12 records (holotype, 7 paratypes, 4 newly collected adults), EyeD row of Table 2 (two blocks). Search: "Hemiphyllodactylus hongkongensis Hong Kong ... Reptile Database" found the Reptile Database page; XML reached through "caecilian/skink" style query. Reptile Database page opened on the second URL form after the first returned server errors twice.

## Weak spots
- All text through the WebFetch page reader; long passages came back in pieces (Brachycephalus list, Hemiphyllodactylus table pairing, confirmed by a second explicit request).
- Hemiphyllodactylus year 2023 inferred from volume 36, not read as a printed date.
- Brachycephalus licence: only the opening of the CC BY 4.0 sentence was returned.

## Not filed and why
- Gastrotheca gemma (VZ 71: 201-218, Table 2 ED row for 4 type specimens, ED defined as greatest length of the orbit): ASW species page returned robots_disallowed, not retried. Strong lead if a later unit reaches an ASW page.
- Pristimantis guianensis (VZ 72: 1035-1065, Table 4): column mapping garbled (holotype 2.7), held out.
- Pseudoeurycea jaguar (VZ 72): holotype 'eye diameter 4.4' but Methods give no eye definition; d600/d601 also passed.
- Bolitoglossa muisca, Andrias yaoluopingensis, Pristimantis spp. 107333/104536/63009, Scinax pyroinguinis, Ranitomeya (ZooKeys 1236): already on main.
- Tylototriton (ZooKeys 1072, 935): eye length only or no ED. Paramesotriton wumengshanensis (ZSE 101: 1933): measurements only in supplement. Enyalioides feiruzae: no ED. Dixonius fulbrighti (EvolSyst 7: 267, CC0): Table 3 not returned. Allobates albiventris: adults give EL only.
- Scinax onca (ZooKeys 706), Adenomera albarena (ZSE 100: 233), Phyllodactylus María Cleofas (ZooKeys 1024), Leptobrachella dorsospina (ZooKeys 995): no article_preview reached in my results; /article/ pages carry no Methods or tables. Leads.
- No salamander or caecilian record: Ichthyophis, Hynobius, Batrachuperus and Plethodon queries returned no unmined paper with ED.
