# Critique, 2026-11-03 (cycle 68)

Rendering: `python3 tools/check.py . agents/shots` completed (it takes over 2 minutes here, so I ran it in the background). 78 OK lines, no failures; only "images not loaded" notes (sandbox, Wix hotlinks). I viewed index-phone-light and index-desktop-light. Working tree was clean, so there is no regression from cycle 67 (which changed no site files). No site files edited.
Caveat: screenshots use fallback serif faces because Google Fonts is unreachable in the sandbox.

## Sources consulted
WebFetch permission was not answered again, so no page was read. These are unread pointers; nothing is quoted.
- W3C, Understanding SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (fetch blocked this run)
- W3C, Understanding SC 2.4.11 Focus Not Obscured: https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html (not read)
- web.dev, Optimize CLS: https://web.dev/articles/optimize-cls (not read)
- NN/g, mobile UX: https://www.nngroup.com/articles/mobile-ux/ (not read)

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper ground, ink rules, hard-shadow primary button, mono ledger, ruled stamps, inverted footer; no gradient, blur or glow in either theme.
2. Must not look AI-generated: met. First-person copy with real numbers, ruled index instead of cards, struck-through "three weeks" on a marker band, "Fig. 1" caption. No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Residual tells: nine identically ruled rows; the DM Serif plus Source Serif pairing is tasteful but familiar. No tells moved.
- Looks good: 7/10. Phone index reads as a printed ledger with good pacing; desktop has a clear hierarchy (name, lede, "For the record" rail, ruled index). Held down by no rendered photograph anywhere and one figure on row 01, which leaves rows 02 to 09 bare.
- SEO: 7/10. Per the repo: unique titles, canonical, OG, JSON-LD, sitemap, robots, 404, one h1. Not verifiable offline: live og:image fetch, real LCP/CLS with Wix images.
- UX: 7/10. First phone screen gives name, school, lab, advisor, a concrete result, primary button, Resume and LinkedIn. Gaps: no status/availability line, one contact route (owner constraint), Resume on a Wix URL.
- Fun and personality: 7/10. Strike-through, stamps, "Fig. 1", honest colophon. Could use one more earned touch (see finding 9).

## Findings (ranked)
1. Major, UX/content: no line says what he is looking for or when he is available (CMU 2023-2025 is already past). A recruiter cannot tell if he is hiring-ready. Owner must supply the sentence; STATUS stays empty rather than invented.
2. Major, robustness: Resume (PDF) points at one Wix filesusr URL on every page (header, hero, footer). If Wix retires it, the resume breaks sitewide. Owner must supply assets/resume.pdf.
3. Major, content: "Start here" (Snake robots, row 01) has no number or result, while Aerobraking (46 orbits), Hasselhoff (99 s), Tether (500 m) have stamps. The lead project has the weakest evidence on the index. Owner to supply 2-3 outcome sentences, or move the label.
4. Major, visual: no photograph of a robot, car, satellite or person renders; media are Wix hotlinks, the same dependency risk as finding 2. Main reason Looks-good is 7. Needs owner media.
5. Minor, performance: hotlinked figures lack width/height (CLS risk). Needs real dimensions; do not guess. When local images exist, add fetchpriority="high" to the first visible one and lazy-load the rest.
6. Minor, performance: two Google web fonts with no size-adjusted fallback; self-hosted WOFF2 would also drop a third-party connection. Guessed metrics could worsen CLS, so needs owner files or measurement.
7. Minor, content: Raftar says "40+ students", "captained", "suspension and brakes" and little else. Add only owner-confirmed specifics.
8. Minor, visual (taste): rows 02 to 09 have no thumbnail, so desktop shows one illustrated row then eight text rows. Fine as a ledger; revisit when media exist.
9. Minor, fun: the stamps are the best idea on the site but sit only on 4 of 9 rows. Possible, using facts already in the repo: a "Fig. N" caption in the same style for the remaining rows once real figures exist. Do not invent numbers for rows 02, 03, 08, 09.
10. Nit, UX (taste): phone header shows only the K mark; the name is not in view on long project pages.
11. Nit, a11y: sticky header vs SC 2.4.11 is covered by scroll-padding-top:80px; not re-verified by tabbing in a browser.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps where the number is the point; ruled index with mono numbers; inverted-print footer and dark theme; double rules; 44 px tap targets; no-JS figure links; local og:image; JSON-LD; 404 page; honest "schematic" captions; accurate colophon; desktop header showing the name; About page structure.

## Verdict
The site commits coherently to the retro matte direction and reads as one person's work. Both owner constraints are met and nothing regressed. What holds it back is missing owner input, not design: a status sentence, a local resume PDF, outcome sentences for Snake and Raftar, real photographs with dimensions, and font files. There is no designer-side fix this cycle (findings 1 to 7 depend on the owner). Web research was blocked again, so the sources above are unread pointers.
