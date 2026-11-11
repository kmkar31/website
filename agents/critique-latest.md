# Critique, 2026-11-11 (cycle 118)

Rendering: `python3 tools/check.py . agents/shots` completed (every page OK, only "images not loaded, sandbox network" notes). I viewed index phone light, index desktop light, projects phone dark and raftar-formula-racing tablet light. I edited no site files. HEAD is 3b87b2e (log-only), so site source is unchanged and I found no regression.

## Sources consulted
WebFetch was blocked by the permission system this cycle for these pages, so I read none in full: https://web.dev/articles/prefers-color-scheme , https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html , https://www.nngroup.com/articles/portfolios/ . WebSearch worked, so the items below are result-level pointers only. Nothing here is a verified quote.
- WCAG 2.2 what's new (Focus Appearance, Target Size): https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- web.dev, prefers-color-scheme: https://web.dev/prefers-color-scheme
- web.dev Learn Design, theming: https://web.dev/learn/design/theming
- Chrome, dark mode guidance: https://developer.chrome.com/docs/modern-web-guidance/guides/visual-design/dark-mode
- Topic this cycle: dark-mode and focus appearance. Local evidence: index.html carries a color-scheme declaration, and the CSS has a 3px `:focus-visible` outline with 3px offset. That is consistent with the guidance as I understand it.

## Scores
- AI-tell: 2/10, unchanged. Paper tone, grain, double rules, one hard-offset button, struck-through "three weeks" on amber, rotated stamps, mono ledger and the serif pairing look authored. The copy is plain first person. The residual tell is the familiar overall shape (intro, ruled list, dark footer). No tell moved.
- Looks good: 8/10. Desktop home has a clear measure and rhythm. The Raftar tablet page is well composed. Weak spots: the lone plate on row 06 next to bare rows, and a gap under the lede on desktop where the ledger ends early.
- SEO: 7/10, unchanged. See findings 5 and 6.
- UX: 6/10. On the phone, name, field, lede, Resume and LinkedIn all sit in the first screen. Two gaps hold the score down: no current status, and an ambiguous lead project.
- Fun and personality: 7/10. Moments: 99 s stamp, 404 joke, strike-through, "Fig. 1 / Orbits" plate, "For the record" ledger. I propose nothing new because the repo holds no further facts.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. The screenshots show no gradients, blur or glow.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). The subtitle reads "MS Mechanical Engineering, Carnegie Mellon University" and About lists 2023 to 2025. Today is 2026-11-11 and there is no status line. `STATUS = ""` at build/build.py:262, so the ledger omits its Status row. A recruiter cannot tell whether he has graduated, is working or is available. Only the owner can supply one line.
2. Major (UX, 30-second test). The lede and row 01 lead with snake robots, whose page states no result. "Start here" and the only plate sit on row 06 (46 orbits). Those are two answers to "strongest project" on one screen. Owner decision: move the label, or state a snake result.
3. Major (robustness). Images and the Resume link are hotlinked from Wix. Resume is the main recruiter action and appears in the header, the lede and the footer, so a Wix change breaks it everywhere at once. It needs a local `resume.pdf` and local photos from the owner. Not verifiable offline.
4. Major (credibility). The Raftar page says "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" (raftar-formula-racing.html, "The question" line, visible in the tablet screenshot) with no source or figure. The owner should source it or cut it.
5. Minor (SEO). `robots.txt` and `sitemap.xml` live under the `/website/` subpath. Crawlers read robots.txt only at the host root, so it is likely ignored. The sitemap works if submitted in Search Console, or with a custom domain. All lastmod values are identical. Not verifiable offline.
6. Minor (SEO, CLS). There is no per-project og:image, only the shared og.png. The Wix figures lack width/height, so shift is likely once they load (https://web.dev/optimize-cls/). Guessed ratios could make it worse, so this needs real dimensions. Google Fonts use `display=swap` with no size-adjusted fallback.
7. Minor (looks, taste). The plate appears on row 06 only. The bare rows beside it read thin, most visibly on desktop.
8. Minor (looks, taste). About has an empty right area on wide screens.
9. Minor (UX). Contact is LinkedIn only, the owner's choice but a single point of failure. The phone header drops Resume and GitHub, which stay in the lede and footer.
10. Nit (copy). Row blurbs share a verb-led cadence ("Trained...", "Landed...", "Compliant..."). Vary them only with facts already present.
11. Nit (looks). The small mono labels are the faintest text on tan and dark. They pass AA in check.py, so this is taste.

Designer-fixable this cycle: none. Regressions: none. The designer has declined these items for several cycles for good reasons (owner facts or files needed), so further identical cycles add no value until the owner replies.

## Good, must not regress
- The retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- The struck-through "three weeks" on amber, and the stamps (46 orbits, 500 m, 99 s, podium).
- The Fig. 1 plate with its "Sheet n of 9" caption and honest "schematic" notes.
- The plain first-person lede with real specifics, and no slogan copy.
- Failed images collapse cleanly. The pager shows the neighbour's first fact.
- One h1 per page, unique titles, JSON-LD, canonical, the 404 joke, skip link, 44 px targets, reduced-motion handling and scroll-padding under the sticky header.
- About's ruled, dated education and experience entries.

## Verdict
The site is authored, coherent and not generic, and nothing has regressed. Every material item waits on the owner: a status line, a decision on the lead project, a sourced or cut Raftar claim, and a local Resume and images with real dimensions. Nothing designer-fixable remains. Research this cycle was search-result level only because page fetches were blocked.
