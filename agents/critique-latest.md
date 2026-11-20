# Critique, 2026-11-20 (HEAD 0fbb40d; no site files edited)

Method: `python3 tools/check.py . agents/shots` ran to completion (rc=0, zero FAIL; only "images not loaded" sandbox notes; it takes about 3 minutes). I viewed index phone-light and index desktop-light. Cycle 169 changed no site files, so there is no regression. Wix and Google Fonts are unreachable in the sandbox (environment limit, not a design bug).

## Sources consulted
Research was limited this cycle. WebFetch for the three pages below was blocked (permission request unanswered), so I read none of them. They are pointers only, and no finding rests on their text. The same applies to the earlier-cycle links in LOG.md.
- https://web.dev/articles/optimize-cls (blocked; image dimensions and CLS, finding 5)
- https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html (blocked; focus visibility, topic for next cycle)
- https://developers.google.com/search/docs/crawling-indexing/robots/intro (blocked; robots.txt must sit at the host root, finding 8)
Topic this cycle: CLS/image dimensions, focus appearance, robots location. Not verified against the sources; flagged as such.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Copy is specific (three weeks struck through to 15 minutes, 99 s, 46 orbits, 500 m). Residual tell: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. In the screenshots: serif name, mono credential line, ledger sidebar, ruled list, one hard-offset button, flat dark footer. Weak spots: stamps appear only on rows 04 to 07, so the desktop right column is ragged (rows 01 to 03, 08, 09 have an empty gap); the Fig. 1 plate on row 06 sits alone on phone; the footer is a heavy dark band.
- SEO: 7/10, unchanged. Unique titles, one h1, sitemap, canonical, JSON-LD, local og:image. Weak: one shared OG card; robots.txt under a subpath (host limit); Wix images lack dimensions. Not verifiable offline: live search and social previews.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 3).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, "For the record" ledger, 404 joke, pressable 99 s stamp. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Paper tones, ink borders, hard shadow, flat dark footer and theme.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).
No new owner notes.

## Ranked findings
1. Major (UX, credibility). No status or date line. The hero reads "MS Mechanical Engineering, Carnegie Mellon University" with no tense; About gives 2023 to 2025. Today is 2026-11-20, so the degree appears to have ended. A recruiter cannot tell if he has graduated, what he does now or whether he is available. `STATUS` in build/build.py renders nothing. The owner must supply the fact.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads and matches the hero sentence, but has no stamp and no stated method, result or personal contribution. "START HERE" sits on row 06 (aerobraking) with no reason. The owner should pick the lead and supply the snake method and result, or move the label.
3. Major (credibility). The aerobraking page never says what Karthik changed beyond cited prior work, and "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. Owner: one sentence of contribution and a source, or cut the claim.
4. Major (robustness). The resume PDF is hotlinked from Wix in the header, hero, footer and 404. It is the main call to action, so a Wix lapse breaks it on every page. Needs a local resume.pdf from the owner.
5. Major (performance). Wix images on content pages (1 to 10 per page per check.py) have no width/height, which risks CLS and an outage dependency. Need local files, then dimensions and `fetchpriority="high"` on the first visible image. (Principle unverified this cycle; see sources.)
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 when files exist and add a metric-adjusted fallback.
7. Minor (visual). Ragged Home right column; the lone Fig. 1 plate looks stray on phone. Root cause is finding 2.
8. Minor (SEO). All pages share one OG card; robots.txt path is a host limit. Noted, not pressed.
9. Minor (content). The tricycle page voice is passive. Owner's call.
10. Minor (UX). Contact is LinkedIn only; the footer says so. Owner constraint.
11. Nit (visual, taste). About right third is empty on wide screens; skills lists are 5/3/3.
12. Nit (process). Findings 1 to 5 need owner facts and files. About 25 cycles in a row have produced no site change. The owner should supply them, or the loop should pause.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark footer and theme.
- Specific copy and the plain "For the record" ledger.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, no tap-target or contrast failures.
- Numbered rows, stamps, filters, press states, 404 joke, Previous/Next with a fact, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page, Fig. 1 schematics with honest captions, the struck-through "three weeks".

## Verdict
The site is coherent, plain and clearly authored. AI-tell is 2 and the retro matte commitment holds. What holds it back is missing owner input: a status and dates line, a decided lead project with a real page behind it, sourced or explained claims, and local copies of the resume, images and fonts. I have no new designer-side item this cycle. Research this cycle was blocked, so no finding rests on a source I read.
