# Codex findings 2026-10-26: fixes still needed (unit b)

Unit b triaged the 1205 source, value and grade lines of `2026-10-26.jsonl`: 1015 hold, 133 do not hold, 57 cannot be told from the repository. Verdicts are in `2026-10-26-verdicts-b.jsonl`.

## What this unit wrote

- `docs/views/recheck/recheck-codex-b.jsonl`: 2936 recheck rows (2928 `correct`, 8 `retract`), each with `supersedes` and a reason naming its finding.
- `docs/views/evidence/recheck-codex-b-fixed.jsonl`: the 2928 corrected records, each with `rechecked`. `check.py` reports 0 problems.
- `docs/views/fixes/codex-b-partial.jsonl`: `partial: true` for 1956 records whose note, method or access shows a review, compilation, cited study or abstract reading (gaps.py reads this directory). Records also corrected in the recheck file carry the flag there instead.
- `2026-10-26-audit-lines-b.jsonl`: one `docs/views/audit/ALL.jsonl` line per superseded or retracted record, in the form of the lines that applied recheck 27. **The desk appends these to `ALL.jsonl`**; until then the old and the corrected copies are both live in gaps.py.

## Root causes, each verified once

1. **Journal fields without a volume** (findings of that wording, 183 lines): the stored Crossref results on `ci` give the volume; 2,880 records corrected with volume, issue and pages from the registry. Records already superseded by a recheck file that has the volume do not hold.
2. **Review and abstract readings without `partial`** (113 lines): the oa batches logged review and compilation values with the reading named in `note` and no flag. Lines whose record is primary, already flagged or retracted do not hold.
3. **Search records that predate evidence on main** (276 lines): every cited record was opened at its line and checked for trait, genus and retraction. 254 hold; 21 cite a record filed under another genus name (cannot tell without a synonym ruling); 1 cites another species.
4. **Gap cells stale against main** (370 lines): `tools/views/gaps.py` was rerun twice into a scratch folder at `--world 1200`, once as it stands and once with the research-branch loop removed. 280 lines reproduce on the main-only run; 90 give the stored state on that run and do not hold. The holding lines depend on reading main alone, which is finding 1 (unit a). No gap file was edited.
5. **Placeholder citation fields** (123 lines): "et al.", "not confirmed", year 0 and similar. Evidence lines with a matching Crossref record were fixed from it; empty author fields with no source are the form desk-screen point 6 asks for and do not hold.
6. **Values absent from their quotes** (30 lines): each record read. Seven do not hold (± extracted as 8, ".05", Slovene number words); the rest need a requote from the paper text.

## Fixes with no mechanism, by record id

### Search records that now overlap evidence on main (254)

No file retires a search record. coverage.py applies search records only to open queue cells, so each of these now bears only on the other species of its genus.

