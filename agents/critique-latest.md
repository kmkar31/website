# Critique, 2026-11-11 (cycle 119)

Rendering: `python3 tools/check.py . agents/shots` completed, every page OK, only "images not loaded, sandbox network" notes. I viewed index phone light, index desktop dark, snake-robots phone light and about tablet dark. HEAD is acf8cc5 (log-only), so site source is unchanged since cycle 117 and I found no regression. I edited no site files.

## Sources consulted
Only WebSearch was used. I did not open any page in full, so these are result-level pointers, not verified quotes.
- web.dev, Optimize Cumulative Layout Shift: https://web.dev/articles/optimize-cls
- web.dev Learn Images, key performance issues: https://web.dev/learn/images/performance-issues
- Google Search Central, robots.txt creation: https://developers.google.com/crawling/docs/robots-txt/create-robots-txt
- Portfolio and recruiter search results (secondary, not primary, treated as weak evidence): https://www.toptal.com/designers/ux/ux-portfolio-tips-recruiter , https://blog.uxfol.io/ux-portfolio-features/
- Topic this cycle: CLS and image loading, robots.txt placement, recruiter scanning. Local check: robots.txt sits at the repo root, so on github.io it is served under /website/, not the host root.

## Scores
- AI-tell: 2/10, unchanged. Paper tone, grain, double rules, hard-offset button, struck-through "three weeks" on amber, stamps, mono ledger and serif pairing read as authored. Copy is plain first person. Residual tell is the familiar shape (intro, ruled list, dark footer). No tell moved.
- Looks good: 8/10. Desktop dark home has clear measure and rhythm. About tablet dark is well ordered. Weak spots: the lone plate on row 06, and the empty area under the ledger on desktop.
- SEO: 7/10, unchanged (findings 5 and 6).
- UX: 6/10. Name, field, lede, Resume and LinkedIn fit in the first phone screen. Held down by no current status and an ambiguous lead project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, "Fig. 1 / Orbits" plate, "For the record". I propose nothing new because the repo holds no further facts.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Screenshots show no gradient, blur or glow.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Subtitle says "MS Mechanical Engineering, Carnegie Mellon University" and About says 2023 to 2025. Today is 2026-11-11 and no status line exists (`STATUS = ""` in build/build.py). A visitor cannot tell whether he has graduated, is working, or is available. Owner must supply one line.
2. Major (UX, 30-second test). Lede and row 01 lead with snake robots, whose page (snake-robots phone screenshot) states no result, only a question and a schematic. "Start here" and the only plate sit on row 06. Two answers to "strongest project" on one screen. Owner decision: move "Start here", or state a snake result.
3. Major (robustness). Images and the Resume link are hotlinked from Wix. Resume is the main recruiter action and appears in the header, lede and footer, so one Wix change breaks all three. Needs a local resume.pdf and local photos from the owner. Not verifiable offline.
4. Major (credibility). The Raftar page says "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" with no source. Owner should source or cut it.
5. Minor (SEO). robots.txt and sitemap.xml live under the /website/ subpath; Google reads robots.txt at the host root only (https://developers.google.com/crawling/docs/robots-txt/create-robots-txt), so it is likely ignored. The sitemap works if submitted in Search Console or on a custom domain. All lastmod values are identical. Not verifiable offline.
6. Minor (SEO, CLS). No per-project og:image, only the shared og.png. Wix figures lack width/height, so shift is likely once they load (https://web.dev/articles/optimize-cls). Guessed ratios could make it worse; needs real dimensions. Google Fonts use swap with no size-adjusted fallback.
7. Minor (looks, taste). The plate appears on row 06 only; bare rows beside it read thin, most visibly on desktop.
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
The site is authored, coherent and not generic, and nothing has regressed. All material items wait on the owner: a status line, a decision on the lead project, a sourced or cut Raftar claim, and a local Resume and images with real dimensions. Nothing designer-fixable remains. Research this cycle was search-result level only.
