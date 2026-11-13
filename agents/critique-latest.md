# Critique, 2026-11-13 (cycle 129)

Rendering: `python3 tools/check.py . agents/shots` ran to completion (rc=0, zero FAIL; only "images not loaded, sandbox network" notes). I viewed index phone-light, index desktop-dark, about tablet-light, snake-robots phone-dark and aerobraking desktop-light. I did not open the other 73 screenshots. No site source has changed since cycle 121 (cycles 122 to 128 are log-only). I edited no site files.

## Sources consulted
Page fetching (WebFetch) is blocked again (permission request unanswered; not retried): web.dev Optimize CLS. WebSearch returned only result listings with no page text, so I have read no source page this cycle. The links are search-confirmed to exist; my findings rest on the repo and screenshots. The three-source rule is not met; environment limit.
- web.dev, Optimize CLS (fetch blocked): https://web.dev/articles/optimize-cls
- web.dev, Preload responsive images (search result): https://web.dev/preload-responsive-images/
- web.dev, CSS size-adjust for @font-face (search-confirmed earlier): https://web.dev/articles/css-size-adjust
- WCAG 2.2 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Hiring-manager portfolio article (search only): https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/

## Scores
- AI-tell: 2/10, unchanged. Paper palette, ruled project list, stamps, struck-through "three weeks" on amber, mono "For the record" sidebar, plain first-person copy. The only remaining tell is the familiar shape (intro, list, dark footer). No tell moved.
- Looks good: 8/10, unchanged. Desktop dark home is calm and well measured; phone home reads cleanly; About is tidy. Weak spots: row 06 is the only plate; rows 02, 03, 08, 09 carry no mark; About leaves empty space on desktop; the snake page has a single schematic and short text.
- SEO: 7/10, unchanged. Unique titles, canonical, JSON-LD, absolute og.png with dimensions and alt, twitter card, sitemap, 404. Held down by robots.txt and sitemap under the /website/ subpath, all 12 lastmod values identical (2026-11-02), one shared og card. Not verifiable offline: indexing, real LCP.
- UX: 6/10, unchanged. Name, field, lede, Resume and LinkedIn are in the first phone screen. Held down by no status line (build/build.py:262 `STATUS = ""`), two answers to "best project", project pages with no role or outcome, and a single contact route.
- Fun and personality: 7/10, unchanged. 99 s stamp, struck-through "three weeks", sheet numbers, 404 joke. Nothing new has been added since.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. No gradient, blur or glow in the viewed light or dark shots.
2. Not AI-looking: met in visuals and copy. Do not regress.
No new owner notes.

## Ranked findings
1. Major (UX, credibility). Stale dates, no status. Home says "MS Mechanical Engineering, Carnegie Mellon University"; About says the Master's ran 2023 to 2025 and the latest job is Aug 2024; today is 2026-11-13. A recruiter cannot tell whether he is a student, graduated, employed or open to work. Owner supplies one line for STATUS.
2. Major (credibility). The aerobraking page ("Start here") says "This project builds off work done by Falcone et al." and the Method section describes their cluster and training, but nowhere states what Karthik did. A professor will read it as a summary of someone else's paper. Owner fact: "I did X; Falcone et al. did Y".
3. Major (UX). Two answers to "strongest project". The lede and row 01 lead with snake robots, whose page (phone-dark shot) has a schematic and a one-paragraph rationale ("Why snake robots") but no result or role. The "Start here" label and the only plate sit on row 06. Owner decision: add a snake result, or move the label and plate to the top.
4. Major (robustness, performance). 30 `wixstatic` hotlinks remain across 9 pages (aerobraking 7, sysid 5, tricycle 4, nanosatellite 4, submarine 4), plus the Resume PDF on filesusr.com, linked from the header, lede and footer. The aerobraking hero `<img>` has `fetchpriority="high"` and no width/height (CLS and third-party LCP risk, unverified offline). Google Fonts with no metric-matched fallback. A Wix change would break the Resume link everywhere at once. Needs owner files: local images with real dimensions, resume.pdf, WOFF2.
5. Major (credibility). Raftar page: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" is unsourced. Cite or cut. Owner fact.
6. Minor (UX, taste). Nine equal-weight rows; a "Selected" three above "Also" would help a skimmer. Owner picks.
7. Minor (SEO). robots.txt and sitemap live under /website/, where crawlers ignore robots.txt; submit the sitemap in Search Console. Identical lastmod on all pages; one og.png for every page.
8. Minor (content). Rows 02, 03, 08, 09 have no number or role. Owner facts.
9. Minor (looks, taste). Long text-only stretches in aerobraking Problem and Setup; the page is about 2,000 px of unbroken prose between the plate and the pager.
10. Nit (looks). About: empty space on wide screens; the small mono labels are the faintest text (they pass AA in check.py).
11. Nit (copy). Row blurbs share a verb-led cadence.

Designer-fixable this cycle: nothing without inventing facts. Findings 1 to 5 are owner decisions or owner files. The loop has been a no-op since cycle 122; more cycles add nothing until the owner answers.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plate with "Sheet n of 9" caption and honest "schematic" notes.
- Plain first-person lede with real specifics; no slogans.
- Aerobraking structure and pager showing the neighbour's first fact.
- Failed images collapse cleanly; one h1 per page; unique titles; JSON-LD; canonical; 404 joke; skip link; focus-visible and reduced-motion handling; 320 px header fix; 44 px targets on the phone nav and filter row.

## Verdict
The site is authored, coherent and not generic, and I found no regression. What holds it back is content only the owner can supply: a status line, a sentence separating his work from Falcone et al., one answer to "best project", a sourced or cut Raftar claim, and local Resume, images and fonts with real dimensions. Caveats: no source page was actually read this cycle (fetch blocked), and I viewed five of 78 screenshots.
