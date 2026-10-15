"""Lists wanted papers that the published Papers Wanted page does not hold yet, as ArtifactData batch files.
Usage: python3 -I tools/views/papers_extra.py IN.csv BASE_IDS.json OUT_DIR [HAVE_DIR]
IN.csv comes from gain.py (docs/views/wanted-merged.csv). BASE_IDS.json is docs/views/papers-base-ids.json (ids embedded
in the page). HAVE_DIR, when given, is where ArtifactData saved a "list" of the collection `extra` (out_dir): papers
whose <id>.json is already there are skipped, since a "set" on an existing document needs its version.
Writes OUT_DIR/batch-N.json (up to 50 `set` writes each, collection `extra`) and prints how many are new."""
import csv, glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from papers_page import row
src, base, out = sys.argv[1], set(json.load(open(sys.argv[2]))), sys.argv[3]
have = set()
if len(sys.argv) > 4:
    have = {os.path.basename(p)[:-5] for p in glob.glob(os.path.join(sys.argv[4], '**', '*.json'), recursive=True)}
new = [row(r) for r in csv.DictReader(open(src, encoding='utf-8'))]
new = [r for r in new if r['id'] not in base and r['id'] not in have]
os.makedirs(out, exist_ok=True)
for p in glob.glob(os.path.join(out, 'batch-*.json')): os.remove(p)  # batch files from an earlier run
for i in range(0, len(new), 50):
    json.dump({'writes': [{'op': 'set', 'collection': 'extra', 'doc_id': r['id'], 'data': r} for r in new[i:i + 50]]}, open(f'{out}/batch-{i // 50 + 1}.json', 'w'), ensure_ascii=False)
print(len(new), 'new papers,', (len(new) + 49) // 50, 'batch files in', out)
