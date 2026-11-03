# Critique, 2026-11-03 (cycle 72)

Rendering: `python3 tools/check.py . agents/shots` completed (first run hit my tool timeout, rerun in background finished); every page reported OK, only "images not loaded, likely sandbox network" notes. I viewed index-phone-light, index-desktop-light and aerobraking-drl-desktop-light. Working tree clean; last commit was the phone filter-chip fix, which this cycle's phone Projects render does not contradict. No regression found. I edited no site files.

Honesty note on research: WebFetch was blocked this cycle (permission not answered), and WebSearch returned only result titles. So I did NOT read any new source page this cycle. Sources below are links surfaced by search or carried from earlier cycles; treat claims attributed to them as unverified this cycle except where marked "carried".

## Sources
- W3C, Understanding SC 2.5.8 Target Size (Minimum), https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (search hit only, not read; site's 44 px targets exceed the 24 px minimum regardless).
- Chrome, Optimize image priority, https://developer.chrome.com/docs/modern-web-guidance/guides/performance/optimize-image-priority (search hit only, not read).
- Addy Osmani, fetchpriority=high for the LCP hero image, https://addyosmani.com/blog/fetch-priority/ (search hit only, not read).
- Carried from earlier cycles (read then): web.dev CLS https://web.dev/optimize-cls/ ; W3C SC 2.4.11 ; W3C SC 1.4.12 ; UX Design Institute hiring-manager portfolio guidance.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper ground with grain, double ink rules, hard-offset button, mono ledger labels, ruled stamps, inverted footer. No gradient, blur or glow in the screenshots.
2. Must not look AI-generated: met. Ruled index instead of cards, struck-through "three weeks", Fig. captions, plain colophon, specific numbers. No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine identically ruled rows; DM Serif Display plus Source Serif pairing is a popular editorial combination. No tells moved.
- Looks good: 7/10. Desktop home and the Aerobraking page are composed (title, deck, "The question", stat strip, schematic, then prose). Weaknesses: no real photograph anywhere in my render, and the Aerobraking body is long unbroken prose after the first screen.
- SEO: 7/10. Per repo: unique title and description, absolute og:image with width/height/alt, JSON-LD (CreativeWork on projects), sitemap, robots, 404. Unverifiable offline: live og:image fetch, field LCP/CLS.
- UX: 7/10. Home answers who, where, what, next step, and contact is in the footer. Gaps: no availability line, Resume on a Wix URL, flagship project thin.
- Fun and personality: 7/10. Strike-through, stamps, "Sheet 6 of 9 . NTS" caption are authored touches. Still only 4 of 9 rows carry a stamp.

## Findings (ranked)
1. Major, content/UX: "Start here" (row 01) is Snake robots, the thinnest page, with a stand-in schematic ("Fig. 1 . Snake robot" is a drawn illustration, not his work) while Aerobraking has problem, setup, method, result and numbers (8.4 km, 1.1M steps, 46 orbits). Owner supplies 2 to 3 true sentences on what he implemented, or decides to move the label to Aerobraking (needs no new facts). Do not invent outcomes.
2. Major, UX: no availability or status sentence; "2023 - 2025" at CMU is past. Owner supplies the sentence; leave STATUS empty until then.
3. Major, robustness: Resume is a single Wix filesusr URL repeated in header, lede and footer on every page. Needs owner's assets/resume.pdf.
4. Major, visual: no photo of a robot, car, satellite or person; project media are Wix hotlinks, a dependency risk (could not render here; environment limit). Needs owner media.
5. Minor, performance (new): `loading="lazy"` is set on every figure including project-list thumbnails (projects.html has 9 lazy imgs). If a thumbnail or the first figure is the LCP element, lazy-loading it delays LCP; guidance is to leave above-the-fold images eager and use fetchpriority="high". Designer can safely make the first visible image per page eager now; cannot verify real LCP offline.
6. Minor, CLS: figures on project pages have no width/height or aspect-ratio (web.dev CLS, carried). Needs owner dimensions; do not guess.
7. Minor, robustness: Aerobraking prose says "As shown in the figure above", "As shown below" (reward formulation) and "as shown below" (result). If Wix images fail the text points at nothing. Designer-fixable partly: the first "above" now has the local Fig. 1 schematic nearby, but the later ones depend on hotlinks.
8. Minor, performance: two Google fonts, no size-adjusted fallback or preload. Needs self-hosted WOFF2 or measured metrics.
9. Minor, content: Raftar says "40+ students", "captained", "suspension and brakes" and little more. Add only owner-confirmed specifics.
10. Minor, fun (taste): stamps on 4 of 9 rows; add only where a true number exists.
11. Nit, readability (taste): Aerobraking body runs about 10 paragraphs with no pull-out between "Method" and "Result" except the code block; one more stat or caption from the real results would help scanning. Use only numbers already on the page.
12. Nit, UX (taste): phone header shows only the K mark; name is in the home H1.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps where the number is the point; ruled index with mono numbers; inverted footer and flat dark theme; double rules; "Sheet N of 9 . NTS" title-block captions; honest "schematic" captions; accurate colophon; 44 px tap targets; scroll-padding-top over the sticky header; Previous/Next footers with a real detail; one-line phone filter row; local og:image with alt; JSON-LD; 404 page; reduced-motion block.

## Verdict
The site commits to the retro matte direction and reads as one person's work; both owner constraints are met and nothing regressed. Little remains that the designer can fix alone: the one new designer-side item is eager-loading the first visible image (5). Everything else (1 to 4, 6, 8, 9) is blocked on owner facts, files or a decision on the "Start here" label. Because I could not read new sources this cycle, treat the performance guidance in 5 as standard practice to be confirmed, not a freshly verified citation.
