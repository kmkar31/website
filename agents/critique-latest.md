# Critique, 2026-11-20 (HEAD fdb7475; no site files edited)

Method: `python3 tools/check.py . agents/shots` ran to completion (rc=0, zero FAIL; only "images not loaded" sandbox notes). I viewed index phone-light, index phone-dark, index desktop-light, snake-robots desktop-light and about tablet-light. I also grepped the HTML for status, image attributes, robots and og:image. Since the last critique only agents/LOG.md changed (no site diff), so nothing can have regressed. Wix and Google Fonts are unreachable in the sandbox (environment limit, not a design bug).

## Sources consulted
Research was again mostly blocked. WebFetch of both pages below was refused (permission request unanswered). One WebSearch returned only titles and links. I read no source text, so no finding rests on one. The three-source requirement was not met; this is an environment limit.
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (blocked; no tap-target problem found by eye or by check.py)
- https://web.dev/articles/optimize-cls (blocked; finding 5)
- https://www.nngroup.com/videos/ux-portfolios-hiring/ (search result only, unread; findings 1 and 2)

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, glow, chips, stats strip or card trio. Copy is specific (three weeks struck through to 15 minutes, 99 s, 46 orbits, 500 m). Residual tell: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Serif name, mono credential line, ruled list, hard-offset red button, flat dark footer, paper grain; dark theme reads well. Weak: stamps appear only on rows 04 to 07, so the right column is ragged on desktop; the Fig. 1 plate on row 06 sits alone; the snake page is visibly thin (one question, one schematic, two sentences, one link); the About right third is empty on wide screens.
- SEO: 7/10, unchanged. Unique titles, one h1, canonical, sitemap, JSON-LD, absolute og:image at assets/og.png. Weak: every page shares one OG card; robots.txt sits under a subpath, so crawlers will ignore it (host limit); Wix images lack width/height.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, "For the record" ledger, 404 joke, pressable 99 s stamp. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, hard shadow, flat footer, inverted-print dark theme).
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).
No new owner notes since 2026-10-22.

## Ranked findings
1. Major (UX, credibility). No status or date line. The hero says "MS Mechanical Engineering, Carnegie Mellon University" with no tense; About says 2023 to 2025. Today is 2026-11-20, so the degree appears finished, yet nothing says what he does now or whether he is available. `STATUS = ""` at build/build.py line 266, so the ledger renders no Status row. Needs an owner fact. A recruiter scans for current status first (NN/g pointer, unread).
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads and matches the hero sentence, but its page has no method, result or personal contribution and its three Wix photos fail offline. "START HERE" is on row 06 (aerobraking) with no reason given. Owner: pick the lead and supply the snake method and result, or move the label.
3. Major (credibility). Raftar's page frames the car as "one-fifth the weight of a Ferrari" with no source or number. Aerobraking never says what Karthik changed, and "46 orbits" has no baseline. Owner: add a source or cut the claim, and add one sentence of contribution.
4. Major (robustness). The Resume PDF is a Wix hotlink in the header, hero, About and footer. It is the main call to action and depends on a third party. Needs a local resume.pdf.
5. Major (performance). Wix images on content pages (1 to 10 per page) have no width and height, which risks CLS and an outage dependency; the snake page's first image has `fetchpriority="high"` but no dimensions. Needs local files first (principle unverified this cycle).
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 when files exist.
7. Minor (visual). Ragged stamp column on Home desktop; lone Fig. 1 plate on row 06. Root cause is finding 2.
8. Minor (SEO). One shared OG card; robots.txt path is a host limit. Owner action: submit the sitemap in Search Console.
9. Minor (content). Tricycle page voice is passive. Owner's call.
10. Minor (UX). Contact is LinkedIn only; the footer states it. Owner constraint.
11. Nit (visual, taste). About right third is empty on wide screens; skills lists are 5/3/3.
12. Nit (process). Findings 1 to 5 need owner facts or files. Five or more cycles in a row have produced no site change. The owner should supply them or the loop should pause.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark footer, readable dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, no tap-target or contrast failures.
- Numbered rows, stamps, filters, press states, 404 joke, Previous/Next with a fact, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page, honest Fig. 1 captions ("Module count is illustrative"), the struck-through "three weeks".
- Raftar page: "My part was..." states his role plainly.

## Verdict
The site is coherent, plain and clearly authored. AI-tell is 2 and the retro matte commitment holds, with no site change since the last critique. What holds it back is missing owner input: a status and dates line, a decided lead project with a real page behind it, sourced or explained claims, and local copies of the resume, images and fonts. There is no new designer-side item this cycle. Research was blocked, so no finding rests on a source I read.
