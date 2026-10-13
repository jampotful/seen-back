"""Turns CC's marks on the Papers Wanted page into docs/views/papers-status.jsonl, which agents read.
Usage: python3 -I tools/views/papers_status.py TICKS.json WANTED.csv OUT.jsonl
TICKS.json is the document ticks/all saved by ArtifactData (action get, with out_dir). WANTED.csv is the merged list
from wanted_csv.py. A mark is true (saved in full), "partial" (printed page with abstract and references only) or
"na" (cannot be obtained). Output lines: {"id","status":"full|partial|n/a","doi","title","authors","year","date"}."""
import csv, json, os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from papers_page import row
raw = json.load(open(sys.argv[1], encoding='utf-8')); marks = raw.get('data', raw)
rows = {r['id']: r for r in (row(x) for x in csv.DictReader(open(sys.argv[2], encoding='utf-8')))}
doi = {pid: x['doi'] for pid, x in ((row(x)['id'], x) for x in csv.DictReader(open(sys.argv[2], encoding='utf-8')))}
today = datetime.date.today().isoformat(); n = 0
with open(sys.argv[3], 'w', encoding='utf-8') as f:
    for pid, v in sorted(marks.items()):
        st = 'full' if v is True or v == 'full' else ('partial' if v == 'partial' else ('n/a' if v == 'na' else ''))
        if not st: continue
        r = rows.get(pid, {})
        f.write(json.dumps({'id': pid, 'status': st, 'doi': doi.get(pid, ''), 'title': r.get('t', ''), 'authors': r.get('a', ''), 'year': r.get('y', ''), 'date': today}, ensure_ascii=False) + '\n'); n += 1
print(n, 'marked papers ->', sys.argv[3])
