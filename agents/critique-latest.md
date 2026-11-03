# Critique, 2026-11-03 (cycle 71)

Rendering: `python3 tools/check.py . agents/shots` ran to the end; every page reported OK, with only "images not loaded, likely sandbox network" notes. I viewed projects-phone-light, index-tablet-dark and snake-robots-desktop-light. Working tree was clean and the last commit changed no site files, so there is no regression. I edited no site files.

New measured this cycle: I tabbed through aerobraking-drl.html at 360 px (56 stops). Every body link and control sat below the sticky header (57 px bottom edge), so SC 2.4.11 holds in practice; the only stops above 57 px were the header's own links. None of the 9 figures on that page has width/height attributes; all have non-empty alt text (the last img entry has empty src and alt, which should be checked, see finding 6). The live site returned 403 to curl from this sandbox, so the live og:image fetch is still unverified.

## Sources consulted (pages read this cycle)
- web.dev, Optimize Cumulative Layout Shift, https://web.dev/optimize-cls/ . Read. It says to always set width and height on images (or aspect-ratio), and for fonts suggests font-display: optional, a close fallback, size-adjust overrides, and preload.
- W3C, Understanding SC 2.4.11 Focus Not Obscured (Minimum), https://w3c.github.io/wcag/understanding/focus-not-obscured-minimum.html . Read. It names CSS scroll-padding (technique C43) as sufficient for sticky banners. This supports the site's scroll-padding-top and closes old finding 11.
- UX Design Institute, what hiring managers look for in a portfolio, https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/ . Read. Secondary source, not NN/g (the NN/g search returned only a listing). It says two to three strong case studies, problem/approach/result structure, metrics where available, skimmable writing.
- Carried from earlier cycles: W3C SC 1.4.12 text spacing; Unlighthouse on font-caused layout shift (https://unlighthouse.dev/learn-lighthouse/cls/web-fonts-causing-foit).

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper ground with faint grain, double ink rules, hard-shadow button, mono ledger labels, ruled stamps, inverted footer; the dark theme stays flat amber on near-black. No gradient, blur or glow in any screenshot.
2. Must not look AI-generated: met. Specific first-person copy with numbers, a ruled index in place of cards, struck-through "three weeks", "Fig." captions, a plain colophon. No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine identically ruled rows and a familiar DM Serif plus Source Serif pairing. No tells moved.
- Looks good: 7/10. The ledger index and desktop project page are composed and calm. The phone Projects page has a rhythm problem (finding 5). No photograph renders anywhere in my environment.
- SEO: 7/10. Per the repo: unique titles, canonical, absolute og:image with alt, twitter card, JSON-LD, sitemap, robots, 404, one h1. Not verifiable offline: live og:image, real LCP/CLS with Wix images.
- UX: 7/10. First screen answers who, where, what and next step. Gaps: no status line, Resume on a Wix URL, and the flagship project page is thin (finding 1).
- Fun and personality: 7/10. Strike-through, stamps, "Sheet 1 of 9 . NTS" title-block caption, honest colophon. The drafting-sheet joke is the best earned touch on the site and only the Snake page seems to use it fully.

## Findings (ranked)
1. Major, content/UX: the page the index labels "Start here" is the thinnest on the site. Snake robots (desktop render) is a title, a lab/advisor row, a placeholder schematic captioned "Module count is illustrative", one 2-sentence paragraph and a link to the lab. No method, no result, no number; the schematic is a stand-in, not his work. The strongest-marked project has the least evidence, against the case-study guidance above (problem, approach, result, metrics). Owner must supply 2 to 3 true sentences on what he implemented and what happened. Alternative that needs no new facts: move "Start here" to Aerobraking (46 orbits), which already has results. Do not invent outcomes.
2. Major, UX/content: no status or availability sentence; the CMU line reads "2023 - 2025", which is past. A recruiter cannot tell if he is open to roles. Owner supplies one sentence; leave STATUS empty until then.
3. Major, robustness: Resume (PDF) is one Wix filesusr URL repeated in header, lede and footer on every page. One retirement breaks it everywhere. Owner must supply assets/resume.pdf.
4. Major, visual: no photograph of a robot, car, satellite or person; project media are Wix hotlinks (same dependency risk as 3). Main reason Looks-good is 7. Needs owner media.
5. Minor, visual (phone, projects.html at 360 px): the filter row wraps so a lone "Build" button sits on a second line, and the five-chip row is heavy, taking about 160 px before the first project. Fix is designer-side and small: shorter chips or a single horizontally scrolling row, or reduce chip padding so all five fit on one line. Taste, but the orphan reads unfinished.
6. Minor, performance/CLS: the 9 figures on aerobraking-drl.html have no width/height (web.dev says always set them or use aspect-ratio). One img entry has an empty src and alt: check it is a template placeholder and not a stray element. Dimensions needed from owner files; do not guess. Once local, set fetchpriority="high" on the first visible one.
7. Minor, robustness: aerobraking prose says "as shown below" and "as shown in the figure above"; if Wix images fail, it points at nothing. Same fix as 4.
8. Minor, performance: two Google fonts with no size-adjusted fallback or preload. Needs self-hosted WOFF2 or a measured run; web.dev lists size-adjust, font-display: optional and preload as the options.
9. Minor, content: Raftar says "40+ students", "captained", "suspension and brakes" and little more. Add only owner-confirmed specifics.
10. Minor, fun (taste): stamps appear on 4 of 9 rows; rows 02, 03, 08, 09 have none. Only add where a true number exists.
11. Nit, UX (taste): the phone header shows only the K mark, so the name is off-screen on long project pages; it is in the H1 on home.

Closed this cycle: sticky header versus SC 2.4.11, verified by tabbing at 360 px.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps where the number is the point; ruled index with mono numbers; inverted-print footer and flat dark theme; double rules; the "Sheet 1 of 9 . NTS" title-block caption; honest "schematic" captions; accurate colophon; 44 px tap targets; scroll-padding-top covering the sticky header (verified); no-JS figure links; local og:image with alt; JSON-LD; 404 page; desktop header with name; Previous/Next footer on project pages; survives WCAG 1.4.12 text-spacing overrides.

## Verdict
The site commits coherently to the retro matte direction and reads as one person's work; both owner constraints are met and nothing regressed. The one new substantive point is that the project the site tells visitors to start with is its weakest page, resting on a stand-in schematic. That is an owner-content problem, but the "Start here" label is a designer-side choice and can be moved to a project that has results. Beyond that, findings 1 to 4 and 6 to 9 need owner facts or files; the only designer-fixable item is the phone filter-chip wrap (5).
