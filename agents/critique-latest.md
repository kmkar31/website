# Critique, 2026-11-03 (cycle 73)

Rendering: `python3 tools/check.py . agents/shots` finished (run in background, it exceeds the 2 min tool limit). All pages OK at phone, tablet and desktop in both themes; only "images not loaded, likely sandbox network" notes. I viewed index-phone-light, projects-tablet-dark and snake-robots-desktop-light. Working tree clean before my run. The cycle 71 phone filter row and cycle 72 eager-loading change show no regression. I edited no site files.

Honesty note on research: WebFetch was blocked again this cycle (permission request unanswered, W3C focus-appearance page). I did NOT read any new source page. The sources below are carried from earlier cycles (read then) or were the page I tried and failed to fetch. Treat nothing here as freshly verified.

## Sources
- Attempted, blocked: W3C Understanding SC 2.4.13 Focus Appearance, https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html (not read).
- Carried from earlier cycles (read then): web.dev CLS https://web.dev/optimize-cls/ ; W3C SC 2.4.11 Focus Not Obscured ; W3C SC 1.4.12 Text Spacing ; W3C SC 2.5.8 Target Size (Minimum) https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html ; UX Design Institute hiring-manager portfolio guidance.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Warm paper with grain, double ink rules, hard-offset red button, mono ledger labels, ruled stamps, inverted footer, flat dark theme. No gradient, blur or glow in any screenshot.
2. Must not look AI-generated: met. Ruled index rather than cards, marker-band strike-through of "three weeks", Fig. captions, plain colophon. No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine identically ruled rows; DM Serif Display plus Source Serif is a common editorial pairing. No tells moved.
- Looks good: 7/10. Phone home has a clear order (name, plain lede, red button, ledger, index). Tablet dark Projects is clean. Weaknesses: no photograph of any real work anywhere in my render; on phone the first row's figure is a drawn line schematic that looks like a chart, not a snake robot; on tablet the right-hand column of rows 01, 02, 03, 08, 09 is nearly empty beside rows with stamps, so rhythm is uneven.
- SEO: 7/10. Per repo: unique titles and descriptions, canonical, OG/Twitter, JSON-LD, sitemap, robots, 404. Unverifiable offline: live og:image fetch, field LCP/CLS.
- UX: 7/10. Home answers who, where, what and next step; contact is only in the footer on phone (below nine rows) and the header on phone shows Home/About/Projects plus theme toggle, with no Resume or contact link above the fold except in the lede.
- Fun and personality: 7/10. Strike-through, stamps, "Sheet 1 of 9 . NTS" are authored. Only 4 of 9 rows have a stamp.

## Findings (ranked)
1. Major, content/UX: "Start here" (row 01) is Snake robots, the thinnest page: one section ("Why snake robots", two sentences, a link out) and a stand-in schematic, in the desktop render. Aerobraking has the real substance (46 orbits, 1 km, method, result). Owner supplies 2 to 3 true sentences on what he implemented, or decides to move the label to Aerobraking (needs no new facts). Do not invent outcomes.
2. Major, UX: no availability sentence; "2023 - 2025" at CMU is past as of November 2026 and the page does not say what he is doing or seeking now. Owner supplies it.
3. Major, robustness: Resume is a single Wix filesusr URL repeated in header, lede and footer. Needs owner's assets/resume.pdf.
4. Major, visual: no photo of a robot, car, satellite or person; project media are Wix hotlinks (dependency risk; could not render here, environment limit). Needs owner media.
5. Minor, visual (taste, new angle): the Snake Fig. 1 schematic is the first image on the home page on phone and in the first row, so the first image a recruiter sees is a generic drawing. The caption admits "Module count is illustrative", which is honest, but consider a smaller treatment (or none) until a real photo exists, so the first impression is not a stand-in. Trade-off: removing it makes row 01 text-only like the others.
6. Minor, UX: on phone, contact is reachable only via the lede's Resume/LinkedIn links or the footer after a very long scroll (home page screenshot is about 2000 css px tall). Header has no contact link on phone. Designer-fixable: a LinkedIn link in the phone header area if it fits the 44 px row, else leave.
7. Minor, CLS: figures lack width/height or aspect-ratio (web.dev CLS, carried). Needs owner dimensions.
8. Minor, robustness: Aerobraking prose says "as shown below" and "above" about figures that depend on hotlinks. Same blocker as 4.
9. Minor, performance: two Google fonts, no size-adjusted fallback. Needs self-hosted WOFF2 or measured metrics.
10. Minor, content: Raftar says "40+ students" and "captained" only. Add only owner-confirmed specifics.
11. Nit, fun (taste): stamps on 4 of 9 rows; add only where a true number exists.
12. Nit, UX (taste): phone header shows only the K mark; name is in the home H1.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps where the number is the point; ruled index with mono numbers; inverted footer and flat dark theme; double rules; "Sheet N of 9 . NTS" title-block captions; honest "schematic" captions; accurate colophon; 44 px tap targets; one-line phone filter row; Previous/Next footers with a real detail; local og:image with alt; JSON-LD; 404 page; reduced-motion block.

## Verdict
The site commits to the retro matte direction and reads as one person's work; both owner constraints are met and nothing regressed. Almost everything left is blocked on owner facts, files or a decision on the "Start here" label (1 to 4, 7 to 10). The only designer-side items are small taste calls (5, 6). Research this cycle was not refreshed because fetches were blocked, so no new external claims are made.
