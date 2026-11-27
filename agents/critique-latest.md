# Critique, 2026-11-27 (after designer cycle 212)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL, only "images not loaded" sandbox notes). Viewed index phone-light, index desktop-dark, snake-robots tablet-light. Read LOG.md (through cycle 212), user-critique.md (unchanged: two notes from 2026-10-22) and the previous critique. `git status` is clean and cycles 206 to 212 changed no site files, so no regression is possible. Wix images and Google Fonts are blocked in the sandbox (environment limit).

## Sources consulted
Below the three-source minimum, and I am saying so. WebFetch of web.dev "Optimize CLS" was refused again this cycle (permission request unanswered); I did not retry and quote nothing from it. Unread pointers for the designer or owner:
- https://web.dev/articles/optimize-cls (finding 5: width/height on images)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- https://www.nngroup.com/articles/ux-design-portfolios/ (findings 1 to 3)
Evidence this cycle is therefore from the repo and screenshots only.

## Scores
- AI-tell: 2/10, unchanged. Ruled list, "For the record" ledger, struck-through "three weeks to 15 minutes", stamps, "Fig. 1" plate. No gradients, glass, chips, stats strip or card trio. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Coherent paper-and-ink system in both themes (viewed). Desktop right column is ragged: rows 01 to 03, 08, 09 carry no mark; row 06 stacks stamp, "Start here" and tags beside the only thumbnail.
- SEO: 7/10, unchanged. Per-page title, description, canonical, absolute og:image, twitter card, JSON-LD, sitemap, robots, 404. Weak: one shared OG card; hotlinked images; robots.txt under a project-site subpath is ignored by crawlers (host limit).
- UX: 6/10, unchanged. Contact, resume, next/previous links are easy to find; remaining gaps need owner content.
- Fun and personality: 7/10, unchanged. Strike-through, "Time allowed: 99 s" stamp, "Start here" tab.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat paper, ink borders, hard offset shadows, no blur, both themes, viewed).
2. Must not look AI-generated: met, AI-tell 2. No new notes in the file.

## Regression check
No site file changed. Screenshots match the last cycle. No regressions.

## Ranked findings
1. Major (UX, credibility). Home subhead is "MS Mechanical Engineering, Carnegie Mellon University" with no dates or status. About says 2023 to 2025; today is 2026-11-27. A recruiter cannot tell if he has graduated, what he does now or if he is available. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads, "Start here" sits on row 06 (aerobraking), about two phone screens down (viewed). Owner picks the lead, moves the label or reorders.
3. Major (content). The snake page, the lead project, is the thinnest (viewed, tablet): a schematic labelled "illustrative", a two-sentence "Why snake robots" and a lab link. No method, result or number, yet the blurb says "I implemented". Owner must supply.
4. Major (credibility). Aerobraking's "46 orbits to target" has no baseline and its Method is third person, hiding his own contribution. Raftar's Ferrari comparison has no source. Owner facts.
5. Major (robustness, performance). The resume PDF and nearly all project images are hotlinked from Wix. Sampled `<img>` tags in snake-robots.html and aerobraking-drl.html have no width or height (verified by grep), a standard CLS risk. The resume link appears in several places on Home, so one dead link breaks several entries. Needs assets/resume.pdf and local images. Link liveness is not verifiable offline. A stray `<img alt="">` also appears in snake-robots.html; confirm it is intentional decoration.
6. Minor (UX). Aerobraking is very long on phone with no pull-out of his own part. Add a short "My part" box once finding 4 is answered.
7. Minor (visual, taste). Desktop Home right column is uneven (row 06). Previously declined; noted only.
8. Minor (consistency). Footer says "no framework" and names DM Serif Display and Source Serif 4, but fonts load from Google Fonts. Self-host WOFF2 when files exist.
9. Minor (SEO). Shared OG card; sitemap submission in Search Console is an owner action.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only (GitHub and resume also linked). Owner constraint.
12. Nit (process). Findings 1 to 5 have repeated for about 19 cycles and no site change can resolve them; the last seven cycles were log-only. Owner should supply facts and files, or the loop should pause.

## Good, must not regress
- Ruled-list Home with the "For the record" ledger; no card trio, no stats strip.
- Struck-through "three weeks to 15 minutes", the 99 s stamp, "Fig. 1" plates, "Sheet 1 of 9" captions.
- Flat paper tones, ink borders, hard offset shadows in both themes; no blur or gradient.
- Per-page titles, descriptions, canonical, OG, JSON-LD, sitemap, robots, 404.
- Next/More-on links on project pages; sticky header with scroll-padding; reduced-motion block.

## Verdict
The design is finished as far as the repo's own material allows: retro, matte, not generated-looking, technically sound. What holds it back is content only the owner can supply: a current status and dates, one clear lead project with a real method and result for the snake work, first-person attribution and baselines on aerobraking, and local copies of the resume and images. Until those arrive, further design cycles will repeat this list. Pause the loop or send the owner the five facts.
