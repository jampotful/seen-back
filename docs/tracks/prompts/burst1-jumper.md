# Burst 1: jumping spider research (Sonnet)

Read `docs/views/research/BRIEF.md` for the evidence rules, the log format, the branch and the writing rules. This burst is narrower than the brief's full sheet: it serves the engine's `jumper` view, which another agent is building at the same time. Your launch prompt also carries private details (the owner's Drive papers and a specialist's account). Never write those into any file you push. Stop after 75 minutes.

On `research/jumper`, deliver:

1. `docs/views/evidence/jumper.jsonl`, extended. Keep the 20 records already there, and add to them without duplicating any.
2. `docs/views/drafts/jumper.md`, rewritten as a parameter table for the view. Give one row for each setting the view needs: each eye pair's field, sharpness and colour classes; the gaze strip's width, jump speed and latency; the scanning sweeps and their rate; the dwell; the time a place is ignored after a look; flicker; dim light; and the sleep-like retinal bouts. Each row gives the value, its log lines and its grade, and says `invented` where the evidence runs out. After the table come a genus-by-genus colour table (two receptor classes, three or more, or unmeasured), then at most six questions for a jumping spider specialist whose answers would change the view.
3. `docs/views/wanted/jumper.jsonl`.
4. `docs/views/progress/jumper.md`, updated with each push.

Method: search before you read. Extract each paper or book to a text file (the brief's download-and-`pdftotext` method for Drive PDFs), grep it for what you need (eye names, cycles, deg, nm, Hz, retina, saccade, scan, latency), and read only the passages around each match. Never load a whole book into context. Before logging a quote, grep the extracted text for it. Draft any rows plainly; their final wording comes later, in one pass over every view. Push every 15 minutes, and if your context passes about 100,000 tokens, update the progress note and stop.

Final report, at most 250 words: the parameter values the engine should use, the weakest of them, the specialist questions, and your last commit.
