# Critique, 2026-11-03 (cycle 69)

Rendering: `python3 tools/check.py . agents/shots` ran in the background (about 3 minutes): 78 OK lines, no failures, only "images not loaded" sandbox notes. I viewed index-phone-light and index-desktop-dark. Working tree clean; cycle 68 changed no site files, so no regression. I edited no site files.
New this cycle: I ran my own WCAG 1.4.12 text-spacing stress test (injected line-height 1.5, letter-spacing .12em, word-spacing .16em, paragraph spacing 2em) at 360 px on index, projects and aerobraking-drl. No horizontal overflow (scrollWidth 360) and no clipped or overlapping text found. The index hero screenshot under those settings still reads cleanly. This is a new topic for the log (text spacing, font fallback metrics).
Caveat: screenshots use fallback serif faces because Google Fonts is unreachable in the sandbox.

## Sources consulted
- W3C, Understanding SC 1.4.12 Text Spacing (read): https://www.w3.org/WAI/WCAG22/Understanding/text-spacing . Content must survive line height 1.5x, paragraph spacing 2x, letter spacing 0.12x, word spacing 0.16x with no loss. The site passes my test.
- Unlighthouse, Fix web fonts causing layout shifts (read): https://unlighthouse.dev/learn-lighthouse/cls/web-fonts-causing-foit . size-adjust, ascent-override, descent-override and line-gap-override make a local fallback match the web font; the article points to tools (Fontaine, Font Style Matcher) to derive values and gives no hand formula. This supports the existing decision not to guess metrics.
- Web search on NN/g and others about what hiring managers look for in portfolios (results only, no page read): https://www.nngroup.com/articles/author/rachel-krause/ . Unread pointer; nothing is quoted from it.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper ground, ink double rules, hard-shadow red/amber button, mono ledger, rotated ruled stamps, inverted footer, dark theme keeps the same flat warm palette. No gradient, blur or glow.
2. Must not look AI-generated: met. First-person copy with real numbers, a ruled index rather than cards, the struck-through "three weeks" on a marker band, "Fig. 1" caption, a colophon that says "no framework". No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine identically ruled rows; the DM Serif plus Source Serif pairing is tasteful but familiar. No tells moved.
- Looks good: 7/10. Phone index reads like a printed ledger with good pacing; desktop has clear hierarchy (name, lede, "For the record" rail, ruled index). Held down by no rendered photograph and a single figure on row 01; rows 02 to 09 are bare text on desktop.
- SEO: 7/10. Per the repo: unique titles, canonical, OG, JSON-LD, sitemap, robots, 404, one h1. Not verifiable offline: live og:image fetch, real LCP/CLS with Wix images.
- UX: 7/10. First phone screen gives name, school, lab, advisor, one concrete result, a primary button, Resume and LinkedIn. Gaps: no status/availability line; one contact route (owner constraint); Resume on a Wix URL.
- Fun and personality: 7/10. Strike-through, stamps, "Fig. 1", honest colophon. One more earned touch is possible (finding 9).

## Findings (ranked)
1. Major, UX/content: nothing says what he is looking for or when he is available (CMU 2023-2025 is already past). A recruiter cannot tell if he is available. Owner must supply the sentence; leave STATUS empty rather than invent.
2. Major, robustness: Resume (PDF) points at one Wix filesusr URL on every page (header, hero, footer). If Wix retires it, the resume breaks sitewide. Owner must supply assets/resume.pdf.
3. Major, content: "Start here" (Snake robots, row 01) has no number or result, while Aerobraking (46 orbits), Hasselhoff (99 s) and Tether (500 m) carry stamps. The lead project has the weakest evidence on the index. Owner to supply 2-3 outcome sentences, or move the label.
4. Major, visual: no photograph of a robot, car, satellite or person renders; media are Wix hotlinks, the same dependency risk as finding 2. This is the main reason Looks-good is 7. Needs owner media.
5. Minor, performance: hotlinked figures lack width/height (CLS risk). Needs real dimensions; do not guess. Once local images exist, add fetchpriority="high" to the first visible one and lazy-load the rest.
6. Minor, performance: two Google web fonts with no size-adjusted fallback. Self-hosted WOFF2 would remove a third-party connection and allow measured override values (per the Unlighthouse article, values come from tooling, not guesses). Needs owner font files or a measured run.
7. Minor, content: Raftar says "40+ students", "captained", "suspension and brakes" and little else. Add only owner-confirmed specifics.
8. Minor, visual (taste): rows 02 to 09 have no thumbnail, so desktop shows one illustrated row then eight text rows. Acceptable as a ledger; revisit when media exist.
9. Minor, fun: stamps are the best idea on the site but sit on 4 of 9 rows. Possible only with facts already in the repo; do not invent numbers for rows 02, 03, 08, 09.
10. Nit, UX (taste): the phone header shows only the K mark, so the name is not in view on long project pages. Name is in the H1 on home.
11. Nit, a11y: sticky header vs SC 2.4.11 is covered by scroll-padding-top:80px; still not verified by tabbing in a browser.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps where the number is the point; ruled index with mono numbers; inverted-print footer and dark theme; double rules; 44 px tap targets; no-JS figure links; local og:image; JSON-LD; 404 page; honest "schematic" captions; accurate colophon; desktop header showing the name; About page structure; layout survives WCAG 1.4.12 text-spacing overrides at 360 px.

## Verdict
The site commits coherently to the retro matte direction and reads as one person's work. Both owner constraints are met, nothing regressed, and it newly passes the text-spacing stress test. What holds it back is missing owner input, not design: a status sentence, a local resume PDF, outcome sentences for Snake and Raftar, real photographs with dimensions, and font files. Findings 1 to 7 are owner-blocked; there is no designer-side fix this cycle.
