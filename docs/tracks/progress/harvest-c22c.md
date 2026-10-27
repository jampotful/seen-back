# harvest-c22c (desk screening, plant genera; 27 October 2026)

Branch research/harvest-c22c, cut from origin/main af02fcc0. This unit takes the ten genera harvest-c22b left (Nemophila to Physocarpus) and three more (Stylophorum, Cyclamen, Delphinium), screened under docs/tracks/prompts/desk-screen.md points 1 to 10, with point 10 (a) to (e) as rewritten on 27 October, and the plant paragraph of round4-harvest.md, after reading audits 81 and 82. Files: docs/views/searched/harvest-c22c.jsonl and docs/views/wanted/harvest-c22c.jsonl. No evidence records. Gate: `screen_candidates.py --check` prints 0 problems before every commit.

## Method

OpenAlex refused this machine (proxy 403 CONNECT on api.openalex.org), so no OpenAlex step ran here. Twelve genera are in no harvest run and hold web searches only, as their records say; Physocarpus is in harvest run 3, and its record lists the harvest's twelve queries and family review word for word before the web searches.

Each genus got the point 10(e) germination searches first ("<Genus> seed germination light dark"; "<Genus> germination gibberellin OR smoke OR dormancy"), then "<Genus> floral scent volatiles" (and "Nerium jasmonate herbivore" for the shrub), then "flower opening time anthesis" and "plant ocelli lens-like epidermal cells focusing light" under the scientific and the common name. Where a cell was about to get a "none" record, a third search with other words went first: Nemophila and Galactites light (species-level germination searches), Physocarpus light (a shading search), Dalea and Stylophorum diel (pollination searches). Three of those five follow-ups found a candidate, so the cell moved to the wanted list. Epacris got no chemical search, since main holds its sense_chemical evidence (sweep-96, Epacris tasmanica smoke germination).

The search tool returned titles and links without snippets, so results were judged by title, and nothing was opened. A result whose title names germination, dormancy or light requirements for a species of the genus went on the wanted list and kept those traits out of the record (point 10e). So did untitled results that came back high on a genus search and may hold such a trial, a hormone or elicitor response, living-flower volatiles or an hour of opening. Distilled oils and extracts (Dalea bicolor essential oil; Delphinium speciosum aerial-part volatiles) were set aside under 10(a).

## Genera

| Genus | Records | Left out, and why |
|---|---|---|
| Nemophila | eye_type | sense_light_nonvisual: untitled Oecologia article 10.1007/BF00377311 from a third light search. sense_chemical: USGS "Mechanism of smoke-induced seed germination in a post-fire chaparral annual", the Annales Botanici Fennici smoke and karrikinolide paper (10.5735/085.061.0106) and an untitled Annals of Botany 62 file. diel: the recurring untitled table of Plants 13: 183 (PMC10818387). |
| Heliopsis | eye_type | sense_light_nonvisual and sense_chemical: "Factors affecting seed germination of Heliopsis helianthoides" (RNGR listing). diel: PMC10818387 table. |
| Galactites | eye_type | sense_light_nonvisual: untitled PMC2802935 figure and other untitled germination items from a third search. sense_chemical: the Annales Botanici Fennici smoke paper. diel: "Sequential Flowering of Thistles Cynareae" (Aust J Bot 34(4): 455). |
| Calandrinia | eye_type | light and chemical: the Chilean sand-dune seed dormancy study, the AFF report on growth regulators and flowering of Calandrinia, the NPN protocol. diel: an untitled Nuytsia PDF, PMC10818387 table. |
| Adonis | eye_type | light and chemical: "Seed Dormancy in Cereal Weed Adonis flammea" and an untitled JAST 20(1) article. diel: an untitled Journal of Ecology and Environment 37(4) article. |
| Dalea | eye_type | light and chemical: the Dalea foliosa life-cycle study (Kentucky), an untitled Ecological Restoration item, the RNGR coloured-light listing. diel: "An Evaluation of Pollination Mechanisms for Purple Prairie-clover" from a third search. |
| Nerium | eye_type | light: untitled Redalyc and Bologna items. chemical: an untitled Molecules 27(2): 408 article and other untitled scent results. diel: PMC10818387 table. |
| Epacris | eye_type | sense_light_nonvisual: Gilmour, Crowden and Koutoulis 2000 (10.1071/BT99029), already on main for sense_chemical, tested darkness as a germination cue. sense_chemical: evidence on main. diel: PMC10818387 table ("Raciation in Epacris impressa. II. Habitat differences and flowering times" also came back; by its title the times are seasonal). |
| Polemonium | eye_type | light and chemical: "Germination Ecophysiology of ... Polemonium reptans var. reptans" (Kentucky), the NPN protocol; chemical also the P. viscosum aroma page and an untitled Acta Physiologiae Plantarum article. diel: "Reproduction in Polemonium: factors influencing outbreeding potential", PMC10818387 table. |
| Physocarpus (run 3) | eye_type | light: PeerJ low-light study on P. amurensis and P. opulifolius 'Diabolo' (shading search). chemical: two untitled Acta Physiologiae Plantarum articles and the harvest's Rosaceae phytoalexin survey (10.1515/znc-1994-9-1014, copper-ion elicitor; excised-leaf fork). diel: the harvest's P. amurensis pollen, stigma and pollinator study (W2240538196). |
| Stylophorum | eye_type, diel | light and chemical: an untitled Native Plants Journal 24(2): 80 article; chemical also an untitled Acta Physiologiae Plantarum article. |
| Cyclamen | eye_type | light: an untitled Turkish Journal of Botany 33(4) PDF and ISHS 261_45. chemical: ISHS 261_45, an untitled AREEO article and "The influence of the cultivation environment on the fragrance of cyclamens" (10.17221/110/2017-HORTSCI). diel: untitled Plant Biology 9(1) article 10.1055/s-2006-924649. |
| Delphinium | eye_type | light and chemical: untitled Plant Ecology article 10.1007/s11258-010-9775-0; light also the RNGR coloured-light listing. diel: an untitled Acta Agrobotanica 65 PDF, PMC10818387 table. |

## Notes for the reader of the wanted list

The untitled table PMC10818387 (Plants 13: 183) came back for flower-opening searches across seven unrelated genera, and the Annales Botanici Fennici smoke and karrikinolide paper for six; both are more likely general works than studies of these genera, and one reading of each settles many cells at once. Two results came from library proxy or login hosts (shibboleth.idm.home.nyu.edu for the Physocarpus light search; 0-www-mdpi-com.brum.beds.ac.uk for the Cyclamen gibberellin search); neither was opened, and the Cyclamen line points to the DOAJ record instead. No ResearchGate result was opened; one academia.edu result (Adonis and Stylophorum scent searches) was left closed.

## Totals

13 genera done, 14 search records (13 eye_type and Stylophorum diel), 40 wanted lines (authors empty throughout; DOIs only where a result link, the harvest or a record on main printed them), check 0 problems. 96 web searches of the ration of 110 were used. No page was opened (WebFetch not used) and no evidence was written. No genera are left.
