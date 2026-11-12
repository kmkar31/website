# Critique, 2026-11-12 (cycle 123)

Rendering: `python3 tools/check.py . agents/shots` ran in the background (over 2 minutes) and finished with zero FAIL lines; only "images not loaded, sandbox network" notes. I viewed index (desktop light, phone dark), aerobraking-drl (desktop light) and projects (tablet light), and inspected the HTML and build.py. I edited no site files except this one.

## Sources consulted
WebFetch of web.dev was blocked again ("permission request not answered"), so I opened nothing. These are search-result pointers only; the principles are unverified until someone opens them.
- web.dev, Optimize Cumulative Layout Shift: https://web.dev/articles/optimize-cls (width/height or aspect-ratio on images)
- web.dev, Optimize web fonts: https://web.dev/learn/performance/optimize-web-fonts (font-display, fallback font metrics)
- Nielsen Norman Group, UX design portfolios: https://nngroup.com/articles/ux-design-portfolios/ (reviewers want to see your role, process and outcome per project)
- Search hit: Fixing layout shifts caused by web fonts: https://vincent.bernat.ch/en/blog/2024-cls-webfonts
Topics this cycle (new versus 122): font-swap CLS, "role and outcome" per project (NN/g), staleness of dated claims.

## Scores
- AI-tell: 2/10, unchanged. Paper palette, ruled list, stamps, struck-through "three weeks" on amber, mono ledger, graph-paper plate. Plain first-person copy. Remaining tell is only the familiar shape (intro, list, dark footer). No tell moved.
- Looks good: 8/10. Desktop home is calm and well measured; the aerobraking page now has headings, a plate, a facts strip and a ledger. Weak spots: one plate on the whole list (row 06), long text-only stretches in Problem and Setup, and rows 02, 03, 08, 09 carry no mark so the list is front-loaded visually in the middle.
- SEO: 7/10, unchanged. Titles, canonical, JSON-LD, local og.png, sitemap and 404 are in place. Held down by subpath robots.txt, identical lastmod (all 2026-11-02) and one shared og card.
- UX: 6/10, unchanged. Name, field, lede, Resume and LinkedIn all sit in the first phone screen. Held down by no status line, two answers to "best project", and no stated role or outcome on several pages.
- Fun and personality: 7/10, unchanged. 99 s stamp, 404 joke, strike-through, sheet numbers. The repo has no further facts to build on.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. No gradient, blur or glow in any screenshot, light or dark.
2. Not AI-looking: met in visuals and copy. Do not regress.
No new owner notes.

## Ranked findings
1. Major (UX, credibility). Stale dates with no status. `STATUS = ""` (build/build.py:262). The home subtitle reads "MS Mechanical Engineering, Carnegie Mellon University" and About says the Master's runs 2023 to 2025. Today is 2026-11-12, so the dates are in the past and a recruiter cannot tell if he is a student, graduated, employed or open to work. This is the single biggest lost conversion on the site. Owner supplies one line.
2. Major (credibility). Aerobraking, the page marked "Start here", reads as Falcone et al.'s work: Setup says it "builds off work done by Falcone et al."; Method says "Falcone et al. simulated their agent..."; Result then says "our NN state-space model". The page never states what Karthik did. NN/g's portfolio guidance is that reviewers look for the writer's own role and outcome. The plain sentence "I did X; Falcone et al. did Y" fixes it. Reopened: unchanged since cycle 121.
3. Major (UX). Two answers to "strongest project". The lede and row 01 lead with snake robots (no result on its page); the "Start here" label and plate sit on row 06. A 30-second reader sees "01" first and "Start here" six rows later. Owner decision: move the label to 01 only if the snake page gains a result; otherwise move the plate and label to the top of the list.
4. Major (robustness, performance). 76 hotlinks to wixstatic (aerobraking 18 matches, sysid 16, tricycle 16) plus the Resume PDF. None of the `<img>` tags I sampled has width/height, and the aerobraking hero figure has `fetchpriority="high"` but no dimensions, so layout shift is likely and LCP depends on a third-party host (web.dev optimize-cls, unverified pointer). Fonts also load from Google Fonts with no metric-matched fallback (web.dev font guidance, unverified pointer). Owner files needed: local images with real dimensions, resume.pdf, WOFF2.
5. Major (credibility). The Raftar page still has the "one-fifth the weight of a Ferrari but matches its 0-60 time" question with no source. Cite it or cut it. Owner fact.
6. Minor (UX, taste plus NN/g). Nine projects at equal weight in a list that is the whole front page. A "Selected" group of three above "Also" would help a skim reader; the owner picks three.
7. Minor (SEO). robots.txt and sitemap.xml live under /website/, where Google ignores robots.txt; submit the sitemap in Search Console. Every lastmod is the same date, which weakens the signal. Only one og.png for all pages.
8. Minor (content). Several rows have no concrete number or role: 02 ARGUS, 03 Landing, 08 Grey-box, 09 Tricycle. Not fixable without owner facts; flagged so it stays visible.
9. Minor (looks, taste). Text-only middle of long project pages (aerobraking Problem and Setup are about 25 lines of paper-style prose). A pull-quote or a figure break would help but needs real content.
10. Nit (looks). About has empty space at lower right on wide screens; the small mono labels are the faintest text (pass AA).
11. Nit (copy). Row blurbs share a verb-led cadence.

Designer-fixable this cycle: nothing without inventing facts. All items above need the owner.

## Good, must not regress
- The retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plates with "Sheet n of 9" captions and honest "schematic" notes.
- Plain first-person lede with real specifics; no slogans.
- Aerobraking structure (four headings, facts strip, orbit-range ledger) and pager showing the neighbour's first fact.
- Failed images collapse cleanly; one h1 per page; unique titles; JSON-LD; canonical; 404 joke; skip link; focus-visible and reduced-motion handling.
- 320 px header fix from cycle 121.

## Verdict
The site is authored, coherent and not generic, and I found no regression. What holds it back is content only the owner can supply: a status line (the dates now lie in the past), a sentence separating his work from Falcone et al., a single answer to "best project", a sourced or cut Raftar claim, and local Resume, images and fonts with real dimensions. The designer has nothing left to fix without inventing facts.
