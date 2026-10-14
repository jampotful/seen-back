"""Lists wanted papers that the published Papers Wanted page does not hold yet, as ArtifactData batch files.
Usage: python3 -I tools/views/papers_extra.py IN.csv BASE_IDS.json OUT_DIR
IN.csv comes from wanted_csv.py. BASE_IDS.json is docs/views/papers-base-ids.json (ids embedded in the page).
Writes OUT_DIR/batch-N.json (up to 50 `set` writes each, collection `extra`) and prints how many are new.
Papers already added are listed in OUT_DIR/../papers-extra-ids.json when you keep it; pass nothing to resend all."""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from papers_page import row
src, base, out = sys.argv[1], set(json.load(open(sys.argv[2]))), sys.argv[3]
new = [row(r) for r in csv.DictReader(open(src, encoding='utf-8'))]
new = [r for r in new if r['id'] not in base]
os.makedirs(out, exist_ok=True)
for i in range(0, len(new), 50):
    json.dump({'writes': [{'op': 'set', 'collection': 'extra', 'doc_id': r['id'], 'data': r} for r in new[i:i + 50]]}, open(f'{out}/batch-{i // 50 + 1}.json', 'w'), ensure_ascii=False)
print(len(new), 'new papers,', (len(new) + 49) // 50, 'batch files in', out)
