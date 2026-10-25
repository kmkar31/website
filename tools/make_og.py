#!/usr/bin/env python3
"""Renders assets/og.png (1200x630 social card) from plain text; no remote assets."""
import os, sys, math
from playwright.sync_api import sync_playwright
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "og.png")
pts = [(40 + i * 55, 100 + 42 * math.sin(i * 0.95)) for i in range(8)]
SNAKE = "".join(f'<line x1="{a[0]:.0f}" y1="{a[1]:.0f}" x2="{b[0]:.0f}" y2="{b[1]:.0f}" stroke="#2b2118" stroke-width="7" stroke-linecap="round"/>' for a, b in zip(pts, pts[1:])) + "".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="8" fill="#efe7d6" stroke="#2b2118" stroke-width="3"/>' for x, y in pts)
HTML = """<body style="margin:0;width:1200px;height:630px;background:#efe7d6;color:#2b2118;font-family:Georgia,'Times New Roman',serif;box-sizing:border-box;padding:70px 80px;border-top:14px double #2b2118;border-bottom:14px double #2b2118">
<div style="font:600 26px monospace;letter-spacing:.08em;color:#9c3a22">PORTFOLIO</div>
<div style="font-size:110px;line-height:1.05;margin-top:50px">Karthik Karumanchi</div>
<div style="font-size:44px;margin-top:30px">Control of robots and spacecraft</div>
<div style="font:28px monospace;margin-top:40px;color:#5b4e40">MS Mechanical Engineering, Carnegie Mellon University</div><div style="position:absolute;right:60px;bottom:34px;width:280px;border:3px solid #2b2118;background:#f6f0e2;box-shadow:6px 6px 0 #2b2118"><svg viewBox="0 0 480 200" width="280" height="117" style="display:block">%s</svg><div style="font:600 12px monospace;letter-spacing:.04em;color:#5b4e40;border-top:3px solid #2b2118;padding:6px 10px">FIG. 1 &middot; SNAKE ROBOT, SCHEMATIC</div></div></body>""" % SNAKE
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1200, "height": 630})
    pg.set_content(HTML); pg.screenshot(path=OUT); b.close()
