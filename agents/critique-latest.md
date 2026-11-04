# Critique, 2026-11-04 (cycle 78)

Rendering: `python3 tools/check.py . agents/shots` ran: every line OK, only "images not loaded, likely sandbox network" notes. I viewed index-phone-light. No site files edited; this is the only file written.

## Sources consulted (honest note)
Two fetches were blocked by the permission layer (not retried): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html and https://web.dev/articles/optimize-cls. No external claim below rests on them. Topic this cycle was target size (WCAG 2.2 SC 2.5.8) and CLS; the repo's 44px targets are above the 24px minimum, from my knowledge of the SC, not from a fetch this cycle. Unverified pointers only; carried over from last cycle: https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast and https://www.nngroup.com/ (portfolio scanning).

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone, double rules, hard-offset button, mono ledger, boxed stamps, inverted flat footer. No gradient, blur or glow.
2. Not AI-looking: met. Struck "three weeks" in a marker band, stamps with real numbers, plain specific copy. No new owner notes.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine uniformly ruled rows; DM Serif plus mono label is a common editorial pairing. No tells moved.
- Looks good: 7/10. Phone home has clear order and rhythm; the rows 04-07 stamps give variety. Weak: only one plate (row 06) in nine rows; no photograph of real work; Aerobraking page is long prose when its Wix figures fail.
- SEO: 7/10. Per repo: unique titles and descriptions, one h1, canonical, local og:image, JSON-LD, sitemap, robots, 404. Not verifiable offline: live og:image, field LCP/CLS.
- UX: 7/10. Name, role, strongest project (Start here, 06) and contact are on the first phone screen. Contact is LinkedIn only.
- Fun and personality: 7/10. Strike-through and stamps are authored. Do not add stamps without a true number.

## Findings (ranked)
1. Major, content (owner fact): no current-status sentence. About says CMU 2023-2025; today is Nov 2026. Recruiter cannot tell if he has graduated, works, or is looking. Owner supplies one line for the STATUS slot.
2. Major, robustness (owner file): Resume is a Wix filesusr URL used in header/home/about/footer/404. One dead URL breaks every link. Owner adds assets/resume.pdf.
3. Major, visual (owner files): no real photograph; project media are Wix hotlinks. Aerobraking says "as shown below" repeatedly; with failed images it reads broken.
4. Major, content (owner facts): row 01 (Snake robots, first thing read) and row 04 (Raftar) have the least measured substance; Raftar has only "40+ students" and "captained". Nothing the designer may invent.
5. Minor, UX: LinkedIn-only contact is a documented decision; owner call if recruiters expect email.
6. Minor, performance (owner dimensions): figures lack width/height or aspect-ratio, risking layout shift on slow load. Needs real dimensions.
7. Minor, performance: Google Fonts, no self-hosted WOFF2 or measured fallback metrics. Needs files.
8. Nit, SEO (owner action): robots.txt/sitemap at a project-site subpath are not found at host root; submit the sitemap in Search Console.
9. Nit, visual (taste): single plate among nine rows; resolved only by owner media.

No designer-fixable defect and no regression from cycle 77.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted footer and flat dark theme; double rules; "Sheet N of 9" captions; honest "schematic" captions; one-line "Fig. 1 - Orbits"; 44px tap targets; one-line phone filter row; Previous/Next footers; local og:image; JSON-LD; 404; reduced-motion block; Start here on Aerobraking.

## Verdict
The site commits to the retro matte direction, reads as one person's work, and both owner constraints are met. Nothing regressed. Remaining gaps are all owner-blocked: a status line, a local resume PDF, photographs and image dimensions, and real substance for Snake and Raftar. My research this cycle was blocked, so I make no external claims.
