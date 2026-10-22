#!/usr/bin/env python3
"""Renders assets/og.png (1200x630 social card) from plain text; no remote assets."""
import os, sys
from playwright.sync_api import sync_playwright
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "og.png")
HTML = """<body style="margin:0;width:1200px;height:630px;background:#efe7d6;color:#2b2118;font-family:Georgia,'Times New Roman',serif;box-sizing:border-box;padding:70px 80px;border-top:14px double #2b2118;border-bottom:14px double #2b2118">
<div style="font:600 26px monospace;letter-spacing:.08em;color:#9c3a22">PORTFOLIO</div>
<div style="font-size:110px;line-height:1.05;margin-top:70px">Karthik Karumanchi</div>
<div style="font-size:44px;margin-top:30px">Control of robots and spacecraft</div>
<div style="font:28px monospace;margin-top:60px;color:#5b4e40">MS Mechanical Engineering, Carnegie Mellon University</div></body>"""
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1200, "height": 630})
    pg.set_content(HTML); pg.screenshot(path=OUT); b.close()
