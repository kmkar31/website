# Critique, 2026-11-27 (after designer cycle 211)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL, only "images not loaded" sandbox notes; the run takes about 2.5 minutes). Viewed index phone-light, index desktop-light and index tablet-dark. Read LOG.md (through cycle 211), user-critique.md (unchanged, two notes from 2026-10-22) and the previous critique. `git status` is clean and cycles 206 to 211 changed no site files, so no regression is possible. Wix images and Google Fonts are blocked in the sandbox, so photos are absent and serifs render as fallbacks (environment limit).

## Sources consulted
Below the three-source minimum again, and I am saying so. WebFetch of all three attempted this cycle was refused (permission not answered): web.dev Optimize CLS, W3C WCAG 2.2 Target Size (Minimum), NN/g portfolio article. I quote nothing from them. Unread pointers:
- https://web.dev/articles/optimize-cls (finding 5)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (tap targets; the sandbox check already enforces 44px)
- https://www.nngroup.com/articles/ux-design-portfolios/ (findings 1 to 3)
Topic this cycle: CLS and image dimensions, tap targets, portfolio credibility.

## Scores
- AI-tell: 2/10, unchanged. Plain ruled list, "For the record" ledger, struck-through "three weeks to 15 minutes", stamps, "Fig. 1" plate. No gradients, glass, chips, stats strip or card trio. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Paper-and-ink system is coherent in light and dark (viewed). Desktop right column is ragged: rows 01 to 03, 08 and 09 carry no mark, and row 06 stacks stamp, "Start here" and tags beside the only thumbnail.
- SEO: 7/10, unchanged. Per-page title, description, canonical, absolute og:image, twitter card, JSON-LD, sitemap, robots, 404. Weak: one shared OG card; hotlinked images; robots.txt under a project-site subpath is ignored by crawlers (host limit).
- UX: 6/10, unchanged. Contact, resume and next/previous links are easy to find; the gaps need owner content (findings 1 to 5).
- Fun and personality: 7/10, unchanged. Strike-through, "Time allowed: 99 s" stamp and "Start here" tab.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat paper, ink borders, hard offset shadows, no blur, both themes, viewed).
2. Must not look AI-generated: met, AI-tell 2. No new notes in the file.

## Regression check
No site file changed since the last critique. Screenshots match. No regressions.

## Ranked findings
1. Major (UX, credibility). Home subhead is "MS Mechanical Engineering, Carnegie Mellon University" with no dates or status. About says 2023 to 2025 and today is 2026-11-27. A recruiter cannot tell whether he has graduated, what he does now or whether he is available. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads, "Start here" sits on row 06 (aerobraking), about two phone screens down (viewed). Owner picks the lead, moves the label or reorders.
3. Major (content). The snake page, the lead project, is the thinnest: an illustrative schematic, a short "Why snake robots" and a lab link. No method, result or number for what he implemented, yet the lead blurb says "I implemented". Owner must supply.
4. Major (credibility). Aerobraking's "46 orbits to target" has no baseline and its Method is third person, which hides his own contribution. Raftar's Ferrari comparison has no source. Owner facts.
5. Major (robustness, performance). The resume PDF (a Wix `ugd/` file) and nearly all project images are hotlinked from Wix. The `<img>` tags I sampled (snake-robots.html) have no width or height, so there is a CLS risk (general knowledge; the web.dev source was blocked). The resume link appears in four places on Home alone, so one dead link breaks several entries. Needs assets/resume.pdf and local images. Link liveness is not verifiable offline.
6. Minor (UX). Aerobraking is very long on phone with no pull-out of his own part. Add a two-line "My part" box once finding 4 is answered.
7. Minor (visual, taste). Desktop Home right column is uneven (row 06). Previously declined; noted only.
8. Minor (consistency). Footer says "no framework" and names DM Serif Display and Source Serif 4, but fonts load from Google Fonts. Self-host WOFF2 when files exist.
9. Minor (SEO). Shared OG card; sitemap submission in Search Console is an owner action.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only (GitHub and resume also linked). Owner constraint.
12. Nit (process). Findings 1 to 5 have repeated for about 18 cycles and no site change can resolve them; the last six cycles were log-only. The owner should supply facts and files, or the loop should pause.

## Good, must not regress
- Ruled-list Home with the "For the record" ledger; no card trio, no stats strip.
- Struck-through "three weeks to 15 minutes", the 99 s stamp, "Fig. 1" plates and "Sheet 1 of 9" captions.
- Flat paper tones, ink borders, hard offset shadows in both themes; no blur or gradient.
- Per-page titles, descriptions, canonical, OG, JSON-LD, sitemap, robots, 404.
- Next/More-on links on project pages; sticky header with scroll-padding; reduced-motion block.

## Verdict
The design is finished as far as the repo's own material allows: it is retro and matte, it does not look generated, and it is technically sound. What holds it back is content only the owner can supply: a current status and dates, one clear lead project with a real method and result for the snake work, first-person attribution and baselines on aerobraking, and local copies of the resume and images. Until those arrive, further design cycles will only repeat this list. Pause the loop or send the owner the five facts.
