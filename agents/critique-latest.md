# Critique, 2026-10-30 (cycle 47)

Rendered with tools/check.py (13 pages x 3 viewports x 2 themes: all OK, only sandbox image-load notes). Screenshots are in the session scratchpad. Looked at home phone light and home desktop light. HEAD 4b278b7 is log-only, so the site is unchanged and there is no regression. No site files edited.

## Sources consulted
Fetching was blocked again this cycle (WebFetch of https://web.dev/articles/optimize-cls returned "permission not answered, do not retry"). Not fetched, from prior knowledge and unverified:
- https://web.dev/articles/optimize-cls (set width and height on images to reserve space)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (24 px minimum; site uses 44 px)
- https://www.nngroup.com/articles/mobile-ux/ (short scannable mobile content)
Repo checks: titles and descriptions unique; og:image absolute (kmkar31.github.io/website/assets/og.png); JSON-LD on content pages (not 404); resume is a filesusr.com (Wix) hotlink; project figures are static.wixstatic.com, lazy, with no width/height attributes (checked snake-robots.html); sitemap lastmod present; one reduced-motion rule.

## Scores
- AI-tell score: 2/10, unchanged. Authored voice: Fig. 1 plate, stamps tied to real numbers (46 orbits, 500 m, 99 s, podium), struck-through "three weeks" on a highlighter band, "For the record" ledger, colophon line. No tells moved. Faint tell: very even ruled rows with a right-hand index/tag column.
- Looks good: 7/10. Warm paper, double rules, steady rhythm; desktop home is calm and legible. Held back by no photograph of a real object or person and rows 02 to 09 being text-only beside one plated row.
- SEO: 7/10. Complete tags, sitemap, robots, 404. CLS unverifiable offline and likely a risk (finding 4).
- UX: 7/10. Phone first screen gives who, where, what, a button, resume and LinkedIn. No status line; LinkedIn only.
- Fun and personality: 7/10. Stamps, 99 s press-and-hold, 404, colophon. Quiet but earned.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like, no glossy gradients: met (flat surfaces, rules, one hard-shadow button, faint grain, no gradients or blur).
2. Must not look AI-generated: met, 2/10.

## Ranked findings
1. Major, content: no status line. Pages say Master's 2023 - 2025 and today is 2026-10-30; a recruiter cannot tell if he has graduated, where he is or whether he is available. Needs one owner sentence (STATUS slot in build.py is ready). Not designer-fixable.
2. Major, content: "Start here" (Snake robots) is the thinnest project (schematic, a question, no result or number) while Aerobraking (46 orbits) is stronger. Owner supplies outcomes or moves the label.
3. Major, robustness: resume and every real project figure are Wix hotlinks; one Wix change silently breaks the primary call to action. Owner must add assets/resume.pdf and media.
4. Major, performance (new, designer-fixable): project-page images carry no width/height attributes (snake-robots.html and the other Wix figures), so with lazy loading each figure pushes content down on load; layout shift risk against the CLS guidance on web.dev. Fix without inventing facts: add a CSS aspect-ratio placeholder (for example a min-height or aspect-ratio box with the paper-tone background) on figures now, and real width/height once the images are downloaded locally. Unverified offline, since images do not load in the sandbox.
5. Major, visual: no photograph of a real object or person (snake robot, RFR23 car, podium); first impression is type and drawings only. Needs owner files.
6. Minor, content: Raftar facts repeat (40+ students, captained, suspension and brakes) across home, About and project page without specifics; the Ferrari weight / 0-60 claim awaits owner confirmation.
7. Minor, readability: Aerobraking is a long run of dense paragraphs pointing at figures ("as shown below") that sit in Wix images.
8. Minor, performance: no size-adjusted fallback for DM Serif Display / Source Serif 4; font swap can reflow headings. Needs real metrics or self-hosted WOFF2.
9. Minor, accessibility: alt text on figures is short ("Aerobraking maneuver definition", "Modular snake robot, figure 1 of 3"); the snake alts are identical in pattern and say nothing about what the figure shows. Cannot judge without the images.
10. Minor, SEO: 404.html has no JSON-LD (fine) but confirm it is noindex; and the sitemap lastmod (2026-10-26) predates later edits. Trivial.
11. Nit, contact: LinkedIn only (owner constraint).
12. Nit: stamps on four rows; add none without real numbers.
13. Nit: on desktop About leaves the right third empty (documented taste).

Finding 4 is the only designer-fixable item; the rest need owner facts or files.

## Good, must not regress
- Home phone first screen: name, degree line, two plain real-fact paragraphs, struck-through "three weeks", one button, resume and LinkedIn.
- Fig. 1 plate with honest caption; stamps tied to real numbers.
- Ruled project index with 44 px targets; Previous/Next pager on project pages.
- Dark theme as inverted print; ink footer; 404 and colophon voice.
- Type: DM Serif Display, Source Serif 4, mono for metadata.
- Aerobraking page: key-results row, orbit diagram, sheet tag.

## Verdict
A coherent retro matte direction with specific plain copy, clean checks and no regressions. The 7s are held mostly by missing owner material (status sentence, real resume PDF and photos, outcomes for the "Start here" project, Raftar specifics). One craft gap remains: reserved space for hotlinked figures to limit layout shift. After that, further designer cycles will only churn until the owner supplies facts and files.