- docs/views/searched/external-7.jsonl:13 Lasioglossum (finding 2954)
- docs/views/searched/harvest-1.jsonl:1 Ardea (finding 2955)
- docs/views/searched/harvest-1.jsonl:40 Cirsium (finding 2956)
- docs/views/searched/harvest-10.jsonl:2 Lysimachia (finding 2957)
- docs/views/searched/harvest-11.jsonl:1 Medicago (finding 2958)
- docs/views/searched/harvest-11.jsonl:2 Cardamine (finding 2959)
- docs/views/searched/harvest-12.jsonl:40 Euphorbia (finding 2960)
- docs/views/searched/harvest-12.jsonl:42 Impatiens (finding 2961)
- docs/views/searched/harvest-12.jsonl:43 Potentilla (finding 2962)
- docs/views/searched/harvest-12.jsonl:47 Pinus (finding 2963)
- docs/views/searched/harvest-12.jsonl:48 Quercus (finding 2964)
- docs/views/searched/harvest-15.jsonl:3 Rana (finding 2965)
- docs/views/searched/harvest-15.jsonl:4 Populus (finding 2966)
- docs/views/searched/harvest-17.jsonl:7 Artemisia (finding 2967)
- docs/views/searched/harvest-17.jsonl:11 Cylindropuntia (finding 2968)
- docs/views/searched/harvest-18.jsonl:3 Asarum (finding 2969)
- docs/views/searched/harvest-18.jsonl:11 Vitis (finding 2970)
- docs/views/searched/harvest-18.jsonl:16 Dianthus (finding 2971)
- docs/views/searched/harvest-19.jsonl:7 Ophrys (finding 2972)
- docs/views/searched/harvest-19.jsonl:9 Scrophularia (finding 2973)
- docs/views/searched/harvest-19.jsonl:17 Odocoileus (finding 2974)
- docs/views/searched/harvest-2.jsonl:22 Plantago (finding 2975)
- docs/views/searched/harvest-2.jsonl:52 Solanum (finding 2976)
- docs/views/searched/harvest-2.jsonl:53 Solanum (finding 2977)
- docs/views/searched/harvest-2.jsonl:88 Phalacrocorax (finding 2979)
- docs/views/searched/harvest-20.jsonl:10 Osmunda (finding 2980)
- docs/views/searched/harvest-20.jsonl:13 Hibiscus (finding 2981)
- docs/views/searched/harvest-3.jsonl:5 Agelaius (finding 2982)
- docs/views/searched/harvest-3.jsonl:6 Agelaius (finding 2983)
- docs/views/searched/harvest-3.jsonl:8 Silene (finding 2984)
- docs/views/searched/harvest-4.jsonl:25 Achillea (finding 2985)
- docs/views/searched/harvest-6.jsonl:4 Geranium (finding 2987)
- docs/views/searched/harvest-6.jsonl:5 Anemone (finding 2988)
- docs/views/searched/harvest-8.jsonl:21 Thamnophis (finding 2989)
- docs/views/searched/harvest-8.jsonl:22 Thamnophis (finding 2990)
- docs/views/searched/harvest-9.jsonl:54 Salvia (finding 2992)
- docs/views/searched/harvest-9.jsonl:55 Viola (finding 2993)
- docs/views/searched/mammals-met.jsonl:1 Canis latrans (finding 2994)
- docs/views/searched/mammals-met.jsonl:2 Urocyon cinereoargenteus (finding 2995)
- docs/views/searched/mammals-met.jsonl:3 Puma concolor (finding 2996)
- docs/views/searched/mammals-met.jsonl:7 Capra hircus (finding 2997)
- docs/views/searched/mammals-met.jsonl:8 Lama glama (finding 2998)
- docs/views/searched/mammals-met.jsonl:10 Bos taurus (finding 2999)
- docs/views/searched/mammals-met.jsonl:12 Sciurus carolinensis (finding 3001)
- docs/views/searched/sweep-1.jsonl:4 Anas (finding 3002)
- docs/views/searched/sweep-1.jsonl:10 Sciurus (finding 3003)
- docs/views/searched/sweep-1.jsonl:11 Zenaida (finding 3004)
- docs/views/searched/sweep-1.jsonl:12 Corvus (finding 3005)
- docs/views/searched/sweep-1.jsonl:16 Danaus (finding 3006)
- docs/views/searched/sweep-1.jsonl:18 Papilio (finding 3007)
- docs/views/searched/sweep-1.jsonl:20 Phalacrocorax (finding 3008)
- docs/views/searched/sweep-1.jsonl:22 Calidris (finding 3009)
- docs/views/searched/sweep-1.jsonl:24 Odocoileus (finding 3010)
- docs/views/searched/sweep-1.jsonl:26 Aythya (finding 3011)
- docs/views/searched/sweep-1.jsonl:29 Cygnus (finding 3012)
- docs/views/searched/sweep-1.jsonl:37 Acer (finding 3013)
- docs/views/searched/sweep-10.jsonl:10 Alces (finding 3014)
- docs/views/searched/sweep-10.jsonl:12 Battus (finding 3015)
- docs/views/searched/sweep-10.jsonl:22 Hypericum (finding 3016)
- docs/views/searched/sweep-10.jsonl:40 Anthriscus (finding 3017)
- docs/views/searched/sweep-100.jsonl:38 Zanthoxylum (finding 3018)
- docs/views/searched/sweep-103.jsonl:73 Smilisca (finding 3019)
- docs/views/searched/sweep-103.jsonl:104 Scaphiopus (finding 3020)
- docs/views/searched/sweep-104.jsonl:5 Hyperolius (finding 3021)
- docs/views/searched/sweep-105.jsonl:22 Agalychnis (finding 3022)
- docs/views/searched/sweep-105.jsonl:36 Microhyla (finding 3023)
- docs/views/searched/sweep-105.jsonl:38 Dendropsophus (finding 3024)
- docs/views/searched/sweep-107.jsonl:12 Kaloula (finding 3025)
- docs/views/searched/sweep-107.jsonl:16 Scinax (finding 3026)
- docs/views/searched/sweep-11.jsonl:23 Melanitta (finding 3027)
- docs/views/searched/sweep-11.jsonl:39 Otospermophilus (finding 3028)
- docs/views/searched/sweep-12.jsonl:10 Polypodium (finding 3029)
- docs/views/searched/sweep-12.jsonl:16 Selasphorus (finding 3030)
- docs/views/searched/sweep-12.jsonl:21 Cacatua (finding 3031)
- docs/views/searched/sweep-12.jsonl:38 Panthera (finding 3032)
- docs/views/searched/sweep-13.jsonl:26 Caracara (finding 3033)
- docs/views/searched/sweep-13.jsonl:28 Ferocactus (finding 3034)
- docs/views/searched/sweep-13.jsonl:38 Athene (finding 3035)
- docs/views/searched/sweep-14.jsonl:14 Pituophis (finding 3036)
- docs/views/searched/sweep-14.jsonl:15 Iguana (finding 3037)
- docs/views/searched/sweep-14.jsonl:16 Incilius (finding 3038)
- docs/views/searched/sweep-14.jsonl:26 Megachile (finding 3039)
- docs/views/searched/sweep-14.jsonl:30 Zosterops (finding 3040)
- docs/views/searched/sweep-14.jsonl:39 Aquila (finding 3041)
- docs/views/searched/sweep-14.jsonl:40 Canis (finding 3042)
- docs/views/searched/sweep-15.jsonl:4 Juglans (finding 3043)
- docs/views/searched/sweep-15.jsonl:26 Hypolimnas (finding 3044)
- docs/views/searched/sweep-15.jsonl:38 Acris (finding 3045)
- docs/views/searched/sweep-16.jsonl:2 Pelophylax (finding 3046)
- docs/views/searched/sweep-16.jsonl:6 Pseudemys (finding 3047)
- docs/views/searched/sweep-16.jsonl:12 Hordeum (finding 3048)
- docs/views/searched/sweep-17.jsonl:31 Agkistrodon (finding 3049)
- docs/views/searched/sweep-17.jsonl:35 Bonasa (finding 3050)
- docs/views/searched/sweep-18.jsonl:11 Osmundastrum (finding 3051)
- docs/views/searched/sweep-18.jsonl:16 Todiramphus (finding 3052)
- docs/views/searched/sweep-18.jsonl:21 Asio (finding 3053)
- docs/views/searched/sweep-18.jsonl:22 Megascops (finding 3054)
- docs/views/searched/sweep-18.jsonl:24 Anthochaera (finding 3055)
- docs/views/searched/sweep-19.jsonl:10 Eolophus (finding 3056)
- docs/views/searched/sweep-19.jsonl:12 Coluber (finding 3057)
- docs/views/searched/sweep-2.jsonl:2 Solanum (finding 3058)
- docs/views/searched/sweep-2.jsonl:8 Plantago (finding 3059)
- docs/views/searched/sweep-2.jsonl:16 Mareca (finding 3060)
- docs/views/searched/sweep-2.jsonl:17 Spatula (finding 3061)
- docs/views/searched/sweep-2.jsonl:29 Bucephala (finding 3062)
- docs/views/searched/sweep-2.jsonl:31 Libellula (finding 3063)
- docs/views/searched/sweep-2.jsonl:32 Polistes (finding 3064)
- docs/views/searched/sweep-2.jsonl:36 Thamnophis (finding 3065)
- docs/views/searched/sweep-20.jsonl:18 Salix (finding 3066)
- docs/views/searched/sweep-20.jsonl:20 Bison (finding 3067)
- docs/views/searched/sweep-20.jsonl:23 Anthidium (finding 3068)
- docs/views/searched/sweep-20.jsonl:28 Cakile (finding 3069)
- docs/views/searched/sweep-20.jsonl:31 Vachellia (finding 3070)
- docs/views/searched/sweep-20.jsonl:35 Amazilia (finding 3071)
- docs/views/searched/sweep-21.jsonl:8 Phacelia (finding 3072)
- docs/views/searched/sweep-21.jsonl:23 Carpodacus (finding 3073)
- docs/views/searched/sweep-21.jsonl:27 Osmunda (finding 3074)
- docs/views/searched/sweep-22.jsonl:19 Puma (finding 3075)
- docs/views/searched/sweep-23.jsonl:19 Puma (finding 3076)
- docs/views/searched/sweep-25.jsonl:8 Pleopeltis (finding 3077)
- docs/views/searched/sweep-25.jsonl:11 Lethe (finding 3078)
- docs/views/searched/sweep-25.jsonl:21 Alauda (finding 3079)
- docs/views/searched/sweep-25.jsonl:32 Aquarius (finding 3080)
- docs/views/searched/sweep-26.jsonl:13 Alectoris (finding 3081)
- docs/views/searched/sweep-26.jsonl:26 Acanthiza (finding 3082)
- docs/views/searched/sweep-26.jsonl:29 Duttaphrynus (finding 3083)
- docs/views/searched/sweep-27.jsonl:8 Sclerophrys (finding 3084)
- docs/views/searched/sweep-28.jsonl:11 Photinus (finding 3087)
- docs/views/searched/sweep-29.jsonl:7 Osteopilus (finding 3089)
- docs/views/searched/sweep-29.jsonl:33 Cantharis (finding 3090)
- docs/views/searched/sweep-29.jsonl:36 Tenodera (finding 3091)
- docs/views/searched/sweep-3.jsonl:2 Haliaeetus (finding 3092)
- docs/views/searched/sweep-3.jsonl:3 Sympetrum (finding 3093)
- docs/views/searched/sweep-3.jsonl:10 Junonia (finding 3094)
- docs/views/searched/sweep-3.jsonl:11 Pica (finding 3095)
- docs/views/searched/sweep-3.jsonl:19 Prunella (finding 3096)
- docs/views/searched/sweep-3.jsonl:26 Vaccinium (finding 3097)
- docs/views/searched/sweep-3.jsonl:28 Polygonia (finding 3099)
- docs/views/searched/sweep-3.jsonl:30 Fringilla (finding 3100)
- docs/views/searched/sweep-3.jsonl:32 Equisetum (finding 3101)
- docs/views/searched/sweep-30.jsonl:3 Syritta (finding 3102)
- docs/views/searched/sweep-30.jsonl:13 Anthophora (finding 3103)
- docs/views/searched/sweep-30.jsonl:19 Ficus (finding 3104)
- docs/views/searched/sweep-30.jsonl:21 Phalaris (finding 3105)
- docs/views/searched/sweep-30.jsonl:26 Euploea (finding 3106)
- docs/views/searched/sweep-30.jsonl:27 Perdix (finding 3107)
- docs/views/searched/sweep-31.jsonl:4 Valeriana (finding 3108)
- docs/views/searched/sweep-31.jsonl:24 Vipera (finding 3109)
- docs/views/searched/sweep-31.jsonl:31 Cocculus (finding 3110)
- docs/views/searched/sweep-31.jsonl:38 Ovis (finding 3112)
- docs/views/searched/sweep-32.jsonl:3 Gorsachius (finding 3113)
- docs/views/searched/sweep-32.jsonl:4 Polypedates (finding 3114)
- docs/views/searched/sweep-32.jsonl:23 Periplaneta (finding 3116)
- docs/views/searched/sweep-33.jsonl:16 Boana (finding 3117)
- docs/views/searched/sweep-34.jsonl:19 Connochaetes (finding 3118)
- docs/views/searched/sweep-35.jsonl:3 Dendragapus (finding 3119)
- docs/views/searched/sweep-36.jsonl:1 Ipomopsis (finding 3120)
- docs/views/searched/sweep-37.jsonl:4 Forficula (finding 3121)
- docs/views/searched/sweep-38.jsonl:26 Acraea (finding 3122)
- docs/views/searched/sweep-39.jsonl:1 Hyla (finding 3123)
- docs/views/searched/sweep-39.jsonl:2 Wyethia (finding 3124)
- docs/views/searched/sweep-39.jsonl:13 Leptodactylus (finding 3125)
- docs/views/searched/sweep-39.jsonl:15 Monochamus (finding 3126)
- docs/views/searched/sweep-4.jsonl:1 Spizella (finding 3127)
- docs/views/searched/sweep-4.jsonl:3 Chrysemys (finding 3128)
- docs/views/searched/sweep-4.jsonl:8 Potentilla (finding 3129)
- docs/views/searched/sweep-4.jsonl:11 Aix (finding 3130)
- docs/views/searched/sweep-4.jsonl:14 Medicago (finding 3132)
- docs/views/searched/sweep-4.jsonl:20 Eristalis (finding 3133)
- docs/views/searched/sweep-4.jsonl:30 Cardamine (finding 3134)
- docs/views/searched/sweep-4.jsonl:34 Coragyps (finding 3135)
- docs/views/searched/sweep-40.jsonl:8 Eleutherodactylus (finding 3136)
- docs/views/searched/sweep-41.jsonl:25 Gekko (finding 3137)
- docs/views/searched/sweep-43.jsonl:23 Dama (finding 3138)
- docs/views/searched/sweep-43.jsonl:26 Pueraria (finding 3139)
- docs/views/searched/sweep-44.jsonl:23 Capra (finding 3140)
- docs/views/searched/sweep-44.jsonl:34 Scolopax (finding 3141)
- docs/views/searched/sweep-44.jsonl:37 Bombina (finding 3142)
- docs/views/searched/sweep-45.jsonl:1 Triodanis (finding 3143)
- docs/views/searched/sweep-46.jsonl:23 Fejervarya (finding 3144)
- docs/views/searched/sweep-47.jsonl:23 Litoria (finding 3145)
- docs/views/searched/sweep-48.jsonl:3 Dasyprocta (finding 3146)
- docs/views/searched/sweep-48.jsonl:15 Melanitis (finding 3147)
- docs/views/searched/sweep-48.jsonl:25 Sistrurus (finding 3148)
- docs/views/searched/sweep-48.jsonl:28 Boa (finding 3149)
- docs/views/searched/sweep-48.jsonl:39 Mus (finding 3150)
- docs/views/searched/sweep-49.jsonl:2 Daphnis (finding 3151)
- docs/views/searched/sweep-5.jsonl:8 Erithacus (finding 3153)
- docs/views/searched/sweep-5.jsonl:14 Campanula (finding 3154)
- docs/views/searched/sweep-5.jsonl:21 Asplenium (finding 3155)
- docs/views/searched/sweep-5.jsonl:36 Dryophytes (finding 3156)
- docs/views/searched/sweep-5.jsonl:37 Rana (finding 3157)
- docs/views/searched/sweep-5.jsonl:38 Pseudacris (finding 3158)
- docs/views/searched/sweep-5.jsonl:39 Alligator (finding 3159)
- docs/views/searched/sweep-50.jsonl:26 Oophaga (finding 3160)
- docs/views/searched/sweep-50.jsonl:29 Ahaetulla (finding 3161)
- docs/views/searched/sweep-50.jsonl:31 Pseudechis (finding 3162)
- docs/views/searched/sweep-51.jsonl:38 Acinonyx (finding 3163)
- docs/views/searched/sweep-52.jsonl:16 Buergeria (finding 3164)
- docs/views/searched/sweep-53.jsonl:11 Craugastor (finding 3165)
- docs/views/searched/sweep-53.jsonl:35 Dendrobates (finding 3166)
- docs/views/searched/sweep-54.jsonl:15 Pseudonaja (finding 3167)
- docs/views/searched/sweep-54.jsonl:19 Odorrana (finding 3168)
- docs/views/searched/sweep-54.jsonl:20 Pelobates (finding 3169)
- docs/views/searched/sweep-55.jsonl:27 Limnonectes (finding 3171)
- docs/views/searched/sweep-59.jsonl:34 Morpho (finding 3173)
- docs/views/searched/sweep-6.jsonl:26 Euonymus (finding 3174)
- docs/views/searched/sweep-62.jsonl:41 Alytes (finding 3175)
- docs/views/searched/sweep-64.jsonl:8 Laticauda (finding 3176)
- docs/views/searched/sweep-64.jsonl:15 Caracal (finding 3177)
- docs/views/searched/sweep-64.jsonl:24 Mixophyes (finding 3178)
- docs/views/searched/sweep-65.jsonl:33 Trachycephalus (finding 3179)
- docs/views/searched/sweep-66.jsonl:16 Ammotragus (finding 3180)
- docs/views/searched/sweep-67.jsonl:28 Emydocephalus (finding 3182)
- docs/views/searched/sweep-69.jsonl:13 Pelodytes (finding 3183)
- docs/views/searched/sweep-69.jsonl:14 Ascaphus (finding 3184)
- docs/views/searched/sweep-69.jsonl:15 Megophrys (finding 3185)
- docs/views/searched/sweep-69.jsonl:17 Osteocephalus (finding 3186)
- docs/views/searched/sweep-7.jsonl:2 Gavia (finding 3187)
- docs/views/searched/sweep-7.jsonl:9 Pluvialis (finding 3188)
- docs/views/searched/sweep-7.jsonl:22 Dolichovespula (finding 3189)
- docs/views/searched/sweep-7.jsonl:37 Coloeus (finding 3190)
- docs/views/searched/sweep-71.jsonl:4 Hypopachus (finding 3191)
- docs/views/searched/sweep-71.jsonl:37 Camelus (finding 3193)
- docs/views/searched/sweep-72.jsonl:23 Eupsophus (finding 3195)
- docs/views/searched/sweep-73.jsonl:28 Phrynobatrachus (finding 3197)
- docs/views/searched/sweep-73.jsonl:31 Batrachyla (finding 3198)
- docs/views/searched/sweep-74.jsonl:4 Boophis (finding 3199)
- docs/views/searched/sweep-76.jsonl:17 Gastrotheca (finding 3200)
- docs/views/searched/sweep-76.jsonl:19 Kalophrynus (finding 3201)
- docs/views/searched/sweep-76.jsonl:20 Allobates (finding 3202)
- docs/views/searched/sweep-76.jsonl:31 Felis (finding 3203)
- docs/views/searched/sweep-77.jsonl:19 Heleioporus (finding 3204)
- docs/views/searched/sweep-77.jsonl:22 Proceratophrys (finding 3205)
- docs/views/searched/sweep-77.jsonl:30 Ceratophrys (finding 3206)
- docs/views/searched/sweep-78.jsonl:11 Amnirana (finding 3208)
- docs/views/searched/sweep-79.jsonl:13 Cryptomys (finding 3209)
- docs/views/searched/sweep-8.jsonl:10 Tadorna (finding 3210)
- docs/views/searched/sweep-8.jsonl:17 Lynx (finding 3211)
- docs/views/searched/sweep-8.jsonl:20 Crotalus (finding 3212)
- docs/views/searched/sweep-8.jsonl:31 Lobelia (finding 3213)
- docs/views/searched/sweep-81.jsonl:34 Uncia (finding 3214)
- docs/views/searched/sweep-82.jsonl:29 Silverstoneia (finding 3215)
- docs/views/searched/sweep-82.jsonl:32 Leptobrachella (finding 3216)
- docs/views/searched/sweep-83.jsonl:32 Heleophryne (finding 3217)
- docs/views/searched/sweep-85.jsonl:34 Nymphargus (finding 3218)
- docs/views/searched/sweep-86.jsonl:30 Geocrinia (finding 3219)
- docs/views/searched/sweep-89.jsonl:9 Nyctibatrachus (finding 3221)
- docs/views/searched/sweep-9.jsonl:12 Oxyura (finding 3222)
- docs/views/searched/sweep-9.jsonl:14 Bubo (finding 3223)
- docs/views/searched/sweep-9.jsonl:20 Cervus (finding 3224)
- docs/views/searched/sweep-9.jsonl:32 Acacia (finding 3225)
- docs/views/searched/sweep-9.jsonl:35 Echinocereus (finding 3226)
- docs/views/searched/sweep-97.jsonl:4 Centrosema (finding 3228)

