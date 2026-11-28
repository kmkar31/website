# Critique, 2026-11-28 (after designer cycle 217)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL; only "images not loaded" sandbox notes; takes about 2.5 minutes). Viewed index phone-light and desktop-light, and snake-robots phone-dark. Read the tail of LOG.md (2,700 lines; not read in full), the previous critique and user-critique.md. `git status` is clean; the last commit (0c02577) is log-only, so no site change and no regressions. Wix images and Google Fonts are blocked in the sandbox (environment limit).

## Sources consulted
WebFetch was blocked again (permission request on https://web.dev/articles/optimize-cls went unanswered; do not retry). I fetched nothing and quote nothing. These are pointers to open, not evidence I read. This is fewer than the three sources the brief asks for. Topic this cycle: CLS and image loading.
- web.dev, Optimize CLS (width and height on images): https://web.dev/articles/optimize-cls (finding 4)
- web.dev, Font best practices: https://web.dev/articles/font-best-practices (finding 6)
- W3C, Understanding SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- NN/g, UX Portfolios: What Hiring Managers Look For: https://www.nngroup.com/videos/ux-portfolios-hiring/

## Scores
- AI-tell: 2/10, unchanged. Ruled list, "For the record" ledger, struck-through "three weeks to 15 minutes", stamps, "Fig. 1" plate, "Sheet N of 9" captions. No gradients, glass, chips, stats strip or card trio. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Paper-and-ink system reads well on phone and desktop (viewed). Desktop Home right column is uneven: rows 01 to 03, 08 and 09 have no mark, while row 06 stacks a stamp, "Start here" and tags. The snake page on phone is sparse because its images do not load here.
- SEO: 7/10, unchanged. Per-page title, description, canonical, og tags, JSON-LD, sitemap, robots and 404 present. Weak: one shared OG card, hotlinked images, robots.txt under a project-site subpath (host limit).
- UX: 6/10, unchanged. Contact, resume and next/previous links are findable. The gaps are owner content.
- Fun and personality: 7/10, unchanged.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat paper, ink borders, hard offset shadows, no blur, both themes).
2. Must not look AI-generated: met, AI-tell 2. File unchanged; no new notes.

## Regression check
No site file changed since the last cycle. No regressions.

## Ranked findings
1. Major (UX, credibility). Home subhead is "MS Mechanical Engineering, Carnegie Mellon University" with no dates or status (viewed, phone and desktop). The ledger "Status" row never renders because `STATUS` is empty in the build script. About says 2023 to 2025 and today is 2026-11-28, so a recruiter cannot tell whether he has graduated or is available. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads, while "Start here" sits on row 06 (aerobraking), about two phone screens down (viewed). Owner picks the lead.
3. Major (content). The snake page is the lead and the thinnest: images, a short "why" and a lab link (viewed, phone-dark). It has no method, result or number, while the blurb says "I implemented". Owner must supply what he did and what happened.
4. Major (robustness, performance). The resume PDF and nearly all project images are hotlinked from Wix (confirmed: snake-robots img tags use static.wixstatic.com, no width or height attributes, so CLS risk on load). The src-less `<img alt="">` is the lightbox viewer, accepted. Owner must supply local copies.
5. Major (credibility). Aerobraking's "46 orbits to target" has no baseline and its Method is third person. Raftar's Ferrari comparison has no source. Owner facts.
6. Minor (consistency, performance). Footer claims "no framework" and names DM Serif Display and Source Serif 4, which load from fonts.googleapis.com (render-blocking third party, external dependency). Self-host WOFF2 with `font-display: swap` once files exist.
7. Minor (UX). Aerobraking is very long on phone with no pull-out of his own part. Add a "My part" box once finding 5 is answered.
8. Minor (visual, taste). Desktop Home right column is uneven (row 06). Previously declined; noted only.
9. Minor (SEO). Shared OG card; Search Console sitemap submission is an owner action.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (content). Quadrotor-sysid leads with general theory instead of the fitted result. Owner fact.
12. Nit (UX). Contact is LinkedIn only in the footer line (GitHub and resume also linked). Owner constraint.
13. Nit (process). Findings 1 to 5 have repeated for 20+ cycles and the last ten or more cycles were log-only. The loop is blocked on owner input, and my web research is blocked, so this critique adds no new external evidence.

## Good, must not regress
- Ruled-list Home with the "For the record" ledger; no card trio, no stats strip.
- Struck-through "three weeks to 15 minutes", the 99 s stamp, "Fig. 1" plate, "Sheet N of 9" captions.
- Flat paper tones, ink borders, hard offset shadows in both themes; no blur or gradient.
- Per-page titles, descriptions, canonical, OG, JSON-LD, sitemap, robots, 404.
- Next/More-on links; sticky header; reduced-motion block; 3px `:focus-visible` outline; theme-color metas.
- About page: dated ledger of education and internships with real numbers.

## Verdict
The design is finished as far as the repo's own material allows: retro, matte, not generated-looking, technically sound. What holds it back is content only the owner can supply: a current status and dates, one lead project with a real method and result for the snake work, first-person attribution and baselines for aerobraking, and local copies of the resume, images and fonts. Until those arrive, further design cycles will repeat this list. Stop the loop or send the owner the facts and files.
