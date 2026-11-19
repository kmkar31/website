# Critique, 2026-11-19 (HEAD 960b076; no site files edited)

Method: `python3 tools/check.py . agents/shots` ran to completion. Every page, 3 viewports and 2 themes came back OK, with only "images not loaded" sandbox notes. I viewed index phone-light, index desktop-light and aerobraking-drl phone-dark. Cycles 164 to 166 changed no site files, so there is no regression. Wix and Google Fonts are unreachable in the sandbox (environment limit, not a design bug).

## Sources consulted
Research was blocked a fourth cycle. WebFetch of https://web.dev/articles/optimize-cls returned PROVENANCE_REQUIRED (permission not answered) and I did not retry. I read no external source, so the "three sources" rule is not met. No finding below depends on a source. Carried-over, unread pointers:
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- https://web.dev/articles/optimize-cls
- https://www.nngroup.com/articles/designer-portfolios/

## Correction to last cycle
Last cycle's finding 3 said the aerobraking page has "no subheads". That was wrong. The page has h2 subheads (The problem, Setup, Method, Result) and the phone screenshot shows them. The designer's cycle 166 objection stands and I withdraw that claim. The real remaining issue on that page is content, not structure: the Method and Result paragraphs are dense, and there is no statement of what Karthik did himself.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip, card trio or sparkle. Copy is specific (three weeks struck through to 15 minutes, 99 s, 46 orbits, 500 m tether). Residual tell: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Serif name, mono credential line, ledger sidebar, ruled list, one hard-offset button, consistent paper palette, flat dark theme. Weak spots: stamps appear only on rows 04 to 07, so the desktop right column is ragged; the Fig. 1 plate on row 06 looks stray on phone (it sits above the title with no sibling); the footer is a heavy dark band against a light page.
- SEO: 7/10, unchanged. Unique titles, one h1, sitemap, canonical, JSON-LD, local og:image. Weak: one shared OG card; robots.txt under /website/ is ignored by crawlers (host limit); Wix images lack dimensions. I could not verify search or social previews offline.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 3).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, "For the record" ledger, 404 joke, "TIME ALLOWED: 99 S". No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Paper tones, ink borders, hard shadow, flat dark theme.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).

## Ranked findings
1. Major (UX, credibility). No status or date line. The hero says "MS Mechanical Engineering, Carnegie Mellon University" with no tense. About gives 2023 to 2025, and today is 2026-11-19, so the degree appears to have ended about a year ago. A recruiter cannot tell whether he has graduated, what he does now or whether he is available. I cannot confirm his status. `STATUS = ""` (build/build.py line 266) renders nothing. Owner must supply the fact.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads and matches the hero sentence, but it has no stamp and no stated method, result or personal contribution. "START HERE" sits on row 06 (aerobraking) with no reason given. Owner should pick the lead and supply the snake method and result, or move the label.
3. Major (credibility). The aerobraking page (the "START HERE" target) never says what Karthik changed beyond the cited Falcone et al. work. "46 orbits" has no baseline. Raftar's "one-fifth the weight of a Ferrari but matches its 0-60 time" has no source. Owner should give one sentence of personal contribution and a source, or cut the claim. The designer need not add an empty slot (agreed with the cycle 166 reasoning).
4. Major (robustness). The resume PDF is hotlinked from a Wix URL in the header, hero, footer and 404. There is no local resume.pdf. It is the main call to action, so one Wix lapse breaks it on every page. Needs the owner's PDF.
5. Major (performance). Wix images on every content page (1 to 10 per page by check.py counts) have no width/height. That risks CLS and an outage dependency. Needs local files, then dimensions and `fetchpriority="high"` on the first visible image. Not verified against sources.
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 once files exist.
7. Minor (visual). Ragged Home right column; the lone Fig. 1 plate on row 06 looks stray on phone. Root cause is finding 2.
8. Minor (SEO). All pages share one OG card; the robots.txt path is a host limit. Noted, not pressed.
9. Minor (content). The tricycle page voice is passive and has no subheads (check before acting; the aerobraking claim last cycle was wrong). Owner's call.
10. Minor (UX). Contact is LinkedIn only; the footer states it. Owner constraint.
11. Nit (visual, taste). About right third is empty on wide screens; skills lists are 5/3/3.
12. Nit (process). Findings 1 to 5 need owner facts and files. The last ten cycles produced one small CSS change. I recommend the owner supplies them, or the loop pauses.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, no tap-target or contrast failures in check.py.
- Numbered rows, stamps, filters, press states, 404 joke, Previous/Next with a fact, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page, Fig. 1 schematics with honest captions, the struck-through "three weeks".
- The cycle 163 About fix.

## Verdict
The site is coherent, plain and clearly authored. AI-tell is 2 and the retro matte commitment holds in both themes. What holds it back is missing owner input: a status and dates line, a decided lead project with a real page behind it, sourced or explained claims, and local copies of the resume, images and fonts. I have no new designer-side item this cycle, and I withdraw last cycle's subheads claim. Research was blocked for a fourth cycle, so none of this rests on newly read sources.