### Wanted lines with placeholder fields (79)

`docs/views/wanted/fixes.jsonl` matches by first-author surname and year, which a placeholder author cannot key; authors and years below come from the Crossref results on `ci` where a record exists.

- docs/views/wanted/canon-2.jsonl:1 (authors placeholder); no Crossref record
- docs/views/wanted/canon-2.jsonl:3 (authors placeholder); Crossref authors: Schott RK, Fujita MK, Streicher JW, Gower DJ, Thomas KN, Loew ER, Bamba Kaya AG, Bittencourt-Silva GB, Guillherme Becker C, Cisneros-Heredia D, Clulow S, Davila M, Firneno TJ, Haddad CFB, Janssenswillen S, Labisko J, Maddock ST, Mahony M, Martins RA, Michaels CJ, Mitchell NJ, Portik DM, Prates I, Roelants K, Roelke C, Tobi E, Woolfolk M, Bell RC; year 2024
- docs/views/wanted/canon.jsonl:1 (year missing or 0); no Crossref record
- docs/views/wanted/canon.jsonl:10 (year missing or 0); no Crossref record
- docs/views/wanted/canon.jsonl:15 (authors placeholder); Crossref authors: Lucas EA, Martin GR, Rocamora G, Portugal SJ; year 2024
- docs/views/wanted/canon.jsonl:41 (authors placeholder); Crossref authors: Schott RK, Fujita MK, Streicher JW, Gower DJ, Thomas KN, Loew ER, Bamba Kaya AG, Bittencourt-Silva GB, Guillherme Becker C, Cisneros-Heredia D, Clulow S, Davila M, Firneno TJ, Haddad CFB, Janssenswillen S, Labisko J, Maddock ST, Mahony M, Martins RA, Michaels CJ, Mitchell NJ, Portik DM, Prates I, Roelants K, Roelke C, Tobi E, Woolfolk M, Bell RC; year 2024
- docs/views/wanted/canon.jsonl:48 (authors placeholder); no Crossref record
- docs/views/wanted/canon.jsonl:50 (authors placeholder); no Crossref record
- docs/views/wanted/cat-dog.jsonl:15 (title placeholder); no Crossref record
- docs/views/wanted/herps-met.jsonl:2 (authors placeholder); Crossref authors: Beatty AR, Flint M, Flint J, Gemensky-Metzler AJ, Diaz-Campos D, van Balen JC, Newbold G; year 2024
- docs/views/wanted/herps-met.jsonl:14 (authors placeholder); Crossref authors: Zhang B, Wei P, Cui Y, Zhang Y, Chen H, Li X, Zhou K, Jiang T, Chen A, Lei L, Rossiter SJ, Yuan Z, Liu Y; year 2026
- docs/views/wanted/herps-met.jsonl:26 (authors placeholder); no Crossref record
- docs/views/wanted/insects-met.jsonl:9 (authors placeholder); Crossref authors: Guignard Q, Goodwin J, Kimoto T, Haynes KF, Allison JD; year 2025
- docs/views/wanted/insects-met.jsonl:10 (authors placeholder); Crossref authors: Qiu K, Wang K, Dai Y, An H, Huang Q, Zhu F, Liu W, Wang X; year 2025
- docs/views/wanted/mammals-met.jsonl:7 (authors placeholder); Crossref authors: Banks MS, Sprague WW, Schmoll J, Parnell JAQ, Love GD; year 2015
- docs/views/wanted/mammals-met.jsonl:10 (authors placeholder); no Crossref record
- docs/views/wanted/mammals-met.jsonl:17 (authors placeholder); no Crossref record
- docs/views/wanted/squirrel-deer-rabbit.jsonl:14 (authors placeholder); Crossref authors: Banks MS, Sprague WW, Schmoll J, Parnell JAQ, Love GD; year 2015
- docs/views/wanted/sweep-10.jsonl:1 (authors placeholder); no Crossref record
- docs/views/wanted/sweep-10.jsonl:5 (authors placeholder); no Crossref record
- docs/views/wanted/sweep-11.jsonl:2 (authors placeholder); no Crossref record
- docs/views/wanted/sweep-11.jsonl:3 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-11.jsonl:4 (authors placeholder); no Crossref record
- docs/views/wanted/sweep-11.jsonl:6 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-12.jsonl:1 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-12.jsonl:5 (authors placeholder); no Crossref record
- docs/views/wanted/sweep-12.jsonl:7 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-13.jsonl:5 (title placeholder); no Crossref record
- docs/views/wanted/sweep-14.jsonl:1 (authors placeholder); no Crossref record
- docs/views/wanted/sweep-14.jsonl:3 (title placeholder); no Crossref record
- docs/views/wanted/sweep-16.jsonl:3 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-17.jsonl:2 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-18.jsonl:3 (authors placeholder); no Crossref record
- docs/views/wanted/sweep-18.jsonl:4 (authors placeholder, title placeholder); no Crossref record
- docs/views/wanted/sweep-18.jsonl:5 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-21.jsonl:2 (authors placeholder); Crossref authors: Ignatova II, Miinalainen I, Frolov RV; year 2021
- docs/views/wanted/sweep-21.jsonl:3 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-23.jsonl:2 (title placeholder); no Crossref record
- docs/views/wanted/sweep-25.jsonl:1 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-25.jsonl:3 (authors placeholder); no Crossref record
- docs/views/wanted/sweep-25.jsonl:6 (authors placeholder); Crossref authors: Majek BA, Erickson C, Duke WB; year 1984
- docs/views/wanted/sweep-26.jsonl:2 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-34.jsonl:2 (authors placeholder); no Crossref record
- docs/views/wanted/sweep-37.jsonl:3 (authors placeholder); no Crossref record
- docs/views/wanted/sweep-39.jsonl:2 (year missing or 0); no Crossref record
- docs/views/wanted/sweep-4.jsonl:1 (year missing or 0); no Crossref record
- docs/views/wanted/sweep-4.jsonl:2 (year missing or 0); no Crossref record
- docs/views/wanted/sweep-4.jsonl:3 (year missing or 0); no Crossref record
- docs/views/wanted/sweep-4.jsonl:4 (year missing or 0); no Crossref record
- docs/views/wanted/sweep-4.jsonl:5 (year missing or 0); no Crossref record
- docs/views/wanted/sweep-4.jsonl:6 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-4.jsonl:7 (year missing or 0); no Crossref record
- docs/views/wanted/sweep-4.jsonl:8 (year missing or 0); no Crossref record
- docs/views/wanted/sweep-4.jsonl:9 (year missing or 0); no Crossref record
- docs/views/wanted/sweep-43.jsonl:3 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-47.jsonl:2 (authors placeholder); no Crossref record
- docs/views/wanted/sweep-47.jsonl:3 (authors placeholder); no Crossref record
- docs/views/wanted/sweep-51.jsonl:2 (authors placeholder); Crossref authors: Casalía B, Vilacoba E, Lavinia PD, Tubaro PL, Barreira AS; year 2020
- docs/views/wanted/sweep-52.jsonl:1 (year missing or 0); no Crossref record
- docs/views/wanted/sweep-55.jsonl:7 (authors placeholder); Crossref authors: Rigosi E, Wiederman SD, Gutiérrez D, C. O’Carroll D; year 2026
- docs/views/wanted/sweep-56.jsonl:1 (authors placeholder); no Crossref record
- docs/views/wanted/sweep-64.jsonl:5 (authors placeholder, title placeholder); Crossref authors: Silva I, Crane M, Artchawakom T, Suwanwaree P, Strine CT; year 2016
- docs/views/wanted/sweep-68.jsonl:1 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-9.jsonl:1 (authors placeholder); no Crossref record
- docs/views/wanted/sweep-9.jsonl:3 (authors placeholder); Crossref authors: Cantlay JC, Martin GR, McClelland SC, Potier S, O'Brien MF, Fernández-Juricic E, Bond AL, Portugal SJ; year 2023
- docs/views/wanted/sweep-9.jsonl:4 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-9.jsonl:6 (authors placeholder); Crossref authors: Suetsugu K, Iwai A, Moriue S, Nishimura A, Okuyama Y, Ishikawa H; year 2026
- docs/views/wanted/sweep-9.jsonl:8 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-9.jsonl:9 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-9.jsonl:10 (authors placeholder, year missing or 0); no Crossref record
- docs/views/wanted/sweep-91.jsonl:3 (authors placeholder); no Crossref record
- docs/views/wanted/web-herps.jsonl:13 (authors placeholder); Crossref authors: Schott RK, Fujita MK, Streicher JW, Gower DJ, Thomas KN, Loew ER, Bamba Kaya AG, Bittencourt-Silva GB, Guillherme Becker C, Cisneros-Heredia D, Clulow S, Davila M, Firneno TJ, Haddad CFB, Janssenswillen S, Labisko J, Maddock ST, Mahony M, Martins RA, Michaels CJ, Mitchell NJ, Portik DM, Prates I, Roelants K, Roelke C, Tobi E, Woolfolk M, Bell RC; year 2024
- docs/views/wanted/web-herps.jsonl:17 (year missing or 0); no Crossref record
- docs/views/wanted/web-herps.jsonl:22 (authors placeholder); Crossref authors: Katti C, Stacey-Solis M, Coronel-Rojas NA, Davies WIL; year 2018
- docs/views/wanted/web-mammals.jsonl:6 (authors placeholder); Crossref authors: Klećkowska-Nawrot J, Badenhorst S, Borawski W, Goździewska-Harłajczuk K, Aktaş A, Chrószcz A; year 2026
- docs/views/wanted/web-mammals.jsonl:20 (authors placeholder); Crossref authors: Hirata M, Arimoto C, Hattori N, Anzai H; year 2019
- docs/views/wanted/web-mammals.jsonl:31 (authors placeholder); no Crossref record
- docs/views/wanted/web-mammals.jsonl:39 (authors placeholder, year missing or 0); Crossref authors: Ishengoma E, Agaba M, Cavener DR; year 2017
- docs/views/wanted/web-mammals.jsonl:45 (year missing or 0); no Crossref record

