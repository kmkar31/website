# Critique, 2026-10-30 (cycle 50)

Rendered with tools/check.py (13 pages x 3 viewports x 2 themes: all OK, only sandbox image-load notes). Looked at home phone light, home desktop dark, About tablet light, snake-robots phone dark. HEAD 3b1ef1b; no site changes since cycle 49, so no regressions. No site files edited.

## Sources consulted
WebSearch and WebFetch were not loaded in this run, so no new research was done. These are pointers from prior knowledge, not verified quotes:
- WCAG 2.2 Focus Not Obscured (2.4.11) and Target Size (2.5.8): https://www.w3.org/TR/WCAG22/
- web.dev, Optimize CLS (set width/height, size-adjust font fallbacks): https://web.dev/articles/optimize-cls
- NN/g, how recruiters review portfolios (state outcomes and your own role): https://www.nngroup.com/articles/
- Cycle 49's search-result pointers (debugbear font layout shift, uxtools case studies) still apply.
The "at least three sources" rule is met only in the weak sense. A networked cycle should verify them.

## Scores
- AI-tell score: 2/10, unchanged. No gradients, glass, blobs or stock card trio. Specific copy and authored marks (struck-through "three weeks" on a highlighter band, stamps tied to real numbers, "For the record" ledger, graph-paper plates with sheet tags, colophon). Faint tell: nine rows with the same ruled anatomy. No tells moved.
- Looks good: 7/10. Coherent warm paper and dark inverted-print themes, even rhythm. Held back by having no photograph of a real object or person. Only row 01 has a visual, and it is a schematic.
- SEO: 7/10. Full head tags, JSON-LD, sitemap, noindex 404, unique descriptions. LCP and CLS on hotlinked Wix images cannot be verified offline.
- UX: 7/10. The phone first screen answers who, where, what and next step. No status line. LinkedIn is the only contact route.
- Fun and personality: 7/10. Stamps, 99 s hold, 404 line, colophon. Quiet but earned.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like, no glossy gradients: met (flat paper, rules, hard-shadow button, faint grain, inverted-print dark mode).
2. Must not look AI-generated: met, 2/10.

## Ranked findings
1. Major, content: no status line. About says the Master's "is at" CMU (2023 - 2025), and today is 2026-10-30. A recruiter cannot tell whether he has graduated, where he is now, or whether he is available. Needs one owner sentence (the STATUS slot in build/build.py is ready). Not designer-fixable.
2. Major, content: "Start here" (Snake robots) is the thinnest project page. It has a schematic, a question and a lab/advisor pair, but no result and no statement of what he did. Aerobraking (46 orbits) is stronger. The owner should supply outcomes or move the label.
3. Major, robustness: the resume and all real project figures are Wix hotlinks. One host change breaks the primary call to action. The owner must add assets/resume.pdf and the media.
4. Major, visual: no photograph of a real object or person (snake robot, RFR23 car, podium). The first impression is type and drawings only. Needs owner files.
5. Minor, performance: figures lack width/height. The 220 px placeholder from cycle 47 will not match real aspect ratios, so some shift remains (web.dev CLS). The real fix needs local images.
6. Minor, content: Raftar facts (40+ students, captained, suspension and brakes) repeat across home, list, About and the project page with no specifics. The Ferrari weight / 0-60 claim still awaits owner confirmation.
7. Minor, readability: Aerobraking is still a long run of dense prose pointing at Wix images. The Result ledger helped.
8. Minor, performance: no size-adjusted fallback for DM Serif Display / Source Serif 4, so a font swap can reflow headings. Needs real metrics or self-hosted WOFF2.
9. Minor, accessibility: figure alt text on Wix images is generic ("figure 1 of 3"). Needs the images or owner descriptions.
10. Minor, UX: on phone the header shows only the "K" mark and not the name. The H1 sits directly below, so it is harmless. Desktop shows the name. Taste-level.
11. Nit, contact: LinkedIn only (owner constraint).
12. Nit: stamps on four of nine rows. Add none without real numbers.
13. Nit: on desktop About leaves the right third empty (documented taste).

Findings 1 to 4 can only move with owner-supplied facts or files. Further designer cycles will churn.

## Good, must not regress
- Home phone first screen: name, degree line, two plain real-fact paragraphs, struck-through "three weeks", one button, resume and LinkedIn.
- Fig. 1 plates with honest captions and sheet tags; stamps tied to real numbers.
- Ruled project index with 44 px targets; Previous/Next pager with a real metric.
- Dark theme as inverted print (amber button, tan rules); ink footer; 404 and colophon voice.
- Type: DM Serif Display, Source Serif 4, mono for metadata.
- Aerobraking key results and orbit diagram.
- Skip link, focus-visible outline, scroll-padding, reduced-motion handling.

## Verdict
A coherent retro matte direction with specific plain copy and no template tells. No regressions this cycle. The 7s are held by missing owner material: a status sentence, a local resume PDF and photographs, outcomes for the "Start here" project, and Raftar specifics. Nothing designer-fixable of substance remains. The remaining craft gaps (figure dimensions, font metrics, alt text) depend on local assets. Research this cycle was not run, so the cited guidance is unverified.
