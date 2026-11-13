# Critique, 2026-11-13 (cycle 128)

Rendering: `python3 tools/check.py . agents/shots` ran to completion (zero FAIL; only "images not loaded, sandbox network" notes). I viewed index phone-light, index desktop-light and projects phone-dark. I did not open the other 75 screenshots. `git status` is clean and no site source changed since cycle 121 (cycles 122 to 127 are log-only). I edited no site files.

## Sources consulted
Page fetching (WebFetch) was blocked again this cycle (permission request unanswered; not retried): web.dev Optimize LCP and the WCAG 2.5.8 Understanding page. WebSearch worked but returned only result listings (titles and URLs), no page text. So I have read NO source pages; the links below are search-confirmed to exist, and my findings rest on the repo and screenshots, not on them. The three-sources rule is not met; environment limit.
- WCAG 2.2 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- web.dev, CSS size-adjust for @font-face: https://web.dev/articles/css-size-adjust
- web.dev, Optimize CLS: https://web.dev/articles/optimize-cls
- Hiring-manager portfolio articles surfaced by search (not opened): https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/ , https://measuringu.com/what-hiring-managers-want-and-what-ux-practitioners-do/

## Scores
- AI-tell: 2/10, unchanged. Paper palette, ruled list, stamps, struck-through "three weeks" on amber, mono "For the record" sidebar, graph-paper plate, plain first-person copy. Remaining tell is the familiar shape (intro, list, dark footer). No tell moved.
- Looks good: 8/10, unchanged. Desktop home is calm and well measured; phone home reads cleanly. Weak spots: one plate in the list (row 06, the others are text only); rows 02, 03, 08, 09 carry no mark; About's right side is empty on desktop.
- SEO: 7/10, unchanged. Unique titles, canonical, JSON-LD, local og.png, sitemap, 404. Held down by subpath robots.txt, identical lastmod, one shared og card. Not verifiable offline: indexing, real LCP.
- UX: 6/10, unchanged. Name, field, lede, Resume and LinkedIn are in the first phone screen. Held down by no status line, two answers to "best project", and project pages with no role or outcome.
- Fun and personality: 7/10, unchanged. 99 s stamp, struck-through "three weeks", sheet numbers, 404 joke.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. No gradient, blur or glow in the viewed light or dark shots.
2. Not AI-looking: met in visuals and copy. Do not regress.
No new owner notes.

## Ranked findings
1. Major (UX, credibility). Stale dates, no status. `STATUS = ""` (build/build.py:262), so the sidebar omits it. Home says "MS Mechanical Engineering, Carnegie Mellon University"; About says the Master's ran 2023 to 2025; today is 2026-11-13. A recruiter cannot tell whether he is a student, graduated, employed or open to work. Owner supplies one line.
2. Major (credibility). Aerobraking ("Start here") reads as Falcone et al.'s work and never states what Karthik did. Owner fact: "I did X; Falcone et al. did Y".
3. Major (UX). Two answers to "strongest project". Lede and row 01 lead with snake robots, whose page has a schematic and a one-paragraph rationale but no result or role. The "Start here" label and the only plate sit on row 06 (seen in the desktop and phone screenshots). Owner decision: add a snake result, or move the label and plate to the top.
4. Major (robustness, performance). About 26 `wixstatic` hotlinks remain plus the Resume PDF; the hero `<img>` on aerobraking has `fetchpriority="high"` and no width/height (CLS and third-party LCP risk, unverified offline); Google Fonts with no metric-matched fallback (size-adjust, see web.dev link above). Needs owner files: local images with real dimensions, resume.pdf, WOFF2.
5. Major (credibility). Raftar page: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" is unsourced. Cite or cut. Owner fact.
6. Minor (UX, taste). Nine equal-weight rows; a "Selected" three above "Also" would help a skimmer. Owner picks.
7. Minor (SEO). robots.txt and sitemap live under /website/, where Google ignores robots.txt; submit the sitemap in Search Console. Same lastmod everywhere; one og.png.
8. Minor (content). Rows 02, 03, 08, 09 have no number or role. Owner facts.
9. Minor (looks, taste). Long text-only stretches in aerobraking Problem and Setup.
10. Nit (looks). About: empty lower right on wide screens; ragged Skills columns; the small mono labels are the faintest text (pass AA in check.py).
11. Nit (copy). Row blurbs share a verb-led cadence.

Designer-fixable this cycle: nothing without inventing facts. Findings 1 to 5 are owner decisions or owner files. The loop has been a no-op for seven cycles; more cycles add nothing until the owner answers.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plate with "Sheet n of 9" caption and honest "schematic" notes.
- Plain first-person lede with real specifics; no slogans.
- Aerobraking structure and pager showing the neighbour's first fact.
- Failed images collapse cleanly; one h1 per page; unique titles; JSON-LD; canonical; 404 joke; skip link; focus-visible and reduced-motion handling; 320 px header fix; projects filter row has 44 px targets on phone.

## Verdict
The site is authored, coherent and not generic, and I found no regression. What holds it back is content only the owner can supply: a status line, a sentence separating his work from Falcone et al., one answer to "best project", a sourced or cut Raftar claim, and local Resume, images and fonts with real dimensions. Caveats: no source page was actually read this cycle (fetch blocked), and I viewed three of 78 screenshots.
