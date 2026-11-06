# Critique, 2026-11-06 (cycle 90)

Rendering: `python3 tools/check.py . agents/shots` ran (about 4 min, run it in the background); all pages OK at phone, tablet and desktop, light and dark; only "images not loaded" sandbox notes. I viewed index phone light, index desktop dark, about tablet light and raftar phone light. Repo greps: `STATUS = ""` (build/build.py:262); Resume is a filesusr.com URL (index.html); wixstatic hotlinks on 11 of 13 pages (index and 404 have none). No site files edited.

## Sources consulted (honest note)
I did not run WebSearch or WebFetch this cycle (no network research was available in this run), so no external source was read. This misses the "three sources" rule in agents/critic.md. Nothing below depends on a cited source; every finding rests on renders and repo greps. Pointers for the designer, unverified:
- WCAG 2.2 SC 2.5.8 Target Size (Minimum), w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- web.dev, Optimize Cumulative Layout Shift, web.dev/articles/optimize-cls
- NN/g, portfolio and hiring-manager scanning (Rachel Krause), nngroup.com

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone with faint grain, double rules, hard-offset red button, mono labels, flat dark footer; no gradient, blur or glow in any render, light or dark.
2. Not AI-looking: met. Struck-through "three weeks" on an amber swatch, stamps that carry real numbers, "Fig. 1 / Sheet 4 of 9 / NTS" captions and plain first-person copy read as authored.

## Scores
- AI-tell score: 2/10, unchanged. Residual: nine same-shape ruled rows; serif headline plus mono labels is a familiar "editorial" pairing. No tells moved.
- Looks good: 7/10. Clear hierarchy and steady rhythm. Weak: no photograph anywhere in the renders; project pages on phone are a title, a large tl;dr, one schematic and a short paragraph (Raftar page ends after about two paragraphs), so they feel thin.
- SEO: 7/10 (repo only). Titles, canonical, OG, JSON-LD, sitemap, local og:image present. Live indexing and field CWV not verifiable offline.
- UX: 7/10. Name, field, projects, Resume and LinkedIn are on the first phone screen. No status line; Resume link is the weak point (finding 2).
- Fun and personality: 7/10. Strike-through, stamps and sheet numbers are earned; more would need real facts.

## Findings (ranked)
1. Major, content (owner fact): `STATUS` is empty. About and the Snake page say the Master's ran 2023 - 2025; today is November 2026; the home lede is present tense ("I work on... I research..."). A recruiter cannot tell if he is a student, employed or looking. The owner supplies one line; I will not invent it.
2. Major, robustness (owner file): "Resume (PDF)" is a filesusr.com hotlink in the header, lede and footer of every page. One dead URL breaks the likeliest recruiter click. Owner adds assets/resume.pdf; build points at it.
3. Major, visual and robustness (owner files): figures and About images are wixstatic hotlinks on 11 pages. If Wix drops them, pages become text plus schematics, and the site has no photograph of the person or the hardware.
4. Major, content (owner facts): the lead row (Snake robots, 01) has a lab and a question but no result of his own; Raftar says what he did but not how the suspension or brakes performed. The first rows a visitor scans have no number except the Raftar stamp.
5. Major, credibility (owner confirmation): Raftar page question claims a car "one-fifth the weight of a Ferrari" matching its 0-60 time. It is original-site wording but is a checkable claim with no figure on the page. Owner confirms or cuts.
6. Minor, UX (taste, reopened): "Start here" is on row 06, roughly 1,100 px below the fold on a 360 px phone, beneath a row 01 with no result. Not fixable without renumbering sheets; the real fix is finding 4.
7. Minor, performance (owner dimensions): hotlinked figures have no known width/height, a CLS risk. A guessed ratio would be worse.
8. Minor, performance: Google Fonts without self-hosted WOFF2 or tuned fallback metrics; a font swap is possible on slow connections.
9. Minor, UX: phone header has Home / About / Projects only; Resume and contact need a scroll to the footer on subpages. LinkedIn-only contact is a documented decision, so only placement is raised.
10. Nit, SEO (owner action): robots.txt and sitemap under /website/ are not read from a project subpath; submit sitemap.xml in Search Console.

## Good, must not regress
- The retro matte system: paper tones, double rules, hard offset button, flat dark theme.
- Specific numbers in copy: 3 weeks to 15 minutes, 46 orbits, 99 s, 500 m, 40+ students, podium at Formula Bharat 2023.
- "Start here" on row 06 with its plate; Next/Previous with a fact under each title.
- Honest captions on schematics; stamps only where the number is the point.
- Visible focus, reduced-motion handling, 44 px targets, one h1 per page, canonical/OG/JSON-LD.

## Verdict
The site commits coherently to a retro print direction and does not read as generated. It is held back by content that only the owner can supply: a status line, a local resume, photographs, and a result on the lead project. Designer-side work is exhausted; the next real gains come from owner files and facts, plus confirming the Ferrari claim.
