# The world test of the full database

3500 photos, research grade, dated 2025 or later, about 500 a continent; 427163 rows; 97.9% of the photos' species have a row. Right species first, with the prior's weight chosen for each continent on the other six. Made by tools/world/worldtest.py.

| Continent | Photos | none | zone@ship1 | zone@ship2 | zone+3@ship1 | zone+3@ship2 | circle |
|---|---:|---:|---:|---:|---:|---:|---:|
| AF | 500 | 65.6% | 79.6% | 79.6% | 80.6% | 80.4% | 82.2% |
| AS | 500 | 63.8% | 78.6% | 78.8% | 81.0% | 80.8% | 82.0% |
| EU | 500 | 76.2% | 90.2% | 90.6% | 91.0% | 91.2% | 90.0% |
| NA | 500 | 79.0% | 90.4% | 90.6% | 91.0% | 91.0% | 91.2% |
| OC | 500 | 69.2% | 82.8% | 83.0% | 84.2% | 84.2% | 84.6% |
| SA | 500 | 66.2% | 78.0% | 78.0% | 78.8% | 78.4% | 79.4% |
| AN | 500 | 26.8% | 31.8% | 32.0% | 33.6% | 33.4% | 42.0% |
| all | 3500 | 63.8% (62.2 to 65.4) | 75.9% (74.5 to 77.3) | 76.1% (74.7 to 77.4) | 77.2% (75.8 to 78.6) | 77.1% (75.7 to 78.5) | 78.8% (77.5 to 80.1) |

Named at the level that was right 97 times in 100 on the other six continents, and the share of those names right:

| Continent | none | zone@ship1 | zone@ship2 | zone+3@ship1 | zone+3@ship2 | circle |
|---|---:|---:|---:|---:|---:|---:|
| AF | 30.6% named, 98.0% right | 59.8% named, 98.0% right | 61.0% named, 97.7% right | 64.2% named, 99.1% right | 64.2% named, 99.1% right | 68.4% named, 98.0% right |
| AS | 33.6% named, 98.2% right | 64.4% named, 96.6% right | 64.4% named, 96.6% right | 66.6% named, 97.6% right | 66.6% named, 97.0% right | 67.8% named, 97.6% right |
| EU | 42.2% named, 98.6% right | 77.0% named, 99.5% right | 77.8% named, 99.2% right | 80.2% named, 99.0% right | 79.8% named, 99.0% right | 81.2% named, 98.8% right |
| NA | 46.2% named, 97.4% right | 78.0% named, 98.2% right | 77.2% named, 98.2% right | 79.6% named, 98.5% right | 79.6% named, 98.2% right | 82.8% named, 98.1% right |
| OC | 32.2% named, 98.1% right | 67.6% named, 97.6% right | 67.6% named, 97.6% right | 73.2% named, 97.5% right | 71.8% named, 97.5% right | 72.2% named, 97.5% right |
| SA | 26.6% named, 98.5% right | 56.8% named, 98.2% right | 56.8% named, 98.2% right | 63.6% named, 96.9% right | 63.4% named, 97.2% right | 64.0% named, 97.2% right |
| AN | 13.0% named, 78.5% right | 21.4% named, 72.9% right | 22.0% named, 75.5% right | 23.8% named, 75.6% right | 24.2% named, 74.4% right | 28.4% named, 83.8% right |
| all | 32.1% named, 97.0% right | 60.7% named, 96.8% right | 61.0% named, 96.8% right | 64.5% named, 96.9% right | 64.2% named, 96.8% right | 66.4% named, 97.0% right |

Alpha chosen on the other six continents: zone@ship1 AF 1.25,AS 1,EU 1.25,NA 1,OC 1,SA 1,AN 1.25; zone@ship2 AF 1,AS 1,EU 1,NA 1,OC 1,SA 1,AN 1; zone+3@ship1 AF 1,AS 1,EU 1,NA 1,OC 1,SA 1,AN 1; zone+3@ship2 AF 1,AS 1,EU 1,NA 1,OC 1,SA 1,AN 1; circle AF 1.25,AS 1.5,EU 1.25,NA 1.25,OC 1.25,SA 1.25,AN 1.25
Alpha best on every photo: zone@ship1 1; zone@ship2 1; zone+3@ship1 1; zone+3@ship2 1; circle 1.25
Creatures met: 3486 photos had three, 14 fewer.
