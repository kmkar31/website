# Critique, 2026-11-04 (cycle 77)

Rendering: `python3 tools/check.py . agents/shots` ran (about 5 minutes): 78 OK lines, no failures, only "images not loaded, likely sandbox network" notes. I viewed index-phone-light, index-desktop-dark and aerobraking-drl-phone-light. I edited no site files; this report is the only file written. `git status` is clean.

## Sources consulted (honest note)
WebSearch worked this cycle but returned only result titles and links. I did not open the pages, so the links below are unverified pointers and no finding depends on a claim from them.
- Nielsen Norman Group, portfolio and hiring-manager material (search: https://www.nngroup.com/articles/author/rachel-krause/?page=5)
- web.dev, Optimize Cumulative Layout Shift: https://web.dev/optimize-cls/
- W3C, Understanding SC 1.4.11 Non-text Contrast: https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast
Topic this cycle: hiring-manager scanning, image dimensions and CLS, non-text contrast of borders and stamps.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone, double ink rules, hard-offset button, mono ledger labels, boxed stamps, inverted footer, flat dark theme. No gradient, blur or glow in any screenshot.
2. Must not look AI-generated: met. Ruled index, struck "three weeks" in a marker band, stamps, Fig. captions, plain specific copy. No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine identically ruled rows; DM Serif plus a mono label is a common editorial pairing. No tells moved.
- Looks good: 7/10. Phone home has clear order and rhythm. Weak spots: no photograph of any real work; the home page shows one image in nine rows; the Aerobraking page (about 6200 px tall at phone width) is long running prose with little visual break because its figures are Wix hotlinks that fail offline.
- SEO: 7/10. Per repo: unique titles and descriptions, one h1, canonical (https://kmkar31.github.io/website/), absolute local og:image, JSON-LD, sitemap, robots.txt, 404. Not verifiable offline: live og:image fetch, field LCP and CLS.
- UX: 7/10. Name, role, strongest project (Start here on 06) and contact path are on the first phone screen. Contact is LinkedIn only.
- Fun and personality: 7/10. Strike-through, stamps, "Sheet N of 9 . NTS" are authored. Do not add stamps without a true number.

## Findings (ranked)
1. Major, content (owner fact): no current-status sentence. About says CMU "2023 - 2025" and today is November 2026; a recruiter cannot tell whether he has graduated, works somewhere or is looking. STATUS slot in build.py is empty. Owner supplies one line.
2. Major, robustness (owner file): Resume is a Wix filesusr URL (3 references on index, 2 on about, 2 on 404, plus header and footer). One dead URL breaks every Resume link. Owner adds assets/resume.pdf.
3. Major, visual and robustness (owner files): no real photograph; project media are Wix hotlinks. Aerobraking prose says "as shown below" and "as shown in the figure above" several times; when images fail the page reads as broken. Needs owner-supplied files.
4. Major, content (owner facts): Snake robots (row 01, the first thing read) has no outcome, and Raftar has only "40+ students" and "captained". The first row of the index is the one with the least measured substance. Owner supplies confirmed specifics. Nothing the designer can invent.
5. Minor, UX: phone and desktop contact is LinkedIn only, no email by design (LOG). Acceptable as a decision, but say so plainly if recruiters expect mail; owner call.
6. Minor, performance (owner dimensions): figures lack width and height or aspect-ratio, so layout shift on slow image load (web.dev optimize-cls). Needs dimensions.
7. Minor, performance: two Google fonts with no self-hosted WOFF2 or measured size-adjust fallback. Needs files.
8. Minor, accessibility (not verified, taste of measurement): stamp borders and hairline row rules in the dark theme are thin tan on near-black; SC 1.4.11 applies to the stamp as a status indicator only if the border carries meaning, and the text inside has its own contrast. Check check.py output for measured ratios; I did not measure them this cycle.
9. Nit, SEO (owner action): sitemap.xml and robots.txt sit at a project-site subpath, so crawlers will not find robots.txt at the host root; submit the sitemap in Search Console.
10. Nit, visual (taste): the home "Fig. 1" plate is the only image among nine rows, so the page looks image-starved next to the one that has it. Fixed only when owner media exist.

No new designer-fixable defect, and no regression from cycle 76.

## Good, must not regress
The plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted footer and flat dark theme; double rules; "Sheet N of 9 . NTS" captions; honest "schematic" captions; one-line "Fig. 1 - Orbits" caption; accurate colophon; 44px tap targets; one-line phone filter row and tighter gap under it; Previous/Next footers with a real detail; local og:image; JSON-LD; 404 page; reduced-motion block; Start here on Aerobraking.

## Verdict
The site commits to the retro matte direction, reads as one person's work, and both owner constraints are met. Nothing regressed. What remains is blocked on the owner: a status line, a local resume PDF, photographs and image dimensions, and substance for Snake and Raftar. Research this cycle was search-result titles only, so I make no external claims.
