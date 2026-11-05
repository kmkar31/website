# Critique, 2026-11-05 (cycle 84)

Rendering: `python3 tools/check.py . agents/shots` completed, all OK (only "images not loaded, likely sandbox network" notes). I viewed index phone light, snake-robots phone dark, about tablet light. Repo checks by script: every page has one h1, a meta description, 4 og/twitter image tags, no img without alt; JSON-LD on all but the 404; sitemap, robots, absolute og:image present. No site files edited.

## Sources consulted (honest note)
Attempted WebFetch of WCAG 2.5.8, web.dev optimize-cls and NN/g portfolio reviews; all were blocked by a permission timeout. A WebSearch returned titles only. These are pointers, not verified citations; no finding depends on them.
- WCAG 2.2 SC 2.5.8: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (not read)
- web.dev CLS: https://web.dev/articles/optimize-cls (not read); search hit https://web.dev/learn/images/performance-issues (title only)
- NN/g: https://www.nngroup.com/articles/portfolio-reviews/ (not read)

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone, double rules, hard-offset button, mono ledger, boxed stamps, flat inverted footer, flat dark theme. No gradient, blur or glow.
2. Not AI-looking: met. Strike-through marker band, stamps carrying real numbers, plain specific copy, graph-paper Fig. plates with sheet numbers. No new owner notes.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine uniform ruled rows; DM Serif plus mono labels is a familiar editorial pairing.
- Looks good: 7/10. Phone home is clear and well ordered. Weak: one plate among nine rows, no photograph; the snake page (dark phone) is a lot of empty dark space under one schematic and one paragraph.
- SEO: 7/10 (per repo, as above). Not verifiable offline: live og:image, field LCP/CLS, Search Console.
- UX: 7/10. Name, role, strongest project ("Start here", 06) and LinkedIn within the first phone screens; Previous/Next on project pages. Missing: status line, email.
- Fun and personality: 7/10. Strike-through, 99-second stamp, Hasselhoff/SpongeBob note, "Sheet 1 of 9 · NTS" are earned. Do not add stamps without a true number.

## Findings (ranked)
1. Major, content (owner fact): no current-status sentence (`STATUS = ""` in build/build.py). About lists the Master's as 2023 – 2025 and it is November 2026; the lede is present tense ("I research"). A recruiter cannot tell if he is a student, employed or looking. Owner supplies one line.
2. Major, robustness (owner file): Resume (PDF) is a Wix filesusr.com hotlink repeated in header, lede and footer on every page; one dead URL breaks all. Owner adds assets/resume.pdf.
3. Major, visual (owner files): no photograph; About portrait and project media are static.wixstatic.com hotlinks (about 30 references; most pages have 1-7). Third-party dependency the owner does not control.
4. Major, content (owner facts): the lead entry, Snake robots (row 01, phone dark), has only a lab, advisor, "The question" and a generic "Why snake robots" paragraph; no result, no gait name, no figure from his work. Raftar similarly thin. The strongest-looking projects (06, 05) have numbers; the first row does not. Owner supplies one outcome each.
5. Minor, UX: the phone header has no resume or contact link (both are in lede and footer). LinkedIn-only is a documented owner decision.
6. Minor, performance (owner dimensions): hotlinked figure images lack known width/height or aspect-ratio, a CLS risk once they load.
7. Minor, performance: Google Fonts, no self-hosted WOFF2 or tuned fallback metrics.
8. Nit, SEO (owner action): robots.txt and sitemap sit under a project-site subpath, so crawlers will not read robots.txt there; submit sitemap.xml in Search Console. Sitemap lastmod (2026-11-02) is behind the cycle dates, harmless.
9. Nit, visual (taste): About desktop/tablet right side empty below the rail; a portrait would fix it.
10. Nit, visual (taste): one plate among nine rows; only owner media fixes it.

No designer-fixable defect and no regression from cycle 83.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted footer and flat dark theme; double rules; honest "schematic" captions; Fig. 1 plate and Start here on row 06; 44px tap targets; Previous/Next footers; absolute og:image; JSON-LD; 404 with its joke; reduced-motion block; no-JS-safe figures.

## Verdict
The site commits to the retro matte direction, reads as one person's work, and both owner constraints are met. The remaining gaps are owner-blocked: a status line (the Master's dates are now past), a local resume PDF, photographs with dimensions, and real outcomes for the Snake and Raftar pages. External sources could not be fetched this cycle, so I make no external claims.
