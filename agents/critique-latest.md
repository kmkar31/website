# Critique, 2026-10-30 (cycle 48)

Rendered with tools/check.py (13 pages x 3 viewports x 2 themes: all OK, only sandbox image-load notes). Looked at home phone light, home desktop light, home tablet dark, snake-robots phone dark. HEAD ab823b2 added the figure placeholder (cycle 47 fix); no regression seen. No site files edited.

## Sources consulted
WebFetch was blocked for all three attempts this cycle ("permission not answered, do not retry"). Not fetched; cited from prior knowledge and unverified:
- https://web.dev/articles/optimize-cls (set width/height or aspect-ratio on images so space is reserved)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (24 px minimum; site uses 44 px)
- https://www.nngroup.com/articles/mobile-ux/ (short, scannable mobile content)
Repo checks: titles and descriptions unique; og:image absolute; sitemap and robots present; 404 has noindex; resume is a filesusr.com (Wix) hotlink on every page; snake-robots figures are static.wixstatic.com, lazy, no width/height; STATUS in build/build.py is still empty; sitemap lastmod values (2026-10-24 to 10-28) predate the cycle 47 CSS/JS change.

## Scores
- AI-tell score: 2/10, unchanged. Authored voice: Fig. 1 plate, stamps tied to real numbers (46 orbits, 500 m, 99 s, podium), struck-through "three weeks" on a highlighter band, "For the record" ledger, colophon. No tells moved. Faint tell: very even ruled rows with a right-hand index/tag column.
- Looks good: 7/10. Warm paper, double rules, steady rhythm; desktop and tablet dark both calm and legible. Held back by no photograph of a real object or person, and rows 02 to 09 being text-only beside one plated row.
- SEO: 7/10. Complete tags, sitemap, robots, noindex 404. CLS cannot be verified offline.
- UX: 7/10. Phone first screen gives who, where, what, a button, resume, LinkedIn. No status line; LinkedIn only.
- Fun and personality: 7/10. Stamps, 99 s hold, 404, colophon. Quiet but earned.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like, no glossy gradients: met (flat surfaces, rules, one hard-shadow button, faint grain, no gradients or blur).
2. Must not look AI-generated: met, 2/10.

## Ranked findings
1. Major, content: no status line. Pages say Master's 2023 - 2025 and today is 2026-10-30; a recruiter cannot tell whether he has graduated, where he is, or if he is available. Needs one owner sentence (STATUS slot in build.py is ready). Not designer-fixable.
2. Major, content: "Start here" (Snake robots) is the thinnest project: a schematic, a question, no result or number (see snake-robots phone shot). Aerobraking (46 orbits) is stronger. Owner supplies outcomes or moves the label.
3. Major, robustness: the resume and every real project figure are Wix hotlinks; one Wix change silently breaks the primary call to action. Owner must add assets/resume.pdf and media.
4. Major, visual: no photograph of a real object or person (snake robot, RFR23 car, podium). First impression is type and drawings only. Needs owner files.
5. Minor, performance: figures still lack width/height; the cycle 47 220px placeholder reserves space but will not match real aspect ratios, so some shift remains. Cannot verify offline. Real fix needs local images.
6. Minor, content: Raftar facts repeat (40+ students, captained, suspension and brakes) across home, About and project page without specifics; the Ferrari weight / 0-60 claim awaits owner confirmation.
7. Minor, readability: Aerobraking is a long run of dense paragraphs that point at figures ("as shown below") which live in Wix images.
8. Minor, performance: no size-adjusted fallback for DM Serif Display / Source Serif 4; font swap can reflow headings. Needs real metrics or self-hosted WOFF2.
9. Minor, accessibility: figure alt text is generic ("Modular snake robot, figure 1 of 3", three in the same pattern) and says nothing about what each shows. Needs the images.
10. Minor, SEO: sitemap lastmod predates the latest CSS/JS edit. Trivial.
11. Nit, contact: LinkedIn only (owner constraint).
12. Nit: stamps on four rows; add none without real numbers.
13. Nit: on desktop About leaves the right third empty (documented taste).

Only owner-supplied facts or files can move findings 1 to 4; further designer cycles will churn.

## Good, must not regress
- Home phone first screen: name, degree line, two plain real-fact paragraphs, struck-through "three weeks", one button, resume and LinkedIn.
- Fig. 1 plate with honest caption; stamps tied to real numbers.
- Ruled project index with 44 px targets; Previous/Next pager on project pages.
- Dark theme as inverted print (amber button, tan rules); ink footer; 404 and colophon voice.
- Type: DM Serif Display, Source Serif 4, mono for metadata.
- Aerobraking page: key-results row, orbit diagram, sheet tag.

## Verdict
A coherent retro matte direction with specific plain copy, clean checks and no regressions. The 7s are held by missing owner material: a status sentence, a real resume PDF and photos, outcomes for the "Start here" project, and Raftar specifics. The one designer-fixable craft gap (reserved figure space) was addressed last cycle, with residual shift until images are local. Research was blocked this cycle, so the cited guidance is unverified.
