# Critique, 2026-11-05 (cycle 81)

Rendering: `python3 tools/check.py . agents/shots` ran; every line OK, only "images not loaded, likely sandbox network" notes. I viewed index phone light and index desktop light. No site files edited; this is the only file written.

## Sources consulted (honest note)
WebFetch of https://web.dev/articles/optimize-cls (topic: image dimensions and CLS) was refused again (PROVENANCE_REQUIRED) and not retried. The same tool refused WCAG 2.2 target size and NN/g scanning pages in cycle 80. I have no verified external source this cycle, so every finding rests on the repo and screenshots, and the rules cited below are pointers, not verified citations.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone, double rules, hard-offset button, mono ledger, boxed stamps, flat inverted footer. No gradient, blur or glow in the screenshots.
2. Not AI-looking: met. Marker-band strike-through, stamps that carry true numbers, plain specific copy, graph-paper plate. The file has no new owner notes.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine uniform ruled rows; DM Serif with a mono label is a familiar editorial pairing. No tells moved.
- Looks good: 7/10. Phone home has clear order and rhythm. Desktop home is well composed, with the record rail beside the lede. Weak: one plate in nine rows, no real photograph, desktop rows 01 to 05 and 07 to 09 are text-only.
- SEO: 7/10. Per repo: og:image is absolute (https://kmkar31.github.io/website/assets/og.png), plus titles, descriptions, canonical, JSON-LD, sitemap, robots and a noindex 404. Not verifiable offline: live og:image and field LCP/CLS.
- UX: 7/10. Name, role, strongest project (Start here, 06) and LinkedIn all sit in the first phone screens. Missing: status line, email.
- Fun and personality: 7/10. Strike-through, stamps, Fig. 1 plate and the 99-second submarine stamp are earned. Do not add stamps without a true number.

## Findings (ranked)
1. Major, content (owner fact): no current-status sentence. `STATUS = ""` at build/build.py:262, so the Status row never renders. The lede says "At CMU's Biorobotics Lab ... I research" in present tense, and About gives CMU 2023 to 2025. It is November 2026, so a recruiter cannot tell whether he has graduated, works, or is looking. Owner supplies one line.
2. Major, robustness (owner file): the Resume (PDF) link is a Wix hotlink. index.html and about.html each contain 3 wixstatic/filesusr references. Resume links sit in the header, lede, footer and 404, so one dead URL breaks every one. Owner adds assets/resume.pdf.
3. Major, visual (owner files): no real photograph, and project media are hotlinked from Wix. They fail in the sandbox (3 to 5 images per page unloaded). The site depends on a third party the owner does not control.
4. Major, content (owner facts): Snake robots (row 01, the lead entry) and Raftar have no result or outcome beyond a lab name and "40+ students". Nothing the designer may invent.
5. Minor, UX: LinkedIn-only contact is a documented decision. The phone header has no resume or contact link; both are in the lede and footer. Owner call.
6. Minor, performance (owner dimensions): figure images lack width/height or aspect-ratio, which risks layout shift once hotlinks load.
7. Minor, performance: Google Fonts without self-hosted WOFF2 or measured fallback metrics.
8. Nit, SEO (owner action): robots.txt and sitemap sit at a project-site subpath, so crawlers will not read robots.txt there. Submit sitemap.xml in Search Console.
9. Nit, visual (taste): the About desktop right third is empty below the rail. A portrait would fix it.
10. Nit, visual (taste): one plate among nine rows. Only owner media fixes it.

No designer-fixable defect and no regression from cycle 80.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted footer and flat dark theme; double rules; honest "schematic" captions; "Fig. 1 . Orbits" plate and Start here on row 06; 44px tap targets; one-line phone filter row; Previous/Next footers; absolute og:image; JSON-LD; 404 with its joke; reduced-motion block; no-JS-safe figures.

## Verdict
The site commits to the retro matte direction, reads as one person's work, and both owner constraints are met. Nothing regressed since cycle 80. Every remaining gap is owner-blocked: a status line (the Master's dates are now past), a local resume PDF, photographs with dimensions, and real substance for the Snake and Raftar pages. Sources were blocked again, so I make no external claims.
