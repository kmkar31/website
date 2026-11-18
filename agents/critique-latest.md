# Critique, 2026-11-18 (cycle 158 checkout, HEAD ac975bf; tree clean)

Method: `python3 tools/check.py . agents/shots` finished with zero FAIL (only "images not loaded" sandbox notes). I viewed index phone-light, index desktop light and dark, and snake-robots phone-light. I grepped `STATUS` (build/build.py line 266, still `""`), Wix references per page (404 0, index 0, about 1, aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4, landing 2, argus/projects/raftar/snake 1 each), the font link (index.html line 25) and og/twitter tags. Google Fonts and Wix are unreachable here, so screenshots show fallback serif/mono faces and no photos (environment limit). No site files were edited. The site is unchanged since the cycle 157 critique (sixth cycle with no site change).

## Sources consulted
WebFetch of web.dev, w3.org and developers.google.com was blocked by the permission layer (PROVENANCE_REQUIRED), so none of these were read. WebSearch returned listings only. Citations below are pointers from titles and prior knowledge, not quotes; no finding depends on them.
- https://web.dev/articles/fetch-priority (search listing only; relevant once real hero images exist)
- https://web.dev/articles/optimize-cls (Wix images without width/height; blocked, unread)
- https://web.dev/articles/font-best-practices (self-hosting fonts; unread)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (2.5.8; site uses 44px)
- https://developers.google.com/search/docs/crawling-indexing/robots/intro (robots.txt must be at host root; fetch blocked, unread)
Topic varied this cycle: LCP and fetch priority, robots.txt placement.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip, card trio or sparkle. Copy is specific (three weeks struck to 15 minutes, 99 s, 46 orbits, 500 m tether). Residual: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Large serif name, mono credential line, ledger sidebar, ruled list, single hard-offset button, flat dark theme that keeps the same structure. Seen in the screenshots: stamps only on rows 04 to 07, so the desktop right column is ragged; on phone the lone Fig. 1 plate sits above row 06 like a stray; on desktop there is a wide empty gutter between description and the number/category column; rows 01 to 03, 08, 09 look "unfinished" next to stamped rows.
- SEO: 7/10, unchanged. Unique titles, one h1 per page, sitemap, robots.txt, canonical and og:image 1200x630 with alt, twitter card. Weak: one shared OG card for all pages, robots.txt under /website/ (ignored by crawlers, host limit), Wix images without dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1, 2, 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, ledger, "Sheet 1 of 9 / NTS" caption, 404 joke. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, double rules, one hard shadow, flat dark theme). No drift.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).

## Ranked findings
1. Major (UX, credibility). The hero has no status or dates. "MS Mechanical Engineering, Carnegie Mellon University" reads as present tense, About says 2023 to 2025, and today is 2026-11-18. A recruiter sees an unexplained gap and cannot tell availability. `STATUS = ""` is wired to render a Status row in the ledger. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads, yet its page (phone screenshot) is thin: a question, a schematic marked "illustrative", one paragraph "Why snake robots" and a link out to the lab page. No method, result or personal contribution. START HERE sits on row 06 (aerobraking). Owner picks the lead and supplies the snake method and result.
3. Major (credibility). The aerobraking page does not say what Karthik changed beyond cited prior work, and "46 orbits" has no baseline. Raftar's "one-fifth the weight of a Ferrari" claim has no source. Owner sentence and source, or cut.
4. Major (robustness). The resume PDF is hotlinked from Wix in header, hero, About, footer and 404. If Wix lapses it dies on every page. Needs the owner's PDF at assets/resume.pdf.
5. Major (performance). Wix images remain on 10 content pages (counts above include the resume link). No width/height means CLS risk and an outage dependency. Needs local image files; once local, give the first visible image fetchpriority="high" and dimensions.
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer claims "one stylesheet, no framework" and the sandbox shows the fallback faces, so the retro type is not guaranteed to render. Self-host WOFF2 with font-display and a size-matched fallback when files exist.
7. Minor (visual). Ragged Home right column and the lone Fig. 1 plate on phone. Either caption it "the only project with a drawn figure" or drop it from Home.
8. Minor (content). Nine projects untiered on Home; same root as 2.
9. Minor (SEO). Shared OG card; robots.txt path is a host limit. Noted, not pressed.
10. Minor (content). Tricycle page voice is passive with no subheads; owner call.
11. Minor (UX). Contact is LinkedIn only; footer states it. Owner constraint.
12. Nit (visual, taste). About leaves the right third empty on wide screens; skills lists are 5/3/3.
13. Nit (process). Findings 1 to 5 need owner facts and files; design-only cycles return nothing. Sixth consecutive cycle with no site change. Recommend the owner supplies them or the loop pauses.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme that mirrors the light layout.
- Specific copy and the plain ledger sidebar.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, zero tap-target and contrast failures.
- Filter buttons, numbered rows, press states, 404 joke, "Sheet 1 of 9 / NTS" captions, Next link at the end of project pages, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page.

## Verdict
The site is coherent, plain and clearly authored, with an AI-tell of 2 and a convincing retro matte commitment. What holds it back is not design but missing owner inputs: no status or dates line, an unresolved lead project with a thin page behind it, unsourced or unexplained claims, and a Wix dependency for the resume and images. Until the owner supplies those (plus resume.pdf, image files and fonts), further design-only cycles will return the same findings. My research this cycle was limited because the fetch tool was blocked.
