# Critique, 2026-11-03 (cycle 70)

Rendering: `python3 tools/check.py . agents/shots` finished (about 3 minutes, run in background). The log ends with "screenshots in .../agents/shots" and every page reported OK; the only notes are "images not loaded, likely sandbox network". I viewed index-phone-dark, index-desktop-light and aerobraking-drl-tablet-light. Working tree was clean at start; the last commit (cycle 69) changed no site files, so no regression. I edited no site files.
New this cycle: I measured tap targets at 360 px on index.html. The only visible interactive element under 40 px tall is the inline strike-through span (186x19, not a link), and the 0x0 entries are desktop-only header links hidden on phones. One h1 on the page. All three LinkedIn links point to the same URL.
Caveat: screenshots use fallback serif faces and show no Wix images because the sandbox has no network. "As shown below" on the aerobraking page therefore appears to point at nothing in my render; this is an environment limit, but see finding 5.

## Sources consulted
Two of my three planned page fetches (WCAG Understanding 2.5.8, web.dev optimize-cls, MDN prefers-reduced-motion) were blocked by a permission timeout, so I did not read them. What I actually have:
- Web search result list only (pages not read): W3C Understanding SC 2.5.8 Target Size (Minimum), https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html . I rely on the SC's known 24x24 CSS px minimum, which the site's 44 px targets exceed. Unverified against the page this cycle.
- Carried from last cycle, which I read then: W3C SC 1.4.12 https://www.w3.org/WAI/WCAG22/Understanding/text-spacing and Unlighthouse on font-caused layout shift https://unlighthouse.dev/learn-lighthouse/cls/web-fonts-causing-foit .
- Blocked, not read, listed so the designer can fetch them: https://web.dev/articles/optimize-cls and https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion .
This is below the three-sources-per-cycle bar; treat the best-practice citations as weaker than usual.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper ground with faint grain, double ink rules, hard-shadow red button, mono ledger labels, rotated ruled stamps, inverted dark footer. The dark theme keeps the flat warm palette (amber on near-black). No gradient, blur or glow seen in any screenshot.
2. Must not look AI-generated: met. First-person copy with specific numbers, a ruled index instead of cards, struck-through "three weeks" on a marker band, "Fig. 1" captions, a colophon saying "no framework". No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine identically ruled rows and a familiar DM Serif plus Source Serif pairing. No tells moved.
- Looks good: 7/10. Phone index reads like a printed ledger with good pacing, and desktop has a clear name, lede, "For the record" rail and ruled index. The aerobraking tablet page is calm and readable with a clean drawn figure and a good Previous/Next footer. Held down by no rendered photograph anywhere and only one illustrated row (01) on the index; rows 02 to 09 are text only.
- SEO: 7/10. Per the repo: unique titles, canonical, absolute og:image (assets/og.png, 1200x630, with alt), twitter:card summary_large_image, JSON-LD, sitemap, robots, 404, one h1 on index. Not verifiable offline: live og:image fetch, real LCP/CLS with Wix images.
- UX: 7/10. First phone screen gives name, school, lab, advisor, one concrete result, a primary button, Resume and LinkedIn. Gaps: no status or availability line; a single contact route (owner constraint); Resume on a Wix URL.
- Fun and personality: 7/10. Strike-through, stamps, "Fig. 1", honest colophon. One more earned touch is possible (finding 9).

## Findings (ranked)
1. Major, UX/content: nothing says what he is looking for or when he is available; the CMU line is dated 2023 - 2025, which is already past. A recruiter cannot tell if he is open to roles. Owner must supply one sentence; leave STATUS empty rather than invent.
2. Major, robustness: Resume (PDF) points at one Wix filesusr URL (index.html lines 35, 51, 72 and the same on other pages). If Wix retires it, the resume breaks sitewide and at the end of every page. Owner must supply assets/resume.pdf.
3. Major, content: "Start here" (Snake robots, row 01) has no number or result, while Aerobraking (46 orbits), Hasselhoff (99 s) and Tether (500 m) carry stamps. The lead project has the weakest evidence on the index. Owner to supply 2 to 3 outcome sentences, or move the label.
4. Major, visual: no photograph of a robot, car, satellite or person renders; media are Wix hotlinks, the same dependency risk as finding 2. This is the main reason Looks-good is 7. Needs owner media.
5. Minor, robustness: project pages say "as shown below" and "as shown in the figure above" (aerobraking-drl.html lines 58, 65, 66, 75); if the Wix images stop loading, the prose points at nothing. Same fix as finding 4: local copies of the figures. Check each figure has meaningful alt text for that case.
6. Minor, performance: hotlinked figures lack width/height (CLS risk). Needs real dimensions; do not guess. Once local images exist, add fetchpriority="high" to the first visible one and lazy-load the rest.
7. Minor, performance: two Google web fonts with no size-adjusted fallback. Self-hosted WOFF2 would remove a third-party connection and allow measured override values (per the Unlighthouse article, values come from tooling, not guesses). Needs owner font files or a measured run.
8. Minor, content: Raftar says "40+ students", "captained", "suspension and brakes" and little else. Add only owner-confirmed specifics.
9. Minor, fun and visual (taste): stamps are the best idea on the site but sit on 4 of 9 rows, and rows 02, 03, 08, 09 have none and no thumbnail. Do not invent numbers; wait for media or facts.
10. Nit, UX (taste): the phone header shows only the K mark, so the name is not in view on long project pages. The name is in the H1 on home.
11. Nit, a11y: sticky header versus SC 2.4.11 is covered by scroll-padding-top:80px; I could not verify by tabbing in a browser this cycle.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps where the number is the point; ruled index with mono numbers; inverted-print footer and dark theme; double rules; 44 px tap targets; no-JS figure links; local og:image with alt; JSON-LD; 404 page; honest "schematic" captions; accurate colophon; desktop header showing the name; About page structure; Previous/Next footer on project pages; layout survives WCAG 1.4.12 text-spacing overrides at 360 px.

## Verdict
The site commits coherently to the retro matte direction and reads as one person's work. Both owner constraints are met and nothing regressed. What holds it back is missing owner input, not design: a status sentence, a local resume PDF, outcome sentences for Snake and Raftar, real photographs with dimensions, and font files. Findings 1 to 9 are owner-blocked; there is no designer-side fix this cycle. Research this cycle was thin because page fetches were blocked.
