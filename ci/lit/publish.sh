#!/usr/bin/env bash
# Join the topics' collections and publish them to pub/lit-<label>; the summaries come back on ci.
set -uo pipefail
mkdir -p corpus out
for d in parts/lit-*/; do cp -R "$d"/. corpus/; done
label="${GITHUB_REF_NAME#run/lit/}"
python3 - <<'PY'
import glob, json, os
rows, seen = [], {}
for p in sorted(glob.glob("corpus/*/index.jsonl")):
    topic = p.split("/")[1]
    for line in open(p, encoding="utf-8"):
        w = json.loads(line)
        k = w["key"]
        if k in seen:
            seen[k]["topics"].append(topic)
            continue
        w["topics"] = [topic]
        if w.get("text"):
            w["text"] = topic + "/" + w["text"]
        seen[k] = w; rows.append(w)
with open("corpus/all.jsonl", "w", encoding="utf-8") as f:
    for w in rows:
        f.write(json.dumps(w, ensure_ascii=False) + "\n")
L = ["# The senses literature", "", "Gathered by `tools/lit/harvest.py` from OpenAlex and Europe PMC. Each topic's folder holds `index.jsonl` (one work a line: citation, OpenAlex's abstract, licence, addresses, and `text` where the full text of an openly licensed work was kept) and `text/`. `all.jsonl` joins the topics, one line per work with the topics it was found under. Full texts are kept only for works under a Creative Commons licence or in the public domain; every other work keeps its citation, abstract and addresses.", "",
     "| Topic | works | with an abstract | full texts |", "|---|---:|---:|---:|"]
for p in sorted(glob.glob("corpus/*/index.jsonl")):
    topic = p.split("/")[1]
    ws = [json.loads(l) for l in open(p, encoding="utf-8")]
    L.append("| %s | %d | %d | %d |" % (topic, len(ws), sum(1 for w in ws if w.get("abstract")), sum(1 for w in ws if w.get("text"))))
L += ["", "All topics: %d works, %d full texts." % (len(rows), sum(1 for w in rows if w.get("text")))]
open("corpus/README.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
open("out/SUMMARY.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
PY
for s in corpus/*/SUMMARY.md; do t="$(basename "$(dirname "$s")")"; cp "$s" "out/$t.md"; done
cp corpus/*.log.txt out/ 2>/dev/null || true
du -sh corpus | tee -a out/SUMMARY.md
# no single file may pass GitHub's 100 MB limit
find corpus -type f -size +95M -print -delete | sed 's/^/dropped (too large): /' | tee -a out/SUMMARY.md
bash ci/put_branch.sh "pub/lit-$label" corpus "the senses literature, $label"
