# Critique, 2026-11-18 (cycle 157 checkout, HEAD 1051072; tree clean)

Method: `python3 tools/check.py . agents/shots` finished with zero FAIL (only "images not loaded" sandbox notes; runtime about 6 minutes). I viewed index phone-light and index desktop-light, and grepped titles, h1 counts, Wix references, robots.txt, sitemap, the font link and `STATUS` in build/build.py. Google Fonts and Wix are unreachable here, so screenshots show fallback faces and no photos. That is an environment limit. No site files were edited. The site is visually unchanged since the cycle 156 critique (last four cycles had no site changes).

## Sources consulted
WebFetch was not used; I only saw search listings, so these are cited by title and prior knowledge, not quoted.
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (2.5.8, 24px minimum; site uses 44px, fine)
- https://web.dev/articles/prefers-reduced-motion (reduced-motion handling; site has a reduced-motion path per earlier cycles)
- https://www.nngroup.com/videos/ux-portfolios-hiring/ (hiring managers scan for role, strongest work and contact; listing only)
- https://web.dev/articles/optimize-cls and https://web.dev/articles/font-best-practices (earlier cycles, still relevant)
No finding depends on an unread claim.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Copy is specific (three weeks struck to 15 minutes, 99 s, 46 orbits, 500 m tether). Residual: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Large serif name, mono credential line, ledger sidebar, ruled list, one hard-offset button, flat dark theme. Weak spots seen in the screenshots: stamps appear only on rows 04 to 07, so the right column is ragged on desktop; on phone the lone Fig. 1 plate sits above row 06 like a stray; desktop right column (number plus category) leaves a wide empty gutter between description and metadata.
- SEO: 7/10, unchanged. Unique titles on all 13 pages, exactly one h1 per page, sitemap with 12 urls, robots.txt, og:image present. Weak: one shared OG card, robots.txt sits under /website/ (Google ignores non-root robots.txt, host limit), Wix images without dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1, 2, 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, ledger, 404 joke. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, double rules, one hard shadow, flat dark theme). No drift.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).

## Ranked findings
1. Major (UX, credibility). The hero has no status or dates. "MS Mechanical Engineering, Carnegie Mellon University" reads as present tense; About says 2023 to 2025; the newest experience ended Aug 2024; today is 2026-11-18. A recruiter sees an unexplained gap and cannot tell availability. `STATUS = ""` (build/build.py line 266) is ready and renders a Status row in the ledger. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads and its page is thin; START HERE sits on row 06 (aerobraking). Owner picks the lead and supplies the snake method and result.
3. Major (credibility). The aerobraking page does not say what Karthik changed beyond cited prior work, and "46 orbits" has no baseline. Raftar's "one-fifth the weight of a Ferrari" claim has no source. Owner sentence and source, or cut.
4. Major (robustness). The resume PDF is hotlinked from Wix in header, hero, About, footer and the 404. If Wix lapses it dies everywhere. Needs the owner's PDF at assets/resume.pdf.
5. Major (performance). Wix references remain on 10 content pages (aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4, landing 2, others 1 each; counts include the resume link). No width/height means CLS risk (web.dev optimize-cls) and an outage dependency. Needs local image files.
6. Minor (performance, consistency). Fonts load from Google Fonts (index.html line 25) while the footer says "one stylesheet, no framework". web.dev font-best-practices favors self-hosting. Do it when WOFF2 files are available.
7. Minor (visual). Ragged Home right column and lone Fig. 1 plate on phone. Caption it as the only drawn figure or drop it from Home.
8. Minor (content). Nine projects untiered on Home; same root as 2.
9. Minor (SEO). Shared OG card; robots path is a host limit. Noted, not pressed.
10. Minor (content). Tricycle page voice is passive with no subheads; owner call.
11. Minor (UX). Contact is LinkedIn only; footer states it. Owner constraint.
12. Nit (visual, taste). About leaves the right third empty on wide screens; skills lists are 5/3/3.
13. Nit (process). Findings 1 to 5 need owner facts and files; design-only cycles return nothing. Recommend the owner supplies them or the loop pauses. This is now the fifth consecutive cycle with no site change.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain ledger sidebar.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, zero tap-target and contrast failures.
- Filter buttons, numbered rows, press states, 404 joke, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page.

## Verdict
The site is coherent, plain and clearly authored, with an AI-tell of 2 and a convincing retro matte commitment. What holds it back is not design but missing owner inputs: no status or dates line, an unresolved lead project, unsourced or unexplained claims, and a Wix dependency for the resume and images. Until the owner supplies those (and the resume.pdf, image files and fonts), further design-only cycles will return the same findings.