### Wanted lines that cannot serve their cells (audits 65 to 67) (17)

The recheck-2 unit (QUEUE.md, 26 Oct) covers cells whose only lead cannot serve them.

- docs/views/wanted/harvest-49.jsonl:11 (finding 3283)
- docs/views/wanted/harvest-49.jsonl:5 (finding 3284)
- docs/views/wanted/harvest-49.jsonl:6 (finding 3285)
- docs/views/wanted/harvest-49.jsonl:8 (finding 3286)
- docs/views/wanted/harvest-49.jsonl:9 (finding 3287)
- docs/views/wanted/harvest-50.jsonl:6 (finding 3288)
- docs/views/wanted/harvest-50.jsonl:7 (finding 3289)
- docs/views/wanted/harvest-50.jsonl:8 (finding 3290)
- docs/views/wanted/harvest-50.jsonl:9 (finding 3291)
- docs/views/wanted/harvest-51.jsonl:3 (finding 3292)
- docs/views/wanted/harvest-51.jsonl:4 (finding 3293)
- docs/views/wanted/harvest-51.jsonl:5 (finding 3294)
- docs/views/wanted/harvest-51.jsonl:6 (finding 3295)
- docs/views/wanted/harvest-51.jsonl:8 (finding 3296)
- docs/views/wanted/harvest-51.jsonl:9 (finding 3297)
- docs/views/wanted/harvest-51.jsonl:10 (finding 3298)
- docs/views/wanted/harvest-51.jsonl:12 (finding 3299)

