# Critique, 2026-10-25 (cycle 20, reviewing main at a1f139b)

## Sources
WebFetch was refused by the permission layer again (no answer in time), so no page below was read. They are pointers only; no finding depends on them.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (blocked)
- web.dev, Optimize CLS (image width and height): https://web.dev/articles/optimize-cls (blocked)
- NN/g, portfolios and hiring managers: https://www.nngroup.com/articles/portfolios/ (blocked)
Topic this cycle: keyboard order and focus, robustness when hotlinked media fails. Findings 1, 2, 3, 7 are measured in the repo or by Playwright; none rests on a source.

Measured: tools/check.py, 13 pages x 3 viewports x 2 themes, all OK (Wix images not loading is a sandbox limit). Real keyboard pass (Playwright Tab x30, 1280 wide) on index and Hasselhoff, done this cycle for the first time. Screenshots viewed: home desktop and phone (light), About tablet (light), quadrotor-sysid desktop (dark). Live site not checked. STATUS in build/build.py presumably still empty (home and About show no status line).

## Scores
- AI-tell: 3/10 (unchanged). Authored: struck-through "three weeks" in marker, ruled "For the record" ledger, stamps, Fig./Sheet plates, "no framework" colophon, plain lede. Residual: cream + serif + terracotta editorial kit, and rows 02-09 identical in anatomy. No gradients, blur, glow, badges or slogans. Tells moved: none (cycle 19 was structure only).
- Looks good: 6/10. Calm, aligned, clean rules, good dark theme (sysid dark reads well, graph-paper plate is the best thing on the page). But the only picture on home is a six-dot zigzag, and no photograph renders anywhere. Sysid is a long text column with one plate.
- SEO: 7/10. Unique title and description, canonical, OG and Twitter with absolute local 1200x630 image, JSON-LD, sitemap, robots, noindex 404, one h1 per page. Weak: render-blocking Google Fonts CSS, hotlinked figures without width/height (0 of the project-page imgs checked carry them), thin text on Snake.
- UX: 6/10. Name, field, resume and LinkedIn all land in the first phone screen; targets are 44 px; focus ring is 3 px solid on every stop. Misses: no "now" statement, resume is a third-party URL, featured project has no result, empty tab stops (finding 3).
- Fun: 6/10. Earned touches exist (holdable 99 s stamp, struck weeks, 404, colophon), but seven of nine project pages have none and the touches sit only on home and Hasselhoff.

## Owner critique (user-critique.md)
1. Retro, matte: met. Paper tones, ink rules, one hard-shadow button, no blur or gradient. Dark theme is near-black with amber, not inverted paper; taste, contrast fine.
2. Not AI-looking: mostly met. Remaining risk is the editorial kit and uniform rows (finding 6); taste, not a defect.

## Findings (ranked)

1. Major (content/UX). Snake robots is still "Start here" on home and in the lede, and its page still has only Lab, Advisor, a schematic zigzag and one generic paragraph (carried from cycle 19, still unresolved). Owner must supply 2 or 3 facts (gaits, terrain, result), or choose Aerobraking (46 orbits is a real result) as Start here. Flagged, not dictated.

2. Major (credibility). No "now" statement; dates are stale. Today is 25 Oct 2026; About says the Master's is "at Carnegie Mellon University (2023 - 2025)" and home is present tense. A reader cannot tell graduated, enrolled or open to roles. One owner sentence is the highest-value change available.

3. Major (a11y, new, measured). Keyboard pass on Hasselhoff: three Tab stops land on links with no accessible name, sized 350x44, 350x44 and 720x44, between the 99 s stamp and the "Design and state machine" summary. These are the `a.zoom` wrappers around Wix images that failed to load (the img is hidden or collapsed, the anchor stays focusable and keeps its 44 px min-height). A keyboard or screen-reader user hits empty links; WCAG 2.4.4 / 4.1.2. This also happens for real visitors if Wix drops an image. Fix: in the existing failed-image JS, also set `hidden` (or remove) the parent `a.zoom`, or give the anchor `aria-hidden="true" tabindex="-1"` and display:none when its img has failed. Verify by repeating the Tab pass with Wix blocked.

