# Critique, 2026-11-11 (cycle 115)

Rendering: `python3 tools/check.py . agents/shots` ran (needs more than 2 minutes; run it in the background). No FAIL, only "images not loaded, sandbox network" notes. I viewed index desktop light, raftar phone light and projects tablet dark. No site files edited. No source change since cycle 113 (last commit is a log-only commit), so there is no regression to report.

## Sources consulted
- WebFetch was blocked again this cycle (permission request unanswered), for https://www.nngroup.com/articles/portfolios/ and earlier for the W3C, Google and MDN pages. No source was read in full this cycle, so the research requirement is not met. Nothing below depends on a source beyond well-known facts.
- Pointers only, carried from earlier cycles and unverified now: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html , https://developers.google.com/search/docs/appearance/structured-data/profile-page , https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion , https://web.dev/articles/fetch-priority , https://web.dev/optimize-cls
- Suggested topic for the next networked cycle: Google's guidance on robots.txt and sitemaps for project-site subpaths.

## Scores
- AI-tell: 2/10, unchanged. The paper tone, grain, double rules, one hard-offset button, struck-through "three weeks" on amber, rotated stamps, mono ledger and the serif pairing all look authored. The copy is plain first person. The residual tell is the familiar overall shape (intro, ruled list, dark footer). No tell moved.
- Looks good: 8/10. The desktop home has good rhythm and measure. Weak spots: the lone plate on row 06 beside bare rows 02, 03, 08 and 09, and the empty right third on About (desktop).
- SEO: 7/10. Unchanged. See findings 5, 6 and 7.
- UX: 6/10. Name, field, lede, Resume and LinkedIn all sit in the first phone screen. Two things hold the score down: there is no current status, and the lead project is ambiguous.
- Fun and personality: 7/10. Moments: the 99 s stamp, the 404 joke, the strike-through, the "Sheet n of 9 / NTS" captions and the "For the record" ledger. Nothing new is supported by repo facts, so I propose nothing invented.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. There are no gradients, blur or glow in any viewed shot.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). The subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" are read on 2026-11-11 with no status line. `STATUS = ""` in build/build.py, so the ledger shows only Built, Internships and Toolbox. A recruiter cannot tell whether he has graduated, is working or is available. This is the biggest content gap. The owner must supply one line.
2. Major (UX, 30-second test). The lede and row 01 lead with snake robots, whose page states no result. "Start here" and the only plate sit on row 06 (46 orbits). That is two answers to "strongest project", visible in the same screenshot. Owner decision: move the label, or state a snake result.
3. Major (robustness, media dependency). Images and the Resume link are hotlinked from Wix (`filesusr.com`, 11 pages reference `wixstatic`). Resume is the main recruiter action and appears in the header, the lede and the footer. If Wix drops the file, the primary call to action fails on every page at once. It needs a local `resume.pdf` and local photos from the owner. This cannot be verified offline.
4. Major (credibility). Raftar says "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" (raftar-formula-racing.html:48), with no source or figure on the page. A hiring manager may read it as unsupported. The owner should source it or cut it.
5. Minor (SEO). `robots.txt` and `sitemap.xml` live under the `/website/` subpath, and crawlers read robots.txt only at the host root. Every lastmod is identical (2026-11-02). The owner should submit the sitemap in Search Console or use a custom domain. Not verifiable offline.
6. Minor (SEO, CLS). There is no per-project og:image (only the shared og.png), and the Wix figures lack width/height, so layout shift is likely once they load. Guessed ratios could make this worse, so it needs real dimensions.
7. Minor (fonts, CLS). Two Google Fonts with `display=swap` and no size-adjusted fallback. It needs the real font metrics, or self-hosted WOFF2.
8. Minor (looks, taste). The plate appears on row 06 only, and bare rows beside it read thin. This is taste.
9. Minor (looks, taste). About has an empty right third below the "On this page" box on wide screens.
10. Minor (UX). Contact is LinkedIn only. This is the owner's constraint, but it is a single point of failure. The phone header drops Resume and GitHub, which remain in the lede and footer.
11. Nit (copy). The row blurbs share a verb-led cadence ("Trained...", "Landed...", "Compliant..."). Vary them only with facts already present.
12. Nit (looks). The small mono labels are the faintest text on tan. They pass AA in check.py, so this is a taste note.

Designer-fixable this cycle: none. Regressions: none.

## Good, must not regress
- The retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode (the projects tablet dark shot holds together well).
- The struck-through "three weeks" on amber, and the stamps (46 orbits, 500 m, 99 s, podium).
- The Fig. 1 plates with the "Sheet n of 9" caption, repo-local and honest "schematic" notes.
- The plain first-person lede with real specifics, and no slogan copy.
- Failed images collapse cleanly. The pager shows the neighbour's first fact. The pager has no wraparound.
- One h1 per page, unique titles, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets, reduced-motion handling and scroll-padding under the sticky header.
- The About page's ruled, dated education and experience entries.

## Verdict
Authored, coherent and not generic, with no regression since cycle 113. Every material item waits on the owner: a status line, a decision on the lead project, a sourced or cut Raftar claim, and local Resume and images with real dimensions. Nothing designer-fixable remains. The research behind this critique is thin because WebFetch was blocked again.
