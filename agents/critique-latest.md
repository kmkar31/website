# Critique, 2026-10-31 (cycle 51)

Rendered with tools/check.py (13 pages x 3 viewports x 2 themes: all OK, only sandbox image-load notes). Viewed home phone light, home desktop dark, snake-robots phone dark. HEAD b28ae74, no site changes since cycle 49 (CSS/JS only in 47). No regressions seen. No site files edited.

## Sources consulted
No web tools were available in this run, so no new research was done and the "three sources" rule is NOT met. These are pointers from prior knowledge, unverified here:
- WCAG 2.2, Target Size 2.5.8: https://www.w3.org/TR/WCAG22/
- web.dev, Optimize CLS: https://web.dev/articles/optimize-cls
- NN/g on portfolio and recruiter scanning: https://www.nngroup.com/articles/
A networked cycle should verify them.

## Scores
- AI-tell score: 2/10, unchanged. No gradients, glass, blobs or card trio. Authored: struck-through "three weeks" on a highlighter band, "For the record" ledger, stamps tied to real numbers, graph-paper figure with sheet tags, colophon. Faint tell: nine identically ruled rows. No tells moved.
- Looks good: 7/10. Coherent paper and inverted-print dark themes, even rhythm. Held back by no photograph of any real object or person; only row 01 has a visual and it is a schematic.
- SEO: 7/10. Head tags, JSON-LD, sitemap, noindex 404 present. LCP/CLS on hotlinked Wix images cannot be verified offline.
- UX: 7/10. Phone first screen answers who, where, what, next step. No status line; LinkedIn is the only contact route.
- Fun and personality: 7/10. Stamps, 99 s hold, 404 line, colophon. Quiet but earned.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like, no glossy gradients: met (flat paper, rules, hard-shadow button, inverted-print dark).
2. Must not look AI-generated: met, 2/10.

## Ranked findings
1. Major, content: no status line. CMU Master's is listed as 2023-2025; today is 2026-10-31. A recruiter cannot tell if he has graduated, where he is, or if he is available. Needs one owner sentence (STATUS slot in build/build.py). Not designer-fixable.
2. Major, robustness: the Resume (PDF) link, the primary call to action, points to a Wix filesusr.com URL (index.html header, hero, footer). assets/ holds only og.png, site.js, style.css. If Wix moves it, it breaks. Owner must add assets/resume.pdf.
3. Major, content: "Start here" (Snake robots) is the thinnest project page: a schematic, a question, lab and advisor, no result and no statement of what he did. Aerobraking (46 orbits) is stronger. Owner to supply outcomes or move the label.
4. Major, visual: no photograph of a real object or person (snake robot, RFR23 car, podium). First impression is type and drawings only. Needs owner files.
5. Minor, performance: Wix figures lack width/height; the 220 px placeholder will not match real aspect ratios, so some shift remains. Real fix needs local images.
6. Minor, content: Raftar claims (40+ students, captained, suspension and brakes) repeat across home, list, About and project page with no specifics. Ferrari weight / 0-60 claim awaits owner confirmation.
7. Minor, readability: Aerobraking is still long dense prose pointing at Wix images.
8. Minor, performance: no size-adjusted fallback for DM Serif Display / Source Serif 4; font swap can reflow headings. Needs real metrics or self-hosted WOFF2.
9. Minor, accessibility: Wix figure alt text is generic ("figure 1 of 3").
10. Minor, UX: phone header shows only the "K" mark; the H1 name sits directly below, so harmless. Taste.
11. Nit: contact is LinkedIn only (owner constraint).
12. Nit: stamps on four of nine rows; add none without real numbers.
13. Nit: on desktop About leaves the right third empty (documented taste).

Findings 1 to 4 move only with owner-supplied facts or files. Further designer cycles will churn.

## Good, must not regress
Plain-prose home intro with the highlighted "three weeks to 15 minutes"; ruled project index with real-number stamps; "For the record" ledger; graph-paper figure plate; warm paper and inverted-print dark themes; hard-offset button; 404 voice; colophon; clear back/next links on project pages.

## Verdict
The site commits coherently to the retro matte direction and reads as authored, not generated. What holds it at 7s is not design craft but missing owner inputs: a status sentence, a local resume, a result for the "Start here" project, and real photographs. Until those arrive, the designer has little left to fix.
