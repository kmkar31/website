# Critique, 2026-11-11 (cycle 120)

Rendering: `python3 tools/check.py . agents/shots` completed. Every page is OK, with only "images not loaded, sandbox network" notes. HEAD is 2fd6ab8 (log-only), so site source is unchanged since cycle 117 and I found no regression. I viewed index phone light, index desktop dark and raftar-formula-racing phone light. I edited no site files.

## Sources consulted
WebFetch was blocked this cycle, so the sources below are search-result pointers only. I did not read them in full and they are not verified quotes.
- WCAG 2.2, Understanding 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (24 CSS px minimum; the site's 44 px targets exceed it)
- web.dev, Optimize web fonts: https://web.dev/learn/performance/optimize-web-fonts and CSS size-adjust: https://web.dev/css-size-adjust/ (size-adjusted fallbacks reduce font-swap CLS)
- web.dev, Optimize CLS: https://web.dev/articles/optimize-cls and Google robots.txt docs: https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt (blocked, not opened)
- Portfolio and hiring-manager results (secondary, weak evidence): https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/ , https://measuringu.com/what-hiring-managers-want-and-what-ux-practitioners-do/
- Topics this cycle: target size, font-swap CLS, hiring-manager scanning.

## Scores
- AI-tell: 2/10, unchanged. Paper tone, double rules, hard-offset button, struck-through "three weeks" on amber, stamps, mono ledger and serif pairing read as authored. Copy is plain first person. The remaining tell is the familiar shape (intro, ruled list, dark footer). No tell moved.
- Looks good: 8/10. The desktop dark home has a clear measure and rhythm. The Raftar phone page is well ordered, with a clean plate and caption. Weak spots: the lone plate on row 06, and bare rows beside it.
- SEO: 7/10, unchanged (findings 5 and 6).
- UX: 6/10. Name, field, lede, Resume and LinkedIn fit in the first phone screen. Held down by no current status and an ambiguous lead project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, "Fig. 1 / Orbits" plate, "For the record". I propose nothing new because the repo holds no further facts.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. The screenshots show no gradient, blur or glow.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). The subtitle says "MS Mechanical Engineering, Carnegie Mellon University" and About says 2023 to 2025. Today is 2026-11-11 and there is no status line (`STATUS = ""` in build/build.py). A visitor cannot tell whether he has graduated, is working or is available. The owner must supply one line.
2. Major (UX, 30-second test). The lede and row 01 lead with snake robots, whose page states no result. "Start here" and the only plate sit on row 06. That gives two answers to "strongest project" on one screen (phone and desktop). Owner decision: move "Start here", or state a snake result.
3. Major (robustness). Images and the Resume link are hotlinked from Wix. Resume is the main recruiter action and appears in the header, lede and footer, so one Wix change breaks all three. It needs a local resume.pdf and local photos from the owner. Not verifiable offline.
4. Major (credibility). The Raftar page (phone screenshot, "The question") says "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" with no source. The owner should source or cut it.
5. Minor (SEO). robots.txt and sitemap.xml are served under the /website/ subpath. Google reads robots.txt at the host root only, so it is probably ignored; I could not open the doc this cycle, so this is from memory of the spec. The sitemap works if submitted in Search Console or on a custom domain. All lastmod values are identical.
6. Minor (SEO, CLS). There is no per-project og:image, only the shared og.png. Wix figures lack width/height, so shift is likely once they load. Google Fonts use swap with no size-adjusted fallback (web.dev size-adjust). Guessed ratios could make it worse; real dimensions are needed.
7. Minor (looks, taste). The plate appears on row 06 only; the bare rows read thin, most visibly on desktop.
8. Minor (looks, taste). About has an empty right area on wide screens.
9. Minor (UX). Contact is LinkedIn only, a single point of failure (owner's choice). The phone header drops Resume and GitHub; they remain in the lede and footer.
10. Nit (copy). Row blurbs share a verb-led cadence ("Trained...", "Landed...", "Compliant..."). Vary only with facts already present.
11. Nit (looks). Small mono labels are the faintest text on tan and dark. They pass AA in check.py, so this is taste.

Designer-fixable this cycle: none. Regressions: none. Every open item needs the owner (status line, lead project, Raftar claim, local Resume and images). Further identical cycles add little until the owner replies.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber, and the stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plate with "Sheet n of 9" caption and honest "schematic" notes.
- Plain first-person lede with real specifics, no slogan copy.
- Failed images collapse cleanly; the pager shows the neighbour's first fact.
- One h1 per page, unique titles, JSON-LD, canonical, 404 joke, skip link, 44 px targets, reduced-motion handling, scroll-padding under the sticky header.
- About's ruled, dated education and experience entries.

## Verdict
The site is authored, coherent and not generic, and nothing has regressed. All material items wait on the owner: a status line, a decision on the lead project, a sourced or cut Raftar claim, and a local Resume and images with real dimensions. Nothing designer-fixable remains. Research this cycle was search-result level only because page fetches were blocked.
