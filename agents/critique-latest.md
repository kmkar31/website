# Critique, 2026-11-28 (after designer cycle 219)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL; only "images not loaded" sandbox notes). Viewed index phone-light and index desktop-light. Read the tail of LOG.md (about 280 KB, not read in full), the previous critique and user-critique.md. `git status` is clean and the last commit is log-only, so no site change and no regression. Wix images and Google Fonts are blocked in the sandbox (environment limit; the screenshots show fallback serif/mono, so type pairing was not judged).

## Sources consulted
WebFetch of https://web.dev/articles/optimize-cls was refused again (permission request unanswered, not retried). No external source was read this cycle, which is under the brief's three-source minimum; this is an environment limit. Pointers only, not quoted:
- web.dev, Optimize CLS (width/height on images): https://web.dev/articles/optimize-cls
- web.dev, Font best practices: https://web.dev/articles/font-best-practices
- NN/g, UX Portfolios: What Hiring Managers Look For: https://www.nngroup.com/videos/ux-portfolios-hiring/

## Scores
- AI-tell: 2/10, unchanged. Ruled list, "For the record" ledger, struck-through "three weeks to 15 minutes", stamps, "Fig. 1" plate; no gradients, glass, chips, stats strip or card trio. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged (viewed). Paper-and-ink system is coherent. Desktop Home right column is uneven: rows 01-03, 08, 09 have no mark, row 06 stacks a stamp and "Start here".
- SEO: 7/10, unchanged. Per-page title, description, canonical, OG, JSON-LD, sitemap, robots, 404 present. Weak: one shared OG card, hotlinked images, robots.txt under a project-site subpath (host limit).
- UX: 6/10, unchanged. Contact, resume, next/previous are findable; gaps are owner content.
- Fun and personality: 7/10, unchanged.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met.
2. Must not look AI-generated: met, AI-tell 2. File unchanged, no new notes.

## Regression check
No site file changed. No regressions.

## Ranked findings
1. Major (UX, credibility). Home subhead gives "MS Mechanical Engineering, Carnegie Mellon University" with no dates or status (viewed, phone and desktop). The ledger "Status" row never renders because `STATUS` is empty. About says 2023 to 2025 and today is 2026-11-28, so a recruiter cannot tell if he has graduated or is available. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads, "Start here" sits on row 06 (aerobraking), about two phone screens down (viewed). Owner picks the lead.
3. Major (content). The snake page leads and is the thinnest: no method, result or number, while the blurb says "I implemented". Owner must supply what he did and what happened.
4. Major (robustness, performance). Nearly all project images are hotlinked from Wix (about 30 references across 11 pages) with no width/height: CLS and link-rot risk. The src-less `<img alt="">` is the lightbox viewer, accepted. Owner must supply local copies.
5. Major (credibility). Aerobraking's "46 orbits to target" has no baseline and its Method is third person. Raftar's Ferrari comparison has no source. Owner facts.
6. Minor (consistency, performance). Footer says "no framework" and names DM Serif Display and Source Serif 4, which load from Google Fonts (render-blocking third party). Self-host WOFF2 with `font-display: swap` once files exist.
7. Minor (UX). Aerobraking is very long on phone with no "My part" box. Add after finding 5.
8. Minor (visual, taste). Desktop Home right column uneven (row 06). Previously declined; noted only.
9. Minor (SEO). Shared OG card; Search Console sitemap submission is an owner action.
10. Minor (content). Tricycle page voice is passive, no subheads. Owner call.
11. Nit (content). Quadrotor-sysid leads with theory rather than the fitted result. Owner fact.
12. Nit (UX). Footer contact line is LinkedIn only (GitHub and resume also linked). Owner constraint.
13. Nit (process). Findings 1 to 5 have repeated for 20+ cycles and recent cycles were log-only. The loop is blocked on owner input and web research is blocked, so this critique adds no new external evidence.

## Good, must not regress
- Ruled-list Home with "For the record" ledger; no card trio, no stats strip.
- Struck-through "three weeks to 15 minutes", the 99 s stamp, "Fig. 1" plate, "Sheet N of 9" captions.
- Flat paper tones, ink borders, hard offset shadows in both themes; no blur or gradient.
- Per-page titles, descriptions, canonical, OG, JSON-LD, sitemap, robots, 404.
- Next/More-on links; sticky header; reduced-motion block; 3px `:focus-visible` outline; theme-color metas.
- About page: dated ledger of education and internships with real numbers.

## Verdict
The design is finished as far as the repo's own material allows: retro, matte, not generated-looking and technically sound. What holds it back is content only the owner can supply: current status and dates, one lead project with a real method and result for the snake work, first-person attribution and baselines for aerobraking, and local copies of the resume, images and fonts. Until those arrive, more design cycles will repeat this list. Stop the loop or send the owner the facts and files.
