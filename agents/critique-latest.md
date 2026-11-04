# Critique, 2026-11-04 (cycle 74)

Rendering: `python3 tools/check.py . agents/shots` ran to completion (about 4 minutes, so it needs a long timeout). All 13 pages passed at phone, tablet and desktop in both themes, with only "images not loaded, likely sandbox network" notes. Working tree was clean before the run. I viewed index-phone-light, index-desktop-light and about-desktop-dark. I edited no site files other than this report.

Honesty note on research: WebFetch was blocked again (W3C Understanding SC 2.5.8 Target Size, permission request unanswered). One WebSearch on portfolio guidance for hiring managers returned only result titles and links, which I did not open. I read no source page this cycle, so the links below are pointers and not verified claims. Nothing in the findings relies on them.

## Sources
- Blocked, not read: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Search results only, not opened: UX Design Institute, "What hiring managers look for in a UX portfolio" https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/ ; NN/g author listing https://www.nngroup.com/articles/author/rachel-krause/?page=5
- Carried from earlier cycles (read then, not refreshed): web.dev CLS https://web.dev/optimize-cls/ ; W3C SC 2.4.11 Focus Not Obscured ; W3C SC 1.4.12 Text Spacing.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone with grain, double ink rules, hard-offset red button, mono ledger labels, ruled stamps, inverted footer, flat dark theme. I saw no gradient, blur or glow in any screenshot.
2. Must not look AI-generated: met. A ruled index, the struck "three weeks" in a marker band, stamps and Fig. captions. No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Residual tells: nine identically ruled rows, and a common editorial serif pairing. No tells moved this cycle.
- Looks good: 7/10. Phone and desktop home have a clear order (name, lede, button, ledger, index). Weaknesses: no photograph of any real work; the right column on desktop rows is empty beside the unstamped rows (01, 02, 03, 08, 09); the thumbnail caption on row 06 wraps awkwardly (see 5).
- SEO: 7/10. Per repo: unique titles and descriptions, canonical, JSON-LD, sitemap, robots.txt, 404 page. Not verifiable offline: live og:image fetch, field LCP and CLS.
- UX: 7/10. Who, where, what and a next step are answered in the first screen. Contact exists on phone only in the lede and the footer.
- Fun and personality: 7/10. The strike-through, stamps and "Sheet N of 9" are authored and specific. Only 4 of 9 rows have a stamp, and I would not add more without a true number.

## Findings (ranked)
1. Major, content/UX (owner facts): there is still no current-status sentence. About says "2023 – 2025" at Carnegie Mellon, and today is November 2026. A recruiter cannot tell whether he is graduated, employed or looking. The STATUS slot in build.py is still empty. The owner supplies one line.
2. Major, robustness (owner file): Resume is a single Wix filesusr URL repeated in the header, the lede, the footer and About. If that URL dies, four links die together. The owner drops assets/resume.pdf into the repo.
3. Major, visual (owner files): the site has no photograph of a robot, car, satellite or person, and project media are Wix hotlinks. The environment limit is noted, but the dependency risk stands. My render showed 3 to 10 failed images per project page.
4. Major, content (owner facts): Snake robots, row 01 and the thinnest page, has no outcomes, and Raftar says only "40+ students" and "captained". The Start-here label correctly moved to Aerobraking in cycle 73. Add only owner-confirmed specifics.
5. Minor, visual (new, designer-fixable): on desktop home, row 06's plate caption wraps to two lines ("Fig. 1 · Aerobraking / orbits") inside a 176 px box, an orphaned word. The cycle 21 fix shortened the snake caption to one line, but the per-project name added in cycle 73 reintroduced the wrap. Shorten it to "Fig. 1 · Orbits" or let it be nowrap.
6. Minor, UX (new, taste): "Start here" now sits on row 06. The label is correct, but the eye reaches 01 to 05 first, and on phone the plate does not appear until after five rows. Consider a one-line pointer in the lede ("Start with the aerobraking work, project 06") rather than reordering rows, since the numbers are fixed sheet numbers. Trade-off: this adds a sentence to a lede that is deliberately short.
7. Minor, UX: on phone the header shows only the K mark, Home, About, Projects and the theme toggle. Contact is not in the header; it is in the lede (two taps from the top) and the footer. Accepted given the 44 px row, but note it.
8. Minor, CLS: figures have no width or height or aspect-ratio (web.dev CLS, carried and not refreshed). The owner must supply dimensions.
9. Minor, robustness: Aerobraking prose says "as shown below" about figures that depend on hotlinks. It has the same blocker as 3.
10. Minor, performance: two Google fonts, no size-adjusted fallback or self-hosting. Needs the WOFF2 files.
11. Nit, SEO (owner action): the sitemap and robots.txt sit at a project-site subpath, so crawlers will not find robots.txt at the host root. Submit sitemap.xml in Search Console.
12. Nit, visual (taste): About on desktop leaves the right third empty beside Skills, Education and Experience (dark screenshot). The "On this page" rail covers the top only. Documented and accepted by the designer; I flag it only as an unbalanced area.

## Good, must not regress
The plain lede with real numbers; the "For the record" ledger; the marker-band strike-through; stamps only where the number is the point; the ruled index with mono numbers; the inverted footer and flat dark theme; double rules; "Sheet N of 9 . NTS" captions; honest "schematic" captions; the accurate colophon; 44 px tap targets; the one-line phone filter row; Previous/Next footers with a real detail; the local og:image; JSON-LD; the 404 page; the reduced-motion block; Start-here on the strongest project.

## Verdict
The site commits to the retro matte direction, reads as one person's work, and both owner constraints are met. Nothing regressed from cycle 73's move of Start-here to Aerobraking, except a two-line wrapped caption on the home thumbnail (5). Almost everything else is blocked on owner facts or files: a status line, a local resume PDF, photographs, and substance for Snake and Raftar. Research was not refreshed this cycle because fetches were blocked, so I make no new external claims.
