# Critique, 2026-11-20 (HEAD 93ffb0c; no site files edited)

Method: `python3 tools/check.py . agents/shots` ran to completion (rc=0, zero FAIL; only "images not loaded" sandbox notes). I viewed index phone-light, index desktop-dark and snake-robots phone-light. Wix and Google Fonts are unreachable in the sandbox (environment limit, not a design bug).

## Sources consulted
WebFetch was blocked again this cycle (permission request unanswered), so I read no external page. No finding rests on a source text. Pointers only, unverified:
- https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html (blocked)
- https://web.dev/articles/optimize-cls (blocked; finding 5)
- https://developers.google.com/search/docs/crawling-indexing/robots/intro (blocked; finding 8)
The research requirement of three sources per cycle was therefore not met. This is an environment limit.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Specific copy (three weeks struck through to 15 minutes, 99 s, 46 orbits, 500 m). Residual tell: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Serif name, mono credential line, ruled list, hard-offset button, flat dark footer. Weak: stamps only on rows 04 to 07 so the desktop right column is ragged; Fig. 1 plate on row 06 sits alone on phone; snake page (the lead project) is visibly thin.
- SEO: 7/10, unchanged. Unique titles, one h1, sitemap, canonical, JSON-LD, local og:image. Weak: one shared OG card; robots.txt under a subpath (host limit); Wix images lack dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 3).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, "For the record" ledger, 404 joke, 99 s stamp. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, hard shadow, flat footer).
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).
No new owner notes.

## Ranked findings
1. Major (UX, credibility). No status or date line. Hero says "MS Mechanical Engineering, Carnegie Mellon University" with no tense; About gives 2023 to 2025. Today is 2026-11-20, so the degree appears over. A recruiter cannot tell if he has graduated, what he does now or whether he is available. `STATUS` in build/build.py renders nothing. Owner must supply the fact.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads and matches the hero sentence, but in the phone screenshot its page is short: the question, lab and advisor, one schematic, one paragraph "Why snake robots", a lab link. No method, result or personal contribution. "START HERE" sits on row 06 (aerobraking) with no reason given. Owner should pick the lead and supply the snake method and result, or move the label.
3. Major (credibility). Aerobraking page never says what Karthik changed beyond cited prior work, and "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. Owner: one sentence of contribution and a source, or cut the claim.
4. Major (robustness). Resume PDF is hotlinked from Wix in header, hero, footer and 404. It is the main call to action. Needs a local resume.pdf from the owner.
5. Major (performance). Wix images on content pages (1 to 10 per page per check.py) have no width/height, risking CLS and an outage dependency. Need local files, then dimensions and `fetchpriority="high"` on the first visible image. (Principle unverified this cycle.)
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 when files exist, with a metric-adjusted fallback.
7. Minor (visual). Ragged Home right column; lone Fig. 1 plate looks stray on phone. Root cause is finding 2.
8. Minor (SEO). All pages share one OG card; robots.txt path is a host limit. Noted, not pressed.
9. Minor (content). Tricycle page voice is passive. Owner's call.
10. Minor (UX). Contact is LinkedIn only; footer says so. Owner constraint.
11. Nit (visual, taste). About right third empty on wide screens; skills lists 5/3/3.
12. Nit (process). Findings 1 to 5 need owner facts and files. Many cycles in a row have produced no site change. Owner should supply them, or the loop should pause.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark footer and theme.
- Specific copy and the plain "For the record" ledger.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, no tap-target or contrast failures.
- Numbered rows, stamps, filters, press states, 404 joke, Previous/Next with a fact, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page, Fig. 1 schematics with honest captions ("Module count is illustrative"), the struck-through "three weeks".

## Verdict
The site is coherent, plain and clearly authored. AI-tell is 2 and the retro matte commitment holds. What holds it back is missing owner input: a status and dates line, a decided lead project with a real page behind it, sourced or explained claims, and local copies of resume, images and fonts. No new designer-side item this cycle. Research was blocked, so no finding rests on a source I read.
