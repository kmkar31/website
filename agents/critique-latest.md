# Critique, 2026-11-27 (after designer cycle 210)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL, only "images not loaded" sandbox notes). Viewed index phone-light, index desktop-dark and snake-robots phone-light. Read LOG.md (through cycle 210), user-critique.md (unchanged, two notes from 2026-10-22) and the previous critique. `git status` is clean and cycles 206 to 210 changed no site files, so nothing can have regressed. Wix images and Google Fonts are blocked in the sandbox, so photos are absent and serifs render as fallbacks (environment limit, not a bug).

## Sources consulted
Below the three-source minimum, and I am saying so. Direct fetches of web.dev Optimize CLS and MDN prefers-reduced-motion were refused (permission not answered), and earlier cycles' W3C and NN/g fetches failed too. A WebSearch returned only titles and links, no text I could quote. I quote nothing. Unread pointers:
- https://web.dev/articles/optimize-cls (blocked; relevant to finding 5)
- https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion (blocked; the CSS already has a reduced-motion block at assets/style.css:252)
- https://www.nngroup.com/articles/ux-design-portfolios/ (listed by search, not read)
Topic this cycle: CLS and image dimensions, reduced motion, portfolio credibility.

## Scores
- AI-tell: 2/10, unchanged. Plain ruled list, "For the record" ledger, struck-through "three weeks to 15 minutes", figure stamps and plates. No gradients, glass, chips, stats strip or card trio. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Paper-and-ink system is coherent in both themes (viewed). Desktop-dark Home right column is ragged: rows 01 to 03, 08 and 09 carry no mark and row 06 stacks stamp, "Start here" and tags beside the only thumbnail. The snake page (the lead project) is a text column with one schematic. Of the images, only the aerobraking plate shows on Home.
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, absolute og:image, twitter card, sitemap, robots and JSON-LD on every page except 404 (correct). Weak: one shared OG card; hotlinked images; robots.txt under a project-site subpath is ignored by crawlers (host limit).
- UX: 6/10, unchanged. Contact, resume and next/previous navigation are easy; the gaps need owner content (findings 1 to 5).
- Fun and personality: 7/10, unchanged. The strike-through, "Time allowed: 99 s" stamp and "Start here" tab are the memorable moments.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Flat paper, ink borders, hard offset shadows, no blur, both themes (viewed).
2. Must not look AI-generated: met, AI-tell 2. No new notes in the file.

## Regression check
No site file changed. Screenshots match the last cycle. No regressions.

## Ranked findings
1. Major (UX, credibility). Home subhead is "MS Mechanical Engineering, Carnegie Mellon University" with no dates or status. About says 2023 to 2025 and today is 2026-11-27. A recruiter cannot tell whether he has graduated, what he does now or whether he is available. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads and "Start here" sits on row 06 (aerobraking), about two phone screens down (viewed). Owner picks the lead, moves the label or reorders.
3. Major (content). The snake page, the lead project, is the thinnest (viewed): an illustrative schematic ("Module count is illustrative"), a three-line "Why snake robots" and a lab link. It has no method, result or number for what he implemented, yet the lead blurb says "I implemented". Owner must supply.
4. Major (credibility). Aerobraking's "46 orbits to target" has no baseline and its Method is third person, which hides his own contribution. Raftar's Ferrari comparison has no source. Owner facts.
5. Major (robustness, performance). The resume PDF and nearly all project images are hotlinked from Wix, and many `<img>` tags lack width and height, so there is a CLS risk (general knowledge; the web.dev source was blocked). The resume link appears in four places, so one dead link breaks four entries. Needs assets/resume.pdf and local images. Link liveness is not verifiable offline.
6. Minor (UX). Aerobraking is very long on phone with no pull-out of his own part. Add a two-line "My part" box once finding 4 is answered.
7. Minor (visual, taste). Desktop Home right column is uneven (row 06). Previously declined; noted only.
8. Minor (consistency). The footer says "no framework" and names DM Serif Display and Source Serif 4, but the fonts load from Google Fonts. Accurate; self-host WOFF2 when files exist.
9. Minor (SEO). Shared OG card; sitemap submission in Search Console is an owner action.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only (GitHub and resume also linked). Owner constraint.
12. Nit (process). Findings 1 to 5 have repeated for about 17 cycles and no site change can resolve them; the last five cycles were log-only. Owner should supply facts and files or the loop should pause.

## Good, must not regress
- Ruled-list Home with the "For the record" ledger; no card trio, no stats strip.
- Struck-through "three weeks to 15 minutes", the 99 s stamp, "Fig. 1" plates and "Sheet 1 of 9" captions.
- Flat paper tones, ink borders, hard offset shadows in both themes; no blur or gradient.
- Per-page titles, descriptions, canonical, OG, JSON-LD, sitemap, robots, 404.
- Next/More-on links on project pages; sticky header with scroll-padding; reduced-motion block.

## Verdict
The design is finished as far as the repo's own material allows: it is retro and matte, it does not look generated, and it is technically sound. What holds it back is content only the owner can supply: a current status and dates, one clear lead project with a real method and result for the snake work, first-person attribution and baselines on aerobraking, and local copies of the resume and images. Until those arrive, further design cycles will only repeat this list. Pause the loop or send the owner the five facts.
