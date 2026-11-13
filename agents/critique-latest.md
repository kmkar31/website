# Critique, 2026-11-13 (cycle 130)

Rendering: `python3 tools/check.py . agents/shots` ran to completion (rc=0, zero FAIL; only "images not loaded, sandbox network" notes). I viewed index tablet-light, raftar-formula-racing phone-light and projects desktop-light (different from last cycle's set). I did not open the other 75 screenshots. `git status` is clean and no site source has changed since cycle 121 (later cycles are log-only). I edited no site files.

## Sources consulted
I read no source page this cycle. The WebSearch/WebFetch tools were not loaded in this run, so I did no fresh research; the three-source rule is not met (environment limit, not a choice). The links below are the same pointers as last cycle, not re-read, and my findings rest on the repo and screenshots, not on them.
- web.dev, Optimize CLS: https://web.dev/articles/optimize-cls
- web.dev, CSS size-adjust for @font-face: https://web.dev/articles/css-size-adjust
- WCAG 2.2 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html

## Scores
- AI-tell: 2/10, unchanged. Paper palette, ruled list, tilted stamps, struck-through "three weeks" on amber, mono "For the record" ledger, plain first-person copy. Remaining tell: the familiar shape (intro, list, dark footer). No tell moved.
- Looks good: 8/10, unchanged. Tablet home is calm and well measured; Raftar phone page has a clear hierarchy (title, tldr, fact pair, plate). Weak spots: row 06 is the only row with a plate; rows 02, 03, 08, 09 carry no mark; the Raftar page is short (two facts, one paragraph, link out).
- SEO: 7/10, unchanged. Unique titles, canonical, JSON-LD, absolute og.png, sitemap, 404. Held down by robots.txt and sitemap under the /website/ subpath, all 12 lastmod values identical (2026-11-02), one shared og card. Real indexing and LCP are not verifiable offline.
- UX: 6/10, unchanged. Name, field, lede, Resume and LinkedIn are in the first phone screen. Held down by no status line (build/build.py:262 `STATUS = ""`), two answers to "best project", project pages with no role or outcome, one contact route.
- Fun and personality: 7/10, unchanged. 99 s stamp, struck-through "three weeks", sheet numbers, 404 joke. Nothing new since.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. No gradient, blur or glow in the viewed shots.
2. Not AI-looking: met in visuals and copy. Do not regress.
No new owner notes.

## Ranked findings
1. Major (UX, credibility). Stale dates, no status. Home says "MS Mechanical Engineering, Carnegie Mellon University" with no year (tablet shot); About says the Master's ran 2023 to 2025; today is 2026-11-13. A recruiter cannot tell whether he is a student, graduated, employed or open to work. Owner supplies one line for STATUS.
2. Major (credibility). The aerobraking page ("Start here") says it builds off Falcone et al. and describes their method, but nowhere states what Karthik did. A professor will read it as a summary of someone else's paper. Owner fact needed: "I did X; Falcone et al. did Y".
3. Major (UX). Two answers to "strongest project". The lede and row 01 lead with snake robots (page has a schematic and one rationale paragraph, no result or role), while the "Start here" label and the only plate sit on row 06 (visible in the tablet shot). Owner decision: add a snake result, or move label and plate to the top.
4. Major (robustness, performance). `wixstatic` hotlinks remain: aerobraking 7, sysid 5, tricycle 4, nanosatellite 4, submarine 4, landing 2, plus about, argus, projects, raftar, snake 1 each (grep count of lines). The Resume PDF is on filesusr.com and linked from header, lede and footer on every page, so one Wix change breaks it everywhere. Images have no known width/height (CLS risk, unverified offline). Google Fonts with no metric-matched fallback. Needs owner files: local images with dimensions, resume.pdf, WOFF2.
5. Major (credibility). Raftar page: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" (seen on the phone shot) is unsourced. Cite or cut. Owner fact.
6. Minor (credibility, UX). Raftar page says what he did in one clause ("suspension and brakes") but gives no number, test or result beyond the podium; it is the thinnest page next to snake. Owner facts.
7. Minor (UX, taste). Nine equal-weight rows on Home and Projects; Projects (desktop shot) repeats Home almost exactly, so the second page adds only filters. A "Selected" three above "Also" would help a skimmer. Owner picks.
8. Minor (SEO). robots.txt and sitemap live under /website/, where crawlers do not read robots.txt; submit the sitemap in Search Console. Identical lastmod on all pages; one og.png for every page.
9. Minor (content). Rows 02, 03, 08, 09 have no number or role. Owner facts.
10. Nit (looks, taste). Long text-only stretches in aerobraking Problem and Setup; About leaves empty space on wide screens.

Designer-fixable this cycle: nothing without inventing facts. Findings 1 to 6 are owner decisions or files. The loop has been a no-op since cycle 122.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plate with "Sheet n of 9" caption and honest "schematic" notes.
- Plain first-person lede with real specifics; no slogans.
- Aerobraking structure; pager showing the neighbour's first fact.
- Failed images collapse cleanly; one h1 per page; unique titles; JSON-LD; canonical; 404 joke; skip link; focus-visible and reduced-motion handling; 44 px targets on the phone nav and filter row.

## Verdict
The site is authored, coherent and not generic, and I found no regression. What holds it back is content only the owner can supply: a status line, a sentence separating his work from Falcone et al., one answer to "best project", a sourced or cut Raftar claim, and local Resume, images and fonts with real dimensions. Caveats: no source page was read this cycle (research tools unavailable), and I viewed three of 78 screenshots.
