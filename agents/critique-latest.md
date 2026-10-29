# Critique, 2026-10-29 (cycle 42)

Rendered with tools/check.py (13 pages x 3 viewports x 2 themes: all OK, only sandbox image-load notes). Looked at home phone light, home desktop light, About desktop dark, Aerobraking phone dark. No site files edited. No regression versus cycle 41 (no site changes since).

## Sources consulted
Fetches were blocked by the permission layer again (WCAG 2.2 target-size-minimum on w3.org; earlier cycle: web.dev optimize-cls, WCAG contrast-minimum, NN/g mobile UX). I did not retry. No source was fetched this cycle, so principle citations below are from prior knowledge and are unverified:
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (24 px minimum; site uses 44 px, passes)
- https://web.dev/articles/optimize-cls (image dimensions, font swap)
- https://www.nngroup.com/articles/mobile-ux/ (short scannable mobile content)
Last fetched sources from earlier cycles (size-adjust, hiring-manager portfolio structure) still stand.

## Scores
- AI-tell score: 2/10. Unchanged, no tells moved. Authored print-notebook voice: Fig. 1 plates, stamps only with real numbers, struck-through "three weeks", "For the record" ledger, 404 and colophon. Faint tell: very even ruled rows with right-hand index/tag column.
- Looks good: 7/10. Palette, double rules, ink footer and dark theme are coherent and the desktop home reads well. Held back by having no photograph of any real object or person, and rows 02 to 09 being text-only next to the one plated row 01.
- SEO: 7/10. Titles, descriptions, canonical, OG, JSON-LD, sitemap, 404 all present. robots.txt and sitemap sit under /website/, not host root (owner: submit sitemap in Search Console). Hotlinked Wix image dimensions unknown, so CLS cannot be verified offline.
- UX: 7/10. First phone screen shows name, degree, two factual paragraphs, one button, resume and LinkedIn; the pager has no dead ends. Weakness is content depth and a missing status line.
- Fun and personality: 7/10. Press-and-hold 99 s stamp, stamps, 404, colophon. Quiet but earned.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like: met (flat surfaces, hairline and double rules, one hard-shadow button, faint grain, no gradients or blur; dark theme is inverted print).
2. Not AI-looking: met; I do not disagree with the score above.

## Ranked findings
1. Major, content: no status line. About and home say Master's 2023 - 2025 ("is at Carnegie Mellon"); today is 2026-10-29. A recruiter cannot tell whether he has graduated, where he is now, or if he is available. Needs one owner sentence (STATUS slot in build.py is ready). Not designer-fixable.
2. Major, content: "Start here" (Snake robots) is the thinnest project page: no result, no number, no photograph; its plate caption admits the schematic is illustrative. Owner either supplies what was done and what happened, or moves the label to Aerobraking (46 orbits). Owner decision.
3. Major, robustness: resume and all real project figures are Wix hotlinks. One Wix change silently breaks the primary call to action. Owner must add assets/resume.pdf and media.
4. Major, visual: no photograph of a real object or person anywhere (snake robot, RFR23 car, podium). First-3-second impression is type and drawings only. Needs owner files.
5. Minor, content: Raftar page states the same facts (40+ students, captained, suspension and brakes) repeatedly in the first screen, and adds no specific beyond the home row. The real fix is owner facts (what changed, mass, rank). The Ferrari weight / 0-60 claim in the page question still awaits owner confirmation.
6. Minor, readability: Aerobraking on phone (dark) is still a long run of dense paragraphs between the plate and the Result ledger; the Problem and Method sections have no sub-structure. Taste/length; the paper's order is honest, so only a light touch (for example a pull-out of the reward function) would help, and only if the owner agrees.
7. Minor, performance: no size-adjusted fallback for DM Serif Display / Source Serif 4, so display=swap can reflow headings. Needs real metrics or self-hosted WOFF2; blocked offline.
8. Minor, accessibility: alt text for Wix figures cannot be checked offline.
9. Nit, contact: LinkedIn only (owner constraint); acceptable.
10. Nit: stamps on four rows; do not add more without real numbers.
11. Nit: About on desktop leaves the right third empty below the "On this page" box (documented, taste).

Unfixable offline, keep open and do not re-argue: 1, 2, 3, 4, 5 (facts part), 7, 8.

## Good, must not regress
- Home phone first screen: name, degree line, two plain real-fact paragraphs, struck-through marker, one button, resume and LinkedIn.
- Fig. 1 plates with sheet tags and honest "illustrative" captions.
- Stamps only where a real number exists (99 s, 46 orbits, 500 m, podium).
- Source Serif 4 as the single UI voice, 44 px targets, double rules, ink footer band, dark theme.
- Press-and-hold 99 s button (keyboard operable), pager without wraparound, aerobraking ledger.
- 404 copy and colophon.

## Verdict
Coherent, specific and well built; there is no designer-fixable defect and no regression. What remains is content only the owner can supply: a status sentence (the 2023 - 2025 dates are now stale), real outcomes or a swapped "Start here" project, a local resume PDF, photographs, and Raftar specifics. Further CSS polish has sharply diminishing returns, and the designer should not invent facts, stamps or jokes. Research this cycle was again limited because external fetches were blocked.
