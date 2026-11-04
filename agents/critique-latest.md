# Critique, 2026-11-04 (cycle 79)

Rendering: `python3 tools/check.py . agents/shots` ran; every line OK, only "images not loaded, likely sandbox network" notes. I viewed index phone light, index desktop light, about desktop dark and snake-robots phone light. No site files edited; this is the only file written.

## Sources consulted (honest note)
All three fetches this cycle were refused by the permission layer and not retried:
- https://web.dev/articles/optimize-lcp (topic: LCP image priority, lazy-loading)
- https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html (topic: focus visibility)
- https://www.nngroup.com/articles/how-people-read-online/ (topic: scanning)
No external claim below rests on them; they are pointers only. Findings come from the repo and screenshots.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone, double rules, hard-offset button, mono ledger, boxed stamps, flat inverted footer, matte dark theme. No gradient, blur or glow seen in any screenshot.
2. Not AI-looking: met. Struck "three weeks" in a marker band, stamps that carry true numbers, plain specific copy, graph-paper plates with sheet numbers. No new owner notes.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine uniformly ruled rows; DM Serif plus mono label is a familiar editorial pairing. No tells moved.
- Looks good: 7/10. Phone home has clear order and rhythm; stamps break the list. Weak: one plate in nine rows, no photograph of real work, About desktop has a large empty right third below the "On this page" rail, Aerobraking is prose-heavy when its Wix figures fail.
- SEO: 7/10. Per repo: unique titles and descriptions, one h1, canonical, local 1200x630 og:image with alt, JSON-LD, sitemap, robots, noindex 404. Not verifiable offline: live og:image, field LCP/CLS.
- UX: 7/10. Name, role, strongest project (Start here, 06) and LinkedIn are on the first phone screen. No current status, LinkedIn-only contact.
- Fun and personality: 7/10. Strike-through, stamps, Fig. 1 plates and the pressable 99 s stamp are authored and earned. Do not add stamps without a true number.

## Findings (ranked)
1. Major, content (owner fact): no current-status sentence. About says CMU 2023 - 2025 and today is Nov 2026 (STATUS in build/build.py line 262 is still ""). A recruiter cannot tell whether he has graduated, works, or is looking; this is the first question a 30-second reader has. Owner supplies one line.
2. Major, robustness (owner file): Resume (PDF) is a Wix filesusr hotlink used in header, home, footer and 404. One dead URL breaks every resume link. Owner adds assets/resume.pdf.
3. Major, visual (owner files): no real photograph anywhere; all project media are Wix hotlinks that fail in the sandbox (e.g. 10 on Aerobraking, 9 on Sysid). Dependency risk is high and a failed host leaves pages as text plus one schematic.
4. Major, content (owner facts): row 01 Snake robots page (viewed on phone) is a tl;dr, lab and advisor, a schematic and one "Why snake robots" paragraph, then Next. It has no result, method or outcome. Raftar says only "40+ students" and "captained". Nothing the designer may invent.
5. Minor, UX: LinkedIn-only contact is a documented decision; owner call if recruiters expect email. The phone header has no contact or resume link (full at 44px); contact sits in the lede and footer.
6. Minor, performance (owner dimensions): figure images have no width/height or aspect-ratio (`<img ... alt decoding>` in raftar page), a layout-shift risk once hotlinks load. Needs real dimensions.
7. Minor, performance: Google Fonts, no self-hosted WOFF2 or measured fallback metrics. Needs files.
8. Nit, SEO (owner action): robots.txt and sitemap sit at a project-site subpath, so crawlers will not find robots.txt; submit sitemap.xml in Search Console.
9. Nit, visual (taste): About desktop right two-thirds under the intro is empty (Skills uses three columns, then a lot of paper). Accepted by designer; a portrait would fix it.
10. Nit, visual (taste): a single plate (row 06) among nine rows; resolved only by owner media.

No designer-fixable defect and no regression from cycle 78.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted footer and flat dark theme; double rules; "Sheet N of 9" captions and honest "schematic" captions; one-line "Fig. 1 . Orbits" plate on row 06; Start here on Aerobraking; 44px tap targets; one-line phone filter row; Previous/Next footers without wraparound; local og:image; JSON-LD; 404 with its 99-second joke; reduced-motion block; no-JS-safe figures and details.

## Verdict
The site commits to the retro matte direction, reads as one person's work, and both owner constraints are met. Nothing regressed since cycle 78. Every remaining gap is owner-blocked: a status line (the Master's dates are now in the past), a local resume PDF, photographs with dimensions, and real substance for the Snake and Raftar pages. My sources this cycle were all blocked, so I make no external claims.
