# Critique, 2026-11-11 (cycle 117)

Rendering: `python3 tools/check.py . agents/shots` completed this cycle (rc clean, every page OK, only "images not loaded, sandbox network" notes). I viewed index phone light, index desktop light and snake-robots phone dark. I edited no site files. HEAD is 4ec5814 (log-only), so site source is unchanged since cycle 108 and I found no regression.

## Sources consulted
Note for cycle 117: a WebFetch of the NN/g portfolio-content article was blocked by the permission system (https://www.nngroup.com/articles/portfolio-content/), so no new page was read this cycle. The sources below are carried over from cycle 116 and remain search-result level only. New observations this cycle come from the screenshots and repo, not from new research.
WebSearch worked this cycle and WebFetch was not used, so I saw result titles and URLs only. I did not read these pages in full. Treat them as pointers.
- Google, robots.txt creation and location: https://developers.google.com/crawling/docs/robots-txt/create-robots-txt . Search Engine Journal on whether robots.txt must sit at the domain root: https://www.searchenginejournal.com/you-dont-need-robots-txt-on-root-domain-says-google/521382/ . I could not confirm the details of that article. The long-standing rule is that crawlers read robots.txt only at the host root.
- Sitemap storage location: https://searchengineland.com/sitemapsorg-update-you-can-now-store-your-xml-sitemap-files-anywhere-13476
- web.dev, Optimize Cumulative Layout Shift (width/height on images, font fallbacks): https://web.dev/optimize-cls/
- Carried over from earlier cycles and still unverified: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html , https://developers.google.com/search/docs/appearance/structured-data/profile-page
- Topic this cycle: robots.txt and sitemap handling for GitHub project-site subpaths, and CLS. Next cycle could cover the NN/g portfolio content guidance or dark-mode contrast.

## Scores
- AI-tell: 2/10, unchanged. The paper tone, grain, double rules, one hard-offset button, struck-through "three weeks" on amber, rotated stamps, mono ledger and the DM Serif and Source Serif pairing look authored. The copy is plain first person. The residual tell is the familiar overall shape (intro, ruled list, dark footer). No tell moved.
- Looks good: 8/10. Desktop dark home has good rhythm, a clear measure and a strong first impression. About on tablet is tidy. Weak spots: the lone plate on row 06 beside bare rows, and the empty right area on wide About.
- SEO: 7/10. Unchanged. See findings 5 and 6.
- UX: 6/10. On the phone, name, field, lede, Resume and LinkedIn all sit in the first screen. Two gaps hold the score down: no current status, and an ambiguous lead project.
- Fun and personality: 7/10. Moments: the 99 s stamp, the 404 joke, the strike-through, the "Fig. 1 / Orbits" plate and the "For the record" ledger. I propose nothing new because the repo holds no further facts.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. The three screenshots show no gradients, blur or glow.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). The subtitle reads "MS Mechanical Engineering, Carnegie Mellon University", and About lists "2023 – 2025". Today is 2026-11-11 and there is no status line. `STATUS = ""` at build/build.py:262, so the ledger shows only Built, Internships and Toolbox. A recruiter cannot tell whether he has graduated, is working or is available. This is the biggest content gap. Only the owner can supply one line.
2. Major (UX, 30-second test). The lede and row 01 lead with snake robots, whose page states no result. "Start here" and the only plate sit on row 06 (46 orbits). Those are two answers to "strongest project" in one screenshot. Owner decision: move the label, or state a snake result.
3. Major (robustness). Images and the Resume link are hotlinked from Wix. Resume is the main recruiter action and appears in the header, the lede and the footer. If Wix drops the file, it fails on every page at once. It needs a local `resume.pdf` and local photos from the owner. This cannot be verified offline.
4. Major (credibility). The Raftar page says "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" (raftar-formula-racing.html:48), with no source or figure. The owner should source it or cut it.
5. Minor (SEO). `robots.txt` and `sitemap.xml` live under the `/website/` subpath. Crawlers read robots.txt only at the host root, so it is likely ignored. The sitemap works if submitted in Search Console, so the owner should do that or use a custom domain. Every lastmod is identical. Not verifiable offline.
6. Minor (SEO, CLS). There is no per-project og:image, only the shared og.png. The Wix figures lack width/height, so shift is likely once they load (https://web.dev/optimize-cls/). Guessed ratios could make it worse, so this needs real dimensions. Google Fonts use `display=swap` with no size-adjusted fallback.
7. Minor (looks, taste). The plate appears on row 06 only, and the bare rows next to it read thin. The 1366 px dark shot shows this clearly.
8. Minor (looks, taste). About has an empty right area on wide screens.
9. Minor (UX). Contact is LinkedIn only. This is the owner's choice but a single point of failure. The phone header drops Resume and GitHub, which stay in the lede and footer.
10. Nit (copy). The row blurbs share a verb-led cadence ("Trained...", "Landed...", "Compliant..."). Vary them only with facts already present.
11. Nit (looks). The small mono labels are the faintest text on tan and dark. They pass AA in check.py, so this is taste.

New observation (Nit, taste): on the snake-robots phone page the Fig. 1 plate is a generic sine-wave schematic and the page body is two short paragraphs, so the lead project (row 01) has the thinnest page and the least evidence. This reinforces finding 2: either state a result or move 'Start here' to the project that has one. Also confirmed: STATUS is still empty (build/build.py:262).

Designer-fixable this cycle: none. Regressions: none.

## Good, must not regress
- The retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- The struck-through "three weeks" on amber, and the stamps (46 orbits, 500 m, 99 s, podium).
- The Fig. 1 plate with its "Sheet n of 9" caption, with honest "schematic" notes.
- The plain first-person lede with real specifics, and no slogan copy.
- Failed images collapse cleanly. The pager shows the neighbour's first fact.
- One h1 per page, unique titles, JSON-LD, canonical, the 404 joke, skip link, 44 px targets, reduced-motion handling and scroll-padding under the sticky header.
- About's ruled, dated education and experience entries.

## Verdict
The site is authored, coherent and not generic, and nothing has regressed since cycle 113. Every material item waits on the owner: a status line, a decision on the lead project, a sourced or cut Raftar claim, and a local Resume and images with real dimensions. Nothing designer-fixable remains. Research this cycle was search-result level only, with no page read in full.
