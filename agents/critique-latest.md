# Critique, 2026-11-28 (after designer cycle 218)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL; only "images not loaded" sandbox notes). Viewed index phone-light, index desktop-dark and about tablet-light. Read the tail of LOG.md (about 280 KB; not read in full), the previous critique and user-critique.md. `git status` is clean; the last commit (f0302d2) is log-only, so there is no site change and no regression. Wix images and Google Fonts are blocked in the sandbox (environment limit). I grepped the repo: og:image is the shared assets/og.png, wixstatic appears in 11 of 13 pages (about 30 references), and aerobraking has one h1 and four h2.

## Sources consulted
WebFetch of https://web.dev/articles/optimize-cls was refused again (permission request unanswered; not retried). I read no external source this cycle and quote none. This is fewer than the three the brief asks for, and it is an environment limit, not a choice. These are pointers only:
- web.dev, Optimize CLS (width and height on images): https://web.dev/articles/optimize-cls
- web.dev, Font best practices: https://web.dev/articles/font-best-practices
- NN/g, UX Portfolios: What Hiring Managers Look For: https://www.nngroup.com/videos/ux-portfolios-hiring/

## Scores
- AI-tell: 2/10, unchanged. Ruled list, "For the record" ledger, struck-through "three weeks to 15 minutes", stamps, "Fig. 1" plate, no gradients, glass, chips, stats strip or card trio. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Paper-and-ink system reads well in both themes (viewed). The desktop Home right column is uneven: rows 01 to 03, 08 and 09 carry no mark, while row 06 stacks a stamp and "Start here".
- SEO: 7/10, unchanged. Per-page title, description, canonical, OG, JSON-LD, sitemap, robots and 404 are present. Weak: one shared OG card, hotlinked images, robots.txt under a project-site subpath (host limit).
- UX: 6/10, unchanged. Contact, resume and next/previous links are findable. The gaps are owner content.
- Fun and personality: 7/10, unchanged.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat paper, ink borders, hard offset shadows, no blur, both themes).
2. Must not look AI-generated: met, AI-tell 2. The file is unchanged; there are no new notes.

## Regression check
No site file changed. No regressions.

## Ranked findings
1. Major (UX, credibility). The Home subhead gives "MS Mechanical Engineering, Carnegie Mellon University" with no dates or status (viewed, phone and desktop). The ledger "Status" row never renders because `STATUS` is empty. About says 2023 to 2025 and today is 2026-11-28, so a recruiter cannot tell whether he has graduated or is available. Owner fact needed.
2. Major (UX). There are two answers to "strongest project". Row 01 (snake) leads, while "Start here" sits on row 06 (aerobraking), roughly two phone screens down (viewed). Owner picks the lead.
3. Major (content). The snake page is the lead and the thinnest, with no method, result or number, while the blurb says "I implemented". Owner must supply what he did and what happened.
4. Major (robustness, performance). Nearly all project images are hotlinked from Wix (about 30 references across 11 pages) and have no width or height, which is a CLS and link-rot risk. The src-less `<img alt="">` is the lightbox viewer, accepted. Owner must supply local copies.
5. Major (credibility). Aerobraking's "46 orbits to target" has no baseline, and its Method is third person. Raftar's Ferrari comparison has no source. Owner facts.
6. Minor (consistency, performance). The footer says "no framework" and names DM Serif Display and Source Serif 4, which load from Google Fonts (render-blocking third party). Self-host WOFF2 with `font-display: swap` once files exist.
7. Minor (UX). Aerobraking is very long on phone and has no "My part" box. Add one once finding 5 is answered.
8. Minor (visual, taste). The desktop Home right column is uneven (row 06). Previously declined; noted only.
9. Minor (SEO). Shared OG card; sitemap submission to Search Console is an owner action.
10. Minor (content). The tricycle page voice is passive with no subheads. Owner call.
11. Nit (content). Quadrotor-sysid leads with theory instead of the fitted result. Owner fact.
12. Nit (UX). Contact in the footer line is LinkedIn only (GitHub and resume are also linked). Owner constraint.
13. Nit (process). Findings 1 to 5 have repeated for 20+ cycles and the last ten or more cycles were log-only. The loop is blocked on owner input, and my web research is blocked, so this critique adds no new external evidence.

## Good, must not regress
- Ruled-list Home with the "For the record" ledger; no card trio, no stats strip.
- Struck-through "three weeks to 15 minutes", the 99 s stamp, "Fig. 1" plate, "Sheet N of 9" captions.
- Flat paper tones, ink borders, hard offset shadows in both themes; no blur or gradient.
- Per-page titles, descriptions, canonical, OG, JSON-LD, sitemap, robots, 404.
- Next/More-on links; sticky header; reduced-motion block; 3px `:focus-visible` outline; theme-color metas.
- About page: dated ledger of education and internships with real numbers.

## Verdict
The design is finished as far as the repo's own material allows: retro, matte, not generated-looking and technically sound. What holds it back is content only the owner can supply: a current status and dates, one lead project with a real method and result for the snake work, first-person attribution and baselines for aerobraking, and local copies of the resume, images and fonts. Until those arrive, more design cycles will repeat this list. Stop the loop or send the owner the facts and files.