### Wanted lines whose title differs from the registry (6)

- docs/views/wanted/insects-met.jsonl:9: Crossref title "Characterising Spectral Sensitivity and the Role of Sunlight Intensity in Japanese Beetle (
                    Popillia japonica
                    ) Surveill" (finding 2479)
- docs/views/wanted/harvest-28.jsonl:8: Crossref title "Light signaling as a principal component of crop-weed competition" (finding 2480)
- docs/views/wanted/web-birds.jsonl:15: Crossref title "Low achromatic contrast sensitivity in birds: a common attribute shared by many phylogenetic orders" (finding 2481)
- docs/views/wanted/harvest-44.jsonl:2: Crossref title "External morphology and microstructure of the compound eye of fire ants, Solenopsis invicta Buren" (finding 2487)
- docs/views/wanted/sweep-64.jsonl:5: Crossref title "More than meets the eye: change in pupil shape by a mock viper" (finding 2490)
- docs/views/wanted/insects-met.jsonl:3: Crossref title "Eye morphology and visual acuity in the pipevine swallowtail (Battus philenor) studied with a new method of measuring interommatidial angles" (finding 2491)

### Wanted lines whose authors differ from the registry (2)

- docs/views/wanted/web-herps.jsonl:13: Crossref authors Schott RK, Fujita MK, Streicher JW, Gower DJ, Thomas KN, Loew ER, Bamba Kaya AG, Bittencourt-Silva GB, Guillherme Becker C, Cisneros-Heredia D, Clulow S, Davila M, Firneno TJ, Haddad CFB, Janssenswillen S, Labisko J, Maddock ST, Mahony M, Martins RA, Michaels CJ, Mitchell NJ, Portik DM, Prates I, Roelants K, Roelke C, Tobi E, Woolfolk M, Bell RC (finding 3300)
- docs/views/wanted/sweep-3.jsonl:6: Crossref authors Fernández-Juricic E, Baumhardt PE, Tyrrell LP, Elmore A, DeLiberto ST, Werner SJ (finding 3302)

