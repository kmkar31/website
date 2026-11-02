# Critique, 2026-11-02 (cycle 67)

Rendering: `python3 tools/check.py . agents/shots` ran to completion. All pages x 3 viewports x 2 themes are OK; the only notes are "images not loaded" (sandbox, Wix hotlinks). I viewed index-phone-light and index-desktop-dark. Working tree was clean. No regression since cycle 66. No site files edited.
Caveat: the screenshots render with fallback serif faces because Google Fonts is unreachable in the sandbox, so type pairing is judged from the CSS and the previous cycles' renders, not from this run.

## Sources consulted
WebFetch permission was not answered again this run and no search result was usable, so none of these pages was read. They are pointers only; nothing is quoted.
- W3C, Understanding SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (fetch blocked)
- W3C, Understanding SC 2.4.11 Focus Not Obscured (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html (not read)
- web.dev, Optimize Cumulative Layout Shift: https://web.dev/articles/optimize-cls (not read)
- NN/g, mobile UX: https://www.nngroup.com/articles/mobile-ux/ (not read)

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper ground, ink rules, hard-shadow button, mono ledger, ruled stamps, inverted footer, no gradient, blur or glow in either theme.
2. Must not look AI-generated: met. First-person copy with real numbers, ruled index instead of cards, struck-through "three weeks" on a marker band, "Fig. 1" caption. No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Residual tells: nine identically ruled rows; DM Serif Display plus Source Serif is tasteful but familiar. No tells moved.
- Looks good: 7/10. Phone index reads as a printed ledger with good pacing; desktop dark has a clear hierarchy (name, lede, "For the record" rail, ruled index). Held down by no rendered photograph anywhere and a single figure on row 01, which makes rows 02 to 09 look bare.
- SEO: 7/10. Unique titles, canonical, OG with local og:image, JSON-LD, sitemap, robots, 404, one h1. Not verifiable offline: live og:image fetch, real LCP/CLS with Wix images.
- UX: 7/10. First phone screen gives name, school, lab, advisor, a concrete result, primary button, Resume and LinkedIn. Gaps: no status/availability line, one contact route (owner constraint), Resume on a Wix URL.
- Fun and personality: 7/10. The strike-through, "Time allowed: 99 s" and "46 orbits to target" stamps and "For the record" are specific and earned. Still mostly tidy; no tactile press state or aside beyond these.

## Findings (ranked)
1. Major, content/UX: no current-status or availability sentence anywhere (home, About, footer). A recruiter cannot tell if he is looking for roles or when he graduates (CMU 2023-2025 is already past). Owner must supply the sentence; the STATUS ledger row stays empty rather than invent one.
2. Major, robustness: Resume (PDF) points at one Wix filesusr URL on every page (header, hero, footer). If Wix retires it, the resume breaks sitewide. Owner must supply assets/resume.pdf.
3. Major, content/UX: "Start here" (Snake robots, row 01) has no number or result on the index, while Aerobraking (46 orbits), Hasselhoff (99 s) and Tether (500 m) carry stamps. The lead project is the one with the weakest evidence. Owner to supply 2-3 outcome sentences, or move the label. Mobile guidance (NN/g, unread) favours leading with the strongest outcome.
4. Major, visual: no photograph of a robot, car, satellite or person renders; media are Wix hotlinks, the same dependency risk as finding 2. Main reason Looks-good is 7. Needs owner media.
5. Minor, performance: hotlinked figures lack width/height (web.dev CLS guidance, unread). Needs real dimensions; do not guess. When local images exist, no loading="lazy" and fetchpriority="high" on the first visible one.
6. Minor, performance: two Google web fonts with no size-adjusted fallback. Self-hosted WOFF2 would also drop a third-party connection. Guessed metrics could worsen CLS, so needs owner files or measurement.
7. Minor, content: Raftar says "40+ students", "captained", "suspension and brakes" and little else. Add only owner-confirmed specifics.
8. Minor, visual (taste): rows 02 to 09 on the index have no thumbnail, so desktop shows one illustrated row followed by eight text rows. Fine as a ledger; revisit when media exist.
9. Nit, UX: phone header shows only the K mark; the owner's name is not in view on long project pages. Taste.
10. Nit, a11y: sticky header vs SC 2.4.11 is covered by scroll-padding-top:80px; not re-verified by tabbing in a browser this cycle.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted-print footer and dark theme; double rules; 44 px tap targets; no-JS figure links; local og:image; JSON-LD; 404 page; honest "schematic" captions; accurate colophon; desktop header showing the name; About page structure.

## Verdict
The site commits coherently to the retro matte direction and reads as one person's work. Both owner constraints are met and nothing regressed. What holds it back is missing owner input, not design: a status sentence, a local resume PDF, outcome sentences for Snake and Raftar, real photographs with dimensions, and font files. There is no designer-side fix this cycle (findings 1 to 7 all depend on the owner). Web research was blocked again, so the sources above are unread pointers.
