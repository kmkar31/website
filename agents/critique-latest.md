# Critique, 2026-11-05 (cycle 83)

Rendering: `python3 tools/check.py . agents/shots` run in the background (it exceeds a 2 minute foreground limit) and finished: 78 OK, no failures; only "images not loaded, likely sandbox network" notes. I viewed index phone light, index desktop dark and hasselhoff-submarine phone light. No site files edited.

## Sources consulted (honest note)
No page text was fetched this cycle, so these are pointers, not verified citations. No finding depends on them.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- web.dev Optimize CLS: https://web.dev/optimize-cls/
- NN/g on portfolio and hiring-manager scanning: https://www.nngroup.com/ (topic only)

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone, double rules, hard-offset button, mono ledger, boxed stamps, flat inverted footer; no gradient, blur or glow in light or dark.
2. Not AI-looking: met. Strike-through marker band, stamps that carry real numbers, plain specific copy, graph-paper "Fig." plates with sheet numbers. No new owner notes.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine uniform ruled rows; DM Serif plus mono labels is a familiar editorial pairing. No tells moved.
- Looks good: 7/10. Clear phone order; desktop home is balanced with the ledger rail beside the lede. Weak: one plate in nine rows, no photograph, rows 01-05 and 07-09 text-only.
- SEO: 7/10 (per repo): unique titles, absolute og:image (https://kmkar31.github.io/website/assets/og.png), canonical, JSON-LD, sitemap, robots, noindex 404. Not verifiable offline: live og:image, field LCP/CLS.
- UX: 7/10. Name, role, strongest project (Start here, 06) and LinkedIn are in the first phone screens; project pages have Previous/Next. Missing: status line, email.
- Fun and personality: 7/10. Strike-through, stamps, 99-second stamp, Hasselhoff/SpongeBob note, "Sheet 5 of 9" are earned. Do not add stamps without a true number.

## Findings (ranked)
1. Major, content (owner fact): no current-status sentence. `STATUS = ""` at build/build.py:262, so the Status row never renders. The lede is present tense ("I research") and the header gives "MS Mechanical Engineering, Carnegie Mellon University" with no dates; the log has the Master's as 2023-2025 and it is November 2026. A recruiter cannot tell if he is a student, employed or looking. Owner supplies one line.
2. Major, robustness (owner file): the Resume (PDF) is a Wix filesusr.com hotlink, repeated in header, lede and footer on every page. One dead URL breaks all of them. Owner adds assets/resume.pdf.
3. Major, visual (owner files): no photograph; the About portrait and project media are static.wixstatic.com hotlinks (about 30 references across project pages). Third-party dependency the owner does not control.
4. Major, content (owner facts): Snake robots (row 01, the lead entry) and Raftar have no result or outcome beyond a lab name and "40+ students". Nothing the designer may invent.
5. Minor, UX: LinkedIn-only contact is a documented decision; the phone header has no resume or contact link (both in lede and footer). Owner call.
6. Minor, performance (owner dimensions): hotlinked figure images lack known width/height or aspect-ratio, a CLS risk once they load.
7. Minor, performance: Google Fonts with no self-hosted WOFF2 or measured fallback metrics.
8. Nit, SEO (owner action): robots.txt and sitemap sit under a project-site subpath, so crawlers will not read robots.txt there. Submit sitemap.xml in Search Console.
9. Nit, visual (taste): About desktop right third is empty below the rail; a portrait would fix it.
10. Nit, visual (taste): one plate among nine rows; only owner media fixes it.

No designer-fixable defect and no regression from cycle 82.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted footer and flat dark theme; double rules; honest "schematic" captions; Fig. 1 plate and Start here on row 06; 44px tap targets; Previous/Next footers; absolute og:image; JSON-LD; 404 with its joke; reduced-motion block; no-JS-safe figures.

## Verdict
The site commits to the retro matte direction, reads as one person's work, and both owner constraints are met. Every remaining gap is owner-blocked: a status line (the Master's dates are now past), a local resume PDF, photographs with dimensions, and real outcomes for the Snake and Raftar pages. External sources were not verified, so I make no external claims.
