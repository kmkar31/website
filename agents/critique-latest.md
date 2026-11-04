# Critique, 2026-11-04 (cycle 76)

Rendering: `python3 tools/check.py . agents/shots` ran (about 5 minutes): 78 OK lines, no failures, no overflow, only "images not loaded, likely sandbox network" notes. I viewed index-phone-light, projects-tablet-dark and snake-robots-desktop-light. I edited no site files; this report is the only file written.

Honesty note on research: WebFetch was blocked again (W3C WCAG 2.2 page, permission request unanswered). I read no source page this cycle, so no finding relies on an external claim. Carried pointers only: W3C SC 2.5.8 Target Size, SC 2.4.11 Focus Not Obscured, SC 1.4.12 Text Spacing, web.dev optimize-cls.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone with grain, double ink rules, hard-offset red button, mono ledger labels, boxed stamps, inverted footer, flat dark theme. No gradient, blur or glow in any screenshot.
2. Must not look AI-generated: met. Ruled index, struck "three weeks" in a marker band, stamps, Fig. captions, plain specific copy. No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine identically ruled rows; DM Serif plus a mono label is a common editorial pairing. No tells moved.
- Looks good: 7/10. Phone home page has clear order and rhythm. Weak spots: no photograph of any real work; on the tablet projects list the right column (number, stamp, tags) floats far from the title with a wide empty gutter; the snake page (row 01, the first thing a reader clicks) is mostly a schematic and two sentences.
- SEO: 7/10. Per repo: unique titles and descriptions, one h1, canonical, absolute og:image, JSON-LD, sitemap, robots.txt, 404. Not verifiable offline: live og:image fetch, field LCP and CLS.
- UX: 7/10. Name, role, one strong project and contact path are in the first screen on phone.
- Fun and personality: 7/10. Strike-through, stamps, "Sheet N of 9 . NTS" are authored. Do not add stamps without a true number.

## Findings (ranked)
1. Major, content (owner facts): no current-status sentence. About says CMU "2023 - 2025" and today is November 2026; a recruiter cannot tell whether he has graduated, is employed or is looking. STATUS slot in build.py is empty. Owner supplies one line.
2. Major, robustness (owner file): Resume is a single Wix filesusr URL used in header, lede, footer, About and the 404 page. One dead URL breaks all. Owner adds assets/resume.pdf.
3. Major, visual and robustness (owner files): no real photograph; project media are Wix hotlinks (Aerobraking has 9 references and its prose says "as shown below"). If Wix changes URLs the pages read as broken.
4. Major, content (owner facts): Snake robots, the first row, has no outcome. Its page (desktop render) is a schematic, "Why snake robots" (two sentences, one link out) and Next. Raftar has only "40+ students" and "captained". A first project with nothing measured weakens the 30-second pitch. Owner supplies confirmed specifics. Designer-side option, no new facts: nothing.
5. Minor, UX (taste): on the tablet projects list the title column and the metadata column are separated by about 150px of blank space and the filter row sits far above the first row (about 70px dead gap under the chips). Tightening the gap under the filters would help scanning. Taste.
6. Minor, UX: phone header has no contact link; contact lives in the lede and footer. Accepted given the 44px row.
7. Minor, CLS: figures lack width and height or aspect-ratio. Needs owner dimensions.
8. Minor, performance: two Google fonts with no self-hosted WOFF2 or measured size-adjust. Needs files.
9. Nit, SEO (owner action): sitemap.xml and robots.txt sit at a project-site subpath, so crawlers will not find robots.txt at the host root; submit the sitemap in Search Console.
10. Nit, visual (taste): About on desktop leaves the right third empty; accepted by the designer.

No new designer-fixable defect beyond finding 5 (taste), and no regression from cycle 75.

## Good, must not regress
The plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted footer and flat dark theme; double rules; "Sheet N of 9 . NTS" captions; honest "schematic" captions; one-line "Fig. 1 - Orbits" caption; accurate colophon; 44px tap targets; one-line phone filter row; Previous/Next footers with a real detail; local og:image; JSON-LD; 404 page; reduced-motion block; Start-here on Aerobraking.

## Verdict
The site commits to the retro matte direction, reads as one person's work, and both owner constraints are met. Nothing regressed. What remains is blocked on the owner: a status line, a local resume PDF, photographs and image dimensions, and substance for Snake and Raftar. Research could not be refreshed because fetches were blocked, so I make no new external claims.
