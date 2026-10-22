#!/usr/bin/env python3
"""Screenshot + automated checks for the portfolio.

Usage: python3 tools/check.py [site_dir] [out_dir]
Defaults: site_dir=. , out_dir=agents/shots

Renders every page at phone / tablet / desktop in light and dark themes, saves
screenshots, and prints objective findings: horizontal overflow, tap targets
under 44px, low text contrast (WCAG AA), missing alt text, images that failed
to load, missing <h1>, console errors.
Note: external requests (Wix images, Google Fonts) are blocked on purpose so the
run is fast; broken images are reported separately and are not layout bugs.
Screenshots therefore show fallback fonts and empty image boxes until media is
local.
"""
import glob, os, sys
from playwright.sync_api import sync_playwright

SITE = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
OUT = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else "agents/shots")
os.makedirs(OUT, exist_ok=True)
VIEWPORTS = {"phone": (390, 844), "tablet": (820, 1180), "desktop": (1366, 900)}

JS_CHECKS = """() => {
  const lum = c => { const [r,g,b] = c.map(v => { v/=255; return v<=.03928 ? v/12.92 : Math.pow((v+.055)/1.055, 2.4); }); return .2126*r+.7152*g+.0722*b; };
  const parse = s => { const m = s.match(/rgba?\\(([^)]+)\\)/); if(!m) return null; const p = m[1].split(',').map(Number); return {c:p.slice(0,3), a: p.length>3?p[3]:1}; };
  const bgOf = el => { while (el) { const cs0 = getComputedStyle(el); if (cs0.backgroundImage && cs0.backgroundImage !== 'none') return null; const p = parse(cs0.backgroundColor); if (p && p.a > .9) return p.c; el = el.parentElement; } return [255,255,255]; };
  const out = {overflow: document.documentElement.scrollWidth - document.documentElement.clientWidth, small: [], contrast: [], noAlt: [], h1: document.querySelectorAll('h1').length};
  document.querySelectorAll('a,button').forEach(e => { if (e.classList.contains('skip')) return; const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
    if (r.width > 0 && cs.display !== 'inline' && (r.height < 44 || r.width < 44) && cs.visibility !== 'hidden') out.small.push((e.className || e.tagName) + ' ' + Math.round(r.width) + 'x' + Math.round(r.height)); });
  document.querySelectorAll('p,li,h1,h2,h3,span,a,strong,figcaption,button').forEach(e => {
    if (!e.childNodes.length || ![...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) return;
    const cs = getComputedStyle(e); const fg = parse(cs.color); if (!fg || cs.webkitTextFillColor === 'rgba(0, 0, 0, 0)') return;
    const bg = bgOf(e); if (!bg) return; const L1 = lum(fg.c), L2 = lum(bg); const ratio = (Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05);
    const size = parseFloat(cs.fontSize), bold = parseInt(cs.fontWeight) >= 700; const need = (size >= 24 || (size >= 18.66 && bold)) ? 3 : 4.5;
    if (ratio < need) out.contrast.push(e.tagName + '.' + (e.className||'') + ' "' + e.textContent.trim().slice(0,28) + '" ' + ratio.toFixed(2) + ' < ' + need); });
  document.querySelectorAll('img').forEach(i => { if (!i.hasAttribute('alt')) out.noAlt.push(i.src.slice(-40)); });
  out.brokenImages = [...document.querySelectorAll('img')].filter(i => i.complete && i.naturalWidth === 0).length;
  return out; }"""

with sync_playwright() as p:
    b = p.chromium.launch()
    for vp, (w, h) in VIEWPORTS.items():
        for theme in ("light", "dark"):
            ctx = b.new_context(viewport={"width": w, "height": h}, color_scheme=theme, has_touch=(vp == "phone"), is_mobile=(vp == "phone"), device_scale_factor=2 if vp == "phone" else 1)
            # Fail external requests fast (fonts/Wix images) so the run stays quick and deterministic.
            ctx.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file:") else route.abort())
            pg = ctx.new_page()
            errs = []
            pg.on("pageerror", lambda e: errs.append(str(e)))
            for f in sorted(glob.glob(os.path.join(SITE, "*.html"))):
                name = os.path.basename(f)[:-5]
                pg.goto("file://" + f, wait_until="domcontentloaded")
                # Smooth scrolling would interrupt the scripted scroll below and leave sections unrevealed.
                pg.add_style_tag(content="html{scroll-behavior:auto!important}")
                pg.wait_for_timeout(300)
                H = pg.evaluate("document.documentElement.scrollHeight"); y = 0
                while y < H:  # scroll like a user so reveal-on-scroll fires
                    pg.evaluate(f"scrollTo(0,{y})"); pg.wait_for_timeout(90); y += 400
                pg.evaluate("document.querySelectorAll('.reveal').forEach(e => e.classList.add('in'))")  # deterministic screenshots
                pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(700)
                pg.screenshot(path=os.path.join(OUT, f"{name}-{vp}-{theme}.png"), full_page=True)
                r = pg.evaluate(JS_CHECKS)
                flags = []
                if r["overflow"] > 0: flags.append(f"HORIZONTAL OVERFLOW {r['overflow']}px")
                if r["small"] and vp == "phone": flags.append("small tap targets: " + "; ".join(sorted(set(r["small"]))[:6]))
                if r["contrast"]: flags.append("low contrast: " + " | ".join(r["contrast"][:4]))
                if r["noAlt"]: flags.append(f"{len(r['noAlt'])} img without alt")
                if r["h1"] != 1: flags.append(f"{r['h1']} h1 elements")
                if errs: flags.append("JS errors: " + "; ".join(errs[:2]))
                print(f"[{vp}/{theme}] {name}: " + ("OK" if not flags else " || ".join(flags)) + (f"  (note: {r['brokenImages']} images not loaded, likely sandbox network)" if r["brokenImages"] else ""))
            ctx.close()
    b.close()
print("screenshots in", OUT)
