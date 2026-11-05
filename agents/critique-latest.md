# Critique, 2026-11-05 (cycle 82)

Rendering: `python3 tools/check.py . agents/shots` hit my 2 minute tool timeout and was killed before finishing, so I have no fresh pass/fail summary this cycle (cycle 81's was all OK). Screenshots were partly regenerated (404 and index sets are current). I viewed index phone light and index desktop light. No site files edited; this is the only file written.

## Sources consulted (honest note)
WebSearch returned only link lists, no page text, and I did not fetch the pages, so these are pointers, not verified citations:
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- web.dev Optimize CLS (image width/height): https://web.dev/optimize-cls/
- Nothing else checked. No finding below depends on them.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone, double rules, hard-offset button, mono ledger, boxed stamps, flat inverted footer. No gradient, blur or glow visible.
2. Not AI-looking: met. Marker-band strike-through, stamps that carry real numbers, plain specific copy, graph-paper plate. No new owner notes in the file.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine uniform ruled rows; DM Serif plus mono labels is a familiar editorial pairing. No tells moved.
- Looks good: 7/10. Phone home has clear order. Desktop home is well composed with the record rail beside the lede. Weak: one plate in nine rows, no real photograph, rows 01 to 05 and 07 to 09 are text-only.
- SEO: 7/10 (per repo, unchanged): absolute og:image, titles, descriptions, canonical, JSON-LD, sitemap, robots, noindex 404. Not verifiable offline: live og:image, field LCP/CLS.
- UX: 7/10. Name, role, strongest project (Start here, 06) and LinkedIn are in the first phone screens. Missing: status line, email.
- Fun and personality: 7/10. Strike-through, stamps, Fig. 1 plate, the 99-second submarine stamp are earned. Do not add stamps without a true number.

## Findings (ranked)
1. Major, content (owner fact): no current-status sentence. `STATUS = ""` at build/build.py:262, so the Status row never renders. The lede says "At CMU's Biorobotics Lab ... I research" in present tense, and the header says "MS Mechanical Engineering, Carnegie Mellon University" with no dates. It is November 2026 and the Master's was 2023 to 2025 per the log, so a recruiter cannot tell whether he is a student, employed or looking. Owner supplies one line.
2. Major, robustness (owner file): the Resume (PDF) link is a Wix filesusr hotlink (index.html has 3, about.html 2, plus the 404 and footers). One dead URL breaks every resume link. Owner adds assets/resume.pdf.
3. Major, visual (owner files): no real photograph; the About portrait (static.wixstatic.com) and project media are hotlinked. The site depends on a third party the owner does not control.
4. Major, content (owner facts): Snake robots (row 01, the lead entry) and Raftar have no result or outcome beyond a lab name and "40+ students". Nothing the designer may invent.
5. Minor, UX: LinkedIn-only contact is a documented decision; the phone header has no resume or contact link (both are in the lede and footer). Owner call.
6. Minor, performance (owner dimensions): figure images lack width/height or aspect-ratio, a CLS risk once hotlinks load.
7. Minor, performance: Google Fonts with no self-hosted WOFF2 or measured fallback metrics.
8. Nit, SEO (owner action): robots.txt and sitemap sit at a project-site subpath, so crawlers will not read robots.txt there. Submit sitemap.xml in Search Console.
9. Nit, visual (taste): About desktop right third is empty below the rail. A portrait would fix it.
10. Nit, visual (taste): one plate among nine rows. Only owner media fixes it.

No designer-fixable defect and no regression from cycle 81 that I could see.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted footer and flat dark theme; double rules; honest "schematic" captions; Fig. 1 plate and Start here on row 06; 44px tap targets; Previous/Next footers; absolute og:image; JSON-LD; 404 with its joke; reduced-motion block; no-JS-safe figures.

## Verdict
The site commits to the retro matte direction, reads as one person's work, and both owner constraints are met. Every remaining gap is owner-blocked: a status line (the Master's dates are now past), a local resume PDF, photographs with dimensions, and real substance for the Snake and Raftar pages. Caveats: check.py did not finish in my run and external sources were not verified, so I make no external claims.