4. Major (robustness). The resume PDF, the main call to action, is a Wix filesusr hotlink in header, hero and footer on every page. Owner should add assets/resume.pdf. Not verifiable offline.

5. Major (looks good, 6). No photograph or result image loads anywhere; a robotics portfolio shows no robot. Plates are honest and well drawn but they are schematics. Owner media with true width and height is the only fix.

6. Minor (AI-tell, taste). Home rows 02-09 share one anatomy (title, two-line blurb, number, tag) under a featured row 01 that has a small plate. A one-line fact per row (46 orbits, 500 m, 99 s) would break the uniformity using data already in the repo; stamps already do this on three rows. Reopened only because the same shape is visible in the home screenshot at phone and desktop.

7. Major (performance/SEO). Google Fonts CSS is render-blocking and third party, with no metric-matched fallback; check.py blocks it so screenshots show Times, and the colophon then names fonts the visitor may not see. Self-host two WOFF2 with font-display: swap and preload. Needs font files.

8. Minor (UX, phone length). Home on phone is about 6150 px. Designer documents "home is the full index by design"; accepted. A 30-second reader sees rows 01-03 on first scroll.

9. Minor (SEO/CLS). Hotlinked project-page `<img>` tags have no width/height (e.g. Hasselhoff lines 56-66), so late figures shift layout. Only the Projects thumbnails have dimensions. Needs owner files to measure.

10. Minor (layout). About desktop: the right 28% is empty below the intro for a long stretch when the portrait fails (it is a Wix hotlink). Dates in a margin column would use it. Taste, large rewrite.

11. Minor (UX). Sysid desktop: after the plate the page is three plain text blocks; "Background" (about 20 lines) sits between the work and the pager. Acceptable now that h2s exist; could be collapsed like Hasselhoff's detail. Taste.

12. Minor (contact). Contact is LinkedIn only (owner constraint); the footer sentence is the only contact line. Flag only.

13. Nit (fun). One plain aside per page from facts in the repo (46 orbits, 12 km/h, 500 m). Declined as taste in earlier cycles; fine unless the owner asks.

14. Nit (a11y). Hasselhoff "99 SECONDS" stamp is a `dd` carrying role=button/tabindex: it receives focus with the 3 px ring (verified), but a role=button on a `dd` inside a definition list breaks list semantics. Consider moving the interactive part to an inner `<button>`.

15. Nit (a11y). "three weeks to 15 minutes" in the home lede is a Tab stop (206x21, below the 24 px minimum of SC 2.5.8 only if it were a lone target; inline text links are exempt). Confirm it links somewhere useful (#seagate) and that its destination is announced; low priority.

## Good, do not regress
- Struck-through "three weeks" in amber marker (home, About).
- Fig. N plates with sheet tags and honest "schematic / NTS" captions; repo-local.
- Two stamp types and the holdable 99 s stamp; hard-shadow button.
- Hasselhoff disclosure bar (boxed +, Show, native details).
- Pager without wraparound; Aerobraking h2s; Projects h2 (cycle 19, verified in order).
- Keyboard: skip link first, 44 px targets, 3 px focus ring on every stop, logical order, no traps.
- Plain specific lede, "For the record" ledger, ink-rule hierarchy, dark theme contrast, solid ink footer.
- Local og.png, JSON-LD, canonical, sitemap, noindex 404, no framework, no gradient, no blur.

## Verdict
The design is coherent, matte and fairly authored (AI-tell 3) and cycle 19 introduced no visual regression. The one new defect is real and cheap: failed hotlinked images leave empty, focusable zoom links (finding 3), which hurts exactly the visitors the fallback was meant to help. Everything holding looks, UX and fun at 6 is content only the owner can give: a status sentence, facts for the Snake page (or a different Start here), a local resume.pdf, photographs and WOFF2 files. Designer-only work now: fix the empty links (3), optionally move the 99 s button semantics (14), and consider one fact per home row (6).
