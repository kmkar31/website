# Critique, 2026-11-18 (HEAD deab3e7; tree clean; no site files edited)

Method: `python3 tools/check.py . agents/shots` ran with zero FAIL (only "images not loaded" sandbox notes). I viewed index phone-light, index desktop-dark, about tablet-light and aerobraking-drl phone-light. I also grepped build/build.py (`STATUS = ""` at line 266), Wix/filesusr references per page, the Google Fonts link (index.html line 25) and the Ferrari claim (raftar-formula-racing.html line 48). Wix and Google Fonts are unreachable here, so screenshots show fallback faces and no photos (environment limit, not a bug). The site is unchanged since the cycle 157 critique: seventh consecutive cycle with no site change.

## Sources consulted
Fetching web.dev was blocked again (PROVENANCE_REQUIRED, permission not answered). Search returned listings only. Nothing below is quoted; citations are pointers and no finding depends on them.
- https://web.dev/articles/optimize-cls (fetch blocked; image width/height and CLS)
- https://www.nngroup.com/videos/ux-portfolios-hiring/ (search listing only; what hiring managers scan for)
- https://measuringu.com/what-hiring-managers-want-and-what-ux-practitioners-do/ (search listing only)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (2.5.8; site uses 44px)
Topic this cycle: hiring-manager portfolio scanning and CLS from unsized images.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip, card trio or sparkle. Copy is specific (three weeks struck through to 15 minutes, 99 s, 46 orbits, 500 m tether). Residual: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. In the screenshots: large serif name, mono credential line, ledger sidebar, ruled list, one hard-offset button, flat dark theme that mirrors the light layout. Weak spots: stamps on rows 04 to 07 only, so the desktop right column is ragged and rows 01 to 03, 08, 09 look bare beside them. On phone the lone Fig. 1 plate sits above row 06 like a stray. On the About tablet view the right third is empty. Aerobraking on phone is one long unbroken text column.
- SEO: 7/10, unchanged. Unique titles, one h1, sitemap, canonical, JSON-LD, og:image with dimensions. Weak: one shared OG card, robots.txt under /website/ is ignored by crawlers (host limit), Wix images without dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1, 2, 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, ledger, "Sheet N of 9 / NTS" captions, 404 joke. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, double rules, one hard shadow, flat dark theme). No drift.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).

## Ranked findings
1. Major (UX, credibility). No status or dates. Hero says "MS Mechanical Engineering, Carnegie Mellon University" in present tense, About says 2023 to 2025, and today is 2026-11-18. A recruiter sees an unexplained gap and cannot tell availability. `STATUS` is wired to render a ledger row; the owner must supply the fact.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads and matches the lede, yet its page has no method, result or personal contribution. START HERE sits on row 06 (aerobraking), which is the substantive page. Owner picks the lead and supplies the snake method and result.
3. Major (credibility). The aerobraking page does not say what Karthik changed beyond the cited Falcone et al. work, and "46 orbits" has no baseline. Raftar's "one-fifth the weight of a Ferrari" has no source on the page. Owner sentence and source, or cut.
4. Major (robustness). The resume PDF is hotlinked from Wix in the header, hero, About, footer and 404. If Wix lapses it breaks on every page. Needs the owner's PDF at assets/resume.pdf.
5. Major (performance). Wix images remain on 10 content pages. No width/height means CLS risk and an outage dependency. Needs local files; then dimensions and fetchpriority="high" on the first visible image.
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Retro type is not guaranteed to render on a blocked network. Self-host WOFF2 with font-display when files exist.
7. Minor (visual). Ragged Home right column and the lone Fig. 1 plate on phone. Caption it as the only drawn figure or drop it from Home.
8. Minor (content). Nine projects untiered on Home; same root as 2.
9. Minor (SEO). Shared OG card; robots.txt path is a host limit. Noted, not pressed.
10. Minor (content). Tricycle page voice is passive with no subheads; owner call.
11. Minor (UX). Contact is LinkedIn only; footer states it. Owner constraint.
12. Nit (visual, taste). About right third empty on wide screens; skills lists are 5/3/3.
13. Nit (process). Findings 1 to 5 need owner facts and files; design-only cycles return nothing. Recommend the owner supplies them or the loop pauses.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain ledger sidebar.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, no tap-target or contrast failures.
- Numbered rows, stamps, filters, press states, 404 joke, "Sheet N of 9" captions, Previous/Next with a fact on project pages, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page.

## Verdict
The site is coherent, plain and clearly authored, with AI-tell 2 and a convincing retro matte commitment. What holds it back is missing owner input: a status and dates line, a decided lead project with a substantive page behind it, sourced or explained claims, and local copies of the resume, images and fonts. Until those arrive, design-only cycles will return the same findings. My research was again limited by blocked fetches.
