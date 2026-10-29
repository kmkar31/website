# Critique, 2026-10-29 (cycle 41)

Rendered with tools/check.py (13 pages x 3 viewports x 2 themes: all OK, only sandbox image-load notes). Looked at home phone light, home tablet light, home desktop dark, Raftar phone light. No site files edited. No regression found since cycle 40 (git status clean).

## Sources consulted
Three WebFetch calls (web.dev optimize-cls, W3C WCAG 2.2 contrast-minimum, NN/g mobile UX) were blocked by the permission layer and were not retried. I therefore have NO fetched sources this cycle. The points below that cite a principle rely on my prior knowledge of these documents and are unverified this cycle:
- https://web.dev/articles/optimize-cls (images need width/height or aspect-ratio; font swap shifts)
- https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html (4.5:1 body, 3:1 large text)
- https://www.nngroup.com/articles/mobile-ux/ (short scannable mobile content, prominent contact)
Last cycle's fetched sources (size-adjust, WCAG 2.5.8, hiring-manager portfolio structure) still stand.

## Scores
- AI-tell score: 2/10. Unchanged. Specific print-notebook voice (Fig. 1 plates, stamps, struck-through "three weeks", "For the record"). No tells moved. Faint tell: the ruled rows with right-hand number/tag column are very tidy; acceptable.
- Looks good: 7/10. Coherent paper palette, double rules, ink footer, dark theme holds up (desktop dark home has good contrast and hierarchy). Still type-only: only row 01 has any image, nothing photographic anywhere. Tablet home shows the hero text column leaving the right ~20% empty while the stamp column sits far right of short titles; fine, but rows 02 to 09 feel flat compared with row 01 because only one has a plate.
- SEO: 7/10. Unchanged (titles, descriptions, canonical, OG, JSON-LD, sitemap, robots, 404). robots.txt and sitemap live under /website/, not host root; owner must submit the sitemap in Search Console. Hotlinked Wix images: dimensions unknown, CLS unverifiable offline.
- UX: 7/10. Name, field, resume, LinkedIn and the strongest hook are visible in the first phone screen. Pager shows no dead ends. Weakness is content depth (findings 1 to 3).
- Fun and personality: 7/10. Press-and-hold 99 s button, stamps, 404 and colophon remain charming; quiet but earned.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like: met (flat surfaces, rules, one hard-shadow button, faint grain, no gradients or blur; dark theme is inverted print).
2. Not AI-looking: met per score above. No disagreement.

## Ranked findings

1. Major, content: no status line. About and home still imply Master's 2023 - 2025; today is 2026-10-29. A recruiter cannot tell if he has graduated, is available, or where he works. Needs one owner sentence. Not designer-fixable.
2. Major, content: "Start here" (Snake robots) is the thinnest project page: no result, no number, no photo, plate caption admits the module count is illustrative. Owner supplies outcomes, or moves "Start here" to Aerobraking (46 orbits). Owner decision.
3. Major, robustness: resume and all real project figures are Wix hotlinks. One Wix change breaks the primary call to action silently. Owner must add assets/resume.pdf and media.
4. Major, visual: no photograph of a real object or person anywhere (snake robot, RFR23 car, podium). Taste plus first-3-second impression. Needs owner files.
5. Minor, content (new observation): on the Raftar page the same facts are stated three times in the first screen (lede "built and raced by 40+ students ... captained ... suspension and brakes", then Team "40+ students" and Result "Podium", then the figure caption "I did the suspension and brakes", then the body "A team of 40+ engineering students"). The page adds no specific beyond the home row. Designer could trim the duplicated "40+ students" in the body, but the real fix is owner facts (what changed in suspension or brakes, mass, rank). Also the question asks about a Ferrari weight and 0-60 claim that still awaits owner confirmation.
6. Minor, performance: no size-adjusted fallback for DM Serif Display / Source Serif 4 (display=swap reflows headings). Needs real font metrics or self-hosted WOFF2; sandbox proxy blocks Google Fonts. Not fixable offline.
7. Minor, accessibility: alt text for Wix figures cannot be verified offline.
8. Nit, contact: LinkedIn only (owner constraint); acceptable.
9. Nit: stamps now on four rows; do not add more without real numbers.
10. Nit: About on desktop leaves the right third empty (documented, taste).

Unfixable offline, keep open and do not re-argue: 1, 2, 3, 4, 5 (facts part), 6.

## Good, must not regress
- Home phone first screen: name, degree line, two plain real-fact paragraphs, struck-through marker, one button, resume and LinkedIn.
- Fig. 1 plates with "Sheet n of 9 . NTS" and honest "illustrative" captions.
- Stamps only where a real number exists (99 s, 46 orbits, 500 m, podium).
- Source Serif 4 as the single UI voice, 44 px targets, double rules, ink footer band, dark theme.
- Press-and-hold 99 s button (keyboard operable), pager without wraparound, aerobraking ledger.
- 404 copy and colophon.

## Verdict
Coherent, specific, well built; no designer-fixable defect and no regression. The remaining gaps are content only the owner can supply: a status sentence, real outcomes for the "Start here" page, a local resume and photographs, and Raftar specifics. Further CSS polish has sharply diminishing returns; the designer should not invent facts, stamps or jokes. Note this cycle's research was limited because external fetches were blocked.
