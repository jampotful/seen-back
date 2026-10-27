# harvest-c22c (desk screening, plant genera; 27 October 2026)

Branch research/harvest-c22c, cut from origin/main af02fcc0. This unit takes the ten genera harvest-c22b left (Nemophila to Physocarpus) and three more (Stylophorum, Cyclamen, Delphinium), screened under docs/tracks/prompts/desk-screen.md points 1 to 10, with point 10 (a) to (e) as rewritten on 27 October, and the plant paragraph of round4-harvest.md, after reading audits 81 and 82. Files: docs/views/searched/harvest-c22c.jsonl and docs/views/wanted/harvest-c22c.jsonl. No evidence records. Gate: `screen_candidates.py --check` prints 0 problems before every commit.

## Method

OpenAlex refused this machine (proxy 403 on api.openalex.org), so no OpenAlex step ran here. Genera in no harvest run hold web searches only and say so. Each plant genus got the point 10(e) germination searches first ("<Genus> seed germination light dark"; "<Genus> germination gibberellin OR smoke OR dormancy"), then "<Genus> floral scent volatiles", then "flower opening time anthesis" and "plant ocelli lens-like epidermal cells focusing light" under the scientific and the common name. Results came back as titles and links without snippets, so they were judged by title, and nothing was opened. Any result whose title names germination, dormancy or light requirements for a species of the genus went on the wanted list and kept its traits out of the search record, as did untitled results that may hold such a trial.

## Progress

Done so far: Nemophila, Heliopsis, Galactites, Calandrinia, Adonis, Dalea.
