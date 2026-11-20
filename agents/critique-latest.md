# Critique, 2026-11-20 (HEAD 4df4c4c; no site files edited)

Method: `python3 tools/check.py . agents/shots` completed (zero FAIL; only "images not loaded" sandbox notes). I viewed index phone-light and index desktop-light. Cycles 165 to 168 changed no site files, so there is no regression. Wix and Google Fonts are unreachable in the sandbox (environment limit, not a design bug).

## Sources consulted
WebSearch returned only titles and links. I did not open the pages, so these are pointers and no finding rests on their text.
- https://www.nngroup.com/videos/ux-portfolios-hiring/ (what hiring managers look for; findings 1 to 3)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (target size; no issue found, check.py passes)
- https://web.dev/articles/font-best-practices and https://developer.chrome.com/docs/modern-web-guidance/guides/visual-design/visually-stable-font-fallbacks (font fallbacks and layout shift; finding 6)
Topic varied this cycle: target size and font loading.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Copy is specific (three weeks struck through to 15 minutes, 99 s, 46 orbits, 500 m). Residual tell: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Serif name, mono credential line, ledger sidebar, ruled list, one hard-offset button, flat dark theme. Weak spots seen in the screenshots: stamps appear only on rows 04 to 07, so the desktop right column is ragged; the Fig. 1 plate on row 06 sits alone on phone; the footer is a heavy dark band.
- SEO: 7/10, unchanged. Unique titles, one h1, sitemap, canonical, JSON-LD, local og:image. Weak: one shared OG card; robots.txt under a subpath is ignored by crawlers (host limit); Wix images lack dimensions. Search and social previews could not be verified offline.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 3).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, "For the record" ledger, 404 joke, pressable 99 s stamp. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Paper tones, ink borders, hard shadow, flat dark theme.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).

## Ranked findings
1. Major (UX, credibility). No status or date line. The hero reads "MS Mechanical Engineering, Carnegie Mellon University" with no tense, and About gives 2023 to 2025. Today is 2026-11-20, so the degree appears to have ended about a year ago. A recruiter cannot tell if he has graduated, what he does now or whether he is available. `STATUS = ""` (build/build.py line 266) renders nothing. I cannot confirm his status; the owner must supply it.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads and matches the hero sentence, but it has no stamp and no stated method, result or personal contribution. "START HERE" sits on row 06 (aerobraking) with no reason given. The owner should pick the lead and supply the snake method and result, or move the label.
3. Major (credibility). The aerobraking page (the "START HERE" target) never says what Karthik changed beyond the cited prior work, and "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. The owner should give one sentence of personal contribution and a source, or cut the claim.
4. Major (robustness). The resume PDF is hotlinked from a Wix URL in the header, hero, footer and 404. It is the main call to action, so one Wix lapse breaks it on every page. It needs a local resume.pdf from the owner.
5. Major (performance). Wix images on every content page (check.py counts 1 to 10 per page) have no width/height, which risks CLS and an outage dependency. They need local files, then dimensions and `fetchpriority="high"` on the first visible image.
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 once the files exist, and add a metric-adjusted fallback (see the web.dev and Chrome links above).
7. Minor (visual). Ragged Home right column; the lone Fig. 1 plate on row 06 looks stray on phone. Root cause is finding 2.
8. Minor (SEO). All pages share one OG card; the robots.txt path is a host limit. Noted, not pressed.
9. Minor (content). The tricycle page voice is passive. The owner's call.
10. Minor (UX). Contact is LinkedIn only; the footer says so. Owner constraint.
11. Nit (visual, taste). About right third is empty on wide screens; skills lists are 5/3/3.
12. Nit (process). Findings 1 to 5 need owner facts and files. About 25 cycles in a row have produced no site change. I recommend the owner supplies them, or the loop pauses.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, no tap-target or contrast failures.
- Numbered rows, stamps, filters, press states, 404 joke, Previous/Next with a fact, per-page JSON-LD, canonical and OG, reduced-motion handling, one h1 per page, Fig. 1 schematics with honest captions, the struck-through "three weeks".

## Verdict
The site is coherent, plain and clearly authored. AI-tell is 2 and the retro matte commitment holds in both themes. What holds it back is missing owner input: a status and dates line, a decided lead project with a real page behind it, sourced or explained claims, and local copies of the resume, images and fonts. I have no new designer-side item this cycle. No finding rests on a source I read in full.
