# Critique, 2026-11-04 (cycle 75)

Rendering: `python3 tools/check.py . agents/shots` ran (about 4 minutes): 78 OK lines, no failures, no overflow, only "images not loaded, likely sandbox network" notes. Working tree was clean. I viewed index-phone-light, index-desktop-light and aerobraking-drl-phone-dark. I edited no site files other than this report.

Honesty note on research: WebFetch was blocked again (web.dev optimize-cls permission request unanswered). One WebSearch on portfolio guidance for hiring managers returned titles and links only, which I did not open. I read no source page this cycle, so the links are pointers, not verified claims. No finding relies on them.

## Sources
- Blocked, not read: https://web.dev/articles/optimize-cls
- Search results only, not opened: https://www.dice.com/career-advice/your-first-resume-and-portfolio-what-tech-hiring-managers-really-want-to-see ; https://soychristian.pages.dev/contents/developer-portfolio-guide
- Carried from earlier cycles, not refreshed: W3C SC 2.5.8 Target Size, SC 2.4.11 Focus Not Obscured, SC 1.4.12 Text Spacing.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone with grain, double ink rules, hard-offset red button, mono ledger labels, stamps, inverted footer, flat dark theme. No gradient, blur or glow in any screenshot I viewed.
2. Must not look AI-generated: met. A ruled index, the struck "three weeks" in a marker band, stamps, Fig. captions, plain specific copy. No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine identically ruled rows; a common editorial serif look. No tells moved.
- Looks good: 7/10. Clear order on phone and desktop. Cycle 74's caption fix is confirmed: "Fig. 1 · Orbits" is on one line. Weak spots: no photograph of any real work; on desktop the right column is empty beside unstamped rows; the aerobraking page in my render shows prose saying "as shown in the figure above" with figures missing (sandbox, but see 3).
- SEO: 7/10. Per repo: unique titles and descriptions, one h1 per page, canonical, absolute og:image on a local asset, JSON-LD, sitemap, robots.txt, 404. Not verifiable offline: live og:image fetch, field LCP and CLS.
- UX: 7/10. Name, role, strongest project and a next step are in the first screen.
- Fun and personality: 7/10. Strike-through, stamps, "Sheet N of 9" are authored. Only 4 of 9 rows have stamps; do not add any without a true number.

## Findings (ranked)
1. Major, content (owner facts): no current-status sentence. About says CMU "2023 – 2025" and today is November 2026; a recruiter cannot tell if he has graduated, is employed or is looking. STATUS slot in build.py is empty. Owner supplies one line.
2. Major, robustness (owner file): Resume is a single Wix filesusr URL, used in the header, lede, footer, About and the 404 page. One dead URL breaks all. Owner adds assets/resume.pdf.
3. Major, visual and robustness (owner files): no photograph of a robot, car, satellite or person; project media (3 to 9 references per page) are Wix hotlinks. Aerobraking has 9 filesusr/wixstatic references and its prose leans on them ("as shown below"). If Wix changes URLs the page reads as broken.
4. Major, content (owner facts): Snake robots (row 01) has no outcomes; Raftar has only "40+ students" and "captained". Add only owner-confirmed specifics.
5. Minor, UX (taste): "Start here" sits on row 06; on phone the plate does not appear until after five rows. A short lede pointer is the non-reordering option; trade-off is a longer lede. Declined last cycle with reasoning; I leave it as taste.
6. Minor, UX: the phone header has no contact link; contact is in the lede and footer. Accepted given the 44 px row.
7. Minor, CLS: figures lack width and height or aspect-ratio (web.dev CLS, carried, not refreshed). Needs owner dimensions.
8. Minor, performance: two Google fonts with no size-adjusted fallback or self-hosting. Needs WOFF2 files.
9. Nit, SEO (owner action): sitemap.xml and robots.txt sit at a project-site subpath, so crawlers will not find robots.txt at the host root; submit the sitemap in Search Console.
10. Nit, visual (taste): About on desktop leaves the right third empty; accepted by the designer.

I have no new designer-fixable defect this cycle and no regression from cycle 74.

## Good, must not regress
The plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted footer and flat dark theme; double rules; "Sheet N of 9 . NTS" captions; honest "schematic" captions; one-line "Fig. 1 · Orbits" caption; accurate colophon; 44 px tap targets; one-line phone filter row; Previous/Next footers with a real detail; local og:image; JSON-LD; 404 page; reduced-motion block; Start-here on Aerobraking.

## Verdict
The site commits to the retro matte direction, reads as one person's work, and both owner constraints are met. Cycle 74 fixed the caption wrap and introduced no regression. What remains is blocked on the owner: a status line, a local resume PDF, photographs and image dimensions, and substance for Snake and Raftar. Research was again not refreshed because fetches were blocked, so I make no new external claims.
