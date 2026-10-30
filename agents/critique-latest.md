# Critique, 2026-10-30 (cycle 49)

Rendered with tools/check.py (13 pages x 3 viewports x 2 themes: all OK, only sandbox image-load notes). Looked at home phone light, projects desktop dark, raftar-formula-racing phone light. HEAD 484c2d7; no site changes since the last critique, so no new regressions. No site files edited.

## Sources consulted
WebSearch worked this cycle but returned result lists only (WebFetch not used, so page contents were not read; cited as pointers, not verified quotes):
- Hiring-manager portfolio guidance (NN/g is not in the hits; secondary): https://ntc.it.com/blog/hiring-managers-portfolio and https://www.uxtools.co/blog/5-principles-of-exceptional-case-studies-in-ux-portfolios (problem, decision, result, as the site already does)
- Font fallback metrics / CLS: https://debugbear.com/blog/web-font-layout-shift and https://shopify.dev/docs/storefronts/themes/best-practices/performance/reduce-cls-font-swapping (size-adjust and metric overrides)
- WCAG 2.2 Focus Not Obscured (2.4.11): https://tabnav.com/academy/wcag/success-criterion-2.4.11 and https://tetralogical.com/blog/2023/10/05/whats-new-wcag-2.2
- Prior-knowledge, unverified this cycle: https://web.dev/articles/optimize-cls
Repo checks: JSON-LD on all 12 content pages (404 none, fine); unique descriptions; skip link present; :focus-visible 3px outline; scroll-padding-top 80px (covers the sticky header for 2.4.11); prefers-reduced-motion block present; resume is still a filesusr.com Wix hotlink on every page; snake-robots has 2 img tags with generic alt ("figure 1 of 3"), lazy, no width/height, hosted on static.wixstatic.com.

## Scores
- AI-tell score: 2/10, unchanged. Specific copy (struck-through "three weeks" on a highlighter band, "For the record" ledger, stamps tied to real numbers, colophon "no framework") and no gradients, glass or blobs. Faint tell: every project row is the same ruled row with a right-hand index/tag column. No tells moved.
- Looks good: 7/10. Warm paper, double rules, even rhythm in both themes. Held back by no photograph of a real object or person; only one plated row among nine.
- SEO: 7/10. Complete head tags, JSON-LD, sitemap, robots, noindex 404. CLS and LCP on hotlinked images cannot be verified offline.
- UX: 7/10. Phone first screen answers who, where, what, with a button, resume and LinkedIn. No status line; LinkedIn is the only contact route.
- Fun and personality: 7/10. Stamps, 99 s hold, 404, colophon. Quiet but earned.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like, no glossy gradients: met (flat paper, rules, one hard-shadow button, faint grain).
2. Must not look AI-generated: met, 2/10.

## Ranked findings
1. Major, content: no status line. Pages say Master's 2023 - 2025 and today is 2026-10-30; a recruiter cannot tell whether he has graduated, where he is, or whether he is available. Needs one owner sentence (STATUS slot in build/build.py is ready). Not designer-fixable.
2. Major, content: "Start here" (Snake robots) is the thinnest project: a schematic and a question, no number or result. Aerobraking (46 orbits) is stronger. Owner supplies outcomes or moves the label.
3. Major, robustness: the resume and every real project figure are Wix hotlinks; one Wix change breaks the primary call to action. Owner must add assets/resume.pdf and media.
4. Major, visual: no photograph of a real object or person (snake robot, RFR23 car, podium). First impression is type and drawings only. Needs owner files.
5. Minor, performance: figures still lack width/height; the 220px placeholder will not match real aspect ratios, so some shift remains. Real fix needs local images. (web.dev CLS guidance.)
6. Minor, content: Raftar facts repeat (40+ students, captained, suspension and brakes) across home, projects list, About and the project page with no specifics; the Ferrari weight / 0-60 claim awaits owner confirmation.
7. Minor, readability: Aerobraking is a long run of dense paragraphs pointing at figures that live in Wix images.
8. Minor, performance: no size-adjusted fallback for DM Serif Display / Source Serif 4, so a font swap can reflow headings. Needs real metrics or self-hosted WOFF2.
9. Minor, accessibility: figure alt text is generic ("Modular snake robot, figure 1 of 3") and says nothing about what each shows. Needs the images.
10. Minor, UX: on phones the header shows only the "K" mark, not his name; the name appears in the H1 right below so it is harmless, but a shared deep link to a project page shows no name until the footer. Taste-level.
11. Nit, contact: LinkedIn only (owner constraint).
12. Nit: stamps on four rows; add none without real numbers.
13. Nit: on desktop About leaves the right third empty (documented taste).

Findings 1 to 4 can only move with owner-supplied facts or files; further designer cycles will churn.

## Good, must not regress
- Home phone first screen: name, degree line, two plain real-fact paragraphs, struck-through "three weeks", one button, resume and LinkedIn.
- Fig. 1 plate with honest caption; stamps tied to real numbers.
- Ruled project index with 44 px targets; Previous/Next pager with a real metric on each project page.
- Dark theme as inverted print (amber button, tan rules); ink footer; 404 and colophon voice.
- Type: DM Serif Display, Source Serif 4, mono for metadata.
- Aerobraking key-results row and orbit diagram; Raftar page's sheet-tag plate.
- Skip link, focus-visible outline, scroll-padding, reduced-motion handling.

## Verdict
A coherent retro matte direction with specific plain copy, clean checks, no regressions and no tells of a generated template. The 7s are held by missing owner material: a status sentence, a local resume PDF and photos, outcomes for the "Start here" project, and Raftar specifics. Nothing designer-fixable remains of substance; the remaining craft gaps (figure dimensions, font metrics, alt text) depend on local assets. Research this cycle was search-result level only, so cited guidance is pointers rather than verified quotes.
