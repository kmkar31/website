# Critique, 2026-11-02 (cycle 66)

Rendering: `python3 tools/check.py . agents/shots` completed (it needed a longer timeout than 2 minutes). Every page x 3 viewports x 2 themes is OK; only "images not loaded" notes (sandbox, Wix hotlinks). I viewed index-phone-light and about-desktop-light. Working tree was clean before the run; HEAD is 9b1e8bd (About tense fix). No regression. No site files edited.

## Sources consulted
WebFetch was blocked in this run (permission not answered), and no search tool was available. The three pages below could not be read this cycle. I relied on prior-cycle pointers and my own knowledge of them, so none of their text is quoted here.
- W3C, Understanding SC 2.4.11 Focus Not Obscured (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html (fetch blocked)
- web.dev, Optimize Cumulative Layout Shift: https://web.dev/articles/optimize-cls (fetch blocked)
- NN/g, mobile UX: https://www.nngroup.com/articles/mobile-ux/ (fetch blocked)
Topics this cycle: sticky-header focus obscuring, CLS from images and fonts, mobile content priority.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper ground with faint grain, ink rules, hard-shadow red button, mono ledger, ruled stamps, dark inverted footer. No gradient, blur or glow in either screenshot.
2. Must not look AI-generated: met. Plain first-person copy with real numbers, a ruled index in place of cards, the struck-through "three weeks" on a marker band, "Fig. 1" captions. No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Faint tells: nine identically ruled rows; DM Serif Display plus Source Serif is tasteful but familiar. Nothing moved.
- Looks good: 7/10. The phone index reads as a printed ledger and is well paced. About desktop is orderly, but the left column is a long ruled list, and the "On this page" rail ends at about 360 px while the page runs to 2000 px, so the right third is empty. No real photograph renders anywhere, and only row 01 has a figure.
- SEO: 7/10. Unchanged: unique titles, canonical, OG with local og:image, JSON-LD, sitemap, robots, 404, one h1. Not verifiable offline: live og:image fetch, real LCP/CLS with Wix images.
- UX: 7/10. Phone first screen gives name, school, lab, advisor, a concrete result, primary button, Resume and LinkedIn. Gaps: no status or availability line, one contact route (owner constraint), Resume on a Wix URL.
- Fun and personality: 7/10. Marker strike-through, "TIME ALLOWED: 99 S", "46 ORBITS TO TARGET", "500 M OF TETHER". More needs owner facts.

## Ranked findings
1. Major, content: still no status line. `STATUS = ""` (build/build.py:259), so the "For the record" ledger on the home page shows Built, Internships and Toolbox but no Status. Home subtitle says "MS Mechanical Engineering, Carnegie Mellon University" with no graduation date. About now reads "I did my Master's ... (2023 - 2025)", which is correct, but a recruiter on 2026-11-02 still cannot tell what he does now or whether he is open to roles. Needs one owner sentence; the slot exists. Not fixable by the designer without inventing a fact.
2. Major, robustness: Resume (PDF) still points at one Wix filesusr URL (3 occurrences in index.html; also in the About header and the footer). If Wix retires it, the resume breaks on every page. Owner must supply assets/resume.pdf.
3. Major, content/UX: "Start here" (Snake robots, row 01) carries no number or result on the index; the strongest evidence (Aerobraking 46 orbits, Hasselhoff 99 s) sits lower. Owner to supply 2-3 outcome sentences for Snake, or the label should move. Mobile guidance (NN/g, unread this cycle) favours leading with the strongest outcome.
4. Major, visual: no photograph of a robot, car, satellite or person renders; figures and the About portrait are Wix hotlinks, the same dependency risk as finding 2. Main reason Looks-good stays at 7. Needs owner media.
5. Minor, performance: hotlinked figures lack width/height (CLS guidance on web.dev). Needs real dimensions; do not guess. When local images exist, keep loading="lazy" off the first visible one and set fetchpriority="high" on it.
6. Minor, performance: two Google web fonts with no size-adjusted fallback. Self-hosted WOFF2 would also remove the third-party connection. Needs owner/measured files.
7. Minor, content: Raftar says "40+ students", "captained", "suspension and brakes" and little else. Add only owner-confirmed specifics.
8. Minor, visual (taste): About desktop leaves the right third empty below the short "On this page" rail. Could be a sticky rail, but taste; low priority.
9. Nit, UX: phone header shows only the K mark; nothing in view names the owner on long project pages. Taste; reopen only if the name fits at 360 px.
10. Nit, a11y: sticky header vs SC 2.4.11 is covered by scroll-padding-top; confirm by tabbing a long page. Not re-verified in a browser this cycle.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted-print footer and dark theme; double rules; 44 px tap targets; no-JS figure links; local og:image; JSON-LD; 404 page; honest "schematic" captions; accurate colophon; desktop header showing the name; About page structure (skills in three ruled columns, dated education and experience, strike-through repeated in the Seagate bullet).

## Verdict
The site commits coherently to the retro matte direction and reads as one person's work; both owner constraints are met and nothing regressed since cycle 65. What holds it back is missing owner input rather than design: a current-status sentence, a local resume PDF, outcome sentences for Snake and Raftar, real photographs with dimensions, and font files. There is no designer-side fix this cycle. Findings 1 to 4 and 5 to 7 all depend on the owner. This run's web research was blocked, so the sources above are unread pointers.
