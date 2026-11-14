# Critique, 2026-11-14 (cycle 133)

Method: `python3 tools/check.py . agents/shots` finished (background run, about 4 min; zero FAIL, only "images not loaded, sandbox network" notes). I viewed index phone-light and desktop-dark, about phone-light, aerobraking tablet-light and tethered phone-light. I did not open the other ~73 screenshots. No site files were edited. The only site change since the last critique is the About wording "I captained the team" (cycle 132, finding 6 resolved, confirmed in about.html and the phone screenshot). No HTML/CSS regressions found.

## Sources consulted
- NN/G, 5 Steps to Creating a UX-Design Portfolio (fetched and read): https://www.nngroup.com/articles/ux-design-portfolios/ . Takeaways: make your role clear, show results, 3 to 5 detailed case studies, decide three takeaways and check the reader gets them.
- W3C, Understanding SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (search result only, page not fetched; used as a pointer, no finding depends on it).
- web.dev, CSS size-adjust for @font-face: https://web.dev/articles/css-size-adjust and Optimize CLS: https://web.dev/articles/optimize-cls (titles from search only, not read; used as pointers for finding 4).
Only the NN/G page was actually read. The three-source rule is only partly met.

## Scores
- AI-tell: 2/10, unchanged. Paper palette, ruled list, tilted stamps, struck-through "three weeks" on amber, mono "For the record" ledger, plain first-person copy, honest footer ("Hand-built static pages, one stylesheet, no framework"). Remaining tell is only the overall shape (intro, list, dark footer). No tell moved.
- Looks good: 8/10, unchanged. Desktop dark home is calm, well measured and keeps contrast. Aerobraking tablet page (question, fact row, Fig. 1, sheet caption, pager) is the best template. Weak: only row 06 on home has a plate, rows 02, 03, 08, 09 carry no mark; aerobraking Problem/Method is a long text-only stretch; tethered page is a wall of four paragraphs after the figure.
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, og with absolute image and dimensions and alt, JSON-LD, 12-URL sitemap, 404. Held down by robots.txt/sitemap served under /website/ (crawlers read robots.txt at host root only), identical lastmod, one shared og card, off-site images.
- UX: 6/10, unchanged. Name, field, lede, Resume and LinkedIn are visible in the first phone screen. Held down by no status line (`build/build.py:262 STATUS = ""`), two answers to "best project", thin project pages, a single contact route (LinkedIn; no email by design).
- Fun and personality: 7/10, unchanged. 99 s stamp, 46 orbits, 500 m tether, struck-through "three weeks", sheet numbers, 404 joke.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Flat paper and ink in light, inverted print in dark; no gradient, blur or glow.
2. Must not look AI-generated: met in visuals and copy. Do not regress.
No new owner notes.

## Ranked findings
1. Major (UX, credibility). No status and stale timeline. Home says "MS Mechanical Engineering, Carnegie Mellon University" with no year; About says 2023 to 2025; today is 2026-11-14. A recruiter cannot tell student, graduated, employed or open to work. NN/G: reviewers need to get the top takeaways fast. Owner supplies one line for STATUS.
2. Major (credibility). Aerobraking page, marked "Start here", says it "builds off work done by Falcone et al." and its Method section describes what Falcone et al. did ("required a training time of 1 week on a 50 core cluster"). Nothing says what Karthik did. NN/G: make your role clear. A professor will read this as a paper summary. Owner fact needed: "I did X; Falcone et al. did Y".
3. Major (UX). Two answers to "strongest project". Lede and row 01 lead with snake robots; "Start here" and the only plate are on row 06. The snake page has a schematic and one paragraph but no result or method. Owner decision: add a snake result, or move the label and plate to row 01.
4. Major (robustness, performance). Wix hotlinks remain (wixstatic lines: aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4, landing 2, one each on about, argus, projects, raftar, snake). The Resume PDF is also off-site and linked from every page. Image dimensions/CLS cannot be verified offline; Google Fonts has no metric-matched fallback (size-adjust). Needs owner files: local images, resume.pdf, WOFF2.
5. Major (credibility). Raftar page line 48: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" is unsourced and is the page's only technical claim. Cite or cut. Owner fact.
6. Minor (UX, taste). Home and Projects list the same nine equal-weight rows; NN/G suggests 3 to 5 detailed cases. A "Selected" three above "Also" would help a skimmer. Owner picks.
7. Minor (SEO). Sitemap/robots under /website/; submit sitemap in Search Console; identical lastmod; one og.png for all pages.
8. Minor (content). Rows 02, 03, 08, 09 lack a number or role stamp; tethered nanosatellites page has no outcome stated beyond the 500 m setup. Owner facts.
9. Nit (looks, taste). Long text-only stretches (aerobraking Problem/Method, tethered body); About right column empty at 1366 px.

Designer-fixable this cycle: nothing without inventing facts. The loop has been a no-op since cycle 122. I recommend the owner answer items 1, 2, 3 and 5 and supply files for 4 before more cycles run.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plate with "Sheet n of 9" caption and honest "schematic"/"not to scale" notes.
- Plain first-person lede with real specifics; no slogans; consistent "captained" wording.
- Pager showing the neighbour's first fact; "All projects" back link.
- Failed images collapse cleanly; one h1 per page; unique titles; JSON-LD; canonical; 404 joke; skip link; focus-visible; reduced-motion; 44 px phone nav targets.

## Verdict
The site is authored, coherent and not generic, and I found no regression. What holds it back is content only the owner can supply: a status line, a sentence separating his work from Falcone et al., one answer to "best project", a sourced or cut Raftar claim, and local Resume, images and fonts with real dimensions. Caveat: only one external source was actually read and 6 of 78 screenshots were viewed.
