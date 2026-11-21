# Critique, 2026-11-21 (HEAD bfd0a94; no site files edited)

Method: `python3 tools/check.py . agents/shots` completed, zero FAIL (only "images not loaded" sandbox notes). I viewed index phone-light, index desktop-light and snake-robots phone-light. Site files are unchanged since the last critique (cycles 169 to 178 touched only LOG.md), so no regression is possible. Wix and Google Fonts are unreachable in the sandbox (environment limit); screenshots show fallback serif for that reason.

## Sources consulted
- https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html : WebFetch blocked (permission unanswered, not retried). Not read.
- Earlier cycles' pointers (web.dev optimize-cls and optimize-lcp, WCAG 2.2 target-size-minimum, NN/g portfolio hiring video) were also blocked or seen only as search listings. Not read this cycle.
- Honest summary: I read zero external pages. Nothing here is newly researched. Claims about CLS, tap targets and hiring-manager scanning are from general knowledge and unverified. Tooling limit, not a design judgement.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, glow, chips, stats strip or card trio. Specific copy (three weeks struck through to 15 minutes, 99 s, 46 orbits, 500 m). Residual tell: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Serif name, mono credential line, ruled list, hard-offset button, flat dark footer, all seen. Weak spots: stamps only on rows 04 to 07 so the desktop right column is ragged; Fig. 1 plate sits alone on row 06; snake page (seen) is short, with a large empty gap before the footer.
- SEO: 7/10, unchanged. Unique titles, one h1, canonical, sitemap, JSON-LD, absolute og:image. Weak: one shared OG card; robots.txt under a subpath is ignored by crawlers (host limit); Wix hotlinks remain on most content pages.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, "For the record" ledger, 404 joke. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Paper tones, ink borders, hard offset shadow, flat footer, confirmed in screenshots.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).
No new owner notes since 2026-10-22.

## Ranked findings
1. Major (UX, credibility). No status or date line. Hero says "MS Mechanical Engineering, Carnegie Mellon University" with no tense; About says 2023 to 2025; today is 2026-11-21. Nothing says what he does now or whether he is available. `STATUS = ""` in build/build.py renders no Status row. Needs an owner fact.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads and matches the hero, but its page (seen) is a stub: question, lab, advisor, one schematic, one paragraph, no method, result or personal contribution. "START HERE" sits on row 06 (aerobraking) with no reason. Owner: pick the lead and supply snake method and result, or move the label.
3. Major (credibility). Raftar frames the car against a Ferrari with no source or number. Aerobraking never says what Karthik changed, and "46 orbits" has no baseline. Owner: source or cut, plus one sentence of contribution.
4. Major (robustness). The Resume PDF is a Wix hotlink in header, hero, About and footer; it is the main call to action and depends on a third party. Needs a local resume.pdf.
5. Major (performance, unverified). Wix images on content pages likely lack width and height (CLS risk, outage dependency). Needs local files first.
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 when files exist.
7. Minor (visual). Ragged stamp column on Home desktop; lone Fig. 1 plate on row 06 (root cause is finding 2).
8. Minor (SEO). One shared OG card; robots.txt path is a host limit. Owner action: submit the sitemap in Search Console.
9. Minor (content). Tricycle page voice is passive. Owner's call.
10. Minor (UX). Contact is LinkedIn only (footer says so). Owner constraint.
11. Nit (visual, taste). About right third empty on wide screens.
12. Nit (process). Findings 1 to 5 need owner facts or files. Ten consecutive cycles (169 to 178) produced no site change; this list repeats until the owner supplies input or the loop pauses.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark footer, readable dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, no tap-target or contrast failures from check.py.
- Numbered rows, stamps, filters, press states, 404 joke, Previous/Next with a fact, per-page JSON-LD, canonical and OG, one h1 per page, honest Fig. 1 captions ("Module count is illustrative"), the struck-through "three weeks".
- About page: dated, scannable education and experience, sticky index.

## Overall verdict
The site is coherent, specific and convincingly hand-made, AI-tell 2. Its weakness is missing owner-supplied content: a current status, a clear lead project with method and result, a sourced Raftar claim, a local resume and local images. Design work has hit its ceiling and UX stays at 6. The highest-value next step is owner input, not another design pass. This critique is also unresearched (all source fetches blocked), so treat its external claims as unverified.