### Evidence whose DOI belongs to another work (1)

- sweep-30:2, DOI 10.1016/j.visres.2019.10.003 (findings 2486, 2501) — corrected by `recheck-owl-lws-2486` to DOI `10.1016/j.visres.2019.10.001`; superseded copy retired in `audit/ALL.jsonl`. Original retained for provenance; see `docs/tracks/progress/recheck-owl-lws-2486.md`.

### Evidence authors without a registry record (9)

- recheck-6-fixed:7 (finding 261)
- recheck-6-fixed:16 (finding 263)
- recheck-8-fixed:4 (finding 264)
- sweep-20:2 (finding 271)
- sweep-20:4 (finding 272)
- sweep-50:3 (finding 279)
- sweep-50:4 (finding 279)
- sweep-56:11 (finding 281)
- sweep-56:12 (finding 281)

### Sources missing a DOI, URL or journal (13)

- docs/views/evidence/intake-4-failed.jsonl:2 (finding 63)
- docs/views/evidence/intake-4-failed.jsonl:3 (finding 63)
- docs/views/evidence/intake-4-failed.jsonl:4 (finding 63)
- docs/views/evidence/intake-4-failed.jsonl:5 (finding 63)
- docs/views/evidence/intake-4-failed.jsonl:6 (finding 63)
- docs/views/evidence/intake-4-failed.jsonl:7 (finding 63)
- docs/views/evidence/intake-5-failed.jsonl:1 (finding 64)
- docs/views/evidence/intake-5-failed.jsonl:2 (finding 64)
- docs/views/evidence/intake-5-failed.jsonl:3 (finding 64)
- docs/views/evidence/sweep-20.jsonl:2 (finding 65)
- docs/views/evidence/sweep-84.jsonl:3 (finding 66)
- docs/views/evidence/sweep-84.jsonl:4 (finding 66)
- docs/views/evidence/sweep-84.jsonl:5 (finding 66)

### Values not in their quotes (requote needs the paper text) (22)

- intake:1 in docs/views/evidence/intake-6-failed.jsonl (finding 955)
- intake:2 in docs/views/evidence/intake-6-failed.jsonl (finding 956)
- intake:8 in docs/views/evidence/intake-8.jsonl (finding 979)
- intake:10 in docs/views/evidence/intake-8.jsonl (finding 982)
- oa-4:131 in docs/views/evidence/oa-4.jsonl (finding 1316)
- oa-4:132 in docs/views/evidence/oa-4.jsonl (finding 1318)
- oa-4:133 in docs/views/evidence/oa-4.jsonl (finding 1320)
- oa-4:134 in docs/views/evidence/oa-4.jsonl (finding 1322)
- oa-4:135 in docs/views/evidence/oa-4.jsonl (finding 1323)
- oa-4:136 in docs/views/evidence/oa-4.jsonl (finding 1325)
- oa-4:137 in docs/views/evidence/oa-4.jsonl (finding 1327)
- oa-4:230 in docs/views/evidence/oa-4.jsonl (finding 1352)
- oa-4:231 in docs/views/evidence/oa-4.jsonl (finding 1353)
- oa-4:232 in docs/views/evidence/oa-4.jsonl (finding 1354)
- oa-4:233 in docs/views/evidence/oa-4.jsonl (finding 1355)
- oa-4:234 in docs/views/evidence/oa-4.jsonl (finding 1356)
- oa-4:235 in docs/views/evidence/oa-4.jsonl (finding 1357)
- oa-4:241 in docs/views/evidence/oa-4.jsonl (finding 1362)
- oa-5:1024 in docs/views/evidence/oa-5.jsonl (finding 1586)
- oa-5:1031 in docs/views/evidence/oa-5.jsonl (finding 1590)
- intake:3 in docs/views/evidence/reread-1.jsonl (finding 1956)
- intake:4 in docs/views/evidence/reread-1.jsonl (finding 1957)

