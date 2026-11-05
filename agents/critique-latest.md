# Critique, 2026-11-05 (cycle 80)

Rendering: `python3 tools/check.py . agents/shots` ran (it needed about 2 to 4 minutes, longer than a 2-minute shell limit). Every line OK, only "images not loaded, likely sandbox network" notes. I viewed index phone light, index desktop dark and projects tablet light. No site files edited; this is the only file written.

## Sources consulted (honest note)
All three fetches were refused by the permission layer (PROVENANCE_REQUIRED) and not retried:
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (topic: tap targets)
- https://web.dev/articles/optimize-cls (topic: image dimensions and CLS)
- https://www.nngroup.com/articles/how-people-read-online/ (topic: scanning)
They are pointers only. No external claim below rests on them; findings come from the repo and screenshots.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone, double rules, hard-offset button, mono ledger, boxed stamps, flat inverted footer, matte dark theme. No gradient, blur or glow in any screenshot viewed.
2. Not AI-looking: met. Struck "three weeks" in a marker band, stamps carrying true numbers, plain specific copy, graph-paper plate. No new owner notes in the file.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine uniformly ruled rows; DM Serif plus mono label is a familiar editorial pairing. No tells moved.
- Looks good: 7/10. Phone home has clear order and rhythm and the stamps break up the list. Weak: one plate in nine rows, no photograph of real work, large empty right third on About desktop.
- SEO: 7/10. Per repo: unique titles (index "Control of Robots and Spacecraft", about names CMU, IIT Madras, Seagate), descriptions, canonical, local og:image, JSON-LD, sitemap, robots, noindex 404. Not verifiable offline: live og:image, field LCP/CLS.
- UX: 7/10. Name, role, strongest project (Start here, 06) and LinkedIn are in the first phone screens. No status line, LinkedIn-only contact.
- Fun and personality: 7/10. Strike-through, stamps, Fig. 1 plate and the 404 joke are earned. Do not add stamps without a true number.

## Findings (ranked)
1. Major, content (owner fact): no current-status sentence. STATUS in build/build.py line 262 is still "". About says CMU 2023 to 2025 and today is November 2026, so a recruiter cannot tell whether he has graduated, works, or is looking. Owner supplies one line.
2. Major, robustness (owner file): Resume (PDF) is a Wix filesusr hotlink used in header, home, footer and 404 (3 Wix references each on index and about). One dead URL breaks every resume link. Owner adds assets/resume.pdf.
3. Major, visual (owner files): no real photograph; project media are Wix hotlinks that fail in the sandbox (10 on Aerobraking, 9 on Sysid and Tricycle, 9 on the projects list). Dependency risk is high.
4. Major, content (owner facts): Snake robots (row 01) and Raftar have no result or outcome beyond a lab and "40+ students"; nothing the designer may invent.
5. Minor, UX: LinkedIn-only contact is a documented decision; owner call. The phone header has no resume or contact link; both sit in the lede and footer.
6. Minor, performance (owner dimensions): figure images lack width/height or aspect-ratio, a layout-shift risk once hotlinks load.
7. Minor, performance: Google Fonts, no self-hosted WOFF2 or measured fallback metrics.
8. Nit, SEO (owner action): robots.txt and sitemap sit at a project-site subpath, so crawlers will not find robots.txt; submit sitemap.xml in Search Console.
9. Nit, visual (taste): About desktop right third is empty below the rail; a portrait would fix it.
10. Nit, visual (taste): a single plate (row 06) among nine rows; fixed only by owner media. Note the desktop dark index looks tidy but text-only for rows 01 to 05 and 07 to 09.

No designer-fixable defect and no regression from cycle 79.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted footer and flat dark theme; double rules; "Sheet N of 9" captions and honest "schematic" captions; "Fig. 1 . Orbits" plate and Start here on row 06; 44px tap targets; one-line phone filter row; Previous/Next footers; local og:image; JSON-LD; 404 with its 99-second joke; reduced-motion block; no-JS-safe figures.

## Verdict
The site commits to the retro matte direction, reads as one person's work, and both owner constraints are met. Nothing regressed since cycle 79. Every remaining gap is owner-blocked: a status line (the Master's dates are now past), a local resume PDF, photographs with dimensions, and real substance for the Snake and Raftar pages. My external sources were all blocked again, so I make no external claims.
