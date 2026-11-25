#!/usr/bin/env python3
"""Keyboard focus checks (WCAG 2.2 Focus Not Obscured, lightbox trap/return).

Usage: python3 tools/focus_check.py [site_dir]
Tabs through every page at phone and desktop width; fails if a focused element
is hidden behind the sticky header or off screen. Then opens the lightbox on
pages with zoomable figures and checks focus moves to Close, stays trapped on
Tab, and returns to the opener on Escape.
"""
import glob, os, sys
from playwright.sync_api import sync_playwright

def _png(w=200, h=150):
    import struct, zlib
    ch = lambda t, d: struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d))
    raw = b"".join(b"\x00" + b"\xcc\xcc\xcc" * w for _ in range(h))
    return b"\x89PNG\r\n\x1a\n" + ch(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)) + ch(b"IDAT", zlib.compress(raw)) + ch(b"IEND", b"")
PNG = _png()
SITE = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
fails = []
with sync_playwright() as p:
    b = p.chromium.launch()
    for vp, (w, h) in {"phone": (390, 844), "desktop": (1366, 900)}.items():
        ctx = b.new_context(viewport={"width": w, "height": h}, has_touch=(vp == "phone"), is_mobile=(vp == "phone"))
        # Serve a stub image for remote requests so figures count as loaded and zoom links are real tab stops.
        ctx.route("**/*", lambda r: r.continue_() if r.request.url.startswith("file:") else r.fulfill(status=200, content_type="image/png", body=PNG))
        pg = ctx.new_page()
        for f in sorted(glob.glob(os.path.join(SITE, "*.html"))):
            name = os.path.basename(f)
            pg.goto("file://" + f, wait_until="domcontentloaded")
            pg.add_style_tag(content="html{scroll-behavior:auto!important}")
            n = pg.evaluate("document.querySelectorAll('a[href],button,input,select,textarea,[tabindex]').length")
            for i in range(n + 3):
                pg.keyboard.press("Tab")
                r = pg.evaluate("""() => { const e = document.activeElement; if (!e || e === document.body) return null;
                  const hd = document.querySelector('.site-header'); const hb = hd ? hd.getBoundingClientRect().bottom : 0;
                  const sticky = hd && getComputedStyle(hd).position === 'sticky';
                  const b = e.getBoundingClientRect(); const inHd = hd && hd.contains(e);
                  return {t: (e.className || e.tagName) + ' ' + (e.getAttribute('href') || ''), top: b.top, bottom: b.bottom, hb: sticky ? hb : 0, inHd, vh: innerHeight, vis: b.width > 0}; }""")
                if not r or not r["vis"] or r["inHd"] or "skip" in r["t"].split()[0]:
                    continue
                if r["top"] < r["hb"] - 1 or r["bottom"] > r["vh"] + 1 or r["top"] < 0:
                    fails.append(f"{vp} {name}: focus obscured/off-screen: {r['t']} top={r['top']:.0f} header={r['hb']:.0f}")
            if vp == "desktop":
                z = pg.query_selector(".project a.zoom")
                if z:
                    pg.goto("file://" + f, wait_until="load")  # fresh page after the Tab loop
                    z = pg.query_selector(".project a.zoom")
                    z.focus(); pg.keyboard.press("Enter"); pg.wait_for_timeout(150)
                    if not pg.url.startswith("file:"): fails.append(f"{name}: zoom link navigated away (lightbox JS did not intercept)"); continue
                    ok = pg.evaluate("!document.getElementById('lightbox').hidden && document.activeElement.classList.contains('lb-close')")
                    pg.keyboard.press("Tab"); pg.keyboard.press("Shift+Tab")
                    trapped = pg.evaluate("document.activeElement.classList.contains('lb-close')")
                    pg.keyboard.press("Escape")
                    back = pg.evaluate("document.activeElement.classList.contains('zoom') && document.getElementById('lightbox').hidden")
                    if not (ok and trapped and back):
                        fails.append(f"{name}: lightbox open={ok} trapped={trapped} returned={back}")
        ctx.close()
    b.close()
print("\n".join(fails) if fails else "focus_check: OK")
sys.exit(1 if fails else 0)
