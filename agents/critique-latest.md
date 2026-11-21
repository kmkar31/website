# Critique, 2026-11-21 (HEAD 1a7451a; no site files edited)

Method: `python3 tools/check.py . agents/shots` completed (zero FAIL; only "images not loaded" sandbox notes). The first foreground run hit the 2 minute tool timeout, so I reran it in the background and it finished. I viewed index at phone-light, tablet-dark and desktop-light, and snake-robots at phone-light. `git status` was clean and the only commit since the last critique is cycle 176 (LOG.md only), so no regression is possible. Wix and Google Fonts are unreachable in the sandbox (environment limit, not a design bug).

## Sources consulted
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum (WCAG 2.2 SC 2.5.8, 24 px minimum target). Found via search this cycle; only the result listing was available to me, I did not read the page body. Used only to back the claim in "Good" that tap targets pass.
- https://www.nngroup.com/articles/ux-design-portfolios/ and https://www.nngroup.com/videos/ux-portfolios-hiring/ (NN/g, what hiring managers look for in a portfolio). Found via search this cycle, bodies not read. The claim that they scan for problem, role, constraints and outcome is carried from earlier cycles. Findings 1 to 3 rely on it.
- https://web.dev/articles/optimize-cls: the fetch was blocked (permission request unanswered, not retried). The result appeared in search but I did not read it. Finding 5 (set width and height on images) is therefore stated from general knowledge and is unverified by me this cycle.
- Honest summary: the three-source requirement is met in listing only. I read none of the three pages in full, and no new topic was researched. This is a tooling limit, not a design judgement.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, glow, chips, stats strip or card trio. Copy is specific (three weeks struck through to 15 minutes, 99 s, 46 orbits, 500 m). Residual tell: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Serif name, mono credential line, ruled list, hard-offset red button, flat dark footer, paper grain; dark theme holds. Weak spots: stamps appear only on rows 04 to 07, so the right column is ragged on desktop; the Fig. 1 plate sits alone on row 06; the About right third is empty on wide screens.
- SEO: 7/10, unchanged. Unique titles, one h1, canonical, sitemap, JSON-LD, absolute 1200x630 og:image with alt. Weak: one shared OG card for every page; robots.txt under a subpath is ignored by crawlers (host limit); Wix images lack dimensions (grep: Wix hotlinks remain on 11 of 13 pages, up to 7 on aerobraking-drl).
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, "For the record" ledger, 404 joke, pressable 99 s stamp. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, hard shadow, flat footer, inverted-print dark theme). Confirmed in the screenshots, not just the CSS.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).
No new owner notes since 2026-10-22.

## Ranked findings
1. Major (UX, credibility). No status or date line. The hero reads "MS Mechanical Engineering, Carnegie Mellon University" with no tense; About says 2023 to 2025. Today is 2026-11-21, so the degree reads as finished, yet nothing says what he does now or whether he is available. `STATUS = ""` at build/build.py:266 renders no Status row in the ledger. Needs an owner fact.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads and matches the hero sentence, but its page (viewed on phone) is a stub: one question, one schematic, one paragraph, no method, result or personal contribution. "START HERE" sits on row 06 (aerobraking) with no reason given. Owner: pick the lead and supply the snake method and result, or move the label.
3. Major (credibility). Raftar's page frames the car as "one-fifth the weight of a Ferrari" with no source or number. Aerobraking never says what Karthik changed, and "46 orbits" has no baseline. Owner: add a source or cut the claim, and add one sentence of contribution.
4. Major (robustness). The Resume PDF is a Wix hotlink in the header, hero, About and footer. It is the main call to action and depends on a third party. Needs a local resume.pdf.
5. Major (performance). Wix images on content pages lack width and height, which risks CLS and an outage dependency (source blocked, unverified by me). Needs local files first.
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 when files exist.
7. Minor (visual). Ragged stamp column on Home desktop; lone Fig. 1 plate on row 06. Root cause is finding 2. At tablet width the row 06 title wraps to three lines beside the plate (seen in tablet-dark).
8. Minor (SEO). One shared OG card; robots.txt path is a host limit. Owner action: submit the sitemap in Search Console.
9. Minor (content). Tricycle page voice is passive. Owner's call.
10. Minor (UX). Contact is LinkedIn only; the footer states it. Owner constraint.
11. Nit (visual, taste). About right third is empty on wide screens; skills lists are 5/3/3.
12. Nit (process). Findings 1 to 5 need owner facts or files. Eleven consecutive cycles have produced no site change. The owner should supply them or the loop should pause; further critiques will repeat this list.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark footer, readable dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, no tap-target or contrast failures reported by check.py.
- Numbered rows, stamps, filters, press states, 404 joke, Previous/Next with a fact, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page, honest Fig. 1 captions ("Module count is illustrative"), the struck-through "three weeks".
- About page: dated, scannable education and experience with quantified bullets, sticky "On this page" index.

## Overall verdict
The site is coherent, specific and convincingly hand-made, with an AI-tell of 2. Its weakness is not craft but missing owner-supplied content: a current status, a clear lead project with method and result, a sourced Raftar claim, a local resume and local images. Until those arrive, design work has hit its ceiling and UX stays at 6. The highest-value next step is owner input, not another design pass.
