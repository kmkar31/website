# Critique, 2026-11-19 (HEAD 9dccb2b; no site files edited)

Method: `python3 tools/check.py . agents/shots` ran to completion: every page, 3 viewports, 2 themes OK, only "images not loaded" sandbox notes. I viewed index phone-light, index desktop-dark and aerobraking-drl phone-light. Cycles 164 and 165 changed no site files, so there is no regression to find. Wix and Google Fonts are unreachable in the sandbox (environment limit, not a design bug).

## Sources consulted
Research was blocked a third cycle. WebFetch of https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html returned PROVENANCE_REQUIRED (permission not answered), and I did not retry. I read no external source this cycle, so the "three sources" rule is not met. No finding below rests on a source; the pointers are carried over from earlier cycles and are unverified:
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (blocked, not read)
- https://web.dev/articles/optimize-cls (not read)
- https://www.nngroup.com/articles/designer-portfolios/ (not read)

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip, card trio or sparkle. Copy is specific (three weeks struck through to 15 minutes, 99 s, 46 orbits, 500 m tether). Residual tell: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Serif name, mono credential line, ledger sidebar, ruled list, one hard-offset button, consistent paper palette and an inverted-print dark theme that holds up on desktop. Weak spots: stamps only on rows 04 to 07, so the desktop right column is ragged; the Fig. 1 plate on row 06 looks stray on phone; the aerobraking page body is long undivided prose.
- SEO: 7/10, unchanged. Unique titles, one h1, sitemap, canonical, JSON-LD, local og:image. Weak: one shared OG card; robots.txt under /website/ is ignored by crawlers (host limit); Wix images lack dimensions. Could not verify rendering in search or social previews offline.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 3).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, "For the record" ledger, 404 joke, "TIME ALLOWED: 99 S" stamp. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Paper tones, ink borders, hard shadow, flat dark theme.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).

## Ranked findings
1. Major (UX, credibility). No status or date line. The hero says "MS Mechanical Engineering, Carnegie Mellon University" with no tense; About gives 2023 to 2025; today is 2026-11-19, so the degree appears to have ended about a year ago. A recruiter cannot tell whether he has graduated, what he does now or whether he is available. I cannot confirm his status. `STATUS = ""` in build/build.py still renders nothing. Owner must supply the fact.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads and matches the hero sentence, but it carries no stamp and its page has no method, result or personal contribution (seen last cycle). "START HERE" sits on row 06 (aerobraking) with no reason given. Owner should pick the lead and supply the snake method and result, or move the label.
3. Major (credibility, new detail this cycle). The aerobraking page (viewed on phone) is the page "START HERE" sends people to, yet its Problem, Setup and Method sections are paper-style prose of five to seven line paragraphs with no subheads, and the page never says what Karthik changed beyond the cited Falcone et al. work. "46 orbits" has no baseline. Raftar's "one-fifth the weight of a Ferrari but matches its 0-60 time" has no source. Owner should give one sentence of personal contribution and a source, or cut the claim. Designer could, without new facts, add subheads or a short "what I did" slot that stays empty until supplied.
4. Major (robustness). The resume PDF is hotlinked from a Wix URL in the header, hero, footer and 404; there is no local resume.pdf. It is the main call to action, so a lapse breaks it on every page. Needs the owner's PDF.
5. Major (performance). Wix images on every content page (1 to 10 per page by check.py counts) have no width/height, which risks CLS and an outage dependency. Needs local files, then dimensions and `fetchpriority="high"` on the first visible image. Not verified against sources.
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 once files exist.
7. Minor (visual). Ragged Home right column; the lone Fig. 1 plate on row 06 looks stray on phone. Root cause is finding 2.
8. Minor (SEO). All pages share one OG card; robots.txt path is a host limit. Noted, not pressed.
9. Minor (content). Tricycle page voice is passive with no subheads. Owner's call.
10. Minor (UX). Contact is LinkedIn only; the footer states it. Owner constraint.
11. Nit (visual, taste). About right third is empty on wide screens; skills lists are 5/3/3.
12. Nit (process). Findings 1 to 5 need owner facts and files. Cycles 157 to 165 produced one small CSS change. I recommend the owner supplies them, or the loop pauses.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, no tap-target or contrast failures in check.py.
- Numbered rows, stamps, filters, press states, 404 joke, Previous/Next with a fact, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page, Fig. 1 schematics with honest captions, the struck-through "three weeks".
- The cycle 163 About fix.

## Verdict
The site is coherent, plain and clearly authored. AI-tell is 2 and the retro matte commitment holds in both themes. What holds it back is missing owner input: a status and dates line, a decided lead project with a real page behind it, sourced or explained claims, and local copies of the resume, images and fonts. The one designer-side item I add is structure on the aerobraking page (subheads), since it is the page the site points visitors to. Research was blocked for a third cycle, so none of this rests on newly read sources.
