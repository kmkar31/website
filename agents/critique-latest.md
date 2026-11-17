# Critique, 2026-11-17 (cycle 156 checkout, HEAD 3fce027; tree clean)

Method: `python3 tools/check.py . agents/shots` ran rc=0, zero FAIL (only "images not loaded" sandbox notes; it takes about 5 minutes). I viewed index phone-light and index desktop-dark, and grepped titles, og tags, robots.txt, sitemap, the font link and Wix reference counts. Google Fonts and Wix are unreachable here, so screenshots show fallback faces and no photos; that is an environment limit. No site files edited.

## Sources consulted
Only search listings were available this cycle (WebFetch not used), so I rely on titles and prior reading, not full-page quotes.
- https://web.dev/articles/optimize-cls (set width/height on images to reserve space)
- https://web.dev/articles/font-best-practices (self-host fonts, preload, font-display)
- https://web.dev/learn/images/performance-issues (image weight and layout shift)
- https://www.nngroup.com/articles/ux-design-portfolios/ (what hiring managers scan for; listing only)
- https://developers.google.com/search/reference/robots_txt (robots.txt valid only at host root; earlier cycle)
No finding depends on an unread claim.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Copy is specific (three weeks struck to 15 minutes, 99 s, 46 orbits, 500 m tether). Residual: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Large serif name, mono credential line, ledger sidebar, ruled list, one hard-offset button, coherent flat dark theme. Weak spots: stamps appear only on rows 04 to 07 so the right column is ragged; on phone the lone Fig. 1 plate sits above the row 06 title like a stray.
- SEO: 7/10, unchanged. Unique titles on all 13 pages, sitemap with 12 urls, robots.txt, og:image (1200x630, alt) present. Weak: one shared OG card, robots.txt under /website/ (ignored by Google), undimensioned Wix images.
- UX: 6/10, unchanged. Below 7, so Major (findings 1, 2, 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, ledger, 404 joke. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, double rules, one hard shadow, flat dark theme). No drift.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).

## Ranked findings
1. Major (UX, credibility). Hero has no status or dates. "MS Mechanical Engineering, Carnegie Mellon University" reads as present tense, About says 2023 to 2025, newest experience ends Aug 2024; today is 2026-11-17. A recruiter sees an unexplained gap and cannot tell availability. `STATUS = ""` in build/build.py is ready. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads and its page is thin; START HERE sits on row 06 (aerobraking). Owner picks the lead and supplies the snake method and result.
3. Major (credibility). Aerobraking page does not say what Karthik changed beyond the cited prior work; "46 orbits" has no baseline. Raftar's "one-fifth the weight of a Ferrari" claim has no source. Owner sentence and source, or cut.
4. Major (robustness). Resume PDF is hotlinked from Wix in header, hero, About, footer and the 404. If Wix lapses it dies everywhere. Needs the owner's PDF at assets/resume.pdf.
5. Major (performance). Wix references remain on every content page (counts: aerobraking 9, sysid 7, tricycle 6, hasselhoff 6, tethered 6, landing 4, about 4, others 2 to 3; these include the resume link). No width/height means CLS risk (web.dev optimize-cls) and an outage dependency. Needs local image files.
6. Minor (performance, consistency). Fonts load from Google Fonts (index.html line 25) while the footer says "one stylesheet, no framework". web.dev font-best-practices favors self-hosting. Do it when files are available.
7. Minor (visual). Ragged Home right column and lone Fig. 1 plate on phone; caption it as the only drawn figure or drop it on Home.
8. Minor (content). Nine projects untiered on Home; same root as 2.
9. Minor (SEO). Shared OG card; robots path is a host limit. Noted, not pressed.
10. Minor (content). Tricycle page voice is passive with no subheads; owner call.
11. Minor (UX). Contact is LinkedIn only; footer states it. Owner constraint.
12. Nit (visual, taste). About leaves the right third empty on wide screens; skills lists are 5/3/3.
13. Nit (process). Findings 1 to 5 need owner facts and files; design-only cycles return nothing. Recommend the owner supplies them or the loop pauses.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain ledger sidebar.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, zero tap-target and contrast failures.
- Filter buttons, numbered rows, press states, 404 joke, per-page JSON-LD, canonical and OG, reduced-motion block, focus ring.
- Drawn figure plates instead of stock imagery; pager with a neighbour fact.

## Verdict
The site is authored-looking, coherent with the retro matte brief, and clean on automated checks, so design work is saturated. What holds it back is not craft but missing owner inputs: an availability line, one agreed lead project with a real snake result, a stated personal contribution on aerobraking, a sourced Ferrari claim, and local copies of the resume and images. Until those arrive, further design cycles will keep returning nothing; the next real gain is the owner's content.
