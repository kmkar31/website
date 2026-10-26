# Critique, 2026-10-26 (cycle 21, reviewing main at b487ffb "Cycle 20")

## Sources
No page was fetched this cycle (WebFetch not used; the previous cycle's fetches were refused). The links are pointers only, no finding depends on them.
- WCAG 2.2 SC 2.4.4 Link Purpose / 4.1.2 Name, Role, Value: https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html (not read)
- web.dev, Optimize web fonts / font-display: https://web.dev/articles/optimize-webfont-loading (not read)
- web.dev, Optimize CLS: https://web.dev/articles/optimize-cls (not read)
- NN/g, portfolios for hiring managers: https://www.nngroup.com/articles/portfolios/ (not read)
Topic this cycle: regression check of cycle 20, fonts, robustness. Findings below are measured in the repo or with Playwright.

Measured: tools/check.py on 13 pages x 3 viewports x 2 themes, every line OK (Wix images not loading is a sandbox limit). Screenshots viewed: home phone (light) and home desktop (light). The desktop shot in agents/shots was stale in my first read (it showed no Fig. 1 plate); a fresh Playwright shot at 1366 wide shows the plate, so no regression there. Live site not checked. STATUS in build/build.py is still "" (line 257), so no status line on home or About.

## Scores
- AI-tell: 3/10 (unchanged). Authored: struck-through "three weeks" in marker, "For the record" ledger, stamps, Fig. plate, plain lede, colophon "no framework". Residual: cream + serif + terracotta editorial kit; rows 02-09 share one anatomy. No gradients, blur, glow, badges, slogans. Tells moved since last cycle: none (cycle 20 was non-visual).
- Looks good: 6/10. Calm, aligned, rules are crisp, the phone first screen is good. But the only image on home is a six-dot zigzag, no photograph renders anywhere, and the desktop home is a long text list with a lot of empty cream to the right of each blurb.
- SEO: 7/10. Unique title, description, canonical, OG/Twitter with local og.png, JSON-LD, sitemap, robots, noindex 404, one h1. Weak: render-blocking Google Fonts CSS, hotlinked project images with no width/height (0 of about 40 img tags carry them), thin Snake page.
- UX: 6/10. Name, field, resume, LinkedIn in the first phone screen; 44 px targets; keyboard order now clean. Misses: no "now" statement, resume is a third-party URL, the featured project has no result.
- Fun: 6/10. Earned touches (holdable 99 s stamp, struck weeks, colophon, 404) live on home and Hasselhoff only; seven of nine project pages have none.

## Owner critique (user-critique.md)
1. Retro, matte: met. Paper tones, ink borders, hard-shadow button, no blur or gradient.
2. Not AI-looking: mostly met. Remaining risk is uniform rows 02-09 and the stock editorial palette; taste, not a defect.

## Findings (ranked)

1. Major (content/UX, carried). Snake robots is "Start here" but its page has little beyond lab, advisor, a schematic and one generic paragraph. Owner must give 2-3 facts (gaits, terrain, result) or pick Aerobraking (46 orbits, a real result) as Start here. Flagged, not dictated.

2. Major (credibility, carried). No "now" statement. Today is 26 Oct 2026; About says CMU "2023 - 2025" and home is present tense. A reader cannot tell if he has graduated, is enrolled or is open to roles. One owner sentence into STATUS is the highest-value change available.

3. Major (robustness). Resume PDF, the main call to action, is a Wix filesusr hotlink in header, hero and footer on every page. Owner should supply assets/resume.pdf. Not verifiable offline.

4. Major (looks good, 6). No photograph or result image loads anywhere; a robotics portfolio shows no robot. Owner media with true dimensions is the only fix. Until then, every figure is a hotlink dependency (about 40 img tags).

5. Major (performance/SEO). Google Fonts stylesheet is render-blocking and third party (index.html line 25), no metric-matched fallback. check.py blocks it, so my screenshots render in a Times-like fallback and the colophon names fonts a visitor may not see. Self-host two WOFF2 with font-display: swap and preload. Needs font files; designer can at least add a size-adjusted local fallback in the font stack.

6. Minor (AI-tell, taste). Home rows 02-09 share one anatomy (title, blurb, number, tag). Rows 04-06 already carry stamps; rows 02, 03, 07, 08, 09 do not. One real fact per row from text already in the repo (500 m tether for 07, four unknown constants for 08, four-bar pedal path for 09) as a stamp would break the uniformity. Reopened only because it is the largest remaining sameness.

7. Minor (SEO/CLS). Hotlinked project-page imgs lack width/height, so late figures shift layout. Needs real dimensions from the owner files.

8. Minor (looks good, desktop). The Fig. 1 caption "Fig. 1 . Snake robot, schematic" wraps to two lines inside the 176 px plate at 1366 wide, which looks cramped next to the single-line title. Widen the plate to about 200 px or shorten to "Fig. 1 . Snake robot".

9. Minor (layout). Desktop home: blurbs cap at 46em and the tag column sits at 240 px, leaving a wide gutter in the middle of every row. Acceptable, but the eye travels far from title to number. Taste.

10. Minor (layout, About desktop). Right 28% is empty for long stretches when the portrait hotlink fails. A date margin column would use it. Taste, large rewrite.

11. Minor (UX). Sysid desktop: Background (about 20 lines) sits between the work and the pager; could be collapsed like Hasselhoff's detail. Taste.

12. Minor (UX, phone length). Home is about 6150 px on phone. Designer documents "full index by design"; accepted, only noted.

13. Minor (contact). Contact is LinkedIn only (owner constraint); the footer sentence is the only contact line.

14. Nit (fun). One plain aside per project page from facts in the repo (46 orbits, 500 m, 99 s) would spread personality to the seven bare pages. Declined as taste before; fine unless owner asks.

15. Nit (verify). Cycle 20 hides `a.zoom` until image load; I did not re-run a real Tab pass this cycle. Check it once on a page where Wix images succeed (live) to confirm the zoom links become focusable again after load.

## Good, do not regress
- Struck-through "three weeks" in amber marker (home, About), now linking to About#seagate.
- Fig. N plate with sheet tag and honest "schematic" caption; repo-local og.png carries it.
- Stamps and the 99 s stamp, now a real button inside the dd.
- Hasselhoff disclosure bar; pager without wraparound; Aerobraking h2s; Projects h2.
- Row links named by title; skip link first; 44 px targets; 3 px focus ring; no empty tab stops with images blocked.
- Plain specific lede, "For the record" ledger, ink-rule hierarchy, solid ink footer, dark theme contrast.
- Canonical, JSON-LD, sitemap, noindex 404, no framework, no gradient, no blur.

## Verdict
The site is coherent, matte and fairly authored (AI-tell 3), and cycle 20 introduced no visible regression; check.py is clean on all 78 combinations. What holds the four axes at 6 is almost entirely owner-only content: a status sentence, Snake facts or a different Start here, a local resume.pdf, photographs with dimensions and WOFF2 files. Designer-only work left is small: add stamps with real facts to the five bare rows (6), fix the wrapping Fig. 1 caption (8), add a size-adjusted fallback font, and consider one aside on the bare project pages (14). Without the owner's input, further cycles will keep returning to the same five items.
