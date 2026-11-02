# desk-d349 progress

Angle: spiders, harvestmen, pseudoscorpions and mites, eye number and eye diameter in new-species papers. 5 records filed (target 10), about 38 WebSearch/WebFetch calls. check.py run on the log.

## Filed (docs/views/evidence/desk-d349.jsonl)
- Otacilia khezu (BDJ 12: e126716, 10.3897/bdj.12.e126716): "Eyes absent." filed as eye_type "none (eyes absent)" per main precedent.
- Afrogarypus foordi (African Invertebrates 65(2), 10.3897/afrinvertebr.65.137694): two pairs of corneate eyes, eyes_count 2 pairs.
- Pararoncus leonardi and P. taeyoungi (Evolutionary Systematics 8(1), 10.3897/evolsyst.8.123108): four eyes with lenses; whole semicolon-chain carapace sentences (under 40 words).
- Speleoticus hei (BDJ 11: e107751, 10.3897/bdj.11.e107751): male holotype eye diameters AME/ALE/PME/PLE as eye_diameter_mm list, one sentence; female sentence differs (PLE 0.07) and is noted only.

## Weak spots
- All text came through WebFetch summaries of the Pensoft XML, reassembled from consecutive pieces. Crossref licences not queried; page-printed CC BY 4.0 sentence used.
- Name registries: only P. leonardi checked (WAC, accepted). World Spider Catalog not opened; others rest on the original descriptions.
- Speleoticus quote has a minus sign and en dashes copied as returned; value is a 4-number list.

## Not filed (leads)
- Hou et al. pseudoscorpions (ZooKeys 1097.82527, 1139.96639): "without eyes or eyespots" sits in long semicolon sentences over 40 words.
- Tetrablemmidae Thailand (ZooKeys 1279.189587): Ablemma theppratan "6 eyes", A. yamae "2 vestigal eyes" inside carapace sentences of about 60 words.
- Spiricoelotes metyr and S. zhengi (ZooKeys 1245.145389): eye-diameter sentences are short, but no cave-specific or count value; not taken.
- Troglocoelotes sinanensis already on main; Barinas guanenta, Avima wayuunaiki, Eukoenenia serrana, Promolotra lushui, Choiroblemma metok have no usable eye sentence. Cataleptoneta (ZooKeys 1294.202010) not reached.
- BDJ and WAC URLs not surfaced by search are blocked by WebFetch.
