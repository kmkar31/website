# Critique, 2026-11-21 (HEAD 058a4b2; no site files edited)

Method: `python3 tools/check.py . agents/shots` finished (rc=0, zero FAIL; only "images not loaded" sandbox notes). I viewed index at phone-light, tablet-dark and desktop-light, and about at desktop-light. Since the last critique only agents/LOG.md changed (cycles 174 and 175: no site changes), so no regression is possible. Wix and Google Fonts are unreachable in the sandbox (environment limit, not a design bug).

## Sources consulted
- Carried from earlier cycles, not re-read now: https://www.nngroup.com/articles/ux-design-portfolios/ (hiring managers scan for problem, role, constraints, outcome; 3-5 strong case studies beat many shallow ones). Findings 1, 2 and 12 rely on it.
- Blocked again this cycle (permission request unanswered, not retried): https://web.dev/articles/optimize-cls. Finding 5 is therefore stated from general knowledge and is unverified.
- The three-source requirement is not met for the third cycle running. This is a tooling limit (web fetch is blocked), not a lack of effort. No new topic could be researched, so this cycle's topic variation is nil.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, glow, chips, stats strip or card trio. Copy is specific (three weeks struck through to 15 minutes, 99 s, 46 orbits, 500 m). Residual tell: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Serif name, mono credential line, ruled list, hard-offset red button, flat dark footer, paper grain; dark theme holds. Weak spots: stamps only on rows 04 to 07 leave the right column ragged on desktop; the Fig. 1 plate sits alone on row 06; the About right third is empty on wide screens.
- SEO: 7/10, unchanged. Unique titles, one h1, canonical, sitemap, JSON-LD, absolute og:image. Weak: one shared OG card; robots.txt under a subpath is ignored by crawlers (host limit); Wix images lack dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, "For the record" ledger, 404 joke, pressable 99 s stamp. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, hard shadow, flat footer, inverted-print dark theme).
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).
No new owner notes since 2026-10-22.

## Ranked findings
1. Major (UX, credibility). No status or date line. The hero reads "MS Mechanical Engineering, Carnegie Mellon University" with no tense; About says 2023 to 2025. Today is 2026-11-21, so the degree reads as finished, yet nothing says what he does now or whether he is available. `STATUS = ""` in build/build.py renders no Status row in the ledger. Needs an owner fact.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads and matches the hero sentence, but its page has no method, result or personal contribution. "START HERE" sits on row 06 (aerobraking) with no reason given. Owner: pick the lead and supply the snake method and result, or move the label.
3. Major (credibility). Raftar's page frames the car as "one-fifth the weight of a Ferrari" with no source or number. Aerobraking never says what Karthik changed, and "46 orbits" has no baseline. Owner: add a source or cut the claim, and add one sentence of contribution.
4. Major (robustness). The Resume PDF is a Wix hotlink in the header, hero, About and footer. It is the main call to action and depends on a third party. Needs a local resume.pdf.
5. Major (performance). Wix images on content pages (1 to 10 per page) lack width and height, which risks CLS and an outage dependency. Needs local files first (principle unverified, source blocked).
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 when files exist.
7. Minor (visual). Ragged stamp column on Home desktop; lone Fig. 1 plate on row 06. Root cause is finding 2. Tablet (820 px) shows the same row 06 title squeezed to three lines beside the plate.
8. Minor (SEO). One shared OG card; robots.txt path is a host limit. Owner action: submit the sitemap in Search Console.
9. Minor (content). Tricycle page voice is passive. Owner's call.
10. Minor (UX). Contact is LinkedIn only; the footer states it. Owner constraint.
11. Nit (visual, taste). About right third is empty on wide screens; skills lists are 5/3/3.
12. Nit (process). Findings 1 to 5 need owner facts or files. Ten consecutive cycles have produced no site change. The owner should supply them or the loop should pause; further critiques will repeat this list.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark footer, readable dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, no tap-target or contrast failures.
- Numbered rows, stamps, filters, press states, 404 joke, Previous/Next with a fact, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page, honest Fig. 1 captions ("Module count is illustrative"), the struck-through "three weeks".
- About page: dated, scannable education and experience with quantified bullets, sticky "On this page" index.

## Overall verdict
The site is coherent, specific and convincingly hand-made, with an AI-tell of 2. Its weakness is not craft but missing owner-supplied content: a current status, a clear lead project with method and result, a sourced Raftar claim, a local resume and local images. Until those arrive, design work has hit its ceiling and UX stays at 6. The highest-value next step is owner input, not another design pass.
