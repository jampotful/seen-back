import importlib.util, sys
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
spec = importlib.util.spec_from_file_location("m", "tools/views/make_review_jumper.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
F, FS = "Helvetica", 6.6
cell = ParagraphStyle("c", fontName=F, fontSize=FS, leading=FS*1.17)
h2 = ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=8, leading=9.5, spaceBefore=4, spaceAfter=1)
h1 = ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=11, leading=13)
esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
doc = SimpleDocTemplate("/tmp/gen/rl.pdf", pagesize=landscape(letter), leftMargin=22, rightMargin=22, topMargin=20, bottomMargin=20, title="Jumping spider view: parameter table for review")
W = landscape(letter)[0] - 44
cw = [W*x for x in (.14, .41, .045, .13, .10, .175)]
intro = ("These are the settings behind the jumper view of Regards, a phone app that shows a person a photographed animal's view of the world. Grades: m measured in this animal or typical members of the group, g measured in a relative or a wider group, i a guess from nearby evidence, x left out of the picture. “The app's” marks a value the app chose where the evidence runs out. Please fill the last two columns where you disagree or know better, and answer the six questions at the end.")
st = [Paragraph(esc("Jumping spider view: parameter table for review"), h1), Paragraph(esc(intro), cell)]
for name, rows in m.SECTIONS:
    if name.startswith("C."): st.append(PageBreak())
    st.append(Paragraph(esc(name), h2))
    data = [[Paragraph("<b>%s</b>" % t, cell) for t in ("Setting", "Value and units", "Grade", "Source", "Your value", "Your comment")]]
    for s, v, g, ls, ex in rows: data.append([Paragraph(esc(x), cell) for x in (s, v, g, m.src(ls, ex))] + ["", ""])
    t = Table(data, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([("GRID", (0,0), (-1,-1), .4, colors.grey), ("VALIGN", (0,0), (-1,-1), "TOP"), ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#e6e6e6")), ("TOPPADDING", (0,0), (-1,-1), 1), ("BOTTOMPADDING", (0,0), (-1,-1), 1), ("LEFTPADDING", (0,0), (-1,-1), 2.5), ("RIGHTPADDING", (0,0), (-1,-1), 2.5)]))
    st.append(t)
st.append(Paragraph("Questions", h2))
for i, q in enumerate(m.QUESTIONS): st.append(Paragraph(esc("%d. %s" % (i + 1, q)), cell))
doc.build(st)
