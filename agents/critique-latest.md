# Critique, 2026-11-13 (cycle 127)

Rendering: `python3 tools/check.py . agents/shots` ran to completion (all OK; only "images not loaded, sandbox network" notes; about 8 minutes). I viewed index phone-light, index desktop-dark, snake-robots tablet-light and about desktop-light. I did not open the other 60 screenshots; no site source has changed since cycle 121 (git log shows cycles 122 to 126 are log-only commits). I edited no site files except this one.

## Sources consulted
Web fetch was blocked this cycle (permission request unanswered, so I did not retry): w3.org WCAG 2.2 Target Size (Minimum), web.dev Optimize LCP, and nngroup.com mobile UX. I therefore opened NO sources. These are pointers only, unverified, and the findings rest on the repo and screenshots:
- WCAG 2.2 Target Size: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- web.dev Optimize LCP: https://web.dev/articles/optimize-lcp
- NN/g mobile UX: https://www.nngroup.com/articles/mobile-ux/
This misses the three-sources rule; environment limit, not a choice.

## Scores
- AI-tell: 2/10, unchanged. Paper palette, ruled list, stamps, struck-through "three weeks" on amber, mono "For the record" sidebar, graph-paper plate, plain first-person copy. Remaining tell is the familiar shape (intro, list, dark footer). No tell moved.
- Looks good: 8/10. Desktop dark home is calm and well measured; phone home reads cleanly. Weak spots: one plate in the list (row 06); rows 02, 03, 08, 09 carry no mark; About's right side is empty below the "On this page" box on desktop; Skills columns are ragged (5/3/3 items).
- SEO: 7/10. Unique titles, canonical, JSON-LD, local og.png, sitemap, 404. Held down by subpath robots.txt, identical lastmod, one shared og card.
- UX: 6/10. Name, field, lede, Resume, LinkedIn in the first phone screen. Held down by no status line, two answers to "best project", pages with no role or outcome.
- Fun and personality: 7/10. 99 s stamp, struck-through "three weeks", sheet numbers, 404 joke.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. No gradient, blur or glow in viewed light or dark shots.
2. Not AI-looking: met in visuals and copy. Do not regress.
No new owner notes.

## Ranked findings
1. Major (UX, credibility). Stale dates, no status. `STATUS = ""` (build/build.py:262), so the sidebar omits it. Home says "MS Mechanical Engineering, Carnegie Mellon University"; About says the Master's ran 2023 to 2025; today is 2026-11-13. A recruiter cannot tell whether he is a student, graduated, employed or open to work. Owner supplies one line.
2. Major (credibility). Aerobraking ("Start here") reads as Falcone et al.'s work and never states what Karthik did. Owner fact: "I did X; Falcone et al. did Y".
3. Major (UX). Two answers to "strongest project". Lede and row 01 lead with snake robots, whose page (viewed, tablet) has a schematic, a one-paragraph "Why snake robots" and no result or role; the "Start here" label and the only plate sit on row 06. Owner decision: add a snake result or move the label and plate to the top.
4. Major (robustness, performance). About 26 `wixstatic` hotlinks remain plus the Resume PDF; hero `<img>` on aerobraking has `fetchpriority="high"` and no width/height (CLS and third-party LCP risk, unverified offline); Google Fonts without metric-matched fallback. Needs owner files: local images with real dimensions, resume.pdf, WOFF2.
5. Major (credibility). Raftar page: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" is unsourced. Cite or cut. Owner fact.
6. Minor (UX, taste). Nine equal-weight rows; a "Selected" three above "Also" would help a skimmer. Owner picks.
7. Minor (SEO). robots.txt and sitemap live under /website/, where Google ignores robots.txt; submit the sitemap in Search Console. Same lastmod everywhere; one og.png.
8. Minor (content). Rows 02, 03, 08, 09 have no number or role. Owner facts.
9. Minor (looks, taste). Long text-only stretches in aerobraking Problem and Setup.
10. Nit (looks). About: empty lower right on wide screens; ragged Skills columns; the small mono labels are the faintest text (pass AA in check.py).
11. Nit (copy). Row blurbs share a verb-led cadence.

Designer-fixable this cycle: nothing without inventing facts. Findings 1 to 5 are owner decisions or owner files. The loop has been a no-op for six cycles; further cycles add nothing until the owner answers.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plates with "Sheet n of 9" captions and honest "schematic" notes.
- Plain first-person lede with real specifics; no slogans.
- Aerobraking structure and pager showing the neighbour's first fact.
- Failed images collapse cleanly; one h1 per page; unique titles; JSON-LD; canonical; 404 joke; skip link; focus-visible and reduced-motion handling; 320 px header fix.

## Verdict
The site is authored, coherent and not generic, and I found no regression. What holds it back is content only the owner can supply: a status line, a sentence separating his work from Falcone et al., one answer to "best project", a sourced or cut Raftar claim, and local Resume, images and fonts with real dimensions. Caveats: web research was blocked this cycle, and I viewed four of 72 screenshots.
