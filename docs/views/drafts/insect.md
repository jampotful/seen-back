# Sensing sheet: insects other than bees and wasps (`insect`), draft

Started 13 October 2026, 01:46 UTC. This sheet re-checks the existing view `insect` in `src/cam.a.js` (build 22) against `docs/SOURCES.md` and the primary literature, and proposes where the view should split. The evidence log is `docs/views/evidence/insect.jsonl` and the wanted list is `docs/views/wanted/insect.jsonl`.

Status: in progress.

## 1. Scope (in progress)

World record counts are iNaturalist research-grade records in GBIF, read on 11 October 2026 (`runs/fetch/10/world-order.json` and `world-family-top.json` on the `ci` branch). Family names for keys missing from that run were read from GBIF's species API on 13 October through the web tool, because the shell's egress proxy refuses api.gbif.org.

- Lepidoptera 19,511,852: butterflies (Nymphalidae 4,407,751, Lycaenidae 1,330,784, Hesperiidae 1,120,084, Pieridae 974,969, Papilionidae 862,188, Riodinidae 45,712, Hedylidae 1,452) 8,742,940, or 44.8%; moths 55.2% (Erebidae 2,142,693, Noctuidae 2,028,294, Geometridae 2,020,890, Crambidae 1,051,630, Sphingidae 633,706, Tortricidae 449,897, Saturniidae 326,675).
- Odonata 3,479,477: dragonflies (Anisoptera) 65.6%, damselflies (Zygoptera) 34.3%.
- Coleoptera 5,702,967: Coccinellidae 21.5%, Cerambycidae 12.3%, Scarabaeidae 12.1%, Chrysomelidae 10.4%, Carabidae 7.6%, Lampyridae 1.2%.
