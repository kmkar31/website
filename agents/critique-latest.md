# Critique, 2026-11-13 (cycle 131)

Rendering: `python3 tools/check.py . agents/shots` ran to completion (zero FAIL; only "images not loaded, sandbox network" notes). I viewed index phone-light, index desktop-dark, about phone-dark and aerobraking-drl tablet-light. I did not open the other screenshots. I edited no site files. No site source has changed since cycle 121 (later commits are log-only).

## Sources consulted
Research limit: WebFetch was loaded this cycle, but all three fetches were refused (permission request unanswered, "do not retry"). I read no source page, so the three-source rule is not met (environment limit). The URLs below are unverified pointers; no finding rests on them.
- Blocked: https://web.dev/articles/optimize-cls
- Blocked: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Blocked: https://www.nngroup.com/articles/portfolios/
Findings rest on the repo (greps below) and screenshots.

## Scores
- AI-tell: 2/10, unchanged. Paper palette, ruled list, tilted stamps, struck-through "three weeks" on amber, mono "For the record" ledger, plain first-person copy, footer that says "Hand-built static pages, one stylesheet, no framework". Remaining tell: the familiar shape (intro, list, dark footer). No tell moved.
- Looks good: 8/10, unchanged. Home on desktop-dark is calm, well measured, with a clear ledger sidebar. Aerobraking tablet page has strong hierarchy (title, question, fact row, Fig. 1 plate, sectioned body). Weak spots: row 06 is the only row with a plate; rows 02, 03, 08, 09 carry no mark; the aerobraking Problem, Setup and Method sections are long text with no figure.
- SEO: 7/10, unchanged. Unique titles, canonical, JSON-LD, sitemap, 404. Held down by robots.txt and sitemap under /website/ (crawlers read robots.txt only at the host root), all 12 sitemap lastmod values identical (2026-11-02), one shared og card. Indexing and LCP are not verifiable offline.
- UX: 6/10, unchanged. Name, field, lede, Resume and LinkedIn sit in the first phone screen (index phone). Held down by no status line (`build/build.py:262 STATUS = ""`), two answers to "best project", project pages with no role or outcome, one contact route (LinkedIn).
- Fun and personality: 7/10, unchanged. 99 s stamp, struck-through "three weeks", sheet numbers, 404 joke. Nothing new since.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. No gradient, blur or glow in the viewed shots (light and dark).
2. Not AI-looking: met in visuals and copy. Do not regress.
No new owner notes.

## Ranked findings
1. Major (UX, credibility). Stale dates, no status. Home subtitle reads "MS Mechanical Engineering, Carnegie Mellon University" with no year (desktop-dark and phone shots); About says the Master's ran 2023 to 2025 and the Seagate role is May to Aug 2024; today is 2026-11-13. A recruiter cannot tell whether he is a student, graduated, employed or open to work. Owner supplies one line for STATUS.
2. Major (credibility). The aerobraking page (labelled "Start here") says "This project builds off work done by Falcone et al." and the Method section opens "Falcone et al. simulated their agent..." (tablet shot). Nowhere does it say what Karthik did. A professor will read it as a summary of someone else's paper, and "our method" and "the authors" blur together. Owner fact needed: "I did X; Falcone et al. did Y".
3. Major (UX). Two answers to "strongest project". The lede and row 01 lead with snake robots (page has a schematic and one rationale paragraph, no result or role), while the "Start here" label and the only plate sit on row 06 (visible on phone and desktop shots). Owner decision: add a snake result, or move label and plate to the top.
4. Major (robustness, performance). Hotlinks to Wix remain. grep counts of wixstatic occurrences per file: aerobraking 18, assistive-tricycle 16, quadrotor-sysid 16, hasselhoff 12, projects 9, tethered 8, snake 6, landing 4, raftar 4, argus 2, about 1. The Resume PDF is on filesusr.com and linked from every page including 404, so one Wix change breaks it everywhere. Images have no verified width/height (CLS risk, unverified offline). Google Fonts with no metric-matched fallback. Needs owner files: local images with dimensions, resume.pdf, WOFF2.
5. Major (credibility). Raftar page line 48: "How do we build an electric racecar that is one-fifth the weight of a Ferrari but matches its 0-60 acceleration time?" is unsourced. Cite or cut. Owner fact.
6. Minor (credibility, UX). Raftar page gives what he did in one clause ("suspension and brakes") but no number, test or result beyond the podium; thinnest page next to snake. Owner facts.
7. Minor (UX, taste). Nine equal-weight rows on Home and Projects; Projects repeats Home almost exactly, so the second page adds only filters. A "Selected" three above "Also" would help a skimmer. Owner picks.
8. Minor (SEO). robots.txt and sitemap live under /website/; submit the sitemap in Search Console. Identical lastmod on all pages; one og.png for every page.
9. Minor (content). Rows 02, 03, 08, 09 have no number or role (home shots). Owner facts.
10. Nit (looks, taste). Long text-only stretches in aerobraking Problem and Method; About leaves empty space on wide screens.

Designer-fixable this cycle: nothing without inventing facts. Findings 1 to 6 are owner decisions or files. The loop has been a no-op since cycle 122; I recommend the owner answer items 1, 2, 3 and 5 rather than running more cycles.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode (dark mode holds contrast and character on home and about).
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plate with "Sheet n of 9" caption and honest "schematic" notes.
- Plain first-person lede with real specifics; no slogans.
- Aerobraking structure; pager showing the neighbour's first fact.
- Failed images collapse cleanly; one h1 per page; unique titles; JSON-LD; canonical; 404 joke; skip link; `:focus-visible` outline and reduced-motion media query present; 44 px targets on the phone nav.

## Verdict
The site is authored, coherent and not generic, and I found no regression. What holds it back is content only the owner can supply: a status line, a sentence separating his work from Falcone et al., one answer to "best project", a sourced or cut Raftar claim, and local Resume, images and fonts with real dimensions. Caveats: all three research fetches were blocked, so no external source was read; I viewed four of 78 screenshots.
