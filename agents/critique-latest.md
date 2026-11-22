# Critique, 2026-11-22 (HEAD ac975bf; tree clean apart from agents/shots)

Method: `python3 tools/check.py . agents/shots` finished with zero FAIL (only "images not loaded" sandbox notes; it takes about 6 minutes). I viewed index phone-light, index desktop-dark and aerobraking tablet-light, and grepped titles, canonical and og:image, robots.txt, sitemap, JSON-LD, Wix references and `STATUS` in build/build.py. Google Fonts and Wix are unreachable here, so screenshots show fallback faces and no photos (environment limit). No site files were edited. The last site change was before cycle 151; the site is visually identical to the previous critique.

## Sources consulted
WebFetch was blocked (permission not answered), so I saw only search listings. These are cited by title and prior knowledge, not quoted.
- https://developers.google.com/search/reference/robots_txt (robots.txt must sit at the host root to be honored)
- https://support.google.com/webmasters/answer/40361 (same, how to write and submit robots.txt)
- https://web.dev/articles/fetch-priority (image priority and LCP discovery)
- https://developer.chrome.com/docs/performance/insights/lcp-discovery (LCP request discovery)
- https://www.w3.org/WAI/WCAG22/Understanding/reflow and https://www.w3.org/WAI/WCAG22/Understanding/text-spacing (1.4.10, 1.4.12; the phone render shows no clipping or horizontal scroll, so no finding)
- Blocked and unread: developers.google.com/search/docs/crawling-indexing/robots/intro, w3.org consistent-help, web.dev/articles/optimize-lcp.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Copy is specific (three weeks struck to 15 minutes, 99 s, 46 orbits, 500 m tether). Residual: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Serif name, mono credential line, ledger sidebar, ruled list, one hard-offset button, flat dark theme. Weak spots seen: stamps only on rows 04 to 07 so the right column is ragged on desktop; the lone Fig. 1 plate sits above row 06 on phone like a stray; wide empty gutter between description and metadata on desktop.
- SEO: 7/10, unchanged. Unique titles on all 13 pages, canonical and og:image absolute, sitemap with 12 urls, robots.txt, JSON-LD present. Weak: one shared OG card, robots.txt under /website/ (ignored by Google, host limit), Wix images without dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1, 2, 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, ledger, 404 joke, orbit plate on the aerobraking page. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, double rules, hard shadow, flat dark theme). No drift.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).

## Ranked findings
1. Major (UX, credibility). The hero has no status or dates. "MS Mechanical Engineering, Carnegie Mellon University" reads as present tense; About says 2023 to 2025; the newest experience ended Aug 2024; today is 2026-11-22. A recruiter sees an unexplained gap and cannot tell availability. `STATUS = ""` (build/build.py line 266) is ready and renders a Status row. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads and its page is thin; START HERE sits on row 06 (aerobraking). Owner picks the lead and supplies the snake method and result.
3. Major (credibility). The aerobraking page describes Method in third person about Falcone et al. and then says "our NN state-space model" and "our method"; the reader cannot tell what Karthik did. "46 orbits" has no baseline. Raftar's "one-fifth the weight of a Ferrari" claim has no source. Owner sentence and source, or cut.
4. Major (robustness). The resume PDF is hotlinked from Wix in header, hero, About, footer and the 404. If Wix lapses it dies everywhere. Needs the owner's PDF at assets/resume.pdf.
5. Major (performance). Wix references remain on 11 pages (aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4, landing 2, others 1 each; counts include the resume link). No width/height means CLS risk and an outage dependency (web.dev optimize-cls, fetch-priority). Needs local image files. Also every one of these pages has an `alt=""` hit; confirm each is decorative, since a real photo with empty alt is invisible to search and screen readers (not verifiable offline).
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host when WOFF2 files are available.
7. Minor (visual). Ragged Home right column and lone Fig. 1 plate on phone. Caption it as the only drawn figure or drop it from Home.
8. Minor (content). Nine projects untiered on Home; same root as 2.
9. Minor (SEO). Shared OG card; robots path is a host limit (Google robots.txt spec). Noted, not pressed.
10. Minor (content). Tricycle page voice is passive with no subheads; owner call.
11. Minor (UX). Contact is LinkedIn only; footer states it. Owner constraint. The phone header drops Resume, LinkedIn and GitHub icons; they appear in the hero and footer, so acceptable.
12. Nit (visual, taste). About leaves the right third empty on wide screens; skills lists are 5/3/3.
13. Nit (process). Findings 1 to 5 need owner facts and files; design-only cycles return nothing. Recommend the owner supplies them or the loop pauses. Now the seventh or so consecutive cycle with no site change.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain ledger sidebar.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, zero tap-target and contrast failures.
- Filter buttons, numbered rows, press states, 404 joke, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page, the Fig. 1 orbit plate and result block on the aerobraking page.

## Verdict
The site is coherent, plain and clearly authored, with an AI-tell of 2 and a convincing retro matte commitment. What holds it back is not design but missing owner inputs: no status or dates line, an unresolved lead project, unsourced or ambiguously attributed claims, and a Wix dependency for the resume and images. Until the owner supplies those (plus resume.pdf, image files and fonts), further design-only cycles will return the same findings.
