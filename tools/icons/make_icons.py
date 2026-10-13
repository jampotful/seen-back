"""Renders the app's icon files from the two SVG sources in icons/source/ (design 18m2, a goat's eye printed in three inks).
Run from the repository root:  python3 -I tools/icons/make_icons.py
Needs python playwright with Chromium (the SVGs use feTurbulence filters, which a plain rasteriser may draw differently).
Writes icons/icon-512.png, icon-192.png, icon-180.png, icon-32.png from icon-master.svg, icons/icon-maskable-512.png from icon-adaptive.svg
(its art sits inside the centre 66 of 108 units, so any mask keeps it)."""
import re, sys
from playwright.sync_api import sync_playwright
SRC = 'icons/source/'
def page_for(svg, px):
    svg = re.sub(r'(<svg[^>]*?)\swidth="\d+"\s+height="\d+"', r'\1', svg, count=1)
    svg = svg.replace('<svg ', '<svg width="%d" height="%d" ' % (px, px), 1)
    return '<body style="margin:0;background:#000">' + svg + '</body>'
def render(pg, svg, px, out):
    pg.set_viewport_size({'width': px, 'height': px}); pg.set_content(page_for(svg, px)); pg.wait_for_timeout(150)
    pg.screenshot(path=out, clip={'x': 0, 'y': 0, 'width': px, 'height': px})
master = open(SRC + 'icon-master.svg').read(); adaptive = open(SRC + 'icon-adaptive.svg').read()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    for px in (512, 192, 180, 32): render(pg, master, px, 'icons/icon-%d.png' % px)
    render(pg, adaptive, 512, 'icons/icon-maskable-512.png')

    b.close()
