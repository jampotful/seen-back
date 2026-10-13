# The full database's world rows

BioCLIP 2's text rows for every species with a research-grade iNaturalist record through 2024, under GBIF's
names, one sentence a species ("a photo of <name>."), at one byte a number with a scale a row; made by
.github/workflows/worlddb.yml (tools/world/names.py, tools/coverage/text.py, tools/world/pack.py).
parts.json gives every file with its length and SHA-256. rows.tsv says where each name came from.