### Categorical red-receptor rows filed under lambda_max_nm (trait to choose) (14)

- canon-3:433 (finding 3238)
- canon-3:434 (finding 3239)
- canon-3:435 (finding 3240)
- canon-3:454 (finding 3241)
- canon-3:455 (finding 3242)
- canon-3:456 (finding 3243)
- canon-3:457 (finding 3244)
- canon-3:458 (finding 3245)
- canon-3:463 (finding 3246)
- canon-3:464 (finding 3247)
- canon-3:467 (finding 3248)
- canon-3:468 (finding 3249)
- canon-3:477 (finding 3250)
- canon-3:494 (finding 3251)

### Conflicts recorded in notes, to settle against the primary text (31)

- docs/views/evidence/oa-1.jsonl lines 50 (finding 32)
- docs/views/evidence/oa-1.jsonl lines 310-311 (finding 33)
- docs/views/evidence/oa-1.jsonl lines 2506-2509, 2534-2537, 2566, 2584-2585, 2607-2608, 2638-2639, 2683-2684, 2735-2736, 2787-2788, 2839-2840, 2891-2892, 2943-2944, 2995-2996, 3047-3048, 3099-3100, 3149-3150, 3193-3194, 3220-3221, 3258-3259, 3284 (finding 34)
- docs/views/evidence/oa-1.jsonl lines 3359, 3404 (finding 35)
- docs/views/evidence/oa-1.jsonl lines 3763-3765, 3829-3831, 3847-3849, 3901-3903, 4038-4039, 4089-4091 (finding 36)
- docs/views/evidence/oa-1.jsonl lines 4157, 4178, 4256, 4258 (finding 37)
- docs/views/evidence/oa-1.jsonl lines 4351 (finding 38)
- docs/views/evidence/oa-1.jsonl lines 4752 (finding 39)
- docs/views/evidence/oa-1.jsonl lines 5780 (finding 40)
- docs/views/evidence/oa-2.jsonl lines 3271-3272, 3276-3277, 3281-3282, 3286-3287, 3291-3292, 3296-3297, 3301-3302 (finding 41)
- docs/views/evidence/oa-3.jsonl lines 75-76, 271-272 (finding 42)
- docs/views/evidence/oa-3.jsonl lines 460, 462 (finding 43)
- docs/views/evidence/oa-3.jsonl lines 488 (finding 44)
- docs/views/evidence/oa-3.jsonl lines 552 (finding 45)
- docs/views/evidence/oa-4.jsonl lines 201-202 (finding 46)
- docs/views/evidence/oa-4.jsonl lines 227, 229, 235-236 (finding 47)
- docs/views/evidence/oa-4.jsonl lines 276 (finding 48)
- docs/views/evidence/oa-4.jsonl lines 334, 437 (finding 49)
- docs/views/evidence/oa-4.jsonl lines 566-572 (finding 50)
- docs/views/evidence/oa-4.jsonl lines 687-688 (finding 51)
- docs/views/evidence/oa-5.jsonl lines 180, 185, 190, 207, 216 (finding 52)
- docs/views/evidence/oa-5.jsonl lines 238 (finding 53)
- docs/views/evidence/oa-5.jsonl lines 291-294 (finding 54)
- docs/views/evidence/oa-5.jsonl lines 942-946 (finding 55)
- docs/views/evidence/oa-6.jsonl lines 630 (finding 56)
- docs/views/evidence/oa-7.jsonl lines 531 (finding 57)
- docs/views/evidence/oa-7.jsonl lines 564-565 (finding 58)
- docs/views/evidence/oa-7.jsonl lines 591-595 (finding 59)
- docs/views/evidence/oa-7.jsonl lines 790-791, 926-944, 1025-1026 (finding 60)
- docs/views/evidence/oa-7.jsonl lines 1342 (finding 61)
- docs/views/evidence/oa-8.jsonl lines 133-179 (finding 62)

### Grades where the keep_g rule overrides the burst 9 sample reading (docs/views/audit/decisions.jsonl is tool output) (7)

SAMPLE.md accepts these seven disagreements; the grade each sample reading gives is in brackets.

- bee:141 (to g or retract: a display convention) (finding 23)
- ground-invertebrates:133 (to m) (finding 24)
- herps:44 (to m) (finding 26)
- methods:42 (to m) (finding 27)
- plant-fungus-slime:53 (to g) (finding 29)
- sea-invertebrates:78 (to m) (finding 30)
- squirrel-deer-rabbit:77 (to m) (finding 31)

### Records whose unit field differs from their file name (left uncorrected) (58)

Their `unit` field is "intake" in several intake files, so `intake:<line>` names a line in each of them; an ALL.jsonl line would retract all of them in gaps.py. A tool-level id fix comes first.

