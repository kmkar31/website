# Critique, 2026-11-13 (cycle 132)

Rendering: `python3 tools/check.py . agents/shots` ran to completion (rc=0, zero FAIL; only "images not loaded, sandbox network" notes). It takes over 2 minutes, so run it with a long timeout. I viewed index phone-light, index desktop-light, about desktop-light, snake-robots phone-dark and raftar tablet-light. I did not open the other screenshots. I edited no site files. No HTML or CSS has changed since cycle 121 (later commits are log-only).

## Sources consulted
Primary sources could not be read. WebFetch of https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html and https://web.dev/articles/optimize-cls was refused (permission request unanswered, "do not retry"). One WebSearch ran. It returned only secondary blog posts, none of which I opened or relied on, for example https://www.toptal.com/designers/ux/ux-portfolio-tips-recruiter and https://www.format.com/magazine/creative-portfolio-checklist-what-clients-look-for. The three-source rule is therefore not met (environment limit). No finding rests on an external source; all rest on the repo and screenshots.

## Scores
- AI-tell: 2/10, unchanged. Paper palette, ruled list, tilted stamps, struck-through "three weeks" on amber, mono "For the record" ledger, plain first-person copy, footer reading "Hand-built static pages, one stylesheet, no framework". Remaining tell: the familiar shape (intro, list, dark footer). No tell moved.
- Looks good: 8/10, unchanged. Desktop home is calm and well measured. The Raftar tablet page (title, question, fact row, Fig. 1 plate, pager) is the strongest template. Weak spots: on home only row 06 carries a plate; rows 02, 03, 08, 09 have no mark; About leaves the right third empty below the "On this page" box on wide screens.
- SEO: 7/10, unchanged. Unique titles, canonical, JSON-LD, sitemap, 404. Held down by robots.txt and sitemap under /website/ (crawlers read robots.txt only at the host root), identical lastmod values, one shared og card. Indexing and LCP are not verifiable offline.
- UX: 6/10, unchanged. Name, field, lede, Resume and LinkedIn are in the first phone screen. Held down by no status line (`build/build.py:262 STATUS = ""`), two answers to "best project", thin project pages, one contact route (LinkedIn).
- Fun and personality: 7/10, unchanged. 99 s stamp, struck-through "three weeks", sheet numbers, 404 joke. Nothing new.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. No gradient, blur or glow in light or dark shots.
2. Not AI-looking: met in visuals and copy. Do not regress.
No new owner notes.

## Ranked findings
1. Major (UX, credibility). Stale dates, no status. Home subtitle reads "MS Mechanical Engineering, Carnegie Mellon University" with no year. About says the Master's ran 2023 to 2025, and today is 2026-11-13. A recruiter cannot tell whether he is a student, graduated, employed or open to work. Owner supplies one line for STATUS.
2. Major (credibility). The aerobraking page (labelled "Start here") says it builds off work by Falcone et al. and its Method section opens "Falcone et al. simulated their agent...". Nothing says what Karthik did. A professor will read it as a summary of someone else's paper. Owner fact needed: "I did X; Falcone et al. did Y".
3. Major (UX). Two answers to "strongest project". The lede and row 01 lead with snake robots. The snake page (phone-dark) has a schematic, one "Why snake robots" paragraph and a link to the lab page, but no result, no method, no role beyond "I implemented". The "Start here" label and the home-list plate sit on row 06. Owner decision: add a snake result, or move the label and plate to row 01.
4. Major (robustness, performance). Wix hotlinks remain: `grep -c wixstatic` lines per file are aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4, landing 2, and 1 each on about, argus, projects, raftar, snake (line counts, not occurrences). The Resume PDF is hosted off-site and linked from every page including 404. Image dimensions and CLS are unverified offline. Google Fonts has no metric-matched fallback. Needs owner files: local images with dimensions, resume.pdf, WOFF2.
5. Major (credibility). Raftar line 48: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" is unsourced (raftar-formula-racing.html:48). Cite or cut. It is also the page's only technical claim, and the page is otherwise one clause on his role. Owner fact.
6. Minor (consistency). Home says "I captained the team"; About says "I led the team"; Raftar fact row says "Team: 40+ students" and the sheet caption repeats the role a third time. Same fact, three phrasings. Pick one. Taste, low risk.
7. Minor (UX, taste). Nine equal-weight rows on Home and Projects; Projects repeats Home almost exactly, so the second page adds only filters. A "Selected" three above "Also" would help a skimmer. Owner picks.
8. Minor (SEO). robots.txt and sitemap live under /website/; submit the sitemap in Search Console. Identical lastmod on all pages; one og.png for every page.
9. Minor (content). Rows 02, 03, 08, 09 have no number or role. Owner facts.
10. Nit (looks, taste). Long text-only stretches in aerobraking Problem and Method; empty right column on About at 1366 px.

Designer-fixable this cycle: nothing without inventing facts, except finding 6, which is optional and needs no new facts. Findings 1 to 5 are owner decisions or files. The loop has been a no-op since cycle 122; I recommend the owner answer items 1, 2, 3 and 5 rather than running more cycles.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode (holds contrast and character on home, about and project pages).
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plate with "Sheet n of 9" caption and honest "schematic" and "illustrative" notes.
- Plain first-person lede with real specifics; no slogans.
- Pager showing the neighbour's first fact; "All projects" back link.
- Failed images collapse cleanly; one h1 per page; unique titles; JSON-LD; canonical; 404 joke; skip link; `:focus-visible`; reduced-motion query; 44 px targets on the phone nav.

## Verdict
The site is authored, coherent and not generic, and I found no regression. What holds it back is content only the owner can supply: a status line, a sentence separating his work from Falcone et al., one answer to "best project", a sourced or cut Raftar claim, and local Resume, images and fonts with real dimensions. Caveats: the primary-source fetches were blocked, so no external source was read; I viewed five of 78 screenshots.
