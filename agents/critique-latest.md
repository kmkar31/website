# Critique, 2026-11-21 (HEAD 76237c0; no site files edited)

Method: `python3 tools/check.py . agents/shots` completed (run in the background because it exceeds the 2 minute tool timeout): zero FAIL, only "images not loaded" sandbox notes. I viewed index at phone-light and desktop-dark. The site is unchanged since the last critique (cycles 169 to 177 changed only LOG.md), so no regression is possible. Wix and Google Fonts are unreachable in the sandbox (environment limit). Screenshots render fallback serif for the same reason.

## Sources consulted
- https://web.dev/articles/optimize-cls : fetch blocked (permission unanswered, not retried). Finding 5 is stated from general knowledge, unverified this cycle.
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html : fetch blocked. Only the search listing seen earlier; used only to support "tap targets pass".
- https://web.dev/optimize-lcp/ and https://web.dev/blog/common-misconceptions-lcp : seen in search results only, bodies not read. Backs finding 6 (fonts) loosely.
- https://www.nngroup.com/videos/ux-portfolios-hiring/ : seen in search results only. Findings 1 to 3 rely on the claim, carried from earlier cycles, that hiring managers scan for role, problem, constraints and outcome.
- Honest summary: I read none of these pages; fetches were blocked. Nothing new was researched. Tooling limit, not a design judgement.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, glow, chips, stats strip or card trio. Copy is specific (three weeks struck through to 15 minutes, 99 s, 46 orbits, 500 m). Residual tell: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Serif name, mono credential line, ruled list, hard-offset button, flat dark footer; dark theme holds (seen). Weak spots: stamps only on rows 04 to 07 so the right column is ragged on desktop; Fig. 1 plate sits alone on row 06; About right third empty on wide screens.
- SEO: 7/10, unchanged. Unique titles, one h1, canonical, sitemap, JSON-LD, absolute og:image. Weak: one shared OG card; robots.txt under a subpath is ignored by crawlers (host limit); Wix hotlinks remain on 12 of 13 content pages (grep count: 7 on aerobraking-drl, 5 on quadrotor-sysid, 4 each on tricycle, submarine, nanosatellite).
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, "For the record" ledger, 404 joke, 99 s stamp. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, hard shadow, flat footer, inverted-print dark theme), confirmed in screenshots.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).
No new owner notes since 2026-10-22.

## Ranked findings
1. Major (UX, credibility). No status or date line. Hero says "MS Mechanical Engineering, Carnegie Mellon University" with no tense; About says 2023 to 2025; today is 2026-11-21. Nothing says what he does now or whether he is available. `STATUS = ""` at build/build.py:266 renders no Status row. Needs an owner fact.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads and matches the hero, but its page is a stub (no method, result or personal contribution). "START HERE" sits on row 06 (aerobraking) with no reason (seen in both screenshots). Owner: pick the lead, supply snake method and result, or move the label.
3. Major (credibility). Raftar frames the car as "one-fifth the weight of a Ferrari" with no source or number. Aerobraking never says what Karthik changed, and "46 orbits" has no baseline. Owner: source or cut, plus one sentence of contribution.
4. Major (robustness). The Resume PDF is a Wix hotlink in header, hero, About and footer; it is the main call to action and depends on a third party. Needs a local resume.pdf.
5. Major (performance). Wix images on content pages lack width and height (CLS risk, outage dependency; unverified by me). Needs local files first.
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 when files exist.
7. Minor (visual). Ragged stamp column on Home desktop; lone Fig. 1 plate on row 06 (root cause is finding 2).
8. Minor (SEO). One shared OG card; robots.txt path is a host limit. Owner action: submit sitemap in Search Console.
9. Minor (content). Tricycle page voice is passive. Owner's call.
10. Minor (UX). Contact is LinkedIn only; the footer states it. Owner constraint.
11. Nit (visual, taste). About right third empty on wide screens; skills lists are 5/3/3.
12. Nit (process). Findings 1 to 5 need owner facts or files. Nine consecutive cycles (169 to 177) produced no site change; this list will keep repeating until the owner supplies input or the loop pauses.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark footer, readable dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, no tap-target or contrast failures from check.py.
- Numbered rows, stamps, filters, press states, 404 joke, Previous/Next with a fact, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page, honest Fig. 1 captions, the struck-through "three weeks".
- About page: dated, scannable education and experience, sticky "On this page" index.

## Overall verdict
The site is coherent, specific and convincingly hand-made, AI-tell 2. Its weakness is missing owner-supplied content: a current status, a clear lead project with method and result, a sourced Raftar claim, a local resume and local images. Until those arrive, design work has hit its ceiling and UX stays at 6. The highest-value next step is owner input, not another design pass.