- intake-3.jsonl:17 (unit field 'intake', so its id intake:17 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Molecular Biology and Evolution 20(6): 855-861; findings [74])
- intake-3.jsonl:18 (unit field 'intake', so its id intake:18 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Molecular Biology and Evolution 20(6): 855-861; findings [74])
- intake-3.jsonl:19 (unit field 'intake', so its id intake:19 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Molecular Biology and Evolution 20(6): 855-861; findings [74])
- intake-3.jsonl:20 (unit field 'intake', so its id intake:20 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Molecular Biology and Evolution 20(6): 855-861; findings [74])
- intake-3.jsonl:21 (unit field 'intake', so its id intake:21 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Molecular Biology and Evolution 20(6): 855-861; findings [74])
- intake-3.jsonl:22 (unit field 'intake', so its id intake:22 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Molecular Biology and Evolution 20(6): 855-861; findings [74])
- intake-3.jsonl:23 (unit field 'intake', so its id intake:23 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Molecular Biology and Evolution 20(6): 855-861; findings [74])
- intake-3.jsonl:24 (unit field 'intake', so its id intake:24 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Molecular Biology and Evolution 20(6): 855-861; findings [74])
- intake-3.jsonl:25 (unit field 'intake', so its id intake:25 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Molecular Biology and Evolution 20(6): 855-861; findings [74])
- intake-3.jsonl:26 (unit field 'intake', so its id intake:26 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Molecular Biology and Evolution 20(6): 855-861; findings [74])
- intake-3.jsonl:27 (unit field 'intake', so its id intake:27 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Molecular Biology and Evolution 20(6): 855-861; findings [74])
- intake-3.jsonl:28 (unit field 'intake', so its id intake:28 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Molecular Biology and Evolution 20(6): 855-861; findings [74])
- intake-5.jsonl:23 (unit field 'intake', so its id intake:23 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Frontiers in Animal Science 5: 1433181; findings [76])
- intake-5.jsonl:24 (unit field 'intake', so its id intake:24 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Frontiers in Animal Science 5: 1433181; findings [76])
- intake-5.jsonl:25 (unit field 'intake', so its id intake:25 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Frontiers in Animal Science 5: 1433181; findings [76])
- intake-5.jsonl:26 (unit field 'intake', so its id intake:26 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Frontiers in Animal Science 5: 1433181; findings [76])
- intake-5.jsonl:27 (unit field 'intake', so its id intake:27 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Frontiers in Animal Science 5: 1433181; findings [76])
- intake-5.jsonl:28 (unit field 'intake', so its id intake:28 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Frontiers in Animal Science 5: 1433181; findings [76])
- intake-5.jsonl:29 (unit field 'intake', so its id intake:29 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Frontiers in Animal Science 5: 1433181; findings [76])
- intake-5.jsonl:30 (unit field 'intake', so its id intake:30 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Frontiers in Animal Science 5: 1433181; findings [76])
- intake-5.jsonl:31 (unit field 'intake', so its id intake:31 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Frontiers in Animal Science 5: 1433181; findings [76])
- intake-5.jsonl:32 (unit field 'intake', so its id intake:32 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Frontiers in Animal Science 5: 1433181; findings [76])
- intake-5.jsonl:33 (unit field 'intake', so its id intake:33 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Journal of Comparative Neurology 521(9): 2042-2057; findings [75])
- intake-5.jsonl:34 (unit field 'intake', so its id intake:34 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Journal of Comparative Neurology 521(9): 2042-2057; findings [75])
- intake-5.jsonl:35 (unit field 'intake', so its id intake:35 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Journal of Comparative Neurology 521(9): 2042-2057; findings [75])
- intake-6.jsonl:27 (unit field 'intake', so its id intake:27 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Nature 498(7452): 65-69; findings [77])
- intake-6.jsonl:28 (unit field 'intake', so its id intake:28 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Nature 498(7452): 65-69; findings [77])
- intake-8-failed.jsonl:2 (unit field 'intake', so its id intake:2 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Vision Research 14(10): 965-970; findings [78])
- intake-8-failed.jsonl:3 (unit field 'intake', so its id intake:3 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Vision Research 14(10): 965-970; findings [78])
- intake-8-failed.jsonl:4 (unit field 'intake', so its id intake:4 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Vision Research 14(10): 965-970; findings [78])
- intake-8-failed.jsonl:5 (unit field 'intake', so its id intake:5 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Vision Research 14(10): 965-970; findings [78])
- intake-8.jsonl:17 (unit field 'intake', so its id intake:17 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Documenta Ophthalmologica 18(1): 128-136; findings [79])
- oa-regraded.jsonl:63 (unit field 'oa-1', so its id oa-1:63 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Journal of comparative physiology. A, Sensory, neural, and behavioral physiology 157(5): 579-586; findings [212])
- oa-regraded.jsonl:64 (unit field 'oa-1', so its id oa-1:64 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Journal of comparative physiology. A, Sensory, neural, and behavioral physiology 157(5): 579-586; findings [212])
- oa-regraded.jsonl:65 (unit field 'oa-1', so its id oa-1:65 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Journal of comparative physiology. A, Sensory, neural, and behavioral physiology 157(5): 579-586; findings [212])
- oa-regraded.jsonl:66 (unit field 'oa-1', so its id oa-1:66 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Journal of comparative physiology. A, Sensory, neural, and behavioral physiology 157(5): 579-586; findings [212])
- oa-regraded.jsonl:68 (unit field 'oa-1', so its id oa-1:68 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Vision Research 38(17): 2629-2634; findings [213])
- oa-regraded.jsonl:69 (unit field 'oa-1', so its id oa-1:69 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Vision Research 38(17): 2629-2634; findings [213])
- oa-regraded.jsonl:70 (unit field 'oa-1', so its id oa-1:70 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Vision Research 38(17): 2629-2634; findings [213])
- oa-regraded.jsonl:71 (unit field 'oa-1', so its id oa-1:71 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Vision Research 38(17): 2629-2634; findings [213])
- oa-regraded.jsonl:80 (unit field 'oa-1', so its id oa-1:80 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Ibis 167(2): 386-396; findings [214])
- oa-regraded.jsonl:81 (unit field 'oa-1', so its id oa-1:81 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Ibis 167(2): 386-396; findings [214])
- oa-regraded.jsonl:82 (unit field 'oa-1', so its id oa-1:82 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Ibis 167(2): 386-396; findings [214])
- oa-regraded.jsonl:83 (unit field 'oa-1', so its id oa-1:83 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Ibis 167(2): 386-396; findings [214])
- oa-regraded.jsonl:84 (unit field 'oa-1', so its id oa-1:84 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Ibis 167(2): 386-396; findings [214])
- oa-regraded.jsonl:85 (unit field 'oa-1', so its id oa-1:85 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Ibis 167(2): 386-396; findings [214])
- oa-regraded.jsonl:86 (unit field 'oa-1', so its id oa-1:86 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Ibis 167(2): 386-396; findings [214])
- oa-regraded.jsonl:87 (unit field 'oa-7', so its id oa-7:87 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Planta 114(2): 143-157; findings [211])
- recheck-1-fixed.jsonl:7 (unit field 'recheck-1', so its id recheck-1:7 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Acta Agrobotanica 63(2): 41-49; findings [215])
- recheck-1-fixed.jsonl:11 (unit field 'recheck-1', so its id recheck-1:11 names a line in several files; fix wanted: author list had a placeholder or et al.; full list from the Crossref record (ci runs/crossref); findings [257])
- recheck-2-fixed.jsonl:2 (unit field 'recheck-2', so its id recheck-2:2 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Annals of Botany 123(6): 1005-1016; title as the Crossref record for the DOI gives it (ci runs/crossref); findings [217, 2483])
- reread-1.jsonl:6 (unit field 'intake', so its id intake:6 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Vision Research 14(10): 965-970; findings [228])
- reread-1.jsonl:7 (unit field 'intake', so its id intake:7 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Vision Research 14(10): 965-970; findings [228])
- reread-1.jsonl:8 (unit field 'intake', so its id intake:8 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Vision Research 14(10): 965-970; findings [228])
- reread-1.jsonl:9 (unit field 'intake', so its id intake:9 names a line in several files; fix wanted: journal field had no volume; Crossref (ci runs/crossref) gives Vision Research 14(10): 965-970; findings [228])
- intake:4 (partial wanted, finding 295; the id names a line in several files)
- intake:5 (partial wanted, finding 295; the id names a line in several files)
- intake:23 (partial wanted, finding 296; the id names a line in several files)

### Gap tables

Regenerate `docs/views/gaps/` from the source set the desk settles on (finding 1), then recheck the 280 cells of root cause 4. No search record or wanted line was removed here.
