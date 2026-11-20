# Critique, 2026-11-20 (HEAD f73a9bd; no site files edited)

Method: `python3 tools/check.py . agents/shots` ran to completion (zero FAIL; only "images not loaded" sandbox notes). I viewed index phone-light, index desktop-light, index tablet-dark, raftar phone-light and about desktop-dark. I also read the snake-robots main content from the HTML. Wix and Google Fonts are unreachable in the sandbox (environment limit, not a design bug).

## Sources consulted
Research was only partly possible. WebFetch of https://web.dev/articles/optimize-cls and https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html was blocked (permission request unanswered). One WebSearch worked and returned only titles and links, no page text. I read none of these, so no finding below rests on a source text:
- https://www.nngroup.com/videos/ux-portfolios-hiring/ (search result only, not read; relevant to findings 1 and 2)
- https://web.dev/articles/optimize-cls (blocked; finding 5)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (blocked; no tap-target issue found)
The three-source requirement was not met. This is an environment limit.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, glow, chips, stats strip or card trio. Specific copy (three weeks struck through to 15 minutes, 99 s, 46 orbits, 500 m). Residual tell: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Serif name, mono credential line, ruled list, hard-offset red button, flat dark footer, paper grain. Weak: the stamp column is ragged (rows 04 to 07 only); the Fig. 1 plate on row 06 sits alone on phone; the snake page is visibly thin; the About right third is empty on wide screens apart from a three-link index.
- SEO: 7/10, unchanged. Unique titles, one h1, canonical, sitemap, JSON-LD, local og:image. Weak: one shared OG card; robots.txt under a subpath (host limit); Wix images lack dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 3).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, "For the record" ledger, 404 joke, pressable 99 s stamp. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, hard shadow, flat footer, inverted-print dark theme).
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).
No new owner notes since 2026-10-22.

## Ranked findings
1. Major (UX, credibility). No status or date line. The hero says "MS Mechanical Engineering, Carnegie Mellon University" with no tense; About says 2023 to 2025. Today is 2026-11-20, so the degree appears finished. A recruiter cannot tell if he has graduated, what he does now or whether he is available. `STATUS` in build/build.py (line 266) is still empty, so the ledger renders no Status row. Owner must supply the fact. Why: a hiring reader scans for current status first (NN/g portfolio-hiring pointer, unread).
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads and matches the hero sentence, but the snake page holds only a question, lab and advisor, one schematic, three Wix photos that fail offline, one generic paragraph "Why snake robots" and a lab link. It has no method, result or personal contribution. "START HERE" sits on row 06 (aerobraking) with no reason given. Owner: pick the lead and supply the snake method and result, or move the label.
3. Major (credibility). Raftar's page asks how to build a car "one-fifth the weight of a Ferrari" with the same 0-60 time, and gives no source or number. Its "My part" paragraph is clear, but the headline claim is unsupported. Aerobraking never says what Karthik changed beyond prior work, and "46 orbits" has no baseline. Owner: a source or cut the Ferrari claim, and one sentence of contribution.
4. Major (robustness). The Resume PDF is a Wix hotlink in the header, hero, About and footer. It is the main call to action. Needs a local resume.pdf from the owner.
5. Major (performance). Wix images on content pages (1 to 10 per page) have no width and height, so they risk CLS and an outage dependency; the snake page's first image carries `fetchpriority="high"` but no dimensions. Needs local files, then dimensions. (Principle unverified this cycle.)
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 when files exist, with a metric-adjusted fallback.
7. Minor (visual). Ragged stamp column on Home desktop; the lone Fig. 1 plate on row 06 looks stray on phone. Root cause is finding 2.
8. Minor (SEO). All pages share one OG card; robots.txt path is a host limit. Submit the sitemap in Search Console (owner action).
9. Minor (content). Tricycle page voice is passive. Owner's call.
10. Minor (UX). Contact is LinkedIn only; footer states it. Owner constraint.
11. Nit (visual, taste). About right third is empty on wide screens; skills lists are 5/3/3.
12. Nit (process). Findings 1 to 5 need owner facts or files, and many cycles in a row have produced no site change. The owner should supply them, or the loop should pause.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark footer, readable dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, no tap-target or contrast failures.
- Numbered rows, stamps, filters, press states, 404 joke, Previous/Next with a fact, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page, Fig. 1 schematics with honest captions ("Module count is illustrative"), the struck-through "three weeks".
- Raftar page: the "My part was..." paragraph states his role plainly.

## Verdict
The site is coherent, plain and clearly authored. AI-tell is 2 and the retro matte commitment holds, with no regression from the last cycle. What holds it back is missing owner input: a status and dates line, a decided lead project with a real page behind it, sourced or explained claims, and local copies of the resume, images and fonts. There is no new designer-side item this cycle. Research was mostly blocked, so no finding rests on a source I read.
