# Critique, 2026-11-19 (HEAD e7e4f75; no site files edited)

Method: `python3 tools/check.py . agents/shots` ran to completion, zero FAIL (only "images not loaded" sandbox notes). I viewed index phone-light, index desktop-light and about tablet-light. `STATUS = ""` is still at build/build.py:266, and every project page except index still hotlinks Wix media. Cycle 163 fixed the About resume-link alignment and spacing (finding 8 last cycle); I confirmed it in about-tablet-light: link is flush left and the gap before Skills is normal. No regressions seen. Wix and Google Fonts are unreachable in the sandbox (environment limit, not a design bug).

## Sources consulted
Access was limited this cycle. WebFetch of the three pages below was blocked (permission request unanswered), so I read none of them. They are pointers only, and no finding rests on them. The "three sources" rule was not met because of this tooling limit.
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (WCAG 2.2 target size; blocked, not read)
- https://web.dev/articles/optimize-cls (image dimensions and font CLS; blocked, not read)
- https://www.nngroup.com/articles/designer-portfolios/ (NN/g hiring-manager portfolio guidance; blocked, not read)
Last cycle's search pointers (NN/g video on hiring managers, aem.live font-fallback) are also still unread.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip, card trio or sparkle. Specific copy (three weeks struck through to 15 minutes, 99 s, 46 orbits, 500 m tether). Residual tell: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Large serif name, mono credential line, ledger sidebar, ruled list, one hard-offset button, cohesive paper palette. Weak spots: stamps only on rows 04 to 07 so the desktop right column is ragged; Fig. 1 plate on row 06 reads as a stray on phone; empty paper under the sidebar on desktop and in the right third of About.
- SEO: 7/10, unchanged. Unique titles, one h1, sitemap, canonical, JSON-LD, local og:image. Weak: one shared OG card; robots.txt under /website/ is ignored by crawlers (host limit); Wix images have no dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, "For the record" ledger, 404 joke, pressable 99 s stamp. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Paper tones, ink borders, hard shadow, flat dark theme.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).

## Ranked findings
1. Major (UX, credibility). No status or date line. Hero says "MS Mechanical Engineering, Carnegie Mellon University" with no tense; About says "2023 – 2025"; today is 2026-11-19, so the degree appears to have ended a year ago. A recruiter cannot tell whether he has graduated, what he does now, or whether he is available. I cannot confirm his current status. `STATUS` is wired to render a ledger row; the owner must supply the fact.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads and matches the hero, but its page has a question, a short "Why snake robots" paragraph and a lab link, with no method, result or personal contribution. START HERE sits on row 06 (aerobraking). Owner should pick the lead and supply the snake method and result, or move the label.
3. Major (credibility). The aerobraking page does not say what Karthik changed beyond cited prior work, and "46 orbits" has no baseline. Raftar's "one-fifth the weight of a Ferrari but matches its 0-60 time" has no source on the page. Owner should give a sentence and a source, or cut the claim.
4. Major (robustness). The resume PDF is hotlinked from a Wix URL in the header, hero, footer and 404; there is no local assets/resume.pdf. If Wix lapses it breaks everywhere. Needs the owner's PDF.
5. Major (performance). Wix images remain on every content page (1 to 7 per page) with no width/height, which risks CLS and an outage dependency. Needs local files, then dimensions and `fetchpriority="high"` on the first visible image.
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 with a metric-adjusted fallback once files exist.
7. Minor (visual). Ragged Home right column; the lone Fig. 1 plate on row 06 looks stray on phone. Root cause is finding 2.
8. Minor (SEO). All pages share one OG card; robots.txt path is a host limit. Noted, not pressed.
9. Minor (content). Tricycle page voice is passive with no subheads. Owner's call.
10. Minor (UX). Contact is LinkedIn only; the footer states it. Owner constraint.
11. Nit (visual, taste). About right third is empty on wide screens; skills lists are 5/3/3.
12. Nit (process). Findings 1 to 5 need owner facts and files. Twelve of the last thirteen cycles produced no design change because of this. I recommend the owner supplies them, or the loop pauses.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, no tap-target or contrast failures in check.py.
- Numbered rows, stamps, filters, press states, 404 joke, Previous/Next with a fact, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page, Fig. 1 schematics with honest captions, the struck-through "three weeks".
- The cycle 163 About fix (flush Resume link, tighter gap before Skills).

## Verdict
The site is coherent, plain and clearly authored. AI-tell is 2 and the retro matte commitment holds in both themes. What holds it back is missing owner input: a status and dates line, a decided lead project with a real page behind it, sourced or explained claims, and local copies of the resume, images and fonts. The only designer-fixable item from last cycle is done, and I found nothing new on screen to fix. Research was thin this cycle because the page fetches were blocked, so none of this rests on newly read sources.
